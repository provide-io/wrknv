#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for task registry."""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from wrknv.tasks.registry import TaskRegistry
from wrknv.tasks.schema import TaskConfig


@pytest.fixture
def fixtures_dir() -> Path:
    """Get the fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def simple_tasks_toml(fixtures_dir: Path) -> Path:
    """Get path to simple_tasks.toml fixture."""
    return fixtures_dir / "simple_tasks.toml"


@pytest.fixture
def complex_tasks_toml(fixtures_dir: Path) -> Path:
    """Get path to complex_tasks.toml fixture."""
    return fixtures_dir / "complex_tasks.toml"


@pytest.fixture
def mixed_tasks_toml(fixtures_dir: Path) -> Path:
    """Get path to mixed_tasks.toml fixture."""
    return fixtures_dir / "mixed_tasks.toml"


class TestTaskRegistryLoading:
    """Tests for loading tasks from TOML files."""

    def test_from_repo_with_simple_tasks(self, tmp_path: Path) -> None:
        """Test loading simple task definitions from wrknv.toml."""
        # Create a wrknv.toml with simple tasks
        toml_content = """
[tasks]
test = "uv run pytest tests/"
lint = "uv run ruff check src/"
"""
        (tmp_path / "wrknv.toml").write_text(toml_content)

        registry = TaskRegistry.from_repo(tmp_path)

        assert len(registry.tasks) == 2
        assert "test" in registry.tasks
        assert "lint" in registry.tasks

        test_task = registry.get_task("test")
        assert test_task is not None
        assert test_task.name == "test"
        assert test_task.run == "uv run pytest tests/"
        assert not test_task.is_composite

    def test_from_repo_with_complex_tasks(self, tmp_path: Path) -> None:
        """Test loading complex task definitions with full config."""
        toml_content = """
[tasks.build]
run = "uv build"
description = "Build the package"
env = { PYTHONPATH = "src" }
"""
        (tmp_path / "wrknv.toml").write_text(toml_content)

        registry = TaskRegistry.from_repo(tmp_path)

        assert len(registry.tasks) == 1
        build_task = registry.get_task("build")
        assert build_task is not None
        assert build_task.name == "build"
        assert build_task.run == "uv build"
        assert build_task.description == "Build the package"
        assert build_task.env == {"PYTHONPATH": "src"}

    def test_from_repo_with_composite_tasks(self, tmp_path: Path) -> None:
        """Test loading composite tasks that run other tasks."""
        toml_content = """
[tasks.quality]
run = ["lint", "typecheck"]
description = "Run quality checks"
"""
        (tmp_path / "wrknv.toml").write_text(toml_content)

        registry = TaskRegistry.from_repo(tmp_path)

        quality_task = registry.get_task("quality")
        assert quality_task is not None
        assert quality_task.is_composite
        assert quality_task.run == ["lint", "typecheck"]

    def test_from_repo_without_wrknv_toml(self, tmp_path: Path) -> None:
        """Test loading from directory without wrknv.toml returns empty registry."""
        registry = TaskRegistry.from_repo(tmp_path)

        assert registry.repo_path == tmp_path
        assert len(registry.tasks) == 0

    def test_from_repo_with_mixed_tasks(self, tmp_path: Path) -> None:
        """Test loading a mix of simple and complex tasks."""
        toml_content = """
[tasks]
simple = "echo hello"

[tasks.complex]
run = "echo complex"
description = "A complex task"
env = { VAR = "value" }

[tasks.composite]
run = ["simple", "complex"]
"""
        (tmp_path / "wrknv.toml").write_text(toml_content)

        registry = TaskRegistry.from_repo(tmp_path)

        assert len(registry.tasks) == 3
        assert not registry.get_task("simple").is_composite  # type: ignore[union-attr]
        assert not registry.get_task("complex").is_composite  # type: ignore[union-attr]
        assert registry.get_task("composite").is_composite  # type: ignore[union-attr]


class TestTaskRegistryAPI:
    """Tests for TaskRegistry API methods."""

    def test_get_task_returns_task_when_exists(self) -> None:
        """Test get_task returns TaskConfig when task exists."""
        task = TaskConfig(name="test", run="pytest")
        registry = TaskRegistry(repo_path=Path(), tasks={"test": task})

        result = registry.get_task("test")

        assert result == task

    def test_get_task_returns_none_when_not_exists(self) -> None:
        """Test get_task returns None when task doesn't exist."""
        registry = TaskRegistry(repo_path=Path(), tasks={})

        result = registry.get_task("nonexistent")

        assert result is None

    def test_list_tasks_returns_all_tasks(self) -> None:
        """Test list_tasks returns all registered tasks."""
        task1 = TaskConfig(name="test", run="pytest")
        task2 = TaskConfig(name="lint", run="ruff")
        registry = TaskRegistry(
            repo_path=Path(),
            tasks={"test": task1, "lint": task2},
        )

        tasks = registry.list_tasks()

        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks

    def test_list_tasks_returns_empty_list_when_no_tasks(self) -> None:
        """Test list_tasks returns empty list when registry is empty."""
        registry = TaskRegistry(repo_path=Path(), tasks={})

        tasks = registry.list_tasks()

        assert tasks == []


class TestTaskRegistryCoverage:
    """Coverage for uncovered branches in registry.py."""

    def test_from_repo_no_tasks_section(self, tmp_path: Path) -> None:
        """Line 55->59: wrknv.toml with no [tasks] section → empty tasks dict."""
        (tmp_path / "wrknv.toml").write_text('[project_name]\nfoo = "bar"\n')
        registry = TaskRegistry.from_repo(tmp_path)
        assert len(registry.tasks) == 0

    def test_from_repo_with_exports_no_toml(self, tmp_path: Path) -> None:
        """Line 84: from_repo_with_exports with no wrknv.toml → empty registry."""
        registry = TaskRegistry.from_repo_with_exports(tmp_path)
        assert len(registry.tasks) == 0

    def test_from_repo_with_exports_no_tasks_section(self, tmp_path: Path) -> None:
        """Line 92->96: from_repo_with_exports with toml but no [tasks] section."""
        (tmp_path / "wrknv.toml").write_text('[project]\nname = "test"\n')
        registry = TaskRegistry.from_repo_with_exports(tmp_path)
        assert len(registry.tasks) == 0

    def test_from_repo_with_exports_no_tasks_list(self, tmp_path: Path) -> None:
        """Line 99->103: export section exists but tasks key is missing."""
        (tmp_path / "wrknv.toml").write_text(
            '[tasks]\nbuild = "make"\n\n[export]\ndescription = "pkg"\n'
        )
        registry = TaskRegistry.from_repo_with_exports(tmp_path)
        assert len(registry.tasks) == 1

    def test_parse_task_list_value(self, tmp_path: Path) -> None:
        """Line 194: simple list task (composite = ["a", "b"]) parsed as composite."""
        (tmp_path / "wrknv.toml").write_text(
            "[tasks]\nall = [\"build\", \"test\"]\n"
        )
        registry = TaskRegistry.from_repo(tmp_path)
        task = registry.get_task("all")
        assert task is not None
        assert task.is_composite

    def test_parse_task_dict_with_null_run_returns_none(self) -> None:
        """Line 200: dict task with run=None → _parse_task returns None."""
        # Call _parse_task directly with a dict that has 'run' but it's None
        result = TaskRegistry._parse_task("mytask", {"run": None, "description": "foo"})
        assert result is None

    def test_parse_task_invalid_value_returns_none(self, tmp_path: Path) -> None:
        """Line 218: task value is not str/list/dict → returns None → task skipped."""
        (tmp_path / "wrknv.toml").write_text("[tasks]\nmy_task = 42\n")
        registry = TaskRegistry.from_repo(tmp_path)
        assert registry.get_task("my_task") is None

    def test_run_task_not_found_raises(self, tmp_path: Path) -> None:
        """Lines 347-348: run_task → resolve_task ValueError → TaskNotFoundError."""
        from wrknv.errors import TaskNotFoundError

        registry = TaskRegistry(repo_path=tmp_path, tasks={})
        with pytest.raises(TaskNotFoundError):
            asyncio.run(registry.run_task("nonexistent"))

    def test_resolve_task_parent_default(self, tmp_path: Path) -> None:
        """Lines 286-287: parent has _default task → resolved with child as arg."""
        default_task = TaskConfig(name="parent._default", run="echo default")
        registry = TaskRegistry(
            repo_path=tmp_path,
            tasks={"parent._default": default_task},
        )
        # "parent.child" doesn't exist; parent doesn't exist; parent._default does
        task, args = registry.resolve_task("parent.child")
        assert task is default_task
        assert args == ["child"]

    def test_parallel_composite_all_succeed_empty_stderr(self, tmp_path: Path) -> None:
        """Line 441: all parallel subtasks succeed → combined_stderr = ''."""
        from unittest.mock import patch

        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskResult

        parallel_task = TaskConfig(name="all", run=["sub1", "sub2"], parallel=True)
        sub1 = TaskConfig(name="sub1", run="echo 1")
        sub2 = TaskConfig(name="sub2", run="echo 2")
        registry = TaskRegistry(
            repo_path=tmp_path,
            tasks={"all": parallel_task, "sub1": sub1, "sub2": sub2},
        )

        async def mock_execute(self: object, task: TaskConfig, **kwargs: object) -> TaskResult:
            return TaskResult(
                task=task, success=True, exit_code=0, stdout="ok", stderr="", duration=0.0
            )

        with patch.object(TaskExecutor, "execute", new=mock_execute):
            result = asyncio.run(registry.run_task("all"))
        assert result.success is True
        assert result.stderr == ""

    def test_parallel_subtask_exception_creates_error_result(self, tmp_path: Path) -> None:
        """Lines 404, 414-415: exception in parallel subtask → error TaskResult."""
        from unittest.mock import patch

        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskResult

        parallel_task = TaskConfig(name="all", run=["sub1"], parallel=True)
        sub1 = TaskConfig(name="sub1", run="echo 1")
        registry = TaskRegistry(
            repo_path=tmp_path,
            tasks={"all": parallel_task, "sub1": sub1},
        )

        async def raise_exc(self: object, *args: object, **kwargs: object) -> TaskResult:
            raise RuntimeError("boom")

        with patch.object(TaskExecutor, "execute", new=raise_exc):
            result = asyncio.run(registry.run_task("all"))
        assert result.success is False

    def test_parallel_failure_no_stderr_skips_append(self, tmp_path: Path) -> None:
        """Line 437->436: failed parallel subtask with empty stderr → skip append, loop continues."""
        from unittest.mock import patch

        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskResult

        parallel_task = TaskConfig(name="all", run=["sub1", "sub2"], parallel=True)
        sub1 = TaskConfig(name="sub1", run="echo 1")
        sub2 = TaskConfig(name="sub2", run="echo 2")
        registry = TaskRegistry(
            repo_path=tmp_path,
            tasks={"all": parallel_task, "sub1": sub1, "sub2": sub2},
        )

        async def fail_no_stderr(self: object, task: TaskConfig, **kwargs: object) -> TaskResult:
            return TaskResult(
                task=task, success=False, exit_code=1, stdout="", stderr="", duration=0.0
            )

        with patch.object(TaskExecutor, "execute", new=fail_no_stderr):
            result = asyncio.run(registry.run_task("all"))
        assert result.success is False

    def test_sequential_composite_all_succeed(self, tmp_path: Path) -> None:
        """Lines 466->475, 470->466: sequential composite where all subtasks succeed."""
        from unittest.mock import patch

        from wrknv.tasks.executor import TaskExecutor
        from wrknv.tasks.schema import TaskResult

        seq_task = TaskConfig(name="all", run=["sub1", "sub2"])  # parallel=False by default
        sub1 = TaskConfig(name="sub1", run="echo 1")
        sub2 = TaskConfig(name="sub2", run="echo 2")
        registry = TaskRegistry(
            repo_path=tmp_path,
            tasks={"all": seq_task, "sub1": sub1, "sub2": sub2},
        )

        async def succeed(self: object, task: TaskConfig, **kwargs: object) -> TaskResult:
            return TaskResult(
                task=task, success=True, exit_code=0, stdout="ok", stderr="", duration=0.0
            )

        with patch.object(TaskExecutor, "execute", new=succeed):
            result = asyncio.run(registry.run_task("all"))
        assert result.success is True

    def test_from_repo_with_exports_export_name_not_in_tasks(self, tmp_path: Path) -> None:
        """Line 104->103: exported task name not in tasks dict → if False → loop continues."""
        (tmp_path / "wrknv.toml").write_text(
            '[tasks]\nbuild = "make"\n\n[export]\ntasks = ["nonexistent"]\n'
        )
        registry = TaskRegistry.from_repo_with_exports(tmp_path)
        build_task = registry.get_task("build")
        assert build_task is not None
        assert not build_task.is_exported


# 🧰🌍🔚
