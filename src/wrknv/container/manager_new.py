#!/usr/bin/env python3
#
# wrknv/container/manager_new.py
#
"""
Refactored Container Manager
============================
Simplified container manager using modular operations.
"""

from pathlib import Path
from typing import Any

from attrs import define, field
from provide.foundation import logger
from rich.console import Console

from wrknv.container.errors import ContainerNotFoundError, ContainerRuntimeError
from wrknv.container.operations import (
    ContainerBuilder,
    ContainerExec,
    ContainerLifecycle,
    ContainerLogs,
    VolumeManager,
)
from wrknv.container.runtime.docker import DockerRuntime
from wrknv.container.storage import ContainerStorage
from wrknv.config import WorkenvConfig


@define
class ContainerManager:
    """High-level container management orchestrator."""
    
    config: WorkenvConfig
    container_name: str
    image_name: str
    image_tag: str
    
    # Injected dependencies
    console: Console = field(factory=Console)
    
    # Runtime and operations (initialized in __attrs_post_init__)
    runtime: DockerRuntime = field(init=False)
    lifecycle: ContainerLifecycle = field(init=False)
    exec: ContainerExec = field(init=False)
    builder: ContainerBuilder = field(init=False)
    logs: ContainerLogs = field(init=False)
    volumes: VolumeManager = field(init=False)
    storage: ContainerStorage = field(init=False)
    
    def __attrs_post_init__(self):
        """Initialize runtime and operation modules."""
        # Get container configuration
        container_config = self.config.container or {}
        
        # Initialize runtime
        runtime_command = container_config.get("runtime", "docker")
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command=runtime_command
        )
        
        # Initialize operations
        self.lifecycle = ContainerLifecycle(
            runtime=self.runtime,
            container_name=self.container_name,
            console=self.console,
            start_emoji=container_config.get("emojis", {}).get("start", "🚀"),
            stop_emoji=container_config.get("emojis", {}).get("stop", "⏹️"),
            restart_emoji=container_config.get("emojis", {}).get("restart", "🔄"),
            status_emoji=container_config.get("emojis", {}).get("status", "📊"),
        )
        
        self.exec = ContainerExec(
            runtime=self.runtime,
            container_name=self.container_name,
            console=self.console,
            available_shells=container_config.get("shells", ["/bin/bash", "/bin/sh"]),
            default_shell=container_config.get("default_shell", "/bin/sh"),
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
        
        backup_dir = Path(container_config.get("backup_dir", "~/.wrknv/backups")).expanduser()
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        self.volumes = VolumeManager(
            runtime=self.runtime,
            console=self.console,
            backup_dir=backup_dir,
        )
        
        storage_path = Path(container_config.get("storage_path", "~/.wrknv/storage")).expanduser()
        self.storage = ContainerStorage(
            container_name=self.container_name,
            storage_base=storage_path,
        )
    
    @property
    def full_image(self) -> str:
        """Get full image name with tag."""
        return f"{self.image_name}:{self.image_tag}"
    
    # Lifecycle operations
    def start(self, **options) -> bool:
        """Start the container."""
        # Add image to options if creating new container
        options["image"] = self.full_image
        
        # Get volumes from config
        container_config = self.config.container or {}
        options["volumes"] = container_config.get("volumes", [])
        options["environment"] = container_config.get("environment", {})
        options["ports"] = container_config.get("ports", [])
        
        return self.lifecycle.start(
            create_if_missing=True,
            **options
        )
    
    def stop(self, timeout: int | None = None) -> bool:
        """Stop the container."""
        container_config = self.config.container or {}
        if timeout is None:
            timeout = container_config.get("stop_timeout", 10)
        return self.lifecycle.stop(timeout=timeout)
    
    def restart(self, timeout: int | None = None) -> bool:
        """Restart the container."""
        container_config = self.config.container or {}
        if timeout is None:
            timeout = container_config.get("stop_timeout", 10)
        return self.lifecycle.restart(timeout=timeout)
    
    def status(self) -> dict[str, Any]:
        """Get container status."""
        return self.lifecycle.status()
    
    def remove(self, force: bool | None = None) -> bool:
        """Remove the container."""
        if force is None:
            force = False
        return self.lifecycle.remove(force=force)
    
    # Exec operations
    def enter(self, shell: str | None = None, **kwargs) -> bool:
        """Enter the container interactively."""
        return self.exec.enter(shell=shell, **kwargs)
    
    def exec_command(self, command: list[str], **kwargs) -> str | None:
        """Execute a command in the container."""
        return self.exec.run_command(
            command=command,
            capture_output=True,
            **kwargs
        )
    
    # Build operations
    def build(self, dockerfile: str | None = None, **options) -> bool:
        """Build the container image."""
        container_config = self.config.container or {}
        
        if dockerfile is None:
            dockerfile = container_config.get("dockerfile", "Dockerfile")
        
        context = container_config.get("build_context", ".")
        build_args = container_config.get("build_args", {})
        
        return self.builder.build(
            dockerfile=dockerfile,
            tag=self.full_image,
            context=context,
            build_args=build_args,
            stream_output=True,
            **options
        )
    
    # Log operations
    def show_logs(self, lines: int | None = None, **kwargs) -> None:
        """Show container logs."""
        if lines is None:
            container_config = self.config.container or {}
            lines = container_config.get("default_log_lines", 50)
        
        self.logs.show_logs(
            lines=lines,
            since_minutes=kwargs.get("since_minutes"),
            grep=kwargs.get("grep"),
        )
    
    def follow_logs(self, **kwargs) -> None:
        """Follow container logs."""
        self.logs.get_logs(
            follow=True,
            tail=kwargs.get("tail", 10),
            since=kwargs.get("since"),
            timestamps=kwargs.get("timestamps", False),
        )
    
    # Volume operations
    def list_volumes(self) -> None:
        """List all volumes."""
        self.volumes.show_volumes()
    
    def backup_volume(self, volume_name: str, mount_path: str) -> Path | None:
        """Backup a volume."""
        return self.volumes.backup_volume(
            volume_name=volume_name,
            container_name=self.container_name,
            mount_path=mount_path,
        )
    
    def restore_volume(self, volume_name: str, backup_file: Path, mount_path: str) -> bool:
        """Restore a volume."""
        return self.volumes.restore_volume(
            volume_name=volume_name,
            backup_file=backup_file,
            mount_path=mount_path,
        )
    
    # Storage operations
    def get_storage_path(self, subpath: str) -> Path:
        """Get a storage path for the container."""
        return self.storage.get_path(subpath)
    
    def clean_storage(self) -> bool:
        """Clean container storage."""
        return self.storage.clean()


from wrknv.container.storage import ContainerStorage

@define
class ContainerStorage:
    """Container storage management."""
    
    container_name: str
    storage_base: Path
    
    def get_path(self, subpath: str) -> Path:
        """Get storage path."""
        path = self.storage_base / self.container_name / subpath
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    def clean(self) -> bool:
        """Clean storage."""
        import shutil
        try:
            container_dir = self.storage_base / self.container_name
            if container_dir.exists():
                shutil.rmtree(container_dir)
            return True
        except Exception as e:
            logger.error("Failed to clean storage", error=str(e))
            return False