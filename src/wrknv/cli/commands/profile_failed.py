"""
Profile Commands for wrknv
===========================
Commands for managing configuration profiles.
"""

from pathlib import Path
from typing import Optional

from provide.foundation.cli import echo_error, echo_info, echo_success
from provide.foundation.hub import register_command

from wrknv.config import WorkenvConfig


@register_command(
    "profile-list",
    description="List available profiles",
)
def profile_list():
    """List all available profiles."""
    config = WorkenvConfig.load()
    profiles = config.list_profiles()
    
    if not profiles:
        echo_info("No profiles defined")
        return
    
    echo_info("Available profiles:")
    for profile_name in profiles:
        profile_data = config.get_profile(profile_name)
        tool_count = len(profile_data) if profile_data else 0
        echo_info(f"  • {profile_name} ({tool_count} tools)")


@register_command(
    "show",
    parent="profile",
    description="Show profile details",
)
def profile_show(name: str):
    """Show details of a specific profile."""
    config = WorkenvConfig.load()
    profile_data = config.get_profile(name)
    
    if not profile_data:
        echo_error(f"Profile '{name}' not found")
        return
    
    echo_info(f"Profile: {name}")
    for tool, version in profile_data.items():
        echo_info(f"  {tool}: {version}")


@register_command(
    "load",
    parent="profile",
    description="Load and apply a profile",
)
def profile_load(name: str, save: bool = False):
    """
    Load and apply a profile to the current configuration.
    
    Args:
        name: Name of the profile to load
        save: Save the profile to the configuration file
    """
    config = WorkenvConfig.load()
    profile_data = config.get_profile(name)
    
    if not profile_data:
        echo_error(f"Profile '{name}' not found")
        return
    
    # Apply profile tools
    for tool, version in profile_data.items():
        if isinstance(config.tools.get(tool), dict):
            config.tools[tool]["version"] = version
        else:
            config.tools[tool] = version
    
    if save:
        config.save_config()
        echo_success(f"Profile '{name}' applied and saved")
    else:
        echo_success(f"Profile '{name}' applied (not saved)")


@register_command(
    "save",
    parent="profile",
    description="Save current configuration as a profile",
)
def profile_save(name: str):
    """Save the current tool configuration as a profile."""
    config = WorkenvConfig.load()
    
    # Get current tools
    tools = config.get_all_tools()
    
    if not tools:
        echo_error("No tools configured to save")
        return
    
    # Save as profile
    config.profiles[name] = tools
    config.save_config()
    
    echo_success(f"Saved current configuration as profile '{name}'")
    echo_info(f"Tools in profile: {', '.join(tools.keys())}")


@register_command(
    "delete",
    parent="profile",
    description="Delete a profile",
)
def profile_delete(name: str):
    """Delete a profile from the configuration."""
    config = WorkenvConfig.load()
    
    if name not in config.profiles:
        echo_error(f"Profile '{name}' not found")
        return
    
    del config.profiles[name]
    config.save_config()
    
    echo_success(f"Deleted profile '{name}'")


@register_command(
    "export",
    parent="profile",
    description="Export a profile to a file",
)
def profile_export(name: str, output: Path):
    """
    Export a profile to a TOML file.
    
    Args:
        name: Name of the profile to export
        output: Output file path
    """
    config = WorkenvConfig.load()
    profile_data = config.get_profile(name)
    
    if not profile_data:
        echo_error(f"Profile '{name}' not found")
        return
    
    try:
        import tomli_w
    except ImportError:
        echo_error("tomli-w is required for exporting profiles")
        return
    
    # Create profile structure
    export_data = {
        "profile": {
            "name": name,
            "tools": profile_data
        }
    }
    
    # Write to file
    with open(output, "wb") as f:
        tomli_w.dump(export_data, f)
    
    echo_success(f"Exported profile '{name}' to {output}")


@register_command(
    "import",
    parent="profile",
    description="Import a profile from a file",
)
def profile_import(input: Path, name: Optional[str] = None):
    """
    Import a profile from a TOML file.
    
    Args:
        input: Input file path
        name: Override the profile name (optional)
    """
    config = WorkenvConfig.load()
    
    if not input.exists():
        echo_error(f"File not found: {input}")
        return
    
    try:
        import tomllib
    except ImportError:
        try:
            import tomli as tomllib
        except ImportError:
            echo_error("tomli or Python 3.11+ is required for importing profiles")
            return
    
    # Read profile data
    with open(input, "rb") as f:
        data = tomllib.load(f)
    
    if "profile" not in data:
        echo_error("Invalid profile file format")
        return
    
    profile_data = data["profile"]
    profile_name = name or profile_data.get("name")
    
    if not profile_name:
        echo_error("Profile name not specified")
        return
    
    # Import profile
    config.profiles[profile_name] = profile_data.get("tools", {})
    config.save_config()
    
    echo_success(f"Imported profile '{profile_name}' from {input}")