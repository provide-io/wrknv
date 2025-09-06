#!/usr/bin/env python3
#
# wrknv/wenv/config_foundation.py
#
"""
wrknv Configuration Management using provide.foundation.config
==============================================================
Simplified configuration system using foundation capabilities.
"""

from pathlib import Path
from typing import Any

from attrs import define, field
from provide.foundation.config import (
    BaseConfig,
    FileConfigLoader,
    MultiSourceLoader,
    SyncConfigManager,
    field as config_field,
)
from provide.foundation.config.env import RuntimeConfig, env_field
from provide.foundation import logger
from provide.foundation.process import run_command

from .exceptions import ConfigurationError, ProfileError


class WorkenvConfigError(ConfigurationError):
    """Raised when there's an error in workenv configuration."""
    pass


@define
class WorkenvToolConfig:
    """Configuration for a single tool."""
    version: str | None = None
    path: str | None = None
    env: dict[str, str] = field(factory=dict)


@define
class WorkenvSettings(BaseConfig):
    """Workenv-specific settings."""
    auto_install: bool = config_field(
        default=True,
        description="Automatically install missing tools",
        env_var="WRKNV_AUTO_INSTALL"
    )
    use_cache: bool = config_field(
        default=True,
        description="Use cached tool installations",
        env_var="WRKNV_USE_CACHE"
    )
    cache_ttl: str = config_field(
        default="7d",
        description="Cache time-to-live",
        env_var="WRKNV_CACHE_TTL"
    )
    log_level: str = config_field(
        default="INFO",
        description="Logging level",
        env_var="WRKNV_LOG_LEVEL"
    )
    container_runtime: str = config_field(
        default="docker",
        description="Container runtime to use",
        env_var="WRKNV_CONTAINER_RUNTIME"
    )
    container_registry: str = config_field(
        default="ghcr.io",
        description="Default container registry",
        env_var="WRKNV_CONTAINER_REGISTRY"
    )


@define
class WorkenvConfig(BaseConfig):
    """Main workenv configuration."""
    
    # Project metadata
    project_name: str = config_field(
        default="my-project",
        description="Project name",
        env_var="WRKNV_PROJECT_NAME"
    )
    version: str = config_field(
        default="1.0.0", 
        description="Project version",
        env_var="WRKNV_VERSION"
    )
    
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
    
    def __init__(self, config_file: Path | None = None):
        """Initialize configuration manager."""
        self.config_path = config_file or self._find_config_file()
        self._manager = self._create_manager()
        self._load_config()
    
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
        """Create configuration manager with loaders."""
        loaders = []
        
        # Add file loader if config file exists
        if self.config_path and self.config_path.exists():
            loaders.append(
                FileConfigLoader(
                    str(self.config_path),
                    format="toml" if str(self.config_path).endswith(".toml") else "auto"
                )
            )
        
        # Create multi-source loader
        if loaders:
            loader = MultiSourceLoader(loaders)
        else:
            loader = None
        
        return SyncConfigManager(loader=loader)
    
    def _load_config(self):
        """Load configuration from all sources."""
        if self._manager.loader:
            config_dict = self._manager.load()
            
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
                self.workenv = WorkenvSettings(**config_dict["workenv"])
            if "env" in config_dict:
                self.env = config_dict["env"]
    
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
    
    def get_all_tools(self) -> dict[str, str]:
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
                raise ConfigurationError(f"Cannot set {key}: parent doesn't exist")
        
        # Set the value
        last_part = parts[-1]
        if hasattr(current, last_part):
            setattr(current, last_part, value)
        elif isinstance(current, dict):
            current[last_part] = value
        else:
            raise ConfigurationError(f"Cannot set {key}: invalid target")
        
        # Save to file
        self.save_config()
    
    def save_config(self):
        """Save configuration to file."""
        if not tomli_w:
            raise ConfigurationError("tomli-w is required to save TOML files")
        
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
        """Validate configuration."""
        errors = []
        
        # Check required fields
        if not self.project_name:
            errors.append("Missing required field: project_name")
        
        # Validate tool versions
        for tool, config in self.tools.items():
            if isinstance(config, dict):
                version = config.get("version")
                if version and not self._is_valid_version(version):
                    errors.append(f"Invalid version for {tool}: {version}")
        
        return len(errors) == 0, errors
    
    def _is_valid_version(self, version: str) -> bool:
        """Check if version string is valid."""
        if version in ("latest", "stable", "dev"):
            return True
        # Basic semver check
        parts = version.split(".")
        return len(parts) >= 2 and all(p.isdigit() for p in parts[:2])
    
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


# Import tomli_w for saving
import os
try:
    import tomli_w
except ImportError:
    tomli_w = None