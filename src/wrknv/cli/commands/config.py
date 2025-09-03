#!/usr/bin/env python3
#
# wrknv/cli/commands/config.py
#
"""
Config Commands
===============
Commands for managing workenv configuration.
"""

import json
import sys
from pathlib import Path

from provide.foundation.hub import register_command
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation import logger

from wrknv.wenv.config import WorkenvConfig
from wrknv.wenv.exceptions import ProfileError


# Register the config group first
@register_command("config", group=True, description="Configuration management")
def config_group():
    """Configuration management commands."""
    pass


@register_command(
    "config.show",
    description="Show current configuration",
)
def config_show(
    output_json: bool = False,
    profile: str | None = None,
):
    """Show current configuration."""
    config = WorkenvConfig()

    if profile:
        # Show specific profile
        profile_data = config.get_profile(profile)
        if not profile_data:
            raise ProfileError(profile, available_profiles=config.list_profiles())

        if output_json:
            echo_info(
                json.dumps({"profile": profile, "tools": profile_data}, indent=2)
            )
        else:
            echo_info(f"Profile: {profile}")
            for tool_name, version in profile_data.items():
                echo_info(f"  {tool_name}: {version}")
    elif output_json:
        # Output entire config as JSON
        config_data = config.to_dict()
        echo_info(json.dumps(config_data, indent=2))
    else:
        # Default formatted output
        config.show_config()


@register_command(
    "config.edit",
    description="Edit configuration file",
)
def config_edit():
    """Edit configuration file."""
    config = WorkenvConfig()
    try:
        config.edit_config()
    except RuntimeError as e:
        echo_error(f"Error: {e}")
        sys.exit(1)


@register_command(
    "config.validate",
    description="Validate configuration file syntax and values",
)
def config_validate(strict: bool = False):
    """Validate configuration file syntax and values."""
    config = WorkenvConfig()

    if not config.config_exists():
        echo_error("No configuration file found")
        echo_info("Create one with: wrknv config init")
        sys.exit(1)

    try:
        is_valid, errors = config.validate()

        if is_valid:
            echo_success("✅ Configuration is valid")
        else:
            echo_error("❌ Configuration validation failed:")
            for error in errors:
                echo_error(f"  • {error}")
            sys.exit(1)

    except Exception as e:
        echo_error(f"Validation error: {e}")
        sys.exit(1)


@register_command(
    "config.init",
    description="Initialize a new configuration file interactively",
)
def config_init(force: bool = False):
    """Initialize a new configuration file interactively."""
    config = WorkenvConfig()

    if config.config_exists() and not force:
        echo_warning("Configuration file already exists")
        echo_info("Use --force to overwrite")
        sys.exit(1)

    try:
        # Interactive initialization
        echo_info("Creating new wrknv configuration...")

        # Prompt for basic settings
        project_name = input("Project name [my-project]: ").strip() or "my-project"

        # Create default config structure
        config_data = {
            "project_name": project_name,
            "workenv": {
                "settings": {
                    "auto_install": True,
                    "use_cache": True,
                    "cache_ttl": "7d",
                }
            },
            "tools": {},
            "profiles": {},
        }

        # Write configuration
        config.write_config(config_data)
        echo_success(f"✅ Configuration created at {config.config_path}")

    except Exception as e:
        echo_error(f"Failed to create configuration: {e}")
        sys.exit(1)


@register_command(
    "config.path",
    description="Show path to configuration file",
)
def config_path():
    """Show path to configuration file."""
    config = WorkenvConfig()
    if config.config_exists():
        echo_info(str(config.config_path))
    else:
        echo_warning("No configuration file found")
        echo_info("Create one with: wrknv config init")


@register_command(
    "config.get",
    description="Get a specific configuration setting",
)
def config_get(key: str):
    """Get a specific configuration setting."""
    config = WorkenvConfig()
    
    try:
        value = config.get_setting(key)
        if value is not None:
            if isinstance(value, (dict, list)):
                echo_info(f"{key}: {json.dumps(value, indent=2)}")
            else:
                echo_info(f"{key}: {value}")
        else:
            echo_warning(f"Setting '{key}' not found")
    except Exception as e:
        echo_error(f"Error getting setting: {e}")
        sys.exit(1)


@register_command(
    "config.set",
    description="Set a configuration value",
)
def config_set(key: str, value: str):
    """Set a configuration value."""
    config = WorkenvConfig()
    
    try:
        # Try to parse value as JSON first (for complex types)
        try:
            parsed_value = json.loads(value)
        except json.JSONDecodeError:
            # If not JSON, treat as string
            # Check for boolean strings
            if value.lower() in ("true", "yes", "on"):
                parsed_value = True
            elif value.lower() in ("false", "no", "off"):
                parsed_value = False
            else:
                parsed_value = value
        
        config.set_setting(key, parsed_value)
        echo_success(f"✅ Set {key} = {parsed_value}")
    except Exception as e:
        echo_error(f"Error setting value: {e}")
        sys.exit(1)