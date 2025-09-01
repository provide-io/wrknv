#!/usr/bin/env python3
#
# wrknv/cli/commands/setup.py
#
"""
Setup Commands
==============
Commands for setting up wrknv environment and integrations.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import click

from wrknv.wenv.exceptions import DependencyError
from wrknv.wenv.visual import (
    Emoji,
    print_error,
    print_info,
    print_success,
    print_warning,
)
from wrknv.wenv.workenv import WorkenvManager


@click.command(name="setup")
@click.option("--shell-integration", is_flag=True, help="Set up shell aliases")
@click.option("--init", is_flag=True, help="Initialize wrknv's own workenv")
@click.option("--force", is_flag=True, help="Force recreate workenv")
@click.option("--check", is_flag=True, help="Check system dependencies")
@click.option(
    "--completions",
    type=click.Choice(["bash", "zsh", "fish"]),
    help="Generate shell completions",
)
@click.option(
    "--install", is_flag=True, help="Install completions (use with --completions)"
)
def setup_command(
    shell_integration: bool,
    init: bool,
    force: bool,
    check: bool,
    completions: str,
    install: bool,
):
    """Set up wrknv environment and integrations."""
    if check:
        # Check system dependencies
        print_info("Checking system dependencies...", Emoji.INFO)

        required_deps = ["git", "curl", "python3"]
        optional_deps = ["docker", "wget"]
        missing_required = []
        missing_optional = []

        for dep in required_deps:
            if shutil.which(dep):
                print_success(f"  ✓ {dep}")
            else:
                print_error(f"  ✗ {dep} (required)")
                missing_required.append(dep)

        for dep in optional_deps:
            if shutil.which(dep):
                print_info(f"  ✓ {dep} (optional)")
            else:
                print_warning(f"  ✗ {dep} (optional)")
                missing_optional.append(dep)

        if missing_required:
            raise DependencyError(missing_required, "wrknv core functionality")
        else:
            print_success("All required dependencies are installed!")
        return

    if completions:
        # Generate shell completions
        from wrknv.wenv.completions import generate_completions

        completion_script = generate_completions(completions)

        if install:
            # Install completions to appropriate location
            install_path = None
            if completions == "bash":
                # Try common bash completion directories
                for path in [
                    Path.home() / ".bash_completion.d",
                    Path("/etc/bash_completion.d"),
                    Path("/usr/local/etc/bash_completion.d"),
                ]:
                    if path.exists() and path.is_dir():
                        install_path = path / "wrknv"
                        break

                if not install_path:
                    # Create user directory
                    user_dir = Path.home() / ".bash_completion.d"
                    user_dir.mkdir(exist_ok=True)
                    install_path = user_dir / "wrknv"

            elif completions == "zsh":
                # Zsh completion paths
                for path in [
                    Path.home() / ".zsh/completions",
                    Path("/usr/local/share/zsh/site-functions"),
                ]:
                    if path.exists() and path.is_dir():
                        install_path = path / "_wrknv"
                        break

                if not install_path:
                    # Create user directory
                    user_dir = Path.home() / ".zsh/completions"
                    user_dir.mkdir(parents=True, exist_ok=True)
                    install_path = user_dir / "_wrknv"

            elif completions == "fish":
                # Fish completion path
                fish_dir = Path.home() / ".config/fish/completions"
                fish_dir.mkdir(parents=True, exist_ok=True)
                install_path = fish_dir / "wrknv.fish"

            if install_path:
                install_path.write_text(completion_script)
                print_success(
                    f"✅ Installed {completions} completions to {install_path}"
                )

                if completions == "bash":
                    print_info("Add this to your ~/.bashrc:")
                    print_info(f"  source {install_path}")
                elif completions == "zsh":
                    print_info("Add this to your ~/.zshrc:")
                    print_info(f"  fpath=({install_path.parent} $fpath)")
                    print_info("  autoload -U compinit && compinit")
        else:
            # Just output the completion script
            click.echo(completion_script)
        return

    if init:
        # Set up wrknv's own workenv
        print_info("Setting up wrknv workenv...", Emoji.CONFIG)
        WorkenvManager.setup_workenv(force=force)
        return

    if shell_integration:
        # Look for script in the repository root
        script_path = (
            Path(__file__).parent.parent.parent.parent.parent
            / "scripts"
            / "shell-integration.sh"
        )
        if script_path.exists():
            print_info("Setting up shell integration...", Emoji.CONFIG)
            try:
                subprocess.run(["bash", str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print_error("Failed to set up shell integration")
                sys.exit(1)
        else:
            print_error(f"Shell integration script not found at {script_path}")
            sys.exit(1)
    else:
        print_info("Available setup options:")
        print_info("  --init                Create wrknv's own workenv")
        print_info("  --shell-integration   Set up shell aliases and shortcuts")
        print_info("  --check               Check system dependencies")
        print_info("  --completions SHELL   Generate shell completions (bash/zsh/fish)")