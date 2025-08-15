"""
🧰🌍 wrkenv - Work Environment Tool
===================================

A flexible tool for managing development environments and tool versions.
Supports Terraform, OpenTofu, Go, UV, and more.

Can be used standalone or integrated with other tools.
"""

__version__ = "0.1.0"

# Public API exports
from wrkenv.wenv.config import WorkenvConfig, WorkenvConfigError
from wrkenv.wenv.managers.factory import get_supported_tools, get_tool_manager

__all__ = [
    "wenv",
    "package",
    "container",
    "WorkenvConfig",
    "WorkenvConfigError",
    "get_tool_manager",
    "get_supported_tools",
]
