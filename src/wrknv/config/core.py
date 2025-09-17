"""
Core Configuration for wrknv
=============================
Main configuration classes using provide.foundation.
"""

import os
from pathlib import Path
from typing import Any

from attrs import define, field
from provide.foundation.config import (
    SyncConfigManager,
    field as config_field,
)
from provide.foundation.config.env import RuntimeConfig
from provide.foundation.logger import get_logger
from provide.foundation.process import run_command

logger = get_logger(__name__)


class WorkenvConfigError(Exception):
    """Raised when there's an error in workenv configuration."""

    pass


@define
class WorkenvToolConfig:
    """Configuration for a single tool."""

    version: str | None = None
    path: str | None = None
    env: dict[str, str] = field(factory=dict)


@define
class WorkenvSettings(RuntimeConfig):
    """Workenv-specific settings with WRKNV_ environment variable support."""

    auto_install: bool = config_field(
        default=True, description="Automatically install missing tools", env_var="WRKNV_AUTO_INSTALL"
    )
    use_cache: bool = config_field(
        default=True, description="Use cached tool installations", env_var="WRKNV_USE_CACHE"
    )
    cache_ttl: str = config_field(default="7d", description="Cache time-to-live", env_var="WRKNV_CACHE_TTL")
    log_level: str = config_field(default="WARNING", description="Logging level", env_var="WRKNV_LOG_LEVEL")
    container_runtime: str = config_field(
        default="docker", description="Container runtime to use", env_var="WRKNV_CONTAINER_RUNTIME"
    )
    container_registry: str = config_field(
        default="ghcr.io", description="Default container registry", env_var="WRKNV_CONTAINER_REGISTRY"
    )


@define
class WorkenvConfig(RuntimeConfig):
    """Main workenv configuration with WRKNV_ environment variable support."""

    # Project metadata
    project_name: str = config_field(
        default="my-project", description="Project name", env_var="WRKNV_PROJECT_NAME"
    )
    version: str = config_field(default="1.0.0", description="Project version", env_var="WRKNV_VERSION")

    # Tool configurations
    tools: dict[str, dict[str, Any]] = field(factory=dict)

    # Profiles
    profiles: dict[str, dict[str, str]] = field(factory=dict)

    # Settings
    workenv: WorkenvSettings = field(factory=WorkenvSettings)

    # Env configuration
    env: dict[str, Any] = field(factory=dict)

    # Internal state
    config_path: Path | None = field(init=False, repr=False, default=None)
    _manager: SyncConfigManager | None = field(init=False, repr=False, default=None)

    @classmethod
    def load(cls, config_file: Path | None = None) -> "WorkenvConfig":
        """Load configuration from file and environment variables."""
        instance = cls()
        instance.config_path = config_file or instance._find_config_file()
        instance._manager = instance._create_manager()
        instance._load_config()

        # Also load from environment variables with WRKNV_ prefix
        env_config = cls.from_env(prefix="WRKNV")

        # Merge environment config over file config
        if env_config.project_name != "my-project":
            instance.project_name = env_config.project_name
        if env_config.version != "1.0.0":
            instance.version = env_config.version

        # Merge workenv settings from environment
        env_settings = WorkenvSettings.from_env(prefix="WRKNV")
        if env_settings.log_level != "WARNING":
            instance.workenv.log_level = env_settings.log_level
        if env_settings.auto_install != True:
            instance.workenv.auto_install = env_settings.auto_install
        if env_settings.use_cache != True:
            instance.workenv.use_cache = env_settings.use_cache
        if env_settings.cache_ttl != "7d":
            instance.workenv.cache_ttl = env_settings.cache_ttl
        if env_settings.container_runtime != "docker":
            instance.workenv.container_runtime = env_settings.container_runtime
        if env_settings.container_registry != "ghcr.io":
            instance.workenv.container_registry = env_settings.container_registry

        return instance

    def _find_config_file(self) -> Path:
        """Find configuration file in standard locations."""
        # Check standard locations
        locations = [
            Path.cwd() / ".wrknv.toml",
            Path.cwd() / "wrknv.toml",
            Path.cwd() / "pyproject.toml",
            Path.home() / ".config" / "wrknv" / "config.toml",
            Path.home() / ".wrknv.toml",
        ]

        for path in locations:
            if path.exists():
                logger.debug(f"Found config file at {path}")
                return path

        # Return default location for new configs
        return Path.cwd() / ".wrknv.toml"

    def _create_manager(self) -> SyncConfigManager:
        """Create configuration manager."""
        # For now, just create a basic manager
        # We'll load files manually to avoid complexity
        return SyncConfigManager()

    def _load_config(self):
        """Load configuration from file."""
        if self.config_path and self.config_path.exists():
            try:
                # Load TOML directly - simple and reliable
                try:
                    import tomli
                except ImportError:
                    import tomllib as tomli

                with open(self.config_path, "rb") as f:
                    config_dict = tomli.load(f)

                # Update attributes from loaded config
                if "project_name" in config_dict:
                    self.project_name = config_dict["project_name"]
                if "version" in config_dict:
                    self.version = config_dict["version"]
                if "tools" in config_dict:
                    self.tools = config_dict["tools"]
                if "profiles" in config_dict:
                    self.profiles = config_dict["profiles"]
                if "workenv" in config_dict and isinstance(config_dict["workenv"], dict):
                    for key, value in config_dict["workenv"].items():
                        if hasattr(self.workenv, key):
                            setattr(self.workenv, key, value)
                if "env" in config_dict:
                    self.env = config_dict["env"]

            except Exception as e:
                logger.warning(f"Failed to load config from {self.config_path}: {e}")

    def config_exists(self) -> bool:
        """Check if configuration file exists."""
        return self.config_path.exists() if self.config_path else False

    def get_config_path(self) -> Path:
        """Get path to configuration file."""
        return self.config_path

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tool_config = self.tools.get(tool_name, {})
        if isinstance(tool_config, dict):
            return tool_config.get("version")
        return tool_config if isinstance(tool_config, str) else None

    def get_all_tools(self) -> dict[str, str | list[str]]:
        """Get all tool versions."""
        result = {}
        for tool_name, config in self.tools.items():
            if isinstance(config, dict):
                version = config.get("version")
            else:
                version = config
            if version:
                result[tool_name] = version
        return result

    def get_profile(self, profile_name: str) -> dict[str, str] | None:
        """Get a configuration profile."""
        return self.profiles.get(profile_name)

    def list_profiles(self) -> list[str]:
        """List all available profiles."""
        return list(self.profiles.keys())

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting using dot notation."""
        parts = key.split(".")
        current = self

        for part in parts:
            if hasattr(current, part):
                current = getattr(current, part)
            elif isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default

        return current

    def get_env_config(self) -> dict[str, Any]:
        """Get environment configuration for env generation."""
        return self.env

    def set_setting(self, key: str, value: Any):
        """Set a configuration setting using dot notation."""
        parts = key.split(".")

        # Navigate to the parent
        current = self
        for part in parts[:-1]:
            if hasattr(current, part):
                current = getattr(current, part)
            elif isinstance(current, dict):
                if part not in current:
                    current[part] = {}
                current = current[part]
            else:
                raise WorkenvConfigError(f"Cannot set {key}: parent doesn't exist")

        # Set the value
        last_part = parts[-1]
        if hasattr(current, last_part):
            setattr(current, last_part, value)
        elif isinstance(current, dict):
            current[last_part] = value
        else:
            raise WorkenvConfigError(f"Cannot set {key}: invalid target")

        # Save to file
        self.save_config()

    def save_config(self):
        """Save configuration to file."""
        try:
            import tomli_w
        except ImportError:
            raise WorkenvConfigError("tomli-w is required to save TOML files")

        # Convert to dict
        config_dict = self.to_dict()

        # Write to file
        with open(self.config_path, "wb") as f:
            tomli_w.dump(config_dict, f)

        logger.info(f"Saved configuration to {self.config_path}")

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "project_name": self.project_name,
            "version": self.version,
            "tools": self.tools,
            "profiles": self.profiles,
            "workenv": {
                "auto_install": self.workenv.auto_install,
                "use_cache": self.workenv.use_cache,
                "cache_ttl": self.workenv.cache_ttl,
                "log_level": self.workenv.log_level,
                "container_runtime": self.workenv.container_runtime,
                "container_registry": self.workenv.container_registry,
            },
            "env": self.env,
        }

    def show_config(self):
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config_path}")
        echo_info(f"  Project: {self.project_name} v{self.version}")

        if self.tools:
            echo_info("\n  Tools:")
            for tool, config in self.tools.items():
                if isinstance(config, dict):
                    version = config.get("version", "latest")
                else:
                    version = config
                echo_info(f"    {tool}: {version}")

        if self.profiles:
            echo_info("\n  Profiles:")
            for profile in self.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.workenv.auto_install}")
        echo_info(f"    use_cache: {self.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.workenv.log_level}")

    def validate(self) -> tuple[bool, list[str]]:
        """Validate configuration comprehensively."""
        errors = []

        # Check required fields
        if not self.project_name:
            errors.append("Missing required field: project_name")
        elif not isinstance(self.project_name, str):
            errors.append("project_name must be a string")
        elif not self.project_name.strip():
            errors.append("project_name cannot be empty")

        if not self.version:
            errors.append("Missing required field: version")
        elif not isinstance(self.version, str):
            errors.append("version must be a string")
        elif not self._is_valid_version(self.version):
            errors.append(f"Invalid version format: {self.version}")

        # Validate project name format
        if self.project_name and isinstance(self.project_name, str):
            if not self._is_valid_project_name(self.project_name):
                errors.append(f"Invalid project name '{self.project_name}': must contain only letters, numbers, hyphens, and underscores")

        # Validate tools configuration
        if not isinstance(self.tools, dict):
            errors.append("tools must be a dictionary")
        else:
            for tool_name, tool_config in self.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles configuration
        if not isinstance(self.profiles, dict):
            errors.append("profiles must be a dictionary")
        else:
            for profile_name, profile_config in self.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate environment configuration
        if not isinstance(self.env, dict):
            errors.append("env must be a dictionary")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def _is_valid_version(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                else:  # Patch and build can be numeric or alphanumeric
                    if not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                        return False
            return True
        except ValueError:
            return False

    def _is_valid_project_name(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re
        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r'^[a-zA-Z0-9._-]+$'
        return bool(re.match(pattern, name)) and len(name) <= 100

    def _validate_tool_config(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def _validate_profile_config(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'")

        return errors

    def _validate_workenv_settings(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        if not isinstance(self.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.workenv.cache_ttl}")

        if not isinstance(self.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.workenv.log_level}")

        if not isinstance(self.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.workenv.container_runtime}")

        if not isinstance(self.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.workenv.container_registry}")

        return errors

    def _validate_env_config(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(f"Invalid environment key '{key}': must contain only letters, numbers, and underscores")

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(f"Environment list item {i} for '{key}' must be string, number, or boolean")

        return errors

    def _is_valid_duration(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re
        pattern = r'^\d+[smhdw]$'
        return bool(re.match(pattern, duration))

    def _is_valid_registry_url(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re
        # Basic URL validation for container registries
        pattern = r'^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$'
        return bool(re.match(pattern, url))

    def write_config(self, config_data: dict[str, Any]):
        """Write configuration data to file."""
        # Update current config
        if "project_name" in config_data:
            self.project_name = config_data["project_name"]
        if "version" in config_data:
            self.version = config_data["version"]
        if "tools" in config_data:
            self.tools = config_data["tools"]
        if "profiles" in config_data:
            self.profiles = config_data["profiles"]
        if "workenv" in config_data:
            if isinstance(config_data["workenv"], dict):
                for key, value in config_data["workenv"].items():
                    if hasattr(self.workenv, key):
                        setattr(self.workenv, key, value)
        if "env" in config_data:
            self.env = config_data["env"]

        # Save to file
        self.save_config()

    def edit_config(self):
        """Open configuration file in editor."""
        # Ensure file exists
        if not self.config_path.exists():
            # Create with defaults
            self.save_config()

        # Get editor from environment
        editor = os.environ.get("EDITOR") or os.environ.get("VISUAL")
        if not editor:
            raise RuntimeError("No editor configured. Set EDITOR or VISUAL environment variable.")

        # Open in editor
        result = run_command([editor, str(self.config_path)])
        if result.returncode != 0:
            raise RuntimeError(f"Editor exited with error code {result.returncode}")

        # Reload configuration
        self._load_config()
