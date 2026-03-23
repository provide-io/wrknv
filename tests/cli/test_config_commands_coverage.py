#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.cli.commands.config — uncovered branches."""

from __future__ import annotations

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    return create_cli()


class TestConfigValidateVerboseException(FoundationTestCase):
    """Line 118->122: if verbose: branch inside except Exception in config.validate."""

    def test_validate_exception_with_verbose_shows_traceback(self) -> None:
        """Line 118->119: exception in config.validate + --verbose → traceback echoed."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
        ):
            mock_config = Mock()
            mock_config.config_exists.return_value = True
            mock_config.validate.side_effect = Exception("unexpected config error")
            mock_get_config.return_value = mock_config

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["config", "validate", "--verbose"])

        assert result.exit_code == 1
        assert "Validation error" in result.output
        assert "Traceback" in result.output

    def test_validate_exception_without_verbose_no_traceback(self) -> None:
        """Line 118->122: exception in config.validate, verbose=False → no traceback (False branch)."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
        ):
            mock_config = Mock()
            mock_config.config_exists.return_value = True
            mock_config.validate.side_effect = Exception("config parse error")
            mock_get_config.return_value = mock_config

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["config", "validate"])

        assert result.exit_code == 1
        assert "Validation error" in result.output
        assert "Traceback" not in result.output


# 🧰🌍🔚
