#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.base module (TfManager) - install and lifecycle operations."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.tf.base import TfManager
from wrknv.managers.tf.metadata import TfMetadataManager


class FakeTfManager(TfManager):
    """Concrete subclass of TfManager for testing."""

    @property
    def tool_name(self) -> str:
        return "ibmtf"

    @property
    def executable_name(self) -> str:
        return "ibmtf"

    @property
    def tool_prefix(self) -> str:
        return "terraform"

    def get_available_versions(self) -> list[str]:
        return ["1.7.0", "1.6.0", "1.5.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/terraform/{version}/terraform.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://example.com/terraform/{version}/SHA256SUMS"

    def verify_installation(self, version: str) -> bool:
        return True


def _make_manager(tmp_dir: pathlib.Path) -> FakeTfManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: {
        "install_path": str(tmp_dir / "tools"),
    }.get(key, default)
    cfg.get_tool_version.return_value = None

    tf_versions_dir = tmp_dir / ".terraform.versions"
    tf_versions_dir.mkdir(parents=True, exist_ok=True)

    with (
        mock.patch("wrknv.managers.tf.base.get_workenv_bin_dir", return_value=tmp_dir / "bin"),
        mock.patch.object(TfMetadataManager, "load_metadata"),
        mock.patch(
            "wrknv.managers.tf.base.pathlib.Path.expanduser",
            return_value=tf_versions_dir,
        ),
    ):
        manager = FakeTfManager(config=cfg)
        manager.install_path = tf_versions_dir
        manager.metadata = manager.metadata_manager.metadata
    return manager


class TestRemoveVersion(FoundationTestCase):
    """Tests for TfManager.remove_version."""

    def test_removes_binary_when_present(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        manager.remove_version("1.7.0")
        assert not binary_path.exists()

    def test_no_error_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.remove_version("9.9.9")  # Should not raise

    def test_removes_version_from_metadata(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        manager.metadata = {"terraform_1.7.0": {"version": "1.7.0"}}
        with mock.patch.object(manager.metadata_manager, "save_metadata"):
            manager.remove_version("1.7.0")
        assert "terraform_1.7.0" not in manager.metadata

    def test_calls_update_recent_file_after_removal(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        manager.metadata = {}
        with (
            mock.patch.object(manager, "_update_recent_file") as mock_recent,
            mock.patch.object(manager.metadata_manager, "save_metadata"),
        ):
            manager.remove_version("1.7.0")
        mock_recent.assert_called_once()


class TestCreateSymlink(FoundationTestCase):
    """Tests for TfManager.create_symlink."""

    def test_skips_when_binary_not_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        # Should not raise
        manager.create_symlink("1.7.0")

    def test_calls_set_installed_version_when_binary_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        with (
            mock.patch.object(manager, "set_installed_version") as mock_siv,
            mock.patch.object(manager, "_copy_active_binaries_to_venv"),
        ):
            manager.create_symlink("1.7.0")
        mock_siv.assert_called_once_with("1.7.0")

    def test_copies_binaries_to_venv(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        with (
            mock.patch.object(manager, "set_installed_version"),
            mock.patch.object(manager, "_copy_active_binaries_to_venv") as mock_copy,
        ):
            manager.create_symlink("1.7.0")
        mock_copy.assert_called_once()


class TestSwitchVersion(FoundationTestCase):
    """Tests for TfManager.switch_version."""

    def test_dry_run_does_not_install(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager, "install_version") as mock_install:
            manager.switch_version("1.7.0", dry_run=True)
        mock_install.assert_not_called()

    def test_dry_run_does_not_call_create_symlink(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager, "create_symlink") as mock_cs:
            manager.switch_version("1.7.0", dry_run=True)
        mock_cs.assert_not_called()

    def test_installs_if_binary_not_present(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch.object(manager, "install_version") as mock_install,
            mock.patch.object(manager, "create_symlink"),
        ):
            manager.switch_version("1.7.0")
        mock_install.assert_called_once_with("1.7.0", dry_run=False)

    def test_skips_install_when_binary_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        with (
            mock.patch.object(manager, "install_version") as mock_install,
            mock.patch.object(manager, "create_symlink"),
        ):
            manager.switch_version("1.7.0")
        mock_install.assert_not_called()

    def test_calls_create_symlink(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        with mock.patch.object(manager, "create_symlink") as mock_cs:
            manager.switch_version("1.7.0")
        mock_cs.assert_called_once_with("1.7.0")

    def test_regenerates_env_script_when_project_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        (tmp / "pyproject.toml").write_text("[tool.wrknv]")
        with (
            mock.patch.object(manager, "create_symlink"),
            mock.patch("wrknv.managers.tf.base.pathlib.Path.cwd", return_value=tmp),
            mock.patch("wrknv.wenv.env_generator.create_project_env_scripts") as mock_regen,
        ):
            manager.switch_version("1.7.0")
        mock_regen.assert_called_once_with(tmp)

    def test_does_not_raise_on_env_regen_failure(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        (tmp / "pyproject.toml").write_text("[tool.wrknv]")
        with (
            mock.patch.object(manager, "create_symlink"),
            mock.patch("wrknv.managers.tf.base.pathlib.Path.cwd", return_value=tmp),
            mock.patch(
                "wrknv.wenv.env_generator.create_project_env_scripts",
                side_effect=RuntimeError("regen failed"),
            ),
        ):
            manager.switch_version("1.7.0")  # Should not raise


class TestInstallFromArchive(FoundationTestCase):
    """Tests for TfManager._install_from_archive."""

    def test_raises_when_binary_not_in_archive(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "terraform.zip"
        archive_path.write_text("fake zip")
        extract_dir = manager.cache_dir / "terraform_1.7.0_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)

        with (
            mock.patch.object(manager, "extract_archive"),
            pytest.raises(ToolManagerError, match="binary not found in archive"),
        ):
            manager._install_from_archive(archive_path, "1.7.0")

    def test_installs_binary_from_archive(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)

        # Create fake archive binary
        extract_dir = manager.cache_dir / "terraform_1.7.0_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        fake_binary = extract_dir / "terraform"
        fake_binary.write_text("fake terraform binary")
        archive_path = tmp / "terraform.zip"
        archive_path.write_text("fake archive")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            # Binary is already in place (simulating extraction)
            pass

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch.object(manager, "make_executable"),
            mock.patch.object(manager, "_update_install_metadata"),
            mock.patch.object(manager, "_update_recent_file"),
            mock.patch.object(manager, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.tf.base.safe_copy"),
            mock.patch("wrknv.managers.tf.base.calculate_file_hash", return_value="abc123"),
        ):
            manager._install_from_archive(archive_path, "1.7.0")


class TestSaveMetadata(FoundationTestCase):
    """Tests for TfManager._save_metadata."""

    def test_delegates_to_metadata_manager(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager.metadata_manager, "save_metadata") as mock_save:
            manager._save_metadata()
        mock_save.assert_called_once()


class TestUpdateRecentFile(FoundationTestCase):
    """Tests for TfManager._update_recent_file."""

    def test_delegates_to_metadata_manager(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager.metadata_manager, "update_recent_file") as mock_update:
            manager._update_recent_file()
        mock_update.assert_called_once()


class TestUpdateRecentFileWithActive(FoundationTestCase):
    """Tests for TfManager._update_recent_file_with_active."""

    def test_delegates_to_metadata_manager(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager.metadata_manager, "update_recent_file_with_active") as mock_update:
            manager._update_recent_file_with_active("1.7.0")
        mock_update.assert_called_once()


# 🧰🌍🔚
