#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.managers.go module."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock, patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.wenv.managers.base import ToolManagerError
from wrknv.wenv.managers.go import GoManager


class TestGoManagerProperties(FoundationTestCase):
    """Test Go manager basic properties."""

    def test_tool_name(self) -> None:
        """Test tool_name property."""
        manager = GoManager()
        assert manager.tool_name == "go"

    def test_executable_name(self) -> None:
        """Test executable_name property."""
        manager = GoManager()
        assert manager.executable_name == "go"


class TestGetAvailableVersions(FoundationTestCase):
    """Test get_available_versions method."""

    def test_get_available_versions_success(self) -> None:
        """Test fetching versions from Go API."""
        # Mock API response - Go API returns releases with 'go' prefix
        mock_data = [
            {"version": "go1.22.0", "stable": True},
            {"version": "go1.21.5", "stable": True},
            {"version": "go1.21.4", "stable": True},
        ]

        manager = GoManager()
        with patch.object(manager, "fetch_json_secure", return_value=mock_data):
            versions = manager.get_available_versions()

        assert isinstance(versions, list)
        # Versions should have 'go' prefix stripped
        assert "1.22.0" in versions
        assert "1.21.5" in versions
        assert "1.21.4" in versions
        # Should NOT have 'go' prefix
        assert "go1.22.0" not in versions

    def test_get_available_versions_includes_unstable(self) -> None:
        """Test fetching versions including unstable when configured."""
        mock_data = [
            {"version": "go1.22.0", "stable": True},
            {"version": "go1.22rc1", "stable": False},
        ]

        manager = GoManager()
        # Mock the config setting check and fetch
        with (
            patch.object(manager, "fetch_json_secure", return_value=mock_data),
            patch.object(manager.config, "get_setting", return_value=True),
        ):
            versions = manager.get_available_versions()
            assert "1.22rc1" in versions

    def test_get_available_versions_filters_unstable(self) -> None:
        """Test that unstable versions are filtered by default."""
        mock_data = [
            {"version": "go1.22.0", "stable": True},
            {"version": "go1.22rc1", "stable": False},
        ]

        manager = GoManager()
        with patch.object(manager, "fetch_json_secure", return_value=mock_data):
            versions = manager.get_available_versions()

        # Unstable should be filtered out by default
        assert "1.22.0" in versions
        assert "1.22rc1" not in versions

    def test_get_available_versions_network_failure(self) -> None:
        """Test handling network failures."""
        manager = GoManager()
        with (
            patch.object(manager, "fetch_json_secure", side_effect=Exception("Network error")),
            pytest.raises(ToolManagerError, match="Failed to fetch Go versions"),
        ):
            manager.get_available_versions()


class TestGetDownloadUrl(FoundationTestCase):
    """Test get_download_url method for different platforms."""

    @patch.object(GoManager, "get_platform_info")
    def test_get_download_url_linux_x86_64(self, mock_platform: Mock) -> None:
        """Test download URL for Linux x86_64."""
        mock_platform.return_value = {"os": "linux", "arch": "amd64"}
        manager = GoManager()

        url = manager.get_download_url("1.22.0")

        assert "go.dev/dl" in url
        assert "go1.22.0" in url
        assert "linux-amd64.tar.gz" in url

    @patch.object(GoManager, "get_platform_info")
    def test_get_download_url_linux_arm64(self, mock_platform: Mock) -> None:
        """Test download URL for Linux ARM64."""
        mock_platform.return_value = {"os": "linux", "arch": "arm64"}
        manager = GoManager()

        url = manager.get_download_url("1.22.0")

        assert "linux-arm64.tar.gz" in url

    @patch.object(GoManager, "get_platform_info")
    def test_get_download_url_macos_x86_64(self, mock_platform: Mock) -> None:
        """Test download URL for macOS x86_64."""
        mock_platform.return_value = {"os": "darwin", "arch": "amd64"}
        manager = GoManager()

        url = manager.get_download_url("1.22.0")

        assert "darwin-amd64.tar.gz" in url

    @patch.object(GoManager, "get_platform_info")
    def test_get_download_url_macos_arm64(self, mock_platform: Mock) -> None:
        """Test download URL for macOS ARM64."""
        mock_platform.return_value = {"os": "darwin", "arch": "arm64"}
        manager = GoManager()

        url = manager.get_download_url("1.22.0")

        assert "darwin-arm64.tar.gz" in url

    @patch.object(GoManager, "get_platform_info")
    def test_get_download_url_windows_x86_64(self, mock_platform: Mock) -> None:
        """Test download URL for Windows x86_64."""
        mock_platform.return_value = {"os": "windows", "arch": "amd64"}
        manager = GoManager()

        url = manager.get_download_url("1.22.0")

        assert "windows-amd64.tar.gz" in url

    @patch.object(GoManager, "get_platform_info")
    def test_get_download_url_with_custom_mirror(self, mock_platform: Mock) -> None:
        """Test download URL with custom mirror configured."""
        mock_platform.return_value = {"os": "linux", "arch": "amd64"}
        manager = GoManager()

        # Mock custom mirror configuration
        with patch.object(manager.config, "get_setting", return_value="https://mirror.example.com/go"):
            url = manager.get_download_url("1.22.0")
            assert "mirror.example.com/go" in url
            assert "go1.22.0.linux-amd64.tar.gz" in url


class TestGetChecksumUrl(FoundationTestCase):
    """Test get_checksum_url method."""

    def test_get_checksum_url_returns_none(self) -> None:
        """Test that Go doesn't provide separate checksum files."""
        manager = GoManager()
        url = manager.get_checksum_url("1.22.0")
        assert url is None


class TestInstallFromArchive(FoundationTestCase):
    """Test _install_from_archive method."""

    @patch.object(Path, "symlink_to")
    @patch("shutil.rmtree")
    @patch.object(GoManager, "verify_installation", return_value=True)
    @patch.object(GoManager, "extract_archive")
    def test_install_from_archive_success(
        self,
        mock_extract: Mock,
        mock_verify: Mock,
        mock_rmtree: Mock,
        mock_symlink: Mock,
        tmp_path: Path,
    ) -> None:
        """Test successful installation from archive."""
        config = WorkenvConfig()
        # Properly set install path via config setting
        with patch.object(config, "get_setting", return_value=str(tmp_path / "tools")):
            manager = GoManager(config)

        # Create fake extracted Go structure
        extract_dir = manager.cache_dir / "go_1.22.0_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        go_root = extract_dir / "go"
        go_root.mkdir(exist_ok=True)
        go_bin = go_root / "bin"
        go_bin.mkdir(exist_ok=True)
        (go_bin / "go").touch()

        archive_path = tmp_path / "go.tar.gz"
        archive_path.touch()

        # Use actual shutil.move so files are actually moved
        import shutil as real_shutil

        with patch("shutil.move", side_effect=real_shutil.move):
            manager._install_from_archive(archive_path, "1.22.0")

        mock_extract.assert_called_once()
        mock_symlink.assert_called_once()
        mock_verify.assert_called_once_with("1.22.0")

    @patch("shutil.rmtree")
    @patch.object(GoManager, "extract_archive")
    def test_install_from_archive_go_dir_not_found(
        self, mock_extract: Mock, mock_rmtree: Mock, tmp_path: Path
    ) -> None:
        """Test error when go directory not found in archive."""
        config = WorkenvConfig()
        with patch.object(config, "get_setting", return_value=str(tmp_path / "tools")):
            manager = GoManager(config)

        # Create extract dir without 'go' subdirectory
        extract_dir = manager.cache_dir / "go_1.22.0_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)

        archive_path = tmp_path / "go.tar.gz"
        archive_path.touch()

        with pytest.raises(ToolManagerError, match="Go directory not found in archive"):
            manager._install_from_archive(archive_path, "1.22.0")

    @patch("shutil.rmtree")
    @patch("shutil.move")
    @patch.object(GoManager, "extract_archive")
    def test_install_from_archive_binary_not_found(
        self, mock_extract: Mock, mock_move: Mock, mock_rmtree: Mock, tmp_path: Path
    ) -> None:
        """Test error when go binary not found in archive."""
        config = WorkenvConfig()
        with patch.object(config, "get_setting", return_value=str(tmp_path / "tools")):
            manager = GoManager(config)

        # Create go directory but no binary
        extract_dir = manager.cache_dir / "go_1.22.0_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        go_root = extract_dir / "go"
        go_root.mkdir(exist_ok=True)

        archive_path = tmp_path / "go.tar.gz"
        archive_path.touch()

        with pytest.raises(ToolManagerError, match="Go binary not found in extracted archive"):
            manager._install_from_archive(archive_path, "1.22.0")

    @patch.object(Path, "symlink_to")
    @patch("shutil.rmtree")
    @patch.object(GoManager, "verify_installation", return_value=False)
    @patch.object(GoManager, "extract_archive")
    def test_install_from_archive_verification_fails(
        self,
        mock_extract: Mock,
        mock_verify: Mock,
        mock_rmtree: Mock,
        mock_symlink: Mock,
        tmp_path: Path,
    ) -> None:
        """Test installation fails when verification fails."""
        config = WorkenvConfig()
        with patch.object(config, "get_setting", return_value=str(tmp_path / "tools")):
            manager = GoManager(config)

        # Create proper structure
        extract_dir = manager.cache_dir / "go_1.22.0_extract"
        extract_dir.mkdir(parents=True, exist_ok=True)
        go_root = extract_dir / "go"
        go_root.mkdir(exist_ok=True)
        go_bin = go_root / "bin"
        go_bin.mkdir(exist_ok=True)
        (go_bin / "go").touch()

        archive_path = tmp_path / "go.tar.gz"
        archive_path.touch()

        # Use actual shutil.move so files are actually moved
        import shutil as real_shutil

        with (
            patch("shutil.move", side_effect=real_shutil.move),
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            manager._install_from_archive(archive_path, "1.22.0")


class TestVerifyInstallation(FoundationTestCase):
    """Test verify_installation method."""

    @patch("subprocess.run")
    def test_verify_installation_success(self, mock_run: Mock, tmp_path: Path) -> None:
        """Test successful installation verification."""
        config = WorkenvConfig()
        config.workenv_cache_dir = str(tmp_path / "cache")
        manager = GoManager(config)

        # Create fake binary structure
        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.touch()

        # Create GOROOT structure
        go_root = binary_path.parent.parent / "go"
        go_root.mkdir(parents=True, exist_ok=True)

        # Mock subprocess to return successful version check
        mock_run.return_value = Mock(returncode=0, stdout="go version go1.22.0 linux/amd64\n", stderr="")

        result = manager.verify_installation("1.22.0")

        assert result is True
        # Verify GOROOT was set in env
        assert mock_run.call_args.kwargs["env"]["GOROOT"] == str(go_root)

    @patch("subprocess.run")
    def test_verify_installation_version_mismatch(self, mock_run: Mock, tmp_path: Path) -> None:
        """Test verification fails on version mismatch."""
        config = WorkenvConfig()
        config.workenv_cache_dir = str(tmp_path / "cache")
        manager = GoManager(config)

        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.touch()

        go_root = binary_path.parent.parent / "go"
        go_root.mkdir(parents=True, exist_ok=True)

        # Mock subprocess with wrong version
        mock_run.return_value = Mock(returncode=0, stdout="go version go1.21.0 linux/amd64\n", stderr="")

        result = manager.verify_installation("1.22.0")
        assert result is False

    def test_verify_installation_binary_missing(self, tmp_path: Path) -> None:
        """Test verification fails when binary doesn't exist."""
        config = WorkenvConfig()
        config.workenv_cache_dir = str(tmp_path / "cache")
        manager = GoManager(config)

        result = manager.verify_installation("1.22.0")
        assert result is False

    @patch("subprocess.run", side_effect=Exception("Command failed"))
    def test_verify_installation_subprocess_error(self, mock_run: Mock, tmp_path: Path) -> None:
        """Test verification handles subprocess errors."""
        config = WorkenvConfig()
        config.workenv_cache_dir = str(tmp_path / "cache")
        manager = GoManager(config)

        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.touch()

        go_root = binary_path.parent.parent / "go"
        go_root.mkdir(parents=True, exist_ok=True)

        result = manager.verify_installation("1.22.0")
        assert result is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
