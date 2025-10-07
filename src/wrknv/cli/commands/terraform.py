#!/usr/bin/env python3
#
# wrknv/cli/commands/terraform.py
#
"""
Terraform/OpenTofu Commands
===========================
Commands for managing Terraform and OpenTofu installations.
"""

from __future__ import annotations


import sys

import click
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation.hub import register_command

from wrknv.config import WorkenvConfig
from wrknv.managers.factory import get_tool_manager
from wrknv.wenv.visual import Emoji


@register_command("tf", description="Manage Terraform/OpenTofu versions", category="tools")
@click.argument("variant_or_version", required=False)
@click.argument("version", required=False)
@click.option("--list", is_flag=True, help="List available versions")
@click.option("--list-variants", is_flag=True, help="List available variants")
@click.option("--dry-run", is_flag=True, help="Show what would be done")
def tf_command(
    variant_or_version: str | None = None,
    version: str | None = None,
    list: bool = False,
    list_variants: bool = False,
    dry_run: bool = False,
):
    """Manage Terraform/OpenTofu versions.

    Switch to a specific variant and version of Terraform ecosystem tools.
    This command will install the version if needed and activate it in your workenv.

    Examples:
        wrknv tf tofu 1.9.0     # Switch to OpenTofu 1.9.0
        wrknv tf ibm 1.6.2      # Switch to IBM Terraform 1.6.2
        wrknv tf 1.9.0          # Switch to default (tofu)
        wrknv tf --list-variants
        wrknv tf tofu --list    # List available OpenTofu versions

    Args:
        variant_or_version: Variant name (tofu/ibm) or version if using default
        version: Version to switch to (if first arg was variant)
        list: List available versions
        list_variants: List available variants
        dry_run: Show what would be done without doing it
    """
    config = WorkenvConfig.load()

    if list_variants:
        echo_info(f"{Emoji.TERRAFORM} Available Terraform ecosystem variants:")
        echo_info("  • tofu - OpenTofu (open source fork)")
        echo_info("  • ibm  - IBM Terraform (formerly HashiCorp)")
        return

    # Get default variant for list/install operations
    default_variant = config.get_setting("tools.tf.default_variant", "tofu")

    # Smart parsing: determine variant and version
    if variant_or_version is None:
        # No args: use default variant (only valid with --list)
        if not list:
            echo_error("Error: Version required. Use 'wrknv tf --list' to see available versions.")
            sys.exit(1)
        actual_variant = default_variant
        actual_version = None
    elif version is None:
        # Single arg: use default variant from config
        actual_variant = default_variant
        actual_version = variant_or_version

        if not list:
            echo_info(f"Using default variant: {actual_variant}")
    else:
        # Two args: explicit variant specified
        actual_variant = variant_or_version
        actual_version = version

    # Map variant to manager name
    variant_map = {
        "tofu": "tofu",
        "opentofu": "tofu",  # Alias
        "ibm": "ibmtf",
        "terraform": "ibmtf",  # Alias
        "ibmtf": "ibmtf",
    }

    manager_name = variant_map.get(actual_variant.lower())
    if not manager_name:
        echo_error(f"Unknown Terraform variant: {actual_variant}")
        echo_info("Available variants: tofu, ibm")
        sys.exit(1)

    # Variant display names
    variant_display = {
        "tofu": "OpenTofu",
        "ibmtf": "IBM Terraform",
    }
    display_name = variant_display.get(manager_name, manager_name)
    tool_emoji = Emoji.OPENTOFU if manager_name == "tofu" else Emoji.TERRAFORM

    if list:
        # List available versions for this variant
        try:
            manager = get_tool_manager(manager_name, config)
            echo_info(f"{tool_emoji} Available {display_name} versions:")
            versions = manager.get_available_versions()
            for v in versions[:20]:  # Show first 20
                echo_info(f"  • {v}")
            if len(versions) > 20:
                echo_info(f"  ... and {len(versions) - 20} more")
            echo_info(f"\nTotal: {len(versions)} versions available")
        except Exception as e:
            echo_error(f"Error listing versions: {e}")
            sys.exit(1)
        return

    # Switch to the specified version
    try:
        manager = get_tool_manager(manager_name, config)

        if dry_run:
            echo_info(f"[DRY-RUN] Would switch to {display_name} {actual_version}")
        else:
            echo_info(
                f"{tool_emoji} Switching to {display_name} {actual_version}...",
            )

        manager.switch_version(actual_version, dry_run=dry_run)

        if not dry_run:
            echo_success(f"✅ Switched to {display_name} {actual_version}")
            echo_info(f"💡 Run 'source env.sh' to activate in current shell")
            echo_info(f"💡 Or restart your terminal")
    except Exception as e:
        echo_error(f"Error: {e}")
        import traceback
        echo_error(traceback.format_exc())
        sys.exit(1)
