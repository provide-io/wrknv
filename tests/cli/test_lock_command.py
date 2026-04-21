#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""Test suite for CLI lock command."""

from __future__ import annotations

from unittest.mock import Mock, patch

import click.testing
from provide.testkit import FoundationTestCase

from wrknv.cli.hub_cli import create_cli
from wrknv.lockfile import ResolvedTool


def get_test_cli():
    """Create a fresh test CLI instance.

    Always creates new instance to avoid race conditions with pytest-xdist.
    Module reloading in create_cli() invalidates patches if instances are cached.
    """
    return create_cli()


class TestLockGenerateCommand(FoundationTestCase):
    """Test lock generate command."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.temp_dir = self.create_temp_dir()

    def test_generate_success(self) -> None:
        """Test generating lockfile successfully."""
        with (
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = False
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path

            mock_lockfile = Mock()
            mock_lockfile.resolved_tools = {"go": Mock(), "terraform": Mock()}
            mock_manager.resolve_and_lock.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "generate"])

            assert result.exit_code == 0
            assert "Generating lockfile" in result.output
            mock_manager.resolve_and_lock.assert_called_once_with(mock_config)

    def test_generate_already_exists_no_force(self) -> None:
        """Test generating lockfile when it already exists without --force."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "generate"])

            assert result.exit_code == 1
            assert "Lockfile already exists" in result.output
            assert "Use --force to overwrite" in result.output
            mock_manager.resolve_and_lock.assert_not_called()

    def test_generate_with_force(self) -> None:
        """Test generating lockfile with --force flag."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path

            mock_lockfile = Mock()
            mock_lockfile.resolved_tools = {"go": Mock()}
            mock_manager.resolve_and_lock.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "generate", "--force"])

            assert result.exit_code == 0
            assert "Generating lockfile" in result.output
            mock_manager.resolve_and_lock.assert_called_once_with(mock_config)

    def test_generate_error(self) -> None:
        """Test error during lockfile generation."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = False
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.resolve_and_lock.side_effect = Exception("Resolution failed")
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "generate"])

            assert result.exit_code == 1
            assert "Failed to generate lockfile" in result.output
            assert "Resolution failed" in result.output


class TestLockCheckCommand(FoundationTestCase):
    """Test lock check command."""

    def test_check_no_lockfile(self) -> None:
        """Test checking when no lockfile exists."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = False
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 1
            assert "No lockfile found" in result.output
            assert "wrknv lock generate" in result.output

    def test_check_valid_lockfile(self) -> None:
        """Test checking with valid lockfile."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.is_lockfile_valid.return_value = True
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 0
            assert "Lockfile is valid" in result.output

    def test_check_invalid_lockfile(self) -> None:
        """Test checking with invalid/outdated lockfile."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.is_lockfile_valid.return_value = False
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 1
            assert "Lockfile is outdated or invalid" in result.output
            assert "wrknv lock generate --force" in result.output

    def test_check_error(self) -> None:
        """Test error during lockfile check."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.is_lockfile_valid.side_effect = Exception("Validation error")
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 1
            assert "Failed to check lockfile" in result.output


class TestLockShowCommand(FoundationTestCase):
    """Test lock show command."""

    def test_show_no_lockfile(self) -> None:
        """Test showing lockfile when none exists."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = False
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "No lockfile found" in result.output

    def test_show_corrupted_lockfile(self) -> None:
        """Test showing corrupted lockfile."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.load_lockfile.return_value = None
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "Failed to load lockfile (corrupted?)" in result.output

    def test_show_lockfile_with_tools(self) -> None:
        """Test showing lockfile with tools."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path

            # Create mock lockfile with tools
            tool1 = ResolvedTool(
                name="go",
                version="1.22.0",
                resolved_from="1.22.x",
                installed_at="2024-01-01T00:00:00",
            )
            tool2 = ResolvedTool(
                name="terraform",
                version="1.7.0",
                resolved_from="latest",
                installed_at=None,  # Not installed
            )

            mock_lockfile = Mock()
            mock_lockfile.config_checksum = "abc123def456"
            mock_lockfile.created_at = "2024-01-01T00:00:00"
            mock_lockfile.wrknv_version = "0.3.0"
            mock_lockfile.resolved_tools = {"go": tool1, "terraform": tool2}

            mock_manager.load_lockfile.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "Config checksum: abc123def456" in result.output
            assert "Tools: 2" in result.output
            assert "go: 1.22.0" in result.output
            assert "terraform: 1.7.0" in result.output
            assert "installed" in result.output
            assert "not installed" in result.output

    def test_show_lockfile_without_tools(self) -> None:
        """Test showing lockfile without any tools."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path

            mock_lockfile = Mock()
            mock_lockfile.config_checksum = "abc123"
            mock_lockfile.created_at = "2024-01-01T00:00:00"
            mock_lockfile.wrknv_version = "0.3.0"
            mock_lockfile.resolved_tools = {}

            mock_manager.load_lockfile.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "Tools: 0" in result.output

    def test_show_error(self) -> None:
        """Test error during lockfile show."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.side_effect = Exception("Filesystem error")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 1
            assert "Failed to show lockfile" in result.output


# 🧰🌍🔚
