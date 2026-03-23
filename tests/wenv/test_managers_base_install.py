#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for BaseToolManager install, network, checksum, and removal operations."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock, patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.wenv.managers.base import BaseToolManager, ToolManagerError


class ConcreteToolManager(BaseToolManager):
    """Concrete implementation for testing."""

    @property
    def tool_name(self) -> str:
        return "testtool"

    @property
    def executable_name(self) -> str:
        return "testtool"

    def get_available_versions(self) -> list[str]:
        return ["2.0.0", "1.1.0", "1.0.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/testtool/{version}/testtool.tar.gz"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://example.com/testtool/{version}/checksums.txt"

    def _install_from_archive(self, archive_path: Path, version: str) -> None:
        version_dir = self.install_path / self.tool_name / version / "bin"
        version_dir.mkdir(parents=True, exist_ok=True)
        binary = version_dir / self.executable_name
        binary.touch()
        binary.chmod(0o755)


class TestFetchJsonSecure(FoundationTestCase):
    """Tests for fetch_json_secure."""

    def test_raises_on_non_https_url(self) -> None:
        manager = ConcreteToolManager()
        with pytest.raises(ToolManagerError, match="Only HTTPS URLs are allowed"):
            manager.fetch_json_secure("http://example.com/api.json")

    def test_raises_on_ftp_url(self) -> None:
        manager = ConcreteToolManager()
        with pytest.raises(ToolManagerError, match="Only HTTPS URLs are allowed"):
            manager.fetch_json_secure("ftp://example.com/api.json")

    def test_fetches_https_url(self) -> None:
        manager = ConcreteToolManager()
        mock_response = Mock()
        mock_response.read.return_value = b'{"key": "value"}'
        mock_response.__enter__ = Mock(return_value=mock_response)
        mock_response.__exit__ = Mock(return_value=False)
        with patch("wrknv.wenv.managers.base.urlopen", return_value=mock_response):
            result = manager.fetch_json_secure("https://example.com/api.json")
        assert result == {"key": "value"}


class TestCreateSymlink(FoundationTestCase):
    """Tests for create_symlink."""

    def test_skips_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.side_effect = lambda k, d=None: str(tmp / "tools") if k == "install_path" else d
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        manager.create_symlink("1.0.0")

    def test_creates_symlink_when_binary_exists(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.side_effect = lambda k, d=None: str(tmp / "tools") if k == "install_path" else d
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        manager.create_symlink("1.0.0")
        symlink = manager.install_path / "bin" / "testtool"
        assert symlink.exists() or symlink.is_symlink()

    def test_removes_existing_symlink_before_recreating(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.side_effect = lambda k, d=None: str(tmp / "tools") if k == "install_path" else d
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        manager.create_symlink("1.0.0")
        manager.create_symlink("1.0.0")


class TestVerifyChecksum(FoundationTestCase):
    """Tests for verify_checksum."""

    def test_skips_when_disabled(self) -> None:
        manager = ConcreteToolManager()
        manager.config = Mock(spec=WorkenvConfig)
        manager.config.get_setting.return_value = False
        result = manager.verify_checksum(Path("/tmp/file"), "abc123")
        assert result is True


class TestExtractArchive(FoundationTestCase):
    """Tests for extract_archive."""

    def test_delegates_to_operations(self) -> None:
        manager = ConcreteToolManager()
        with patch("wrknv.wenv.operations.install.extract_archive") as mock_ext:
            manager.extract_archive(Path("/tmp/archive.tar.gz"), Path("/tmp/out"))
        assert mock_ext.called


class TestMakeExecutable(FoundationTestCase):
    """Tests for make_executable."""

    def test_delegates_to_operations(self) -> None:
        manager = ConcreteToolManager()
        with patch("wrknv.wenv.operations.install.make_executable") as mock_me:
            manager.make_executable(Path("/tmp/binary"))
        assert mock_me.called


class TestInstallVersion(FoundationTestCase):
    """Tests for install_version."""

    def test_dry_run_does_nothing(self) -> None:
        manager = ConcreteToolManager()
        with patch.object(manager, "get_download_url") as mock_dl:
            manager.install_version("1.0.0", dry_run=True)
        mock_dl.assert_not_called()

    def test_skips_download_when_already_installed(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        cfg.get_command_option = Mock(return_value=False)
        manager = ConcreteToolManager(config=cfg)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with patch.object(manager, "download_file") as mock_dl:
            manager.install_version("1.0.0")
        mock_dl.assert_not_called()

    def test_uses_cache_when_available(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.side_effect = lambda k, d=None: {
            "install_path": str(tmp / "tools"),
            "cache_downloads": True,
            "verify_checksums": False,
        }.get(k, d)
        cfg.get_tool_version.return_value = None
        cfg.get_command_option = Mock(return_value=False)
        manager = ConcreteToolManager(config=cfg)
        download_path = manager.cache_dir / "testtool.tar.gz"
        download_path.write_bytes(b"cached")
        with (
            patch.object(manager, "download_file") as mock_dl,
            patch.object(manager, "_install_from_archive"),
            patch.object(manager, "set_installed_version"),
        ):
            manager.install_version("1.0.0")
        mock_dl.assert_not_called()

    def test_raises_on_download_failure(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.side_effect = lambda k, d=None: {
            "install_path": str(tmp / "tools"),
            "cache_downloads": False,
            "clean_on_failure": False,
        }.get(k, d)
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        with (
            patch.object(manager, "download_file", side_effect=RuntimeError("network error")),
            pytest.raises(ToolManagerError, match="Failed to install"),
        ):
            manager.install_version("1.0.0")

    def test_cleanup_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.side_effect = lambda k, d=None: {
            "install_path": str(tmp / "tools"),
            "cache_downloads": False,
            "clean_on_failure": True,
        }.get(k, d)
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        with (
            patch.object(manager, "download_file", side_effect=RuntimeError("net error")),
            patch.object(manager, "_cleanup_failed_installation") as mock_cleanup,
            pytest.raises(ToolManagerError),
        ):
            manager.install_version("1.0.0")
        mock_cleanup.assert_called_once_with("1.0.0")


class TestVerifyDownloadChecksum(FoundationTestCase):
    """Tests for _verify_download_checksum."""

    def test_parses_and_verifies_checksum(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        download_path = tmp / "testtool.tar.gz"
        download_path.write_bytes(b"archive data")
        checksum_file = manager.cache_dir / "checksums.txt"
        checksum_file.write_text("abc123  testtool.tar.gz\n")
        with (
            patch.object(manager, "download_file"),
            patch.object(manager, "verify_checksum", return_value=True) as mock_vc,
        ):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")
        mock_vc.assert_called_once()

    def test_raises_when_checksum_mismatch(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        download_path = tmp / "testtool.tar.gz"
        download_path.write_bytes(b"archive data")
        checksum_file = manager.cache_dir / "checksums.txt"
        checksum_file.write_text("wronghash  testtool.tar.gz\n")
        with (
            patch.object(manager, "download_file"),
            patch.object(manager, "verify_checksum", return_value=False),
            pytest.raises(ToolManagerError, match="Checksum verification failed"),
        ):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")

    def test_logs_warning_when_no_checksum_found(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        download_path = tmp / "testtool.tar.gz"
        download_path.write_bytes(b"data")
        checksum_file = manager.cache_dir / "checksums.txt"
        checksum_file.write_text("abc123  other_file.tar.gz\n")
        with patch.object(manager, "download_file"):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")


class TestCleanupFailedInstallation(FoundationTestCase):
    """Tests for _cleanup_failed_installation."""

    def test_removes_version_dir_when_exists(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        tool_dir = manager.install_path / "testtool" / "1.0.0"
        tool_dir.mkdir(parents=True)
        manager._cleanup_failed_installation("1.0.0")
        assert not tool_dir.exists()

    def test_no_error_when_dir_missing(self) -> None:
        manager = ConcreteToolManager()
        manager._cleanup_failed_installation("9.9.9")


class TestInstallLatest(FoundationTestCase):
    """Tests for install_latest."""

    def test_installs_first_version(self) -> None:
        manager = ConcreteToolManager()
        with patch.object(manager, "install_version") as mock_iv:
            manager.install_latest()
        mock_iv.assert_called_once_with("2.0.0", dry_run=False)

    def test_raises_when_no_versions_available(self) -> None:
        manager = ConcreteToolManager()
        with (
            patch.object(manager, "get_available_versions", return_value=[]),
            pytest.raises(ToolManagerError, match="No versions available"),
        ):
            manager.install_latest()


class TestListVersionsExtra(FoundationTestCase):
    """Additional list_versions tests for branch coverage."""

    @patch("wrknv.wenv.managers.base.pout")
    @patch.object(ConcreteToolManager, "get_installed_version", return_value=None)
    def test_list_versions_shows_more_when_over_limit(self, mock_ver: Mock, mock_pout: Mock) -> None:
        manager = ConcreteToolManager()
        manager.list_versions(limit=1)
        calls = [str(c) for c in mock_pout.call_args_list]
        assert any("more" in c for c in calls)


class TestShowCurrentExtra(FoundationTestCase):
    """show_current branch: version set but binary missing."""

    @patch("wrknv.wenv.managers.base.pout")
    @patch.object(ConcreteToolManager, "get_current_binary_path")
    @patch.object(ConcreteToolManager, "get_installed_version", return_value="1.0.0")
    def test_show_current_binary_missing(
        self, mock_ver: Mock, mock_binary: Mock, mock_pout: Mock, tmp_path: Path
    ) -> None:
        nonexistent = tmp_path / "nonexistent"
        mock_binary.return_value = nonexistent
        manager = ConcreteToolManager()
        manager.show_current()
        output = mock_pout.call_args[0][0]
        assert "binary missing" in output


class TestRemoveVersion(FoundationTestCase):
    """Tests for remove_version."""

    def test_removes_version_directory(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        version_dir = manager.install_path / "testtool" / "1.0.0"
        version_dir.mkdir(parents=True)
        manager.remove_version("1.0.0")
        assert not version_dir.exists()

    def test_clears_config_when_removing_current_version(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = "1.0.0"
        manager = ConcreteToolManager(config=cfg)
        manager.remove_version("1.0.0")
        cfg.set_tool_version.assert_called_once_with("testtool", "")

    def test_no_error_when_version_dir_missing(self) -> None:
        manager = ConcreteToolManager()
        manager.remove_version("9.9.9")


class TestVerifyInstallation(FoundationTestCase):
    """Tests for verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        manager = ConcreteToolManager()
        assert manager.verify_installation("9.9.9") is False

    def test_returns_true_on_success(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = Mock()
        mock_result.returncode = 0
        with patch("wrknv.wenv.managers.base.process_run", return_value=mock_result):
            assert manager.verify_installation("1.0.0") is True

    def test_returns_false_on_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = Mock()
        mock_result.returncode = 1
        with patch("wrknv.wenv.managers.base.process_run", return_value=mock_result):
            assert manager.verify_installation("1.0.0") is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        cfg = Mock(spec=WorkenvConfig)
        cfg.get_setting.return_value = str(tmp / "tools")
        cfg.get_tool_version.return_value = None
        manager = ConcreteToolManager(config=cfg)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with patch("wrknv.wenv.managers.base.process_run", side_effect=RuntimeError("crash")):
            assert manager.verify_installation("1.0.0") is False


# 🧰🌍🔚
