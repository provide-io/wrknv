#
# wrkenv/workenv/config.py
#
"""
wrkenv Configuration Management
==============================
Flexible configuration system that supports multiple sources.
"""

import os
import pathlib
from typing import Any

try:
    import tomllib
except ImportError:
    import tomli as tomllib

try:
    import tomli_w
except ImportError:
    tomli_w = None

from pyvider.telemetry import logger


class WorkenvConfigError(Exception):
    """Raised when there's an error in workenv configuration."""

    pass


class ConfigSource:
    """Base class for configuration sources."""

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        return None

    def get_all_tools(self) -> dict[str, str]:
        """Get all tool versions."""
        return {}

    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        return {}

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        return default


class FileConfigSource(ConfigSource):
    """Configuration source from a TOML file."""

    def __init__(self, file_path: pathlib.Path, section: str = "workenv"):
        self.file_path = file_path
        self.section = section
        self._data = {}
        self._load()

    def _load(self):
        """Load configuration from file."""
        if self.file_path and self.file_path.exists():
            try:
                with open(self.file_path, "rb") as f:
                    all_data = tomllib.load(f)
                    self._data = all_data.get(self.section, {})
                logger.debug(
                    f"Loaded config from {self.file_path}", section=self.section
                )
            except Exception as e:
                logger.warning(f"Failed to load {self.file_path}", error=str(e))
                self._data = {}

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get("tools", {})
        return tools.get(tool_name)

    def get_all_tools(self) -> dict[str, str]:
        """Get all tool versions."""
        return self._data.get("tools", {})

    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        profiles = self._data.get("profiles", {})
        return profiles.get(profile_name, {})

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        settings = self._data.get("settings", {})
        return settings.get(key, default)


class EnvironmentConfigSource(ConfigSource):
    """Configuration source from environment variables."""

    def __init__(self, prefix: str = "WRKENV"):
        self.prefix = prefix

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        return os.environ.get(env_var)

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        env_var = f"{self.prefix}_{key.upper()}"
        value = os.environ.get(env_var)

        if value is None:
            return default

        # Try to parse as boolean
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False

        return value


class WorkenvConfig:
    """
    Flexible workenv configuration manager.

    Supports multiple configuration sources with priority ordering.
    Default priority (highest to lowest):
    1. Environment variables (WRKENV_*)
    2. wrkenv.toml [workenv] section
    3. Built-in defaults
    """

    def __init__(self, sources: list[ConfigSource] | None = None):
        """
        Initialize with configuration sources.

        If sources is None, uses default sources.
        """
        if sources is None:
            # Default configuration sources
            sources = []

            # Environment variables (highest priority)
            sources.append(EnvironmentConfigSource("WRKENV"))

            # Also support legacy TOFUSOUP_WORKENV_ prefix
            sources.append(EnvironmentConfigSource("TOFUSOUP_WORKENV"))

            # Look for wrkenv.toml first
            wrkenv_toml = self._find_config_file("wrkenv.toml")
            if wrkenv_toml:
                sources.append(FileConfigSource(wrkenv_toml, "workenv"))

            # Fall back to soup.toml for backward compatibility
            soup_toml = self._find_config_file("soup.toml")
            if soup_toml:
                sources.append(FileConfigSource(soup_toml, "workenv"))

        self.sources = sources
        self.config_path = self._get_config_path()
        self._config_data = self._get_merged_config_data()

    def _find_config_file(self, filename: str) -> pathlib.Path | None:
        """Find config file in current directory or parent directories."""
        current = pathlib.Path.cwd()

        while current != current.parent:
            config_file = current / filename
            if config_file.exists():
                return config_file
            current = current.parent

        return None

    def _get_config_path(self) -> pathlib.Path | None:
        """Get the primary config file path."""
        for source in self.sources:
            if isinstance(source, FileConfigSource):
                return source.file_path
        return None

    def _get_merged_config_data(self) -> dict[str, Any]:
        """Get merged configuration data from all file sources."""
        merged = {}
        for source in reversed(self.sources):  # Start with lowest priority
            if isinstance(source, FileConfigSource):
                # Get the raw data from the file source
                merged.update({"workenv": source._data})
        return merged

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get configured version for a tool."""
        for source in self.sources:
            version = source.get_tool_version(tool_name)
            if version is not None:
                logger.debug(
                    f"Found {tool_name} version from {source.__class__.__name__}",
                    version=version,
                )
                return version

        logger.debug(f"No version configured for {tool_name}")
        return None

    def get_all_tools(self) -> dict[str, str]:
        """Get all configured tools and their versions."""
        # Start with lowest priority and override with higher
        tools = {}
        for source in reversed(self.sources):
            tools.update(source.get_all_tools())

        return tools

    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        for source in self.sources:
            profile = source.get_profile(profile_name)
            if profile:
                return profile
        return {}

    def get_current_profile(self) -> str:
        """Get the current active profile name."""
        # Check for profile in sources
        for source in self.sources:
            profile = source.get_setting("current_profile")
            if profile:
                return profile
        return "default"

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        for source in self.sources:
            value = source.get_setting(key, None)
            if value is not None:
                return value
        return default

    def get_workenv_dir_name(self) -> str:
        """Get the workenv directory name based on current profile and platform."""
        import platform

        profile = self.get_current_profile()

        # Get platform info
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture names
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        # Build directory name: workenv/[profile_]wrkenv_os_arch
        if profile == "default":
            return f"workenv/wrkenv_{system}_{arch}"
        else:
            return f"workenv/{profile}_wrkenv_{system}_{arch}"

    def validate_version(self, tool_name: str, version: str) -> bool:
        """Validate that a version string is valid for a tool."""
        if not version:
            return False

        # Allow 'latest' as a special case
        if version == "latest":
            return True

        # Basic semantic version check
        import re

        pattern = r"^\d+\.\d+(\.\d+)?(-[\w\.-]+)?(\+[\w\.-]+)?$"
        return bool(re.match(pattern, version))

    def save_profile(
        self, profile_name: str, tools: dict[str, str] | None = None
    ) -> None:
        """Save a profile to the configuration file."""
        # This would need to determine which file to save to
        # For now, we'll raise NotImplementedError
        raise NotImplementedError("Profile saving not yet implemented")

    def list_profiles(self) -> list[str]:
        """List all available profile names."""
        profiles = self._config_data.get("workenv", {}).get("profiles", {})
        return list(profiles.keys()) if profiles else []

    def show_config(self) -> None:
        """Display current configuration to console."""
        # This is a placeholder for tests
        pass

    def edit_config(self) -> None:
        """Open configuration file for editing."""
        # This is a placeholder for tests
        pass


# Convenience function for TofuSoup integration
def create_soup_config() -> WorkenvConfig:
    """
    Create a WorkenvConfig that prioritizes soup.toml.

    This is for backward compatibility with TofuSoup.
    """
    sources = [
        EnvironmentConfigSource("TOFUSOUP_WORKENV"),
        EnvironmentConfigSource("WRKENV"),
    ]

    # Look for soup.toml first
    soup_toml = WorkenvConfig()._find_config_file("soup.toml")
    if soup_toml:
        sources.append(FileConfigSource(soup_toml, "workenv"))

    # Also check wrkenv.toml
    wrkenv_toml = WorkenvConfig()._find_config_file("wrkenv.toml")
    if wrkenv_toml:
        sources.append(FileConfigSource(wrkenv_toml, "workenv"))

    return WorkenvConfig(sources)


# 🧰🌍🖥️🪄
