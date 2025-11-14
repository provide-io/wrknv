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

from provide.foundation.hub import register_command
from provide.foundation.cli import echo_error, echo_info, echo_success
from provide.foundation.logger import get_logger

from wrknv.wenv.exceptions import DependencyError
from wrknv.wenv.workenv import WorkenvManager

log = get_logger(__name__)


@register_command(
    "setup",
    description="Set up wrknv environment and integrations",
    category="core",
)
def setup_command(
    shell_integration: bool = False,
    init: bool = False,
    force: bool = False,
    check: bool = False,
    completions: str | None = None,
    install: bool = False,
):
    """Set up wrknv environment and integrations.
    
    Args:
        shell_integration: Set up shell aliases
        init: Initialize wrknv's own workenv
        force: Force recreate workenv
        check: Check system dependencies
        completions: Generate shell completions (bash/zsh/fish)
        install: Install completions (use with --completions)
    """
    if check:
        # Check system dependencies
        echo_info("Checking system dependencies...")

        required_deps = ["git", "curl", "python3"]
        optional_deps = ["docker", "wget"]
        missing_required = []
        missing_optional = []

        for dep in required_deps:
            if shutil.which(dep):
                echo_success(f"  ✓ {dep}")
            else:
                echo_error(f"  ✗ {dep} (required)")
                missing_required.append(dep)

        for dep in optional_deps:
            if shutil.which(dep):
                echo_info(f"  ✓ {dep} (optional)")
            else:
                echo_info(f"  ✗ {dep} (optional)")
                missing_optional.append(dep)

        if missing_required:
            raise DependencyError(missing_required, "wrknv core functionality")
        else:
            echo_success("All required dependencies are installed!")
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
                echo_success(f"✅ Installed {completions} completions to {install_path}")

                if completions == "bash":
                    echo_info("Add this to your ~/.bashrc:")
                    echo_info(f"  source {install_path}")
                elif completions == "zsh":
                    echo_info("Add this to your ~/.zshrc:")
                    echo_info(f"  fpath=({install_path.parent} $fpath)")
                    echo_info("  autoload -U compinit && compinit")
        else:
            # Just output the completion script
            print(completion_script)
        return

    if init:
        # Set up wrknv's own workenv
        echo_info("Setting up wrknv workenv...")
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
            echo_info("Setting up shell integration...")
            try:
                subprocess.run(["bash", str(script_path)], check=True)
            except subprocess.CalledProcessError:
                echo_error("Failed to set up shell integration")
                sys.exit(1)
        else:
            echo_error(f"Shell integration script not found at {script_path}")
            sys.exit(1)
    else:
        echo_info("Available setup options:")
        echo_info("  --init                Create wrknv's own workenv")
        echo_info("  --shell-integration   Set up shell aliases and shortcuts")
        echo_info("  --check               Check system dependencies")
        echo_info("  --completions SHELL   Generate shell completions (bash/zsh/fish)")