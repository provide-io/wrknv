#
# wrknv/workenv/operations/__init__.py
#
"""
wrknv Operations
===========================
Core operation modules for workenv functionality.
"""

from .download import download_file, verify_checksum
from .install import extract_archive, make_executable
from .platform import get_architecture, get_os_name, get_platform_info
from .verify import run_version_check, verify_tool_installation

__all__ = [
    "download_file",
    "extract_archive",
    "get_architecture",
    "get_os_name",
    "get_platform_info",
    "make_executable",
    "run_version_check",
    "verify_checksum",
    "verify_tool_installation",
]


# 🍲🥄📄🪄
