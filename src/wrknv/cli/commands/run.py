#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Runner Commands

Commands for running tasks defined in wrknv.toml."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys

from provide.foundation.cli import echo_error, echo_info, echo_success
from provide.foundation.hub import register_command

from wrknv.tasks.registry import TaskRegistry


@register_command("run", description="Run tasks defined in wrknv.toml")
def run_command(
    tasks: tuple[str, ...],
    dry_run: bool = False,
    info: bool = False,
    env: tuple[str, ...] = (),
) -> None:
    """Run one or more tasks.

    Examples:
        wrknv run test
        wrknv run lint format typecheck
        wrknv run build --dry-run
        wrknv run test --env PYTEST_WORKERS=4
    """
    if not tasks:
        echo_error("No tasks specified. Usage: wrknv run <task> [<task>...]")
        sys.exit(1)

    # Parse environment variables
    env_dict = {}
    for e in env:
        if "=" not in e:
            echo_error(f"Invalid env format: {e}. Use KEY=VALUE")
            sys.exit(1)
        key, value = e.split("=", 1)
        env_dict[key] = value

    # Load task registry
    repo_path = Path.cwd()
    registry = TaskRegistry.from_repo(repo_path)

    # Show info mode
    if info:
        for task_name in tasks:
            task = registry.get_task(task_name)
            if not task:
                echo_error(f"Task not found: {task_name}")
                continue

            echo_info(f"\nTask: {task.name}")
            if task.description:
                echo_info(f"  Description: {task.description}")
            echo_info(f"  Command: {task.run}")
            if task.depends_on:
                echo_info(f"  Depends on: {', '.join(task.depends_on)}")
            if task.env:
                echo_info(f"  Environment: {task.env}")
        return

    # Execute tasks
    asyncio.run(_run_tasks(registry, tasks, dry_run, env_dict))


async def _run_tasks(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, dry_run, env)

            if result.stdout:
                print(result.stdout, end="")
            if result.stderr:
                print(result.stderr, end="", file=sys.stderr)

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


@register_command("tasks", description="List available tasks")
def tasks_command(verbose: bool = False) -> None:
    """List all available tasks defined in wrknv.toml.

    Examples:
        wrknv tasks              # List all tasks
        wrknv tasks --verbose    # Show task details
    """
    repo_path = Path.cwd()
    registry = TaskRegistry.from_repo(repo_path)

    tasks = registry.list_tasks()

    if not tasks:
        echo_info("No tasks defined in wrknv.toml")
        return

    echo_info("\nAvailable tasks:")
    for task in tasks:
        if verbose:
            echo_info(f"\n  {task.name}")
            if task.description:
                echo_info(f"    {task.description}")
            if task.is_composite:
                echo_info(f"    Runs: {', '.join(task.run)}")  # type: ignore[arg-type]
            else:
                echo_info(f"    Command: {task.run}")
        else:
            desc = f" - {task.description}" if task.description else ""
            echo_info(f"  {task.name}{desc}")
