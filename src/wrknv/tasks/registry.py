#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Registry

Manages task discovery and loading from wrknv.toml files."""

from __future__ import annotations

from pathlib import Path
import tomllib
from typing import Any

from attrs import define

from .executor import TaskExecutor
from .schema import TaskConfig, TaskResult


@define
class TaskRegistry:
    """Manages task discovery and execution for a repository."""

    repo_path: Path
    tasks: dict[str, TaskConfig]

    @classmethod
    def from_repo(cls, repo_path: Path) -> TaskRegistry:
        """Load tasks from wrknv.toml in the repository.

        Args:
            repo_path: Path to repository root containing wrknv.toml

        Returns:
            TaskRegistry with loaded tasks
        """
        config_path = repo_path / "wrknv.toml"

        if not config_path.exists():
            return cls(repo_path=repo_path, tasks={})

        with config_path.open("rb") as f:
            config = tomllib.load(f)

        tasks = {}

        # Load tasks section
        if "tasks" in config and isinstance(config["tasks"], dict):
            for name, value in config["tasks"].items():
                task = cls._parse_task(name, value)
                if task:
                    tasks[name] = task

        return cls(repo_path=repo_path, tasks=tasks)

    @classmethod
    def _parse_task(cls, name: str, value: Any) -> TaskConfig | None:
        """Parse a task definition from TOML value.

        Args:
            name: Task name
            value: Task definition (string or dict)

        Returns:
            TaskConfig or None if invalid
        """
        if isinstance(value, str):
            # Simple task: name = "command"
            return TaskConfig(name=name, run=value)

        if isinstance(value, dict):
            # Complex task with full configuration
            run = value.get("run")
            if run is None:
                return None

            return TaskConfig(
                name=name,
                run=run,
                description=value.get("description"),
                env=value.get("env", {}),
                depends_on=value.get("depends_on", []),
                working_dir=Path(value["working_dir"]) if "working_dir" in value else None,
            )

        return None

    def get_task(self, name: str) -> TaskConfig | None:
        """Get a task by name.

        Args:
            name: Task name

        Returns:
            TaskConfig if found, None otherwise
        """
        return self.tasks.get(name)

    def list_tasks(self) -> list[TaskConfig]:
        """List all registered tasks.

        Returns:
            List of all TaskConfig objects
        """
        return list(self.tasks.values())

    async def run_task(
        self,
        name: str,
        dry_run: bool = False,
        env: dict[str, str] | None = None,
    ) -> TaskResult:
        """Run a task by name.

        Args:
            name: Task name to execute
            dry_run: If True, show what would be executed without running
            env: Additional environment variables

        Returns:
            TaskResult with execution details

        Raises:
            ValueError: If task not found
        """
        task = self.get_task(name)
        if not task:
            msg = f"Task not found: {name}"
            raise ValueError(msg)

        # Check if composite task
        if task.is_composite:
            return await self._run_composite_task(task, dry_run, env)

        # Run single task
        executor = TaskExecutor(self.repo_path, env)
        return await executor.execute(task, dry_run)

    async def _run_composite_task(
        self,
        task: TaskConfig,
        dry_run: bool,
        env: dict[str, str] | None,
    ) -> TaskResult:
        """Run a composite task that executes other tasks.

        Args:
            task: Composite task to execute
            dry_run: If True, show what would be executed
            env: Additional environment variables

        Returns:
            TaskResult aggregating all subtask results
        """
        assert isinstance(task.run, list)

        results = []
        for subtask_name in task.run:
            result = await self.run_task(subtask_name, dry_run, env)
            results.append(result)

            if not result.success:
                # Stop on first failure
                break

        # Aggregate results
        success = all(r.success for r in results)
        exit_code = 0 if success else 1

        return TaskResult(
            task=task,
            success=success,
            exit_code=exit_code,
            stdout="",
            stderr="",
            duration=sum(r.duration for r in results),
        )
