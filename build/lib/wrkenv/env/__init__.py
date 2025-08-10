#
# wrkenv/env/__init__.py
#
"""
wrkenv.env
==========
Core environment management functionality for development tool management.

Provides:
- Cross-platform tool installation (Terraform, OpenTofu, Go, UV, etc.)
- Version management and switching
- Development environment profiles  
- Version matrix testing support
- Flexible configuration system

This module can be used standalone or integrated with other tools.
"""

__version__ = "0.1.0"

# Submodules are available but not imported to avoid circular imports
# Use explicit imports: from wrkenv.env import config, managers, etc.

__all__ = ["config", "managers", "operations", "testing"]


# 🧰🌍🖥️🪄
