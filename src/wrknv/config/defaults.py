from __future__ import annotations

from pathlib import Path

"""Centralized default values for wrknv configuration.
All defaults are defined here instead of inline in field definitions.
"""

# =================================
# Command Operation defaults
# =================================
DEFAULT_TIMEOUT = 10
DEFAULT_SHORT_TIMEOUT = 5
DEFAULT_DRY_RUN = False
DEFAULT_FORCE = False
DEFAULT_VERIFY = True
DEFAULT_ACTIVATE = True
DEFAULT_AUTO_DISCOVER = True

# =================================
# Version and Release defaults
# =================================
DEFAULT_VERSION = "1.0.0"
DEFAULT_WORKSPACE_VERSION = "1.0"

# =================================
# Workspace Configuration defaults
# =================================
DEFAULT_SYNC_STRATEGY = "manual"  # "manual", "auto", "check"

# =================================
# Container defaults
# =================================
DEFAULT_CONTAINER_RUNTIME = "docker"
DEFAULT_CONTAINER_PLATFORM = "linux/amd64"

# =================================
# Package and Registry defaults
# =================================
DEFAULT_PACKAGE_FORMAT = "psp"
DEFAULT_SEARCH_LIMIT = 10

# =================================
# Tool Manager defaults
# =================================
DEFAULT_TOOL_TIMEOUT = 10
DEFAULT_DOWNLOAD_TIMEOUT = 30

# =================================
# Environment defaults
# =================================
DEFAULT_PYTHON_VERSION = "3.11"

# =================================
# Registry and URL defaults
# =================================
DEFAULT_REGISTRY_URL = None  # Will be set when registry is implemented

# =================================
# Template defaults
# =================================
DEFAULT_TEMPLATE_VERSION = None
DEFAULT_TEMPLATE_BRANCH = None

# =================================
# Logging defaults
# =================================
DEFAULT_LOG_LEVEL = "INFO"

# =================================
# CLI defaults
# =================================
DEFAULT_CLI_NAME = "wrknv"
DEFAULT_CLI_VERSION = "0.1.0"
DEFAULT_CLI_HELP = (
    "🧰🌍 Manage development environment tools and versions.\n\n"
    "wrknv provides cross-platform tool installation and version management "
    "for development environments, including Terraform, OpenTofu, Go, UV, and more."
)

# =================================
# Factory functions for mutable defaults
# =================================


def default_workenv_cache_dir() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "cache" / "packages"


def default_config_dir() -> Path:
    """Factory for wrknv config directory."""
    return Path.home() / ".wrknv"


def default_workenv_dir() -> Path:
    """Factory for workenv directory."""
    return Path("workenv")


def default_empty_list() -> list[str]:
    """Factory for empty string lists."""
    return []


def default_empty_dict() -> dict[str, str]:
    """Factory for empty string dictionaries."""
    return {}


def default_custom_values() -> dict[str, any]:
    """Factory for custom values dictionary."""
    return {}
