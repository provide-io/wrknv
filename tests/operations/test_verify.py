#!/usr/bin/env python3
#
# tests/test_operations_verify.py
#
"""
Comprehensive tests for the operations/verify module.
"""

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from wrkenv.wenv.operations.verify import (
    check_binary_compatibility,
    get_installed_version_info,
    get_version_command_args,
    parse_generic_version,
    parse_go_version,
    parse_terraform_version,
    parse_tofu_version,
    parse_uv_version,
    run_version_check,
    validate_installation_directory,
    verify_tool_installation,
)


class TestVerifyOperations(unittest.TestCase):
    """Test suite for verification operations."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    # Test verify_tool_installation
    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_verify_tool_installation_success(self, mock_run_check):
        """Test successful tool installation verification."""
        binary_path = self.temp_path / "bin" / "terraform"
        binary_path.parent.mkdir(parents=True)
        binary_path.touch()
        
        mock_run_check.return_value = "Terraform v1.5.0"
        
        result = verify_tool_installation(binary_path, "1.5.0", "terraform")
        
        self.assertTrue(result)
        mock_run_check.assert_called_once_with(binary_path, "terraform")

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_verify_tool_installation_binary_not_found(self, mock_run_check):
        """Test verification when binary doesn't exist."""
        binary_path = self.temp_path / "bin" / "terraform"
        
        result = verify_tool_installation(binary_path, "1.5.0", "terraform")
        
        self.assertFalse(result)
        mock_run_check.assert_not_called()

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_verify_tool_installation_version_mismatch(self, mock_run_check):
        """Test verification with version mismatch."""
        binary_path = self.temp_path / "bin" / "terraform"
        binary_path.parent.mkdir(parents=True)
        binary_path.touch()
        
        mock_run_check.return_value = "Terraform v1.4.0"
        
        result = verify_tool_installation(binary_path, "1.5.0", "terraform")
        
        self.assertFalse(result)

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_verify_tool_installation_check_fails(self, mock_run_check):
        """Test verification when version check fails."""
        binary_path = self.temp_path / "bin" / "terraform"
        binary_path.parent.mkdir(parents=True)
        binary_path.touch()
        
        mock_run_check.return_value = None
        
        result = verify_tool_installation(binary_path, "1.5.0", "terraform")
        
        self.assertFalse(result)

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_verify_tool_installation_exception(self, mock_run_check):
        """Test verification with exception."""
        binary_path = self.temp_path / "bin" / "terraform"
        binary_path.parent.mkdir(parents=True)
        binary_path.touch()
        
        mock_run_check.side_effect = Exception("Test error")
        
        result = verify_tool_installation(binary_path, "1.5.0", "terraform")
        
        self.assertFalse(result)

    # Test run_version_check
    @patch("subprocess.run")
    def test_run_version_check_success(self, mock_run):
        """Test successful version check."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.return_value = Mock(
            returncode=0, stdout="Terraform v1.5.0\n", stderr=""
        )
        
        result = run_version_check(binary_path, "terraform", timeout=10)
        
        self.assertEqual(result, "Terraform v1.5.0")
        mock_run.assert_called_once_with(
            [str(binary_path), "version"],
            capture_output=True,
            text=True,
            timeout=10,
        )

    def test_run_version_check_binary_not_exists(self):
        """Test version check when binary doesn't exist."""
        binary_path = self.temp_path / "terraform"
        
        result = run_version_check(binary_path, "terraform")
        
        self.assertIsNone(result)

    @patch("subprocess.run")
    def test_run_version_check_failure(self, mock_run):
        """Test version check with non-zero return code."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.return_value = Mock(
            returncode=1, stdout="", stderr="Error running command"
        )
        
        result = run_version_check(binary_path, "terraform")
        
        self.assertIsNone(result)

    @patch("subprocess.run")
    def test_run_version_check_timeout(self, mock_run):
        """Test version check with timeout."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.side_effect = subprocess.TimeoutExpired("cmd", 10)
        
        result = run_version_check(binary_path, "terraform")
        
        self.assertIsNone(result)

    @patch("subprocess.run")
    def test_run_version_check_exception(self, mock_run):
        """Test version check with general exception."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.side_effect = Exception("Test error")
        
        result = run_version_check(binary_path, "terraform")
        
        self.assertIsNone(result)

    # Test get_version_command_args
    def test_get_version_command_args_terraform(self):
        """Test getting version args for terraform."""
        args = get_version_command_args("terraform")
        self.assertEqual(args, ["version"])

    def test_get_version_command_args_tofu(self):
        """Test getting version args for tofu."""
        args = get_version_command_args("tofu")
        self.assertEqual(args, ["version"])

    def test_get_version_command_args_go(self):
        """Test getting version args for go."""
        args = get_version_command_args("go")
        self.assertEqual(args, ["version"])

    def test_get_version_command_args_uv(self):
        """Test getting version args for uv."""
        args = get_version_command_args("uv")
        self.assertEqual(args, ["--version"])

    def test_get_version_command_args_unknown(self):
        """Test getting version args for unknown tool."""
        args = get_version_command_args("unknown")
        self.assertEqual(args, ["--version"])

    # Test check_binary_compatibility
    @patch("subprocess.run")
    def test_check_binary_compatibility_success(self, mock_run):
        """Test successful binary compatibility check."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.return_value = Mock(
            returncode=0, stdout="Usage: terraform ...", stderr=""
        )
        
        result = check_binary_compatibility(binary_path)
        
        self.assertTrue(result["compatible"])
        self.assertEqual(result["returncode"], 0)
        self.assertIn("Usage", result["stdout"])

    def test_check_binary_compatibility_not_found(self):
        """Test compatibility check when binary not found."""
        binary_path = self.temp_path / "terraform"
        
        result = check_binary_compatibility(binary_path)
        
        self.assertFalse(result["compatible"])
        self.assertEqual(result["error"], "Binary not found")

    @patch("subprocess.run")
    def test_check_binary_compatibility_incompatible(self, mock_run):
        """Test incompatible binary."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.return_value = Mock(
            returncode=127, stdout="", stderr="cannot execute binary file"
        )
        
        result = check_binary_compatibility(binary_path)
        
        self.assertFalse(result["compatible"])
        self.assertEqual(result["returncode"], 127)

    @patch("subprocess.run")
    def test_check_binary_compatibility_timeout(self, mock_run):
        """Test compatibility check with timeout."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.side_effect = subprocess.TimeoutExpired("cmd", 5)
        
        result = check_binary_compatibility(binary_path)
        
        self.assertFalse(result["compatible"])
        self.assertEqual(result["error"], "Binary execution timed out")

    @patch("subprocess.run")
    def test_check_binary_compatibility_exception(self, mock_run):
        """Test compatibility check with exception."""
        binary_path = self.temp_path / "terraform"
        binary_path.touch()
        
        mock_run.side_effect = Exception("Test error")
        
        result = check_binary_compatibility(binary_path)
        
        self.assertFalse(result["compatible"])
        self.assertEqual(result["error"], "Test error")

    # Test validate_installation_directory
    @patch("wrkenv.env.operations.install.is_executable")
    @patch("wrkenv.env.operations.platform.get_executable_extension")
    def test_validate_installation_directory_success(
        self, mock_get_ext, mock_is_exec
    ):
        """Test successful installation directory validation."""
        install_dir = self.temp_path / "terraform" / "1.5.0"
        bin_dir = install_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        mock_get_ext.return_value = ""
        binary_path = bin_dir / "terraform"
        binary_path.touch()
        mock_is_exec.return_value = True
        
        result = validate_installation_directory(install_dir, "terraform", "1.5.0")
        
        self.assertTrue(result)
        mock_is_exec.assert_called_once_with(binary_path)

    def test_validate_installation_directory_not_exists(self):
        """Test validation when directory doesn't exist."""
        install_dir = self.temp_path / "terraform" / "1.5.0"
        
        result = validate_installation_directory(install_dir, "terraform", "1.5.0")
        
        self.assertFalse(result)

    @patch("wrkenv.env.operations.platform.get_executable_extension")
    def test_validate_installation_directory_no_bin(self, mock_get_ext):
        """Test validation when bin directory doesn't exist."""
        install_dir = self.temp_path / "terraform" / "1.5.0"
        install_dir.mkdir(parents=True)
        mock_get_ext.return_value = ""
        
        result = validate_installation_directory(install_dir, "terraform", "1.5.0")
        
        self.assertFalse(result)

    @patch("wrkenv.env.operations.platform.get_executable_extension")
    def test_validate_installation_directory_no_binary(self, mock_get_ext):
        """Test validation when binary doesn't exist."""
        install_dir = self.temp_path / "terraform" / "1.5.0"
        bin_dir = install_dir / "bin"
        bin_dir.mkdir(parents=True)
        mock_get_ext.return_value = ""
        
        result = validate_installation_directory(install_dir, "terraform", "1.5.0")
        
        self.assertFalse(result)

    @patch("wrkenv.env.operations.install.is_executable")
    @patch("wrkenv.env.operations.platform.get_executable_extension")
    def test_validate_installation_directory_not_executable(
        self, mock_get_ext, mock_is_exec
    ):
        """Test validation when binary is not executable."""
        install_dir = self.temp_path / "terraform" / "1.5.0"
        bin_dir = install_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        mock_get_ext.return_value = ""
        binary_path = bin_dir / "terraform"
        binary_path.touch()
        mock_is_exec.return_value = False
        
        result = validate_installation_directory(install_dir, "terraform", "1.5.0")
        
        self.assertFalse(result)

    # Test get_installed_version_info
    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_get_installed_version_info_terraform(self, mock_run_check):
        """Test getting terraform version info."""
        binary_path = self.temp_path / "terraform"
        mock_run_check.return_value = "Terraform v1.5.0\non linux_amd64"
        
        result = get_installed_version_info(binary_path, "terraform")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["tool"], "terraform")
        self.assertEqual(result["version"], "1.5.0")
        self.assertEqual(result["platform"], "linux_amd64")

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_get_installed_version_info_tofu(self, mock_run_check):
        """Test getting tofu version info."""
        binary_path = self.temp_path / "tofu"
        mock_run_check.return_value = "OpenTofu v1.6.0\non darwin_arm64"
        
        result = get_installed_version_info(binary_path, "tofu")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["tool"], "tofu")
        self.assertEqual(result["version"], "1.6.0")

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_get_installed_version_info_go(self, mock_run_check):
        """Test getting go version info."""
        binary_path = self.temp_path / "go"
        mock_run_check.return_value = "go version go1.21.0 linux/amd64"
        
        result = get_installed_version_info(binary_path, "go")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["tool"], "go")
        self.assertEqual(result["version"], "1.21.0")
        self.assertEqual(result["platform"], "linux/amd64")

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_get_installed_version_info_uv(self, mock_run_check):
        """Test getting uv version info."""
        binary_path = self.temp_path / "uv"
        mock_run_check.return_value = "uv 0.1.0"
        
        result = get_installed_version_info(binary_path, "uv")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["tool"], "uv")
        self.assertEqual(result["version"], "0.1.0")

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_get_installed_version_info_generic(self, mock_run_check):
        """Test getting generic tool version info."""
        binary_path = self.temp_path / "tool"
        mock_run_check.return_value = "tool version 2.3.4"
        
        result = get_installed_version_info(binary_path, "tool")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["tool"], "tool")
        self.assertIn("2.3.4", result["raw_output"])

    @patch("wrkenv.env.operations.verify.run_version_check")
    def test_get_installed_version_info_no_output(self, mock_run_check):
        """Test getting version info with no output."""
        binary_path = self.temp_path / "tool"
        mock_run_check.return_value = None
        
        result = get_installed_version_info(binary_path, "tool")
        
        self.assertIsNone(result)

    # Test parse functions
    def test_parse_terraform_version(self):
        """Test parsing terraform version output."""
        output = "Terraform v1.5.0\non linux_amd64"
        result = parse_terraform_version(output)
        
        self.assertEqual(result["tool"], "terraform")
        self.assertEqual(result["version"], "1.5.0")
        self.assertEqual(result["platform"], "linux_amd64")

    def test_parse_tofu_version(self):
        """Test parsing tofu version output."""
        output = "OpenTofu v1.6.0\non darwin_arm64"
        result = parse_tofu_version(output)
        
        self.assertEqual(result["tool"], "tofu")
        self.assertEqual(result["version"], "1.6.0")

    def test_parse_go_version(self):
        """Test parsing go version output."""
        output = "go version go1.21.0 linux/amd64"
        result = parse_go_version(output)
        
        self.assertEqual(result["tool"], "go")
        self.assertEqual(result["version"], "1.21.0")
        self.assertEqual(result["platform"], "linux/amd64")

    def test_parse_uv_version(self):
        """Test parsing uv version output."""
        output = "uv 0.1.0"
        result = parse_uv_version(output)
        
        self.assertEqual(result["tool"], "uv")
        self.assertEqual(result["version"], "0.1.0")

    def test_parse_generic_version(self):
        """Test parsing generic version output."""
        output = "some-tool version 1.2.3\nother info"
        result = parse_generic_version(output, "some-tool")
        
        self.assertEqual(result["tool"], "some-tool")
        self.assertEqual(result["raw_output"], output)
        # Should attempt to extract version
        self.assertIn("version", result)


if __name__ == "__main__":
    unittest.main()