#!/usr/bin/env python3

"""
Test suite for platform detection operations.
"""

import unittest
from unittest.mock import patch

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


class TestPlatformOperations(unittest.TestCase):
    """Test platform detection operations."""

    @patch("wrknv.wenv.operations.platform.platform.system")
    def test_get_os_name_darwin(self, mock_system):
        """Test OS name detection for macOS."""
        mock_system.return_value = "Darwin"
        self.assertEqual(get_os_name(), "darwin")

    @patch("wrknv.wenv.operations.platform.platform.system")
    def test_get_os_name_linux(self, mock_system):
        """Test OS name detection for Linux."""
        mock_system.return_value = "Linux"
        self.assertEqual(get_os_name(), "linux")

    @patch("wrknv.wenv.operations.platform.platform.system")
    def test_get_os_name_windows(self, mock_system):
        """Test OS name detection for Windows."""
        mock_system.return_value = "Windows"
        self.assertEqual(get_os_name(), "windows")

    @patch("wrknv.wenv.operations.platform.platform.system")
    def test_get_os_name_freebsd(self, mock_system):
        """Test OS name detection for FreeBSD."""
        mock_system.return_value = "FreeBSD"
        self.assertEqual(get_os_name(), "freebsd")

    @patch("wrknv.wenv.operations.platform.platform.system")
    def test_get_os_name_unknown(self, mock_system):
        """Test OS name detection for unknown OS."""
        mock_system.return_value = "Unknown"
        self.assertEqual(get_os_name(), "unknown")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_x86_64(self, mock_machine):
        """Test architecture detection for x86_64."""
        mock_machine.return_value = "x86_64"
        self.assertEqual(get_architecture(), "amd64")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_amd64(self, mock_machine):
        """Test architecture detection for amd64."""
        mock_machine.return_value = "AMD64"
        self.assertEqual(get_architecture(), "amd64")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_arm64(self, mock_machine):
        """Test architecture detection for arm64."""
        mock_machine.return_value = "arm64"
        self.assertEqual(get_architecture(), "arm64")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_aarch64(self, mock_machine):
        """Test architecture detection for aarch64."""
        mock_machine.return_value = "aarch64"
        self.assertEqual(get_architecture(), "arm64")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_i386(self, mock_machine):
        """Test architecture detection for i386."""
        mock_machine.return_value = "i386"
        self.assertEqual(get_architecture(), "386")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_i686(self, mock_machine):
        """Test architecture detection for i686."""
        mock_machine.return_value = "i686"
        self.assertEqual(get_architecture(), "386")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_arm(self, mock_machine):
        """Test architecture detection for ARM."""
        mock_machine.return_value = "armv7l"
        self.assertEqual(get_architecture(), "arm")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_arm64_variant(self, mock_machine):
        """Test architecture detection for ARM64 variant."""
        mock_machine.return_value = "armv8-64"
        self.assertEqual(get_architecture(), "arm64")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    def test_get_architecture_unknown(self, mock_machine):
        """Test architecture detection for unknown arch."""
        mock_machine.return_value = "riscv64"
        self.assertEqual(get_architecture(), "riscv64")

    @patch("wrknv.wenv.operations.platform.platform.machine")
    @patch("wrknv.wenv.operations.platform.platform.system")
    @patch("wrknv.wenv.operations.platform.sys.platform", "darwin")
    def test_get_platform_info(self, mock_system, mock_machine):
        """Test getting complete platform info."""
        mock_system.return_value = "Darwin"
        mock_machine.return_value = "arm64"

        info = get_platform_info()

        self.assertEqual(info["os"], "darwin")
        self.assertEqual(info["arch"], "arm64")
        self.assertEqual(info["platform"], "darwin_arm64")
        self.assertEqual(info["python_platform"], "darwin")
        self.assertEqual(info["machine"], "arm64")
        self.assertEqual(info["system"], "Darwin")

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_darwin_arm64(self, mock_arch, mock_os):
        """Test supported platform check for Darwin ARM64."""
        mock_os.return_value = "darwin"
        mock_arch.return_value = "arm64"
        self.assertTrue(is_supported_platform())

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_linux_amd64(self, mock_arch, mock_os):
        """Test supported platform check for Linux AMD64."""
        mock_os.return_value = "linux"
        mock_arch.return_value = "amd64"
        self.assertTrue(is_supported_platform())

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_windows_amd64(self, mock_arch, mock_os):
        """Test supported platform check for Windows AMD64."""
        mock_os.return_value = "windows"
        mock_arch.return_value = "amd64"
        self.assertTrue(is_supported_platform())

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_unsupported(self, mock_arch, mock_os):
        """Test unsupported platform check."""
        mock_os.return_value = "aix"
        mock_arch.return_value = "ppc64"
        self.assertFalse(is_supported_platform())

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_executable_extension_windows(self, mock_os):
        """Test executable extension for Windows."""
        mock_os.return_value = "windows"
        self.assertEqual(get_executable_extension(), ".exe")

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_executable_extension_unix(self, mock_os):
        """Test executable extension for Unix-like systems."""
        mock_os.return_value = "linux"
        self.assertEqual(get_executable_extension(), "")

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_archive_extension_windows(self, mock_os):
        """Test archive extension for Windows."""
        mock_os.return_value = "windows"
        self.assertEqual(get_archive_extension(), ".zip")

    @patch("wrknv.wenv.operations.platform.get_os_name")
    def test_get_archive_extension_unix(self, mock_os):
        """Test archive extension for Unix-like systems."""
        mock_os.return_value = "linux"
        self.assertEqual(get_archive_extension(), ".tar.gz")

    def test_format_platform_string(self):
        """Test platform string formatting."""
        self.assertEqual(format_platform_string("darwin", "arm64"), "darwin_arm64")
        self.assertEqual(format_platform_string("linux", "amd64"), "linux_amd64")

    def test_parse_platform_string_valid(self):
        """Test parsing valid platform strings."""
        result = parse_platform_string("darwin_arm64")
        self.assertEqual(result["os"], "darwin")
        self.assertEqual(result["arch"], "arm64")

    def test_parse_platform_string_os_only(self):
        """Test parsing platform string with OS only."""
        result = parse_platform_string("linux")
        self.assertEqual(result["os"], "linux")
        self.assertEqual(result["arch"], "unknown")

    def test_parse_platform_string_arch_only(self):
        """Test parsing platform string with arch only."""
        result = parse_platform_string("amd64")
        self.assertEqual(result["os"], "unknown")
        self.assertEqual(result["arch"], "amd64")

    def test_parse_platform_string_unknown(self):
        """Test parsing unknown platform string."""
        result = parse_platform_string("something")
        self.assertEqual(result["os"], "unknown")
        self.assertEqual(result["arch"], "unknown")

    def test_get_download_platform_mappings(self):
        """Test getting platform mappings."""
        mappings = get_download_platform_mappings()

        self.assertIn("terraform", mappings)
        self.assertIn("tofu", mappings)
        self.assertIn("go", mappings)
        self.assertIn("uv", mappings)

        # Check UV has special mappings
        self.assertEqual(mappings["uv"]["darwin"], "apple-darwin")
        self.assertEqual(mappings["uv"]["linux"], "unknown-linux-gnu")
        self.assertEqual(mappings["uv"]["windows"], "pc-windows-msvc")

    def test_get_platform_mapping_terraform_os(self):
        """Test platform mapping for Terraform OS."""
        result = get_platform_mapping("terraform", "darwin", "os")
        self.assertEqual(result, "darwin")

    def test_get_platform_mapping_uv_os(self):
        """Test platform mapping for UV OS."""
        result = get_platform_mapping("uv", "darwin", "os")
        self.assertEqual(result, "apple-darwin")

    def test_get_platform_mapping_arch(self):
        """Test platform mapping for architecture."""
        result = get_platform_mapping("terraform", "arm64", "arch")
        self.assertEqual(result, "arm64")

    def test_get_platform_mapping_unknown_tool(self):
        """Test platform mapping for unknown tool."""
        result = get_platform_mapping("unknown", "darwin", "os")
        self.assertEqual(result, "darwin")

    def test_get_platform_mapping_other_type(self):
        """Test platform mapping for other type."""
        result = get_platform_mapping("terraform", "something", "other")
        self.assertEqual(result, "something")


class TestPlatformEdgeCases(unittest.TestCase):
    """Test edge cases in platform detection."""

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_freebsd(self, mock_arch, mock_os):
        """Test FreeBSD platform support."""
        mock_os.return_value = "freebsd"
        mock_arch.return_value = "amd64"
        self.assertTrue(is_supported_platform())

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_windows_386(self, mock_arch, mock_os):
        """Test Windows 32-bit platform support."""
        mock_os.return_value = "windows"
        mock_arch.return_value = "386"
        self.assertTrue(is_supported_platform())

    @patch("wrknv.wenv.operations.platform.get_os_name")
    @patch("wrknv.wenv.operations.platform.get_architecture")
    def test_is_supported_platform_linux_386(self, mock_arch, mock_os):
        """Test Linux 32-bit platform support."""
        mock_os.return_value = "linux"
        mock_arch.return_value = "386"
        self.assertTrue(is_supported_platform())

    def test_parse_platform_string_multiple_underscores(self):
        """Test parsing platform string with multiple underscores."""
        result = parse_platform_string("darwin_arm64_extra")
        self.assertEqual(result["os"], "darwin")
        self.assertEqual(result["arch"], "arm64_extra")

    def test_get_platform_mapping_missing_os_mapping(self):
        """Test platform mapping when OS mapping is missing."""
        result = get_platform_mapping("uv", "freebsd", "os")
        # Should return original value when not in mappings
        self.assertEqual(result, "freebsd")


if __name__ == "__main__":
    unittest.main()
