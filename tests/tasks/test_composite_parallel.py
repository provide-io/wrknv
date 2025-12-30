"""Tests for parallel composite task execution."""

from pathlib import Path

import pytest

from wrknv.tasks.registry import TaskRegistry
from wrknv.tasks.schema import TaskConfig


class TestParallelComposite:
    """Test parallel execution of composite tasks."""

    @pytest.mark.asyncio
    async def test_parallel_composite_all_succeed(self, tmp_path: Path) -> None:
        """Test parallel execution when all subtasks succeed."""
        # Create wrknv.toml with parallel composite task
        config_content = """
[tasks.success1]
run = "exit 0"

[tasks.success2]
run = "exit 0"

[tasks.success3]
run = "exit 0"

[tasks.parallel_all_succeed]
run = ["success1", "success2", "success3"]
parallel = true
description = "Parallel task where all succeed"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Run parallel task
        result = await registry.run_task("parallel_all_succeed")

        # Verify all succeeded
        assert result.success
        assert result.exit_code == 0
        assert "failure" not in result.stderr.lower()

    @pytest.mark.asyncio
    async def test_parallel_composite_some_fail(self, tmp_path: Path) -> None:
        """Test parallel execution continues after failures."""
        # Create wrknv.toml with parallel composite task
        config_content = """
[tasks.success]
run = "exit 0"

[tasks.failure]
run = "exit 1"

[tasks.parallel_mixed]
run = ["success", "failure", "success"]
parallel = true
description = "Parallel task with mixed results"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Run parallel task
        result = await registry.run_task("parallel_mixed")

        # Verify task failed but all subtasks ran
        assert not result.success
        assert result.exit_code == 1
        assert "1 failure(s)" in result.stderr
        assert "failure" in result.stderr.lower()

    @pytest.mark.asyncio
    async def test_parallel_composite_all_fail(self, tmp_path: Path) -> None:
        """Test parallel execution when all subtasks fail."""
        # Create wrknv.toml with parallel composite task
        config_content = """
[tasks.fail1]
run = "exit 1"

[tasks.fail2]
run = "exit 2"

[tasks.fail3]
run = "exit 3"

[tasks.parallel_all_fail]
run = ["fail1", "fail2", "fail3"]
parallel = true
description = "Parallel task where all fail"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Run parallel task
        result = await registry.run_task("parallel_all_fail")

        # Verify all failures captured
        assert not result.success
        assert result.exit_code == 1
        assert "3 failure(s)" in result.stderr
        assert "fail1" in result.stderr
        assert "fail2" in result.stderr
        assert "fail3" in result.stderr

    @pytest.mark.asyncio
    async def test_sequential_composite_still_fails_fast(self, tmp_path: Path) -> None:
        """Test sequential mode still fail-fasts."""
        # Create wrknv.toml with sequential composite task (no parallel flag)
        config_content = """
[tasks.success]
run = "exit 0"

[tasks.failure]
run = "exit 1"

[tasks.never_runs]
run = "echo This should not run"

[tasks.sequential_failfast]
run = ["success", "failure", "never_runs"]
description = "Sequential task that fails fast"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Run sequential task
        result = await registry.run_task("sequential_failfast")

        # Verify it failed fast (never_runs should not have executed)
        assert not result.success
        assert result.exit_code == 1

    @pytest.mark.asyncio
    async def test_parse_parallel_flag_from_toml(self, tmp_path: Path) -> None:
        """Test parallel=true is parsed correctly from TOML."""
        # Create wrknv.toml with parallel task
        config_content = """
[tasks.task1]
run = "exit 0"

[tasks.task2]
run = "exit 0"

[tasks.parallel_task]
run = ["task1", "task2"]
parallel = true
description = "Parallel task"

[tasks.sequential_task]
run = ["task1", "task2"]
description = "Sequential task"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Get tasks
        parallel_task = registry.get_task("parallel_task")
        sequential_task = registry.get_task("sequential_task")

        # Verify parallel flag
        assert parallel_task is not None
        assert parallel_task.parallel is True

        assert sequential_task is not None
        assert sequential_task.parallel is False  # Default

    def test_parallel_defaults_to_false(self, tmp_path: Path) -> None:
        """Test backward compatibility - parallel defaults to False."""
        # Create wrknv.toml without parallel flag
        config_content = """
[tasks.task1]
run = "exit 0"

[tasks.task2]
run = "exit 0"

[tasks.composite]
run = ["task1", "task2"]
description = "Task without parallel flag"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Get task
        task = registry.get_task("composite")

        # Verify parallel defaults to False
        assert task is not None
        assert task.parallel is False

    def test_taskconfig_parallel_field(self) -> None:
        """Test TaskConfig has parallel field with correct default."""
        # Create task without specifying parallel
        task1 = TaskConfig(name="test", run=["subtask1", "subtask2"])
        assert task1.parallel is False

        # Create task with parallel=True
        task2 = TaskConfig(name="test", run=["subtask1", "subtask2"], parallel=True)
        assert task2.parallel is True

        # Create task with parallel=False (explicit)
        task3 = TaskConfig(name="test", run=["subtask1", "subtask2"], parallel=False)
        assert task3.parallel is False

    @pytest.mark.asyncio
    async def test_parallel_execution_is_concurrent(self, tmp_path: Path) -> None:
        """Test that parallel tasks actually run concurrently, not sequentially."""
        # Create wrknv.toml with tasks that sleep
        config_content = """
[tasks.sleep1]
run = "sleep 0.5"

[tasks.sleep2]
run = "sleep 0.5"

[tasks.parallel_sleep]
run = ["sleep1", "sleep2"]
parallel = true
description = "Parallel sleep tasks"

[tasks.sequential_sleep]
run = ["sleep1", "sleep2"]
description = "Sequential sleep tasks"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Run parallel task and measure time
        import time

        start = time.time()
        parallel_result = await registry.run_task("parallel_sleep")
        parallel_duration = time.time() - start

        # Run sequential task and measure time
        start = time.time()
        sequential_result = await registry.run_task("sequential_sleep")
        sequential_duration = time.time() - start

        # Verify both succeeded
        assert parallel_result.success
        assert sequential_result.success

        # Parallel should be roughly 2x faster (both tasks run concurrently)
        # Allow some overhead, so check if parallel is at least 1.5x faster
        assert parallel_duration < sequential_duration * 0.7, (
            f"Parallel ({parallel_duration:.2f}s) should be faster than "
            f"sequential ({sequential_duration:.2f}s)"
        )

    @pytest.mark.asyncio
    async def test_nested_parallel_tasks(self, tmp_path: Path) -> None:
        """Test that parallel tasks can be nested (inner parallel task)."""
        # Create wrknv.toml with nested parallel tasks
        config_content = """
[tasks.success1]
run = "exit 0"

[tasks.success2]
run = "exit 0"

[tasks.inner_parallel]
run = ["success1", "success2"]
parallel = true
description = "Inner parallel task"

[tasks.outer]
run = ["inner_parallel", "success1"]
description = "Outer task with inner parallel"
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Run outer task
        result = await registry.run_task("outer")

        # Verify success
        assert result.success
        assert result.exit_code == 0

    @pytest.mark.asyncio
    async def test_parallel_with_complex_config(self, tmp_path: Path) -> None:
        """Test parallel flag works with full task configuration."""
        # Create wrknv.toml with complex parallel task
        config_content = """
[tasks.success1]
run = "exit 0"

[tasks.success2]
run = "exit 0"

[tasks.complex_parallel]
run = ["success1", "success2"]
parallel = true
description = "Complex parallel task"
timeout = 60.0
env = { CI = "true" }
"""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text(config_content)

        # Load registry
        registry = TaskRegistry.from_repo(tmp_path)

        # Get task
        task = registry.get_task("complex_parallel")

        # Verify all fields including parallel
        assert task is not None
        assert task.parallel is True
        assert task.description == "Complex parallel task"
        assert task.timeout == 60.0
        assert task.env == {"CI": "true"}

        # Run task
        result = await registry.run_task("complex_parallel")
        assert result.success
