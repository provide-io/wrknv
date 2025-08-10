#
# wrkenv/env/package/manager.py
#
"""
Package Manager for wrkenv
==========================
Manages package building, signing, and distribution.
"""

import importlib.util
import os
from pathlib import Path

from pyvider.telemetry import logger

from wrkenv.env.config import WorkenvConfig
from wrkenv.env.managers.factory import get_tool_manager


class PackageManager:
    """Manages package operations and tool integration."""

    def __init__(self, config: WorkenvConfig):
        """Initialize package manager with configuration."""
        self.config = config
        self._flavor_available = None

    def is_flavor_available(self) -> bool:
        """Check if flavor package is available."""
        if self._flavor_available is None:
            spec = importlib.util.find_spec("flavor")
            self._flavor_available = spec is not None
        return self._flavor_available

    def check_required_tools(self) -> dict[str, str]:
        """Check for required tools and their versions."""
        required_tools = {
            "go": self.config.get_tool_version("go") or "1.21.5",
            "uv": self.config.get_tool_version("uv") or "0.4.15",
            "python": "3.13.0",  # Minimum Python version
        }

        available = {}
        for tool, _required_version in required_tools.items():
            if tool == "python":
                # Check Python version
                try:
                    import sys

                    current = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
                    available[tool] = current
                except Exception:
                    available[tool] = None
            else:
                # Check via tool managers
                manager = get_tool_manager(tool, self.config)
                if manager:
                    try:
                        version = manager.get_installed_version()
                        available[tool] = version
                    except Exception:
                        available[tool] = None

        return available

    def get_required_tools(self) -> dict[str, str]:
        """Get required tool versions for package building."""
        return self.check_required_tools()

    def setup_build_environment(self) -> dict[str, str]:
        """Set up environment variables for building."""
        env = os.environ.copy()

        # Add tool paths
        workenv_dir = Path.home() / ".wrkenv"

        # Go environment
        go_path = workenv_dir / "tools" / "go"
        if go_path.exists():
            env["GOPATH"] = str(workenv_dir / "go")
            env["PATH"] = f"{go_path / 'bin'}:{env.get('PATH', '')}"

        # UV cache
        env["UV_CACHE_DIR"] = str(workenv_dir / "cache" / "uv")

        # Package-specific settings from config
        package_config = self.config.get_setting("package", {})
        if package_config.get("signing_curve"):
            env["FLAVOR_SIGNING_CURVE"] = package_config["signing_curve"]

        return env

    def get_build_environment(self) -> dict[str, str]:
        """Get the build environment variables."""
        return self.setup_build_environment()

    def install_missing_tools(self, tools: dict[str, str | None]) -> bool:
        """Install any missing required tools."""
        success = True

        for tool, current_version in tools.items():
            if current_version is None or tool == "python":
                # Skip Python - must be installed separately
                if tool == "python":
                    logger.warning("Python version requirement not met")
                    continue

                # Try to install the tool
                required_version = self.get_required_tools().get(tool)
                if required_version:
                    manager = get_tool_manager(tool, self.config)
                    if manager:
                        try:
                            logger.info(f"Installing {tool} {required_version}")
                            manager.install_version(required_version)
                        except Exception as e:
                            logger.error(f"Failed to install {tool}: {e}")
                            success = False

        return success

    def get_package_cache_dir(self) -> Path:
        """Get the package cache directory."""
        cache_dir = Path.home() / ".wrkenv" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def get_package_output_dir(self) -> Path:
        """Get the default package output directory."""
        package_config = self.config.get_setting("package", {})
        out_dir = package_config.get("default_out_dir", "dist")

        # If relative path, make it relative to current directory
        path = Path(out_dir)
        if not path.is_absolute():
            path = Path.cwd() / path

        path.mkdir(parents=True, exist_ok=True)
        return path


# 🧰🌍🖥️🪄
