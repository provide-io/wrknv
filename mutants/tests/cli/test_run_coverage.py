#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for CLI run/tasks commands uncovered branches."""

from __future__ import annotations

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    return create_cli()


def _make_task(name, description=None, run="echo hi", depends_on=None, is_composite=False, env=None, is_default=False, namespace=None):
    t = Mock()
    t.name = name
    t.description = description
    t.run = run if not is_composite else ["task1", "task2"]
    t.depends_on = depends_on or []
    t.is_composite = is_composite
    t.env = env
    t.is_default = is_default
    t.namespace = namespace
    return t



class TestTasksListCoverage(FoundationTestCase):
    """Cover uncovered branches in _list_tasks/_show_tasks."""

    def _make_registry_with_tasks(self, tasks, flat_tasks=None):
        mock_reg = Mock()
        mock_reg.list_tasks.return_value = tasks
        mock_reg.get_flat_tasks.return_value = flat_tasks or []
        return mock_reg

    def test_tasks_with_description(self) -> None:
        """Branch 144->147: namespaced task has description -> include in display."""
        cli = get_test_cli()
        task = _make_task("build", description="Build the project", namespace="app")

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg_cls.from_repo.return_value = self._make_registry_with_tasks([task])
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["tasks"])

        assert result.exit_code == 0
        assert "Build the project" in result.output

    def test_tasks_verbose_long_command(self) -> None:
        """Line 158: command > 60 chars -> truncated with '...' in verbose mode."""
        cli = get_test_cli()
        long_cmd = "echo " + "x" * 70
        task = _make_task("build", run=long_cmd, namespace="app")

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg_cls.from_repo.return_value = self._make_registry_with_tasks([task])
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["tasks", "--verbose"])

        assert result.exit_code == 0
        assert "..." in result.output

    def test_flat_task_with_description(self) -> None:
        """Lines 166->169: flat task (no namespace) has description -> include in display."""
        cli = get_test_cli()
        # namespace=None → flat task
        flat_task = _make_task("fmt", description="Format code", namespace=None)

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg_cls.from_repo.return_value = self._make_registry_with_tasks([flat_task])
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["tasks"])

        assert result.exit_code == 0
        assert "Format code" in result.output

    def test_flat_task_verbose_composite(self) -> None:
        """Lines 173-174: flat composite task verbose -> show sub-tasks."""
        cli = get_test_cli()
        flat_task = _make_task("all", is_composite=True, namespace=None)

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg_cls.from_repo.return_value = self._make_registry_with_tasks([flat_task])
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["tasks", "--verbose"])

        assert result.exit_code == 0

    def test_flat_task_verbose_long_command(self) -> None:
        """Lines 177->179: flat task verbose with long command -> truncated."""
        cli = get_test_cli()
        long_cmd = "echo " + "y" * 70
        flat_task = _make_task("run-all", run=long_cmd, namespace=None)

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg_cls.from_repo.return_value = self._make_registry_with_tasks([flat_task])
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["tasks", "--verbose"])

        assert result.exit_code == 0
        assert "..." in result.output


class TestRunInfoCoverage(FoundationTestCase):
    """Cover info mode branches in run command."""

    def test_run_info_task_with_description(self) -> None:
        """Lines 63-64: task with description -> echo description."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg = Mock()
            task = _make_task("build", description="Build everything")
            mock_reg.get_task.return_value = task
            mock_reg_cls.from_repo.return_value = mock_reg
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["run", "build", "--info"])

        assert result.exit_code == 0
        assert "Build everything" in result.output

    def test_run_info_task_no_description(self) -> None:
        """Branch 63->65: task with no description -> skip echo."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg = Mock()
            task = _make_task("build", description=None)
            mock_reg.get_task.return_value = task
            mock_reg_cls.from_repo.return_value = mock_reg
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["run", "build", "--info"])

        assert result.exit_code == 0

    def test_flat_task_verbose_short_command(self) -> None:
        """Branch 177->179: short command (≤60 chars) in verbose -> no truncation."""
        cli = get_test_cli()
        flat_task = _make_task("lint", run="echo short", namespace=None)

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_reg_cls:
            mock_reg_cls.from_repo.return_value = Mock()
            mock_reg_cls.from_repo.return_value.list_tasks.return_value = [flat_task]
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["tasks", "--verbose"])

        assert result.exit_code == 0
        assert "..." not in result.output


class TestRunCommandEnvParsing(FoundationTestCase):
    """Lines 47-48: valid KEY=VALUE env var parsing (direct call, bypasses hub tuple issue)."""

    def test_valid_env_var_parsed(self) -> None:
        """Lines 47-48: env=('FOO=bar',) → key split at '=', stored in env_dict."""
        from wrknv.cli.commands.run import run_command

        mock_registry = Mock()
        mock_registry.get_task.return_value = None  # info mode exits early

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_cls:
            mock_cls.from_repo.return_value = mock_registry
            run_command("test", env=("FOO=bar",), info=True)

        mock_registry.get_task.assert_called_once_with("test")

    def test_env_value_with_equals_preserved(self) -> None:
        """Lines 47-48: split('=', 1) keeps trailing '=' in value part."""
        from wrknv.cli.commands.run import run_command

        captured_env: dict[str, str] = {}

        mock_registry = Mock()

        result_mock = Mock()
        result_mock.success = True
        result_mock.stdout = ""
        result_mock.stderr = ""
        result_mock.duration = 0.1
        result_mock.exit_code = 0

        async def mock_run_task(*args: object, **kwargs: object) -> Mock:  # type: ignore[misc]
            captured_env.update(kwargs.get("env", {}))
            return result_mock

        mock_registry.run_task = mock_run_task

        with patch("wrknv.cli.commands.run.TaskRegistry") as mock_cls:
            mock_cls.from_repo.return_value = mock_registry
            run_command("test", env=("TOKEN=abc=def",))

        assert captured_env.get("TOKEN") == "abc=def"


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])

# 🧰🌍🔚
