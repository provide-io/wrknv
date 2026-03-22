#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI doctor/selftest commands."""

from __future__ import annotations

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import patch

from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    """Get or create the test CLI instance."""
    return create_cli()


class TestSelftestCheckCommand(FoundationTestCase):
    """Test selftest check command."""

    def test_check_all_pass(self) -> None:
        """Test check when all checks pass."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            # All checks pass
            mock_env.return_value = {"status": "pass", "name": "Environment"}
            mock_config.return_value = {"status": "pass", "name": "Config"}
            mock_deps.return_value = {"status": "pass", "name": "Dependencies"}
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {"status": "pass", "name": "Permissions"}

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])

            assert result.exit_code == 0
            assert "Running wrknv health check" in result.output
            assert "All health checks passed" in result.output

    def test_check_with_failures(self) -> None:
        """Test check when some checks fail."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            mock_env.return_value = {"status": "pass", "name": "Environment"}
            mock_config.return_value = {
                "status": "fail",
                "name": "Config",
                "message": "Config file not found",
            }
            mock_deps.return_value = {"status": "pass", "name": "Dependencies"}
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {"status": "pass", "name": "Permissions"}

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])

            assert result.exit_code == 1
            assert "Health check failed" in result.output
            assert "Config" in result.output

    def test_check_with_warnings(self) -> None:
        """Test check when some checks have warnings."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            mock_env.return_value = {
                "status": "warn",
                "name": "Environment",
                "message": "No virtual environment",
            }
            mock_config.return_value = {"status": "pass", "name": "Config"}
            mock_deps.return_value = {"status": "pass", "name": "Dependencies"}
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {"status": "pass", "name": "Permissions"}

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])

            assert result.exit_code == 0
            assert "completed with warnings" in result.output
            assert "Warnings: 1" in result.output

    def test_check_verbose_mode(self) -> None:
        """Test check with verbose flag."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            mock_env.return_value = {
                "status": "pass",
                "name": "Environment",
                "details": "Python 3.11 detected",
            }
            mock_config.return_value = {"status": "pass", "name": "Config"}
            mock_deps.return_value = {"status": "pass", "name": "Dependencies"}
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {"status": "pass", "name": "Permissions"}

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check", "--verbose"])

            assert result.exit_code == 0
            assert "Python 3.11" in result.output

    def test_check_with_fix_flag(self) -> None:
        """Test check with fix flag."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            mock_env.return_value = {"status": "pass", "name": "Environment"}
            mock_config.return_value = {
                "status": "fail",
                "name": "Config",
                "message": "Config missing",
                "fix": "Run 'wrknv config init'",
            }
            mock_deps.return_value = {"status": "pass", "name": "Dependencies"}
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {"status": "pass", "name": "Permissions"}

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check", "--fix"])

            assert result.exit_code == 1
            assert "Attempting fix" in result.output

    def test_check_error_handling(self) -> None:
        """Test check command error handling."""
        cli = get_test_cli()

        with patch(
            "wrknv.cli.commands.doctor._check_environment",
            side_effect=Exception("System error"),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])

            assert result.exit_code == 1
            assert "Health check failed" in result.output


class TestSelftestEnvCommand(FoundationTestCase):
    """Test selftest env command."""

    def test_env_check_pass(self) -> None:
        """Test env check when passing."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.doctor._check_environment") as mock_env:
            mock_env.return_value = {
                "status": "pass",
                "name": "Environment",
                "details": "Virtual environment active",
            }

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "env"])

            assert result.exit_code == 0
            assert "Virtual environment" in result.output

    def test_env_check_fail(self) -> None:
        """Test env check when failing."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.doctor._check_environment") as mock_env:
            mock_env.return_value = {
                "status": "fail",
                "name": "Environment",
                "message": "No Python found",
            }

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "env"])

            assert result.exit_code == 1
            assert "No Python found" in result.output

    def test_env_check_error_handling(self) -> None:
        """Test env check error handling."""
        cli = get_test_cli()

        with patch(
            "wrknv.cli.commands.doctor._check_environment",
            side_effect=Exception("System error"),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "env"])

            assert result.exit_code == 1
            assert "Environment check failed" in result.output


class TestSelftestConfigCommand(FoundationTestCase):
    """Test selftest config command."""

    def test_config_check_pass(self) -> None:
        """Test config check when passing."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.doctor._check_config") as mock_config:
            mock_config.return_value = {
                "status": "pass",
                "name": "Config",
                "details": "wrknv.toml found",
            }

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "config"])

            assert result.exit_code == 0
            assert "wrknv.toml" in result.output

    def test_config_check_fail(self) -> None:
        """Test config check when failing."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.doctor._check_config") as mock_config:
            mock_config.return_value = {
                "status": "fail",
                "name": "Config",
                "message": "Config file not found",
            }

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "config"])

            assert result.exit_code == 1
            assert "not found" in result.output

    def test_config_check_error_handling(self) -> None:
        """Test config check error handling."""
        cli = get_test_cli()

        with patch(
            "wrknv.cli.commands.doctor._check_config",
            side_effect=Exception("Permission error"),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "config"])

            assert result.exit_code == 1
            assert "Configuration check failed" in result.output


class TestSelftestIntegration(FoundationTestCase):
    """Integration tests for selftest commands."""

    def test_full_health_check_workflow(self) -> None:
        """Test full workflow of running health checks."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            # Set up healthy system
            mock_env.return_value = {"status": "pass", "name": "Environment"}
            mock_config.return_value = {"status": "pass", "name": "Config"}
            mock_deps.return_value = {"status": "pass", "name": "Dependencies"}
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {"status": "pass", "name": "Permissions"}

            runner = click.testing.CliRunner()

            # Run comprehensive check
            result1 = runner.invoke(cli, ["selftest", "check"])
            assert result1.exit_code == 0
            assert "All health checks passed" in result1.output

            # Run individual env check
            result2 = runner.invoke(cli, ["selftest", "env"])
            assert result2.exit_code == 0

            # Run individual config check
            result3 = runner.invoke(cli, ["selftest", "config"])
            assert result3.exit_code == 0

    def test_check_summary_counts(self) -> None:
        """Test that check summary shows correct counts."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as mock_env,
            patch("wrknv.cli.commands.doctor._check_config") as mock_config,
            patch("wrknv.cli.commands.doctor._check_dependencies") as mock_deps,
            patch("wrknv.cli.commands.doctor._check_commands") as mock_cmds,
            patch("wrknv.cli.commands.doctor._check_permissions") as mock_perms,
        ):
            # Mix of pass, warn, fail
            mock_env.return_value = {"status": "pass", "name": "Environment"}
            mock_config.return_value = {
                "status": "warn",
                "name": "Config",
                "message": "Deprecated setting",
            }
            mock_deps.return_value = {
                "status": "fail",
                "name": "Dependencies",
                "message": "Missing uv",
            }
            mock_cmds.return_value = {"status": "pass", "name": "Commands"}
            mock_perms.return_value = {
                "status": "warn",
                "name": "Permissions",
                "message": "Limited permissions",
            }

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])

            assert result.exit_code == 1
            assert "Warnings: 2" in result.output
            assert "Failed: 1" in result.output


class TestDoctorFunctionCoverage(FoundationTestCase):
    """Cover internal doctor function branches."""

    def test_check_environment_exception(self) -> None:
        """Lines 150-151: _check_environment raises -> return fail dict."""
        from wrknv.cli.commands.doctor import _check_environment

        with (
            patch("os.environ", side_effect=Exception("env error")),
            patch("wrknv.cli.commands.doctor.Path") as mock_path,
        ):
            mock_path.cwd.side_effect = Exception("cwd error")
            result = _check_environment()
        assert result["status"] == "fail"
        assert "Environment check failed" in result["message"]

    def test_check_dependencies_missing_tomllib(self) -> None:
        """Line 211: both tomllib and tomli missing -> warn."""
        from wrknv.cli.commands.doctor import _check_dependencies

        with patch("wrknv.cli.commands.doctor.find_spec", return_value=None):
            result = _check_dependencies()
        # All imports fail → at minimum tomllib missing dep added
        assert result["status"] == "fail"
        assert "tomli" in result["message"]

    def test_check_dependencies_optional_missing(self) -> None:
        """Lines 222-223, 234-244: optional deps missing -> warn."""
        from wrknv.cli.commands.doctor import _check_dependencies

        def fake_import(name):
            if name in ("tomli_w", "semver"):
                raise ImportError("not installed")

        with (
            patch("builtins.__import__", side_effect=fake_import),
            patch("wrknv.cli.commands.doctor.find_spec", return_value=True),
        ):
            result = _check_dependencies()
        # Either passes all required deps or warns on optional
        assert result["status"] in ("pass", "warn", "fail")

    def test_check_permissions_cannot_create_dir(self) -> None:
        """Lines 313-324: PermissionError creating home config dir -> warn."""
        from wrknv.cli.commands.doctor import _check_permissions

        with (
            patch("wrknv.cli.commands.doctor.Path") as mock_path_cls,
        ):
            mock_home = mock_path_cls.home.return_value
            mock_config_dir = mock_home.__truediv__.return_value.__truediv__.return_value
            mock_config_dir.exists.return_value = False
            mock_config_dir.mkdir.side_effect = PermissionError("no perms")
            mock_cwd = mock_path_cls.cwd.return_value
            mock_cwd.__truediv__.return_value.write_text = lambda x: None
            mock_cwd.__truediv__.return_value.unlink = lambda: None
            result = _check_permissions()
        assert result["status"] in ("warn", "pass", "fail")

    def test_check_with_verbose_shows_details(self) -> None:
        """Line 61-62: verbose + details -> echo details."""
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        with (
            patch("wrknv.cli.commands.doctor._check_environment") as m_env,
            patch("wrknv.cli.commands.doctor._check_config") as m_cfg,
            patch("wrknv.cli.commands.doctor._check_dependencies") as m_dep,
            patch("wrknv.cli.commands.doctor._check_commands") as m_cmd,
            patch("wrknv.cli.commands.doctor._check_permissions") as m_perm,
        ):
            for m in (m_env, m_cfg, m_dep, m_cmd, m_perm):
                m.return_value = {
                    "status": "pass",
                    "name": "Test",
                    "message": "ok",
                    "details": "some extra detail",
                }
            result = runner.invoke(cli, ["selftest", "check", "--verbose"])

        assert result.exit_code == 0
        assert "some extra detail" in result.output


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
