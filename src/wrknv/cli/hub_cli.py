#!/usr/bin/env python3
#
# wrknv/cli/hub_cli.py
#
"""
Hub-based CLI Entry Point
=========================
Main CLI using provide.foundation.hub for command registration.
"""

import os
from provide.foundation.hub import Hub, get_hub
from provide.foundation.context import Context
from provide.foundation import logger


def setup_logging_environment():
    """Set up logging environment variables to bridge WRKNV_ to PROVIDE_ variables."""
    # Bridge WRKNV_LOG_LEVEL to PROVIDE_LOG_LEVEL if set
    wrknv_log_level = os.environ.get("WRKNV_LOG_LEVEL")
    if wrknv_log_level and not os.environ.get("PROVIDE_LOG_LEVEL"):
        os.environ["PROVIDE_LOG_LEVEL"] = wrknv_log_level
    
    # Set default if neither is set
    if not os.environ.get("PROVIDE_LOG_LEVEL") and not wrknv_log_level:
        os.environ["PROVIDE_LOG_LEVEL"] = "WARNING"


def load_commands():
    """Import all command modules to trigger registration."""
    # Import command modules to trigger @register_command decorators
    from wrknv.cli.commands import setup  # noqa: F401
    from wrknv.cli.commands import terraform  # noqa: F401
    from wrknv.cli.commands import tools  # noqa: F401
    from wrknv.cli.commands import config  # noqa: F401
    from wrknv.cli.commands import container  # noqa: F401
    from wrknv.cli.commands import gitignore  # noqa: F401
    from wrknv.cli.commands import profile  # noqa: F401
    from wrknv.cli.commands import package  # noqa: F401
    
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
    # Set up logging environment before foundation initialization
    setup_logging_environment()
    
    cli = create_cli()
    cli()


if __name__ == "__main__":
    main()