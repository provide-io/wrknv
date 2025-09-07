"""
🧰🌍 wrknv - Work Environment Tool
===================================

A flexible tool for managing development environments and tool versions.
Supports Terraform, OpenTofu, Go, UV, and more.

Can be used standalone or integrated with other tools.
"""

from wrknv._version import __version__

# Public API exports
from wrknv.config import WorkenvConfig, WorkenvConfigError
from wrknv.wenv.managers.factory import get_supported_tools, get_tool_manager

__all__ = [
    "__version__",
    "wenv",
    "package",
    "container",
    "WorkenvConfig",
    "WorkenvConfigError",
    "get_tool_manager",
    "get_supported_tools",
]
