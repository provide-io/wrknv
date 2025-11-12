#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Configuration Schema

Data models for task definitions and execution results."""

from __future__ import annotations

from pathlib import Path

from attrs import define, field


@define(frozen=True)
class TaskConfig:
    """Configuration for a single task."""

    name: str
    run: str | list[str]  # Command string or list of task names
    description: str | None = None
    env: dict[str, str] = field(factory=dict)
    depends_on: list[str] = field(factory=list)
    working_dir: Path | None = None

    @property
    def is_composite(self) -> bool:
        """Check if task runs other tasks (composite task)."""
        return isinstance(self.run, list)


@define
class TaskResult:
    """Result of task execution."""

    task: TaskConfig
    success: bool
    exit_code: int
    stdout: str
    stderr: str
    duration: float
