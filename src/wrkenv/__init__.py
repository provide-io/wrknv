"""
🧰🌍 wrkenv - Work Environment Tool
===================================

A flexible tool for managing development environments and tool versions.
Supports Terraform, OpenTofu, Go, UV, and more.

Can be used standalone or integrated with other tools like TofuSoup.
"""

__version__ = "0.1.0"

# Import env module to make it accessible
from . import env

# Public API
from .env.config import WorkenvConfig, WorkenvConfigError
from .env.managers.factory import get_tool_manager, get_supported_tools

__all__ = [
    "env",
    "WorkenvConfig",
    "WorkenvConfigError", 
    "get_tool_manager",
    "get_supported_tools",
]