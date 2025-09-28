#!/usr/bin/env python3

"""
Container Manager Implementation
================================
Core container management functionality for wrknv.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from attrs import define, field
from provide.foundation import logger
from provide.foundation.process import run_command
from rich.console import Console

from wrknv.config import WorkenvConfig
from wrknv.container.operations import (
    ContainerBuilder,
    ContainerExec,
    ContainerLifecycle,
    ContainerLogs,
    VolumeManager,
)
from wrknv.container.runtime.docker import DockerRuntime
from wrknv.container.storage import ContainerStorage
from wrknv.wenv.schema import ContainerConfig, get_default_config


@define
class ContainerManager:
    """Manages Docker containers for wrknv development environments."""

    config: WorkenvConfig = field()
    console: Console = field(factory=Console)

    # Container identification
    container_name: str = field(init=False)
    image_name: str = field(init=False)
    image_tag: str = field(init=False, default="latest")
    full_image: str = field(init=False)

    # Container configuration
    container_config: ContainerConfig = field(init=False)

    # Operations and storage (initialized in __attrs_post_init__)
    storage: ContainerStorage = field(init=False)
    runtime: DockerRuntime = field(init=False)
    lifecycle: ContainerLifecycle = field(init=False)
    exec: ContainerExec = field(init=False)
    builder: ContainerBuilder = field(init=False)
    logs: ContainerLogs = field(init=False)
    volumes: VolumeManager = field(init=False)

    def __attrs_post_init__(self):
        """Initialize container configuration and operations."""
        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.container_name = f"{project_name}-dev"
        else:
            self.container_name = "wrknv-dev"

        self.image_name = self.container_name
        self.full_image = f"{self.image_name}:{self.image_tag}"

        # Initialize storage
        self.storage = ContainerStorage(
            container_name=self.container_name,
            container_config=self.container_config,
        )
        self.storage.setup_storage()

        # Initialize runtime
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker",
        )

        # Initialize operations with dependencies (simplified for compatibility)
        self.lifecycle = ContainerLifecycle(
            runtime=self.runtime,
            container_name=self.container_name,
            console=self.console,
            start_emoji="🚀",
            stop_emoji="⏹️",
            restart_emoji="🔄",
            status_emoji="📊",
        )

        self.exec = ContainerExec(
            runtime=self.runtime,
            container_name=self.container_name,
            console=self.console,
            available_shells=["/bin/bash", "/bin/sh"],
            default_shell="/bin/bash",
        )

        self.builder = ContainerBuilder(
            runtime=self.runtime,
            console=self.console,
        )

        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name=self.container_name,
            console=self.console,
        )

        self.volumes = VolumeManager(
            runtime=self.runtime,
            container_name=self.container_name,
            console=self.console,
        )

    # Convenience methods that delegate to operations

    def check_docker(self) -> bool:
        """Check if Docker is available and running."""
        return self.runtime.is_available()

    def container_exists(self) -> bool:
        """Check if the container exists."""
        return self.lifecycle.exists()

    def container_running(self) -> bool:
        """Check if the container is currently running."""
        return self.lifecycle.is_running()

    def image_exists(self) -> bool:
        """Check if the container image exists."""
        return self.builder.image_exists()

    def build_image(self, rebuild: bool = False) -> bool:
        """Build the container image."""
        return self.builder.build(rebuild=rebuild)

    def start(self, force_rebuild: bool = False) -> bool:
        """Start the container, building if necessary."""
        return self.lifecycle.start(force_rebuild=force_rebuild)

    def enter(
        self,
        command: str | None = None,
        user: str | None = None,
        workdir: str | None = None,
        environment: dict[str, str] | None = None,
    ) -> bool:
        """Enter the container with an interactive shell or command."""
        return self.exec.enter(
            command=command,
            user=user,
            workdir=workdir,
            environment=environment,
        )

    def stop(self) -> bool:
        """Stop the container."""
        return self.lifecycle.stop()

    def restart(self) -> bool:
        """Restart the container."""
        return self.lifecycle.restart()

    def status(self) -> dict[str, Any]:
        """Get container status information."""
        return self.lifecycle.get_status()

    def backup_volumes(
        self,
        backup_path: Path | None = None,
        volumes: list[str] | None = None,
        compress: bool = True,
    ) -> bool:
        """Backup container volumes."""
        return self.volumes.backup(
            backup_path=backup_path,
            volumes=volumes,
            compress=compress,
        )

    def restore_volumes(self, backup_path: Path, force: bool = False) -> bool:
        """Restore container volumes from backup."""
        return self.volumes.restore(backup_path=backup_path, force=force)

    def clean_volumes(self, preserve: list[str] | None = None) -> bool:
        """Clean up container volumes."""
        return self.volumes.clean(preserve=preserve)

    def get_logs(
        self,
        lines: int | None = None,
        follow: bool = False,
        since: str | None = None,
    ) -> str | None:
        """Get container logs."""
        return self.logs.get_logs(lines=lines, follow=follow, since=since)

    def clean(self, preserve_volumes: bool = False) -> bool:
        """Clean up container and optionally volumes."""
        success = True

        # Stop and remove container
        if self.container_exists():
            if self.container_running():
                success = self.stop() and success

            success = self.lifecycle.remove() and success

        # Clean up volumes if requested
        if not preserve_volumes:
            success = self.clean_volumes() and success

        # Clean up storage
        success = self.storage.clean_storage(preserve_backups=True) and success

        if success:
            logger.info("🧹 Container cleanup completed", container=self.container_name)
        else:
            logger.warning("⚠️ Container cleanup had some issues", container=self.container_name)

        return success

    def get_container_path(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file."""
        return self.storage.get_container_path(subpath)

    def get_volume_mappings(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        return self.storage.get_volume_mappings()

    def save_metadata(self) -> None:
        """Save container metadata."""
        metadata = {
            "container_name": self.container_name,
            "image_name": self.full_image,
            "project_name": self.config.project_name,
            "config_version": self.config.version,
        }
        self.storage.save_metadata(metadata)

    def load_metadata(self) -> dict[str, Any] | None:
        """Load container metadata."""
        return self.storage.load_metadata()

    def update_metadata(self, updates: dict[str, Any]) -> None:
        """Update container metadata."""
        self.storage.update_metadata(updates)


def create_container_manager(project_name: str | None = None) -> ContainerManager:
    """Create a ContainerManager with default configuration."""
    config = get_default_config(project_name or "my-project")
    return ContainerManager(config=config)