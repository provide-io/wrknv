#!/usr/bin/env python3
#
# wrknv/cli/commands/profile.py
#
"""
Profile Commands
================
Commands for managing workenv profiles.
"""

import pathlib
import sys

import click

from wrknv.wenv.config import WorkenvConfig
from wrknv.wenv.managers.factory import get_tool_manager


@click.group(name="profile")
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
        click.echo("No profiles found")


@profile_group.command(name="save")
@click.argument("name")
@click.option("--force", is_flag=True, help="Overwrite existing profile")
def profile_save(name: str, force: bool):
    """Save current tool versions as a profile."""
    config = WorkenvConfig()

    # Check if profile exists
    if not force and config.profile_exists(name):
        if not click.confirm(f"Profile '{name}' already exists. Overwrite?"):
            return

    # Get current tools
    tools = config.get_all_tools()
    config.save_profile(name, tools)
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


@profile_group.command(name="show")
@click.argument("name")
def profile_show(name: str):
    """Show details of a profile."""
    config = WorkenvConfig()

    profile = config.get_profile(name)
    if not profile:
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    click.echo(f"Profile: {name}")
    for tool_name, version in profile.items():
        click.echo(f"  {tool_name}: {version}")


@profile_group.command(name="delete")
@click.argument("name")
def profile_delete(name: str):
    """Delete a profile."""
    config = WorkenvConfig()

    if not config.profile_exists(name):
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    if click.confirm(f"Delete profile '{name}'?"):
        if config.delete_profile(name):
            click.echo(f"Profile '{name}' deleted")
        else:
            click.echo(f"Failed to delete profile '{name}'")
            sys.exit(1)


@profile_group.command(name="export")
@click.argument("name")
@click.option("--output", "-o", help="Output file path")
def profile_export(name: str, output: str):
    """Export a profile to a file."""
    import tomli_w

    config = WorkenvConfig()
    profile = config.get_profile(name)

    if not profile:
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    profile_data = {"name": name, "tools": profile}

    if output:
        output_path = pathlib.Path(output)
    else:
        output_path = pathlib.Path(f"{name}-profile.toml")

    with open(output_path, "w") as f:
        f.write(tomli_w.dumps(profile_data))

    click.echo(f"Exported profile '{name}' to {output_path}")


@profile_group.command(name="import")
@click.argument("file")
def profile_import(file: str):
    """Import a profile from a file."""
    import tomllib

    file_path = pathlib.Path(file)
    if not file_path.exists():
        click.echo(f"File '{file}' not found")
        sys.exit(1)

    with open(file_path, "rb") as f:
        profile_data = tomllib.load(f)

    name = profile_data.get("name", file_path.stem)
    tools = profile_data.get("tools", {})

    config = WorkenvConfig()
    config.save_profile(name, tools)

    click.echo(f"Imported profile '{name}'")