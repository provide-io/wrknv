#
# wrkenv/container/manager.py
#
"""
Container Manager Implementation
================================
Core container management functionality for wrkenv.
"""

import json
import os
import shutil
import subprocess
from pathlib import Path

from pyvider.telemetry import logger
from rich.console import Console

from wrkenv.env.config import WorkenvConfig


class ContainerManager:
    """Manages Docker containers for wrkenv development environments."""

    CONTAINER_NAME = "wrkenv-dev"
    IMAGE_NAME = "wrkenv-dev"
    IMAGE_TAG = "latest"

    # Emoji constants for visual feedback
    CONTAINER_EMOJI = "🐳"
    BUILD_EMOJI = "🔨"
    START_EMOJI = "🚀"
    STOP_EMOJI = "⏹️"
    CLEAN_EMOJI = "🧹"
    STATUS_EMOJI = "📊"

    def __init__(self, config: WorkenvConfig | None = None):
        self.config = config or WorkenvConfig()
        self.console = Console()
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

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

        # Create temporary build directory
        build_dir = Path.home() / ".wrkenv" / "container-build"
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
            return True
        except subprocess.CalledProcessError as e:
            self.console.print(f"[red]❌ Failed to build image: {e}[/red]")
            return False
        finally:
            # Clean up build directory
            shutil.rmtree(build_dir, ignore_errors=True)

    def start(self, force_rebuild: bool = False) -> bool:
        """Start the container."""
        if not self.check_docker():
            return False

        # Build image if needed
        if force_rebuild or not self.image_exists():
            if not self.build_image(rebuild=force_rebuild):
                return False

        # Check if container is already running
        if self.container_running():
            self.console.print(
                f"[yellow]⚠️  Container {self.CONTAINER_NAME} is already running[/yellow]"
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
            "-v",
            f"{home_dir}:/host-home",
            "-v",
            "/var/run/docker.sock:/var/run/docker.sock",
            "-e",
            f"HOST_USER={os.environ.get('USER', 'user')}",
            "-e",
            f"HOST_UID={os.getuid()}",
            "-e",
            f"HOST_GID={os.getgid()}",
            "--workdir",
            "/workspace",
            self.full_image,
            "tail",
            "-f",
            "/dev/null",
        ]

        try:
            subprocess.run(cmd, check=True)
            self.console.print(
                f"[green]✅ Container {self.CONTAINER_NAME} started successfully[/green]"
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
            self.console.print("Run 'wrkenv container start' first")
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
        return """FROM ubuntu:22.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install base dependencies
RUN apt-get update && apt-get install -y \\
    curl \\
    git \\
    wget \\
    unzip \\
    build-essential \\
    python3 \\
    python3-pip \\
    python3-venv \\
    docker.io \\
    sudo \\
    zsh \\
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

# Install wrkenv in development mode
WORKDIR /workspace

# Set up entrypoint
CMD ["/bin/bash"]
"""
