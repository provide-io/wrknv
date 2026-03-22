#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.cli.commands.doctor — uncovered branches."""

from __future__ import annotations

from unittest.mock import patch

import click.testing
from provide.testkit import FoundationTestCase

from wrknv.cli.hub_cli import create_cli


class TestDoctorUnknownStatusBranch(FoundationTestCase):
    """Line 56->61: check result with status other than pass/fail/warn."""

    def test_unknown_status_skips_to_verbose_check(self) -> None:
        """Line 56->61: elif 'warn' is False → goes to line 61 (verbose check)."""
        cli = create_cli()
        skip_check = {"name": "Custom", "status": "skip", "message": "skipped"}
        pass_check = {"name": "Pass", "status": "pass", "message": "ok"}
        with (
            patch("wrknv.cli.commands.doctor._check_environment", return_value=skip_check),
            patch("wrknv.cli.commands.doctor._check_config", return_value=pass_check),
            patch("wrknv.cli.commands.doctor._check_dependencies", return_value=pass_check),
            patch("wrknv.cli.commands.doctor._check_commands", return_value=pass_check),
            patch("wrknv.cli.commands.doctor._check_permissions", return_value=pass_check),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["selftest", "check"])
        assert result.exit_code == 0


class TestCheckDependenciesException(FoundationTestCase):
    """Lines 243-244: except Exception in _check_dependencies."""

    def test_exception_returns_fail_status(self) -> None:
        """Lines 243-244: exception in _check_dependencies → fail dict returned."""
        from wrknv.cli.commands.doctor import _check_dependencies

        with patch("wrknv.cli.commands.doctor.find_spec", side_effect=RuntimeError("spec error")):
            result = _check_dependencies()
        assert result["status"] == "fail"
        assert "Dependency check failed" in result["message"]


class TestCheckPermissionsException(FoundationTestCase):
    """Lines 323-324: except Exception in _check_permissions."""

    def test_exception_returns_fail_status(self) -> None:
        """Lines 323-324: exception in _check_permissions → fail dict returned."""
        from wrknv.cli.commands.doctor import _check_permissions

        with patch("pathlib.Path.home", side_effect=RuntimeError("home error")):
            result = _check_permissions()
        assert result["status"] == "fail"
        assert "Permission check failed" in result["message"]


# 🧰🌍🔚
