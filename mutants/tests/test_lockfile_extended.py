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


class TestResolveAndLockBranches(FoundationTestCase):
    """Branches in LockfileManager.resolve_and_lock (lines 178->182, 199->183)."""

    def test_valid_lockfile_skips_recreation(self, tmp_path: Path) -> None:
        """Line 178->182: lockfile exists and is valid → skip create_lockfile (line 179)."""
        config = WorkenvConfig()
        config.tools = {"uv": "0.5.x"}
        manager = LockfileManager(tmp_path)

        existing_lockfile = Mock()
        existing_lockfile.resolved_tools = {}

        with (
            patch.object(manager, "load_lockfile", return_value=existing_lockfile),
            patch.object(manager, "is_lockfile_valid", return_value=True),
            patch.object(manager, "create_lockfile") as mock_create,
            patch.object(manager, "save_lockfile"),
            patch("wrknv.managers.factory.get_tool_manager", return_value=Mock()),
            patch("wrknv.utils.version_resolver.resolve_tool_versions", return_value=["0.5.0"]),
        ):
            manager.resolve_and_lock(config)

        # create_lockfile should NOT have been called — lockfile was already valid
        mock_create.assert_not_called()

    def test_empty_resolved_versions_skips_add(self, tmp_path: Path) -> None:
        """Line 199->183: resolve_tool_versions returns [] → add_resolved_tool not called."""
        config = WorkenvConfig()
        config.tools = {"uv": "0.5.x"}
        manager = LockfileManager(tmp_path)

        with (
            patch.object(manager, "save_lockfile"),
            patch("wrknv.managers.factory.get_tool_manager") as mock_get_mgr,
            patch("wrknv.utils.version_resolver.resolve_tool_versions") as mock_resolve,
        ):
            mock_mgr = Mock()
            mock_get_mgr.return_value = mock_mgr
            # Return empty list → if resolved_versions: is False → line 199->183
            mock_resolve.return_value = []

            result = manager.resolve_and_lock(config)

        assert result is not None
        # uv should NOT be in resolved tools since resolve returned empty
        assert "uv" not in result.resolved_tools


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
