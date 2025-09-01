#!/usr/bin/env python3
#
# wrknv/wenv/cli.py
#
"""
CLI Entry Point
===============
Entry point for the wrknv CLI using foundation hub.
"""

from wrknv.cli.hub_cli import main, create_cli

# Export for compatibility
entry_point = main
workenv_cli = create_cli()

if __name__ == "__main__":
    main()


# 🧰🌍🖥️🪄