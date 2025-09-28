"""
Main Configuration Manager for wenv
====================================
Core WorkenvConfig class with delegation to other modules.
"""
from __future__ import annotations

import pathlib
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

from provide.foundation import logger

from .sources import ConfigSource, EnvironmentConfigSource, FileConfigSource
from .profiles import WorkenvProfileManager


class WorkenvConfig:
    """
    Flexible workenv configuration manager.

    Supports multiple configuration sources with priority ordering.
    Default priority (highest to lowest):
    1. Environment variables (WRKENV_*)
    2. wrknv.toml [workenv] section
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

            # Look for wrknv.toml
            wrknv_toml = self._find_config_file("wrknv.toml")
            if wrknv_toml:
                sources.append(FileConfigSource(wrknv_toml, "workenv"))

        self.sources = sources
        self.config_path = self._get_config_path()
        self._config_data = self._get_merged_config_data()

        # Initialize profile manager
        self._profile_manager = WorkenvProfileManager(self)

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
                merged.update(source._data)
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

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        for source in self.sources:
            value = source.get_setting(key, None)
            if value is not None:
                return value
        return default

    def get_env_config(self) -> dict[str, Any]:
        """Get merged env configuration from all sources."""
        merged = {}
        # Start with lowest priority sources
        for source in reversed(self.sources):
            env_config = source.get_env_config()
            if env_config:
                merged.update(env_config)
        return merged

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

    def get_config_path(self) -> Path:
        """Get the path to the configuration file."""
        return Path.cwd() / "wrknv.toml"

    def config_exists(self) -> bool:
        """Check if configuration file exists."""
        return self.get_config_path().exists()

    def get_raw_config(self) -> str:
        """Get raw configuration file content."""
        config_file = self.get_config_path()
        if config_file.exists():
            return config_file.read_text()
        return ""

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return self._config_data.copy()

    def validate(self) -> tuple[bool, list[str]]:
        """Validate the configuration."""
        # Import here to avoid circular imports
        from wrknv.wenv.schema import validate_config_dict

        return validate_config_dict(self._config_data)

    def set_setting(self, key: str, value: Any) -> bool:
        """Set a configuration setting."""
        if tomli_w is None:
            raise ImportError("tomli-w is required to set settings")

        config_file = self.get_config_path()

        # Load existing config or create new one
        if config_file.exists():
            with open(config_file, "rb") as f:
                config_data = tomllib.load(f)
        else:
            config_data = {"project_name": Path.cwd().name}

        # Set the value (supports nested keys with dots)
        keys = key.split(".")
        current = config_data
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value

        # Write back to file
        with open(config_file, "w") as f:
            f.write(tomli_w.dumps(config_data))

        return True

    def show_config(self) -> None:
        """Display current configuration to console."""
        from rich.console import Console
        from rich.syntax import Syntax

        console = Console()
        config_file = Path.cwd() / "wrknv.toml"

        if config_file.exists():
            content = config_file.read_text()
            syntax = Syntax(content, "toml", theme="monokai", line_numbers=True)
            console.print(syntax)
        else:
            console.print("[yellow]No configuration file found[/yellow]")

    def edit_config(self) -> None:
        """Open configuration file for editing."""
        import os

        from provide.foundation.process import run_command

        config_file = Path.cwd() / "wrknv.toml"

        # Get editor from environment
        editor = os.environ.get("EDITOR", os.environ.get("VISUAL", ""))

        if not editor:
            raise RuntimeError("No editor configured. Set EDITOR or VISUAL environment variable.")

        # Create file if it doesn't exist
        if not config_file.exists():
            # Create a basic template
            template = f"""# wrknv configuration file
project_name = "{Path.cwd().name}"
version = "1.0.0"
log_level = "INFO"

[tools]
# terraform = {{ version = "1.5.0" }}
# go = {{ version = "1.21.0" }}
# uv = {{ version = "0.4.0" }}

[container]
enabled = false
base_image = "ubuntu:22.04"
python_version = "3.11"
"""
            config_file.write_text(template)

        # Open in editor
        run_command([editor, str(config_file)])

    def get_command_option(self, command: str, option: str, default: Any = None) -> Any:
        """Get a command-specific option from configuration.

        Args:
            command: The command path (e.g., "workenv.terraform")
            option: The option name (e.g., "create_symlinks")
            default: Default value if not found

        Returns:
            The option value or default
        """
        # For now, return the default value
        # In the future, this could look up command-specific settings
        return default

    # Delegation methods to profile manager
    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        return self._profile_manager.get_profile(profile_name)

    def get_current_profile(self) -> str:
        """Get the current active profile name."""
        return self._profile_manager.get_current_profile()

    def get_workenv_dir_name(self) -> str:
        """Get the workenv directory name based on current profile and platform."""
        return self._profile_manager.get_workenv_dir_name()

    def save_profile(self, profile_name: str, tools: dict[str, str] | None = None) -> None:
        """Save a profile to the configuration file."""
        self._profile_manager.save_profile(profile_name, tools)

    def list_profiles(self) -> list[str]:
        """List all available profile names."""
        return self._profile_manager.list_profiles()

    def profile_exists(self, profile_name: str) -> bool:
        """Check if a profile exists."""
        return self._profile_manager.profile_exists(profile_name)

    def delete_profile(self, profile_name: str) -> bool:
        """Delete a profile."""
        return self._profile_manager.delete_profile(profile_name)