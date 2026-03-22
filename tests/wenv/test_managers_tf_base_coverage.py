#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.wenv.managers.tf_base — uncovered branches."""

from __future__ import annotations

import json
import pathlib
from unittest.mock import MagicMock, patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.managers.base import ToolManagerError
from wrknv.wenv.managers.tf_base import TfVersionsManager


class ConcreteTfManager(TfVersionsManager):
    """Minimal concrete subclass for testing."""

    @property
    def tool_name(self) -> str:
        return "terraform"

    @property
    def executable_name(self) -> str:
        return "terraform"

    @property
    def tool_prefix(self) -> str:
        return "terraform"

    def get_available_versions(self) -> list[str]:
        return ["1.6.0", "1.5.7"]

    def get_download_url(self, version: str) -> str:
        return f"https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://releases.hashicorp.com/terraform/{version}/terraform_{version}_SHA256SUMS"


def _make_mgr(tmp: pathlib.Path) -> ConcreteTfManager:
    """Create a manager with all paths redirected to tmp."""
    with (
        patch("pathlib.Path.exists", return_value=False),
        patch("pathlib.Path.mkdir"),
    ):
        mgr = ConcreteTfManager()
    mgr.install_path = tmp / "versions"
    mgr.install_path.mkdir(parents=True, exist_ok=True)
    mgr.metadata_file = tmp / "metadata.json"
    mgr.metadata = {}
    mgr.cache_dir = tmp / "cache"
    mgr.cache_dir.mkdir(parents=True, exist_ok=True)
    mgr.venv_bin_dir = tmp / "bin"
    mgr.venv_bin_dir.mkdir(parents=True, exist_ok=True)
    return mgr


class TestUpdateRecentFileDeletesBranch(FoundationTestCase):
    """Lines 132->133 and 132->137: branches of the elif in _update_recent_file."""

    def test_removes_tool_from_recent_when_no_versions_installed(self) -> None:
        """132->133: no installed versions + key IN recent_data → key deleted."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        # Create RECENT file with an existing entry for this tool
        recent_file = mgr.install_path / "RECENT"
        recent_file.write_text(json.dumps({"terraform": ["1.5.7"]}))

        # get_installed_versions returns empty (no files in install_path)
        with patch.object(mgr, "get_installed_versions", return_value=[]):
            mgr._update_recent_file()

        remaining = json.loads(recent_file.read_text())
        assert "terraform" not in remaining

    def test_skips_elif_when_no_versions_and_key_absent(self) -> None:
        """132->137: no installed versions + key NOT in recent_data → no change."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        # Create RECENT file WITHOUT the terraform key
        recent_file = mgr.install_path / "RECENT"
        recent_file.write_text(json.dumps({"opentofu": ["1.6.0"]}))

        with patch.object(mgr, "get_installed_versions", return_value=[]):
            mgr._update_recent_file()

        remaining = json.loads(recent_file.read_text())
        # opentofu entry preserved; nothing changed
        assert "opentofu" in remaining
        assert "terraform" not in remaining


class TestGetInstalledVersionsNonVersionFile(FoundationTestCase):
    """Line 194->190: file matches prefix but _is_version_dir returns False → skipped."""

    def test_non_version_filename_is_skipped(self) -> None:
        """A file like 'terraform_LOCK' starts with prefix but fails version check."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        # Create a file that starts with "terraform_" but has a non-semver suffix
        (mgr.install_path / "terraform_LOCK").write_text("lock")
        (mgr.install_path / "terraform_1.6.0").write_text("binary")

        versions = mgr.get_installed_versions()

        assert "1.6.0" in versions
        assert "LOCK" not in versions


class TestRemoveVersionNoBinary(FoundationTestCase):
    """Line 263->277: binary_path.exists() is False → skip deletion, still update config."""

    def test_remove_version_skips_unlink_when_binary_missing(self) -> None:
        """If binary is already gone, removal skips unlink but checks config update."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        # No binary file created → binary_path.exists() returns False

        with (
            patch.object(mgr, "get_binary_path", return_value=tmp / "nonexistent_binary"),
            patch.object(mgr, "get_installed_version", return_value="other"),
        ):
            mgr.remove_version("1.6.0")  # Should not raise


class TestInstallFromArchiveLoopSkip(FoundationTestCase):
    """Line 307->306: rglob finds file matching pattern but NOT exact name → loop skip."""

    def test_non_matching_binary_name_triggers_error(self) -> None:
        """File like 'terraform_ui' matches glob but not exact name → ToolManagerError."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        archive = tmp / "terraform_1.6.0.zip"
        archive.write_text("archive")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            dst.mkdir(parents=True, exist_ok=True)
            (dst / "terraform_ui").write_text("ui helper")
            # No "terraform" binary → loop iterates terraform_ui, skips it, raises

        with (
            patch.object(mgr, "extract_archive", side_effect=fake_extract),
            pytest.raises(ToolManagerError, match="terraform binary not found"),
        ):
            mgr._install_from_archive(archive, "1.6.0")


class TestInstallFromArchiveVerifyFails(FoundationTestCase):
    """Line 337: verify_installation returns False → ToolManagerError raised."""

    def test_verification_failure_raises_error(self) -> None:
        """After successful extract and copy, failed verify raises ToolManagerError."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        archive = tmp / "terraform_1.6.0.zip"
        archive.write_text("archive")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            dst.mkdir(parents=True, exist_ok=True)
            (dst / "terraform").write_text("binary")

        with (
            patch.object(mgr, "extract_archive", side_effect=fake_extract),
            patch.object(mgr, "make_executable"),
            patch.object(mgr, "verify_installation", return_value=False),
            patch("shutil.copy2"),
            patch.object(mgr, "_calculate_file_hash", return_value="abc123"),
            patch.object(mgr, "_update_install_metadata"),
            patch.object(mgr, "_update_recent_file"),
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            mgr._install_from_archive(archive, "1.6.0")


class TestSetGlobalVersionBinaryMissing(FoundationTestCase):
    """Line 408: set_global_version when binary doesn't exist → early return."""

    def test_returns_early_when_binary_not_found(self) -> None:
        """If binary path doesn't exist, set_global_version returns without copying."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        with (
            patch("shutil.copy2") as mock_copy,
            patch.object(mgr, "get_binary_path", return_value=tmp / "nonexistent"),
        ):
            mgr.set_global_version("1.6.0")

        mock_copy.assert_not_called()


class TestSetGlobalVersionExistingGlobalKey(FoundationTestCase):
    """Line 430->433: 'global' already in metadata → skip creating the dict."""

    def test_updates_existing_global_entry(self) -> None:
        """When metadata already has 'global', update it without creating new dict."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        binary = tmp / "terraform_1.6.0"
        binary.write_text("#!/bin/sh")
        mgr.metadata = {"global": {"terraform_version": "1.5.7"}}

        with (
            patch.object(mgr, "get_binary_path", return_value=binary),
            patch("shutil.copy2"),
            patch("pathlib.Path.chmod"),
            patch.object(mgr, "_save_metadata"),
        ):
            mgr.set_global_version("1.6.0")

        assert mgr.metadata["global"]["terraform_version"] == "1.6.0"


class TestFindProjectRootNotFound(FoundationTestCase):
    """Lines 518-520: _find_project_root traverses to filesystem root without finding pyproject.toml."""

    def test_returns_none_when_no_pyproject_toml_found(self) -> None:
        """When no pyproject.toml exists anywhere, _find_project_root returns None."""
        mgr = ConcreteTfManager()

        with patch("pathlib.Path.exists", return_value=False):
            result = mgr._find_project_root()

        assert result is None


class TestGetVenvBinDirNotInVenv(FoundationTestCase):
    """Lines 484->497, 498->499/505, 501->502/505: _get_venv_bin_dir outside a venv."""

    def test_not_in_venv_uses_project_root_bin_when_exists(self) -> None:
        """484->497, 498->499, 501->502: not in venv + project root found + bin exists → return it."""
        import sys

        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        project_root = tmp / "project"
        project_root.mkdir()
        workenv_bin = project_root / "workenv" / "bin"
        workenv_bin.mkdir(parents=True)

        mock_config = MagicMock()
        mock_config.get_workenv_dir_name.return_value = "workenv"
        mgr.config = mock_config

        # Simulate not being in a venv by temporarily removing the venv markers
        original_real_prefix = getattr(sys, "real_prefix", None)
        if hasattr(sys, "real_prefix"):
            del sys.real_prefix
        original_base_prefix = sys.base_prefix
        sys.base_prefix = sys.prefix  # make base_prefix == prefix → not in venv

        try:
            with patch.object(mgr, "_find_project_root", return_value=project_root):
                result = mgr._get_venv_bin_dir()
        finally:
            if original_real_prefix is not None:
                sys.real_prefix = original_real_prefix  # type: ignore[attr-defined]
            sys.base_prefix = original_base_prefix

        assert result == workenv_bin

    def test_not_in_venv_falls_back_to_local_bin_when_no_project_root(self) -> None:
        """484->497, 498->505: not in venv + no project root → fall back to ~/.local/bin."""
        import sys

        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        original_real_prefix = getattr(sys, "real_prefix", None)
        if hasattr(sys, "real_prefix"):
            del sys.real_prefix
        original_base_prefix = sys.base_prefix
        sys.base_prefix = sys.prefix

        try:
            with (
                patch.object(mgr, "_find_project_root", return_value=None),
                patch("pathlib.Path.mkdir"),
            ):
                result = mgr._get_venv_bin_dir()
        finally:
            if original_real_prefix is not None:
                sys.real_prefix = original_real_prefix  # type: ignore[attr-defined]
            sys.base_prefix = original_base_prefix

        assert ".local" in str(result) or "local" in str(result)

    def test_not_in_venv_project_root_found_but_bin_missing_falls_back(self) -> None:
        """501->505: not in venv + project root found but bin_dir doesn't exist → .local/bin."""
        import sys

        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        project_root = tmp / "project"
        project_root.mkdir()
        # Do NOT create workenv/bin → bin_dir.exists() returns False

        mock_config = MagicMock()
        mock_config.get_workenv_dir_name.return_value = "workenv"
        mgr.config = mock_config

        original_real_prefix = getattr(sys, "real_prefix", None)
        if hasattr(sys, "real_prefix"):
            del sys.real_prefix
        original_base_prefix = sys.base_prefix
        sys.base_prefix = sys.prefix

        try:
            with (
                patch.object(mgr, "_find_project_root", return_value=project_root),
                patch("pathlib.Path.mkdir"),
            ):
                result = mgr._get_venv_bin_dir()
        finally:
            if original_real_prefix is not None:
                sys.real_prefix = original_real_prefix  # type: ignore[attr-defined]
            sys.base_prefix = original_base_prefix

        assert ".local" in str(result) or "local" in str(result)


class TestCopyActiveBinariesToVenvTofuPath(FoundationTestCase):
    """Lines 542->529, 544->529: tofu iteration with no active version or missing source."""

    def test_no_active_version_skips_copy(self) -> None:
        """Line 542->529: tofu has no active version → inner block skipped."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)

        mock_tofu_mgr = MagicMock()
        mock_tofu_mgr.get_installed_version.return_value = None  # 542->529

        # Managers are imported lazily with "from .tofu import TofuManager"
        with (
            patch("wrknv.wenv.managers.tofu.TofuManager", return_value=mock_tofu_mgr),
            patch("shutil.copy2") as mock_copy,
        ):
            # Only "tofu" iteration runs successfully; "terraform" raises ImportError (caught)
            mgr._copy_active_binaries_to_venv()

        mock_copy.assert_not_called()

    def test_source_binary_missing_skips_copy(self) -> None:
        """Line 544->529: source path doesn't exist → copy skipped."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        non_existent = tmp / "nonexistent_tofu_binary"

        mock_tofu_mgr = MagicMock()
        mock_tofu_mgr.get_installed_version.return_value = "1.6.0"
        mock_tofu_mgr.get_binary_path.return_value = non_existent  # 544->529

        with (
            patch("wrknv.wenv.managers.tofu.TofuManager", return_value=mock_tofu_mgr),
            patch("shutil.copy2") as mock_copy,
        ):
            mgr._copy_active_binaries_to_venv()

        mock_copy.assert_not_called()


# 🧰🌍🔚
