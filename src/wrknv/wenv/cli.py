#!/usr/bin/env python3
#
# wrknv/wenv/cli.py
#
"""
Legacy CLI Entry Point
======================
This file now just imports from the new modular CLI structure.
Kept for backwards compatibility.
"""

from wrknv.cli.main import entry_point, workenv_cli

# Export the same interface for backwards compatibility
__all__ = ["workenv_cli", "entry_point"]

if __name__ == "__main__":
    entry_point()


# 🧰🌍🖥️🪄