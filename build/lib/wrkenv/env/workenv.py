#
# wrkenv/env/workenv.py
#
"""
Workenv Management
==================
Manages wrkenv's own virtual environment.
"""

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from pyvider.telemetry import logger

from wrkenv.env.visual import Emoji, print_error, print_info, print_success


class WorkenvManager:
    """Manages wrkenv's own workenv virtual environment."""

    @classmethod
    def get_workenv_name(cls) -> str:
        """Get the workenv name for current platform."""
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize platform names
        if system == "darwin":
            system = "darwin"
        elif system == "linux":
            system = "linux"
        elif system == "windows":
            system = "windows"
        else:
            system = system

        # Normalize architecture
        if machine in ("x86_64", "amd64"):
            machine = "amd64"
        elif machine in ("arm64", "aarch64"):
            machine = "arm64"
        else:
            machine = machine

        return f"wrkenv_{system}_{machine}"

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
        subprocess.run(
            [sys.executable, "-m", "venv", str(workenv_path)],
            check=True,
        )

        # Install wrkenv in development mode
        pip_path = cls._get_pip_path(workenv_path)
        wrkenv_root = Path(__file__).parent.parent.parent.parent

        print_info("Installing wrkenv in development mode...", Emoji.INSTALL)
        subprocess.run(
            [str(pip_path), "install", "-e", str(wrkenv_root)],
            check=True,
        )

        # Install development dependencies
        print_info("Installing development dependencies...", Emoji.PACKAGE)
        subprocess.run(
            [str(pip_path), "install", "-e", f"{wrkenv_root}[dev]"],
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
        
        # Use the env generator with wrkenv-specific config
        from wrkenv.env.env_generator import create_project_env_scripts
        
        sh_path, ps1_path = create_project_env_scripts(base_path, workenv_name)
        
        return {"env.sh": sh_path, "env.ps1": ps1_path}

    @classmethod
    def setup_workenv(cls, base_path: Path | None = None, force: bool = False) -> None:
        """Complete workenv setup including creation and scripts."""
        # Create workenv
        workenv_path = cls.create_workenv(base_path, force)

        # Generate activation scripts
        cls.generate_env_scripts(base_path)

        # Print usage instructions
        print_info("\nTo activate the workenv:", Emoji.INFO)
        if platform.system() == "Windows":
            print_info("  PowerShell: .\\env.ps1", Emoji.CONFIG)
        else:
            print_info("  Bash/Zsh: source ./env.sh", Emoji.CONFIG)


# 🧰🌍🖥️🪄