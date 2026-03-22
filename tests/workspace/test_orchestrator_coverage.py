#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.workspace.orchestrator — uncovered branches."""

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.workspace.orchestrator import WorkspaceOrchestrator


def _make_repo_info(path: Path, name: str) -> object:
    """Create a minimal RepoInfo-like object."""
    from wrknv.workspace.discovery import RepoInfo

    return RepoInfo(
        path=path,
        name=name,
        has_git=True,
        has_pyproject=True,
        detected_type="foundation-based",
        current_config=None,
    )


class TestSequentialSuccessIncrementsCounter(FoundationTestCase):
    """Line 161: sequential task succeeds → succeeded += 1."""

    def test_sequential_success_increments_succeeded(self) -> None:
        """Line 161: when result.success is True, succeeded counter is incremented."""
        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskConfig, TaskResult

        tmp = self.create_temp_dir()
        repo_path = tmp / "myrepo"
        repo_path.mkdir()
        (repo_path / "wrknv.toml").write_text('[tasks]\nbuild = "echo ok"\n')

        orchestrator = WorkspaceOrchestrator(root=tmp)
        repo = _make_repo_info(repo_path, "myrepo")

        task_config = TaskConfig(name="build", run="echo ok")
        success_result = TaskResult(
            task=task_config,
            success=True,
            exit_code=0,
            stdout="ok",
            stderr="",
            duration=0.1,
        )

        async def mock_execute(
            self: object, task: TaskConfig, **kwargs: object
        ) -> TaskResult:
            return success_result

        with mock.patch.object(TaskExecutor, "execute", new=mock_execute):
            result = asyncio.run(orchestrator.run_task_sequential("build", repos=[repo]))

        assert result.succeeded == 1
        assert result.failed == 0


class TestSequentialFailFastBreaksOnException(FoundationTestCase):
    """Line 205: fail_fast=True when exception occurs during execution → breaks out of loop."""

    def test_fail_fast_stops_after_exception(self) -> None:
        """Line 205: exception thrown + fail_fast=True → break in except block."""
        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskResult

        tmp = self.create_temp_dir()

        repo1_path = tmp / "repo1"
        repo1_path.mkdir()
        (repo1_path / "wrknv.toml").write_text('[tasks]\nbuild = "echo ok"\n')

        repo2_path = tmp / "repo2"
        repo2_path.mkdir()
        (repo2_path / "wrknv.toml").write_text('[tasks]\nbuild = "echo ok"\n')

        orchestrator = WorkspaceOrchestrator(root=tmp)
        repo1 = _make_repo_info(repo1_path, "repo1")
        repo2 = _make_repo_info(repo2_path, "repo2")

        async def raise_exc(self: object, *args: object, **kwargs: object) -> TaskResult:
            raise RuntimeError("execution failed")

        with mock.patch.object(TaskExecutor, "execute", new=raise_exc):
            result = asyncio.run(
                orchestrator.run_task_sequential("build", repos=[repo1, repo2], fail_fast=True)
            )

        # Only one repo was processed (fail_fast stopped after exception in repo1)
        assert result.failed == 1
        assert len(result.repo_results) == 1


class TestParallelSuccessIncrementsCounter(FoundationTestCase):
    """Line 317: parallel task succeeds → succeeded += 1."""

    def test_parallel_success_increments_succeeded(self) -> None:
        """Line 317: when parallel subtask result.success is True, succeeded is incremented."""
        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskConfig, TaskResult

        tmp = self.create_temp_dir()
        repo_path = tmp / "myrepo"
        repo_path.mkdir()
        (repo_path / "wrknv.toml").write_text('[tasks]\nbuild = "echo ok"\n')

        orchestrator = WorkspaceOrchestrator(root=tmp)
        repo = _make_repo_info(repo_path, "myrepo")

        task_config = TaskConfig(name="build", run="echo ok")
        success_result = TaskResult(
            task=task_config,
            success=True,
            exit_code=0,
            stdout="ok",
            stderr="",
            duration=0.1,
        )

        async def mock_execute(
            self: object, task: TaskConfig, **kwargs: object
        ) -> TaskResult:
            return success_result

        with mock.patch.object(TaskExecutor, "execute", new=mock_execute):
            result = asyncio.run(orchestrator.run_task_parallel("build", repos=[repo]))

        assert result.succeeded == 1
        assert result.failed == 0


# 🧰🌍🔚
