#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""Test suite for CLI lock command (extended)."""

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


class TestLockCleanCommand(FoundationTestCase):
    """Test lock clean command."""

    def test_clean_no_lockfile(self) -> None:
        """Test cleaning when no lockfile exists."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = False
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "clean"])

            assert result.exit_code == 0
            assert "No lockfile to remove" in result.output

    def test_clean_success(self) -> None:
        """Test successfully removing lockfile."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_lockfile_path.unlink = Mock()
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "clean"])

            assert result.exit_code == 0
            mock_lockfile_path.unlink.assert_called_once()

    def test_clean_error(self) -> None:
        """Test error during lockfile removal."""
        with patch("wrknv.lockfile.LockfileManager") as mock_manager_class:
            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_lockfile_path.unlink.side_effect = Exception("Permission denied")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "clean"])

            assert result.exit_code == 1
            assert "Failed to remove lockfile" in result.output


class TestLockSyncCommand(FoundationTestCase):
    """Test lock sync command."""

    def test_sync_no_lockfile(self) -> None:
        """Test syncing when no lockfile exists."""
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
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 1
            assert "No lockfile found" in result.output

    def test_sync_outdated_lockfile(self) -> None:
        """Test syncing with outdated lockfile."""
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
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 1
            assert "Lockfile is outdated" in result.output

    def test_sync_corrupted_lockfile(self) -> None:
        """Test syncing with corrupted lockfile."""
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
            mock_manager.load_lockfile.return_value = None
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 1
            assert "Failed to load lockfile" in result.output

    def test_sync_success(self) -> None:
        """Test successful sync with tools."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
            patch("wrknv.managers.factory.get_tool_manager") as mock_get_manager,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            # Create tools
            tool1 = ResolvedTool(
                name="go",
                version="1.22.0",
                resolved_from="1.22.x",
            )
            tool2 = ResolvedTool(
                name="terraform",
                version="1.7.0",
                resolved_from="latest",
            )

            mock_lockfile = Mock()
            mock_lockfile.resolved_tools = {"go": tool1, "terraform": tool2}

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.is_lockfile_valid.return_value = True
            mock_manager.load_lockfile.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            # Mock tool managers
            mock_tool_manager = Mock()
            mock_tool_manager.install_version = Mock()
            mock_get_manager.return_value = mock_tool_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 0
            assert "Installing tools from lockfile" in result.output
            assert "Installing go 1.22.0" in result.output
            assert "Installing terraform 1.7.0" in result.output

    def test_sync_skip_matrix_entries(self) -> None:
        """Test that sync skips matrix entries (tools with @ in name)."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
            patch("wrknv.managers.factory.get_tool_manager") as mock_get_manager,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            # Create tools including matrix entry
            tool1 = ResolvedTool(
                name="go",
                version="1.22.0",
                resolved_from="1.22.x",
            )
            tool2 = ResolvedTool(
                name="terraform@linux",  # Matrix entry - should be skipped
                version="1.7.0",
                resolved_from="latest",
            )

            mock_lockfile = Mock()
            mock_lockfile.resolved_tools = {"go": tool1, "terraform@linux": tool2}

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.is_lockfile_valid.return_value = True
            mock_manager.load_lockfile.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            # Mock tool manager - should only be called once for 'go'
            mock_tool_manager = Mock()
            mock_tool_manager.install_version = Mock()
            mock_get_manager.return_value = mock_tool_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 0
            assert "Installing go 1.22.0" in result.output
            assert "terraform@linux" not in result.output
            # get_tool_manager should only be called once for 'go'
            mock_get_manager.assert_called_once_with("go", mock_config)

    def test_sync_partial_failure(self) -> None:
        """Test sync with partial installation failure."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
            patch("wrknv.managers.factory.get_tool_manager") as mock_get_manager,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            # Create tools
            tool1 = ResolvedTool(
                name="go",
                version="1.22.0",
                resolved_from="1.22.x",
            )
            tool2 = ResolvedTool(
                name="terraform",
                version="1.7.0",
                resolved_from="latest",
            )

            mock_lockfile = Mock()
            mock_lockfile.resolved_tools = {"go": tool1, "terraform": tool2}

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.return_value = True
            mock_lockfile_path.__str__ = Mock(return_value="/tmp/wrknv.lock")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager.is_lockfile_valid.return_value = True
            mock_manager.load_lockfile.return_value = mock_lockfile
            mock_manager_class.return_value = mock_manager

            # Mock tool managers - second one fails
            def side_effect(tool_name, config):
                mock_tool_manager = Mock()
                if tool_name == "go":
                    mock_tool_manager.install_version = Mock()
                else:
                    mock_tool_manager.install_version.side_effect = Exception("Install failed")
                return mock_tool_manager

            mock_get_manager.side_effect = side_effect

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 0
            assert "Installing go 1.22.0" in result.output
            assert "Error installing terraform 1.7.0" in result.output

    def test_sync_general_error(self) -> None:
        """Test error during sync."""
        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_load,
            patch("wrknv.lockfile.LockfileManager") as mock_manager_class,
        ):
            mock_config = Mock()
            mock_load.return_value = mock_config

            mock_manager = Mock()
            mock_lockfile_path = Mock()
            mock_lockfile_path.exists.side_effect = Exception("Filesystem error")
            mock_manager.lockfile_path = mock_lockfile_path
            mock_manager_class.return_value = mock_manager

            runner = click.testing.CliRunner()
            cli = get_test_cli()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 1
            assert "Failed to sync from lockfile" in result.output


# 🧰🌍🔚
