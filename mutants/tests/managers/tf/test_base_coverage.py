#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for managers.tf.base - uncovered branches."""

from __future__ import annotations

import os
import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.tf.base import TfManager
from wrknv.managers.tf.metadata import TfMetadataManager


class FakeTfManager(TfManager):
    """Concrete subclass for testing."""

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
        return ["1.7.0", "1.6.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/terraform/{version}/terraform.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return None

    def verify_installation(self, version: str) -> bool:
        return True


class FakeTofuManager(TfManager):
    """Concrete subclass with tool_name == 'tofu' for testing."""

    @property
    def tool_name(self) -> str:
        return "tofu"

    @property
    def executable_name(self) -> str:
        return "tofu"

    @property
    def tool_prefix(self) -> str:
        return "tofu"

    def get_available_versions(self) -> list[str]:
        return ["1.7.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/tofu/{version}/tofu.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return None

    def verify_installation(self, version: str) -> bool:
        return True


class FakeCustomManager(TfManager):
    """Concrete subclass with tool_name not 'tofu' or 'ibmtf' — exercises else branch."""

    @property
    def tool_name(self) -> str:
        return "faketool"

    @property
    def executable_name(self) -> str:
        return "faketool"

    @property
    def tool_prefix(self) -> str:
        return "faketool"

    def get_available_versions(self) -> list[str]:
        return ["1.0.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/faketool/{version}/faketool.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return None

    def verify_installation(self, version: str) -> bool:
        return True


def _make_manager(tmp_dir: pathlib.Path, manager_cls: type = FakeTfManager) -> TfManager:
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
        manager = manager_cls(config=cfg)
        manager.install_path = tf_versions_dir
        manager.metadata = manager.metadata_manager.metadata
    return manager


class TestRemoveVersionExceptionHandler(FoundationTestCase):
    """Cover exception handler in remove_version (lines 160-162)."""

    def test_config_error_is_swallowed(self) -> None:
        """Lines 160-162: exception from set_tool_version is caught and logged."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version = "1.7.0"
        # get_installed_version must return version to enter the try block
        with (
            mock.patch.object(manager, "get_installed_version", return_value=version),
            mock.patch.object(manager.config, "set_tool_version", side_effect=Exception("DB error")),
        ):
            # Should not raise
            manager.remove_version(version)


class TestInstallFromArchiveBranches(FoundationTestCase):
    """Cover _install_from_archive branches (lines 178, 182, 186->185, 218)."""

    def test_tofu_uses_tofu_binary_name(self) -> None:
        """Line 178: tool_name == 'tofu' sets archive_binary_name = 'tofu'."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, FakeTofuManager)
        version = "1.7.0"

        # Create a fake archive with a 'tofu' binary
        extract_dir = manager.cache_dir / f"tofu_{version}_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        fake_binary = extract_dir / "tofu"
        fake_binary.write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive"),
            mock.patch("wrknv.managers.tf.base.safe_copy"),
            mock.patch.object(manager, "make_executable"),
            mock.patch("wrknv.managers.tf.base.calculate_file_hash", return_value="abc123"),
            mock.patch.object(manager, "_update_install_metadata"),
            mock.patch.object(manager, "_update_recent_file"),
            mock.patch.object(manager, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.tf.base.safe_rmtree"),
            mock.patch(
                "wrknv.managers.tf.base.pathlib.Path.rglob",
                return_value=iter([fake_binary]),
            ),
        ):
            manager._install_from_archive(tmp / "archive.zip", version)

    def test_else_branch_uses_executable_name(self) -> None:
        """Line 182: else branch sets archive_binary_name = self.executable_name."""
        tmp = self.create_temp_dir()
        # FakeCustomManager has tool_name="faketool" → hits else branch (not tofu, not ibmtf)
        manager = _make_manager(tmp, FakeCustomManager)
        version = "1.0.0"

        extract_dir = manager.cache_dir / f"faketool_{version}_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        fake_binary = extract_dir / "faketool"
        fake_binary.write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive"),
            mock.patch("wrknv.managers.tf.base.safe_copy"),
            mock.patch.object(manager, "make_executable"),
            mock.patch("wrknv.managers.tf.base.calculate_file_hash", return_value="abc123"),
            mock.patch.object(manager, "_update_install_metadata"),
            mock.patch.object(manager, "_update_recent_file"),
            mock.patch.object(manager, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.tf.base.safe_rmtree"),
            mock.patch(
                "wrknv.managers.tf.base.pathlib.Path.rglob",
                return_value=iter([fake_binary]),
            ),
        ):
            manager._install_from_archive(tmp / "archive.zip", version)

    def test_binary_not_found_raises(self) -> None:
        """Lines 186->185, 193-196: binary not found in archive raises ToolManagerError."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version = "1.7.0"

        with (
            mock.patch.object(manager, "extract_archive"),
            mock.patch("wrknv.managers.tf.base.safe_rmtree"),
            mock.patch("wrknv.managers.tf.base.pathlib.Path.rglob", return_value=iter([])),
            pytest.raises(ToolManagerError, match="binary not found in archive"),
        ):
            manager._install_from_archive(tmp / "archive.zip", version)

    def test_verify_installation_fails_raises(self) -> None:
        """Line 218: verify_installation returns False → ToolManagerError."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version = "1.7.0"

        extract_dir = manager.cache_dir / f"terraform_{version}_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        fake_binary = extract_dir / "terraform"
        fake_binary.write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive"),
            mock.patch("wrknv.managers.tf.base.safe_copy"),
            mock.patch.object(manager, "make_executable"),
            mock.patch("wrknv.managers.tf.base.calculate_file_hash", return_value="abc123"),
            mock.patch.object(manager, "_update_install_metadata"),
            mock.patch.object(manager, "_update_recent_file"),
            mock.patch.object(manager, "verify_installation", return_value=False),
            mock.patch("wrknv.managers.tf.base.safe_rmtree"),
            mock.patch(
                "wrknv.managers.tf.base.pathlib.Path.rglob",
                return_value=iter([fake_binary]),
            ),
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            manager._install_from_archive(tmp / "archive.zip", version)


class TestUpdateInstallMetadata(FoundationTestCase):
    """Cover _update_install_metadata method (lines 226-262)."""

    def test_updates_metadata_dict(self) -> None:
        """Lines 226-262: metadata dict is populated and saved."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version = "1.7.0"
        archive_path = tmp / "archive.zip"
        archive_path.write_bytes(b"fake")
        binary = manager.get_binary_path(version)
        binary.parent.mkdir(parents=True, exist_ok=True)
        binary.write_bytes(b"binary")

        with mock.patch.object(manager, "_save_metadata") as mock_save:
            manager._update_install_metadata(version, archive_path, "abc123sha256")

        assert f"terraform_{version}" in manager.metadata
        assert manager.metadata[f"terraform_{version}"]["binary_sha256"] == "abc123sha256"
        mock_save.assert_called_once()


class TestSetGlobalVersionBranches(FoundationTestCase):
    """Cover set_global_version branches (lines 299, 307->311, 311->314)."""

    def test_windows_adds_exe_suffix(self) -> None:
        """Line 299: os.name == 'nt' appends .exe to target_name."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version = "1.7.0"
        binary = manager.get_binary_path(version)
        binary.parent.mkdir(parents=True, exist_ok=True)
        binary.write_bytes(b"binary")

        fake_os = mock.MagicMock()
        fake_os.name = "nt"
        with (
            mock.patch("wrknv.managers.tf.base.os", fake_os),
            mock.patch("wrknv.managers.tf.base.safe_copy"),
            mock.patch.object(manager, "_save_metadata"),
        ):
            manager.set_global_version(version)

        assert manager.metadata.get("global", {}).get("ibmtf_version") == version

    def test_global_key_already_exists(self) -> None:
        """Line 311->314: 'global' already in metadata skips initialization."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata["global"] = {"existing_key": "val"}
        version = "1.7.0"
        binary = manager.get_binary_path(version)
        binary.parent.mkdir(parents=True, exist_ok=True)
        binary.write_bytes(b"binary")

        with (
            mock.patch("wrknv.managers.tf.base.safe_copy"),
            mock.patch.object(manager, "_save_metadata"),
        ):
            if os.name != "nt":
                with mock.patch("pathlib.Path.chmod"):
                    manager.set_global_version(version)
            else:
                manager.set_global_version(version)

        assert manager.metadata["global"]["existing_key"] == "val"
        assert manager.metadata["global"]["ibmtf_version"] == version


class TestCopyActiveBinaries(FoundationTestCase):
    """Cover _copy_active_binaries_to_venv (line 364)."""

    def test_delegates_to_copy_tf_binaries(self) -> None:
        """Line 364: delegates to copy_tf_binaries_to_workenv."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.managers.tf.base.copy_tf_binaries_to_workenv") as mock_copy:
            manager._copy_active_binaries_to_venv()
        mock_copy.assert_called_once_with(manager.workenv_bin_dir, manager.config)


# 🧰🌍🔚
