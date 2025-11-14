#!/usr/bin/env python3
#
# wrknv/cli/commands/container.py
#
"""
Container Commands
==================
Commands for managing development containers.
"""

import json
import sys

import click
from rich.console import Console
from rich.table import Table

from wrknv.container import (
    build_container,
    clean_container,
    container_logs,
    container_status,
    enter_container,
    rebuild_container,
    restart_container,
    start_container,
    stop_container,
)
from wrknv.container.commands import (
    backup_volumes,
    clean_volumes,
    list_volumes,
    restore_volumes,
)
from wrknv.container.shell_commands import exec_in_container, get_container_stats
from wrknv.wenv.config import WorkenvConfig


@click.group(name="container")
def container_group():
    """🐳 Manage development containers."""
    pass


@container_group.command(name="build")
@click.option("--rebuild", is_flag=True, help="Force rebuild without cache")
def container_build(rebuild: bool):
    """Build the development container image."""
    config = WorkenvConfig()

    if build_container(config, rebuild=rebuild):
        click.echo("✅ Container image built successfully")
    else:
        click.echo("❌ Failed to build container image", err=True)
        sys.exit(1)


@container_group.command(name="start")
@click.option("--rebuild", is_flag=True, help="Rebuild image before starting")
def container_start(rebuild: bool):
    """Start the development container."""
    config = WorkenvConfig()

    if start_container(config, rebuild=rebuild):
        click.echo("✅ Container started successfully")
        click.echo("Run 'wrknv container enter' to access the container")
    else:
        click.echo("❌ Failed to start container", err=True)
        sys.exit(1)


@container_group.command(name="enter")
@click.argument("command", nargs=-1, required=False)
@click.option("-s", "--shell", default="/bin/bash", help="Shell to use")
@click.option("-w", "--working-dir", help="Working directory in container")
@click.option("-e", "--env", multiple=True, help="Environment variables (KEY=VALUE)")
@click.option("-u", "--user", help="User to run as")
@click.option("--auto-start", is_flag=True, help="Auto-start container if not running")
def container_enter(
    command: tuple,
    shell: str,
    working_dir: str | None,
    env: tuple,
    user: str | None,
    auto_start: bool,
):
    """Enter the running container with an interactive shell."""
    config = WorkenvConfig()

    # Convert tuple to list
    cmd_list = list(command) if command else None
    
    # Parse environment variables
    environment = {}
    for env_var in env:
        if "=" in env_var:
            key, value = env_var.split("=", 1)
            environment[key] = value
    
    enter_container(
        config,
        command=cmd_list,
        shell=shell,
        working_dir=working_dir,
        environment=environment if environment else None,
        user=user,
        auto_start=auto_start,
    )


@container_group.command(name="stop")
def container_stop():
    """Stop the development container."""
    config = WorkenvConfig()

    if stop_container(config):
        click.echo("✅ Container stopped successfully")
    else:
        click.echo("❌ Failed to stop container", err=True)
        sys.exit(1)


@container_group.command(name="restart")
def container_restart():
    """Restart the development container."""
    config = WorkenvConfig()

    if restart_container(config):
        click.echo("✅ Container restarted successfully")
    else:
        click.echo("❌ Failed to restart container", err=True)
        sys.exit(1)


@container_group.command(name="status")
def container_status_cmd():
    """Show container status."""
    config = WorkenvConfig()
    container_status(config)


@container_group.command(name="logs")
@click.option("-f", "--follow", is_flag=True, help="Follow log output")
@click.option("-n", "--tail", default=100, help="Number of lines to show")
@click.option("--since", help="Show logs since timestamp (e.g., '1h', '2023-01-01')")
@click.option("-t", "--timestamps", is_flag=True, help="Show timestamps")
@click.option("--details", is_flag=True, help="Show extra details")
def container_logs_cmd(
    follow: bool,
    tail: int,
    since: str | None,
    timestamps: bool,
    details: bool,
):
    """Show container logs."""
    config = WorkenvConfig()
    container_logs(
        config,
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
        details=details,
    )


@container_group.command(name="exec")
@click.argument("command", nargs=-1, required=True)
@click.option("-w", "--working-dir", help="Working directory in container")
@click.option("-e", "--env", multiple=True, help="Environment variables (KEY=VALUE)")
@click.option("-u", "--user", help="User to run as")
@click.option("-i", "--interactive", is_flag=True, help="Keep STDIN open")
def container_exec(
    command: tuple,
    working_dir: str | None,
    env: tuple,
    user: str | None,
    interactive: bool,
):
    """Execute a command in the container."""
    config = WorkenvConfig()
    
    # Parse environment variables
    environment = {}
    for env_var in env:
        if "=" in env_var:
            key, value = env_var.split("=", 1)
            environment[key] = value
    
    result = exec_in_container(
        config,
        command=list(command),
        working_dir=working_dir,
        environment=environment if environment else None,
        user=user,
        interactive=interactive,
    )
    
    if result:
        if not interactive and result.stdout:
            click.echo(result.stdout)
        if result.returncode != 0:
            sys.exit(result.returncode)
    else:
        click.echo("❌ Failed to execute command", err=True)
        sys.exit(1)


@container_group.command(name="stats")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def container_stats(as_json: bool):
    """Show container resource usage statistics."""
    config = WorkenvConfig()
    stats = get_container_stats(config)
    
    if not stats:
        click.echo("❌ Container is not running or stats unavailable", err=True)
        sys.exit(1)
    
    if as_json:
        click.echo(json.dumps(stats, indent=2))
    else:
        console = Console()
        table = Table(title="Container Resource Usage")
        
        table.add_column("Resource", style="cyan")
        table.add_column("Usage", style="green")
        
        table.add_row("Container", stats["name"])
        table.add_row("CPU", stats["cpu"])
        table.add_row("Memory", f"{stats['memory']['usage']} ({stats['memory']['percent']})")
        table.add_row("Network I/O", stats["network"])
        table.add_row("Disk I/O", stats["disk"])
        table.add_row("PIDs", stats["pids"])
        
        console.print(table)


@container_group.command(name="clean")
def container_clean():
    """Remove container and image."""
    config = WorkenvConfig()

    if clean_container(config):
        click.echo("✅ Container resources cleaned successfully")
    else:
        click.echo("❌ Failed to clean container resources", err=True)
        sys.exit(1)


@container_group.command(name="rebuild")
def container_rebuild():
    """Rebuild container from scratch."""
    config = WorkenvConfig()

    if rebuild_container(config):
        click.echo("✅ Container rebuilt successfully")
    else:
        click.echo("❌ Failed to rebuild container", err=True)
        sys.exit(1)


# === Container Volume Commands ===


@container_group.group(name="volumes")
def volumes_group():
    """📦 Manage container volumes."""
    pass


@volumes_group.command(name="list")
def volumes_list():
    """List container volumes."""
    config = WorkenvConfig()
    list_volumes(config)


@volumes_group.command(name="backup")
@click.option("--name", help="Custom name for the backup")
def volumes_backup(name: str | None):
    """Create a backup of container volumes."""
    config = WorkenvConfig()
    if backup_volumes(config, name=name):
        sys.exit(0)
    else:
        sys.exit(1)


@volumes_group.command(name="restore")
@click.option("--backup", help="Path to specific backup file")
@click.option("--force", is_flag=True, help="Overwrite existing volumes")
def volumes_restore(backup: str | None, force: bool):
    """Restore container volumes from backup."""
    config = WorkenvConfig()
    if restore_volumes(config, backup_path=backup, force=force):
        sys.exit(0)
    else:
        sys.exit(1)


@volumes_group.command(name="clean")
@click.option("--preserve", multiple=True, help="Volume names to preserve")
def volumes_clean(preserve: tuple[str]):
    """Clean container volumes."""
    config = WorkenvConfig()
    preserve_list = list(preserve) if preserve else []
    if clean_volumes(config, preserve=preserve_list):
        sys.exit(0)
    else:
        sys.exit(1)