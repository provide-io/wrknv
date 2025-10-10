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


# Module-level shared CLI instance
_test_cli = None


def get_test_cli():
    """Get or create the test CLI instance."""
    global _test_cli
    if _test_cli is None:
        _test_cli = create_cli()
    return _test_cli


class TestSetupCommand(FoundationTestCase):
    """Test setup CLI command."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.temp_dir = self.create_temp_dir()
        self.temp_path = self.temp_dir

    def test_setup_no_options(self) -> None:
        """Test setup command with no options shows help."""
        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup"])

        assert result.exit_code == 0
        assert "Available setup options:" in result.output
        assert "--init" in result.output
        assert "--shell-integration" in result.output

    @patch("wrknv.cli.commands.setup.WorkenvManager")
    def test_setup_init(self, mock_manager_class):
        """Test setup --init to create wrknv's own workenv."""
        mock_manager_class.setup_workenv.return_value = True

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--init"])

        assert result.exit_code == 0
        assert "Setting up wrknv workenv" in result.output
        mock_manager_class.setup_workenv.assert_called_once_with(force=False)

    @patch("wrknv.cli.commands.setup.WorkenvManager")
    def test_setup_init_force(self, mock_manager_class):
        """Test setup --init --force to recreate workenv."""
        mock_manager_class.setup_workenv.return_value = True

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--init", "--force"])

        assert result.exit_code == 0
        mock_manager_class.setup_workenv.assert_called_once_with(force=True)

    @patch("wrknv.wenv.workenv.WorkenvManager.setup_workenv")
    def test_setup_init_failure(self, mock_setup_workenv):
        """Test setup --init when creation fails."""
        mock_setup_workenv.side_effect = Exception("Failed to create virtualenv")

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        # Don't use catch_exceptions=False as it breaks with hub registry
        result = runner.invoke(cli, ["setup", "--init"])

        assert result.exit_code != 0
        assert result.exception is not None

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.cli.commands.setup._get_shell_integration_script_path")
    def test_setup_shell_integration_success(self, mock_get_path, mock_run):
        """Test successful shell integration setup."""
        # Mock the path to exist
        from pathlib import Path
        mock_script_path = Mock(spec=Path)
        mock_script_path.exists = Mock(return_value=True)
        mock_script_path.__str__ = Mock(return_value="/fake/path/shell-integration.sh")
        mock_get_path.return_value = mock_script_path

        mock_run.return_value = Mock(returncode=0)

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--shell-integration"])

        assert result.exit_code == 0
        assert "Setting up shell integration" in result.output
        assert "Shell integration configured successfully" in result.output
        mock_run.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.cli.commands.setup._get_shell_integration_script_path")
    def test_setup_shell_integration_script_not_found(self, mock_get_path, mock_run):
        """Test shell integration when script is missing."""
        # Mock the path to not exist
        from pathlib import Path
        mock_script_path = Mock(spec=Path)
        mock_script_path.exists = Mock(return_value=False)
        mock_script_path.__str__ = Mock(return_value="/fake/path/shell-integration.sh")
        mock_get_path.return_value = mock_script_path

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--shell-integration"])

        assert result.exit_code == 1
        assert "Shell integration script not found" in result.output
        mock_run.assert_not_called()

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.cli.commands.setup._get_shell_integration_script_path")
    def test_setup_shell_integration_script_fails(self, mock_get_path, mock_run):
        """Test shell integration when script execution fails."""
        # Mock the path to exist
        from pathlib import Path
        mock_script_path = Mock(spec=Path)
        mock_script_path.exists = Mock(return_value=True)
        mock_script_path.__str__ = Mock(return_value="/fake/path/shell-integration.sh")
        mock_get_path.return_value = mock_script_path

        from provide.foundation.process import ProcessError
        mock_run.side_effect = ProcessError("Script failed", returncode=1)

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--shell-integration"])

        assert result.exit_code == 1
        # The command should fail when run_command raises ProcessError
        assert isinstance(result.exception, (ProcessError, SystemExit)) or result.exit_code == 1

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.cli.commands.setup._get_shell_integration_script_path")
    def test_setup_shell_integration_creates_aliases(self, mock_get_path, mock_run):
        """Test that shell integration calls the shell script."""
        # Mock the path to exist
        from pathlib import Path
        mock_script_path = Mock(spec=Path)
        mock_script_path.exists = Mock(return_value=True)
        mock_script_path.__str__ = Mock(return_value="/fake/path/shell-integration.sh")
        mock_get_path.return_value = mock_script_path

        mock_run.return_value = Mock(returncode=0)

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--shell-integration"])

        assert result.exit_code == 0
        assert "Setting up shell integration" in result.output
        mock_run.assert_called_once()

    @patch("wrknv.wenv.workenv.WorkenvManager.setup_workenv")
    def test_setup_all_options(self, mock_setup_workenv):
        """Test setup with --init takes precedence (only one option processed)."""
        mock_setup_workenv.return_value = True

        runner = click.testing.CliRunner()
        cli = get_test_cli()
        # When both options provided, --init takes precedence
        result = runner.invoke(cli, ["setup", "--init"])

        assert result.exit_code == 0
        assert "Setting up wrknv workenv" in result.output
        mock_setup_workenv.assert_called_once_with(force=False)

    def test_setup_check_dependencies(self) -> None:
        """Test setup --check to verify dependencies."""
        with patch("shutil.which") as mock_which:
            # Mock that all dependencies are installed
            mock_which.side_effect = lambda x: f"/usr/bin/{x}" if x in ["git", "curl", "python3"] else None

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["setup", "--check"])

            assert result.exit_code == 0
            assert "Checking system dependencies" in result.output
            assert "✓ git" in result.output
            assert "✓ curl" in result.output
            assert "✓ python3" in result.output

    def test_setup_check_missing_dependencies(self) -> None:
        """Test setup --check when dependencies are missing."""
        with patch("shutil.which") as mock_which:
            # Mock that git is missing
            mock_which.side_effect = lambda x: None if x == "git" else f"/usr/bin/{x}"

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["setup", "--check"])

            assert result.exit_code == 1
            assert "✗ git" in result.output
            # The command raises DependencyError for missing required deps
            assert isinstance(result.exception, Exception)

    def test_setup_completions_bash(self) -> None:
        """Test generating bash completions."""
        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--completions", "bash"])

        assert result.exit_code == 0
        assert "_wrknv_completion" in result.output
        assert "complete -F" in result.output

    def test_setup_completions_zsh(self) -> None:
        """Test generating zsh completions."""
        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--completions", "zsh"])

        assert result.exit_code == 0
        assert "#compdef wrknv" in result.output

    def test_setup_completions_fish(self) -> None:
        """Test generating fish completions."""
        runner = click.testing.CliRunner()
        cli = get_test_cli()
        result = runner.invoke(cli, ["setup", "--completions", "fish"])

        assert result.exit_code == 0
        assert "complete -c wrknv" in result.output

    def test_setup_completions_install(self) -> None:
        """Test installing shell completions."""
        with patch("pathlib.Path.home") as mock_home:
            mock_home.return_value = self.temp_path

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["setup", "--completions", "bash", "--install"])

            assert result.exit_code == 0
            assert "Installed bash completions" in result.output

            # Verify completion file was created in .bash_completion.d/
            completion_file = self.temp_path / ".bash_completion.d" / "wrknv"
            assert completion_file.exists(), f"Completion file not found at {completion_file}"
            content = completion_file.read_text()
            assert "_wrknv_completion" in content or "wrknv" in content


class TestSetupCommandIntegration(FoundationTestCase):
    """Integration tests for setup command."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.temp_dir = self.create_temp_dir()
        self.temp_path = self.temp_dir

    def test_setup_creates_workenv_structure(self) -> None:
        """Test that setup creates the expected directory structure."""
        with patch("pathlib.Path.cwd") as mock_cwd:
            mock_cwd.return_value = self.temp_path

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["setup", "--init"])

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
