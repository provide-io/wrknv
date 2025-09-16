#
# wrknv/container/manager.py
#
"""
Container Manager Implementation
================================
Core container management functionality for wrknv.
"""

from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import tarfile
from typing import Any

from provide.foundation import logger
from provide.foundation.process import run_command
from rich.console import Console

from wrknv.config import WorkenvConfig
from wrknv.wenv.schema import ContainerConfig, get_default_config


class ContainerManager:
    """Manages Docker containers for wrknv development environments."""

    # Default values (can be overridden by config)
    DEFAULT_CONTAINER_NAME = "wrknv-dev"
    DEFAULT_IMAGE_NAME = "wrknv-dev"
    DEFAULT_IMAGE_TAG = "latest"

    # Emoji constants for visual feedback
    CONTAINER_EMOJI = "🐳"
    BUILD_EMOJI = "🔨"
    START_EMOJI = "🚀"
    STOP_EMOJI = "⏹️"
    CLEAN_EMOJI = "🧹"
    STATUS_EMOJI = "📊"

    def __init__(self, config: WorkenvConfig | None = None):
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def _setup_storage(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def get_container_path(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(self.container_config.storage_path).expanduser()
        container_dir = storage_base / self.CONTAINER_NAME

        if subpath:
            return container_dir / subpath
        return container_dir

    def check_docker(self) -> bool:
        """Check if Docker is available and running."""
        try:
            result = run_command(["docker", "info"], check=False)
            if result.returncode != 0:
                logger.error("Docker daemon is not running")
                return False
            return True
        except FileNotFoundError:
            logger.error("Docker is not installed")
            return False

    def container_exists(self) -> bool:
        """Check if the container exists."""
        result = run_command(
            ["docker", "ps", "-a", "--format", "{{.Names}}"],
            check=False,
        )
        return self.CONTAINER_NAME in result.stdout.splitlines()

    def container_running(self) -> bool:
        """Check if the container is running."""
        result = run_command(
            ["docker", "ps", "--format", "{{.Names}}"],
            check=False,
        )
        return self.CONTAINER_NAME in result.stdout.splitlines()

    def image_exists(self) -> bool:
        """Check if the Docker image exists."""
        result = run_command(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"],
            check=False,
        )
        return self.full_image in result.stdout.splitlines()

    def build_image(self, rebuild: bool = False) -> bool:
        """Build the Docker image."""
        self.console.print(f"{self.BUILD_EMOJI} Building container image...")

        # Create Dockerfile content
        dockerfile_content = self._generate_dockerfile()

        # Use new build directory structure
        build_dir = self.get_container_path("build")
        build_dir.mkdir(parents=True, exist_ok=True)

        # Write Dockerfile
        dockerfile_path = build_dir / "Dockerfile"
        dockerfile_path.write_text(dockerfile_content)

        # Build image
        cmd = ["docker", "build", "-t", self.full_image, str(build_dir)]
        if rebuild:
            cmd.extend(["--no-cache"])

        try:
            run_command(cmd, check=True)
            self.console.print(f"[green]✅ Successfully built image {self.full_image}[/green]")
            # Save metadata after successful build
            self.save_metadata()
            return True
        except subprocess.CalledProcessError as e:
            self.console.print(f"[red]❌ Failed to build image: {e}[/red]")
            return False

    def start(self, force_rebuild: bool = False) -> bool:
        """Start the container."""
        if not self.check_docker():
            return False

        # Build image if needed
        if (force_rebuild or not self.image_exists()) and not self.build_image(rebuild=force_rebuild):
            return False

        # Check if container is already running
        if self.container_running():
            self.console.print(f"[yellow]⚠️  Container {self.CONTAINER_NAME} is already running[/yellow]")
            return True

        # Remove existing container if it exists but is not running
        if self.container_exists():
            self.console.print(f"{self.CLEAN_EMOJI} Removing existing container...")
            run_command(["docker", "rm", self.CONTAINER_NAME], check=False)

        # Start new container
        self.console.print(f"{self.START_EMOJI} Starting container {self.CONTAINER_NAME}...")

        # Get current user's home directory for volume mounting
        home_dir = str(Path.home())

        cmd = [
            "docker",
            "run",
            "-d",
            "--name",
            self.CONTAINER_NAME,
        ]

        # Add persistent volumes using new mapping system
        volume_mappings = self.get_volume_mappings()
        for volume_name, mapping in volume_mappings.items():
            cmd.extend(["-v", mapping])

        # Add default host volumes
        cmd.extend(["-v", f"{home_dir}:/host-home"])
        cmd.extend(["-v", "/var/run/docker.sock:/var/run/docker.sock"])

        # Add old-style configured volumes (for backward compatibility)
        for volume in self.container_config.volumes:
            if volume not in volume_mappings.values():
                cmd.extend(["-v", volume])

        # Add default environment variables
        cmd.extend(["-e", f"HOST_USER={os.environ.get('USER', 'user')}"])
        cmd.extend(["-e", f"HOST_UID={os.getuid()}"])
        cmd.extend(["-e", f"HOST_GID={os.getgid()}"])

        # Add configured environment variables
        for key, value in self.container_config.environment.items():
            cmd.extend(["-e", f"{key}={value}"])

        # Add configured port mappings
        for port_mapping in self.container_config.ports:
            cmd.extend(["-p", port_mapping])

        # Add workdir and image
        cmd.extend(
            [
                "--workdir",
                "/workspace",
                self.full_image,
                "tail",
                "-f",
                "/dev/null",
            ]
        )

        try:
            run_command(cmd, check=True)
            self.console.print(f"[green]✅ Container {self.CONTAINER_NAME} started successfully[/green]")
            return True
        except subprocess.CalledProcessError as e:
            self.console.print(f"[red]❌ Failed to start container: {e}[/red]")
            return False

    def enter(
        self,
        command: list[str] | None = None,
        shell: str | None = None,
        working_dir: str | None = None,
        environment: dict[str, str] | None = None,
        user: str | None = None,
        auto_start: bool = False,
    ) -> bool:
        """Enter the running container with enhanced options.

        Args:
            command: Command to execute (defaults to shell)
            shell: Shell to use (defaults to /bin/bash)
            working_dir: Working directory in container
            environment: Environment variables to set
            user: User to run as
            auto_start: Auto-start container if not running

        Returns:
            True if successful
        """
        if not self.container_running():
            if auto_start and self.container_exists():
                self.console.print(
                    f"[yellow]⚠️  Container {self.CONTAINER_NAME} is not running. Starting...[/yellow]"
                )
                if not self.start():
                    self.console.print("[red]❌ Failed to start container[/red]")
                    return False
            else:
                self.console.print(f"[red]❌ Container {self.CONTAINER_NAME} is not running[/red]")
                self.console.print("Run 'wrknv container start' first or use --auto-start")
                return False

        # Build docker exec command
        cmd = ["docker", "exec", "-it"]

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

        # Add container name
        cmd.append(self.CONTAINER_NAME)

        # Add command or shell
        if command:
            cmd.extend(command)
        else:
            # Use specified shell or default to /bin/bash
            cmd.append(shell or "/bin/bash")

        # Use os.system for interactive terminal
        result = os.system(" ".join(cmd))
        return result == 0

    def stop(self) -> bool:
        """Stop the container."""
        if not self.container_running():
            self.console.print(f"[yellow]⚠️  Container {self.CONTAINER_NAME} is not running[/yellow]")
            return True

        self.console.print(f"{self.STOP_EMOJI} Stopping container {self.CONTAINER_NAME}...")

        try:
            run_command(["docker", "stop", self.CONTAINER_NAME], check=True)
            self.console.print("[green]✅ Container stopped successfully[/green]")
            return True
        except subprocess.CalledProcessError as e:
            self.console.print(f"[red]❌ Failed to stop container: {e}[/red]")
            return False

    def restart(self) -> bool:
        """Restart the container."""
        self.stop()
        return self.start()

    def status(self) -> dict[str, any]:
        """Get container status information."""
        status = {
            "docker_available": self.check_docker(),
            "image_exists": False,
            "container_exists": False,
            "container_running": False,
            "container_info": {},
        }

        if not status["docker_available"]:
            return status

        status["image_exists"] = self.image_exists()
        status["container_exists"] = self.container_exists()
        status["container_running"] = self.container_running()

        if status["container_exists"]:
            # Get detailed container info
            result = run_command(
                ["docker", "inspect", self.CONTAINER_NAME],
                check=False,
            )
            if result.returncode == 0:
                info = json.loads(result.stdout)[0]
                status["container_info"] = {
                    "id": info["Id"][:12],
                    "created": info["Created"],
                    "state": info["State"]["Status"],
                    "ports": info["NetworkSettings"]["Ports"],
                }

        return status

    def save_metadata(self) -> None:
        """Save container metadata to JSON file."""
        metadata = {
            "created": datetime.now().isoformat(),
            "container_name": self.CONTAINER_NAME,
            "image": self.full_image,
            "config": {
                "python_version": self.container_config.python_version,
                "base_image": self.container_config.base_image,
                "additional_packages": self.container_config.additional_packages,
                "environment": self.container_config.environment,
                "volumes": self.container_config.volumes,
                "ports": self.container_config.ports,
                "persistent_volumes": self.container_config.persistent_volumes,
                "volume_mappings": self.container_config.volume_mappings,
            },
        }

        metadata_file = self.get_container_path("metadata.json")
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=2)

    def load_metadata(self) -> dict[str, Any] | None:
        """Load container metadata from JSON file.

        Returns:
            Metadata dictionary or None if file doesn't exist
        """
        metadata_file = self.get_container_path("metadata.json")
        if not metadata_file.exists():
            return None

        with open(metadata_file) as f:
            return json.load(f)

    def update_metadata(self, updates: dict[str, Any]) -> None:
        """Update existing metadata with new values.

        Args:
            updates: Dictionary of values to update in metadata
        """
        metadata = self.load_metadata() or {}
        metadata.update(updates)
        metadata["last_updated"] = datetime.now().isoformat()

        metadata_file = self.get_container_path("metadata.json")
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=2)

    def get_volume_mappings(self) -> dict[str, str]:
        """Get volume mappings for the container.

        Returns:
            Dictionary of volume name to Docker volume mount string
        """
        mappings = {}
        volumes_dir = self.get_container_path("volumes")

        # Add persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            volume_path = volumes_dir / volume_name
            volume_path.mkdir(parents=True, exist_ok=True)

            # Map workspace to /workspace, others to /home/user/.{name}
            if volume_name == "workspace":
                container_path = "/workspace"
            elif volume_name == "cache":
                container_path = "/home/user/.cache"
            elif volume_name == "config":
                container_path = "/home/user/.config"
            else:
                container_path = f"/volumes/{volume_name}"

            mappings[volume_name] = f"{volume_path}:{container_path}"

        # Add shared downloads (read-only)
        shared_downloads = Path(self.container_config.storage_path).expanduser() / "shared" / "downloads"
        shared_downloads.mkdir(parents=True, exist_ok=True)
        mappings["shared_downloads"] = f"{shared_downloads}:/downloads:ro"

        # Add custom volume mappings
        for name, mapping in self.container_config.volume_mappings.items():
            mappings[name] = mapping

        return mappings

    def list_volumes(self) -> list[dict[str, Any]]:
        """List all container volumes with information.

        Returns:
            List of volume information dictionaries
        """
        volumes = []
        volumes_dir = self.get_container_path("volumes")

        for volume_name in self.container_config.persistent_volumes:
            volume_path = volumes_dir / volume_name

            volume_info = {
                "name": volume_name,
                "path": str(volume_path),
                "exists": volume_path.exists(),
                "size": 0,
                "files": 0,
            }

            if volume_path.exists() and volume_path.is_dir():
                # Calculate size and file count
                total_size = 0
                file_count = 0
                for item in volume_path.rglob("*"):
                    if item.is_file():
                        file_count += 1
                        total_size += item.stat().st_size

                volume_info["size"] = total_size
                volume_info["files"] = file_count

            volumes.append(volume_info)

        return volumes

    def backup_volumes(
        self, compress: bool = True, include_metadata: bool = True, name: str | None = None
    ) -> Path:
        """Create a backup of container volumes.

        Args:
            compress: Whether to compress the backup
            include_metadata: Whether to include metadata in backup
            name: Custom name for the backup file

        Returns:
            Path to the created backup file
        """
        backups_dir = self.get_container_path("backups")
        backups_dir.mkdir(parents=True, exist_ok=True)

        # Generate backup filename
        if name:
            backup_name = name
            if not backup_name.endswith((".tar", ".tar.gz")):
                backup_name += ".tar.gz" if compress else ".tar"
        else:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            extension = ".tar.gz" if compress else ".tar"
            backup_name = f"backup-{timestamp}{extension}"

        backup_path = backups_dir / backup_name

        # Create backup
        mode = "w:gz" if compress else "w"
        with tarfile.open(backup_path, mode) as tar:
            # Add volumes
            volumes_dir = self.get_container_path("volumes")
            if volumes_dir.exists():
                tar.add(volumes_dir, arcname="volumes")

            # Add metadata if requested
            if include_metadata:
                metadata_file = self.get_container_path("metadata.json")
                if metadata_file.exists():
                    tar.add(metadata_file, arcname="metadata.json")

        logger.info(f"Created backup: {backup_path}")
        return backup_path

    def restore_volumes(self, backup_path: Path, force: bool = False) -> bool:
        """Restore container volumes from a backup.

        Args:
            backup_path: Path to the backup file
            force: Whether to overwrite existing volumes

        Returns:
            True if successful, False otherwise
        """
        if not backup_path.exists():
            logger.error(f"Backup file not found: {backup_path}")
            return False

        # Check if volumes exist and force is not set
        volumes_dir = self.get_container_path("volumes")
        if volumes_dir.exists() and any(volumes_dir.iterdir()) and not force:
            logger.warning("Volumes directory not empty. Use force=True to overwrite.")
            return False

        # Clear existing volumes if force is set
        if force and volumes_dir.exists():
            shutil.rmtree(volumes_dir)
            volumes_dir.mkdir(parents=True)

        # Extract backup
        try:
            with tarfile.open(backup_path, "r:*") as tar:
                # Extract to container directory
                container_dir = self.get_container_path()
                # Use data filter for safety (Python 3.12+)
                if hasattr(tarfile, "data_filter"):
                    tar.extractall(container_dir, filter="data")
                else:
                    tar.extractall(container_dir)

            logger.info(f"Restored volumes from: {backup_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore backup: {e}")
            return False

    def get_latest_backup(self) -> Path | None:
        """Get the path to the most recent backup file.

        Returns:
            Path to latest backup or None if no backups exist
        """
        backups_dir = self.get_container_path("backups")
        if not backups_dir.exists():
            return None

        backups = list(backups_dir.glob("backup-*.tar*"))
        if not backups:
            return None

        # Sort by modification time
        return max(backups, key=lambda p: p.stat().st_mtime)

    def clean_volumes(self, preserve: list[str] = None) -> bool:
        """Clean container volumes.

        Args:
            preserve: List of volume names to preserve

        Returns:
            True if successful
        """
        preserve = preserve or []
        volumes_dir = self.get_container_path("volumes")

        if not volumes_dir.exists():
            return True

        for volume_path in volumes_dir.iterdir():
            if volume_path.name not in preserve:
                if volume_path.is_dir():
                    shutil.rmtree(volume_path)
                else:
                    volume_path.unlink()
                logger.info(f"Cleaned volume: {volume_path.name}")
            else:
                logger.info(f"Preserved volume: {volume_path.name}")

        # Recreate default volume directories
        for volume_name in self.container_config.persistent_volumes:
            if volume_name not in preserve:
                (volumes_dir / volume_name).mkdir(exist_ok=True)

        return True

    def logs(
        self,
        follow: bool = False,
        tail: int | None = 100,
        since: str | None = None,
        timestamps: bool = False,
        details: bool = False,
    ) -> str | None:
        """Show container logs with enhanced options.

        Args:
            follow: Follow log output
            tail: Number of lines to show from the end
            since: Show logs since timestamp (e.g., "1h", "2023-01-01")
            timestamps: Show timestamps
            details: Show extra details

        Returns:
            Log output as string (if not following), None otherwise
        """
        if not self.container_exists():
            self.console.print(f"[red]❌ Container {self.CONTAINER_NAME} does not exist[/red]")
            return None

        cmd = ["docker", "logs"]

        # Add options
        if follow:
            cmd.append("-f")

        if timestamps:
            cmd.append("-t")

        if details:
            cmd.append("--details")

        if tail is not None:
            cmd.extend(["--tail", str(tail)])

        if since:
            cmd.extend(["--since", since])

        # Add container name
        cmd.append(self.CONTAINER_NAME)

        logger.info(f"Getting container logs: {' '.join(cmd)}")

        if follow:
            # Stream logs without capturing
            run_command(cmd, check=False)
            return None
        else:
            # Capture and return logs
            result = run_command(cmd)
            if result.returncode != 0:
                self.console.print(f"[red]Failed to get logs: {result.stderr}[/red]")
                return None
            return result.stdout

    def clean(self, preserve_volumes: bool = False) -> bool:
        """Remove container and optionally the image.

        Args:
            preserve_volumes: Whether to preserve container volumes

        Returns:
            True if successful
        """
        self.console.print(f"{self.CLEAN_EMOJI} Cleaning up container resources...")

        # Stop container if running
        if self.container_running():
            self.stop()

        # Remove container
        if self.container_exists():
            try:
                run_command(["docker", "rm", self.CONTAINER_NAME], check=True)
                self.console.print("[green]✅ Container removed[/green]")
            except subprocess.CalledProcessError:
                self.console.print("[red]❌ Failed to remove container[/red]")
                return False

        # Remove image
        if self.image_exists():
            try:
                run_command(["docker", "rmi", self.full_image], check=True)
                self.console.print("[green]✅ Image removed[/green]")
            except subprocess.CalledProcessError:
                self.console.print("[yellow]⚠️  Failed to remove image (may be in use)[/yellow]")

        # Clean volumes unless preserving
        if not preserve_volumes:
            self.clean_volumes()
            self.console.print("[green]✅ Volumes cleaned[/green]")
        else:
            self.console.print("[yellow]⚠️  Volumes preserved[/yellow]")

        return True

    def _generate_dockerfile(self) -> str:
        """Generate Dockerfile content for the development container."""
        # Get configuration values
        base_image = self.container_config.base_image
        python_version = self.container_config.python_version
        additional_packages = self.container_config.additional_packages
        environment_vars = self.container_config.environment

        # Build package list
        base_packages = [
            "curl",
            "git",
            "wget",
            "unzip",
            "build-essential",
        ]

        # Only add Python packages if not using a Python base image
        if not base_image.startswith("python:"):
            base_packages.extend(
                [
                    f"python{python_version}" if python_version != "3" else "python3",
                    f"python{python_version}-pip" if python_version != "3" else "python3-pip",
                    f"python{python_version}-venv" if python_version != "3" else "python3-venv",
                ]
            )

        # Add other packages
        base_packages.extend(
            [
                "sudo",
                "zsh",
            ]
        )

        all_packages = base_packages + additional_packages
        packages_str = " \\\n    ".join(all_packages)

        # Build environment variables section
        env_vars_section = ""
        if environment_vars:
            env_lines = [f"ENV {key}={value}" for key, value in environment_vars.items()]
            env_vars_section = "\n".join(env_lines) + "\n"

        return f"""FROM {base_image}

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive
{env_vars_section}
# Install base dependencies
RUN apt-get update && apt-get install -y \\
    {packages_str} \\
    && rm -rf /var/lib/apt/lists/*

# Install UV package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Create workspace directory
RUN mkdir -p /workspace

# Set zsh as default shell
RUN chsh -s /bin/zsh root

# Set up shell
SHELL ["/bin/zsh", "-c"]

# Install wrknv in development mode
WORKDIR /workspace

# Set up entrypoint
CMD ["/bin/bash"]
"""
