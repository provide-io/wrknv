#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.base module."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import BaseToolManager, ToolManagerError


class FakeToolManager(BaseToolManager):
    """Concrete subclass for testing BaseToolManager."""

    @property
    def tool_name(self) -> str:
        return "faketool"

    @property
    def executable_name(self) -> str:
        return "faketool"

    def get_available_versions(self) -> list[str]:
        return ["2.0.0", "1.1.0", "1.0.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://fake.example.com/faketool/{version}/faketool.tar.gz"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://fake.example.com/faketool/{version}/checksums.txt"

    def _install_from_archive(self, archive_path: pathlib.Path, version: str) -> None:
        pass


def _make_manager(tmp_dir: pathlib.Path) -> FakeToolManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: {
        "install_path": str(tmp_dir / "tools"),
    }.get(key, default)
    cfg.get_tool_version.return_value = None
    return FakeToolManager(config=cfg)


class TestBaseToolManagerInit(FoundationTestCase):
    """Tests for BaseToolManager.__init__."""

    def test_stores_config(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.config is not None

    def test_creates_install_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.install_path.exists()

    def test_creates_cache_dir(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.cache_dir.exists()

    def test_cache_dir_is_sibling_of_tools(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.cache_dir == manager.install_path.parent / "cache"


class TestGetPlatformInfo(FoundationTestCase):
    """Tests for get_platform_info."""

    def test_returns_dict(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        fake_info = {"os": "linux", "arch": "amd64"}
        with mock.patch("wrknv.wenv.operations.platform.get_platform_info", return_value=fake_info):
            result = manager.get_platform_info()
        assert result == fake_info


class TestGetInstalledVersion(FoundationTestCase):
    """Tests for get_installed_version."""

    def test_returns_version_from_config(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "1.2.3"
        assert manager.get_installed_version() == "1.2.3"

    def test_returns_none_when_not_installed(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = None
        assert manager.get_installed_version() is None


class TestSetInstalledVersion(FoundationTestCase):
    """Tests for set_installed_version."""

    def test_no_error_on_base_call(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.set_installed_version("1.0.0")  # should not raise


class TestGetBinaryPath(FoundationTestCase):
    """Tests for get_binary_path."""

    def test_returns_correct_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("platform.system", return_value="Linux"):
            result = manager.get_binary_path("1.0.0")
        assert result == manager.install_path / "faketool" / "1.0.0" / "bin" / "faketool"

    def test_adds_exe_on_windows(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("platform.system", return_value="Windows"):
            result = manager.get_binary_path("1.0.0")
        assert result.name == "faketool.exe"


class TestGetCurrentBinaryPath(FoundationTestCase):
    """Tests for get_current_binary_path."""

    def test_returns_none_when_no_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = None
        assert manager.get_current_binary_path() is None

    def test_returns_binary_path_when_version_set(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "2.0.0"
        result = manager.get_current_binary_path()
        assert result is not None
        assert "2.0.0" in str(result)


class TestCreateSymlink(FoundationTestCase):
    """Tests for create_symlink."""

    def test_skips_when_binary_not_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        # Binary doesn't exist - should not raise
        manager.create_symlink("1.0.0")

    def test_creates_symlink_when_binary_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        # Create the binary
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        manager.create_symlink("1.0.0")
        symlink = manager.install_path / "bin" / "faketool"
        assert symlink.exists() or symlink.is_symlink()

    def test_replaces_existing_symlink(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        bin_dir = manager.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)
        symlink = bin_dir / "faketool"
        symlink.write_text("old")
        manager.create_symlink("1.0.0")
        # Should not raise

    def test_handles_oserror_gracefully(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with mock.patch("pathlib.Path.symlink_to", side_effect=OSError("permission denied")):
            manager.create_symlink("1.0.0")  # Should not raise


class TestDownloadFile(FoundationTestCase):
    """Tests for download_file."""

    def test_delegates_to_download_file(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.wenv.operations.download.download_file") as mock_dl:
            manager.download_file("https://example.com/file.tar.gz", tmp / "file.tar.gz")
        mock_dl.assert_called_once()


class TestVerifyChecksum(FoundationTestCase):
    """Tests for verify_checksum."""

    def test_returns_true_when_disabled(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "install_path": str(tmp / "tools"),
            "verify_checksums": False,
        }.get(key, default)
        result = manager.verify_checksum(tmp / "file", "abc123")
        assert result is True

    def test_delegates_when_enabled(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "install_path": str(tmp / "tools"),
            "verify_checksums": True,
        }.get(key, default)
        with mock.patch("wrknv.wenv.operations.download.verify_checksum", return_value=True) as mock_vc:
            result = manager.verify_checksum(tmp / "file", "abc123")
        mock_vc.assert_called_once()
        assert result is True


class TestExtractArchive(FoundationTestCase):
    """Tests for extract_archive."""

    def test_delegates_to_extract_archive(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.wenv.operations.install.extract_archive") as mock_ea:
            manager.extract_archive(tmp / "archive.tar.gz", tmp / "out")
        mock_ea.assert_called_once()


class TestMakeExecutable(FoundationTestCase):
    """Tests for make_executable."""

    def test_delegates_to_make_executable(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.wenv.operations.install.make_executable") as mock_me:
            manager.make_executable(tmp / "binary")
        mock_me.assert_called_once()


class TestInstallVersion(FoundationTestCase):
    """Tests for install_version."""

    def test_dry_run_does_not_install(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager, "download_file") as mock_dl:
            manager.install_version("1.0.0", dry_run=True)
        mock_dl.assert_not_called()

    def test_skips_if_already_installed(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        # Create the binary so it looks installed
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "install_path": str(tmp / "tools"),
            "create_symlinks": False,
        }.get(key, default)
        with mock.patch.object(manager, "download_file") as mock_dl:
            manager.install_version("1.0.0")
        mock_dl.assert_not_called()

    def test_raises_tool_manager_error_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "install_path": str(tmp / "tools"),
            "clean_on_failure": False,
            "cache_downloads": False,
            "verify_checksums": False,
            "create_symlinks": False,
        }.get(key, default)
        with (
            mock.patch.object(manager, "download_file", side_effect=RuntimeError("network error")),
            pytest.raises(ToolManagerError, match="Failed to install"),
        ):
            manager.install_version("1.0.0")

    def test_cleans_up_on_failure_when_configured(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "install_path": str(tmp / "tools"),
            "clean_on_failure": True,
            "cache_downloads": False,
            "verify_checksums": False,
            "create_symlinks": False,
        }.get(key, default)
        with (
            mock.patch.object(manager, "download_file", side_effect=RuntimeError("fail")),
            mock.patch.object(manager, "_cleanup_failed_installation") as mock_cleanup,
            pytest.raises(ToolManagerError),
        ):
            manager.install_version("1.0.0")
        mock_cleanup.assert_called_once_with("1.0.0")


# 🧰🌍🔚
