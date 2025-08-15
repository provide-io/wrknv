#
# wrkenv/container/commands.py
#
"""
Container Command Implementations
=================================
Command implementations for container management.
"""

from rich.console import Console
from rich.table import Table

from wrkenv.wenv.config import WorkenvConfig

from .manager import ContainerManager


def build_container(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Build the development container image."""
    manager = ContainerManager(config)
    return manager.build_image(rebuild=rebuild)


def start_container(config: WorkenvConfig | None = None, rebuild: bool = False) -> bool:
    """Start the development container."""
    manager = ContainerManager(config)
    return manager.start(force_rebuild=rebuild)


def enter_container(
    config: WorkenvConfig | None = None, command: list[str] | None = None
) -> None:
    """Enter the running container."""
    manager = ContainerManager(config)
    manager.enter(command=command)


def stop_container(config: WorkenvConfig | None = None) -> bool:
    """Stop the development container."""
    manager = ContainerManager(config)
    return manager.stop()


def restart_container(config: WorkenvConfig | None = None) -> bool:
    """Restart the development container."""
    manager = ContainerManager(config)
    return manager.restart()


def container_status(config: WorkenvConfig | None = None) -> None:
    """Display container status information."""
    manager = ContainerManager(config)
    console = Console()

    status = manager.status()

    # Create status table
    table = Table(title=f"{manager.STATUS_EMOJI} Container Status", show_header=True)
    table.add_column("Property", style="cyan")
    table.add_column("Status", style="green")

    # Docker status
    docker_status = "✅ Available" if status["docker_available"] else "❌ Not Available"
    table.add_row("Docker", docker_status)

    # Image status
    image_status = "✅ Exists" if status["image_exists"] else "❌ Not Found"
    table.add_row(f"Image ({manager.full_image})", image_status)

    # Container status
    if status["container_exists"]:
        if status["container_running"]:
            container_status = "🟢 Running"
        else:
            container_status = "🟡 Stopped"
    else:
        container_status = "❌ Not Created"
    table.add_row(f"Container ({manager.CONTAINER_NAME})", container_status)

    # Additional info if container exists
    if status["container_info"]:
        info = status["container_info"]
        table.add_row("Container ID", info.get("id", "N/A"))
        table.add_row("State", info.get("state", "N/A"))

    console.print(table)

    # Show helpful commands
    if not status["docker_available"]:
        console.print(
            "\n[yellow]Please install Docker to use container features[/yellow]"
        )
    elif not status["container_running"]:
        console.print(
            "\n[dim]Run 'wrkenv container start' to start the container[/dim]"
        )
    else:
        console.print(
            "\n[dim]Run 'wrkenv container enter' to access the container[/dim]"
        )


def container_logs(
    config: WorkenvConfig | None = None, follow: bool = False, tail: int = 100
) -> None:
    """Show container logs."""
    manager = ContainerManager(config)
    manager.logs(follow=follow, tail=tail)


def clean_container(config: WorkenvConfig | None = None) -> bool:
    """Clean up container and image."""
    manager = ContainerManager(config)
    return manager.clean()


def rebuild_container(config: WorkenvConfig | None = None) -> bool:
    """Rebuild the container from scratch."""
    manager = ContainerManager(config)
    console = Console()

    console.print(f"{manager.BUILD_EMOJI} Rebuilding container from scratch...")

    # Clean existing resources
    if not manager.clean():
        return False

    # Build fresh image
    if not manager.build_image(rebuild=True):
        return False

    # Start new container
    return manager.start()
