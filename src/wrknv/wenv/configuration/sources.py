"""
Configuration Sources for wenv
===============================
Different sources for loading workenv configuration.
"""

from __future__ import annotations

import os
import pathlib
from typing import Any

try:
    import tomllib
except ImportError:
    import tomli as tomllib

from provide.foundation import logger

from wrknv.wenv.exceptions import ConfigurationError


class WorkenvConfigError(ConfigurationError):
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

    def get_env_config(self) -> dict[str, Any]:
        """Get env configuration section."""
        return {}


class FileConfigSource(ConfigSource):
    """Configuration source from a TOML file."""

    def __init__(self, file_path: pathlib.Path, section: str = "workenv") -> None:
        self.file_path = file_path
        self.section = section
        self._data = {}
        self._load()

    def _load(self) -> None:
        """Load configuration from file."""
        if self.file_path and self.file_path.exists():
            try:
                with open(self.file_path, "rb") as f:
                    all_data = tomllib.load(f)
                    # If section exists, use it, otherwise use the whole file
                    if self.section in all_data:
                        self._data = all_data.get(self.section, {})
                    else:
                        # Use the whole file if section doesn't exist
                        self._data = all_data
                logger.debug(f"Loaded config from {self.file_path}", section=self.section)
            except Exception as e:
                logger.warning(f"Failed to load {self.file_path}", error=str(e))
                self._data = {}

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get("tools", {})
        return tools.get(tool_name)

    def get_all_tools(self) -> dict[str, str]:
        """Get all tool versions."""
        tools_data = self._data.get("tools", {})
        # Extract versions from tool configs
        result = {}
        for tool_name, tool_config in tools_data.items():
            if isinstance(tool_config, dict):
                result[tool_name] = tool_config.get("version", "")
            else:
                result[tool_name] = tool_config
        return result

    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        # Try to get from the section data first
        profiles = self._data.get("profiles", {})
        if profile_name in profiles:
            return profiles[profile_name]

        # If not found, try to load from the top-level profiles
        if self.file_path and self.file_path.exists():
            try:
                with open(self.file_path, "rb") as f:
                    import tomllib

                    all_data = tomllib.load(f)
                    top_profiles = all_data.get("profiles", {})
                    return top_profiles.get(profile_name, {})
            except Exception:
                pass

        return {}

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        settings = self._data.get("settings", {})
        return settings.get(key, default)

    def get_env_config(self) -> dict[str, Any]:
        """Get env configuration section."""
        return self._data.get("env", {})


class ValidatedTomlSource(ConfigSource):
    """Configuration source from a TOML file with schema validation."""

    def __init__(self, file_path: pathlib.Path) -> None:
        self.file_path = file_path
        self._config = None  # Will be WorkenvConfig when imported
        self._raw_data: dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        """Load and validate configuration from file."""
        if self.file_path and self.file_path.exists():
            try:
                with open(self.file_path, "rb") as f:
                    self._raw_data = tomllib.load(f)

                # Import here to avoid circular imports
                from wrknv.wenv.schema import load_config_from_dict, validate_config_dict

                # Validate the configuration
                is_valid, errors = validate_config_dict(self._raw_data)
                if not is_valid:
                    error_msg = "\n".join(errors)
                    logger.error(f"Configuration validation failed: {error_msg}")
                    raise WorkenvConfigError(f"Invalid configuration in {self.file_path}:\n{error_msg}")

                # Load into typed config
                self._config = load_config_from_dict(self._raw_data)
                logger.debug(f"Loaded and validated config from {self.file_path}")
            except WorkenvConfigError:
                raise
            except Exception as e:
                logger.warning(f"Failed to load {self.file_path}", error=str(e))
                self._config = None
                self._raw_data = {}

    def get_config(self):
        """Get the validated configuration object."""
        return self._config

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        if self._config:
            tool_config = self._config.get_tool_config(tool_name)
            return tool_config.version if tool_config else None
        return None

    def get_all_tools(self) -> dict[str, str]:
        """Get all tool versions."""
        if self._config:
            return {name: config.version for name, config in self._config.tools.items() if config.enabled}
        return {}

    def get_profile(self, profile_name: str) -> dict[str, Any]:
        """Get a configuration profile."""
        if self._config:
            profile = self._config.get_profile(profile_name)
            if profile:
                return profile.model_dump()
        return {}

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        if self._config:
            return getattr(self._config, key, default)
        return default

    def get_env_config(self) -> dict[str, Any]:
        """Get env configuration section."""
        if self._config:
            return self._config.environment
        return {}


class EnvironmentConfigSource(ConfigSource):
    """Configuration source from environment variables."""

    def __init__(self, prefix: str = "WRKENV") -> None:
        self.prefix = prefix

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        return os.environ.get(env_var)

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        from provide.foundation.utils.parsing import parse_bool

        env_var = f"{self.prefix}_{key.upper()}"
        value = os.environ.get(env_var)

        if value is None:
            return default

        # Try to parse as boolean
        try:
            return parse_bool(value)
        except ValueError:
            # Not a boolean, return as string
            return value
