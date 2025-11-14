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

from provide.foundation.hub import register_command
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation.logger import get_logger

from wrknv.wenv.config import WorkenvConfig
from wrknv.wenv.managers.factory import get_tool_manager
from wrknv.wenv.visual import Emoji

log = get_logger(__name__)


@register_command("tf", description="Install or manage Terraform/OpenTofu versions", category="tools")
def tf_command(
    version: str | None = None,
    latest: bool = False,
    list: bool = False,
    dry_run: bool = False,
    terraform: bool = False,
):
    """Install or manage Terraform/OpenTofu versions.
    
    Args:
        version: Version to install
        latest: Install latest version
        list: List available versions
        dry_run: Show what would be installed
        terraform: Install Terraform instead of OpenTofu
    """
    config = WorkenvConfig()

    # Determine which tool to manage
    tool_name = "terraform" if terraform else "tofu"
    tool_display = "Terraform" if terraform else "OpenTofu"
    tool_emoji = Emoji.TERRAFORM if terraform else Emoji.OPENTOFU

    if list:
        # List available versions
        try:
            manager = get_tool_manager(tool_name, config)
            echo_info(f"Available {tool_display} versions:", prefix=tool_emoji)
            manager.list_versions()
        except Exception as e:
            echo_error(f"Error: {e}")
            sys.exit(1)
    elif latest:
        # Install latest version
        try:
            manager = get_tool_manager(tool_name, config)
            manager.install_latest(dry_run=dry_run)
        except Exception as e:
            echo_error(f"Error: {e}")
            sys.exit(1)
    elif version:
        # Install specific version
        try:
            manager = get_tool_manager(tool_name, config)
            if dry_run:
                echo_info(f"[DRY-RUN] Would install {tool_display} {version}")
            else:
                echo_info(
                    f"Installing {tool_display} {version}...",
                    prefix=f"{tool_emoji} {Emoji.DOWNLOAD}",
                )
            manager.install_version(version, dry_run=dry_run)
            if not dry_run:
                echo_success(f"Successfully installed {tool_display} {version}")
        except Exception as e:
            echo_error(f"Error: {e}")
            sys.exit(1)
    else:
        echo_warning("Please specify a version, --latest, or --list")
        echo_info("Examples:")
        echo_info("  wrknv tf --list              # List OpenTofu versions")
        echo_info("  wrknv tf 1.8.0               # Install OpenTofu 1.8.0")
        echo_info("  wrknv tf --terraform 1.5.7   # Install Terraform 1.5.7")
        echo_info("  wrknv tf --terraform --list  # List Terraform versions")
        sys.exit(1)