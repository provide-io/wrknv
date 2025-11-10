#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Logging Setup
===================
Provides setup functions for wrknv logging configuration."""

from __future__ import annotations

from provide.foundation.logger.emoji.hierarchy import register_emoji_hierarchy

from .emojis import WRKNV_EMOJI_HIERARCHY


def setup_wrknv_logging() -> None:
    """
    Set up wrknv-specific logging configuration.

    This includes registering the wrknv emoji hierarchy.
    """
    # Register wrknv emoji hierarchy
    register_emoji_hierarchy("wrknv", WRKNV_EMOJI_HIERARCHY)


def setup_wrknv_config_logging() -> None:
    """
    Set up logging based on wrknv configuration.

    This now only registers the emoji hierarchy.
    The actual log level configuration is handled by WorkenvConfig.
    """
    # Register emoji hierarchy
    register_emoji_hierarchy("wrknv", WRKNV_EMOJI_HIERARCHY)


# 🧰🌍🔚
