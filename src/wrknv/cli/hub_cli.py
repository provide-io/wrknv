#!/usr/bin/env python3
#
# wrknv/cli/hub_cli.py
#
"""
Hub-based CLI Entry Point
=========================
Main CLI using provide.foundation.hub for command registration.
"""

from provide.foundation.hub import get_hub
from provide.foundation.logger import get_logger

logger = get_logger(__name__)


def load_commands():
    """Import all command modules to trigger registration."""
    # Import command modules to trigger @register_command decorators
    from wrknv.cli.commands import (
        config,  # noqa: F401
        container,  # noqa: F401
        doctor,  # noqa: F401
        gitignore,  # noqa: F401
        lock,  # noqa: F401
        package,  # noqa: F401
        profile,  # noqa: F401
        setup,  # noqa: F401
        terraform,  # noqa: F401
        tools,  # noqa: F401
        workenv,  # noqa: F401
        workspace,  # noqa: F401
    )

    logger.debug("Loaded wrknv command modules")


def create_cli():
    """Create the main CLI application using the hub."""
    # Load all commands
    load_commands()

    # Get or create hub
    hub = get_hub()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.1.0",
        help="🧰🌍 Manage development environment tools and versions.\n\n"
        "wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def main():
    """Main entry point for the CLI."""
    # Note: Logging setup disabled for now due to missing dependencies
    # from wrknv.logging.setup import setup_wrknv_logging
    # setup_wrknv_logging()

    cli = create_cli()
    cli()


if __name__ == "__main__":
    main()
