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


class TestToolsCommandsBranchCoverage(FoundationTestCase):
    """Cover uncovered branches in tools commands."""

    def _make_mock_config(self, tools=None):
        cfg = Mock()
        cfg.get_all_tools.return_value = tools or {"uv": "0.5.0"}
        return cfg

    def test_sync_no_lock(self) -> None:
        """Branch 103->107: sync with lock=False skips locking (direct call)."""
        from wrknv.cli.commands.tools import sync_command

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.get_tool_manager") as mock_mgr_fn,
            patch("wrknv.cli.commands.tools.resolve_tool_versions", return_value=["0.5.0"]),
            patch("wrknv.cli.commands.tools.LockfileManager") as mock_lf_cls,
        ):
            mock_get_config.return_value = self._make_mock_config()
            mock_mgr = Mock()
            mock_mgr_fn.return_value = mock_mgr

            sync_command(lock=False)

            # With lock=False, resolve_and_lock should NOT be called
            mock_lf_cls.return_value.resolve_and_lock.assert_not_called()

    def test_status_list_version_resolved_differs(self) -> None:
        """Line 62: list version where resolved != input patterns -> arrow notation."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.get_tool_manager") as mock_mgr_fn,
            patch("wrknv.cli.commands.tools.resolve_tool_versions", return_value=["0.5.1", "0.6.0"]),
        ):
            cfg = Mock()
            cfg.get_all_tools.return_value = {"uv": [">=0.5", ">=0.6"]}
            mock_get_config.return_value = cfg
            mock_mgr_fn.return_value = Mock()

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["status"])
        assert result.exit_code == 0

    def test_status_list_version_resolve_empty(self) -> None:
        """Branch 58->81: list version where resolved_versions is empty."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.get_tool_manager") as mock_mgr_fn,
            patch("wrknv.cli.commands.tools.resolve_tool_versions", return_value=[]),
        ):
            cfg = Mock()
            cfg.get_all_tools.return_value = {"uv": [">=0.5"]}
            mock_get_config.return_value = cfg
            mock_mgr_fn.return_value = Mock()

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["status"])
        assert result.exit_code == 0

    def test_status_list_version_exception(self) -> None:
        """Line 65: exception resolving list versions -> debug log, continue."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.tools.get_tool_manager") as mock_mgr_fn,
            patch("wrknv.cli.commands.tools.resolve_tool_versions", side_effect=Exception("err")),
        ):
            cfg = Mock()
            cfg.get_all_tools.return_value = {"uv": [">=0.5"]}
            mock_get_config.return_value = cfg
            mock_mgr_fn.return_value = Mock()

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["status"])
        assert result.exit_code == 0

    def test_status_none_version(self) -> None:
        """Branch 70->81: version is None -> 'Not specified', skip resolve."""
        cli = get_test_cli()
        with patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config:
            cfg = Mock()
            cfg.get_all_tools.return_value = {"go": None}
            mock_get_config.return_value = cfg

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["status"])
        assert result.exit_code == 0
        assert "Not specified" in result.output


class TestGenerateEnvNoMoveBranches(FoundationTestCase):
    """Lines 164->169 and 166->169: branches where output already equals target path.

    Hub passes pathlib.Path parameters as strings, so these branches are only reachable
    by calling generate_env_command directly with Path objects.
    """

    def test_powershell_output_equals_ps1_path_no_move(self, tmp_path: Path) -> None:
        """Line 164->169: shell=powershell, output == ps1_path → safe_move NOT called."""
        import pathlib

        from wrknv.cli.commands.tools import generate_env_command

        ps1_path = pathlib.Path("env.ps1")
        sh_path = pathlib.Path("env.sh")

        with (
            patch(
                "wrknv.cli.commands.tools.create_project_env_scripts",
                return_value=(sh_path, ps1_path),
            ),
            patch("wrknv.cli.commands.tools.safe_move") as mock_move,
            patch("wrknv.cli.commands.tools.echo_info"),
        ):
            generate_env_command(
                output=ps1_path,
                shell="powershell",
                project_dir=pathlib.Path(),
            )

        mock_move.assert_not_called()

    def test_sh_output_equals_sh_path_no_move(self, tmp_path: Path) -> None:
        """Line 166->169: shell=sh, output == sh_path → safe_move NOT called."""
        import pathlib

        from wrknv.cli.commands.tools import generate_env_command

        sh_path = pathlib.Path("env.sh")
        ps1_path = pathlib.Path("env.ps1")

        with (
            patch(
                "wrknv.cli.commands.tools.create_project_env_scripts",
                return_value=(sh_path, ps1_path),
            ),
            patch("wrknv.cli.commands.tools.safe_move") as mock_move,
            patch("wrknv.cli.commands.tools.echo_info"),
        ):
            generate_env_command(
                output=sh_path,
                shell="sh",
                project_dir=pathlib.Path(),
            )

        mock_move.assert_not_called()


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])

# 🧰🌍🔚
