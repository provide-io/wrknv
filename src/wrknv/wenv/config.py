#
# wrknv/workenv/config.py
#
"""
wrknv Configuration Management
==============================
Flexible configuration system that supports multiple sources.
"""

import os
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

from pyvider.telemetry import logger

from .schema import (
    WorkenvConfig,
    load_config_from_dict,
    validate_config_dict,
)


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

    def get_env_config(self) -> dict[str, Any]:
        """Get env configuration section."""
        return {}


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
                    # If section exists, use it, otherwise use the whole file
                    if self.section in all_data:
                        self._data = all_data.get(self.section, {})
                    else:
                        # Use the whole file if section doesn't exist
                        self._data = all_data
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

    def __init__(self, file_path: pathlib.Path):
        self.file_path = file_path
        self._config: WorkenvConfig | None = None
        self._raw_data: dict[str, Any] = {}
        self._load()

    def _load(self):
        """Load and validate configuration from file."""
        if self.file_path and self.file_path.exists():
            try:
                with open(self.file_path, "rb") as f:
                    self._raw_data = tomllib.load(f)

                # Validate the configuration
                is_valid, errors = validate_config_dict(self._raw_data)
                if not is_valid:
                    error_msg = "\n".join(errors)
                    logger.error(f"Configuration validation failed: {error_msg}")
                    raise WorkenvConfigError(
                        f"Invalid configuration in {self.file_path}:\n{error_msg}"
                    )

                # Load into typed config
                self._config = load_config_from_dict(self._raw_data)
                logger.debug(f"Loaded and validated config from {self.file_path}")
            except WorkenvConfigError:
                raise
            except Exception as e:
                logger.warning(f"Failed to load {self.file_path}", error=str(e))
                self._config = None
                self._raw_data = {}

    def get_config(self) -> WorkenvConfig | None:
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
            return {
                name: config.version
                for name, config in self._config.tools.items()
                if config.enabled
            }
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

    def get_env_config(self) -> dict[str, Any]:
        """Get merged env configuration from all sources."""
        merged = {}
        # Start with lowest priority sources
        for source in reversed(self.sources):
            env_config = source.get_env_config()
            if env_config:
                merged.update(env_config)
        return merged

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

        # Build directory name: workenv/[profile_]wrknv_os_arch
        if profile == "default":
            return f"workenv/wrknv_{system}_{arch}"
        else:
            return f"workenv/{profile}_wrknv_{system}_{arch}"

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
        import tomli_w

        # Get the primary config file (wrknv.toml)
        config_file = Path.cwd() / "wrknv.toml"

        # Load existing config or create new one
        if config_file.exists():
            with open(config_file, "rb") as f:
                import tomllib

                config_data = tomllib.load(f)
        else:
            config_data = {"project_name": Path.cwd().name}

        # Ensure profiles section exists
        if "profiles" not in config_data:
            config_data["profiles"] = {}

        # Save the profile
        if tools is None:
            # Get current tool versions
            tools = self.get_all_tools()

        config_data["profiles"][profile_name] = tools

        # Write back to file
        with open(config_file, "w") as f:
            f.write(tomli_w.dumps(config_data))

    def list_profiles(self) -> list[str]:
        """List all available profile names."""
        profiles = self._config_data.get("workenv", {}).get("profiles", {})
        if not profiles:
            # Also check top-level profiles
            profiles = self._config_data.get("profiles", {})
        return list(profiles.keys()) if profiles else []

    def profile_exists(self, profile_name: str) -> bool:
        """Check if a profile exists."""
        profiles = self.list_profiles()
        return profile_name in profiles

    def delete_profile(self, profile_name: str) -> bool:
        """Delete a profile."""
        import tomli_w

        config_file = Path.cwd() / "wrknv.toml"
        if not config_file.exists():
            return False

        with open(config_file, "rb") as f:
            import tomllib

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
        from .schema import validate_config_dict

        return validate_config_dict(self._config_data)

    def set_setting(self, key: str, value: Any) -> bool:
        """Set a configuration setting."""
        import tomli_w

        config_file = self.get_config_path()

        # Load existing config or create new one
        if config_file.exists():
            with open(config_file, "rb") as f:
                import tomllib

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
        import subprocess

        config_file = Path.cwd() / "wrknv.toml"

        # Get editor from environment
        editor = os.environ.get("EDITOR", os.environ.get("VISUAL", ""))

        if not editor:
            raise RuntimeError(
                "No editor configured. Set EDITOR or VISUAL environment variable."
            )

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
        subprocess.run([editor, str(config_file)])

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


# 🧰🌍🖥️🪄
