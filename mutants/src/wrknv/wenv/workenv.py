#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Workenv Management
==================
Manages wrknv's own virtual environment."""

from __future__ import annotations

from pathlib import Path
import platform
import shutil
import sys

from provide.foundation.process import run

from wrknv.cli.visual import Emoji, print_info, print_success
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class WorkenvManager:
    """Manages wrknv's own workenv virtual environment."""

    @classmethod
    def get_workenv_name(cls) -> str:
        """Get the workenv name for current platform."""
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture names
        if machine in ("x86_64", "amd64"):
            machine = "amd64"
        elif machine in ("arm64", "aarch64"):
            machine = "arm64"
        # Note: system (darwin/linux/windows) already normalized by platform.system().lower()

        return f"wrknv_{system}_{machine}"

    @classmethod
    def get_workenv_path(cls, base_path: Path | None = None) -> Path:
        """Get the path to the workenv directory."""
        if base_path is None:
            base_path = Path.cwd()
        return base_path / "workenv" / cls.get_workenv_name()

    @classmethod
    def create_workenv(cls, base_path: Path | None = None, force: bool = False) -> Path:
        """Create a new workenv virtual environment."""
        workenv_path = cls.get_workenv_path(base_path)

        if workenv_path.exists() and not force:
            print_info(f"Workenv already exists at {workenv_path}", Emoji.SUCCESS)
            return workenv_path

        if workenv_path.exists() and force:
            print_info(f"Removing existing workenv at {workenv_path}", Emoji.CLEAN)
            shutil.rmtree(workenv_path)

        print_info(f"Creating workenv at {workenv_path}", Emoji.BUILD)
        workenv_path.parent.mkdir(parents=True, exist_ok=True)

        # Create virtual environment
        run(
            [sys.executable, "-m", "venv", str(workenv_path)],
            check=True,
        )

        # Install wrknv in development mode
        pip_path = cls._get_pip_path(workenv_path)
        wrknv_root = Path(__file__).parent.parent.parent.parent

        print_info("Installing wrknv in development mode...", Emoji.INSTALL)
        run(
            [str(pip_path), "install", "-e", str(wrknv_root)],
            check=True,
        )

        # Install development dependencies
        print_info("Installing development dependencies...", Emoji.PACKAGE)
        run(
            [str(pip_path), "install", "-e", f"{wrknv_root}[dev]"],
            check=True,
        )

        print_success(f"Workenv created successfully at {workenv_path}", Emoji.SUCCESS)
        return workenv_path

    @classmethod
    def _get_pip_path(cls, workenv_path: Path) -> Path:
        """Get the path to pip in the workenv."""
        if platform.system() == "Windows":
            return workenv_path / "Scripts" / "pip.exe"
        else:
            return workenv_path / "bin" / "pip"

    @classmethod
    def _get_python_path(cls, workenv_path: Path) -> Path:
        """Get the path to python in the workenv."""
        if platform.system() == "Windows":
            return workenv_path / "Scripts" / "python.exe"
        else:
            return workenv_path / "bin" / "python"

    @classmethod
    def generate_env_scripts(cls, base_path: Path | None = None) -> dict[str, Path]:
        """Generate env.sh and env.ps1 scripts for the workenv."""
        if base_path is None:
            base_path = Path.cwd()

        workenv_name = cls.get_workenv_name()

        # For now, skip the template generation due to Jinja2 issues
        # Just create simple activation scripts
        scripts = {}

        # Create simple env.sh if it doesn't exist
        env_sh_path = base_path / "env.sh"
        if not env_sh_path.exists():
            env_sh_content = f"""#!/usr/bin/env bash
# Generated by wrknv - Simple activation script

# Activate the workenv
source workenv/{workenv_name}/bin/activate

echo "   Python: $(which python)"
echo "   wrknv: $(which wrknv)"
"""
            env_sh_path.write_text(env_sh_content)
            env_sh_path.chmod(0o755)
        scripts["env.sh"] = env_sh_path

        # Create simple env.ps1
        env_ps1_path = base_path / "env.ps1"
        env_ps1_content = f"""# Generated by wrknv - Simple activation script

# Activate the workenv
& workenv\\{workenv_name}\\Scripts\\Activate.ps1

Write-Host "   Python: $(Get-Command python | Select-Object -ExpandProperty Source)"
Write-Host "   wrknv: $(Get-Command wrknv | Select-Object -ExpandProperty Source)"
"""
        env_ps1_path.write_text(env_ps1_content)
        scripts["env.ps1"] = env_ps1_path

        print_success("Generated activation scripts:", Emoji.SUCCESS)
        print_info(f"  • env.sh: {env_sh_path}", Emoji.CONFIG)
        print_info(f"  • env.ps1: {env_ps1_path}", Emoji.CONFIG)

        return scripts

    @classmethod
    def setup_workenv(cls, base_path: Path | None = None, force: bool = False) -> None:
        """Complete workenv setup including creation and scripts."""
        # Create workenv
        cls.create_workenv(base_path, force)

        # Generate activation scripts
        cls.generate_env_scripts(base_path)

        # Print usage instructions
        print_info("\nTo activate the workenv:", Emoji.INFO)
        if platform.system() == "Windows":
            print_info("  PowerShell: .\\env.ps1", Emoji.CONFIG)
        else:
            print_info("  Bash/Zsh: source ./env.sh", Emoji.CONFIG)


# 🧰🌍🔚
