# wrknv/cli/hub_cli.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#
# wrknv/cli/hub_cli.py
#
"""
"""
Hub-based CLI Entry Point
=========================
Main CLI using provide.foundation.hub for command registration.
from __future__ import annotations

import importlib
import sys

from provide.foundation.hub import get_hub
from provide.foundation.logger import get_logger

from wrknv.config import WorkenvConfig

logger = get_logger(__name__)


class WrknvContext:
    """Shared context for wrknv CLI commands."""

    _config = None

    @classmethod
    def get_config(cls) -> WorkenvConfig:
        """Get or load the WorkenvConfig singleton."""
        if cls._config is None:
            cls._config = WorkenvConfig.load()
        return cls._config

    @classmethod
    def reset(cls):
        """Reset config cache (for testing)."""
        cls._config = None


def load_commands():
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def create_cli():
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

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
# 🧰🌍🖥️🪄
