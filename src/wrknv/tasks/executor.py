#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Executor

Executes task commands and captures results."""

from __future__ import annotations

import asyncio
import os
from pathlib import Path
import time

from attrs import define
from provide.foundation import logger

from .schema import TaskConfig, TaskResult


@define
class TaskExecutor:
    """Executes tasks defined in wrknv.toml."""

    repo_path: Path
    env: dict[str, str] | None = None

    async def execute(
        self,
        task: TaskConfig,
        dry_run: bool = False,
    ) -> TaskResult:
        """Execute a single task.

        Args:
            task: Task to execute
            dry_run: If True, show what would be executed without running

        Returns:
            TaskResult with execution details
        """
        if dry_run:
            logger.info(f"[DRY RUN] Would execute: {task.name}")
            logger.info(f"  Command: {task.run}")
            return TaskResult(
                task=task,
                success=True,
                exit_code=0,
                stdout="",
                stderr="",
                duration=0.0,
            )

        # Build environment
        exec_env = {**os.environ}
        if self.env:
            exec_env.update(self.env)
        exec_env.update(task.env)

        # Determine working directory
        cwd = task.working_dir or self.repo_path

        # Execute command
        if isinstance(task.run, str):
            return await self._execute_command(task, task.run, exec_env, cwd)

        msg = "Composite tasks should be handled by registry"
        raise NotImplementedError(msg)

    async def _execute_command(
        self,
        task: TaskConfig,
        command: str,
        env: dict[str, str],
        cwd: Path,
    ) -> TaskResult:
        """Execute a shell command.

        Args:
            task: Task being executed
            command: Shell command to run
            env: Environment variables
            cwd: Working directory

        Returns:
            TaskResult with command output and exit code
        """
        start = time.time()

        try:
            proc = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
                cwd=str(cwd),
            )

            stdout_bytes, stderr_bytes = await proc.communicate()
            duration = time.time() - start

            return TaskResult(
                task=task,
                success=proc.returncode == 0,
                exit_code=proc.returncode or 0,
                stdout=stdout_bytes.decode(),
                stderr=stderr_bytes.decode(),
                duration=duration,
            )

        except Exception as e:
            duration = time.time() - start
            logger.error(f"Task {task.name} failed: {e}")

            return TaskResult(
                task=task,
                success=False,
                exit_code=1,
                stdout="",
                stderr=str(e),
                duration=duration,
            )
