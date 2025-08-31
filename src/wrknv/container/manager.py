#
# wrknv/container/manager.py
#
"""
Container Manager Implementation
================================
Core container management functionality for wrknv.
"""

import json
import os
import shutil
import subprocess
import tarfile
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from pyvider.telemetry import logger
from rich.console import Console

from wrknv.wenv.config import WorkenvConfig
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
        
        # Migrate old structure if needed
        self._migrate_old_structure()
    
    def _migrate_old_structure(self) -> None:
        """Migrate from old container-build directory to new structure."""
        old_build = Path.home() / ".wrknv" / "container-build"
        if not old_build.exists():
            return
        
        new_build = self.get_container_path("build")
        
        # If new build directory is empty, move old content
        if not any(new_build.iterdir()):
            logger.info(f"Migrating old build directory to {new_build}")
            for item in old_build.iterdir():
                shutil.move(str(item), str(new_build / item.name))
        
        # Remove old directory
        shutil.rmtree(old_build, ignore_errors=True)
        logger.info("Removed old container-build directory")
    
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
            result = subprocess.run(
                ["docker", "info"], capture_output=True, text=True, check=False
            )
            if result.returncode != 0:
                logger.error("Docker daemon is not running")
                return False
            return True
        except FileNotFoundError:
            logger.error("Docker is not installed")
            return False

    def container_exists(self) -> bool:
        """Check if the container exists."""
        result = subprocess.run(
            ["docker", "ps", "-a", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=False,
        )
        return self.CONTAINER_NAME in result.stdout.splitlines()

    def container_running(self) -> bool:
        """Check if the container is running."""
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=False,
        )
        return self.CONTAINER_NAME in result.stdout.splitlines()

    def image_exists(self) -> bool:
        """Check if the Docker image exists."""
        result = subprocess.run(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"],
            capture_output=True,
            text=True,
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
            subprocess.run(cmd, check=True)
            self.console.print(
                f"[green]✅ Successfully built image {self.full_image}[/green]"
            )
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
        if (force_rebuild or not self.image_exists()) and not self.build_image(
            rebuild=force_rebuild
        ):
            return False

        # Check if container is already running
        if self.container_running():
            self.console.print(
                f"[yellow]⚠️  Container {self.CONTAINER_NAME} "
                "is already running[/yellow]"
            )
            return True

        # Remove existing container if it exists but is not running
        if self.container_exists():
            self.console.print(f"{self.CLEAN_EMOJI} Removing existing container...")
            subprocess.run(["docker", "rm", self.CONTAINER_NAME], check=False)

        # Start new container
        self.console.print(
            f"{self.START_EMOJI} Starting container {self.CONTAINER_NAME}..."
        )

        # Get current user's home directory for volume mounting
        home_dir = str(Path.home())

        cmd = [
            "docker",
            "run",
            "-d",
            "--name",
            self.CONTAINER_NAME,
        ]

        # Add default volumes
        cmd.extend(["-v", f"{home_dir}:/host-home"])
        cmd.extend(["-v", "/var/run/docker.sock:/var/run/docker.sock"])

        # Add configured volumes
        for volume in self.container_config.volumes:
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
            subprocess.run(cmd, check=True)
            self.console.print(
                f"[green]✅ Container {self.CONTAINER_NAME} "
                "started successfully[/green]"
            )
            return True
        except subprocess.CalledProcessError as e:
            self.console.print(f"[red]❌ Failed to start container: {e}[/red]")
            return False

    def enter(self, command: list[str] | None = None) -> None:
        """Enter the running container."""
        if not self.container_running():
            self.console.print(
                f"[red]❌ Container {self.CONTAINER_NAME} is not running[/red]"
            )
            self.console.print("Run 'wrknv container start' first")
            return

        # Default to interactive bash shell
        if not command:
            command = ["/bin/bash"]

        cmd = ["docker", "exec", "-it", self.CONTAINER_NAME] + command

        # Use os.system for interactive terminal
        os.system(" ".join(cmd))

    def stop(self) -> bool:
        """Stop the container."""
        if not self.container_running():
            self.console.print(
                f"[yellow]⚠️  Container {self.CONTAINER_NAME} is not running[/yellow]"
            )
            return True

        self.console.print(
            f"{self.STOP_EMOJI} Stopping container {self.CONTAINER_NAME}..."
        )

        try:
            subprocess.run(["docker", "stop", self.CONTAINER_NAME], check=True)
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
            result = subprocess.run(
                ["docker", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
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
            }
        }
        
        metadata_file = self.get_container_path("metadata.json")
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=2)
    
    def load_metadata(self) -> Optional[dict[str, Any]]:
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

    def logs(self, follow: bool = False, tail: int = 100) -> None:
        """Show container logs."""
        if not self.container_exists():
            self.console.print(
                f"[red]❌ Container {self.CONTAINER_NAME} does not exist[/red]"
            )
            return

        cmd = ["docker", "logs"]
        if follow:
            cmd.append("-f")
        cmd.extend(["--tail", str(tail), self.CONTAINER_NAME])

        subprocess.run(cmd)

    def clean(self) -> bool:
        """Remove container and optionally the image."""
        self.console.print(f"{self.CLEAN_EMOJI} Cleaning up container resources...")

        # Stop container if running
        if self.container_running():
            self.stop()

        # Remove container
        if self.container_exists():
            try:
                subprocess.run(["docker", "rm", self.CONTAINER_NAME], check=True)
                self.console.print("[green]✅ Container removed[/green]")
            except subprocess.CalledProcessError:
                self.console.print("[red]❌ Failed to remove container[/red]")
                return False

        # Remove image
        if self.image_exists():
            try:
                subprocess.run(["docker", "rmi", self.full_image], check=True)
                self.console.print("[green]✅ Image removed[/green]")
            except subprocess.CalledProcessError:
                self.console.print(
                    "[yellow]⚠️  Failed to remove image (may be in use)[/yellow]"
                )

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
            f"python{python_version}" if python_version != "3" else "python3",
            f"python{python_version}-pip" if python_version != "3" else "python3-pip",
            f"python{python_version}-venv" if python_version != "3" else "python3-venv",
            "docker.io",
            "sudo",
            "zsh",
        ]

        all_packages = base_packages + additional_packages
        packages_str = " \\\n    ".join(all_packages)

        # Build environment variables section
        env_vars_section = ""
        if environment_vars:
            env_lines = [
                f"ENV {key}={value}" for key, value in environment_vars.items()
            ]
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
