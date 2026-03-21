#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task Runner Commands

Commands for running tasks defined in wrknv.toml."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
from typing import Annotated

from provide.foundation.cli import echo_error, echo_info, echo_success
from provide.foundation.console.output import perr, pout
from provide.foundation.hub import register_command

from wrknv.tasks.registry import TaskRegistry
from wrknv.tasks.schema import TaskConfig
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


@register_command("run", description="Run tasks defined in wrknv.toml")
def run_command(
    task: Annotated[str, "argument"],
    dry_run: bool = False,
    info: bool = False,
    env: tuple[str, ...] | None = None,
) -> None:
    """Run a task.

    Examples:
        wrknv run test
        wrknv run build --dry-run
        wrknv run test --env PYTEST_WORKERS=4
    """
    tasks = (task,)  # Convert to tuple for compatibility

    # Parse environment variables
    env_dict = {}
    for e in env or ():
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
            found_task = registry.get_task(task_name)
            if not found_task:
                echo_error(f"Task not found: {task_name}")
                continue

            echo_info(f"\nTask: {found_task.name}")
            if found_task.description:
                echo_info(f"  Description: {found_task.description}")
            echo_info(f"  Command: {found_task.run}")
            if found_task.depends_on:
                echo_info(f"  Depends on: {', '.join(found_task.depends_on)}")
            if found_task.env:
                echo_info(f"  Environment: {found_task.env}")
        return

    # Execute tasks
    asyncio.run(_run_tasks(registry, tasks, dry_run, env_dict))


async def x__run_tasks__mutmut_orig(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_1(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(None)

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_2(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = None

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_3(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(None, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_4(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=None, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_5(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=None)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_6(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_7(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_8(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_9(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, )

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_10(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(None, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_11(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end=None)
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_12(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_13(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, )
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_14(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="XXXX")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_15(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(None, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_16(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end=None)

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_17(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_18(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, )

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_19(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="XXXX")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_20(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(None)
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_21(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(None)
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_22(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(None)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(1)


async def x__run_tasks__mutmut_23(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(None)
            sys.exit(1)


async def x__run_tasks__mutmut_24(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(None))
            sys.exit(1)


async def x__run_tasks__mutmut_25(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(None)


async def x__run_tasks__mutmut_26(
    registry: TaskRegistry,
    task_names: tuple[str, ...],
    dry_run: bool,
    env: dict[str, str],
) -> None:
    """Run tasks sequentially."""

    for task_name in task_names:
        echo_info(f"\n▶ Running task: {task_name}")

        try:
            result = await registry.run_task(task_name, args=None, dry_run=dry_run, env=env)

            if result.stdout:
                pout(result.stdout, end="")
            if result.stderr:
                perr(result.stderr, end="")

            if result.success:
                echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            else:
                echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
                sys.exit(result.exit_code)

        except ValueError as e:
            echo_error(str(e))
            sys.exit(2)

x__run_tasks__mutmut_mutants : ClassVar[MutantDict] = {
'x__run_tasks__mutmut_1': x__run_tasks__mutmut_1, 
    'x__run_tasks__mutmut_2': x__run_tasks__mutmut_2, 
    'x__run_tasks__mutmut_3': x__run_tasks__mutmut_3, 
    'x__run_tasks__mutmut_4': x__run_tasks__mutmut_4, 
    'x__run_tasks__mutmut_5': x__run_tasks__mutmut_5, 
    'x__run_tasks__mutmut_6': x__run_tasks__mutmut_6, 
    'x__run_tasks__mutmut_7': x__run_tasks__mutmut_7, 
    'x__run_tasks__mutmut_8': x__run_tasks__mutmut_8, 
    'x__run_tasks__mutmut_9': x__run_tasks__mutmut_9, 
    'x__run_tasks__mutmut_10': x__run_tasks__mutmut_10, 
    'x__run_tasks__mutmut_11': x__run_tasks__mutmut_11, 
    'x__run_tasks__mutmut_12': x__run_tasks__mutmut_12, 
    'x__run_tasks__mutmut_13': x__run_tasks__mutmut_13, 
    'x__run_tasks__mutmut_14': x__run_tasks__mutmut_14, 
    'x__run_tasks__mutmut_15': x__run_tasks__mutmut_15, 
    'x__run_tasks__mutmut_16': x__run_tasks__mutmut_16, 
    'x__run_tasks__mutmut_17': x__run_tasks__mutmut_17, 
    'x__run_tasks__mutmut_18': x__run_tasks__mutmut_18, 
    'x__run_tasks__mutmut_19': x__run_tasks__mutmut_19, 
    'x__run_tasks__mutmut_20': x__run_tasks__mutmut_20, 
    'x__run_tasks__mutmut_21': x__run_tasks__mutmut_21, 
    'x__run_tasks__mutmut_22': x__run_tasks__mutmut_22, 
    'x__run_tasks__mutmut_23': x__run_tasks__mutmut_23, 
    'x__run_tasks__mutmut_24': x__run_tasks__mutmut_24, 
    'x__run_tasks__mutmut_25': x__run_tasks__mutmut_25, 
    'x__run_tasks__mutmut_26': x__run_tasks__mutmut_26
}

def _run_tasks(*args, **kwargs):
    result = _mutmut_trampoline(x__run_tasks__mutmut_orig, x__run_tasks__mutmut_mutants, args, kwargs)
    return result 

_run_tasks.__signature__ = _mutmut_signature(x__run_tasks__mutmut_orig)
x__run_tasks__mutmut_orig.__name__ = 'x__run_tasks'


def x__display_tasks_hierarchical__mutmut_orig(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_1(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = None
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_2(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = None

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_3(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_4(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = None
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_5(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(None)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_6(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(None)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_7(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info(None)

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_8(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("XX\nAvailable tasks:XX")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_9(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\navailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_10(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAVAILABLE TASKS:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_11(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(None):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_12(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(None)
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_13(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = None

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_14(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(None, key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_15(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=None)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_16(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_17(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], )

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_18(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: None)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_19(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(None):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_20(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = None
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_21(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i != len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_22(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) + 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_23(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 2
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_24(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = None

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_25(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "XX└── XX" if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_26(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "XX├── XX"

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_27(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = None
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_28(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display = " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_29(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display -= " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_30(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += "XX (default)XX"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_31(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (DEFAULT)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_32(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display = f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_33(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display -= f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_34(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(None)

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_35(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = None
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_36(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "XX    XX" if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_37(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "XX│   XX"
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_38(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(None)
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_39(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(None)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_40(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {'XX, XX'.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_41(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = None
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_42(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(None)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_43(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:61]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_44(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) >= 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_45(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 61:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_46(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview = "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_47(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview -= "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_48(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "XX...XX"
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_49(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(None)

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_50(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info(None)
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_51(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("XX\nFlat tasks:XX")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_52(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nflat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_53(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFLAT TASKS:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_54(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(None, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_55(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=None):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_56(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_57(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, ):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_58(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: None):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_59(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = None
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_60(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display = f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_61(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display -= f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_62(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(None)

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_63(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(None)
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_64(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(None)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_65(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {'XX, XX'.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_66(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = None
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_67(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(None)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_68(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:61]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_69(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) >= 60:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_70(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 61:
                        cmd_preview += "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_71(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview = "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_72(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview -= "..."
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_73(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "XX...XX"
                    echo_info(f"    Command: {cmd_preview}")


def x__display_tasks_hierarchical__mutmut_74(tasks: list[TaskConfig], verbose: bool) -> None:
    """Display tasks in a hierarchical tree structure.

    Groups tasks by namespace and shows them in a tree format.
    Flat tasks are shown separately at the end.

    Args:
        tasks: List of TaskConfig objects to display
        verbose: If True, show detailed task information
    """
    # Organize tasks by namespace
    namespaced_tasks: dict[str, list[TaskConfig]] = {}
    flat_tasks: list[TaskConfig] = []

    for task in tasks:
        if task.namespace:
            if task.namespace not in namespaced_tasks:
                namespaced_tasks[task.namespace] = []
            namespaced_tasks[task.namespace].append(task)
        else:
            flat_tasks.append(task)

    echo_info("\nAvailable tasks:")

    # Display namespaced tasks as trees
    for namespace in sorted(namespaced_tasks.keys()):
        echo_info(f"\n{namespace}")
        tasks_in_namespace = sorted(namespaced_tasks[namespace], key=lambda t: t.name)

        for i, task in enumerate(tasks_in_namespace):
            is_last = i == len(tasks_in_namespace) - 1
            prefix = "└── " if is_last else "├── "

            # Build task display
            task_display = task.name
            if task.is_default:
                task_display += " (default)"

            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"{prefix}{task_display}")

            # Show details in verbose mode
            if verbose:
                detail_prefix = "    " if is_last else "│   "
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"{detail_prefix}Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(f"{detail_prefix}Command: {cmd_preview}")

    # Display flat tasks
    if flat_tasks:
        echo_info("\nFlat tasks:")
        for task in sorted(flat_tasks, key=lambda t: t.name):
            task_display = f"• {task.name}"
            if task.description:
                task_display += f"  {task.description}"

            echo_info(f"  {task_display}")

            if verbose:
                if task.is_composite:
                    assert isinstance(task.run, list)  # nosec B101 - Type narrowing
                    echo_info(f"    Runs: {', '.join(task.run)}")
                else:
                    cmd_preview = str(task.run)[:60]
                    if len(str(task.run)) > 60:
                        cmd_preview += "..."
                    echo_info(None)

x__display_tasks_hierarchical__mutmut_mutants : ClassVar[MutantDict] = {
'x__display_tasks_hierarchical__mutmut_1': x__display_tasks_hierarchical__mutmut_1, 
    'x__display_tasks_hierarchical__mutmut_2': x__display_tasks_hierarchical__mutmut_2, 
    'x__display_tasks_hierarchical__mutmut_3': x__display_tasks_hierarchical__mutmut_3, 
    'x__display_tasks_hierarchical__mutmut_4': x__display_tasks_hierarchical__mutmut_4, 
    'x__display_tasks_hierarchical__mutmut_5': x__display_tasks_hierarchical__mutmut_5, 
    'x__display_tasks_hierarchical__mutmut_6': x__display_tasks_hierarchical__mutmut_6, 
    'x__display_tasks_hierarchical__mutmut_7': x__display_tasks_hierarchical__mutmut_7, 
    'x__display_tasks_hierarchical__mutmut_8': x__display_tasks_hierarchical__mutmut_8, 
    'x__display_tasks_hierarchical__mutmut_9': x__display_tasks_hierarchical__mutmut_9, 
    'x__display_tasks_hierarchical__mutmut_10': x__display_tasks_hierarchical__mutmut_10, 
    'x__display_tasks_hierarchical__mutmut_11': x__display_tasks_hierarchical__mutmut_11, 
    'x__display_tasks_hierarchical__mutmut_12': x__display_tasks_hierarchical__mutmut_12, 
    'x__display_tasks_hierarchical__mutmut_13': x__display_tasks_hierarchical__mutmut_13, 
    'x__display_tasks_hierarchical__mutmut_14': x__display_tasks_hierarchical__mutmut_14, 
    'x__display_tasks_hierarchical__mutmut_15': x__display_tasks_hierarchical__mutmut_15, 
    'x__display_tasks_hierarchical__mutmut_16': x__display_tasks_hierarchical__mutmut_16, 
    'x__display_tasks_hierarchical__mutmut_17': x__display_tasks_hierarchical__mutmut_17, 
    'x__display_tasks_hierarchical__mutmut_18': x__display_tasks_hierarchical__mutmut_18, 
    'x__display_tasks_hierarchical__mutmut_19': x__display_tasks_hierarchical__mutmut_19, 
    'x__display_tasks_hierarchical__mutmut_20': x__display_tasks_hierarchical__mutmut_20, 
    'x__display_tasks_hierarchical__mutmut_21': x__display_tasks_hierarchical__mutmut_21, 
    'x__display_tasks_hierarchical__mutmut_22': x__display_tasks_hierarchical__mutmut_22, 
    'x__display_tasks_hierarchical__mutmut_23': x__display_tasks_hierarchical__mutmut_23, 
    'x__display_tasks_hierarchical__mutmut_24': x__display_tasks_hierarchical__mutmut_24, 
    'x__display_tasks_hierarchical__mutmut_25': x__display_tasks_hierarchical__mutmut_25, 
    'x__display_tasks_hierarchical__mutmut_26': x__display_tasks_hierarchical__mutmut_26, 
    'x__display_tasks_hierarchical__mutmut_27': x__display_tasks_hierarchical__mutmut_27, 
    'x__display_tasks_hierarchical__mutmut_28': x__display_tasks_hierarchical__mutmut_28, 
    'x__display_tasks_hierarchical__mutmut_29': x__display_tasks_hierarchical__mutmut_29, 
    'x__display_tasks_hierarchical__mutmut_30': x__display_tasks_hierarchical__mutmut_30, 
    'x__display_tasks_hierarchical__mutmut_31': x__display_tasks_hierarchical__mutmut_31, 
    'x__display_tasks_hierarchical__mutmut_32': x__display_tasks_hierarchical__mutmut_32, 
    'x__display_tasks_hierarchical__mutmut_33': x__display_tasks_hierarchical__mutmut_33, 
    'x__display_tasks_hierarchical__mutmut_34': x__display_tasks_hierarchical__mutmut_34, 
    'x__display_tasks_hierarchical__mutmut_35': x__display_tasks_hierarchical__mutmut_35, 
    'x__display_tasks_hierarchical__mutmut_36': x__display_tasks_hierarchical__mutmut_36, 
    'x__display_tasks_hierarchical__mutmut_37': x__display_tasks_hierarchical__mutmut_37, 
    'x__display_tasks_hierarchical__mutmut_38': x__display_tasks_hierarchical__mutmut_38, 
    'x__display_tasks_hierarchical__mutmut_39': x__display_tasks_hierarchical__mutmut_39, 
    'x__display_tasks_hierarchical__mutmut_40': x__display_tasks_hierarchical__mutmut_40, 
    'x__display_tasks_hierarchical__mutmut_41': x__display_tasks_hierarchical__mutmut_41, 
    'x__display_tasks_hierarchical__mutmut_42': x__display_tasks_hierarchical__mutmut_42, 
    'x__display_tasks_hierarchical__mutmut_43': x__display_tasks_hierarchical__mutmut_43, 
    'x__display_tasks_hierarchical__mutmut_44': x__display_tasks_hierarchical__mutmut_44, 
    'x__display_tasks_hierarchical__mutmut_45': x__display_tasks_hierarchical__mutmut_45, 
    'x__display_tasks_hierarchical__mutmut_46': x__display_tasks_hierarchical__mutmut_46, 
    'x__display_tasks_hierarchical__mutmut_47': x__display_tasks_hierarchical__mutmut_47, 
    'x__display_tasks_hierarchical__mutmut_48': x__display_tasks_hierarchical__mutmut_48, 
    'x__display_tasks_hierarchical__mutmut_49': x__display_tasks_hierarchical__mutmut_49, 
    'x__display_tasks_hierarchical__mutmut_50': x__display_tasks_hierarchical__mutmut_50, 
    'x__display_tasks_hierarchical__mutmut_51': x__display_tasks_hierarchical__mutmut_51, 
    'x__display_tasks_hierarchical__mutmut_52': x__display_tasks_hierarchical__mutmut_52, 
    'x__display_tasks_hierarchical__mutmut_53': x__display_tasks_hierarchical__mutmut_53, 
    'x__display_tasks_hierarchical__mutmut_54': x__display_tasks_hierarchical__mutmut_54, 
    'x__display_tasks_hierarchical__mutmut_55': x__display_tasks_hierarchical__mutmut_55, 
    'x__display_tasks_hierarchical__mutmut_56': x__display_tasks_hierarchical__mutmut_56, 
    'x__display_tasks_hierarchical__mutmut_57': x__display_tasks_hierarchical__mutmut_57, 
    'x__display_tasks_hierarchical__mutmut_58': x__display_tasks_hierarchical__mutmut_58, 
    'x__display_tasks_hierarchical__mutmut_59': x__display_tasks_hierarchical__mutmut_59, 
    'x__display_tasks_hierarchical__mutmut_60': x__display_tasks_hierarchical__mutmut_60, 
    'x__display_tasks_hierarchical__mutmut_61': x__display_tasks_hierarchical__mutmut_61, 
    'x__display_tasks_hierarchical__mutmut_62': x__display_tasks_hierarchical__mutmut_62, 
    'x__display_tasks_hierarchical__mutmut_63': x__display_tasks_hierarchical__mutmut_63, 
    'x__display_tasks_hierarchical__mutmut_64': x__display_tasks_hierarchical__mutmut_64, 
    'x__display_tasks_hierarchical__mutmut_65': x__display_tasks_hierarchical__mutmut_65, 
    'x__display_tasks_hierarchical__mutmut_66': x__display_tasks_hierarchical__mutmut_66, 
    'x__display_tasks_hierarchical__mutmut_67': x__display_tasks_hierarchical__mutmut_67, 
    'x__display_tasks_hierarchical__mutmut_68': x__display_tasks_hierarchical__mutmut_68, 
    'x__display_tasks_hierarchical__mutmut_69': x__display_tasks_hierarchical__mutmut_69, 
    'x__display_tasks_hierarchical__mutmut_70': x__display_tasks_hierarchical__mutmut_70, 
    'x__display_tasks_hierarchical__mutmut_71': x__display_tasks_hierarchical__mutmut_71, 
    'x__display_tasks_hierarchical__mutmut_72': x__display_tasks_hierarchical__mutmut_72, 
    'x__display_tasks_hierarchical__mutmut_73': x__display_tasks_hierarchical__mutmut_73, 
    'x__display_tasks_hierarchical__mutmut_74': x__display_tasks_hierarchical__mutmut_74
}

def _display_tasks_hierarchical(*args, **kwargs):
    result = _mutmut_trampoline(x__display_tasks_hierarchical__mutmut_orig, x__display_tasks_hierarchical__mutmut_mutants, args, kwargs)
    return result 

_display_tasks_hierarchical.__signature__ = _mutmut_signature(x__display_tasks_hierarchical__mutmut_orig)
x__display_tasks_hierarchical__mutmut_orig.__name__ = 'x__display_tasks_hierarchical'


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

    _display_tasks_hierarchical(tasks, verbose)
