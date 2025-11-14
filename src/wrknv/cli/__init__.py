"""
wrknv CLI Module
================
Command-line interface for wrknv tool management.
"""

from wrknv.cli.hub_cli import create_cli, main

# Legacy compatibility - will be removed
try:
    from wrknv.cli.main import entry_point, workenv_cli
except ImportError:
    # If old modules don't exist, use new ones
    entry_point = main
    workenv_cli = create_cli

__all__ = ["create_cli", "main", "workenv_cli", "entry_point"]