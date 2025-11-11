#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Executor

Executes task commands and captures results using provide.foundation process APIs."""

from __future__ import annotations

from pathlib import Path
import shlex
import sys
import time

from attrs import define
from provide.foundation import logger
from provide.foundation.errors import ProcessError, ProcessTimeoutError
from provide.foundation.process import async_run, async_stream

from wrknv.errors import TaskTimeoutError

from .schema import TaskConfig, TaskResult


def _should_stream_output(task: TaskConfig) -> bool:
    """Determine if task output should be streamed in real-time.

    Streaming is enabled when:
    1. Task explicitly sets stream_output=True, OR
    2. stdout is a TTY (interactive terminal)

    Args:
        task: Task configuration

    Returns:
        True if output should be streamed, False if buffered
    """
    # Explicit config takes precedence
    if task.stream_output:
        return True

    # Auto-detect: stream if stdout is a TTY (interactive terminal)
    return sys.stdout.isatty()


@define
class TaskExecutor:
    """Executes tasks defined in wrknv.toml using provide-foundation process APIs."""

    repo_path: Path
    env: dict[str, str] | None = None
    default_timeout: float = 300.0  # 5 minute default timeout

    async def execute(
        self,
        task: TaskConfig,
        args: list[str] | None = None,
        dry_run: bool = False,
    ) -> TaskResult:
        """Execute a single task.

        Args:
            task: Task to execute
            args: Optional arguments to append to the command
            dry_run: If True, show what would be executed without running

        Returns:
            TaskResult with execution details
        """
        # Build the command with args
        if isinstance(task.run, str):
            command = task.run
            if args:
                # Append args with proper shell quoting
                quoted_args = " ".join(shlex.quote(arg) for arg in args)
                command = f"{command} {quoted_args}"
        else:
            # Composite tasks should be handled by registry
            msg = "Composite tasks should be handled by registry"
            raise NotImplementedError(msg)

        if dry_run:
            logger.info(
                "Dry run task",
                task=task.full_name,
                command=command,
                cwd=str(task.working_dir or self.repo_path),
            )
            return TaskResult(
                task=task,
                success=True,
                exit_code=0,
                stdout="",
                stderr="",
                duration=0.0,
            )

        # Determine working directory
        cwd = task.working_dir or self.repo_path
        timeout = task.timeout or self.default_timeout

        # Log task start
        logger.info(
            "Starting task",
            task=task.full_name,
            command=command[:100] + "..." if len(command) > 100 else command,
            cwd=str(cwd),
            timeout=timeout,
        )

        # Build environment: merge executor env with task env
        exec_env = {}
        if self.env:
            exec_env.update(self.env)
        exec_env.update(task.env)

        # Determine if we should stream output
        use_streaming = _should_stream_output(task)

        # Execute command using foundation's async_run or async_stream
        start = time.time()

        try:
            if use_streaming:
                # Streaming mode: show output in real-time
                # Parse command into list for async_stream (which doesn't support shell=True)
                cmd_list = ["/bin/sh", "-c", command]

                stdout_lines = []

                async for line in async_stream(
                    cmd=cmd_list,
                    cwd=cwd,
                    env=exec_env if exec_env else None,
                    timeout=timeout,
                    stream_stderr=True,  # Merge stderr into stdout for streaming
                ):
                    # Print line immediately for user feedback (add newline back)
                    print(line, flush=True)
                    # Also accumulate for TaskResult (preserve original format)
                    stdout_lines.append(line + "\n")

                duration = time.time() - start

                # async_stream doesn't provide exit code, assume success if no exception
                exit_code = 0
                stdout_text = "".join(stdout_lines)
                stderr_text = ""  # Merged into stdout

                logger.info(
                    "Task completed",
                    task=task.full_name,
                    success=True,
                    duration=f"{duration:.2f}s",
                    exit_code=exit_code,
                )

                return TaskResult(
                    task=task,
                    success=True,
                    exit_code=exit_code,
                    stdout=stdout_text,
                    stderr=stderr_text,
                    duration=duration,
                )
            else:
                # Buffered mode: capture all output (original behavior)
                result = await async_run(
                    cmd=command,
                    cwd=cwd,
                    env=exec_env if exec_env else None,  # Foundation merges with os.environ
                    capture_output=True,
                    check=False,  # We handle errors ourselves
                    timeout=timeout,
                    shell=True,  # Explicit shell usage for command strings
                )

                duration = time.time() - start

                # Log task completion
                logger.info(
                    "Task completed",
                    task=task.full_name,
                    success=result.returncode == 0,
                    duration=f"{duration:.2f}s",
                    exit_code=result.returncode,
                )

                return TaskResult(
                    task=task,
                    success=result.returncode == 0,
                    exit_code=result.returncode,
                    stdout=result.stdout or "",
                    stderr=result.stderr or "",
                    duration=duration,
                )

        except ProcessTimeoutError as e:
            duration = time.time() - start
            logger.error(
                "Task timeout",
                task=task.full_name,
                timeout=timeout,
                duration=f"{duration:.2f}s",
            )

            # Raise task-specific timeout error
            raise TaskTimeoutError(task.full_name, timeout) from e

        except ProcessError as e:
            duration = time.time() - start
            logger.error(
                "Task execution failed",
                task=task.full_name,
                exit_code=e.exit_code if hasattr(e, "exit_code") else 1,
                duration=f"{duration:.2f}s",
                error=str(e),
            )

            # Return error result instead of raising (for non-critical failures)
            return TaskResult(
                task=task,
                success=False,
                exit_code=e.exit_code if hasattr(e, "exit_code") else 1,
                stdout="",
                stderr=str(e),
                duration=duration,
            )
