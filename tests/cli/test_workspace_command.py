#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for CLI workspace commands."""

from __future__ import annotations

from unittest import mock

import click.testing
from provide.testkit import FoundationTestCase

from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    return create_cli()


class TestWorkspaceInit(FoundationTestCase):
    """Tests for workspace init command."""

    def test_init_success(self) -> None:
        mock_config = mock.Mock()
        mock_config.template_source = None
        mock_manager = mock.Mock()
        mock_manager.init_workspace.return_value = mock_config
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "init"])
        assert result.exit_code == 0

    def test_init_with_template_source(self) -> None:
        mock_source = mock.Mock()
        mock_source.location = "/some/template"
        mock_config = mock.Mock()
        mock_config.template_source = mock_source
        mock_manager = mock.Mock()
        mock_manager.init_workspace.return_value = mock_config
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "init"])
        assert result.exit_code == 0

    def test_init_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.init_workspace.side_effect = RuntimeError("init failed")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "init"])
        assert result.exit_code != 0


class TestWorkspaceAdd(FoundationTestCase):
    """Tests for workspace add command."""

    def test_add_repo_success(self) -> None:
        mock_config = mock.Mock()
        mock_config.repos = [mock.Mock(), mock.Mock()]
        mock_manager = mock.Mock()
        mock_manager.add_repo.return_value = mock_config
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "add", "/path/to/repo"])
        assert result.exit_code == 0

    def test_add_repo_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.add_repo.side_effect = RuntimeError("add failed")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "add", "/path/to/repo"])
        assert result.exit_code != 0


class TestWorkspaceRemove(FoundationTestCase):
    """Tests for workspace remove command."""

    def test_remove_repo_success(self) -> None:
        mock_config = mock.Mock()
        mock_config.repos = [mock.Mock()]
        mock_manager = mock.Mock()
        mock_manager.remove_repo.return_value = mock_config
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "remove", "my-repo"])
        assert result.exit_code == 0

    def test_remove_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.remove_repo.side_effect = RuntimeError("not found")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "remove", "my-repo"])
        assert result.exit_code != 0


class TestWorkspaceList(FoundationTestCase):
    """Tests for workspace list command."""

    def test_list_no_config(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.load_config.return_value = None
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "list"])
        assert result.exit_code == 0

    def test_list_with_repos(self) -> None:
        repo1 = mock.Mock()
        repo1.path = "/repo1"
        repo1.template_profile = "default"
        repo1.features = ["python", "docker"]
        mock_config = mock.Mock()
        mock_config.repos = [repo1]
        mock_manager = mock.Mock()
        mock_manager.load_config.return_value = mock_config
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "list"])
        assert result.exit_code == 0

    def test_list_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.load_config.side_effect = RuntimeError("load failed")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "list"])
        assert result.exit_code != 0


class TestWorkspaceStatus(FoundationTestCase):
    """Tests for workspace status command."""

    def test_status_with_error_in_result(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.get_workspace_status.return_value = {"error": "no config"}
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "status"])
        assert result.exit_code == 0

    def test_status_success_minimal(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.get_workspace_status.return_value = {
            "repos_discovered": 3,
            "sync_strategy": "git",
        }
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "status"])
        assert result.exit_code == 0

    def test_status_with_type_distribution(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.get_workspace_status.return_value = {
            "repos_discovered": 3,
            "sync_strategy": "git",
            "type_distribution": {"python": 2, "terraform": 1},
        }
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "status"])
        assert result.exit_code == 0

    def test_status_with_issues(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.get_workspace_status.return_value = {
            "repos_discovered": 1,
            "sync_strategy": "git",
            "issues": ["missing config", "stale lock"],
        }
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "status"])
        assert result.exit_code == 0

    def test_status_with_template_source(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.get_workspace_status.return_value = {
            "repos_discovered": 1,
            "sync_strategy": "git",
            "template_source": {"location": "/templates", "type": "local"},
        }
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "status"])
        assert result.exit_code == 0

    def test_status_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.get_workspace_status.side_effect = RuntimeError("status failed")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "status"])
        assert result.exit_code != 0


class TestWorkspaceSync(FoundationTestCase):
    """Tests for workspace sync command."""

    def test_sync_all_success(self) -> None:

        mock_manager = mock.Mock()
        mock_manager.sync_all = mock.AsyncMock(
            return_value={"repo1": {"success": True}, "repo2": {"success": True}}
        )
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync"])
        assert result.exit_code == 0

    def test_sync_all_with_failures(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_all = mock.AsyncMock(
            return_value={"repo1": {"success": True}, "repo2": {"success": False, "error": "failed"}}
        )
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync"])
        assert result.exit_code == 0

    def test_sync_dry_run(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_all = mock.AsyncMock(return_value={"repo1": {"success": True}})
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync", "--dry-run"])
        assert result.exit_code == 0

    def test_sync_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_all = mock.AsyncMock(side_effect=RuntimeError("sync failed"))
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync"])
        assert result.exit_code != 0


class TestWorkspaceSyncRepo(FoundationTestCase):
    """Tests for workspace sync-repo command."""

    def test_sync_repo_success(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_repo = mock.AsyncMock(return_value={"my-repo": {"success": True}})
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync-repo", "my-repo"])
        assert result.exit_code == 0

    def test_sync_repo_dry_run_success(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_repo = mock.AsyncMock(return_value={"my-repo": {"success": True}})
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync-repo", "my-repo", "--dry-run"])
        assert result.exit_code == 0

    def test_sync_repo_failure(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_repo = mock.AsyncMock(return_value={"my-repo": {"success": False, "error": "fail"}})
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync-repo", "my-repo"])
        assert result.exit_code == 0

    def test_sync_repo_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.sync_repo = mock.AsyncMock(side_effect=RuntimeError("sync failed"))
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "sync-repo", "my-repo"])
        assert result.exit_code != 0


class TestWorkspaceDrift(FoundationTestCase):
    """Tests for workspace drift command."""

    def test_drift_no_drift(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.check_drift.return_value = {"drift_detected": False}
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "drift"])
        assert result.exit_code == 0

    def test_drift_detected_with_repos(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.check_drift.return_value = {
            "drift_detected": True,
            "drifted_repos": ["repo1", "repo2"],
        }
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "drift"])
        assert result.exit_code == 0

    def test_drift_detected_no_drifted_repos_key(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.check_drift.return_value = {"drift_detected": True}
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "drift"])
        assert result.exit_code == 0

    def test_drift_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.check_drift.side_effect = RuntimeError("check failed")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "drift"])
        assert result.exit_code != 0


class TestWorkspaceSetup(FoundationTestCase):
    """Tests for workspace setup command."""

    def test_setup_success(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.setup_workspace.return_value = {"success_count": 3, "total_count": 3}
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "setup"])
        assert result.exit_code == 0

    def test_setup_generate_only(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.setup_workspace.return_value = {"success_count": 2, "total_count": 2}
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "setup", "--generate-only"])
        assert result.exit_code == 0

    def test_setup_with_failures(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.setup_workspace.return_value = {
            "success_count": 1,
            "total_count": 2,
            "failures": {"repo2": "permission denied"},
        }
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "setup"])
        assert result.exit_code == 0

    def test_setup_propagates_exception(self) -> None:
        mock_manager = mock.Mock()
        mock_manager.setup_workspace.side_effect = RuntimeError("setup failed")
        cli = get_test_cli()
        with mock.patch("wrknv.cli.commands.workspace.WorkspaceManager", return_value=mock_manager):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "setup"])
        assert result.exit_code != 0


class TestWorkspaceRun(FoundationTestCase):
    """Tests for workspace run command."""

    def test_run_all_success(self) -> None:
        mock_result = mock.Mock()
        mock_result.task_name = "test"
        mock_result.total_repos = 2
        mock_result.succeeded = 2
        mock_result.failed = 0
        mock_result.skipped = 0
        mock_result.duration = 1.5
        mock_result.get_failed_repos.return_value = []
        mock_orchestrator = mock.Mock()
        mock_orchestrator.run_task = mock.AsyncMock(return_value=mock_result)
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.workspace.WorkspaceOrchestrator", return_value=mock_orchestrator),
            mock.patch("wrknv.cli.commands.workspace.Path"),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "run", "test"])
        assert result.exit_code == 0

    def test_run_with_failures_exits_nonzero(self) -> None:
        failed_repo = mock.Mock()
        failed_repo.exit_code = 1
        mock_result = mock.Mock()
        mock_result.task_name = "test"
        mock_result.total_repos = 2
        mock_result.succeeded = 1
        mock_result.failed = 1
        mock_result.skipped = 0
        mock_result.duration = 2.0
        mock_result.get_failed_repos.return_value = ["repo2"]
        mock_result.repo_results = {"repo2": failed_repo}
        mock_orchestrator = mock.Mock()
        mock_orchestrator.run_task = mock.AsyncMock(return_value=mock_result)
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.workspace.WorkspaceOrchestrator", return_value=mock_orchestrator),
            mock.patch("wrknv.cli.commands.workspace.Path"),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "run", "test"])
        assert result.exit_code == 1

    def test_run_propagates_exception(self) -> None:
        mock_orchestrator = mock.Mock()
        mock_orchestrator.run_task = mock.AsyncMock(side_effect=RuntimeError("orchestrator failed"))
        cli = get_test_cli()
        with (
            mock.patch("wrknv.cli.commands.workspace.WorkspaceOrchestrator", return_value=mock_orchestrator),
            mock.patch("wrknv.cli.commands.workspace.Path"),
        ):
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["workspace", "run", "test"])
        assert result.exit_code != 0


# 🧰🌍🔚
