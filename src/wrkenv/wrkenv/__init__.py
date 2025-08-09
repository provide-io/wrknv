#
# wrkenv/workenv/__init__.py
#
"""
wrkenv.workenv
==============
Core workenv functionality for development tool management.

Provides:
- Cross-platform tool installation (Terraform, OpenTofu, Go, UV, etc.)
- Version management and switching
- Development environment profiles  
- Version matrix testing support
- Flexible configuration system

This module can be used standalone or integrated with other tools.
"""

__version__ = "0.1.0"

# Import submodules to make them accessible
from . import config
from . import managers
from . import operations
from . import testing

__all__ = ["config", "managers", "operations", "testing"]


# 🧰🌍🖥️🪄
