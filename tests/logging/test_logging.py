#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for logging.emojis and logging.setup modules."""

from __future__ import annotations

from provide.testkit import FoundationTestCase

from wrknv.logging.emojis import WRKNV_EMOJI_HIERARCHY
from wrknv.logging.setup import setup_wrknv_config_logging, setup_wrknv_logging


class TestWrknvEmojiHierarchy(FoundationTestCase):
    """Tests for WRKNV_EMOJI_HIERARCHY constant."""

    def test_is_dict(self) -> None:
        assert isinstance(WRKNV_EMOJI_HIERARCHY, dict)

    def test_has_cli_key(self) -> None:
        assert "wrknv.cli" in WRKNV_EMOJI_HIERARCHY

    def test_has_config_key(self) -> None:
        assert "wrknv.config.core" in WRKNV_EMOJI_HIERARCHY

    def test_all_values_are_strings(self) -> None:
        for key, value in WRKNV_EMOJI_HIERARCHY.items():
            assert isinstance(value, str), f"Key {key!r} has non-string value"

    def test_all_keys_start_with_wrknv(self) -> None:
        for key in WRKNV_EMOJI_HIERARCHY:
            assert key.startswith("wrknv."), f"Key {key!r} does not start with 'wrknv.'"


class TestSetupWrknvLogging(FoundationTestCase):
    """Tests for setup_wrknv_logging."""

    def test_runs_without_error(self) -> None:
        # Function is a no-op placeholder; just verify it doesn't raise
        setup_wrknv_logging()

    def test_returns_none(self) -> None:
        result = setup_wrknv_logging()
        assert result is None


class TestSetupWrknvConfigLogging(FoundationTestCase):
    """Tests for setup_wrknv_config_logging."""

    def test_runs_without_error(self) -> None:
        setup_wrknv_config_logging()

    def test_returns_none(self) -> None:
        result = setup_wrknv_config_logging()
        assert result is None


# 🧰🌍🔚
