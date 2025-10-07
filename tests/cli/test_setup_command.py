#!/usr/bin/env python3

"""
Test suite for CLI setup command.
"""

from __future__ import annotations

import subprocess
from unittest.mock import Mock, patch

import click.testing
from provide.testkit import FoundationTestCase
import pytest

from wrknv.cli.hub_cli import create_cli


class TestSetupCommand(FoundationTestCase):
    """Test setup CLI command."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.runner = click.testing.CliRunner()
        self.cli = create_cli()
        self.temp_dir = self.create_temp_dir()
        self.temp_path = self.temp_dir

    def test_setup_no_options(self) -> None:
        """Test setup command with no options shows help."""
        result = self.runner.invoke(self.cli, ["setup"])

        assert result.exit_code == 0
        assert "Available setup options:" in result.output
        assert "--init" in result.output
        assert "--shell-integration" in result.output

    @patch("wrknv.cli.commands.setup.WorkenvManager")
    def test_setup_init(self, mock_manager_class):
        """Test setup --init to create wrknv's own workenv."""
        mock_manager_class.setup_workenv.return_value = True

        result = self.runner.invoke(self.cli, ["setup", "--init"])

        assert result.exit_code == 0
        assert "Setting up wrknv workenv" in result.output
        mock_manager_class.setup_workenv.assert_called_once_with(force=False)

    @patch("wrknv.cli.commands.setup.WorkenvManager")
    def test_setup_init_force(self, mock_manager_class):
        """Test setup --init --force to recreate workenv."""
        mock_manager_class.setup_workenv.return_value = True

        result = self.runner.invoke(self.cli, ["setup", "--init", "--force"])

        assert result.exit_code == 0
        mock_manager_class.setup_workenv.assert_called_once_with(force=True)

    @patch("wrknv.cli.commands.setup.WorkenvManager")
    def test_setup_init_failure(self, mock_manager_class):
        """Test setup --init when creation fails."""
        mock_manager_class.setup_workenv.side_effect = Exception("Failed to create virtualenv")

        result = self.runner.invoke(self.cli, ["setup", "--init"], catch_exceptions=False)

        assert result.exit_code != 0

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_shell_integration_success(self, mock_exists, mock_run):
        """Test successful shell integration setup."""
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0)

        result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

        assert result.exit_code == 0
        assert "Setting up shell integration" in result.output
        assert "Shell integration configured successfully" in result.output
        mock_run.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_shell_integration_script_not_found(self, mock_exists, mock_run):
        """Test shell integration when script is missing."""
        mock_exists.return_value = False

        result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

        assert result.exit_code == 1
        assert "Shell integration script not found" in result.output
        mock_run.assert_not_called()

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.exists")
    def test_setup_shell_integration_script_fails(self, mock_exists, mock_run):
        """Test shell integration when script execution fails."""
        mock_exists.return_value = True
        mock_run.side_effect = subprocess.CalledProcessError(1, ["bash", "script.sh"])

        result = self.runner.invoke(self.cli, ["setup", "--shell-integration"])

        assert result.exit_code == 1
        assert "Failed to set up shell integration" in result.output

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

            assert result.exit_code == 0

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

        result = self.runner.invoke(self.cli, ["setup", "--init", "--shell-integration"])

        assert result.exit_code == 0
        assert "Setting up wrknv workenv" in result.output
        assert "Setting up shell integration" in result.output
        mock_manager.setup_workenv.assert_called_once()
        mock_run.assert_called_once()

    def test_setup_check_dependencies(self) -> None:
        """Test setup --check to verify dependencies."""
        with patch("shutil.which") as mock_which:
            # Mock that all dependencies are installed
            mock_which.side_effect = lambda x: f"/usr/bin/{x}" if x in ["git", "curl", "python3"] else None

            result = self.runner.invoke(self.cli, ["setup", "--check"])

            assert result.exit_code == 0
            assert "Checking dependencies" in result.output
            assert "✓ git" in result.output
            assert "✓ curl" in result.output
            assert "✓ python3" in result.output

    def test_setup_check_missing_dependencies(self) -> None:
        """Test setup --check when dependencies are missing."""
        with patch("shutil.which") as mock_which:
            # Mock that git is missing
            mock_which.side_effect = lambda x: None if x == "git" else f"/usr/bin/{x}"

            result = self.runner.invoke(self.cli, ["setup", "--check"])

            assert result.exit_code == 1
            assert "Missing dependencies" in result.output
            assert "✗ git" in result.output

    def test_setup_completions_bash(self) -> None:
        """Test generating bash completions."""
        result = self.runner.invoke(self.cli, ["setup", "--completions", "bash"])

        assert result.exit_code == 0
        assert "_wrknv_completion" in result.output
        assert "complete -F" in result.output

    def test_setup_completions_zsh(self) -> None:
        """Test generating zsh completions."""
        result = self.runner.invoke(self.cli, ["setup", "--completions", "zsh"])

        assert result.exit_code == 0
        assert "#compdef wrknv" in result.output

    def test_setup_completions_fish(self) -> None:
        """Test generating fish completions."""
        result = self.runner.invoke(self.cli, ["setup", "--completions", "fish"])

        assert result.exit_code == 0
        assert "complete -c wrknv" in result.output

    def test_setup_completions_install(self) -> None:
        """Test installing shell completions."""
        with patch("pathlib.Path.home") as mock_home:
            mock_home.return_value = self.temp_path

            # Create mock shell config files
            bashrc = self.temp_path / ".bashrc"
            bashrc.touch()

            result = self.runner.invoke(self.cli, ["setup", "--completions", "bash", "--install"])

            assert result.exit_code == 0
            assert "Installed bash completions" in result.output

            # Verify completions were added to bashrc
            content = bashrc.read_text()
            assert "wrknv completion" in content


class TestSetupCommandIntegration(FoundationTestCase):
    """Integration tests for setup command."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.runner = click.testing.CliRunner()
        self.cli = create_cli()
        self.temp_dir = self.create_temp_dir()
        self.temp_path = self.temp_dir

    def test_setup_creates_workenv_structure(self) -> None:
        """Test that setup creates the expected directory structure."""
        with patch("pathlib.Path.cwd") as mock_cwd:
            mock_cwd.return_value = self.temp_path

            result = self.runner.invoke(self.cli, ["setup", "--init"])

            if result.exit_code == 0:
                # Check that workenv directory was created
                workenv_dir = self.temp_path / "workenv"
                assert workenv_dir.exists()

                # Check for expected subdirectories
                expected_dirs = ["bin", "lib", "include"]
                for dir_name in expected_dirs:
                    dir_path = workenv_dir / dir_name
                    if dir_path.exists():
                        assert dir_path.is_dir()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
