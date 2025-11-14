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

import click
from click import secho

from wrknv.wenv.config import WorkenvConfig
from wrknv.wenv.exceptions import ProfileError
from wrknv.wenv.visual import print_error, print_info, print_success, print_warning


@click.group(name="config")
def config_group():
    """⚙️ Manage workenv configuration."""
    pass


@config_group.command(name="show")
@click.option("--json", "output_json", is_flag=True, help="Output in JSON format")
@click.option("--profile", help="Show specific profile configuration")
def config_show(output_json: bool, profile: str):
    """Show current configuration."""
    config = WorkenvConfig()

    if profile:
        # Show specific profile
        profile_data = config.get_profile(profile)
        if not profile_data:
            raise ProfileError(profile, available_profiles=config.list_profiles())

        if output_json:
            click.echo(
                json.dumps({"profile": profile, "tools": profile_data}, indent=2)
            )
        else:
            click.echo(f"Profile: {profile}")
            for tool_name, version in profile_data.items():
                click.echo(f"  {tool_name}: {version}")
    elif output_json:
        # Output entire config as JSON
        config_data = config.to_dict()
        click.echo(json.dumps(config_data, indent=2))
    else:
        # Default formatted output
        config.show_config()


@config_group.command(name="edit")
def config_edit():
    """Edit configuration file."""
    config = WorkenvConfig()
    try:
        config.edit_config()
    except RuntimeError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@config_group.command(name="validate")
@click.option("--strict", is_flag=True, help="Strict validation mode")
def config_validate(strict: bool):
    """Validate configuration file syntax and values."""
    config = WorkenvConfig()

    if not config.config_exists():
        print_error("No configuration file found")
        print_info("Create one with: wrknv config init")
        sys.exit(1)

    try:
        is_valid, errors = config.validate()

        if is_valid:
            print_success("✅ Configuration is valid")
        else:
            print_error("❌ Configuration validation failed:")
            for error in errors:
                click.echo(f"  • {error}", err=True)
            sys.exit(1)

    except Exception as e:
        print_error(f"Validation error: {e}")
        sys.exit(1)


@config_group.command(name="init")
@click.option("--force", is_flag=True, help="Overwrite existing configuration")
def config_init(force: bool):
    """Initialize a new configuration file interactively."""
    config_path = Path.cwd() / "wrknv.toml"

    if config_path.exists() and not force:
        print_error("Configuration file already exists")
        print_info("Use --force to overwrite")
        sys.exit(1)

    # Interactive prompts
    project_name = click.prompt("Project name", default=Path.cwd().name)
    version = click.prompt("Version", default="1.0.0")
    log_level = click.prompt(
        "Log level",
        default="INFO",
        type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    )

    # Ask about common tools
    tools = {}
    if click.confirm("Do you want to configure Terraform/OpenTofu?"):
        tool_choice = click.prompt(
            "Which tool?", type=click.Choice(["terraform", "tofu"]), default="tofu"
        )
        version = click.prompt(
            f"{tool_choice} version",
            default="1.8.0" if tool_choice == "tofu" else "1.5.7",
        )
        tools[tool_choice] = {"version": version}

    if click.confirm("Do you want to configure Go?"):
        version = click.prompt("Go version", default="1.22.1")
        tools["go"] = {"version": version}

    if click.confirm("Do you want to configure UV?"):
        version = click.prompt("UV version", default="0.4.0")
        tools["uv"] = {"version": version}

    # Create configuration
    import tomli_w

    config_data = {
        "project_name": project_name,
        "version": version,
        "log_level": log_level,
    }

    if tools:
        config_data["tools"] = tools

    # Add container section if requested
    if click.confirm("Enable container support?"):
        config_data["container"] = {
            "enabled": True,
            "base_image": "ubuntu:22.04",
            "python_version": "3.11",
        }

    # Write configuration
    with open(config_path, "w") as f:
        f.write(tomli_w.dumps(config_data))

    print_success(f"✅ Created configuration file: {config_path}")
    print_info("You can edit it with: wrknv config edit")


@config_group.command(name="get")
@click.argument("key")
def config_get(key: str):
    """Get a configuration value."""
    config = WorkenvConfig()

    try:
        value = config.get_setting(key)
        if value is None:
            print_warning(f"Key '{key}' not found")
            sys.exit(1)

        if isinstance(value, (dict, list)):
            secho(json.dumps(value, indent=2), fg="cyan")
        else:
            # Output format expected by tests
            click.echo(f"{key}: {value}")

    except Exception as e:
        print_error(f"Error getting config value: {e}")
        sys.exit(1)


@config_group.command(name="set")
@click.argument("key")
@click.argument("value")
def config_set(key: str, value: str):
    """Set a configuration value."""
    config = WorkenvConfig()

    try:
        # Try to parse value as JSON first (for complex types)
        try:
            parsed_value = json.loads(value)
        except json.JSONDecodeError:
            # Not JSON, treat as string
            parsed_value = value

        if config.set_setting(key, parsed_value):
            print_success(f"✅ Set {key} to {value}")
        else:
            print_error(f"Failed to set {key}")
            sys.exit(1)

    except Exception as e:
        print_error(f"Error setting config value: {e}")
        sys.exit(1)


@config_group.command(name="path")
def config_path():
    """Show path to configuration file."""
    config = WorkenvConfig()
    config_file = config.get_config_path()

    if config_file.exists():
        click.echo(str(config_file.absolute()))
    else:
        print_warning("No configuration file found")
        print_info("Create one with: wrknv config init")
        sys.exit(1)