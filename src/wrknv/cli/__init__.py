"""
wrknv CLI Module
================
Command-line interface for wrknv tool management.
"""

from wrknv.cli.hub_cli import create_cli, main

# Compatibility aliases
entry_point = main
workenv_cli = create_cli

__all__ = ["create_cli", "main", "workenv_cli", "entry_point"]