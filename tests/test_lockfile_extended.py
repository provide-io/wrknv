#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for lockfile management (extended)."""

from __future__ import annotations

from pathlib import Path

from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch
import pytest

from wrknv.config import WorkenvConfig
from wrknv.lockfile import Lockfile, LockfileManager


class TestLockfileIntegration(FoundationTestCase):
    """Integration tests for lockfile functionality."""

    def test_full_lockfile_workflow(self, tmp_path: Path) -> None:
        """Test complete workflow of creating, saving, and loading lockfile."""
        config = WorkenvConfig()
        config.tools = {"uv": "0.5.x"}

        manager = LockfileManager(tmp_path)

        # Create lockfile
        with patch("provide.foundation.time.provide_now") as mock_now:
            mock_now.return_value = Mock(isoformat=Mock(return_value="2025-01-01T00:00:00"))
            lockfile = Lockfile.from_config(config)
            lockfile.add_resolved_tool(
                name="uv",
                version="0.5.0",
                resolved_from="0.5.x",
            )

        # Save lockfile
        manager.save_lockfile(lockfile)

        # Load lockfile
        loaded = manager.load_lockfile()
        assert loaded is not None
        assert loaded.config_checksum == lockfile.config_checksum
        assert "uv" in loaded.resolved_tools
        assert loaded.resolved_tools["uv"].version == "0.5.0"

        # Check validity
        assert manager.is_lockfile_valid(config) is True

        # Get locked versions
        versions = manager.get_locked_versions()
        assert versions["uv"] == "0.5.0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
