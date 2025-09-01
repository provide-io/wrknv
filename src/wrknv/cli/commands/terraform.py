#!/usr/bin/env python3
#
# wrknv/cli/commands/terraform.py
#
"""
Terraform/OpenTofu Commands
===========================
Commands for managing Terraform and OpenTofu installations.
"""

import sys

import click

from wrknv.wenv.config import WorkenvConfig
from wrknv.wenv.managers.factory import get_tool_manager
from wrknv.wenv.visual import Emoji, print_error, print_info, print_success, print_warning


@click.command(name="tf")
@click.argument("version", required=False)
@click.option("--latest", is_flag=True, help="Install latest version")
@click.option("--list", is_flag=True, help="List available versions")
@click.option("--dry-run", is_flag=True, help="Show what would be installed")
@click.option("--terraform", is_flag=True, help="Install Terraform instead of OpenTofu")
def tf_command(
    version: str | None, latest: bool, list: bool, dry_run: bool, terraform: bool
):
    """Install or manage Terraform/OpenTofu versions."""
    config = WorkenvConfig()

    # Determine which tool to manage
    tool_name = "terraform" if terraform else "tofu"
    tool_display = "Terraform" if terraform else "OpenTofu"
    tool_emoji = Emoji.TERRAFORM if terraform else Emoji.OPENTOFU

    if list:
        # List available versions
        try:
            manager = get_tool_manager(tool_name, config)
            print_info(f"Available {tool_display} versions:", tool_emoji)
            manager.list_versions()
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    elif latest:
        # Install latest version
        try:
            manager = get_tool_manager(tool_name, config)
            manager.install_latest(dry_run=dry_run)
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    elif version:
        # Install specific version
        try:
            manager = get_tool_manager(tool_name, config)
            if dry_run:
                print_info(f"[DRY-RUN] Would install {tool_display} {version}")
            else:
                print_info(
                    f"Installing {tool_display} {version}...",
                    f"{tool_emoji} {Emoji.DOWNLOAD}",
                )
            manager.install_version(version, dry_run=dry_run)
            if not dry_run:
                print_success(f"Successfully installed {tool_display} {version}")
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    else:
        print_warning("Please specify a version, --latest, or --list")
        print_info("Examples:")
        print_info("  wrknv tf --list              # List OpenTofu versions")
        print_info("  wrknv tf 1.8.0               # Install OpenTofu 1.8.0")
        print_info("  wrknv tf --terraform 1.5.7   # Install Terraform 1.5.7")
        print_info("  wrknv tf --terraform --list  # List Terraform versions")
        sys.exit(1)