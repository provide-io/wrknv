#!/usr/bin/env python3

"""
Test suite for platform detection operations.
"""
from __future__ import annotations


from unittest.mock import patch

import pytest
from provide.testkit import FoundationTestCase

from wrknv.wenv.operations.platform import (
    format_platform_string,
    get_architecture,
    get_archive_extension,
    get_download_platform_mappings,
    get_executable_extension,
    get_os_name,
    get_platform_info,
    get_platform_mapping,
    is_supported_platform,
    parse_platform_string,
)


class TestPlatformOperations(FoundationTestCase):
    """Test platform detection operations."""

    def test_get_os_name_darwin(self):
        """Test OS name detection re-exports foundation."""
        # These tests verify the re-export works - just check current platform
        result = get_os_name()
        assert isinstance(result, str)
        assert result in ["darwin", "linux", "windows", "freebsd", "unknown"]

    def test_get_os_name_matches_foundation(self):
        """Test OS name matches foundation."""
        from provide.foundation.platform import get_os_name as foundation_get_os
        assert get_os_name() == foundation_get_os()

    def test_get_architecture_matches_foundation(self):
        """Test architecture matches foundation."""
        from provide.foundation.platform import get_arch_name as foundation_get_arch
        assert get_architecture() == foundation_get_arch()

    @patch("wrknv.wenv.operations.platform.get_system_info")
    def test_get_platform_info(self, mock_get_system_info):
        """Test getting complete platform info."""
        from unittest.mock import MagicMock

        mock_sys_info = MagicMock()
        mock_sys_info.os_name = "darwin"
        mock_sys_info.arch = "arm64"
        mock_sys_info.platform = "darwin_arm64"
        mock_get_system_info.return_value = mock_sys_info

        info = get_platform_info()

        assert info["os"] == "darwin"
        assert info["arch"] == "arm64"
        assert info["platform"] == "darwin_arm64"

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_darwin_arm64(self, mock_arch, mock_os):
        """Test supported platform check for Darwin ARM64."""
        mock_os.return_value = "darwin"
        mock_arch.return_value = "arm64"
        assert is_supported_platform()

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_linux_amd64(self, mock_arch, mock_os):
        """Test supported platform check for Linux AMD64."""
        mock_os.return_value = "linux"
        mock_arch.return_value = "amd64"
        assert is_supported_platform()

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_windows_amd64(self, mock_arch, mock_os):
        """Test supported platform check for Windows AMD64."""
        mock_os.return_value = "windows"
        mock_arch.return_value = "amd64"
        assert is_supported_platform()

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_unsupported(self, mock_arch, mock_os):
        """Test unsupported platform check."""
        mock_os.return_value = "aix"
        mock_arch.return_value = "ppc64"
        assert not is_supported_platform()

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_executable_extension_windows(self, mock_os):
        """Test executable extension for Windows."""
        mock_os.return_value = "windows"
        assert get_executable_extension() == ".exe"

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_executable_extension_unix(self, mock_os):
        """Test executable extension for Unix-like systems."""
        mock_os.return_value = "linux"
        assert get_executable_extension() == ""

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_archive_extension_windows(self, mock_os):
        """Test archive extension for Windows."""
        mock_os.return_value = "windows"
        assert get_archive_extension() == ".zip"

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_archive_extension_unix(self, mock_os):
        """Test archive extension for Unix-like systems."""
        mock_os.return_value = "linux"
        assert get_archive_extension() == ".tar.gz"

    def test_format_platform_string(self) -> None:
        """Test platform string formatting."""
        assert format_platform_string("darwin" == "arm64", "darwin_arm64")
        assert format_platform_string("linux" == "amd64", "linux_amd64")

    def test_parse_platform_string_valid(self) -> None:
        """Test parsing valid platform strings."""
        result = parse_platform_string("darwin_arm64")
        assert result["os"] == "darwin"
        assert result["arch"] == "arm64"

    def test_parse_platform_string_os_only(self) -> None:
        """Test parsing platform string with OS only."""
        result = parse_platform_string("linux")
        assert result["os"] == "linux"
        assert result["arch"] == "unknown"

    def test_parse_platform_string_arch_only(self) -> None:
        """Test parsing platform string with arch only."""
        result = parse_platform_string("amd64")
        assert result["os"] == "unknown"
        assert result["arch"] == "amd64"

    def test_parse_platform_string_unknown(self) -> None:
        """Test parsing unknown platform string."""
        result = parse_platform_string("something")
        assert result["os"] == "unknown"
        assert result["arch"] == "unknown"

    def test_get_download_platform_mappings(self) -> None:
        """Test getting platform mappings."""
        mappings = get_download_platform_mappings()

        assert "terraform" in mappings
        assert "tofu" in mappings
        assert "go" in mappings
        assert "uv" in mappings

        # Check UV has special mappings
        assert mappings["uv"]["darwin"] == "apple-darwin"
        assert mappings["uv"]["linux"] == "unknown-linux-gnu"
        assert mappings["uv"]["windows"] == "pc-windows-msvc"

    def test_get_platform_mapping_terraform_os(self) -> None:
        """Test platform mapping for Terraform OS."""
        result = get_platform_mapping("terraform", "darwin", "os")
        assert result == "darwin"

    def test_get_platform_mapping_uv_os(self) -> None:
        """Test platform mapping for UV OS."""
        result = get_platform_mapping("uv", "darwin", "os")
        assert result == "apple-darwin"

    def test_get_platform_mapping_arch(self) -> None:
        """Test platform mapping for architecture."""
        result = get_platform_mapping("terraform", "arm64", "arch")
        assert result == "arm64"

    def test_get_platform_mapping_unknown_tool(self) -> None:
        """Test platform mapping for unknown tool."""
        result = get_platform_mapping("unknown", "darwin", "os")
        assert result == "darwin"

    def test_get_platform_mapping_other_type(self) -> None:
        """Test platform mapping for other type."""
        result = get_platform_mapping("terraform", "something", "other")
        assert result == "something"


class TestPlatformEdgeCases(FoundationTestCase):
    """Test edge cases in platform detection."""

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_freebsd(self, mock_arch, mock_os):
        """Test FreeBSD platform support."""
        mock_os.return_value = "freebsd"
        mock_arch.return_value = "amd64"
        assert is_supported_platform()

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_windows_386(self, mock_arch, mock_os):
        """Test Windows 32-bit platform support."""
        mock_os.return_value = "windows"
        mock_arch.return_value = "386"
        assert is_supported_platform()

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_linux_386(self, mock_arch, mock_os):
        """Test Linux 32-bit platform support."""
        mock_os.return_value = "linux"
        mock_arch.return_value = "386"
        assert is_supported_platform()

    def test_parse_platform_string_multiple_underscores(self) -> None:
        """Test parsing platform string with multiple underscores."""
        result = parse_platform_string("darwin_arm64_extra")
        assert result["os"] == "darwin"
        assert result["arch"] == "arm64_extra"

    def test_get_platform_mapping_missing_os_mapping(self) -> None:
        """Test platform mapping when OS mapping is missing."""
        result = get_platform_mapping("uv", "freebsd", "os")
        # Should return original value when not in mappings
        assert result == "freebsd"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])