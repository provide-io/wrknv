#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Container Command Implementations
=================================
Command implementations for container management."""

from __future__ import annotations

from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from wrknv.config import WorkenvConfig

from .manager import ContainerManager
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


def x_build_container__mutmut_orig(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Build the development container image."""
    manager = ContainerManager(config)
    return manager.build_image(rebuild=rebuild)


def x_build_container__mutmut_1(config: WorkenvConfig | None = None, rebuild: bool = True) -> bool:
    """Build the development container image."""
    manager = ContainerManager(config)
    return manager.build_image(rebuild=rebuild)


def x_build_container__mutmut_2(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Build the development container image."""
    manager = None
    return manager.build_image(rebuild=rebuild)


def x_build_container__mutmut_3(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Build the development container image."""
    manager = ContainerManager(None)
    return manager.build_image(rebuild=rebuild)


def x_build_container__mutmut_4(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Build the development container image."""
    manager = ContainerManager(config)
    return manager.build_image(rebuild=None)

x_build_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_container__mutmut_1': x_build_container__mutmut_1, 
    'x_build_container__mutmut_2': x_build_container__mutmut_2, 
    'x_build_container__mutmut_3': x_build_container__mutmut_3, 
    'x_build_container__mutmut_4': x_build_container__mutmut_4
}

def build_container(*args, **kwargs):
    result = _mutmut_trampoline(x_build_container__mutmut_orig, x_build_container__mutmut_mutants, args, kwargs)
    return result 

build_container.__signature__ = _mutmut_signature(x_build_container__mutmut_orig)
x_build_container__mutmut_orig.__name__ = 'x_build_container'


def x_start_container__mutmut_orig(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Start the development container."""
    manager = ContainerManager(config)
    return manager.start(force_rebuild=rebuild)


def x_start_container__mutmut_1(config: WorkenvConfig | None = None, rebuild: bool = True) -> bool:
    """Start the development container."""
    manager = ContainerManager(config)
    return manager.start(force_rebuild=rebuild)


def x_start_container__mutmut_2(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Start the development container."""
    manager = None
    return manager.start(force_rebuild=rebuild)


def x_start_container__mutmut_3(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Start the development container."""
    manager = ContainerManager(None)
    return manager.start(force_rebuild=rebuild)


def x_start_container__mutmut_4(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Start the development container."""
    manager = ContainerManager(config)
    return manager.start(force_rebuild=None)

x_start_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_start_container__mutmut_1': x_start_container__mutmut_1, 
    'x_start_container__mutmut_2': x_start_container__mutmut_2, 
    'x_start_container__mutmut_3': x_start_container__mutmut_3, 
    'x_start_container__mutmut_4': x_start_container__mutmut_4
}

def start_container(*args, **kwargs):
    result = _mutmut_trampoline(x_start_container__mutmut_orig, x_start_container__mutmut_mutants, args, kwargs)
    return result 

start_container.__signature__ = _mutmut_signature(x_start_container__mutmut_orig)
x_start_container__mutmut_orig.__name__ = 'x_start_container'


def x_enter_container__mutmut_orig(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_1(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = True,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_2(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = None
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_3(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(None)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_4(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=None,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_5(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=None,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_6(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=None,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_7(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=None,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_8(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=None,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_9(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=None,
    )


def x_enter_container__mutmut_10(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_11(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        working_dir=working_dir,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_12(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        environment=environment,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_13(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        user=user,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_14(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        auto_start=auto_start,
    )


def x_enter_container__mutmut_15(
    config: WorkenvConfig | None = None,
    command: list[str] | None = None,
    shell: str | None = None,
    working_dir: str | None = None,
    environment: dict[str, str] | None = None,
    user: str | None = None,
    auto_start: bool = False,
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(  # nosec B604 - shell is shell path, not subprocess shell=True
        command=command,
        shell=shell,
        working_dir=working_dir,
        environment=environment,
        user=user,
        )

x_enter_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_enter_container__mutmut_1': x_enter_container__mutmut_1, 
    'x_enter_container__mutmut_2': x_enter_container__mutmut_2, 
    'x_enter_container__mutmut_3': x_enter_container__mutmut_3, 
    'x_enter_container__mutmut_4': x_enter_container__mutmut_4, 
    'x_enter_container__mutmut_5': x_enter_container__mutmut_5, 
    'x_enter_container__mutmut_6': x_enter_container__mutmut_6, 
    'x_enter_container__mutmut_7': x_enter_container__mutmut_7, 
    'x_enter_container__mutmut_8': x_enter_container__mutmut_8, 
    'x_enter_container__mutmut_9': x_enter_container__mutmut_9, 
    'x_enter_container__mutmut_10': x_enter_container__mutmut_10, 
    'x_enter_container__mutmut_11': x_enter_container__mutmut_11, 
    'x_enter_container__mutmut_12': x_enter_container__mutmut_12, 
    'x_enter_container__mutmut_13': x_enter_container__mutmut_13, 
    'x_enter_container__mutmut_14': x_enter_container__mutmut_14, 
    'x_enter_container__mutmut_15': x_enter_container__mutmut_15
}

def enter_container(*args, **kwargs):
    result = _mutmut_trampoline(x_enter_container__mutmut_orig, x_enter_container__mutmut_mutants, args, kwargs)
    return result 

enter_container.__signature__ = _mutmut_signature(x_enter_container__mutmut_orig)
x_enter_container__mutmut_orig.__name__ = 'x_enter_container'


def x_stop_container__mutmut_orig(config: WorkenvConfig | None = None) -> bool:
    """Stop the development container."""
    manager = ContainerManager(config)
    return manager.stop()


def x_stop_container__mutmut_1(config: WorkenvConfig | None = None) -> bool:
    """Stop the development container."""
    manager = None
    return manager.stop()


def x_stop_container__mutmut_2(config: WorkenvConfig | None = None) -> bool:
    """Stop the development container."""
    manager = ContainerManager(None)
    return manager.stop()

x_stop_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_stop_container__mutmut_1': x_stop_container__mutmut_1, 
    'x_stop_container__mutmut_2': x_stop_container__mutmut_2
}

def stop_container(*args, **kwargs):
    result = _mutmut_trampoline(x_stop_container__mutmut_orig, x_stop_container__mutmut_mutants, args, kwargs)
    return result 

stop_container.__signature__ = _mutmut_signature(x_stop_container__mutmut_orig)
x_stop_container__mutmut_orig.__name__ = 'x_stop_container'


def x_restart_container__mutmut_orig(config: WorkenvConfig | None = None) -> bool:
    """Restart the development container."""
    manager = ContainerManager(config)
    return manager.restart()


def x_restart_container__mutmut_1(config: WorkenvConfig | None = None) -> bool:
    """Restart the development container."""
    manager = None
    return manager.restart()


def x_restart_container__mutmut_2(config: WorkenvConfig | None = None) -> bool:
    """Restart the development container."""
    manager = ContainerManager(None)
    return manager.restart()

x_restart_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_restart_container__mutmut_1': x_restart_container__mutmut_1, 
    'x_restart_container__mutmut_2': x_restart_container__mutmut_2
}

def restart_container(*args, **kwargs):
    result = _mutmut_trampoline(x_restart_container__mutmut_orig, x_restart_container__mutmut_mutants, args, kwargs)
    return result 

restart_container.__signature__ = _mutmut_signature(x_restart_container__mutmut_orig)
x_restart_container__mutmut_orig.__name__ = 'x_restart_container'


def x_container_status__mutmut_orig(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_1(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = None
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_2(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(None)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_3(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = None

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_4(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = None

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_5(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_6(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["XXdocker_availableXX"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_7(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["DOCKER_AVAILABLE"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_8(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = None
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_9(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "XX[red]❌ Not Available[/red]XX"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_10(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ not available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_11(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[RED]❌ NOT AVAILABLE[/RED]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_12(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = None

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_13(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "XX[green]✅ Available[/green]XX"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_14(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_15(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[GREEN]✅ AVAILABLE[/GREEN]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_16(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = None

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_17(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "XX[red]❌ Not Found[/red]XX" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_18(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ not found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_19(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[RED]❌ NOT FOUND[/RED]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_20(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_21(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["XXimage_foundXX"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_22(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["IMAGE_FOUND"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_23(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "XX[green]✅ Found[/green]XX"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_24(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_25(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[GREEN]✅ FOUND[/GREEN]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_26(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = None
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_27(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title=None, show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_28(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=None)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_29(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_30(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", )
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_31(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="XX📊 Container StatusXX", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_32(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 container status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_33(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 CONTAINER STATUS", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_34(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=False)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_35(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column(None, style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_36(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style=None)
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_37(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column(style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_38(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", )
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_39(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("XXPropertyXX", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_40(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_41(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("PROPERTY", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_42(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="XXcyanXX")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_43(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="CYAN")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_44(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column(None, style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_45(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style=None)

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_46(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column(style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_47(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", )

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_48(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("XXStatusXX", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_49(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_50(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("STATUS", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_51(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="XXgreenXX")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_52(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="GREEN")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_53(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row(None, docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_54(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", None)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_55(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row(docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_56(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", )

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_57(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("XXDockerXX", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_58(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_59(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("DOCKER", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_60(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(None, image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_61(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", None)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_62(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_63(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", )

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_64(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["XXcontainer_existsXX"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_65(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["CONTAINER_EXISTS"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_66(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = None
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_67(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "XX\U0001f7e2 RunningXX" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_68(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_69(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001F7E2 RUNNING" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_70(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["XXcontainer_runningXX"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_71(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["CONTAINER_RUNNING"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_72(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "XX\U0001f7e1 StoppedXX"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_73(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_74(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001F7E1 STOPPED"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_75(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = None
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_76(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "XX❌ Not CreatedXX"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_77(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ not created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_78(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ NOT CREATED"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_79(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(None, container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_80(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", None)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_81(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_82(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", )

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_83(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["XXcontainer_infoXX"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_84(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["CONTAINER_INFO"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_85(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = None
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_86(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["XXcontainer_infoXX"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_87(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["CONTAINER_INFO"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_88(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row(None, info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_89(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", None)
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_90(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row(info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_91(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", )
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_92(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("XXContainer IDXX", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_93(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("container id", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_94(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("CONTAINER ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_95(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get(None, "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_96(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", None))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_97(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_98(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", ))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_99(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("XXidXX", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_100(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("ID", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_101(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "XXN/AXX"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_102(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "n/a"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_103(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row(None, info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_104(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", None)

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_105(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row(info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_106(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", )

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_107(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("XXStateXX", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_108(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("state", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_109(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("STATE", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_110(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get(None, "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_111(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", None))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_112(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_113(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", ))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_114(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("XXstateXX", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_115(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("STATE", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_116(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "XXN/AXX"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_117(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "n/a"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_118(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(None)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_119(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_120(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["XXdocker_availableXX"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_121(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["DOCKER_AVAILABLE"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_122(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print(None)
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_123(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("XX\n[yellow]Please install Docker to use container features[/yellow]XX")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_124(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]please install docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_125(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[YELLOW]PLEASE INSTALL DOCKER TO USE CONTAINER FEATURES[/YELLOW]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_126(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_127(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["XXcontainer_runningXX"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_128(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["CONTAINER_RUNNING"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_129(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print(None)
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_130(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("XX\n[dim]Run 'wrknv container start' to start the container[/dim]XX")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_131(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_132(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[DIM]RUN 'WRKNV CONTAINER START' TO START THE CONTAINER[/DIM]")
    else:
        console.print("\n[dim]Run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_133(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print(None)


def x_container_status__mutmut_134(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("XX\n[dim]Run 'wrknv container enter' to access the container[/dim]XX")


def x_container_status__mutmut_135(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[dim]run 'wrknv container enter' to access the container[/dim]")


def x_container_status__mutmut_136(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Docker status
    if not status["docker_available"]:
        docker_status = "[red]❌ Not Available[/red]"
    else:
        docker_status = "[green]✅ Available[/green]"

    # Image status
    image_status = "[red]❌ Not Found[/red]" if not status["image_found"] else "[green]✅ Found[/green]"

    # Create status table
    table = Table(title="📊 Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    table.add_row("Docker", docker_status)

    # Image status
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        container_status = "\U0001f7e2 Running" if status["container_running"] else "\U0001f7e1 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.container_name})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print("\n[yellow]Please install Docker to use container features[/yellow]")
    elif not status["container_running"]:
        console.print("\n[dim]Run 'wrknv container start' to start the container[/dim]")
    else:
        console.print("\n[DIM]RUN 'WRKNV CONTAINER ENTER' TO ACCESS THE CONTAINER[/DIM]")

x_container_status__mutmut_mutants : ClassVar[MutantDict] = {
'x_container_status__mutmut_1': x_container_status__mutmut_1, 
    'x_container_status__mutmut_2': x_container_status__mutmut_2, 
    'x_container_status__mutmut_3': x_container_status__mutmut_3, 
    'x_container_status__mutmut_4': x_container_status__mutmut_4, 
    'x_container_status__mutmut_5': x_container_status__mutmut_5, 
    'x_container_status__mutmut_6': x_container_status__mutmut_6, 
    'x_container_status__mutmut_7': x_container_status__mutmut_7, 
    'x_container_status__mutmut_8': x_container_status__mutmut_8, 
    'x_container_status__mutmut_9': x_container_status__mutmut_9, 
    'x_container_status__mutmut_10': x_container_status__mutmut_10, 
    'x_container_status__mutmut_11': x_container_status__mutmut_11, 
    'x_container_status__mutmut_12': x_container_status__mutmut_12, 
    'x_container_status__mutmut_13': x_container_status__mutmut_13, 
    'x_container_status__mutmut_14': x_container_status__mutmut_14, 
    'x_container_status__mutmut_15': x_container_status__mutmut_15, 
    'x_container_status__mutmut_16': x_container_status__mutmut_16, 
    'x_container_status__mutmut_17': x_container_status__mutmut_17, 
    'x_container_status__mutmut_18': x_container_status__mutmut_18, 
    'x_container_status__mutmut_19': x_container_status__mutmut_19, 
    'x_container_status__mutmut_20': x_container_status__mutmut_20, 
    'x_container_status__mutmut_21': x_container_status__mutmut_21, 
    'x_container_status__mutmut_22': x_container_status__mutmut_22, 
    'x_container_status__mutmut_23': x_container_status__mutmut_23, 
    'x_container_status__mutmut_24': x_container_status__mutmut_24, 
    'x_container_status__mutmut_25': x_container_status__mutmut_25, 
    'x_container_status__mutmut_26': x_container_status__mutmut_26, 
    'x_container_status__mutmut_27': x_container_status__mutmut_27, 
    'x_container_status__mutmut_28': x_container_status__mutmut_28, 
    'x_container_status__mutmut_29': x_container_status__mutmut_29, 
    'x_container_status__mutmut_30': x_container_status__mutmut_30, 
    'x_container_status__mutmut_31': x_container_status__mutmut_31, 
    'x_container_status__mutmut_32': x_container_status__mutmut_32, 
    'x_container_status__mutmut_33': x_container_status__mutmut_33, 
    'x_container_status__mutmut_34': x_container_status__mutmut_34, 
    'x_container_status__mutmut_35': x_container_status__mutmut_35, 
    'x_container_status__mutmut_36': x_container_status__mutmut_36, 
    'x_container_status__mutmut_37': x_container_status__mutmut_37, 
    'x_container_status__mutmut_38': x_container_status__mutmut_38, 
    'x_container_status__mutmut_39': x_container_status__mutmut_39, 
    'x_container_status__mutmut_40': x_container_status__mutmut_40, 
    'x_container_status__mutmut_41': x_container_status__mutmut_41, 
    'x_container_status__mutmut_42': x_container_status__mutmut_42, 
    'x_container_status__mutmut_43': x_container_status__mutmut_43, 
    'x_container_status__mutmut_44': x_container_status__mutmut_44, 
    'x_container_status__mutmut_45': x_container_status__mutmut_45, 
    'x_container_status__mutmut_46': x_container_status__mutmut_46, 
    'x_container_status__mutmut_47': x_container_status__mutmut_47, 
    'x_container_status__mutmut_48': x_container_status__mutmut_48, 
    'x_container_status__mutmut_49': x_container_status__mutmut_49, 
    'x_container_status__mutmut_50': x_container_status__mutmut_50, 
    'x_container_status__mutmut_51': x_container_status__mutmut_51, 
    'x_container_status__mutmut_52': x_container_status__mutmut_52, 
    'x_container_status__mutmut_53': x_container_status__mutmut_53, 
    'x_container_status__mutmut_54': x_container_status__mutmut_54, 
    'x_container_status__mutmut_55': x_container_status__mutmut_55, 
    'x_container_status__mutmut_56': x_container_status__mutmut_56, 
    'x_container_status__mutmut_57': x_container_status__mutmut_57, 
    'x_container_status__mutmut_58': x_container_status__mutmut_58, 
    'x_container_status__mutmut_59': x_container_status__mutmut_59, 
    'x_container_status__mutmut_60': x_container_status__mutmut_60, 
    'x_container_status__mutmut_61': x_container_status__mutmut_61, 
    'x_container_status__mutmut_62': x_container_status__mutmut_62, 
    'x_container_status__mutmut_63': x_container_status__mutmut_63, 
    'x_container_status__mutmut_64': x_container_status__mutmut_64, 
    'x_container_status__mutmut_65': x_container_status__mutmut_65, 
    'x_container_status__mutmut_66': x_container_status__mutmut_66, 
    'x_container_status__mutmut_67': x_container_status__mutmut_67, 
    'x_container_status__mutmut_68': x_container_status__mutmut_68, 
    'x_container_status__mutmut_69': x_container_status__mutmut_69, 
    'x_container_status__mutmut_70': x_container_status__mutmut_70, 
    'x_container_status__mutmut_71': x_container_status__mutmut_71, 
    'x_container_status__mutmut_72': x_container_status__mutmut_72, 
    'x_container_status__mutmut_73': x_container_status__mutmut_73, 
    'x_container_status__mutmut_74': x_container_status__mutmut_74, 
    'x_container_status__mutmut_75': x_container_status__mutmut_75, 
    'x_container_status__mutmut_76': x_container_status__mutmut_76, 
    'x_container_status__mutmut_77': x_container_status__mutmut_77, 
    'x_container_status__mutmut_78': x_container_status__mutmut_78, 
    'x_container_status__mutmut_79': x_container_status__mutmut_79, 
    'x_container_status__mutmut_80': x_container_status__mutmut_80, 
    'x_container_status__mutmut_81': x_container_status__mutmut_81, 
    'x_container_status__mutmut_82': x_container_status__mutmut_82, 
    'x_container_status__mutmut_83': x_container_status__mutmut_83, 
    'x_container_status__mutmut_84': x_container_status__mutmut_84, 
    'x_container_status__mutmut_85': x_container_status__mutmut_85, 
    'x_container_status__mutmut_86': x_container_status__mutmut_86, 
    'x_container_status__mutmut_87': x_container_status__mutmut_87, 
    'x_container_status__mutmut_88': x_container_status__mutmut_88, 
    'x_container_status__mutmut_89': x_container_status__mutmut_89, 
    'x_container_status__mutmut_90': x_container_status__mutmut_90, 
    'x_container_status__mutmut_91': x_container_status__mutmut_91, 
    'x_container_status__mutmut_92': x_container_status__mutmut_92, 
    'x_container_status__mutmut_93': x_container_status__mutmut_93, 
    'x_container_status__mutmut_94': x_container_status__mutmut_94, 
    'x_container_status__mutmut_95': x_container_status__mutmut_95, 
    'x_container_status__mutmut_96': x_container_status__mutmut_96, 
    'x_container_status__mutmut_97': x_container_status__mutmut_97, 
    'x_container_status__mutmut_98': x_container_status__mutmut_98, 
    'x_container_status__mutmut_99': x_container_status__mutmut_99, 
    'x_container_status__mutmut_100': x_container_status__mutmut_100, 
    'x_container_status__mutmut_101': x_container_status__mutmut_101, 
    'x_container_status__mutmut_102': x_container_status__mutmut_102, 
    'x_container_status__mutmut_103': x_container_status__mutmut_103, 
    'x_container_status__mutmut_104': x_container_status__mutmut_104, 
    'x_container_status__mutmut_105': x_container_status__mutmut_105, 
    'x_container_status__mutmut_106': x_container_status__mutmut_106, 
    'x_container_status__mutmut_107': x_container_status__mutmut_107, 
    'x_container_status__mutmut_108': x_container_status__mutmut_108, 
    'x_container_status__mutmut_109': x_container_status__mutmut_109, 
    'x_container_status__mutmut_110': x_container_status__mutmut_110, 
    'x_container_status__mutmut_111': x_container_status__mutmut_111, 
    'x_container_status__mutmut_112': x_container_status__mutmut_112, 
    'x_container_status__mutmut_113': x_container_status__mutmut_113, 
    'x_container_status__mutmut_114': x_container_status__mutmut_114, 
    'x_container_status__mutmut_115': x_container_status__mutmut_115, 
    'x_container_status__mutmut_116': x_container_status__mutmut_116, 
    'x_container_status__mutmut_117': x_container_status__mutmut_117, 
    'x_container_status__mutmut_118': x_container_status__mutmut_118, 
    'x_container_status__mutmut_119': x_container_status__mutmut_119, 
    'x_container_status__mutmut_120': x_container_status__mutmut_120, 
    'x_container_status__mutmut_121': x_container_status__mutmut_121, 
    'x_container_status__mutmut_122': x_container_status__mutmut_122, 
    'x_container_status__mutmut_123': x_container_status__mutmut_123, 
    'x_container_status__mutmut_124': x_container_status__mutmut_124, 
    'x_container_status__mutmut_125': x_container_status__mutmut_125, 
    'x_container_status__mutmut_126': x_container_status__mutmut_126, 
    'x_container_status__mutmut_127': x_container_status__mutmut_127, 
    'x_container_status__mutmut_128': x_container_status__mutmut_128, 
    'x_container_status__mutmut_129': x_container_status__mutmut_129, 
    'x_container_status__mutmut_130': x_container_status__mutmut_130, 
    'x_container_status__mutmut_131': x_container_status__mutmut_131, 
    'x_container_status__mutmut_132': x_container_status__mutmut_132, 
    'x_container_status__mutmut_133': x_container_status__mutmut_133, 
    'x_container_status__mutmut_134': x_container_status__mutmut_134, 
    'x_container_status__mutmut_135': x_container_status__mutmut_135, 
    'x_container_status__mutmut_136': x_container_status__mutmut_136
}

def container_status(*args, **kwargs):
    result = _mutmut_trampoline(x_container_status__mutmut_orig, x_container_status__mutmut_mutants, args, kwargs)
    return result 

container_status.__signature__ = _mutmut_signature(x_container_status__mutmut_orig)
x_container_status__mutmut_orig.__name__ = 'x_container_status'


def x_container_logs__mutmut_orig(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_1(
    config: WorkenvConfig | None = None,
    follow: bool = True,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_2(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 101,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_3(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = True,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_4(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = True,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_5(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = None
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_6(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(None)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_7(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=None,
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_8(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=None,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_9(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=None,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_10(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        timestamps=None,
    )


def x_container_logs__mutmut_11(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        tail=tail,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_12(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        since=since,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_13(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        timestamps=timestamps,
    )


def x_container_logs__mutmut_14(
    config: WorkenvConfig | None = None,
    follow: bool = False,
    tail: int = 100,
    since: str | None = None,
    timestamps: bool = False,
    details: bool = False,
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    # Note: details parameter is ignored for now
    manager.logs.get_logs(
        follow=follow,
        tail=tail,
        since=since,
        )

x_container_logs__mutmut_mutants : ClassVar[MutantDict] = {
'x_container_logs__mutmut_1': x_container_logs__mutmut_1, 
    'x_container_logs__mutmut_2': x_container_logs__mutmut_2, 
    'x_container_logs__mutmut_3': x_container_logs__mutmut_3, 
    'x_container_logs__mutmut_4': x_container_logs__mutmut_4, 
    'x_container_logs__mutmut_5': x_container_logs__mutmut_5, 
    'x_container_logs__mutmut_6': x_container_logs__mutmut_6, 
    'x_container_logs__mutmut_7': x_container_logs__mutmut_7, 
    'x_container_logs__mutmut_8': x_container_logs__mutmut_8, 
    'x_container_logs__mutmut_9': x_container_logs__mutmut_9, 
    'x_container_logs__mutmut_10': x_container_logs__mutmut_10, 
    'x_container_logs__mutmut_11': x_container_logs__mutmut_11, 
    'x_container_logs__mutmut_12': x_container_logs__mutmut_12, 
    'x_container_logs__mutmut_13': x_container_logs__mutmut_13, 
    'x_container_logs__mutmut_14': x_container_logs__mutmut_14
}

def container_logs(*args, **kwargs):
    result = _mutmut_trampoline(x_container_logs__mutmut_orig, x_container_logs__mutmut_mutants, args, kwargs)
    return result 

container_logs.__signature__ = _mutmut_signature(x_container_logs__mutmut_orig)
x_container_logs__mutmut_orig.__name__ = 'x_container_logs'


def x_clean_container__mutmut_orig(config: WorkenvConfig | None = None) -> bool:
    """Clean up container and image."""
    manager = ContainerManager(config)
    return manager.clean()


def x_clean_container__mutmut_1(config: WorkenvConfig | None = None) -> bool:
    """Clean up container and image."""
    manager = None
    return manager.clean()


def x_clean_container__mutmut_2(config: WorkenvConfig | None = None) -> bool:
    """Clean up container and image."""
    manager = ContainerManager(None)
    return manager.clean()

x_clean_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_clean_container__mutmut_1': x_clean_container__mutmut_1, 
    'x_clean_container__mutmut_2': x_clean_container__mutmut_2
}

def clean_container(*args, **kwargs):
    result = _mutmut_trampoline(x_clean_container__mutmut_orig, x_clean_container__mutmut_mutants, args, kwargs)
    return result 

clean_container.__signature__ = _mutmut_signature(x_clean_container__mutmut_orig)
x_clean_container__mutmut_orig.__name__ = 'x_clean_container'


def x_rebuild_container__mutmut_orig(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_1(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = None
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_2(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(None)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_3(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = None

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_4(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print(None)

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_5(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("XX🔨 Rebuilding container from scratch...XX")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_6(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_7(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 REBUILDING CONTAINER FROM SCRATCH...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_8(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_9(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return True

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_10(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_11(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=None):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_12(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=False):
        return False

    # Start new container
    return manager.start()


def x_rebuild_container__mutmut_13(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print("🔨 Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return True

    # Start new container
    return manager.start()

x_rebuild_container__mutmut_mutants : ClassVar[MutantDict] = {
'x_rebuild_container__mutmut_1': x_rebuild_container__mutmut_1, 
    'x_rebuild_container__mutmut_2': x_rebuild_container__mutmut_2, 
    'x_rebuild_container__mutmut_3': x_rebuild_container__mutmut_3, 
    'x_rebuild_container__mutmut_4': x_rebuild_container__mutmut_4, 
    'x_rebuild_container__mutmut_5': x_rebuild_container__mutmut_5, 
    'x_rebuild_container__mutmut_6': x_rebuild_container__mutmut_6, 
    'x_rebuild_container__mutmut_7': x_rebuild_container__mutmut_7, 
    'x_rebuild_container__mutmut_8': x_rebuild_container__mutmut_8, 
    'x_rebuild_container__mutmut_9': x_rebuild_container__mutmut_9, 
    'x_rebuild_container__mutmut_10': x_rebuild_container__mutmut_10, 
    'x_rebuild_container__mutmut_11': x_rebuild_container__mutmut_11, 
    'x_rebuild_container__mutmut_12': x_rebuild_container__mutmut_12, 
    'x_rebuild_container__mutmut_13': x_rebuild_container__mutmut_13
}

def rebuild_container(*args, **kwargs):
    result = _mutmut_trampoline(x_rebuild_container__mutmut_orig, x_rebuild_container__mutmut_mutants, args, kwargs)
    return result 

rebuild_container.__signature__ = _mutmut_signature(x_rebuild_container__mutmut_orig)
x_rebuild_container__mutmut_orig.__name__ = 'x_rebuild_container'


def x_list_volumes__mutmut_orig(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_1(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = None
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_2(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(None)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_3(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = None

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_4(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = None

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_5(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_6(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print(None)
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_7(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("XX[yellow]No volumes found[/yellow]XX")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_8(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]no volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_9(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[YELLOW]NO VOLUMES FOUND[/YELLOW]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_10(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = None
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_11(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title=None, show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_12(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=None)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_13(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_14(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", )
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_15(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="XX📦 Container VolumesXX", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_16(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 container volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_17(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 CONTAINER VOLUMES", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_18(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=False)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_19(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column(None, style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_20(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style=None)
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_21(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column(style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_22(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", )
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_23(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("XXVolumeXX", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_24(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_25(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("VOLUME", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_26(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="XXcyanXX")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_27(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="CYAN")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_28(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column(None, style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_29(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style=None)
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_30(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column(style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_31(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", )
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_32(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("XXPathXX", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_33(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_34(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("PATH", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_35(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="XXdimXX")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_36(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="DIM")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_37(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column(None, style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_38(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style=None)
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_39(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column(style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_40(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", )
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_41(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("XXStatusXX", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_42(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_43(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("STATUS", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_44(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="XXgreenXX")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_45(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="GREEN")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_46(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column(None, justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_47(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify=None)
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_48(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column(justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_49(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", )
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_50(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("XXSizeXX", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_51(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_52(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("SIZE", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_53(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="XXrightXX")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_54(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="RIGHT")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_55(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column(None, justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_56(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify=None)

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_57(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column(justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_58(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", )

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_59(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("XXFilesXX", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_60(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_61(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("FILES", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_62(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="XXrightXX")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_63(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="RIGHT")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_64(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = None
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_65(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["XXsizeXX"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_66(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["SIZE"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_67(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size >= 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_68(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 / 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_69(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 / 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_70(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1025 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_71(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1025 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_72(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1025:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_73(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = None
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_74(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size * (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_75(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 / 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_76(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 / 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_77(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1025 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_78(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1025 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_79(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1025):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_80(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size >= 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_81(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 / 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_82(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1025 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_83(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1025:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_84(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = None
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_85(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size * (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_86(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 / 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_87(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1025 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_88(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1025):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_89(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size >= 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_90(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1025:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_91(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = None
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_92(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size * 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_93(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1025:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_94(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = None

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_95(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = None
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_96(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['XXfilesXX']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_97(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['FILES']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_98(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["XXexistsXX"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_99(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["EXISTS"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_100(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "XX-XX"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_101(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = None

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_102(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "XX[green]✅ Mounted[/green]XX" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_103(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_104(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[GREEN]✅ MOUNTED[/GREEN]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_105(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["XXexistsXX"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_106(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["EXISTS"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_107(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "XX[yellow]⚠️ Not Mounted[/yellow]XX"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_108(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ not mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_109(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[YELLOW]⚠️ NOT MOUNTED[/YELLOW]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_110(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(None, volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_111(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], None, status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_112(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], None, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_113(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, None, files_str)

    console.print(table)


def x_list_volumes__mutmut_114(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", None)

    console.print(table)


def x_list_volumes__mutmut_115(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_116(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_117(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_118(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, files_str)

    console.print(table)


def x_list_volumes__mutmut_119(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", )

    console.print(table)


def x_list_volumes__mutmut_120(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["XXnameXX"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_121(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["NAME"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_122(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["XXpathXX"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_123(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["PATH"], status, size_str if volume["exists"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_124(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["XXexistsXX"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_125(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["EXISTS"] else "-", files_str)

    console.print(table)


def x_list_volumes__mutmut_126(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "XX-XX", files_str)

    console.print(table)


def x_list_volumes__mutmut_127(config: WorkenvConfig | None = None) -> None:
    """List container volumes with information."""
    manager = ContainerManager(config)
    console = Console()

    volumes = manager.list_volumes()

    if not volumes:
        console.print("[yellow]No volumes found[/yellow]")
        return

    # Create table
    table = Table(title="📦 Container Volumes", show_header=True)
    table.add_column("Volume", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Status", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Files", justify="right")

    for volume in volumes:
        # Format size
        size = volume["size"]
        if size > 1024 * 1024 * 1024:  # GB
            size_str = f"{size / (1024 * 1024 * 1024):.1f} GB"
        elif size > 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.1f} MB"
        elif size > 1024:  # KB
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"

        files_str = f"{volume['files']} files" if volume["exists"] else "-"
        status = "[green]✅ Mounted[/green]" if volume["exists"] else "[yellow]⚠️ Not Mounted[/yellow]"

        table.add_row(volume["name"], volume["path"], status, size_str if volume["exists"] else "-", files_str)

    console.print(None)

x_list_volumes__mutmut_mutants : ClassVar[MutantDict] = {
'x_list_volumes__mutmut_1': x_list_volumes__mutmut_1, 
    'x_list_volumes__mutmut_2': x_list_volumes__mutmut_2, 
    'x_list_volumes__mutmut_3': x_list_volumes__mutmut_3, 
    'x_list_volumes__mutmut_4': x_list_volumes__mutmut_4, 
    'x_list_volumes__mutmut_5': x_list_volumes__mutmut_5, 
    'x_list_volumes__mutmut_6': x_list_volumes__mutmut_6, 
    'x_list_volumes__mutmut_7': x_list_volumes__mutmut_7, 
    'x_list_volumes__mutmut_8': x_list_volumes__mutmut_8, 
    'x_list_volumes__mutmut_9': x_list_volumes__mutmut_9, 
    'x_list_volumes__mutmut_10': x_list_volumes__mutmut_10, 
    'x_list_volumes__mutmut_11': x_list_volumes__mutmut_11, 
    'x_list_volumes__mutmut_12': x_list_volumes__mutmut_12, 
    'x_list_volumes__mutmut_13': x_list_volumes__mutmut_13, 
    'x_list_volumes__mutmut_14': x_list_volumes__mutmut_14, 
    'x_list_volumes__mutmut_15': x_list_volumes__mutmut_15, 
    'x_list_volumes__mutmut_16': x_list_volumes__mutmut_16, 
    'x_list_volumes__mutmut_17': x_list_volumes__mutmut_17, 
    'x_list_volumes__mutmut_18': x_list_volumes__mutmut_18, 
    'x_list_volumes__mutmut_19': x_list_volumes__mutmut_19, 
    'x_list_volumes__mutmut_20': x_list_volumes__mutmut_20, 
    'x_list_volumes__mutmut_21': x_list_volumes__mutmut_21, 
    'x_list_volumes__mutmut_22': x_list_volumes__mutmut_22, 
    'x_list_volumes__mutmut_23': x_list_volumes__mutmut_23, 
    'x_list_volumes__mutmut_24': x_list_volumes__mutmut_24, 
    'x_list_volumes__mutmut_25': x_list_volumes__mutmut_25, 
    'x_list_volumes__mutmut_26': x_list_volumes__mutmut_26, 
    'x_list_volumes__mutmut_27': x_list_volumes__mutmut_27, 
    'x_list_volumes__mutmut_28': x_list_volumes__mutmut_28, 
    'x_list_volumes__mutmut_29': x_list_volumes__mutmut_29, 
    'x_list_volumes__mutmut_30': x_list_volumes__mutmut_30, 
    'x_list_volumes__mutmut_31': x_list_volumes__mutmut_31, 
    'x_list_volumes__mutmut_32': x_list_volumes__mutmut_32, 
    'x_list_volumes__mutmut_33': x_list_volumes__mutmut_33, 
    'x_list_volumes__mutmut_34': x_list_volumes__mutmut_34, 
    'x_list_volumes__mutmut_35': x_list_volumes__mutmut_35, 
    'x_list_volumes__mutmut_36': x_list_volumes__mutmut_36, 
    'x_list_volumes__mutmut_37': x_list_volumes__mutmut_37, 
    'x_list_volumes__mutmut_38': x_list_volumes__mutmut_38, 
    'x_list_volumes__mutmut_39': x_list_volumes__mutmut_39, 
    'x_list_volumes__mutmut_40': x_list_volumes__mutmut_40, 
    'x_list_volumes__mutmut_41': x_list_volumes__mutmut_41, 
    'x_list_volumes__mutmut_42': x_list_volumes__mutmut_42, 
    'x_list_volumes__mutmut_43': x_list_volumes__mutmut_43, 
    'x_list_volumes__mutmut_44': x_list_volumes__mutmut_44, 
    'x_list_volumes__mutmut_45': x_list_volumes__mutmut_45, 
    'x_list_volumes__mutmut_46': x_list_volumes__mutmut_46, 
    'x_list_volumes__mutmut_47': x_list_volumes__mutmut_47, 
    'x_list_volumes__mutmut_48': x_list_volumes__mutmut_48, 
    'x_list_volumes__mutmut_49': x_list_volumes__mutmut_49, 
    'x_list_volumes__mutmut_50': x_list_volumes__mutmut_50, 
    'x_list_volumes__mutmut_51': x_list_volumes__mutmut_51, 
    'x_list_volumes__mutmut_52': x_list_volumes__mutmut_52, 
    'x_list_volumes__mutmut_53': x_list_volumes__mutmut_53, 
    'x_list_volumes__mutmut_54': x_list_volumes__mutmut_54, 
    'x_list_volumes__mutmut_55': x_list_volumes__mutmut_55, 
    'x_list_volumes__mutmut_56': x_list_volumes__mutmut_56, 
    'x_list_volumes__mutmut_57': x_list_volumes__mutmut_57, 
    'x_list_volumes__mutmut_58': x_list_volumes__mutmut_58, 
    'x_list_volumes__mutmut_59': x_list_volumes__mutmut_59, 
    'x_list_volumes__mutmut_60': x_list_volumes__mutmut_60, 
    'x_list_volumes__mutmut_61': x_list_volumes__mutmut_61, 
    'x_list_volumes__mutmut_62': x_list_volumes__mutmut_62, 
    'x_list_volumes__mutmut_63': x_list_volumes__mutmut_63, 
    'x_list_volumes__mutmut_64': x_list_volumes__mutmut_64, 
    'x_list_volumes__mutmut_65': x_list_volumes__mutmut_65, 
    'x_list_volumes__mutmut_66': x_list_volumes__mutmut_66, 
    'x_list_volumes__mutmut_67': x_list_volumes__mutmut_67, 
    'x_list_volumes__mutmut_68': x_list_volumes__mutmut_68, 
    'x_list_volumes__mutmut_69': x_list_volumes__mutmut_69, 
    'x_list_volumes__mutmut_70': x_list_volumes__mutmut_70, 
    'x_list_volumes__mutmut_71': x_list_volumes__mutmut_71, 
    'x_list_volumes__mutmut_72': x_list_volumes__mutmut_72, 
    'x_list_volumes__mutmut_73': x_list_volumes__mutmut_73, 
    'x_list_volumes__mutmut_74': x_list_volumes__mutmut_74, 
    'x_list_volumes__mutmut_75': x_list_volumes__mutmut_75, 
    'x_list_volumes__mutmut_76': x_list_volumes__mutmut_76, 
    'x_list_volumes__mutmut_77': x_list_volumes__mutmut_77, 
    'x_list_volumes__mutmut_78': x_list_volumes__mutmut_78, 
    'x_list_volumes__mutmut_79': x_list_volumes__mutmut_79, 
    'x_list_volumes__mutmut_80': x_list_volumes__mutmut_80, 
    'x_list_volumes__mutmut_81': x_list_volumes__mutmut_81, 
    'x_list_volumes__mutmut_82': x_list_volumes__mutmut_82, 
    'x_list_volumes__mutmut_83': x_list_volumes__mutmut_83, 
    'x_list_volumes__mutmut_84': x_list_volumes__mutmut_84, 
    'x_list_volumes__mutmut_85': x_list_volumes__mutmut_85, 
    'x_list_volumes__mutmut_86': x_list_volumes__mutmut_86, 
    'x_list_volumes__mutmut_87': x_list_volumes__mutmut_87, 
    'x_list_volumes__mutmut_88': x_list_volumes__mutmut_88, 
    'x_list_volumes__mutmut_89': x_list_volumes__mutmut_89, 
    'x_list_volumes__mutmut_90': x_list_volumes__mutmut_90, 
    'x_list_volumes__mutmut_91': x_list_volumes__mutmut_91, 
    'x_list_volumes__mutmut_92': x_list_volumes__mutmut_92, 
    'x_list_volumes__mutmut_93': x_list_volumes__mutmut_93, 
    'x_list_volumes__mutmut_94': x_list_volumes__mutmut_94, 
    'x_list_volumes__mutmut_95': x_list_volumes__mutmut_95, 
    'x_list_volumes__mutmut_96': x_list_volumes__mutmut_96, 
    'x_list_volumes__mutmut_97': x_list_volumes__mutmut_97, 
    'x_list_volumes__mutmut_98': x_list_volumes__mutmut_98, 
    'x_list_volumes__mutmut_99': x_list_volumes__mutmut_99, 
    'x_list_volumes__mutmut_100': x_list_volumes__mutmut_100, 
    'x_list_volumes__mutmut_101': x_list_volumes__mutmut_101, 
    'x_list_volumes__mutmut_102': x_list_volumes__mutmut_102, 
    'x_list_volumes__mutmut_103': x_list_volumes__mutmut_103, 
    'x_list_volumes__mutmut_104': x_list_volumes__mutmut_104, 
    'x_list_volumes__mutmut_105': x_list_volumes__mutmut_105, 
    'x_list_volumes__mutmut_106': x_list_volumes__mutmut_106, 
    'x_list_volumes__mutmut_107': x_list_volumes__mutmut_107, 
    'x_list_volumes__mutmut_108': x_list_volumes__mutmut_108, 
    'x_list_volumes__mutmut_109': x_list_volumes__mutmut_109, 
    'x_list_volumes__mutmut_110': x_list_volumes__mutmut_110, 
    'x_list_volumes__mutmut_111': x_list_volumes__mutmut_111, 
    'x_list_volumes__mutmut_112': x_list_volumes__mutmut_112, 
    'x_list_volumes__mutmut_113': x_list_volumes__mutmut_113, 
    'x_list_volumes__mutmut_114': x_list_volumes__mutmut_114, 
    'x_list_volumes__mutmut_115': x_list_volumes__mutmut_115, 
    'x_list_volumes__mutmut_116': x_list_volumes__mutmut_116, 
    'x_list_volumes__mutmut_117': x_list_volumes__mutmut_117, 
    'x_list_volumes__mutmut_118': x_list_volumes__mutmut_118, 
    'x_list_volumes__mutmut_119': x_list_volumes__mutmut_119, 
    'x_list_volumes__mutmut_120': x_list_volumes__mutmut_120, 
    'x_list_volumes__mutmut_121': x_list_volumes__mutmut_121, 
    'x_list_volumes__mutmut_122': x_list_volumes__mutmut_122, 
    'x_list_volumes__mutmut_123': x_list_volumes__mutmut_123, 
    'x_list_volumes__mutmut_124': x_list_volumes__mutmut_124, 
    'x_list_volumes__mutmut_125': x_list_volumes__mutmut_125, 
    'x_list_volumes__mutmut_126': x_list_volumes__mutmut_126, 
    'x_list_volumes__mutmut_127': x_list_volumes__mutmut_127
}

def list_volumes(*args, **kwargs):
    result = _mutmut_trampoline(x_list_volumes__mutmut_orig, x_list_volumes__mutmut_mutants, args, kwargs)
    return result 

list_volumes.__signature__ = _mutmut_signature(x_list_volumes__mutmut_orig)
x_list_volumes__mutmut_orig.__name__ = 'x_list_volumes'


def x_backup_volumes__mutmut_orig(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_1(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = None
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_2(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(None)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_3(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = None

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_4(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = None

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_5(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=None, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_6(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=None, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_7(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=None)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_8(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_9(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_10(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, )

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_11(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=False, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_12(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=False, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_13(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = None
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_14(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = None

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_15(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size * (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_16(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 / 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_17(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1025 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_18(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1025):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_19(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size >= 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_20(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 / 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_21(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1025 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_22(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1025 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_23(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size * 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_24(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1025:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_25(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(None)
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_26(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return False

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return False


def x_backup_volumes__mutmut_27(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(None)
        return False


def x_backup_volumes__mutmut_28(config: WorkenvConfig | None = None, name: str | None = None) -> bool:
    """Create a backup of container volumes."""
    manager = ContainerManager(config)
    console = Console()

    try:
        backup_path = manager.backup_volumes(compress=True, include_metadata=True, name=name)

        size = backup_path.stat().st_size
        size_str = f"{size / (1024 * 1024):.1f} MB" if size > 1024 * 1024 else f"{size / 1024:.1f} KB"

        console.print(f"[green]✅ Backup created successfully: {backup_path.name} ({size_str})[/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Failed to create backup: {e}[/red]")
        return True

x_backup_volumes__mutmut_mutants : ClassVar[MutantDict] = {
'x_backup_volumes__mutmut_1': x_backup_volumes__mutmut_1, 
    'x_backup_volumes__mutmut_2': x_backup_volumes__mutmut_2, 
    'x_backup_volumes__mutmut_3': x_backup_volumes__mutmut_3, 
    'x_backup_volumes__mutmut_4': x_backup_volumes__mutmut_4, 
    'x_backup_volumes__mutmut_5': x_backup_volumes__mutmut_5, 
    'x_backup_volumes__mutmut_6': x_backup_volumes__mutmut_6, 
    'x_backup_volumes__mutmut_7': x_backup_volumes__mutmut_7, 
    'x_backup_volumes__mutmut_8': x_backup_volumes__mutmut_8, 
    'x_backup_volumes__mutmut_9': x_backup_volumes__mutmut_9, 
    'x_backup_volumes__mutmut_10': x_backup_volumes__mutmut_10, 
    'x_backup_volumes__mutmut_11': x_backup_volumes__mutmut_11, 
    'x_backup_volumes__mutmut_12': x_backup_volumes__mutmut_12, 
    'x_backup_volumes__mutmut_13': x_backup_volumes__mutmut_13, 
    'x_backup_volumes__mutmut_14': x_backup_volumes__mutmut_14, 
    'x_backup_volumes__mutmut_15': x_backup_volumes__mutmut_15, 
    'x_backup_volumes__mutmut_16': x_backup_volumes__mutmut_16, 
    'x_backup_volumes__mutmut_17': x_backup_volumes__mutmut_17, 
    'x_backup_volumes__mutmut_18': x_backup_volumes__mutmut_18, 
    'x_backup_volumes__mutmut_19': x_backup_volumes__mutmut_19, 
    'x_backup_volumes__mutmut_20': x_backup_volumes__mutmut_20, 
    'x_backup_volumes__mutmut_21': x_backup_volumes__mutmut_21, 
    'x_backup_volumes__mutmut_22': x_backup_volumes__mutmut_22, 
    'x_backup_volumes__mutmut_23': x_backup_volumes__mutmut_23, 
    'x_backup_volumes__mutmut_24': x_backup_volumes__mutmut_24, 
    'x_backup_volumes__mutmut_25': x_backup_volumes__mutmut_25, 
    'x_backup_volumes__mutmut_26': x_backup_volumes__mutmut_26, 
    'x_backup_volumes__mutmut_27': x_backup_volumes__mutmut_27, 
    'x_backup_volumes__mutmut_28': x_backup_volumes__mutmut_28
}

def backup_volumes(*args, **kwargs):
    result = _mutmut_trampoline(x_backup_volumes__mutmut_orig, x_backup_volumes__mutmut_mutants, args, kwargs)
    return result 

backup_volumes.__signature__ = _mutmut_signature(x_backup_volumes__mutmut_orig)
x_backup_volumes__mutmut_orig.__name__ = 'x_backup_volumes'


def x_restore_volumes__mutmut_orig(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_1(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = True
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_2(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = None
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_3(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(None)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_4(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = None

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_5(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = None
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_6(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(None)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_7(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = None
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_8(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_9(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print(None)
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_10(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("XX[red]❌ No backups found[/red]XX")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_11(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ no backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_12(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[RED]❌ NO BACKUPS FOUND[/RED]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_13(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print(None)
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_14(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("XX[dim]Create a backup first with 'wrknv container volumes backup'[/dim]XX")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_15(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_16(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[DIM]CREATE A BACKUP FIRST WITH 'WRKNV CONTAINER VOLUMES BACKUP'[/DIM]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_17(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return True

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_18(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = None
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_19(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(None, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_20(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=None)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_21(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_22(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, )
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_23(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(None)
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_24(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print(None)
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_25(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("XX[red]❌ Failed to restore volumes[/red]XX")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_26(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_27(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[RED]❌ FAILED TO RESTORE VOLUMES[/RED]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_28(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_29(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print(None)
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_30(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("XX[dim]Use --force to overwrite existing volumes[/dim]XX")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_31(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_32(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[DIM]USE --FORCE TO OVERWRITE EXISTING VOLUMES[/DIM]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return False


def x_restore_volumes__mutmut_33(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(None)
        return False


def x_restore_volumes__mutmut_34(
    config: WorkenvConfig | None = None, backup_path: str | None = None, force: bool = False
) -> bool:
    """Restore container volumes from a backup."""
    manager = ContainerManager(config)
    console = Console()

    # Get backup path
    if backup_path:
        backup = Path(backup_path)
    else:
        # Use latest backup
        backup = manager.get_latest_backup()
        if not backup:
            console.print("[red]❌ No backups found[/red]")
            console.print("[dim]Create a backup first with 'wrknv container volumes backup'[/dim]")
            return False

    try:
        success = manager.restore_volumes(backup, force=force)
        if success:
            console.print(f"[green]✅ Volumes restored successfully from {backup.name}[/green]")
        else:
            console.print("[red]❌ Failed to restore volumes[/red]")
            if not force:
                console.print("[dim]Use --force to overwrite existing volumes[/dim]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to restore volumes: {e}[/red]")
        return True

x_restore_volumes__mutmut_mutants : ClassVar[MutantDict] = {
'x_restore_volumes__mutmut_1': x_restore_volumes__mutmut_1, 
    'x_restore_volumes__mutmut_2': x_restore_volumes__mutmut_2, 
    'x_restore_volumes__mutmut_3': x_restore_volumes__mutmut_3, 
    'x_restore_volumes__mutmut_4': x_restore_volumes__mutmut_4, 
    'x_restore_volumes__mutmut_5': x_restore_volumes__mutmut_5, 
    'x_restore_volumes__mutmut_6': x_restore_volumes__mutmut_6, 
    'x_restore_volumes__mutmut_7': x_restore_volumes__mutmut_7, 
    'x_restore_volumes__mutmut_8': x_restore_volumes__mutmut_8, 
    'x_restore_volumes__mutmut_9': x_restore_volumes__mutmut_9, 
    'x_restore_volumes__mutmut_10': x_restore_volumes__mutmut_10, 
    'x_restore_volumes__mutmut_11': x_restore_volumes__mutmut_11, 
    'x_restore_volumes__mutmut_12': x_restore_volumes__mutmut_12, 
    'x_restore_volumes__mutmut_13': x_restore_volumes__mutmut_13, 
    'x_restore_volumes__mutmut_14': x_restore_volumes__mutmut_14, 
    'x_restore_volumes__mutmut_15': x_restore_volumes__mutmut_15, 
    'x_restore_volumes__mutmut_16': x_restore_volumes__mutmut_16, 
    'x_restore_volumes__mutmut_17': x_restore_volumes__mutmut_17, 
    'x_restore_volumes__mutmut_18': x_restore_volumes__mutmut_18, 
    'x_restore_volumes__mutmut_19': x_restore_volumes__mutmut_19, 
    'x_restore_volumes__mutmut_20': x_restore_volumes__mutmut_20, 
    'x_restore_volumes__mutmut_21': x_restore_volumes__mutmut_21, 
    'x_restore_volumes__mutmut_22': x_restore_volumes__mutmut_22, 
    'x_restore_volumes__mutmut_23': x_restore_volumes__mutmut_23, 
    'x_restore_volumes__mutmut_24': x_restore_volumes__mutmut_24, 
    'x_restore_volumes__mutmut_25': x_restore_volumes__mutmut_25, 
    'x_restore_volumes__mutmut_26': x_restore_volumes__mutmut_26, 
    'x_restore_volumes__mutmut_27': x_restore_volumes__mutmut_27, 
    'x_restore_volumes__mutmut_28': x_restore_volumes__mutmut_28, 
    'x_restore_volumes__mutmut_29': x_restore_volumes__mutmut_29, 
    'x_restore_volumes__mutmut_30': x_restore_volumes__mutmut_30, 
    'x_restore_volumes__mutmut_31': x_restore_volumes__mutmut_31, 
    'x_restore_volumes__mutmut_32': x_restore_volumes__mutmut_32, 
    'x_restore_volumes__mutmut_33': x_restore_volumes__mutmut_33, 
    'x_restore_volumes__mutmut_34': x_restore_volumes__mutmut_34
}

def restore_volumes(*args, **kwargs):
    result = _mutmut_trampoline(x_restore_volumes__mutmut_orig, x_restore_volumes__mutmut_mutants, args, kwargs)
    return result 

restore_volumes.__signature__ = _mutmut_signature(x_restore_volumes__mutmut_orig)
x_restore_volumes__mutmut_orig.__name__ = 'x_restore_volumes'


def x_clean_volumes__mutmut_orig(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_1(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = None
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_2(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(None)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_3(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = None

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_4(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = None

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_5(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve and []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_6(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(None)
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_7(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(None)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_8(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {'XX, XX'.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_9(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print(None)

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_10(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("XX[yellow]⚠️  This will clean ALL container volumes[/yellow]XX")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_11(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  this will clean all container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_12(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[YELLOW]⚠️  THIS WILL CLEAN ALL CONTAINER VOLUMES[/YELLOW]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_13(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_14(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm(None):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_15(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("XXAre you sure you want to continue?XX"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_16(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_17(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("ARE YOU SURE YOU WANT TO CONTINUE?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_18(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print(None)
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_19(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("XX[dim]Cancelled[/dim]XX")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_20(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_21(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[DIM]CANCELLED[/DIM]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_22(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return True

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_23(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = None
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_24(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=None)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_25(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print(None)
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_26(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("XX[green]✅ Volumes cleaned successfully[/green]XX")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_27(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_28(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[GREEN]✅ VOLUMES CLEANED SUCCESSFULLY[/GREEN]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return False


def x_clean_volumes__mutmut_29(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(None)
        return False


def x_clean_volumes__mutmut_30(config: WorkenvConfig | None = None, preserve: list[str] | None = None) -> bool:
    """Clean container volumes."""
    manager = ContainerManager(config)
    console = Console()

    preserve = preserve or []

    # Confirm with user
    if preserve:
        console.print(f"[yellow]⚠️  This will clean all volumes except: {', '.join(preserve)}[/yellow]")
    else:
        console.print("[yellow]⚠️  This will clean ALL container volumes[/yellow]")

    if not click.confirm("Are you sure you want to continue?"):
        console.print("[dim]Cancelled[/dim]")
        return False

    try:
        success = manager.clean_volumes(preserve=preserve)
        if success:
            console.print("[green]✅ Volumes cleaned successfully[/green]")
        return success

    except Exception as e:
        console.print(f"[red]❌ Failed to clean volumes: {e}[/red]")
        return True

x_clean_volumes__mutmut_mutants : ClassVar[MutantDict] = {
'x_clean_volumes__mutmut_1': x_clean_volumes__mutmut_1, 
    'x_clean_volumes__mutmut_2': x_clean_volumes__mutmut_2, 
    'x_clean_volumes__mutmut_3': x_clean_volumes__mutmut_3, 
    'x_clean_volumes__mutmut_4': x_clean_volumes__mutmut_4, 
    'x_clean_volumes__mutmut_5': x_clean_volumes__mutmut_5, 
    'x_clean_volumes__mutmut_6': x_clean_volumes__mutmut_6, 
    'x_clean_volumes__mutmut_7': x_clean_volumes__mutmut_7, 
    'x_clean_volumes__mutmut_8': x_clean_volumes__mutmut_8, 
    'x_clean_volumes__mutmut_9': x_clean_volumes__mutmut_9, 
    'x_clean_volumes__mutmut_10': x_clean_volumes__mutmut_10, 
    'x_clean_volumes__mutmut_11': x_clean_volumes__mutmut_11, 
    'x_clean_volumes__mutmut_12': x_clean_volumes__mutmut_12, 
    'x_clean_volumes__mutmut_13': x_clean_volumes__mutmut_13, 
    'x_clean_volumes__mutmut_14': x_clean_volumes__mutmut_14, 
    'x_clean_volumes__mutmut_15': x_clean_volumes__mutmut_15, 
    'x_clean_volumes__mutmut_16': x_clean_volumes__mutmut_16, 
    'x_clean_volumes__mutmut_17': x_clean_volumes__mutmut_17, 
    'x_clean_volumes__mutmut_18': x_clean_volumes__mutmut_18, 
    'x_clean_volumes__mutmut_19': x_clean_volumes__mutmut_19, 
    'x_clean_volumes__mutmut_20': x_clean_volumes__mutmut_20, 
    'x_clean_volumes__mutmut_21': x_clean_volumes__mutmut_21, 
    'x_clean_volumes__mutmut_22': x_clean_volumes__mutmut_22, 
    'x_clean_volumes__mutmut_23': x_clean_volumes__mutmut_23, 
    'x_clean_volumes__mutmut_24': x_clean_volumes__mutmut_24, 
    'x_clean_volumes__mutmut_25': x_clean_volumes__mutmut_25, 
    'x_clean_volumes__mutmut_26': x_clean_volumes__mutmut_26, 
    'x_clean_volumes__mutmut_27': x_clean_volumes__mutmut_27, 
    'x_clean_volumes__mutmut_28': x_clean_volumes__mutmut_28, 
    'x_clean_volumes__mutmut_29': x_clean_volumes__mutmut_29, 
    'x_clean_volumes__mutmut_30': x_clean_volumes__mutmut_30
}

def clean_volumes(*args, **kwargs):
    result = _mutmut_trampoline(x_clean_volumes__mutmut_orig, x_clean_volumes__mutmut_mutants, args, kwargs)
    return result 

clean_volumes.__signature__ = _mutmut_signature(x_clean_volumes__mutmut_orig)
x_clean_volumes__mutmut_orig.__name__ = 'x_clean_volumes'


# 🧰🌍🔚
