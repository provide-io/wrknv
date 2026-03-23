#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for CLI container commands."""

from __future__ import annotations

from unittest import mock

import click.testing
from provide.testkit import FoundationTestCase

from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    return create_cli()


def _mock_config():
    return mock.Mock()


class TestContainerStatus(FoundationTestCase):
    """Tests for container status command."""

    def test_status_command(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.container_status") as mock_status,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "status"])
        assert result.exit_code == 0
        mock_status.assert_called_once_with(cfg)


class TestContainerBuild(FoundationTestCase):
    """Tests for container build command."""

    def test_build_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.build_container", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "build"])
        assert result.exit_code == 0

    def test_build_failure_exits_nonzero(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.build_container", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "build"])
        assert result.exit_code != 0

    def test_build_with_rebuild_flag(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.build_container", return_value=True) as mock_build,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "build", "--rebuild"])
        assert result.exit_code == 0
        mock_build.assert_called_once_with(cfg, rebuild=True)


class TestContainerStart(FoundationTestCase):
    """Tests for container start command."""

    def test_start_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.start_container", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "start"])
        assert result.exit_code == 0

    def test_start_failure_exits_nonzero(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.start_container", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "start"])
        assert result.exit_code != 0


class TestContainerStop(FoundationTestCase):
    """Tests for container stop command."""

    def test_stop_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.stop_container", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "stop"])
        assert result.exit_code == 0

    def test_stop_failure_exits_nonzero(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.stop_container", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "stop"])
        assert result.exit_code != 0


class TestContainerRestart(FoundationTestCase):
    """Tests for container restart command."""

    def test_restart_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.restart_container", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "restart"])
        assert result.exit_code == 0

    def test_restart_failure_exits_nonzero(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.restart_container", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "restart"])
        assert result.exit_code != 0


class TestContainerEnter(FoundationTestCase):
    """Tests for container enter command."""

    def test_enter_default(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.enter_container") as mock_enter,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "enter"])
        assert result.exit_code == 0
        mock_enter.assert_called_once()

    def test_enter_with_command(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.enter_container") as mock_enter,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "enter", "ls -la"])
        assert result.exit_code == 0
        call_kwargs = mock_enter.call_args.kwargs
        assert call_kwargs["command"] == ["ls", "-la"]


class TestContainerLogs(FoundationTestCase):
    """Tests for container logs command."""

    def test_logs_default(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.container_logs") as mock_logs,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "logs"])
        assert result.exit_code == 0
        mock_logs.assert_called_once()


class TestContainerClean(FoundationTestCase):
    """Tests for container clean command."""

    def test_clean_cancelled(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.clean_container") as mock_clean,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "clean"], input="n\n")
        assert result.exit_code == 0
        mock_clean.assert_not_called()

    def test_clean_confirmed_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.clean_container", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "clean"], input="y\n")
        assert result.exit_code == 0

    def test_clean_confirmed_failure(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.clean_container", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "clean"], input="y\n")
        assert result.exit_code != 0


class TestContainerRebuild(FoundationTestCase):
    """Tests for container rebuild command."""

    def test_rebuild_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.rebuild_container", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "rebuild"])
        assert result.exit_code == 0

    def test_rebuild_failure_exits_nonzero(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.rebuild_container", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "rebuild"])
        assert result.exit_code != 0


class TestContainerVolumes(FoundationTestCase):
    """Tests for container volumes subcommands."""

    def test_volumes_list(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.list_volumes") as mock_list,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "list"])
        assert result.exit_code == 0
        mock_list.assert_called_once_with(cfg)

    def test_volumes_backup_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.backup_volumes", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "backup"])
        assert result.exit_code == 0

    def test_volumes_backup_failure(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.backup_volumes", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "backup"])
        assert result.exit_code != 0

    def test_volumes_restore_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.restore_volumes", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "restore"])
        assert result.exit_code == 0

    def test_volumes_restore_failure(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.restore_volumes", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "restore"])
        assert result.exit_code != 0

    def test_volumes_clean_success(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.clean_volumes", return_value=True),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "clean"])
        assert result.exit_code == 0

    def test_volumes_clean_failure(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.clean_volumes", return_value=False),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "volumes", "clean"])
        assert result.exit_code != 0


class TestContainerShell(FoundationTestCase):
    """Tests for container shell command (hidden, tested directly)."""

    def test_shell_command(self) -> None:
        from wrknv.cli.commands.container import container_shell_command

        cfg = _mock_config()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.enter_container") as mock_enter,
        ):
            container_shell_command()
        call_kwargs = mock_enter.call_args.kwargs
        assert call_kwargs["shell"] == "/bin/bash"


class TestContainerExec(FoundationTestCase):
    """Tests for container exec command."""

    def test_exec_with_command(self) -> None:
        cfg = _mock_config()
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg),
            mock.patch("wrknv.cli.commands.container.enter_container") as mock_enter,
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "exec", "ls -la"])
        assert result.exit_code == 0
        call_kwargs = mock_enter.call_args.kwargs
        assert call_kwargs["command"] == ["ls", "-la"]


class TestContainerCommandFunctions(FoundationTestCase):
    """Cover remaining branches in container command functions."""

    def test_container_status_docker_unavailable(self) -> None:
        """Line 77: docker not available -> red status."""
        from wrknv.container.commands import container_status

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.status.return_value = {
                "docker_available": False,
                "image_found": False,
                "container_exists": False,
                "container_running": False,
                "container_info": None,
            }
            mock_mgr.full_image = "myimg:latest"
            mock_mgr.container_name = "mycontainer"
            mock_mgr_cls.return_value = mock_mgr
            # Should not raise
            container_status(None)

    def test_container_status_no_container(self) -> None:
        """Line 99: container doesn't exist -> 'Not Created' status."""
        from wrknv.container.commands import container_status

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.status.return_value = {
                "docker_available": True,
                "image_found": True,
                "container_exists": False,
                "container_running": False,
                "container_info": None,
            }
            mock_mgr.full_image = "myimg:latest"
            mock_mgr.container_name = "mycontainer"
            mock_mgr_cls.return_value = mock_mgr
            container_status(None)

    def test_rebuild_clean_fails(self) -> None:
        """Line 153: rebuild when clean fails -> return False."""
        from wrknv.container.commands import rebuild_container

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.clean.return_value = False
            mock_mgr_cls.return_value = mock_mgr
            result = rebuild_container(None)
        assert result is False

    def test_rebuild_build_fails(self) -> None:
        """Line 157: rebuild when build_image fails -> return False."""
        from wrknv.container.commands import rebuild_container

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.clean.return_value = True
            mock_mgr.build_image.return_value = False
            mock_mgr_cls.return_value = mock_mgr
            result = rebuild_container(None)
        assert result is False

    def test_list_volumes_gb_size(self) -> None:
        """Line 186: volume size > 1GB -> GB format."""
        from wrknv.container.commands import list_volumes

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.list_volumes.return_value = [
                {
                    "name": "data",
                    "path": "/mnt/data",
                    "size": 2 * 1024 * 1024 * 1024,
                    "exists": True,
                    "files": 100,
                }
            ]
            mock_mgr_cls.return_value = mock_mgr
            # Should not raise
            list_volumes(None)

    def test_restore_volumes_exception(self) -> None:
        """Lines 249-251: exception during restore -> return False."""
        from wrknv.container.commands import restore_volumes

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.restore_volumes.side_effect = RuntimeError("restore failed")
            mock_mgr_cls.return_value = mock_mgr
            result = restore_volumes(None, "/tmp/backup.tar.gz")
        assert result is False

    def test_restore_volumes_fails_no_force(self) -> None:
        """Line 245: restore fails without force -> show hint."""
        from wrknv.container.commands import restore_volumes

        with mock.patch("wrknv.container.commands.ContainerManager") as mock_mgr_cls:
            mock_mgr = mock.Mock()
            mock_mgr.restore_volumes.return_value = False
            mock_mgr_cls.return_value = mock_mgr
            result = restore_volumes(None, "/tmp/backup.tar.gz", force=False)
        assert result is False

    def test_container_exec_empty_command(self) -> None:
        """Lines 345-347: exec with empty command -> error exit."""
        cfg = _mock_config()
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.container.WrknvContext.get_config", return_value=cfg):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["container", "exec", ""])
        assert result.exit_code != 0


# 🧰🌍🔚
