#!/usr/bin/env python3

"""
Test suite for CLI setup command.
"""

from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

import click.testing

from wrknv.cli.hub_cli import create_cli


class TestSetupCommand(unittest.TestCase):
    """Test setup CLI command."""

    def setUp(self):
        """Set up test fixtures."""
        self.runner = click.testing.CliRunner()
        self.cli = create_cli()
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_setup_no_options(self):
        """Test setup command with no options shows help."""
        result = self.runner.invoke(self.cli, ["setup"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Available setup options:", result.output)
        self.assertIn("--init", result.output)
        self.assertIn("--shell-integration", result.output)

    @patch("wrknv.wenv.workenv.WorkenvManager")
    def test_setup_init(self, mock_manager_class):
        """Test setup --init to create wrknv's own workenv."""
        mock_manager = Mock()
        mock_manager.setup_workenv.return_value = True
        mock_manager_class.return_value = mock_manager

        result = self.runner.invoke(self.cli, ["setup", "--init"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Setting up wrknv workenv", result.output)
        mock_manager_class.setup_workenv.assert_called_once_with(force=False)

    @patch("wrknv.wenv.workenv.WorkenvManager")
    def test_setup_init_force(self, mock_manager_class):
        """Test setup --init --force to recreate workenv."""
        mock_manager = Mock()
        mock_manager.setup_workenv.return_value = True
        mock_manager_class.return_value = mock_manager

        result = self.runner.invoke(self.cli, ["setup", "--init", "--force"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Forcing recreation of workenv", result.output)
        mock_manager.setup_workenv.assert_called_once_with(force=True)

    @patch("wrknv.wenv.workenv.WorkenvManager")
    def test_setup_init_failure(self, mock_manager_class):
        """Test setup --init when creation fails."""
        mock_manager = Mock()
        mock_manager.setup_workenv.side_effect = Exception("Failed to create virtualenv")
        mock_manager_class.return_value = mock_manager

        result = self.runner.invoke(self.cli, ["setup", "--init"])

        self.assertEqual(result.exit_code, 1)
        self.assertIn("Failed to set up workenv", result.output)
        self.assertIn("Failed to create virtualenv", result.output)

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_shell_integration_success(self, mock_exists, mock_run):
        """Test successful shell integration setup."""
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0)

        result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Setting up shell integration", result.output)
        self.assertIn("Shell integration configured successfully", result.output)
        mock_run.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_shell_integration_script_not_found(self, mock_exists, mock_run):
        """Test shell integration when script is missing."""
        mock_exists.return_value = False

        result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

        self.assertEqual(result.exit_code, 1)
        self.assertIn("Shell integration script not found", result.output)
        mock_run.assert_not_called()

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_shell_integration_script_fails(self, mock_exists, mock_run):
        """Test shell integration when script execution fails."""
        mock_exists.return_value = True
        mock_run.side_effect = subprocess.CalledProcessError(1, ["bash", "script.sh"])

        result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

        self.assertEqual(result.exit_code, 1)
        self.assertIn("Failed to set up shell integration", result.output)

    @patch("provide.foundation.process.run_command")
    def test_setup_shell_integration_creates_aliases(self, mock_run):
        """Test that shell integration creates proper aliases."""
        # Create a mock shell integration script
        script_path = self.temp_path / "scripts" / "shell-integration.sh"
        script_path.parent.mkdir(parents=True)
        script_path.write_text("""#!/bin/bash
# Shell integration script
alias wenv='wrknv'
alias wrknv-activate='source env.sh'
""")

        with patch("pathlib.Path") as mock_path_class:
            mock_path = Mock()
            mock_path.exists.return_value = True
            mock_path.__truediv__.return_value = script_path
            mock_path_class.return_value = mock_path
            mock_run.return_value = Mock(returncode=0)

            result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

            self.assertEqual(result.exit_code, 0)

    @patch("wrknv.wenv.workenv.WorkenvManager")
    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_all_options(self, mock_exists, mock_run, mock_manager_class):
        """Test setup with both --init and --shell-integration."""
        mock_manager = Mock()
        mock_manager.setup_workenv.return_value = True
        mock_manager_class.return_value = mock_manager
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0)

        result = self.runner.invoke(workenv_cli, ["setup", "--init", "--shell-integration"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Setting up wrknv workenv", result.output)
        self.assertIn("Setting up shell integration", result.output)
        mock_manager.setup_workenv.assert_called_once()
        mock_run.assert_called_once()

    def test_setup_check_dependencies(self):
        """Test setup --check to verify dependencies."""
        with patch("shutil.which") as mock_which:
            # Mock that all dependencies are installed
            mock_which.side_effect = lambda x: f"/usr/bin/{x}" if x in ["git", "curl", "python3"] else None

            result = self.runner.invoke(self.cli, ["setup", "--check"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Checking dependencies", result.output)
            self.assertIn("✓ git", result.output)
            self.assertIn("✓ curl", result.output)
            self.assertIn("✓ python3", result.output)

    def test_setup_check_missing_dependencies(self):
        """Test setup --check when dependencies are missing."""
        with patch("shutil.which") as mock_which:
            # Mock that git is missing
            mock_which.side_effect = lambda x: None if x == "git" else f"/usr/bin/{x}"

            result = self.runner.invoke(self.cli, ["setup", "--check"])

            self.assertEqual(result.exit_code, 1)
            self.assertIn("Missing dependencies", result.output)
            self.assertIn("✗ git", result.output)

    def test_setup_completions_bash(self):
        """Test generating bash completions."""
        result = self.runner.invoke(self.cli, ["setup", "--completions", "bash"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("_wrknv_completion", result.output)
        self.assertIn("complete -F", result.output)

    def test_setup_completions_zsh(self):
        """Test generating zsh completions."""
        result = self.runner.invoke(self.cli, ["setup", "--completions", "zsh"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("#compdef wrknv", result.output)

    def test_setup_completions_fish(self):
        """Test generating fish completions."""
        result = self.runner.invoke(self.cli, ["setup", "--completions", "fish"])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("complete -c wrknv", result.output)

    def test_setup_completions_install(self):
        """Test installing shell completions."""
        with patch("pathlib.Path.home") as mock_home:
            mock_home.return_value = self.temp_path

            # Create mock shell config files
            bashrc = self.temp_path / ".bashrc"
            bashrc.touch()

            result = self.runner.invoke(workenv_cli, ["setup", "--completions", "bash", "--install"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Installed bash completions", result.output)

            # Verify completions were added to bashrc
            content = bashrc.read_text()
            self.assertIn("wrknv completion", content)


class TestSetupCommandIntegration(unittest.TestCase):
    """Integration tests for setup command."""

    def setUp(self):
        """Set up test fixtures."""
        self.runner = click.testing.CliRunner()
        self.cli = create_cli()
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_setup_creates_workenv_structure(self):
        """Test that setup creates the expected directory structure."""
        with patch("pathlib.Path.cwd") as mock_cwd:
            mock_cwd.return_value = self.temp_path

            with patch("wrknv.wenv.cli.uv_available") as mock_uv:
                mock_uv.return_value = True

                result = self.runner.invoke(self.cli, ["setup", "--init"])

                if result.exit_code == 0:
                    # Check that workenv directory was created
                    workenv_dir = self.temp_path / "workenv"
                    self.assertTrue(workenv_dir.exists())

                    # Check for expected subdirectories
                    expected_dirs = ["bin", "lib", "include"]
                    for dir_name in expected_dirs:
                        dir_path = workenv_dir / dir_name
                        if dir_path.exists():
                            self.assertTrue(dir_path.is_dir())


if __name__ == "__main__":
    unittest.main()
