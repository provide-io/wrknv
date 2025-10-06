"""
Configuration Persistence for wrknv
====================================
Save, load, and file operations for configuration data.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from provide.foundation.file import read_toml, write_toml
from provide.foundation.logger import get_logger
from provide.foundation.process import run_command

logger = get_logger(__name__)


class WorkenvConfigPersistence:
    """Handles saving and loading configuration files."""

    def __init__(self, config) -> None:
        """Initialize persistence handler with config instance."""
        self.config = config

    def load_config(self) -> None:
        """Load configuration from file."""
        if self.config.config_path and self.config.config_path.exists():
            try:
                # Load TOML using foundation
                config_dict = read_toml(self.config.config_path, default={})

                # Update attributes from loaded config
                if "project_name" in config_dict:
                    self.config.project_name = config_dict["project_name"]
                if "version" in config_dict:
                    self.config.version = config_dict["version"]
                if "tools" in config_dict:
                    self.config.tools = config_dict["tools"]
                if "profiles" in config_dict:
                    self.config.profiles = config_dict["profiles"]
                if "workenv" in config_dict and isinstance(config_dict["workenv"], dict):
                    for key, value in config_dict["workenv"].items():
                        if hasattr(self.config.workenv, key):
                            setattr(self.config.workenv, key, value)
                if "env" in config_dict:
                    self.config.env = config_dict["env"]

            except Exception as e:
                logger.warning(f"Failed to load config from {self.config.config_path}: {e}")

    def save_config(self) -> None:
        """Save configuration to file."""
        # Convert to dict
        config_dict = self.to_dict()

        # Write to file using foundation's atomic TOML writer
        write_toml(self.config.config_path, config_dict, atomic=True)

        logger.info(f"Saved configuration to {self.config.config_path}")

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "project_name": self.config.project_name,
            "version": self.config.version,
            "tools": self.config.tools,
            "profiles": self.config.profiles,
            "workenv": {
                "auto_install": self.config.workenv.auto_install,
                "use_cache": self.config.workenv.use_cache,
                "cache_ttl": self.config.workenv.cache_ttl,
                "log_level": self.config.workenv.log_level,
                "container_runtime": self.config.workenv.container_runtime,
                "container_registry": self.config.workenv.container_registry,
            },
            "env": self.config.env,
        }

    def write_config(self, config_data: dict[str, Any]) -> None:
        """Write configuration data to file."""
        # Update current config
        if "project_name" in config_data:
            self.config.project_name = config_data["project_name"]
        if "version" in config_data:
            self.config.version = config_data["version"]
        if "tools" in config_data:
            self.config.tools = config_data["tools"]
        if "profiles" in config_data:
            self.config.profiles = config_data["profiles"]
        if "workenv" in config_data and isinstance(config_data["workenv"], dict):
            for key, value in config_data["workenv"].items():
                if hasattr(self.config.workenv, key):
                    setattr(self.config.workenv, key, value)
        if "env" in config_data:
            self.config.env = config_data["env"]

        # Save to file
        self.save_config()

    def edit_config(self) -> None:
        """Open configuration file in editor."""
        # Ensure file exists
        if not self.config.config_path.exists():
            # Create with defaults
            self.save_config()

        # Get editor from environment
        editor = os.environ.get("EDITOR") or os.environ.get("VISUAL")
        if not editor:
            raise RuntimeError("No editor configured. Set EDITOR or VISUAL environment variable.")

        # Open in editor
        result = run_command([editor, str(self.config.config_path)])
        if result.returncode != 0:
            raise RuntimeError(f"Editor exited with error code {result.returncode}")

        # Reload configuration
        self.load_config()

    def config_exists(self) -> bool:
        """Check if configuration file exists."""
        return self.config.config_path.exists() if self.config.config_path else False

    def get_config_path(self) -> Path:
        """Get path to configuration file."""
        return self.config.config_path
