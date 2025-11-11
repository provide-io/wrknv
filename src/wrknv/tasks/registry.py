#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Registry

Manages task discovery and loading from wrknv.toml files."""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from attrs import define

from .schema import TaskConfig


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

        with open(config_path, "rb") as f:
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
