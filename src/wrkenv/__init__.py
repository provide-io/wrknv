"""
🧰🌍 wrkenv - Work Environment Tool
===================================

A flexible tool for managing development environments and tool versions.
Supports Terraform, OpenTofu, Go, UV, and more.

Can be used standalone or integrated with other tools like TofuSoup.
"""

__version__ = "0.1.0"

# Import workenv module to make it accessible
from . import workenv

# Public API
from .workenv.config import WorkenvConfig, WorkenvConfigError
from .workenv.managers.factory import get_tool_manager, get_supported_tools

__all__ = [
    "workenv",
    "WorkenvConfig",
    "WorkenvConfigError", 
    "get_tool_manager",
    "get_supported_tools",
]