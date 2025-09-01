#!/usr/bin/env python3
#
# wrknv/cli/commands/tools.py
#
"""
Tool Management Commands
========================
Commands for managing development tools (status, sync, doctor, etc).
"""

import pathlib
import sys

import click
from rich.table import Table

from wrknv.wenv.config import WorkenvConfig
from wrknv.wenv.doctor import run_doctor
from wrknv.wenv.env_generator import create_project_env_scripts
from wrknv.wenv.managers.factory import get_tool_manager
from wrknv.wenv.visual import (
    Emoji,
    get_console,
    get_tool_emoji,
    print_warning,
)


@click.command(name="status")
def status_command():
    """📊 Show status of all managed tools."""
    config = WorkenvConfig()
    tools = config.get_all_tools()
    console = get_console()

    if not tools:
        print_warning("No tools configured")
        return

    # Create status table
    table = Table(title=f"{Emoji.STATUS} Tool Status", show_header=True)
    table.add_column("Tool", style="cyan")
    table.add_column("Configured Version", style="yellow")
    table.add_column("Status", style="green")

    for tool_name, version in tools.items():
        tool_emoji = get_tool_emoji(tool_name)
        # Check if tool is installed (simplified for now)
        table.add_row(
            f"{tool_emoji} {tool_name}",
            version or "Not specified",
            f"{Emoji.INFO} Configured",
        )

    console.print(table)


@click.command(name="sync")
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


@click.command(name="generate-env")
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=pathlib.Path),
    default=pathlib.Path("env.sh"),
    help="Output path for the environment script",
)
@click.option(
    "--shell",
    type=click.Choice(["bash", "zsh", "sh", "powershell", "ps1"]),
    default="sh",
    help="Target shell type",
)
@click.option(
    "--project-dir",
    type=click.Path(exists=True, dir_okay=True, path_type=pathlib.Path),
    default=pathlib.Path.cwd(),
    help="Project directory to generate env script for",
)
def generate_env_command(output: pathlib.Path, shell: str, project_dir: pathlib.Path):
    """🌍 Generate optimized environment setup script."""
    click.echo(f"🔧 Generating environment scripts for {project_dir.name}...")

    try:
        # Use the existing function that works
        sh_path, ps1_path = create_project_env_scripts(project_dir)

        # Move to requested output location if different
        if shell in ["powershell", "ps1"]:
            if output != ps1_path:
                import shutil

                shutil.move(str(ps1_path), str(output))
                ps1_path = output
            click.echo(f"✅ Generated {ps1_path}")
        else:
            if output != sh_path:
                import shutil

                shutil.move(str(sh_path), str(output))
                sh_path = output
            click.echo(f"✅ Generated {sh_path}")

        click.echo("\nTo use the environment:")
        click.echo(f"  source {output}")

    except FileNotFoundError as e:
        click.echo(f"❌ Error: {e}")
        click.echo("Make sure you're in a project directory with pyproject.toml")


@click.command()
@click.option("--verbose", "-v", is_flag=True, help="Show detailed diagnostic output")
def doctor(verbose):
    """🩺 Diagnose and fix common wrknv environment issues.
    
    Checks for:
    - Correct workenv directory structure
    - Valid env.sh script
    - Required dependencies (uv, git, etc.)
    - Configuration file validity
    - Common problems and their solutions
    """
    sys.exit(run_doctor(verbose))