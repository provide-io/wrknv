#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI tools commands - generate-env, doctor, and integration tests."""

from __future__ import annotations

from pathlib import Path

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    """Get or create the test CLI instance."""
    # Always create a fresh CLI to ensure module reloading works with mocks
    return create_cli()


class TestGenerateEnvCommand(FoundationTestCase):
    """Test generate-env command."""

    def test_generate_env_default_shell(self, tmp_path: Path) -> None:
        """Test generating env script with default shell."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.create_project_env_scripts") as mock_create,
            patch("wrknv.cli.commands.tools.safe_move"),
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            sh_path = tmp_path / "env.sh"
            ps1_path = tmp_path / "env.ps1"

            mock_create.return_value = (sh_path, ps1_path)

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["generate-env"])

            assert result.exit_code == 0
            assert "To use the environment" in result.output
            mock_create.assert_called_once()

    def test_generate_env_powershell(self, tmp_path: Path) -> None:
        """Test generating env script for PowerShell."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.create_project_env_scripts") as mock_create,
            patch("wrknv.cli.commands.tools.safe_move") as mock_move,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            sh_path = tmp_path / "env.sh"
            ps1_path = tmp_path / "env.ps1"
            output_path = tmp_path / "custom.ps1"
            sh_path.touch()
            ps1_path.touch()

            mock_create.return_value = (sh_path, ps1_path)

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["generate-env", "--shell", "powershell", str(output_path)])

            assert result.exit_code == 0
            # Should move ps1 file to custom location
            mock_move.assert_called_once()

    def test_generate_env_custom_output(self, tmp_path: Path) -> None:
        """Test generating env script to custom output path."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.create_project_env_scripts") as mock_create,
            patch("wrknv.cli.commands.tools.safe_move") as mock_move,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            sh_path = tmp_path / "env.sh"
            ps1_path = tmp_path / "env.ps1"
            output_path = tmp_path / "custom-env.sh"
            sh_path.touch()
            ps1_path.touch()

            mock_create.return_value = (sh_path, ps1_path)

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["generate-env", str(output_path)])

            assert result.exit_code == 0
            # Should move sh file to custom location
            mock_move.assert_called_once()

    def test_generate_env_file_not_found(self) -> None:
        """Test generate-env handles missing project file."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.create_project_env_scripts") as mock_create,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            # Simulate missing pyproject.toml
            mock_create.side_effect = FileNotFoundError("pyproject.toml not found")

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["generate-env"])

            assert "Error" in result.output
            assert "pyproject.toml" in result.output


class TestDoctorCommand(FoundationTestCase):
    """Test doctor command for diagnostics."""

    def test_doctor_success(self) -> None:
        """Test doctor command when all checks pass."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.run_doctor") as mock_run_doctor,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            # Doctor returns 0 for success
            mock_run_doctor.return_value = 0

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["doctor"])

            assert result.exit_code == 0
            mock_run_doctor.assert_called_once_with(False)

    def test_doctor_with_verbose(self) -> None:
        """Test doctor command with verbose flag."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.run_doctor") as mock_run_doctor,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_run_doctor.return_value = 0

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["doctor", "--verbose"])

            assert result.exit_code == 0
            # Should pass verbose=True
            mock_run_doctor.assert_called_once_with(True)

    def test_doctor_with_issues(self) -> None:
        """Test doctor command when issues are found."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.run_doctor") as mock_run_doctor,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            # Doctor returns 1 for issues found
            mock_run_doctor.return_value = 1

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["doctor"])

            assert result.exit_code == 1
            mock_run_doctor.assert_called_once()


class TestToolsCommandIntegration(FoundationTestCase):
    """Integration tests for tools commands."""

    def test_status_then_sync_workflow(self) -> None:
        """Test workflow of checking status then syncing tools."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.get_tool_manager") as mock_get_manager,
            patch("wrknv.cli.commands.tools.resolve_tool_versions") as mock_resolve,
            patch("wrknv.cli.commands.tools.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_config.get_all_tools.return_value = {
                "uv": "0.5.0",
            }
            mock_get_config.return_value = mock_config

            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager
            mock_resolve.return_value = ["0.5.0"]

            mock_lockfile = Mock()
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()

            # First check status
            result1 = runner.invoke(cli, ["status"])
            assert result1.exit_code == 0
            assert "uv" in result1.output

            # Then sync
            result2 = runner.invoke(cli, ["sync"])
            assert result2.exit_code == 0
            mock_manager.install_version.assert_called_with("0.5.0", dry_run=False)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])

# 🧰🌍🔚
