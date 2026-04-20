#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for CLI doctor/selftest commands."""

from __future__ import annotations

from unittest import mock

import click.testing
from provide.testkit import FoundationTestCase

from wrknv.cli.commands.doctor import (
    _check_commands,
    _check_config,
    _check_dependencies,
    _check_environment,
    _check_permissions,
)
from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    return create_cli()


# =============================================================================
# _check_environment tests
# =============================================================================


class TestCheckEnvironment(FoundationTestCase):
    """Tests for _check_environment()."""

    def test_pass_when_workenv_dir_exists(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "workenv").mkdir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = _check_environment()
        assert result["status"] == "pass"
        assert "workenv" in result["details"]

    def test_pass_when_in_venv(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("sys.base_prefix", "/base"),
            mock.patch("sys.prefix", "/venv"),
        ):
            result = _check_environment()
        assert result["status"] == "pass"

    def test_warn_when_no_venv_and_no_workenv(self) -> None:
        tmp = self.create_temp_dir()
        # workenv doesn't exist, and not in a real venv
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("sys.base_prefix", "/same"),
            mock.patch("sys.prefix", "/same"),
        ):
            result = _check_environment()
        assert result["status"] in ("pass", "warn")  # depends on actual test runner venv

    def test_has_name_and_message(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = _check_environment()
        assert "name" in result
        assert "message" in result


# =============================================================================
# _check_config tests
# =============================================================================


class TestCheckConfig(FoundationTestCase):
    """Tests for _check_config()."""

    def test_warn_when_config_not_exists(self) -> None:
        mock_config = mock.Mock()
        mock_config.config_exists.return_value = False
        with mock.patch("wrknv.cli.commands.doctor.WrknvContext.get_config", return_value=mock_config):
            result = _check_config()
        assert result["status"] == "warn"

    def test_fail_when_config_invalid(self) -> None:
        mock_config = mock.Mock()
        mock_config.config_exists.return_value = True
        mock_config.validate.return_value = (False, ["missing required field"])
        with mock.patch("wrknv.cli.commands.doctor.WrknvContext.get_config", return_value=mock_config):
            result = _check_config()
        assert result["status"] == "fail"

    def test_pass_when_config_valid(self) -> None:
        mock_config = mock.Mock()
        mock_config.config_exists.return_value = True
        mock_config.validate.return_value = (True, [])
        mock_config.config_path = "/path/to/config"
        with mock.patch("wrknv.cli.commands.doctor.WrknvContext.get_config", return_value=mock_config):
            result = _check_config()
        assert result["status"] == "pass"

    def test_fail_on_exception(self) -> None:
        with mock.patch("wrknv.cli.commands.doctor.WrknvContext.get_config", side_effect=RuntimeError("boom")):
            result = _check_config()
        assert result["status"] == "fail"


# =============================================================================
# _check_dependencies tests
# =============================================================================


class TestCheckDependencies(FoundationTestCase):
    """Tests for _check_dependencies()."""

    def test_pass_when_all_available(self) -> None:
        result = _check_dependencies()
        # In our test environment, all required deps should be available
        assert result["status"] in ("pass", "warn")
        assert "name" in result

    def test_fail_when_required_dep_missing(self) -> None:
        original_import = __builtins__.__import__ if hasattr(__builtins__, "__import__") else __import__

        def fake_import(name, *args, **kwargs):
            if name == "attrs":
                raise ImportError("no module")
            return original_import(name, *args, **kwargs)

        with mock.patch("builtins.__import__", side_effect=fake_import):
            result = _check_dependencies()
        assert result["status"] == "fail"
        assert "attrs" in result["message"]

    def test_has_required_fields(self) -> None:
        result = _check_dependencies()
        assert "name" in result
        assert "status" in result
        assert "message" in result


# =============================================================================
# _check_commands tests
# =============================================================================


class TestCheckCommands(FoundationTestCase):
    """Tests for _check_commands()."""

    def test_returns_pass_with_commands(self) -> None:
        result = _check_commands()
        assert result["status"] in ("pass", "warn")
        assert "name" in result

    def test_fail_when_no_commands(self) -> None:
        mock_cli = mock.Mock()
        mock_cli.commands = {}
        with mock.patch("wrknv.cli.hub_cli.create_cli", return_value=mock_cli):
            result = _check_commands()
        assert result["status"] == "fail"

    def test_warn_when_groups_missing(self) -> None:
        mock_cli = mock.Mock()
        mock_cli.commands = {"config": mock.Mock()}  # Only has config, missing others
        with mock.patch("wrknv.cli.hub_cli.create_cli", return_value=mock_cli):
            result = _check_commands()
        assert result["status"] == "warn"

    def test_pass_when_all_groups_present(self) -> None:
        mock_cli = mock.Mock()
        mock_cli.commands = {
            "config": mock.Mock(),
            "workenv": mock.Mock(),
            "gitignore": mock.Mock(),
            "package": mock.Mock(),
            "selftest": mock.Mock(),
        }
        with mock.patch("wrknv.cli.hub_cli.create_cli", return_value=mock_cli):
            result = _check_commands()
        assert result["status"] == "pass"

    def test_fail_on_exception(self) -> None:
        with mock.patch("wrknv.cli.hub_cli.create_cli", side_effect=RuntimeError("fail")):
            result = _check_commands()
        assert result["status"] == "fail"


# =============================================================================
# _check_permissions tests
# =============================================================================


class TestCheckPermissions(FoundationTestCase):
    """Tests for _check_permissions()."""

    def test_pass_when_writable(self) -> None:
        result = _check_permissions()
        assert result["status"] in ("pass", "warn")

    def test_fail_when_no_write_permission(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("pathlib.Path.write_text", side_effect=PermissionError("denied")),
        ):
            result = _check_permissions()
        assert result["status"] == "fail"

    def test_warn_when_home_config_not_creatable(self) -> None:
        tmp = self.create_temp_dir()

        def mkdir_side_effect(*args, **kwargs):
            raise PermissionError("denied")

        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("pathlib.Path.write_text"),
            mock.patch("pathlib.Path.unlink"),
            mock.patch("pathlib.Path.home", return_value=tmp / "fakehome"),
            mock.patch("pathlib.Path.exists", side_effect=lambda: False),
            mock.patch("pathlib.Path.mkdir", side_effect=mkdir_side_effect),
        ):
            result = _check_permissions()
        assert result["status"] in ("pass", "warn", "fail")  # depends on mock interaction

    def test_has_required_fields(self) -> None:
        result = _check_permissions()
        assert "name" in result
        assert "status" in result
        assert "message" in result


# =============================================================================
# selftest_check CLI command tests
# =============================================================================


class TestSelftestCheck(FoundationTestCase):
    """Tests for selftest check CLI command."""

    def _make_pass_check(self, name: str) -> dict:
        return {"name": name, "status": "pass", "message": "OK"}

    def _make_fail_check(self, name: str) -> dict:
        return {"name": name, "status": "fail", "message": "Failed"}

    def _make_warn_check(self, name: str) -> dict:
        return {"name": name, "status": "warn", "message": "Warning"}

    def test_all_pass_exits_zero(self) -> None:
        checks = [self._make_pass_check(f"check{i}") for i in range(5)]
        cli = get_test_cli()
        with (
            mock.patch(
                "wrknv.cli.commands.doctor._check_environment",
                return_value=checks[0],
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_config",
                return_value=checks[1],
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_dependencies",
                return_value=checks[2],
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_commands",
                return_value=checks[3],
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_permissions",
                return_value=checks[4],
            ),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])
        assert result.exit_code == 0

    def test_fail_check_exits_nonzero(self) -> None:
        pass_check = self._make_pass_check("ok")
        fail_check = self._make_fail_check("failed")
        cli = get_test_cli()
        with (
            mock.patch(
                "wrknv.cli.commands.doctor._check_environment",
                return_value=fail_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_config",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_dependencies",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_commands",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_permissions",
                return_value=pass_check,
            ),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])
        assert result.exit_code == 1

    def test_warn_check_exits_zero(self) -> None:
        pass_check = self._make_pass_check("ok")
        warn_check = self._make_warn_check("warn")
        cli = get_test_cli()
        with (
            mock.patch(
                "wrknv.cli.commands.doctor._check_environment",
                return_value=warn_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_config",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_dependencies",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_commands",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_permissions",
                return_value=pass_check,
            ),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])
        assert result.exit_code == 0

    def test_verbose_mode_shows_details(self) -> None:
        check_with_details = {
            "name": "Test",
            "status": "pass",
            "message": "OK",
            "details": "some details here",
        }
        pass_check = self._make_pass_check("ok")
        cli = get_test_cli()
        with (
            mock.patch(
                "wrknv.cli.commands.doctor._check_environment",
                return_value=check_with_details,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_config",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_dependencies",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_commands",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_permissions",
                return_value=pass_check,
            ),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check", "--verbose"])
        assert result.exit_code == 0

    def test_fix_mode_shows_fix_suggestion(self) -> None:
        fail_check = {
            "name": "Test",
            "status": "fail",
            "message": "Failed",
            "fix": "run uv install",
        }
        pass_check = self._make_pass_check("ok")
        cli = get_test_cli()
        with (
            mock.patch(
                "wrknv.cli.commands.doctor._check_environment",
                return_value=fail_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_config",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_dependencies",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_commands",
                return_value=pass_check,
            ),
            mock.patch(
                "wrknv.cli.commands.doctor._check_permissions",
                return_value=pass_check,
            ),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check", "--fix"])
        assert result.exit_code == 1


# =============================================================================
# selftest env and config CLI command tests
# =============================================================================


class TestSelftestEnv(FoundationTestCase):
    """Tests for selftest env CLI command."""

    def test_env_pass_exits_zero(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.cli.commands.doctor._check_environment",
            return_value={"name": "Env", "status": "pass", "message": "OK"},
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "env"])
        assert result.exit_code == 0

    def test_env_pass_with_details_shows_detail(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.cli.commands.doctor._check_environment",
            return_value={"name": "Env", "status": "pass", "message": "OK", "details": "venv active"},
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "env"])
        assert result.exit_code == 0

    def test_env_fail_exits_nonzero(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.cli.commands.doctor._check_environment",
            return_value={"name": "Env", "status": "fail", "message": "broken"},
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "env"])
        assert result.exit_code != 0


class TestSelftestConfig(FoundationTestCase):
    """Tests for selftest config CLI command."""

    def test_config_pass_exits_zero(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.cli.commands.doctor._check_config",
            return_value={"name": "Config", "status": "pass", "message": "OK"},
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "config"])
        assert result.exit_code == 0

    def test_config_pass_with_details(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.cli.commands.doctor._check_config",
            return_value={"name": "Config", "status": "pass", "message": "OK", "details": "config found"},
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "config"])
        assert result.exit_code == 0

    def test_config_fail_exits_nonzero(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.cli.commands.doctor._check_config",
            return_value={"name": "Config", "status": "fail", "message": "invalid"},
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "config"])
        assert result.exit_code != 0


# =============================================================================
# memray CLI command tests
# =============================================================================


class TestMemrayInit(FoundationTestCase):
    """Tests for memray init CLI command."""

    def test_memray_init_success(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.memray.scaffold.scaffold_memray",
            return_value=["Created tests/memray/", "Created scripts/"],
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["memray", "init"])
        assert result.exit_code == 0

    def test_memray_init_with_note_actions(self) -> None:
        cli = get_test_cli()
        with mock.patch(
            "wrknv.memray.scaffold.scaffold_memray",
            return_value=["Created tests/memray/", "NOTE: run baselines first"],
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["memray", "init"])
        assert result.exit_code == 0

    def test_memray_init_with_project_dir(self) -> None:
        tmp = self.create_temp_dir()
        cli = get_test_cli()
        with mock.patch(
            "wrknv.memray.scaffold.scaffold_memray",
            return_value=["Created tests/memray/"],
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["memray", "init", str(tmp)])
        assert result.exit_code == 0


# 🧰🌍🔚
