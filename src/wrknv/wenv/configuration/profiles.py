"""
Profile Management for wenv
============================
Management of configuration profiles.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import tomllib
except ImportError:
    import tomli as tomllib

try:
    import tomli_w
except ImportError:
    tomli_w = None


class WorkenvProfileManager:
    """Manages configuration profiles for workenv."""

    def __init__(self, config) -> None:
        """Initialize profile manager with config instance."""
        self.config = config

    def get_current_profile(self) -> str:
        """Get the current active profile name."""
        # Check for profile in sources
        for source in self.config.sources:
            profile = source.get_setting("current_profile")
            if profile:
                return profile
        return "default"

    def save_profile(self, profile_name: str, tools: dict[str, str] | None = None) -> None:
        """Save a profile to the configuration file."""
        if tomli_w is None:
            raise ImportError("tomli-w is required to save profiles")

        # Get the primary config file (wrknv.toml)
        config_file = Path.cwd() / "wrknv.toml"

        # Load existing config or create new one
        if config_file.exists():
            with open(config_file, "rb") as f:
                config_data = tomllib.load(f)
        else:
            config_data = {"project_name": Path.cwd().name}

        # Ensure profiles section exists
        if "profiles" not in config_data:
            config_data["profiles"] = {}

        # Save the profile
        if tools is None:
            # Get current tool versions
            tools = self.config.get_all_tools()

        config_data["profiles"][profile_name] = tools

        # Write back to file
        with open(config_file, "w") as f:
            f.write(tomli_w.dumps(config_data))

    def list_profiles(self) -> list[str]:
        """List all available profile names."""
        profiles = self.config._config_data.get("workenv", {}).get("profiles", {})
        if not profiles:
            # Also check top-level profiles
            profiles = self.config._config_data.get("profiles", {})
        return list(profiles.keys()) if profiles else []

    def profile_exists(self, profile_name: str) -> bool:
        """Check if a profile exists."""
        profiles = self.list_profiles()
        return profile_name in profiles

    def delete_profile(self, profile_name: str) -> bool:
        """Delete a profile."""
        if tomli_w is None:
            raise ImportError("tomli-w is required to delete profiles")

        config_file = Path.cwd() / "wrknv.toml"
        if not config_file.exists():
            return False

        with open(config_file, "rb") as f:
            config_data = tomllib.load(f)

        # Check both locations for profiles
        deleted = False
        if "profiles" in config_data and profile_name in config_data["profiles"]:
            del config_data["profiles"][profile_name]
            deleted = True
        elif "workenv" in config_data and "profiles" in config_data["workenv"]:
            if profile_name in config_data["workenv"]["profiles"]:
                del config_data["workenv"]["profiles"][profile_name]
                deleted = True

        if deleted:
            with open(config_file, "w") as f:
                f.write(tomli_w.dumps(config_data))

        return deleted

    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        for source in self.config.sources:
            profile = source.get_profile(profile_name)
            if profile:
                return profile
        return {}

    def get_workenv_dir_name(self) -> str:
        """Get the workenv directory name based on current profile and platform."""
        import platform

        profile = self.get_current_profile()

        # Get system info
        system = platform.system().lower()
        if system == "darwin":
            system = "darwin"
        elif system == "linux":
            system = "linux"
        elif system == "windows":
            system = "win32"

        arch = platform.machine().lower()
        if arch in ("x86_64", "amd64"):
            arch = "amd64"
        elif arch in ("aarch64", "arm64"):
            arch = "arm64"

        # Build directory name: workenv/[profile_]wrknv_os_arch
        if profile == "default":
            return f"workenv/wrknv_{system}_{arch}"
        else:
            return f"workenv/{profile}_wrknv_{system}_{arch}"
