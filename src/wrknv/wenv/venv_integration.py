#
# wrknv/managers/tf/venv.py
#
"""
Tf Venv Integration
===================
Virtual environment integration utilities for Terraform/OpenTofu managers.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import sys

from provide.foundation import logger


def get_venv_bin_dir(config) -> pathlib.Path:
    """Get the bin directory for venv binaries."""
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv
        # Check if this is a wrknv (has 'workenv' in the path)
        if "workenv" in str(venv_path):
            # Use the workenv structure
            if os.name == "nt":  # Windows
                bin_dir = venv_path / "Scripts"
            else:  # Unix/Linux/macOS
                bin_dir = venv_path / "bin"
        else:
            # Regular venv
            if os.name == "nt":  # Windows
                bin_dir = venv_path / "Scripts"
            else:  # Unix/Linux/macOS
                bin_dir = venv_path / "bin"
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = config.get_workenv_dir_name()
            bin_dir = project_root / workenv_dir_name / "bin"
            if bin_dir.exists():
                return bin_dir

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def find_project_root() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent

    return None


def copy_active_binaries_to_venv(venv_bin_dir: pathlib.Path, config) -> None:
    """Copy all active tf binaries to venv bin directory."""
    if not venv_bin_dir:
        logger.warning("No venv bin directory available for tf binary copying")
        return

    # Get active versions for both tools
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                if source_path.exists():
                    # IBM Terraform is copied as 'ibmtf', OpenTofu stays as 'tofu'
                    target_name = temp_manager.executable_name

                    if os.name == "nt":  # Windows
                        target_name += ".exe"

                    target_path = venv_bin_dir / target_name

                    # Copy the binary
                    shutil.copy2(source_path, target_path)

                    # Make executable on Unix systems
                    if os.name != "nt":
                        target_path.chmod(0o755)

                    logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")
