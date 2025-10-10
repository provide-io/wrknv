#!/usr/bin/env python3
#
# wrknv/cli/commands/tools.py
#
"""
Tool Management Commands
========================
Commands for managing development tools (status, sync, doctor, etc).
"""

from __future__ import annotations


import pathlib
import sys

from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation.hub import register_command
from provide.foundation.logger import get_logger
from rich.table import Table

logger = get_logger(__name__)

from wrknv.config import WorkenvConfig
from wrknv.lockfile import LockfileManager
from wrknv.wenv.doctor import run_doctor
from wrknv.wenv.env_generator import create_project_env_scripts
from wrknv.managers.factory import get_tool_manager
from wrknv.utils.version_resolver import resolve_tool_versions
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

        # Handle matrix format (list of versions) and resolve patterns
        if isinstance(version, list):
            version_str = ", ".join(version)
            try:
                manager = get_tool_manager(tool_name, config)
                resolved_versions = resolve_tool_versions(manager, version)
                if resolved_versions:
                    resolved_str = ", ".join(resolved_versions)
                    # Show both pattern and resolved if different
                    if set(version) != set(resolved_versions):
                        version_str = f"{version_str} → {resolved_str}"
                    else:
                        version_str = resolved_str
            except Exception as e:
                logger.debug(f"Could not resolve versions for {tool_name}: {e}")
        else:
            version_str = version or "Not specified"
            # Try to resolve single version pattern
            if version and version != "Not specified":
                try:
                    manager = get_tool_manager(tool_name, config)
                    resolved_versions = resolve_tool_versions(manager, version)
                    if resolved_versions and resolved_versions[0] != version:
                        version_str = f"{version} → {resolved_versions[0]}"
                    else:
                        version_str = resolved_versions[0] if resolved_versions else version
                except Exception as e:
                    logger.debug(f"Could not resolve version for {tool_name}: {e}")

        table.add_row(
            f"{tool_emoji} {tool_name}",
            version_str,
            f"{Emoji.INFO} Configured",
        )

    console.print(table)


@register_command("sync", description="Install all tools defined in configuration", category="tools")
def sync_command(lock: bool = True):
    """Install all tools defined in configuration."""
    config = WorkenvConfig.load()
    tools = config.get_all_tools()

    if not tools:
        echo_info("No tools configured in workenv configuration")
        return

    # Initialize lockfile manager
    lockfile_manager = LockfileManager()

    if lock:
        echo_info("🔒 Resolving and locking tool versions...")
        lockfile = lockfile_manager.resolve_and_lock(config)
        echo_success(f"✅ Lockfile updated with {len(lockfile.resolved_tools)} resolved tools")

    echo_info("Syncing tools from configuration...")

    for tool_name, version in tools.items():
        try:
            manager = get_tool_manager(tool_name, config)

            # Handle matrix format (list of versions)
            if isinstance(version, list):
                # Resolve version patterns to specific versions
                resolved_versions = resolve_tool_versions(manager, version)
                echo_info(f"\nResolved {tool_name} patterns {version} to {resolved_versions}")

                for v in resolved_versions:
                    echo_info(f"Installing {tool_name} {v}...")
                    manager.install_version(v, dry_run=False)
                    echo_success(f"✅ Successfully installed {tool_name} {v}")
            else:
                # Resolve single version pattern
                resolved_versions = resolve_tool_versions(manager, version)
                if resolved_versions:
                    resolved_version = resolved_versions[0]
                    if resolved_version != version:
                        echo_info(f"Resolved {tool_name} pattern '{version}' to '{resolved_version}'")

                    echo_info(f"Installing {tool_name} {resolved_version}...")
                    manager.install_version(resolved_version, dry_run=False)
                    echo_success(f"✅ Successfully installed {tool_name} {resolved_version}")
                else:
                    echo_error(f"❌ Could not resolve version pattern '{version}' for {tool_name}")

        except Exception as e:
            version_str = ", ".join(version) if isinstance(version, list) else version
            echo_error(f"❌ Error installing {tool_name} {version_str}: {e}")


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
