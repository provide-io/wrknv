#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI lock commands."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.hub_cli import create_cli
from wrknv.lockfile import Lockfile, ResolvedTool


def get_test_cli():
    """Get or create the test CLI instance."""
    return create_cli()


class TestLockGenerateCommand(FoundationTestCase):
    """Test lock generate command."""

    def test_lock_generate_success(self) -> None:
        """Test generating lockfile successfully."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "generate"])

            assert result.exit_code == 0
            assert "Generating lockfile" in result.output
            mock_lockfile.resolve_and_lock.assert_called_once_with(mock_config)

    def test_lock_generate_already_exists(self) -> None:
        """Test generating lockfile when it already exists."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "generate"])

            assert result.exit_code == 1
            assert "already exists" in result.output
            assert "Use --force" in result.output
            mock_lockfile.resolve_and_lock.assert_not_called()

    def test_lock_generate_with_force(self) -> None:
        """Test generating lockfile with --force flag."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "generate", "--force"])

            assert result.exit_code == 0
            mock_lockfile.resolve_and_lock.assert_called_once_with(mock_config)

    def test_lock_generate_error(self) -> None:
        """Test lock generate handles errors gracefully."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            mock_lockfile.resolve_and_lock.side_effect = Exception("Network error")
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "generate"])

            assert result.exit_code == 1
            assert "Failed to generate lockfile" in result.output


class TestLockCheckCommand(FoundationTestCase):
    """Test lock check command."""

    def test_lock_check_valid(self) -> None:
        """Test checking valid lockfile."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.is_lockfile_valid.return_value = True
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 0
            assert "valid and up to date" in result.output

    def test_lock_check_invalid(self) -> None:
        """Test checking invalid lockfile."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.is_lockfile_valid.return_value = False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 1
            assert "outdated or invalid" in result.output

    def test_lock_check_no_lockfile(self) -> None:
        """Test checking when no lockfile exists."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 1
            assert "No lockfile found" in result.output

    def test_lock_check_error(self) -> None:
        """Test lock check handles errors."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = side_effect=Exception("IO error")
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "check"])

            assert result.exit_code == 1
            assert "Failed to check lockfile" in result.output


class TestLockShowCommand(FoundationTestCase):
    """Test lock show command."""

    def test_lock_show_success(self) -> None:
        """Test showing lockfile contents."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls:
            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True

            # Create mock lockfile data
            lockfile_data = Lockfile(
                version="1.0",
                config_checksum="abc123",
                created_at=datetime.now().isoformat(),
                resolved_tools={
                    "uv": ResolvedTool(
                        name="uv",
                        version="0.5.0",
                        resolved_from="0.5.0",
                        checksum="xyz789",
                        installed_at=None,
                    )
                },
            )
            mock_lockfile.load_lockfile.return_value = lockfile_data
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "Config checksum:" in result.output
            assert "abc123" in result.output
            assert "uv" in result.output
            assert "0.5.0" in result.output

    def test_lock_show_no_lockfile(self) -> None:
        """Test showing when no lockfile exists."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls:
            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "No lockfile found" in result.output

    def test_lock_show_corrupted(self) -> None:
        """Test showing corrupted lockfile."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls:
            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.load_lockfile.return_value = None
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "show"])

            assert result.exit_code == 0
            assert "corrupted" in result.output


class TestLockCleanCommand(FoundationTestCase):
    """Test lock clean command."""

    def test_lock_clean_success(self, tmp_path: Path) -> None:
        """Test removing lockfile successfully."""
        cli = get_test_cli()

        lockfile_path = tmp_path / "wrknv.lock"
        lockfile_path.touch()

        with patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls:
            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = lockfile_path
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "clean"])

            assert result.exit_code == 0
            assert not lockfile_path.exists()

    def test_lock_clean_no_lockfile(self) -> None:
        """Test cleaning when no lockfile exists."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls:
            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "clean"])

            assert result.exit_code == 0
            assert "No lockfile to remove" in result.output


class TestLockSyncCommand(FoundationTestCase):
    """Test lock sync command."""

    def test_lock_sync_success(self) -> None:
        """Test syncing from valid lockfile."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
            patch("wrknv.cli.commands.lock.get_tool_manager") as mock_get_manager,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.is_lockfile_valid.return_value = True

            lockfile_data = Lockfile(
                version="1.0",
                config_checksum="abc123",
                created_at=datetime.now().isoformat(),
                resolved_tools={
                    "uv": ResolvedTool(
                        name="uv",
                        version="0.5.0",
                        resolved_from="0.5.0",
                        checksum="xyz789",
                        installed_at=None,
                    )
                },
            )
            mock_lockfile.load_lockfile.return_value = lockfile_data
            mock_lockfile_cls.return_value = mock_lockfile

            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 0
            assert "Installing tools from lockfile" in result.output
            mock_manager.install_version.assert_called_once_with("0.5.0", dry_run=False)

    def test_lock_sync_no_lockfile(self) -> None:
        """Test syncing when no lockfile exists."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 1
            assert "No lockfile found" in result.output

    def test_lock_sync_outdated_lockfile(self) -> None:
        """Test syncing with outdated lockfile."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.is_lockfile_valid.return_value = False
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 1
            assert "outdated" in result.output

    def test_lock_sync_skips_matrix_entries(self) -> None:
        """Test that sync skips matrix entries (with @ in name)."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
            patch("wrknv.cli.commands.lock.get_tool_manager") as mock_get_manager,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = Mock()
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.is_lockfile_valid.return_value = True

            lockfile_data = Lockfile(
                version="1.0",
                config_checksum="abc123",
                created_at=datetime.now().isoformat(),
                resolved_tools={
                    "go@1": ResolvedTool(  # Matrix entry - should be skipped
                        name="go@1",
                        version="1.22.0",
                        resolved_from="1.22.*",
                        checksum="xyz789",
                        installed_at=None,
                    ),
                    "uv": ResolvedTool(  # Regular entry - should be installed
                        name="uv",
                        version="0.5.0",
                        resolved_from="0.5.0",
                        checksum="abc456",
                        installed_at=None,
                    ),
                },
            )
            mock_lockfile.load_lockfile.return_value = lockfile_data
            mock_lockfile_cls.return_value = mock_lockfile

            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["lock", "sync"])

            assert result.exit_code == 0
            # Should only install uv, not go@1
            mock_manager.install_version.assert_called_once_with("0.5.0", dry_run=False)


class TestLockCommandIntegration(FoundationTestCase):
    """Integration tests for lock commands."""

    def test_generate_check_clean_workflow(self, tmp_path: Path) -> None:
        """Test workflow of generating, checking, and cleaning lockfile."""
        cli = get_test_cli()

        lockfile_path = tmp_path / "wrknv.lock"

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config") as mock_get_config,
            patch("wrknv.cli.commands.lock.LockfileManager") as mock_lockfile_cls,
        ):
            mock_config = Mock()
            mock_get_config.return_value = mock_config

            # Mock lockfile manager
            mock_lockfile = Mock()
            mock_lockfile.lockfile_path = lockfile_path
            mock_lockfile_cls.return_value = mock_lockfile

            runner = click.testing.CliRunner()

            # Generate lockfile
            mock_lockfile.lockfile_path.exists.return_value = return_value=False
            result1 = runner.invoke(cli, ["lock", "generate"])
            assert result1.exit_code == 0

            # Check lockfile
            mock_lockfile.lockfile_path.exists.return_value = return_value=True
            mock_lockfile.is_lockfile_valid.return_value = True
            result2 = runner.invoke(cli, ["lock", "check"])
            assert result2.exit_code == 0
            assert "valid" in result2.output

            # Clean lockfile
            lockfile_path.touch()  # Create actual file for clean
            result3 = runner.invoke(cli, ["lock", "clean"])
            assert result3.exit_code == 0
            assert not lockfile_path.exists()


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
