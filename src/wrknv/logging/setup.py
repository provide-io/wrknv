"""
wrknv Logging Setup
===================
Provides setup functions for wrknv logging configuration.
"""

from __future__ import annotations


import os

from provide.foundation.logger.emoji.hierarchy import register_emoji_hierarchy

from .emojis import WRKNV_EMOJI_HIERARCHY


def setup_wrknv_logging() -> None:
    """
    Set up wrknv-specific logging configuration.

    This includes:
    1. Registering wrknv emoji hierarchy
    2. Bridging WRKNV_LOG_LEVEL to PROVIDE_LOG_LEVEL
    """
    # Register wrknv emoji hierarchy
    register_emoji_hierarchy("wrknv", WRKNV_EMOJI_HIERARCHY)

    # Bridge WRKNV_LOG_LEVEL to foundation logging
    wrknv_log_level = os.environ.get("WRKNV_LOG_LEVEL")
    if wrknv_log_level and not os.environ.get("PROVIDE_LOG_LEVEL"):
        os.environ["PROVIDE_LOG_LEVEL"] = wrknv_log_level


def setup_wrknv_config_logging() -> None:
    """
    Set up logging based on wrknv configuration.

    Reads WRKNV_LOG_LEVEL from wrknv config and applies it to foundation logging.
    """
    try:
        from wrknv.config import WorkenvConfig

        config = WorkenvConfig.load()

        # Only override if PROVIDE_LOG_LEVEL is not already set
        if not os.environ.get("PROVIDE_LOG_LEVEL"):
            if config.workenv.log_level != "WARNING":  # Only if changed from default
                os.environ["PROVIDE_LOG_LEVEL"] = config.workenv.log_level
    except Exception:
        # If config loading fails, don't break logging setup
        pass

    # Always register emoji hierarchy
    register_emoji_hierarchy("wrknv", WRKNV_EMOJI_HIERARCHY)
