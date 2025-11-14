#!/usr/bin/env python3
#
# wrknv/cli/main.py
#
"""
Main CLI Entry Point
====================
Minimal main CLI that imports and registers all command modules.
"""

import click

# Import command groups
from wrknv.cli.commands.config import config_group
from wrknv.cli.commands.container import container_group
from wrknv.cli.commands.gitignore import gitignore_group
from wrknv.cli.commands.package import package_group
from wrknv.cli.commands.profile import profile_group

# Import individual commands
from wrknv.cli.commands.setup import setup_command
from wrknv.cli.commands.terraform import tf_command
from wrknv.cli.commands.tools import (
    doctor,
    generate_env_command,
    status_command,
    sync_command,
)


@click.group(name="workenv", invoke_without_command=True)
@click.pass_context
def workenv_cli(ctx):
    """🧰🌍 Manage development environment tools and versions.

    wrknv provides cross-platform tool installation and version management
    for development environments, including Terraform, OpenTofu, Go, UV, and more.
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


# Register command groups
workenv_cli.add_command(config_group)
workenv_cli.add_command(container_group)
workenv_cli.add_command(gitignore_group)
workenv_cli.add_command(package_group)
workenv_cli.add_command(profile_group)

# Register individual commands
workenv_cli.add_command(setup_command)
workenv_cli.add_command(tf_command)
workenv_cli.add_command(status_command)
workenv_cli.add_command(sync_command)
workenv_cli.add_command(generate_env_command)
workenv_cli.add_command(doctor)


def entry_point():
    """Main entry point for the wrknv CLI."""
    workenv_cli()


if __name__ == "__main__":
    entry_point()


# 🧰🌍🖥️🪄