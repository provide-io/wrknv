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
from rich.table import Table

from provide.foundation.hub import register_command
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation import logger

from wrknv.config import WorkenvConfig
from wrknv.wenv.doctor import run_doctor
from wrknv.wenv.env_generator import create_project_env_scripts
from wrknv.wenv.managers.factory import get_tool_manager
from wrknv.wenv.visual import Emoji, get_console, get_tool_emoji


@register_command("status", description="Show status of all managed tools", category="tools")
def status_command():
    """Show status of all managed tools."""
    config = WorkenvConfig.load()
    tools = config.get_all_tools()
    console = get_console()

    if not tools:
        echo_warning("No tools configured")
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


@register_command("sync", description="Install all tools defined in configuration", category="tools")
def sync_command():
    """Install all tools defined in configuration."""
    config = WorkenvConfig.load()
    tools = config.get_all_tools()

    if not tools:
        echo_info("No tools configured in workenv configuration")
        return

    echo_info("Syncing tools from configuration...")

    for tool_name, version in tools.items():
        try:
            manager = get_tool_manager(tool_name, config)
            echo_info(f"\nInstalling {tool_name} {version}...")
            manager.install_version(version, dry_run=False)
            echo_success(f"✅ Successfully installed {tool_name} {version}")
        except Exception as e:
            echo_error(f"❌ Error installing {tool_name} {version}: {e}")


@register_command(
    "generate-env",
    description="Generate optimized environment setup script",
    category="tools",
)
def generate_env_command(
    output: pathlib.Path = pathlib.Path("env.sh"),
    shell: str = "sh",
    project_dir: pathlib.Path = pathlib.Path.cwd(),
):
    """Generate optimized environment setup script.
    
    Args:
        output: Output path for the environment script
        shell: Target shell type (bash/zsh/sh/powershell/ps1)
        project_dir: Project directory to generate env script for
    """
    echo_info(f"🔧 Generating environment scripts for {project_dir.name}...")

    try:
        # Use the existing function that works
        sh_path, ps1_path = create_project_env_scripts(project_dir)

        # Move to requested output location if different
        if shell in ["powershell", "ps1"]:
            if output != ps1_path:
                import shutil
                shutil.move(str(ps1_path), str(output))
                ps1_path = output
            echo_success(f"✅ Generated {ps1_path}")
        else:
            if output != sh_path:
                import shutil
                shutil.move(str(sh_path), str(output))
                sh_path = output
            echo_success(f"✅ Generated {sh_path}")

        echo_info("\nTo use the environment:")
        echo_info(f"  source {output}")

    except FileNotFoundError as e:
        echo_error(f"❌ Error: {e}")
        echo_error("Make sure you're in a project directory with pyproject.toml")


@register_command("doctor", description="Diagnose and fix common wrknv environment issues", category="tools")
def doctor(verbose: bool = False):
    """Diagnose and fix common wrknv environment issues.
    
    Checks for:
    - Correct workenv directory structure
    - Valid env.sh script
    - Required dependencies (uv, git, etc.)
    - Configuration file validity
    - Common problems and their solutions
    
    Args:
        verbose: Show detailed diagnostic output
    """
    sys.exit(run_doctor(verbose))