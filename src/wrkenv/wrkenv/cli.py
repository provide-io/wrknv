#!/usr/bin/env python3
#
# wrkenv/wrkenv/cli.py
#
"""
wrkenv CLI Commands
===================
Command-line interface for wrkenv tool management.
"""

import pathlib
import sys
from typing import Optional

import click
from click.testing import CliRunner

from wrkenv.wrkenv.config import WorkenvConfig, WorkenvConfigError
from wrkenv.wrkenv.managers.factory import get_supported_tools, get_tool_manager


@click.group(name="workenv", invoke_without_command=True)
@click.pass_context
def workenv_cli(ctx):
    """🧰🌍 Manage development environment tools and versions.

    wrkenv provides cross-platform tool installation and version management
    for development environments, including Terraform, OpenTofu, Go, UV, and more.
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


# === Direct Tool Commands ===

@workenv_cli.command(name="tf")
@click.argument("version", required=False)
@click.option("--latest", is_flag=True, help="Install latest version")
@click.option("--list", is_flag=True, help="List available versions")
@click.option("--dry-run", is_flag=True, help="Show what would be installed")
def tf_command(version: Optional[str], latest: bool, list: bool, dry_run: bool):
    """Install or manage OpenTofu versions."""
    config = WorkenvConfig()
    
    if list:
        # List available versions
        try:
            manager = get_tool_manager("tofu", config)
            click.echo("Available OpenTofu versions:")
            manager.list_versions()
        except Exception as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    elif latest:
        # Install latest version
        try:
            manager = get_tool_manager("tofu", config)
            manager.install_latest(dry_run=dry_run)
        except Exception as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    elif version:
        # Install specific version
        try:
            manager = get_tool_manager("tofu", config)
            if dry_run:
                click.echo(f"[DRY-RUN] Would install OpenTofu {version}")
            else:
                click.echo(f"Installing OpenTofu {version}...")
            manager.install_version(version, dry_run=dry_run)
            if not dry_run:
                click.echo(f"✅ Successfully installed OpenTofu {version}")
        except Exception as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    else:
        click.echo("Please specify a version, --latest, or --list")
        sys.exit(1)


@workenv_cli.command(name="terraform")
@click.argument("version")
@click.option("--dry-run", is_flag=True, help="Show what would be installed")
def terraform_command(version: str, dry_run: bool):
    """Install specific Terraform version."""
    config = WorkenvConfig()
    
    try:
        manager = get_tool_manager("terraform", config)
        if dry_run:
            click.echo(f"[DRY-RUN] Would install Terraform {version}")
        else:
            click.echo(f"Installing Terraform {version}...")
        manager.install_version(version, dry_run=dry_run)
        if not dry_run:
            click.echo(f"✅ Successfully installed Terraform {version}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


# === Status Command ===

@workenv_cli.command(name="status")
def status_command():
    """📊 Show status of all managed tools."""
    config = WorkenvConfig()
    tools = config.get_all_tools()
    
    if not tools:
        click.echo("No tools configured")
        return
    
    for tool_name, version in tools.items():
        click.echo(f"{tool_name}: {version}")


# === Sync Command ===

@workenv_cli.command(name="sync")
def sync_command():
    """🔄 Install all tools defined in configuration."""
    config = WorkenvConfig()
    tools = config.get_all_tools()
    
    if not tools:
        click.echo("No tools configured in workenv configuration")
        return
    
    click.echo("Syncing tools from configuration...")
    
    for tool_name, version in tools.items():
        try:
            manager = get_tool_manager(tool_name, config)
            click.echo(f"\nInstalling {tool_name} {version}...")
            manager.install_version(version, dry_run=False)
            click.echo(f"✅ Successfully installed {tool_name} {version}")
        except Exception as e:
            click.echo(f"❌ Error installing {tool_name} {version}: {e}")


# === Matrix Test Command ===

@workenv_cli.command(name="matrix-test")
def matrix_test_command():
    """🧪 Run tests against multiple tool version combinations."""
    try:
        from wrkenv.workenv.testing.matrix import VersionMatrix
    except ImportError:
        click.echo("Matrix testing not available", err=True)
        sys.exit(1)
    
    config = WorkenvConfig()
    
    # Get matrix configuration
    matrix_config = config.get_setting("matrix", {})
    if not matrix_config:
        click.echo("No matrix configuration found")
        sys.exit(1)
    
    matrix = VersionMatrix(matrix_config)
    
    # Run the matrix tests
    click.echo("Running matrix tests...")
    results = matrix.run_tests(lambda versions: True)  # Dummy test function
    
    click.echo(f"\nResults:")
    click.echo(f"  Success: {results.get('success_count', 0)}")
    click.echo(f"  Failure: {results.get('failure_count', 0)}")


# === Profile Commands ===

@workenv_cli.group(name="profile")
def profile_group():
    """👤 Manage workenv profiles."""
    pass


@profile_group.command(name="list")
def profile_list():
    """List available profiles."""
    config = WorkenvConfig()
    
    profiles = config.list_profiles()
    
    if profiles:
        click.echo("Available profiles:")
        for name in profiles:
            if name == config.get_current_profile():
                click.echo(f"  * {name} (active)")
            else:
                click.echo(f"    {name}")
    else:
        click.echo("No profiles configured")


@profile_group.command(name="save")
@click.argument("name")
def profile_save(name: str):
    """Save current tool versions as a profile."""
    config = WorkenvConfig()
    
    config.save_profile(name)
    click.echo(f"Saved profile '{name}'")


@profile_group.command(name="load")
@click.argument("name")
def profile_load(name: str):
    """Load and install tools from a profile."""
    config = WorkenvConfig()
    
    profile = config.get_profile(name)
    if not profile:
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)
    
    click.echo(f"Loading profile '{name}'...")
    for tool_name, version in profile.items():
        try:
            manager = get_tool_manager(tool_name, config)
            click.echo(f"Installing {tool_name} {version}...")
            manager.install_version(version, dry_run=False)
            click.echo(f"✅ Successfully installed {tool_name} {version}")
        except Exception as e:
            click.echo(f"❌ Error installing {tool_name} {version}: {e}")


# === Config Commands ===

@workenv_cli.group(name="config")
def config_group():
    """⚙️ Manage workenv configuration."""
    pass


@config_group.command(name="show")
def config_show():
    """Show current configuration."""
    config = WorkenvConfig()
    config.show_config()


@config_group.command(name="edit")
def config_edit():
    """Edit configuration file."""
    config = WorkenvConfig()
    config.edit_config()


# === TF Subcommands (moved to tf command above) ===
# Removed tf group to avoid conflict with tf command


# === Entry Point ===

def entry_point():
    """Main entry point for the wrkenv CLI."""
    workenv_cli()


if __name__ == "__main__":
    entry_point()


# 🧰🌍🖥️🪄