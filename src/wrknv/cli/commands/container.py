#!/usr/bin/env python3
#
# wrknv/cli/commands/container.py
#
"""
Container Commands
==================
Commands for managing development containers.
"""

import sys
from typing import Optional

from provide.foundation.hub import register_command
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation import logger

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
    list_volumes,
    backup_volumes,
    restore_volumes,
    clean_volumes,
)
from wrknv.wenv.config import WorkenvConfig


# Register the container group first
@register_command("container", group=True, description="Docker container management")
def container_group():
    """Docker container management commands."""
    pass


@register_command(
    "container.status",
    description="Show container status",
)
def container_status_command():
    """Display container status information."""
    config = WorkenvConfig()
    container_status(config)


@register_command(
    "container.build",
    description="Build container image",
)
def container_build_command(rebuild: bool = False):
    """Build the development container image."""
    config = WorkenvConfig()
    
    if rebuild:
        echo_info("🔨 Rebuilding container image from scratch...")
    else:
        echo_info("🔨 Building container image...")
    
    success = build_container(config, rebuild=rebuild)
    
    if success:
        echo_success("✅ Container image built successfully")
    else:
        echo_error("❌ Failed to build container image")
        sys.exit(1)


@register_command(
    "container.start",
    description="Start development container",
)
def container_start_command(rebuild: bool = False):
    """Start the development container."""
    config = WorkenvConfig()
    
    echo_info("🚀 Starting container...")
    
    success = start_container(config, rebuild=rebuild)
    
    if success:
        echo_success("✅ Container started successfully")
        echo_info("Run 'wrknv container enter' to access the container")
    else:
        echo_error("❌ Failed to start container")
        sys.exit(1)


@register_command(
    "container.stop",
    description="Stop development container",
)
def container_stop_command():
    """Stop the development container."""
    config = WorkenvConfig()
    
    echo_info("🛑 Stopping container...")
    
    success = stop_container(config)
    
    if success:
        echo_success("✅ Container stopped successfully")
    else:
        echo_error("❌ Failed to stop container")
        sys.exit(1)


@register_command(
    "container.restart",
    description="Restart development container",
)
def container_restart_command():
    """Restart the development container."""
    config = WorkenvConfig()
    
    echo_info("🔄 Restarting container...")
    
    success = restart_container(config)
    
    if success:
        echo_success("✅ Container restarted successfully")
    else:
        echo_error("❌ Failed to restart container")
        sys.exit(1)


@register_command(
    "container.enter",
    description="Enter running container",
)
def container_enter_command(
    command: Optional[str] = None,
    shell: Optional[str] = None,
    working_dir: Optional[str] = None,
    user: Optional[str] = None,
    auto_start: bool = False,
):
    """Enter the running container."""
    config = WorkenvConfig()
    
    # Parse command if provided
    command_list = command.split() if command else None
    
    enter_container(
        config=config,
        command=command_list,
        shell=shell,
        working_dir=working_dir,
        user=user,
        auto_start=auto_start,
    )


@register_command(
    "container.logs",
    description="Show container logs",
)
def container_logs_command(
    follow: bool = False,
    tail: int = 100,
    since: Optional[str] = None,
    timestamps: bool = False,
    details: bool = False,
):
    """Show container logs."""
    config = WorkenvConfig()
    
    container_logs(
        config=config,
        follow=follow,
        tail=tail,
        since=since,
        timestamps=timestamps,
        details=details,
    )


@register_command(
    "container.clean",
    description="Clean up container and image",
)
def container_clean_command():
    """Clean up container and image."""
    config = WorkenvConfig()
    
    echo_warning("⚠️  This will remove the container and image")
    
    # Confirm with user
    response = input("Continue? [y/N]: ").strip().lower()
    if response != 'y':
        echo_info("Cancelled")
        return
    
    echo_info("🧹 Cleaning container resources...")
    
    success = clean_container(config)
    
    if success:
        echo_success("✅ Container resources cleaned successfully")
    else:
        echo_error("❌ Failed to clean container resources")
        sys.exit(1)


@register_command(
    "container.rebuild",
    description="Rebuild container from scratch",
)
def container_rebuild_command():
    """Rebuild the container from scratch."""
    config = WorkenvConfig()
    
    echo_info("🔨 Rebuilding container from scratch...")
    
    success = rebuild_container(config)
    
    if success:
        echo_success("✅ Container rebuilt successfully")
        echo_info("Run 'wrknv container enter' to access the new container")
    else:
        echo_error("❌ Failed to rebuild container")
        sys.exit(1)


# Volume management commands

# Create a volumes subgroup under container
@register_command(
    "container.volumes",
    group=True,
    description="Container volume management",
)
def container_volumes_group():
    """Container volume management commands."""
    pass


@register_command(
    "container.volumes.list",
    description="List container volumes",
)
def container_volumes_list_command():
    """List container volumes with information."""
    config = WorkenvConfig()
    list_volumes(config)


@register_command(
    "container.volumes.backup",
    description="Backup container volumes",
)
def container_volumes_backup_command(name: Optional[str] = None):
    """Create a backup of container volumes."""
    config = WorkenvConfig()
    
    success = backup_volumes(config, name=name)
    
    if not success:
        sys.exit(1)


@register_command(
    "container.volumes.restore",
    description="Restore container volumes from backup",
)
def container_volumes_restore_command(
    backup_path: Optional[str] = None,
    force: bool = False,
):
    """Restore container volumes from a backup."""
    config = WorkenvConfig()
    
    success = restore_volumes(config, backup_path=backup_path, force=force)
    
    if not success:
        sys.exit(1)


@register_command(
    "container.volumes.clean",
    description="Clean container volumes",
)
def container_volumes_clean_command(preserve: Optional[str] = None):
    """Clean container volumes."""
    config = WorkenvConfig()
    
    # Parse preserve list
    preserve_list = preserve.split(',') if preserve else []
    
    success = clean_volumes(config, preserve=preserve_list)
    
    if not success:
        sys.exit(1)


# Convenience shortcuts

@register_command(
    "container.shell",
    description="Open shell in container (alias for enter)",
    hidden=True,
)
def container_shell_command():
    """Open an interactive shell in the container."""
    config = WorkenvConfig()
    
    enter_container(
        config=config,
        command=None,
        shell="/bin/bash",
        auto_start=True,
    )


@register_command(
    "container.exec",
    description="Execute command in container",
)
def container_exec_command(command: str):
    """Execute a command in the container."""
    config = WorkenvConfig()
    
    if not command:
        echo_error("No command specified")
        echo_info("Usage: wrknv container exec 'command to run'")
        sys.exit(1)
    
    enter_container(
        config=config,
        command=command.split(),
        auto_start=True,
    )