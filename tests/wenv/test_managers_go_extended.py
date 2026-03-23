#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.managers.go module (extended)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock, patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.wenv.managers.go import GoManager


class TestHarnessCompatibility(FoundationTestCase):
    """Test harness compatibility methods."""

    @patch.object(GoManager, "get_installed_version", return_value="1.22.0")
    def test_get_harness_compatibility_installed(self, mock_version: Mock) -> None:
        """Test harness compatibility when Go is installed."""
        manager = GoManager()
        compat = manager.get_harness_compatibility()

        assert compat["status"] == "compatible"
        assert compat["version"] == "1.22.0"
        assert "harness" in compat
        # All harnesses should be compatible with Go 1.22
        assert compat["harness"]["go.cty"]["compatible"] is True
        assert compat["harness"]["go.rpc"]["compatible"] is True
        assert compat["harness"]["go.wire"]["compatible"] is True
        assert compat["harness"]["go.hcl"]["compatible"] is True

    @patch.object(GoManager, "get_installed_version", return_value=None)
    def test_get_harness_compatibility_not_installed(self, mock_version: Mock) -> None:
        """Test harness compatibility when Go is not installed."""
        manager = GoManager()
        compat = manager.get_harness_compatibility()

        assert compat["status"] == "not_installed"

    def test_check_go_cty_compatibility_compatible(self) -> None:
        """Test Go CTY compatibility check with compatible version."""
        manager = GoManager()
        result = manager._check_go_cty_compatibility("1.20.0")

        assert result["compatible"] is True
        assert "1.18+" in result["notes"]

    def test_check_go_cty_compatibility_incompatible(self) -> None:
        """Test Go CTY compatibility check with incompatible version."""
        manager = GoManager()
        result = manager._check_go_cty_compatibility("1.17.0")

        assert result["compatible"] is False
        assert "1.18+" in result["notes"]

    def test_check_go_rpc_compatibility_compatible(self) -> None:
        """Test Go RPC compatibility check with compatible version."""
        manager = GoManager()
        result = manager._check_go_rpc_compatibility("1.20.0")

        assert result["compatible"] is True
        assert "1.19+" in result["notes"]

    def test_check_go_rpc_compatibility_incompatible(self) -> None:
        """Test Go RPC compatibility check with incompatible version."""
        manager = GoManager()
        result = manager._check_go_rpc_compatibility("1.18.0")

        assert result["compatible"] is False
        assert "1.19+" in result["notes"]

    def test_check_go_wire_compatibility(self) -> None:
        """Test Go wire protocol compatibility check."""
        manager = GoManager()
        result = manager._check_go_wire_compatibility("1.20.0")

        assert result["compatible"] is True
        assert "1.18+" in result["notes"]

    def test_check_go_hcl_compatibility(self) -> None:
        """Test Go HCL compatibility check."""
        manager = GoManager()
        result = manager._check_go_hcl_compatibility("1.20.0")

        assert result["compatible"] is True
        assert "1.18+" in result["notes"]


class TestVersionComparison(FoundationTestCase):
    """Test version comparison method."""

    def test_version_compare_less_than(self) -> None:
        """Test version comparison with first version less than second."""
        manager = GoManager()
        result = manager._version_compare("1.20.0", "1.21.0")
        assert result == -1

    def test_version_compare_greater_than(self) -> None:
        """Test version comparison with first version greater than second."""
        manager = GoManager()
        result = manager._version_compare("1.21.0", "1.20.0")
        assert result == 1

    def test_version_compare_equal(self) -> None:
        """Test version comparison with equal versions."""
        manager = GoManager()
        result = manager._version_compare("1.20.0", "1.20.0")
        assert result == 0

    def test_version_compare_patch_level(self) -> None:
        """Test version comparison at patch level."""
        manager = GoManager()
        result = manager._version_compare("1.20.1", "1.20.5")
        assert result == -1

    def test_version_compare_different_lengths(self) -> None:
        """Test version comparison with different segment counts."""
        manager = GoManager()
        # 1.20.0.0 vs 1.20.0 - should handle gracefully
        result = manager._version_compare("1.20.0", "1.21.0")
        assert result == -1


class TestGoPathMethods(FoundationTestCase):
    """Test GOROOT and GOPATH methods."""

    def test_get_goroot(self, tmp_path: Path) -> None:
        """Test GOROOT path generation."""
        config = WorkenvConfig()
        config.workenv_cache_dir = str(tmp_path / "cache")
        manager = GoManager(config)

        goroot = manager.get_goroot("1.22.0")

        assert goroot == manager.install_path / "go" / "1.22.0" / "go"
        assert "1.22.0" in str(goroot)

    def test_get_gopath(self, tmp_path: Path) -> None:
        """Test GOPATH path generation."""
        config = WorkenvConfig()
        config.workenv_cache_dir = str(tmp_path / "cache")
        manager = GoManager(config)

        gopath = manager.get_gopath("1.22.0")

        assert gopath == manager.install_path / "go" / "1.22.0" / "gopath"
        assert "1.22.0" in str(gopath)
        assert "gopath" in str(gopath)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
