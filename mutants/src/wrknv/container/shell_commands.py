#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Container Shell Commands
========================
Commands for interacting with running containers."""

from __future__ import annotations

from typing import Any

from provide.foundation import logger
from provide.foundation.process import CompletedProcess, run, stream
from rich.console import Console

from wrknv.config import WorkenvConfig
from wrknv.container.manager import ContainerManager
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


def x_shell_into_container__mutmut_orig(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_1(
    config: WorkenvConfig,
    shell: str = "XX/bin/bashXX",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_2(
    config: WorkenvConfig,
    shell: str = "/BIN/BASH",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_3(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = True,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_4(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = None

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_5(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container and not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_6(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_7(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_8(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print(None)
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_9(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("XX[red]❌ Container support is not enabled[/red]XX")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_10(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_11(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[RED]❌ CONTAINER SUPPORT IS NOT ENABLED[/RED]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_12(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return True

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_13(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = None

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_14(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(None)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_15(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_16(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_17(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(None)
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_18(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return True

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_19(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                None
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_20(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_21(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print(None)
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_22(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("XX[red]❌ Failed to start container[/red]XX")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_23(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_24(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[RED]❌ FAILED TO START CONTAINER[/RED]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_25(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return True
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_26(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(None)
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_27(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print(None)
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_28(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("XXUse --auto-start to start it automaticallyXX")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_29(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_30(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("USE --AUTO-START TO START IT AUTOMATICALLY")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_31(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return True

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_32(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = None

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_33(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["XXdockerXX", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_34(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["DOCKER", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_35(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "XXexecXX", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_36(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "EXEC", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_37(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "XX-itXX"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_38(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-IT"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_39(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(None)

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_40(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["XX-wXX", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_41(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-W", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_42(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(None)

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_43(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["XX-eXX", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_44(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-E", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_45(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend(None)

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_46(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(None)
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_47(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(None)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_48(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {'XX XX'.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_49(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(None)

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_50(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = None
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_51(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(None, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_52(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=None)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_53(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_54(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, )
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_55(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=True)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_56(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode != 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_57(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 1
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_58(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print(None)
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_59(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("XX\n[yellow]Shell session interrupted[/yellow]XX")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_60(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_61(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[YELLOW]SHELL SESSION INTERRUPTED[/YELLOW]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_62(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return False
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_63(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(None)
        logger.error(f"Shell failed: {e}")
        return False


def x_shell_into_container__mutmut_64(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(None)
        return False


def x_shell_into_container__mutmut_65(
    config: WorkenvConfig,
    shell: str = "/bin/bash",
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    auto_start: bool = False,
) -> bool:
    """
    Open an interactive shell session in the container.

    Args:
        config: Workenv configuration
        shell: Shell to use (default: /bin/bash)
        working_dir: Working directory in container
        environment: Environment variables to set
        auto_start: Auto-start container if not running

    Returns:
        True if shell session was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        if not manager.container_exists():
            console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
            return False

        if auto_start:
            console.print(
                f"[yellow]⚠️  Container {manager.container_name} is not running. Starting...[/yellow]"
            )
            if not manager.start():
                console.print("[red]❌ Failed to start container[/red]")
                return False
        else:
            console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
            console.print("Use --auto-start to start it automatically")
            return False

    # Build docker exec command
    cmd = ["docker", "exec", "-it"]

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and shell
    cmd.extend([manager.container_name, shell])

    logger.info(f"Opening shell in container: {' '.join(cmd)}")
    console.print(f"[green]🐚 Opening {shell} in {manager.container_name}...[/green]")

    try:
        # Run interactively without capturing output
        result = run(cmd, check=False)
        return result.returncode == 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Shell session interrupted[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to open shell: {e}[/red]")
        logger.error(f"Shell failed: {e}")
        return True

x_shell_into_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_shell_into_container__mutmut_1': x_shell_into_container__mutmut_1, 
    'x_shell_into_container__mutmut_2': x_shell_into_container__mutmut_2, 
    'x_shell_into_container__mutmut_3': x_shell_into_container__mutmut_3, 
    'x_shell_into_container__mutmut_4': x_shell_into_container__mutmut_4, 
    'x_shell_into_container__mutmut_5': x_shell_into_container__mutmut_5, 
    'x_shell_into_container__mutmut_6': x_shell_into_container__mutmut_6, 
    'x_shell_into_container__mutmut_7': x_shell_into_container__mutmut_7, 
    'x_shell_into_container__mutmut_8': x_shell_into_container__mutmut_8, 
    'x_shell_into_container__mutmut_9': x_shell_into_container__mutmut_9, 
    'x_shell_into_container__mutmut_10': x_shell_into_container__mutmut_10, 
    'x_shell_into_container__mutmut_11': x_shell_into_container__mutmut_11, 
    'x_shell_into_container__mutmut_12': x_shell_into_container__mutmut_12, 
    'x_shell_into_container__mutmut_13': x_shell_into_container__mutmut_13, 
    'x_shell_into_container__mutmut_14': x_shell_into_container__mutmut_14, 
    'x_shell_into_container__mutmut_15': x_shell_into_container__mutmut_15, 
    'x_shell_into_container__mutmut_16': x_shell_into_container__mutmut_16, 
    'x_shell_into_container__mutmut_17': x_shell_into_container__mutmut_17, 
    'x_shell_into_container__mutmut_18': x_shell_into_container__mutmut_18, 
    'x_shell_into_container__mutmut_19': x_shell_into_container__mutmut_19, 
    'x_shell_into_container__mutmut_20': x_shell_into_container__mutmut_20, 
    'x_shell_into_container__mutmut_21': x_shell_into_container__mutmut_21, 
    'x_shell_into_container__mutmut_22': x_shell_into_container__mutmut_22, 
    'x_shell_into_container__mutmut_23': x_shell_into_container__mutmut_23, 
    'x_shell_into_container__mutmut_24': x_shell_into_container__mutmut_24, 
    'x_shell_into_container__mutmut_25': x_shell_into_container__mutmut_25, 
    'x_shell_into_container__mutmut_26': x_shell_into_container__mutmut_26, 
    'x_shell_into_container__mutmut_27': x_shell_into_container__mutmut_27, 
    'x_shell_into_container__mutmut_28': x_shell_into_container__mutmut_28, 
    'x_shell_into_container__mutmut_29': x_shell_into_container__mutmut_29, 
    'x_shell_into_container__mutmut_30': x_shell_into_container__mutmut_30, 
    'x_shell_into_container__mutmut_31': x_shell_into_container__mutmut_31, 
    'x_shell_into_container__mutmut_32': x_shell_into_container__mutmut_32, 
    'x_shell_into_container__mutmut_33': x_shell_into_container__mutmut_33, 
    'x_shell_into_container__mutmut_34': x_shell_into_container__mutmut_34, 
    'x_shell_into_container__mutmut_35': x_shell_into_container__mutmut_35, 
    'x_shell_into_container__mutmut_36': x_shell_into_container__mutmut_36, 
    'x_shell_into_container__mutmut_37': x_shell_into_container__mutmut_37, 
    'x_shell_into_container__mutmut_38': x_shell_into_container__mutmut_38, 
    'x_shell_into_container__mutmut_39': x_shell_into_container__mutmut_39, 
    'x_shell_into_container__mutmut_40': x_shell_into_container__mutmut_40, 
    'x_shell_into_container__mutmut_41': x_shell_into_container__mutmut_41, 
    'x_shell_into_container__mutmut_42': x_shell_into_container__mutmut_42, 
    'x_shell_into_container__mutmut_43': x_shell_into_container__mutmut_43, 
    'x_shell_into_container__mutmut_44': x_shell_into_container__mutmut_44, 
    'x_shell_into_container__mutmut_45': x_shell_into_container__mutmut_45, 
    'x_shell_into_container__mutmut_46': x_shell_into_container__mutmut_46, 
    'x_shell_into_container__mutmut_47': x_shell_into_container__mutmut_47, 
    'x_shell_into_container__mutmut_48': x_shell_into_container__mutmut_48, 
    'x_shell_into_container__mutmut_49': x_shell_into_container__mutmut_49, 
    'x_shell_into_container__mutmut_50': x_shell_into_container__mutmut_50, 
    'x_shell_into_container__mutmut_51': x_shell_into_container__mutmut_51, 
    'x_shell_into_container__mutmut_52': x_shell_into_container__mutmut_52, 
    'x_shell_into_container__mutmut_53': x_shell_into_container__mutmut_53, 
    'x_shell_into_container__mutmut_54': x_shell_into_container__mutmut_54, 
    'x_shell_into_container__mutmut_55': x_shell_into_container__mutmut_55, 
    'x_shell_into_container__mutmut_56': x_shell_into_container__mutmut_56, 
    'x_shell_into_container__mutmut_57': x_shell_into_container__mutmut_57, 
    'x_shell_into_container__mutmut_58': x_shell_into_container__mutmut_58, 
    'x_shell_into_container__mutmut_59': x_shell_into_container__mutmut_59, 
    'x_shell_into_container__mutmut_60': x_shell_into_container__mutmut_60, 
    'x_shell_into_container__mutmut_61': x_shell_into_container__mutmut_61, 
    'x_shell_into_container__mutmut_62': x_shell_into_container__mutmut_62, 
    'x_shell_into_container__mutmut_63': x_shell_into_container__mutmut_63, 
    'x_shell_into_container__mutmut_64': x_shell_into_container__mutmut_64, 
    'x_shell_into_container__mutmut_65': x_shell_into_container__mutmut_65
}

def shell_into_container(*args, **kwargs):
    result = _mutmut_trampoline(x_shell_into_container__mutmut_orig, x_shell_into_container__mutmut_mutants, args, kwargs)
    return result 

shell_into_container.__signature__ = _mutmut_signature(x_shell_into_container__mutmut_orig)
x_shell_into_container__mutmut_orig.__name__ = 'x_shell_into_container'


def x_exec_in_container__mutmut_orig(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_1(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = True,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_2(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = None

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_3(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container and not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_4(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_5(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_6(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print(None)
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_7(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("XX[red]❌ Container support is not enabled[/red]XX")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_8(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_9(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[RED]❌ CONTAINER SUPPORT IS NOT ENABLED[/RED]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_10(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = None

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_11(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(None)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_12(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_13(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(None)
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_14(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = None

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_15(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["XXdockerXX", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_16(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["DOCKER", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_17(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "XXexecXX"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_18(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "EXEC"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_19(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append(None)

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_20(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("XX-itXX")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_21(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-IT")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_22(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(None)

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_23(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["XX-wXX", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_24(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-W", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_25(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(None)

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_26(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["XX-uXX", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_27(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-U", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_28(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(None)

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_29(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["XX-eXX", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_30(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-E", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_31(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(None)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_32(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(None)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_33(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(None)

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_34(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(None)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_35(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {'XX XX'.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_36(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = None

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_37(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(None, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_38(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=None)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_39(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_40(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, )

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_41(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=True)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_42(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 or result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_43(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_44(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 1 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_45(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(None)

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_46(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(None)
        logger.error(f"Exec failed: {e}")
        return None


def x_exec_in_container__mutmut_47(
    config: WorkenvConfig,
    command: list[str],
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    interactive: bool = False,
) -> CompletedProcess | None:
    """
    Execute a command in the container.

    Args:
        config: Workenv configuration
        command: Command and arguments to execute
        working_dir: Working directory in container
        environment: Environment variables to set
        user: User to run command as
        interactive: Run interactively (for commands like python, node, etc.)

    Returns:
        CompletedProcess result or None if container not running
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container is running
    if not manager.container_running():
        console.print(f"[yellow]⚠️  Container {manager.container_name} is not running[/yellow]")
        return None

    # Build docker exec command
    cmd = ["docker", "exec"]

    # Add interactive flags if needed
    if interactive:
        cmd.append("-it")

    # Add working directory if specified
    if working_dir:
        cmd.extend(["-w", working_dir])

    # Add user if specified
    if user:
        cmd.extend(["-u", user])

    # Add environment variables
    if environment:
        for key, value in environment.items():
            cmd.extend(["-e", f"{key}={value}"])

    # Add container name and command
    cmd.append(manager.container_name)
    cmd.extend(command)

    logger.info(f"Executing in container: {' '.join(cmd)}")

    try:
        # Run command (interactively if requested)
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stderr:
            console.print(f"[red]Command failed: {result.stderr}[/red]")

        return result
    except Exception as e:
        console.print(f"[red]❌ Failed to execute command: {e}[/red]")
        logger.error(None)
        return None

x_exec_in_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_exec_in_container__mutmut_1': x_exec_in_container__mutmut_1, 
    'x_exec_in_container__mutmut_2': x_exec_in_container__mutmut_2, 
    'x_exec_in_container__mutmut_3': x_exec_in_container__mutmut_3, 
    'x_exec_in_container__mutmut_4': x_exec_in_container__mutmut_4, 
    'x_exec_in_container__mutmut_5': x_exec_in_container__mutmut_5, 
    'x_exec_in_container__mutmut_6': x_exec_in_container__mutmut_6, 
    'x_exec_in_container__mutmut_7': x_exec_in_container__mutmut_7, 
    'x_exec_in_container__mutmut_8': x_exec_in_container__mutmut_8, 
    'x_exec_in_container__mutmut_9': x_exec_in_container__mutmut_9, 
    'x_exec_in_container__mutmut_10': x_exec_in_container__mutmut_10, 
    'x_exec_in_container__mutmut_11': x_exec_in_container__mutmut_11, 
    'x_exec_in_container__mutmut_12': x_exec_in_container__mutmut_12, 
    'x_exec_in_container__mutmut_13': x_exec_in_container__mutmut_13, 
    'x_exec_in_container__mutmut_14': x_exec_in_container__mutmut_14, 
    'x_exec_in_container__mutmut_15': x_exec_in_container__mutmut_15, 
    'x_exec_in_container__mutmut_16': x_exec_in_container__mutmut_16, 
    'x_exec_in_container__mutmut_17': x_exec_in_container__mutmut_17, 
    'x_exec_in_container__mutmut_18': x_exec_in_container__mutmut_18, 
    'x_exec_in_container__mutmut_19': x_exec_in_container__mutmut_19, 
    'x_exec_in_container__mutmut_20': x_exec_in_container__mutmut_20, 
    'x_exec_in_container__mutmut_21': x_exec_in_container__mutmut_21, 
    'x_exec_in_container__mutmut_22': x_exec_in_container__mutmut_22, 
    'x_exec_in_container__mutmut_23': x_exec_in_container__mutmut_23, 
    'x_exec_in_container__mutmut_24': x_exec_in_container__mutmut_24, 
    'x_exec_in_container__mutmut_25': x_exec_in_container__mutmut_25, 
    'x_exec_in_container__mutmut_26': x_exec_in_container__mutmut_26, 
    'x_exec_in_container__mutmut_27': x_exec_in_container__mutmut_27, 
    'x_exec_in_container__mutmut_28': x_exec_in_container__mutmut_28, 
    'x_exec_in_container__mutmut_29': x_exec_in_container__mutmut_29, 
    'x_exec_in_container__mutmut_30': x_exec_in_container__mutmut_30, 
    'x_exec_in_container__mutmut_31': x_exec_in_container__mutmut_31, 
    'x_exec_in_container__mutmut_32': x_exec_in_container__mutmut_32, 
    'x_exec_in_container__mutmut_33': x_exec_in_container__mutmut_33, 
    'x_exec_in_container__mutmut_34': x_exec_in_container__mutmut_34, 
    'x_exec_in_container__mutmut_35': x_exec_in_container__mutmut_35, 
    'x_exec_in_container__mutmut_36': x_exec_in_container__mutmut_36, 
    'x_exec_in_container__mutmut_37': x_exec_in_container__mutmut_37, 
    'x_exec_in_container__mutmut_38': x_exec_in_container__mutmut_38, 
    'x_exec_in_container__mutmut_39': x_exec_in_container__mutmut_39, 
    'x_exec_in_container__mutmut_40': x_exec_in_container__mutmut_40, 
    'x_exec_in_container__mutmut_41': x_exec_in_container__mutmut_41, 
    'x_exec_in_container__mutmut_42': x_exec_in_container__mutmut_42, 
    'x_exec_in_container__mutmut_43': x_exec_in_container__mutmut_43, 
    'x_exec_in_container__mutmut_44': x_exec_in_container__mutmut_44, 
    'x_exec_in_container__mutmut_45': x_exec_in_container__mutmut_45, 
    'x_exec_in_container__mutmut_46': x_exec_in_container__mutmut_46, 
    'x_exec_in_container__mutmut_47': x_exec_in_container__mutmut_47
}

def exec_in_container(*args, **kwargs):
    result = _mutmut_trampoline(x_exec_in_container__mutmut_orig, x_exec_in_container__mutmut_mutants, args, kwargs)
    return result 

exec_in_container.__signature__ = _mutmut_signature(x_exec_in_container__mutmut_orig)
x_exec_in_container__mutmut_orig.__name__ = 'x_exec_in_container'


def x_get_container_logs__mutmut_orig(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_1(
    config: WorkenvConfig,
    follow: bool = True,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_2(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = True,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_3(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = None

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_4(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container and not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_5(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_6(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_7(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print(None)
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_8(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("XX[red]❌ Container support is not enabled[/red]XX")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_9(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_10(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[RED]❌ CONTAINER SUPPORT IS NOT ENABLED[/RED]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_11(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = None

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_12(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(None)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_13(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_14(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(None)
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_15(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = None

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_16(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["XXdockerXX", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_17(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["DOCKER", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_18(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "XXlogsXX"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_19(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "LOGS"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_20(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append(None)

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_21(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("XX-fXX")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_22(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-F")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_23(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append(None)

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_24(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("XX-tXX")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_25(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-T")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_26(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_27(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(None)

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_28(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["XX--tailXX", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_29(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--TAIL", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_30(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(None)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_31(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(None)

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_32(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["XX--sinceXX", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_33(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--SINCE", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_34(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(None)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_35(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(None)

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_36(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(None)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_37(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {'XX XX'.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_38(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(None, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_39(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=None)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_40(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_41(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, )
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_42(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=True)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_43(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = None

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_44(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(None, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_45(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=None)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_46(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_47(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, )

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_48(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=True)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_49(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode == 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_50(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 1:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_51(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(None)
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_52(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(None)
        logger.error(f"Logs failed: {e}")
        return None


def x_get_container_logs__mutmut_53(
    config: WorkenvConfig,
    follow: bool = False,
    tail: int | None = None,
    since: str | None = None,
    timestamps: bool = False,
) -> str | None:
    """
    Get container logs.

    Args:
        config: Workenv configuration
        follow: Follow log output (like tail -f)
        tail: Number of lines to show from the end
        since: Show logs since timestamp (e.g., "1h", "2023-01-01")
        timestamps: Show timestamps in logs

    Returns:
        Log output as string, or None if container doesn't exist
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    # Check if container exists
    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return None

    # Build docker logs command
    cmd = ["docker", "logs"]

    # Add options
    if follow:
        cmd.append("-f")

    if timestamps:
        cmd.append("-t")

    if tail is not None:
        cmd.extend(["--tail", str(tail)])

    if since:
        cmd.extend(["--since", since])

    # Add container name
    cmd.append(manager.container_name)

    logger.info(f"Getting container logs: {' '.join(cmd)}")

    try:
        if follow:
            # Stream logs without capturing (for follow mode)
            run(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run(cmd, check=False)

            if result.returncode != 0:
                console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None

            return result.stdout
    except Exception as e:
        console.print(f"[red]❌ Failed to get logs: {e}[/red]")
        logger.error(None)
        return None

x_get_container_logs__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_container_logs__mutmut_1': x_get_container_logs__mutmut_1, 
    'x_get_container_logs__mutmut_2': x_get_container_logs__mutmut_2, 
    'x_get_container_logs__mutmut_3': x_get_container_logs__mutmut_3, 
    'x_get_container_logs__mutmut_4': x_get_container_logs__mutmut_4, 
    'x_get_container_logs__mutmut_5': x_get_container_logs__mutmut_5, 
    'x_get_container_logs__mutmut_6': x_get_container_logs__mutmut_6, 
    'x_get_container_logs__mutmut_7': x_get_container_logs__mutmut_7, 
    'x_get_container_logs__mutmut_8': x_get_container_logs__mutmut_8, 
    'x_get_container_logs__mutmut_9': x_get_container_logs__mutmut_9, 
    'x_get_container_logs__mutmut_10': x_get_container_logs__mutmut_10, 
    'x_get_container_logs__mutmut_11': x_get_container_logs__mutmut_11, 
    'x_get_container_logs__mutmut_12': x_get_container_logs__mutmut_12, 
    'x_get_container_logs__mutmut_13': x_get_container_logs__mutmut_13, 
    'x_get_container_logs__mutmut_14': x_get_container_logs__mutmut_14, 
    'x_get_container_logs__mutmut_15': x_get_container_logs__mutmut_15, 
    'x_get_container_logs__mutmut_16': x_get_container_logs__mutmut_16, 
    'x_get_container_logs__mutmut_17': x_get_container_logs__mutmut_17, 
    'x_get_container_logs__mutmut_18': x_get_container_logs__mutmut_18, 
    'x_get_container_logs__mutmut_19': x_get_container_logs__mutmut_19, 
    'x_get_container_logs__mutmut_20': x_get_container_logs__mutmut_20, 
    'x_get_container_logs__mutmut_21': x_get_container_logs__mutmut_21, 
    'x_get_container_logs__mutmut_22': x_get_container_logs__mutmut_22, 
    'x_get_container_logs__mutmut_23': x_get_container_logs__mutmut_23, 
    'x_get_container_logs__mutmut_24': x_get_container_logs__mutmut_24, 
    'x_get_container_logs__mutmut_25': x_get_container_logs__mutmut_25, 
    'x_get_container_logs__mutmut_26': x_get_container_logs__mutmut_26, 
    'x_get_container_logs__mutmut_27': x_get_container_logs__mutmut_27, 
    'x_get_container_logs__mutmut_28': x_get_container_logs__mutmut_28, 
    'x_get_container_logs__mutmut_29': x_get_container_logs__mutmut_29, 
    'x_get_container_logs__mutmut_30': x_get_container_logs__mutmut_30, 
    'x_get_container_logs__mutmut_31': x_get_container_logs__mutmut_31, 
    'x_get_container_logs__mutmut_32': x_get_container_logs__mutmut_32, 
    'x_get_container_logs__mutmut_33': x_get_container_logs__mutmut_33, 
    'x_get_container_logs__mutmut_34': x_get_container_logs__mutmut_34, 
    'x_get_container_logs__mutmut_35': x_get_container_logs__mutmut_35, 
    'x_get_container_logs__mutmut_36': x_get_container_logs__mutmut_36, 
    'x_get_container_logs__mutmut_37': x_get_container_logs__mutmut_37, 
    'x_get_container_logs__mutmut_38': x_get_container_logs__mutmut_38, 
    'x_get_container_logs__mutmut_39': x_get_container_logs__mutmut_39, 
    'x_get_container_logs__mutmut_40': x_get_container_logs__mutmut_40, 
    'x_get_container_logs__mutmut_41': x_get_container_logs__mutmut_41, 
    'x_get_container_logs__mutmut_42': x_get_container_logs__mutmut_42, 
    'x_get_container_logs__mutmut_43': x_get_container_logs__mutmut_43, 
    'x_get_container_logs__mutmut_44': x_get_container_logs__mutmut_44, 
    'x_get_container_logs__mutmut_45': x_get_container_logs__mutmut_45, 
    'x_get_container_logs__mutmut_46': x_get_container_logs__mutmut_46, 
    'x_get_container_logs__mutmut_47': x_get_container_logs__mutmut_47, 
    'x_get_container_logs__mutmut_48': x_get_container_logs__mutmut_48, 
    'x_get_container_logs__mutmut_49': x_get_container_logs__mutmut_49, 
    'x_get_container_logs__mutmut_50': x_get_container_logs__mutmut_50, 
    'x_get_container_logs__mutmut_51': x_get_container_logs__mutmut_51, 
    'x_get_container_logs__mutmut_52': x_get_container_logs__mutmut_52, 
    'x_get_container_logs__mutmut_53': x_get_container_logs__mutmut_53
}

def get_container_logs(*args, **kwargs):
    result = _mutmut_trampoline(x_get_container_logs__mutmut_orig, x_get_container_logs__mutmut_mutants, args, kwargs)
    return result 

get_container_logs.__signature__ = _mutmut_signature(x_get_container_logs__mutmut_orig)
x_get_container_logs__mutmut_orig.__name__ = 'x_get_container_logs'


def x_stream_container_logs__mutmut_orig(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_1(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = None

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_2(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container and not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_3(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_4(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_5(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print(None)
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_6(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("XX[red]❌ Container support is not enabled[/red]XX")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_7(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_8(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[RED]❌ CONTAINER SUPPORT IS NOT ENABLED[/RED]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_9(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return True

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_10(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = None

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_11(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(None)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_12(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_13(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(None)
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_14(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return True

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_15(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(None)
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_16(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print(None)

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_17(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("XX[dim]Press Ctrl+C to stop[/dim]\nXX")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_18(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]press ctrl+c to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_19(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[DIM]PRESS CTRL+C TO STOP[/DIM]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_20(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = None

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_21(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["XXdockerXX", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_22(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["DOCKER", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_23(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "XXlogsXX", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_24(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "LOGS", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_25(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "XX-fXX", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_26(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-F", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_27(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(None):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_28(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern or not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_29(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_30(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(None, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_31(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, None):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_32(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_33(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, ):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_34(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                break

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_35(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = None

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_36(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(None, r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_37(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", None, line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_38(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", None)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_39(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_40(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_41(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", )

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_42(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"XX[bold yellow]\1[/bold yellow]XX", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_43(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[BOLD YELLOW]\1[/BOLD YELLOW]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_44(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(None, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_45(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end=None)

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_46(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_47(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, )

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_48(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="XXXX")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_49(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print(None)
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_50(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("XX\n[yellow]Log streaming stopped[/yellow]XX")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_51(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_52(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[YELLOW]LOG STREAMING STOPPED[/YELLOW]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_53(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return False
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_54(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(None)
        logger.error(f"Log streaming failed: {e}")
        return False

    return True


def x_stream_container_logs__mutmut_55(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(None)
        return False

    return True


def x_stream_container_logs__mutmut_56(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return True

    return True


def x_stream_container_logs__mutmut_57(
    config: WorkenvConfig,
    filter_pattern: str | None = None,
    highlight_pattern: str | None = None,
) -> bool:
    """
    Stream container logs with optional filtering and highlighting.

    Args:
        config: Workenv configuration
        filter_pattern: Regex pattern to filter logs
        highlight_pattern: Pattern to highlight in output

    Returns:
        True if streaming was successful
    """
    console = Console()

    if not config.container or not config.container.enabled:
        console.print("[red]❌ Container support is not enabled[/red]")
        return False

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_exists():
        console.print(f"[yellow]⚠️  Container {manager.container_name} doesn't exist[/yellow]")
        return False

    console.print(f"[green]📜 Streaming logs from {manager.container_name}...[/green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Build command
    cmd = ["docker", "logs", "-f", manager.container_name]

    try:
        import re

        # Start streaming process
        for line in stream(cmd):
            # Apply filter if specified
            if filter_pattern and not re.search(filter_pattern, line):
                continue

            # Apply highlighting if specified
            if highlight_pattern:
                line = re.sub(f"({highlight_pattern})", r"[bold yellow]\1[/bold yellow]", line)

            console.print(line, end="")

    except KeyboardInterrupt:
        console.print("\n[yellow]Log streaming stopped[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Failed to stream logs: {e}[/red]")
        logger.error(f"Log streaming failed: {e}")
        return False

    return False

x_stream_container_logs__mutmut_mutants : ClassVar[MutantDict] = {
'x_stream_container_logs__mutmut_1': x_stream_container_logs__mutmut_1, 
    'x_stream_container_logs__mutmut_2': x_stream_container_logs__mutmut_2, 
    'x_stream_container_logs__mutmut_3': x_stream_container_logs__mutmut_3, 
    'x_stream_container_logs__mutmut_4': x_stream_container_logs__mutmut_4, 
    'x_stream_container_logs__mutmut_5': x_stream_container_logs__mutmut_5, 
    'x_stream_container_logs__mutmut_6': x_stream_container_logs__mutmut_6, 
    'x_stream_container_logs__mutmut_7': x_stream_container_logs__mutmut_7, 
    'x_stream_container_logs__mutmut_8': x_stream_container_logs__mutmut_8, 
    'x_stream_container_logs__mutmut_9': x_stream_container_logs__mutmut_9, 
    'x_stream_container_logs__mutmut_10': x_stream_container_logs__mutmut_10, 
    'x_stream_container_logs__mutmut_11': x_stream_container_logs__mutmut_11, 
    'x_stream_container_logs__mutmut_12': x_stream_container_logs__mutmut_12, 
    'x_stream_container_logs__mutmut_13': x_stream_container_logs__mutmut_13, 
    'x_stream_container_logs__mutmut_14': x_stream_container_logs__mutmut_14, 
    'x_stream_container_logs__mutmut_15': x_stream_container_logs__mutmut_15, 
    'x_stream_container_logs__mutmut_16': x_stream_container_logs__mutmut_16, 
    'x_stream_container_logs__mutmut_17': x_stream_container_logs__mutmut_17, 
    'x_stream_container_logs__mutmut_18': x_stream_container_logs__mutmut_18, 
    'x_stream_container_logs__mutmut_19': x_stream_container_logs__mutmut_19, 
    'x_stream_container_logs__mutmut_20': x_stream_container_logs__mutmut_20, 
    'x_stream_container_logs__mutmut_21': x_stream_container_logs__mutmut_21, 
    'x_stream_container_logs__mutmut_22': x_stream_container_logs__mutmut_22, 
    'x_stream_container_logs__mutmut_23': x_stream_container_logs__mutmut_23, 
    'x_stream_container_logs__mutmut_24': x_stream_container_logs__mutmut_24, 
    'x_stream_container_logs__mutmut_25': x_stream_container_logs__mutmut_25, 
    'x_stream_container_logs__mutmut_26': x_stream_container_logs__mutmut_26, 
    'x_stream_container_logs__mutmut_27': x_stream_container_logs__mutmut_27, 
    'x_stream_container_logs__mutmut_28': x_stream_container_logs__mutmut_28, 
    'x_stream_container_logs__mutmut_29': x_stream_container_logs__mutmut_29, 
    'x_stream_container_logs__mutmut_30': x_stream_container_logs__mutmut_30, 
    'x_stream_container_logs__mutmut_31': x_stream_container_logs__mutmut_31, 
    'x_stream_container_logs__mutmut_32': x_stream_container_logs__mutmut_32, 
    'x_stream_container_logs__mutmut_33': x_stream_container_logs__mutmut_33, 
    'x_stream_container_logs__mutmut_34': x_stream_container_logs__mutmut_34, 
    'x_stream_container_logs__mutmut_35': x_stream_container_logs__mutmut_35, 
    'x_stream_container_logs__mutmut_36': x_stream_container_logs__mutmut_36, 
    'x_stream_container_logs__mutmut_37': x_stream_container_logs__mutmut_37, 
    'x_stream_container_logs__mutmut_38': x_stream_container_logs__mutmut_38, 
    'x_stream_container_logs__mutmut_39': x_stream_container_logs__mutmut_39, 
    'x_stream_container_logs__mutmut_40': x_stream_container_logs__mutmut_40, 
    'x_stream_container_logs__mutmut_41': x_stream_container_logs__mutmut_41, 
    'x_stream_container_logs__mutmut_42': x_stream_container_logs__mutmut_42, 
    'x_stream_container_logs__mutmut_43': x_stream_container_logs__mutmut_43, 
    'x_stream_container_logs__mutmut_44': x_stream_container_logs__mutmut_44, 
    'x_stream_container_logs__mutmut_45': x_stream_container_logs__mutmut_45, 
    'x_stream_container_logs__mutmut_46': x_stream_container_logs__mutmut_46, 
    'x_stream_container_logs__mutmut_47': x_stream_container_logs__mutmut_47, 
    'x_stream_container_logs__mutmut_48': x_stream_container_logs__mutmut_48, 
    'x_stream_container_logs__mutmut_49': x_stream_container_logs__mutmut_49, 
    'x_stream_container_logs__mutmut_50': x_stream_container_logs__mutmut_50, 
    'x_stream_container_logs__mutmut_51': x_stream_container_logs__mutmut_51, 
    'x_stream_container_logs__mutmut_52': x_stream_container_logs__mutmut_52, 
    'x_stream_container_logs__mutmut_53': x_stream_container_logs__mutmut_53, 
    'x_stream_container_logs__mutmut_54': x_stream_container_logs__mutmut_54, 
    'x_stream_container_logs__mutmut_55': x_stream_container_logs__mutmut_55, 
    'x_stream_container_logs__mutmut_56': x_stream_container_logs__mutmut_56, 
    'x_stream_container_logs__mutmut_57': x_stream_container_logs__mutmut_57
}

def stream_container_logs(*args, **kwargs):
    result = _mutmut_trampoline(x_stream_container_logs__mutmut_orig, x_stream_container_logs__mutmut_mutants, args, kwargs)
    return result 

stream_container_logs.__signature__ = _mutmut_signature(x_stream_container_logs__mutmut_orig)
x_stream_container_logs__mutmut_orig.__name__ = 'x_stream_container_logs'


def x_get_container_stats__mutmut_orig(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_1(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container and not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_2(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_3(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_4(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = None

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_5(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(None)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_6(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_7(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = None
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_8(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["XXdockerXX", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_9(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["DOCKER", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_10(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "XXstatsXX", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_11(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "STATS", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_12(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "XX--no-streamXX", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_13(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--NO-STREAM", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_14(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "XX--formatXX", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_15(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--FORMAT", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_16(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "XXjsonXX", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_17(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "JSON", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_18(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = None

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_19(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(None, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_20(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=None)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_21(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_22(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, )

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_23(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=True)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_24(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 or result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_25(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode != 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_26(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 1 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_27(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = None

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_28(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(None)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_29(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "XXnameXX": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_30(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "NAME": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_31(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get(None, manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_32(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", None),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_33(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get(manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_34(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", ),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_35(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("XXNameXX", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_36(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_37(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("NAME", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_38(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "XXcpuXX": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_39(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "CPU": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_40(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get(None, "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_41(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", None),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_42(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_43(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", ),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_44(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("XXCPUPercXX", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_45(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("cpuperc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_46(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPERC", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_47(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "XX0%XX"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_48(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "XXmemoryXX": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_49(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "MEMORY": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_50(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"XXusageXX": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_51(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"USAGE": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_52(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get(None, "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_53(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", None), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_54(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_55(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", ), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_56(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("XXMemUsageXX", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_57(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("memusage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_58(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MEMUSAGE", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_59(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "XX0B / 0BXX"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_60(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0b / 0b"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_61(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "XXpercentXX": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_62(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "PERCENT": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_63(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get(None, "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_64(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", None)},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_65(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_66(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", )},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_67(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("XXMemPercXX", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_68(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("memperc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_69(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MEMPERC", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_70(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "XX0%XX")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_71(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "XXnetworkXX": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_72(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "NETWORK": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_73(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get(None, "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_74(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", None),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_75(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_76(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", ),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_77(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("XXNetIOXX", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_78(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("netio", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_79(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NETIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_80(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "XX0B / 0BXX"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_81(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0b / 0b"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_82(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "XXdiskXX": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_83(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "DISK": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_84(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get(None, "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_85(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", None),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_86(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_87(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", ),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_88(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("XXBlockIOXX", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_89(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("blockio", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_90(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BLOCKIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_91(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "XX0B / 0BXX"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_92(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0b / 0b"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_93(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "XXpidsXX": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_94(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "PIDS": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_95(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get(None, "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_96(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", None),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_97(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_98(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", ),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_99(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("XXPIDsXX", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_100(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("pids", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_101(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDS", "0"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_102(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "XX0XX"),
            }
    except Exception as e:
        logger.error(f"Failed to get container stats: {e}")

    return None


def x_get_container_stats__mutmut_103(config: WorkenvConfig) -> dict[str, Any] | None:
    """
    Get container resource usage statistics.

    Args:
        config: Workenv configuration

    Returns:
        Dictionary with container stats or None
    """
    Console()

    if not config.container or not config.container.enabled:
        return None

    # Reuse existing ContainerManager
    manager = ContainerManager(config)

    if not manager.container_running():
        return None

    try:
        # Get container stats
        cmd = ["docker", "stats", "--no-stream", "--format", "json", manager.container_name]
        result = run(cmd, check=False)

        if result.returncode == 0 and result.stdout:
            import json

            stats = json.loads(result.stdout)

            # Parse and format stats
            return {
                "name": stats.get("Name", manager.container_name),
                "cpu": stats.get("CPUPerc", "0%"),
                "memory": {"usage": stats.get("MemUsage", "0B / 0B"), "percent": stats.get("MemPerc", "0%")},
                "network": stats.get("NetIO", "0B / 0B"),
                "disk": stats.get("BlockIO", "0B / 0B"),
                "pids": stats.get("PIDs", "0"),
            }
    except Exception as e:
        logger.error(None)

    return None

x_get_container_stats__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_container_stats__mutmut_1': x_get_container_stats__mutmut_1, 
    'x_get_container_stats__mutmut_2': x_get_container_stats__mutmut_2, 
    'x_get_container_stats__mutmut_3': x_get_container_stats__mutmut_3, 
    'x_get_container_stats__mutmut_4': x_get_container_stats__mutmut_4, 
    'x_get_container_stats__mutmut_5': x_get_container_stats__mutmut_5, 
    'x_get_container_stats__mutmut_6': x_get_container_stats__mutmut_6, 
    'x_get_container_stats__mutmut_7': x_get_container_stats__mutmut_7, 
    'x_get_container_stats__mutmut_8': x_get_container_stats__mutmut_8, 
    'x_get_container_stats__mutmut_9': x_get_container_stats__mutmut_9, 
    'x_get_container_stats__mutmut_10': x_get_container_stats__mutmut_10, 
    'x_get_container_stats__mutmut_11': x_get_container_stats__mutmut_11, 
    'x_get_container_stats__mutmut_12': x_get_container_stats__mutmut_12, 
    'x_get_container_stats__mutmut_13': x_get_container_stats__mutmut_13, 
    'x_get_container_stats__mutmut_14': x_get_container_stats__mutmut_14, 
    'x_get_container_stats__mutmut_15': x_get_container_stats__mutmut_15, 
    'x_get_container_stats__mutmut_16': x_get_container_stats__mutmut_16, 
    'x_get_container_stats__mutmut_17': x_get_container_stats__mutmut_17, 
    'x_get_container_stats__mutmut_18': x_get_container_stats__mutmut_18, 
    'x_get_container_stats__mutmut_19': x_get_container_stats__mutmut_19, 
    'x_get_container_stats__mutmut_20': x_get_container_stats__mutmut_20, 
    'x_get_container_stats__mutmut_21': x_get_container_stats__mutmut_21, 
    'x_get_container_stats__mutmut_22': x_get_container_stats__mutmut_22, 
    'x_get_container_stats__mutmut_23': x_get_container_stats__mutmut_23, 
    'x_get_container_stats__mutmut_24': x_get_container_stats__mutmut_24, 
    'x_get_container_stats__mutmut_25': x_get_container_stats__mutmut_25, 
    'x_get_container_stats__mutmut_26': x_get_container_stats__mutmut_26, 
    'x_get_container_stats__mutmut_27': x_get_container_stats__mutmut_27, 
    'x_get_container_stats__mutmut_28': x_get_container_stats__mutmut_28, 
    'x_get_container_stats__mutmut_29': x_get_container_stats__mutmut_29, 
    'x_get_container_stats__mutmut_30': x_get_container_stats__mutmut_30, 
    'x_get_container_stats__mutmut_31': x_get_container_stats__mutmut_31, 
    'x_get_container_stats__mutmut_32': x_get_container_stats__mutmut_32, 
    'x_get_container_stats__mutmut_33': x_get_container_stats__mutmut_33, 
    'x_get_container_stats__mutmut_34': x_get_container_stats__mutmut_34, 
    'x_get_container_stats__mutmut_35': x_get_container_stats__mutmut_35, 
    'x_get_container_stats__mutmut_36': x_get_container_stats__mutmut_36, 
    'x_get_container_stats__mutmut_37': x_get_container_stats__mutmut_37, 
    'x_get_container_stats__mutmut_38': x_get_container_stats__mutmut_38, 
    'x_get_container_stats__mutmut_39': x_get_container_stats__mutmut_39, 
    'x_get_container_stats__mutmut_40': x_get_container_stats__mutmut_40, 
    'x_get_container_stats__mutmut_41': x_get_container_stats__mutmut_41, 
    'x_get_container_stats__mutmut_42': x_get_container_stats__mutmut_42, 
    'x_get_container_stats__mutmut_43': x_get_container_stats__mutmut_43, 
    'x_get_container_stats__mutmut_44': x_get_container_stats__mutmut_44, 
    'x_get_container_stats__mutmut_45': x_get_container_stats__mutmut_45, 
    'x_get_container_stats__mutmut_46': x_get_container_stats__mutmut_46, 
    'x_get_container_stats__mutmut_47': x_get_container_stats__mutmut_47, 
    'x_get_container_stats__mutmut_48': x_get_container_stats__mutmut_48, 
    'x_get_container_stats__mutmut_49': x_get_container_stats__mutmut_49, 
    'x_get_container_stats__mutmut_50': x_get_container_stats__mutmut_50, 
    'x_get_container_stats__mutmut_51': x_get_container_stats__mutmut_51, 
    'x_get_container_stats__mutmut_52': x_get_container_stats__mutmut_52, 
    'x_get_container_stats__mutmut_53': x_get_container_stats__mutmut_53, 
    'x_get_container_stats__mutmut_54': x_get_container_stats__mutmut_54, 
    'x_get_container_stats__mutmut_55': x_get_container_stats__mutmut_55, 
    'x_get_container_stats__mutmut_56': x_get_container_stats__mutmut_56, 
    'x_get_container_stats__mutmut_57': x_get_container_stats__mutmut_57, 
    'x_get_container_stats__mutmut_58': x_get_container_stats__mutmut_58, 
    'x_get_container_stats__mutmut_59': x_get_container_stats__mutmut_59, 
    'x_get_container_stats__mutmut_60': x_get_container_stats__mutmut_60, 
    'x_get_container_stats__mutmut_61': x_get_container_stats__mutmut_61, 
    'x_get_container_stats__mutmut_62': x_get_container_stats__mutmut_62, 
    'x_get_container_stats__mutmut_63': x_get_container_stats__mutmut_63, 
    'x_get_container_stats__mutmut_64': x_get_container_stats__mutmut_64, 
    'x_get_container_stats__mutmut_65': x_get_container_stats__mutmut_65, 
    'x_get_container_stats__mutmut_66': x_get_container_stats__mutmut_66, 
    'x_get_container_stats__mutmut_67': x_get_container_stats__mutmut_67, 
    'x_get_container_stats__mutmut_68': x_get_container_stats__mutmut_68, 
    'x_get_container_stats__mutmut_69': x_get_container_stats__mutmut_69, 
    'x_get_container_stats__mutmut_70': x_get_container_stats__mutmut_70, 
    'x_get_container_stats__mutmut_71': x_get_container_stats__mutmut_71, 
    'x_get_container_stats__mutmut_72': x_get_container_stats__mutmut_72, 
    'x_get_container_stats__mutmut_73': x_get_container_stats__mutmut_73, 
    'x_get_container_stats__mutmut_74': x_get_container_stats__mutmut_74, 
    'x_get_container_stats__mutmut_75': x_get_container_stats__mutmut_75, 
    'x_get_container_stats__mutmut_76': x_get_container_stats__mutmut_76, 
    'x_get_container_stats__mutmut_77': x_get_container_stats__mutmut_77, 
    'x_get_container_stats__mutmut_78': x_get_container_stats__mutmut_78, 
    'x_get_container_stats__mutmut_79': x_get_container_stats__mutmut_79, 
    'x_get_container_stats__mutmut_80': x_get_container_stats__mutmut_80, 
    'x_get_container_stats__mutmut_81': x_get_container_stats__mutmut_81, 
    'x_get_container_stats__mutmut_82': x_get_container_stats__mutmut_82, 
    'x_get_container_stats__mutmut_83': x_get_container_stats__mutmut_83, 
    'x_get_container_stats__mutmut_84': x_get_container_stats__mutmut_84, 
    'x_get_container_stats__mutmut_85': x_get_container_stats__mutmut_85, 
    'x_get_container_stats__mutmut_86': x_get_container_stats__mutmut_86, 
    'x_get_container_stats__mutmut_87': x_get_container_stats__mutmut_87, 
    'x_get_container_stats__mutmut_88': x_get_container_stats__mutmut_88, 
    'x_get_container_stats__mutmut_89': x_get_container_stats__mutmut_89, 
    'x_get_container_stats__mutmut_90': x_get_container_stats__mutmut_90, 
    'x_get_container_stats__mutmut_91': x_get_container_stats__mutmut_91, 
    'x_get_container_stats__mutmut_92': x_get_container_stats__mutmut_92, 
    'x_get_container_stats__mutmut_93': x_get_container_stats__mutmut_93, 
    'x_get_container_stats__mutmut_94': x_get_container_stats__mutmut_94, 
    'x_get_container_stats__mutmut_95': x_get_container_stats__mutmut_95, 
    'x_get_container_stats__mutmut_96': x_get_container_stats__mutmut_96, 
    'x_get_container_stats__mutmut_97': x_get_container_stats__mutmut_97, 
    'x_get_container_stats__mutmut_98': x_get_container_stats__mutmut_98, 
    'x_get_container_stats__mutmut_99': x_get_container_stats__mutmut_99, 
    'x_get_container_stats__mutmut_100': x_get_container_stats__mutmut_100, 
    'x_get_container_stats__mutmut_101': x_get_container_stats__mutmut_101, 
    'x_get_container_stats__mutmut_102': x_get_container_stats__mutmut_102, 
    'x_get_container_stats__mutmut_103': x_get_container_stats__mutmut_103
}

def get_container_stats(*args, **kwargs):
    result = _mutmut_trampoline(x_get_container_stats__mutmut_orig, x_get_container_stats__mutmut_mutants, args, kwargs)
    return result 

get_container_stats.__signature__ = _mutmut_signature(x_get_container_stats__mutmut_orig)
x_get_container_stats__mutmut_orig.__name__ = 'x_get_container_stats'


# 🧰🌍🔚
