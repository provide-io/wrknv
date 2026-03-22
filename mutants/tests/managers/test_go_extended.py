#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.go module - verify, harness compatibility, version compare, paths."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.config import WorkenvConfig
from wrknv.managers.go import GoManager


def _make_manager(tmp_dir: pathlib.Path) -> GoManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: (
        str(tmp_dir / "tools") if key == "install_path" else default
    )
    cfg.get_tool_version.return_value = None
    cfg.install_path = str(tmp_dir / "tools")
    return GoManager(config=cfg)


class TestVerifyInstallation(FoundationTestCase):
    """Tests for GoManager.verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.verify_installation("1.22.0")
        assert result is False

    def test_returns_true_when_version_matches(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "go version go1.22.0 linux/amd64"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.22.0")
        assert result is True

    def test_returns_false_when_version_not_in_stdout(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "go version go1.21.5 linux/amd64"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.22.0")
        assert result is False

    def test_returns_false_when_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 1
        mock_result.stderr = "error"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.22.0")
        assert result is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.22.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with mock.patch("provide.foundation.process.run", side_effect=OSError("exec failed")):
            result = manager.verify_installation("1.22.0")
        assert result is False


class TestGetHarnessCompatibility(FoundationTestCase):
    """Tests for GoManager.get_harness_compatibility."""

    def test_returns_not_installed_when_no_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = None
        result = manager.get_harness_compatibility()
        assert result == {"status": "not_installed"}

    def test_returns_compatibility_dict_when_installed(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "1.22.0"
        result = manager.get_harness_compatibility()
        assert result["status"] == "compatible"
        assert result["version"] == "1.22.0"
        assert "harness" in result

    def test_harness_contains_expected_keys(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "1.22.0"
        result = manager.get_harness_compatibility()
        harness = result["harness"]
        assert "go.cty" in harness
        assert "go.rpc" in harness
        assert "go.wire" in harness
        assert "go.hcl" in harness


class TestCompatibilityChecks(FoundationTestCase):
    """Tests for GoManager compatibility check methods."""

    def test_cty_compatible_with_118(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_cty_compatibility("1.18.0")
        assert result["compatible"] is True

    def test_cty_not_compatible_below_118(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_cty_compatibility("1.17.5")
        assert result["compatible"] is False

    def test_rpc_compatible_with_119(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_rpc_compatibility("1.19.0")
        assert result["compatible"] is True

    def test_rpc_not_compatible_below_119(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_rpc_compatibility("1.18.9")
        assert result["compatible"] is False

    def test_wire_compatible_with_118(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_wire_compatibility("1.18.0")
        assert result["compatible"] is True

    def test_wire_not_compatible_below_118(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_wire_compatibility("1.17.0")
        assert result["compatible"] is False

    def test_hcl_compatible_with_118(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_hcl_compatibility("1.18.0")
        assert result["compatible"] is True

    def test_hcl_not_compatible_below_118(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_go_hcl_compatibility("1.17.13")
        assert result["compatible"] is False

    def test_all_checks_include_notes(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        for method in [
            manager._check_go_cty_compatibility,
            manager._check_go_rpc_compatibility,
            manager._check_go_wire_compatibility,
            manager._check_go_hcl_compatibility,
        ]:
            result = method("1.22.0")
            assert "notes" in result


class TestVersionCompare(FoundationTestCase):
    """Tests for GoManager._version_compare."""

    def test_equal_versions_return_zero(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._version_compare("1.22.0", "1.22.0") == 0

    def test_greater_version_returns_one(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._version_compare("1.22.0", "1.21.0") == 1

    def test_lesser_version_returns_minus_one(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._version_compare("1.17.0", "1.18.0") == -1

    def test_patch_version_comparison(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._version_compare("1.22.3", "1.22.1") == 1
        assert manager._version_compare("1.22.0", "1.22.1") == -1

    def test_major_version_dominates(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._version_compare("2.0.0", "1.99.99") == 1


class TestGetGoRootAndGoPath(FoundationTestCase):
    """Tests for GoManager.get_goroot and get_gopath."""

    def test_get_goroot_returns_expected_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_goroot("1.22.0")
        assert result == manager.install_path / "go" / "1.22.0" / "go"

    def test_get_gopath_returns_expected_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_gopath("1.22.0")
        assert result == manager.install_path / "go" / "1.22.0" / "gopath"

    def test_get_goroot_is_pathlib_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_goroot("1.22.0")
        assert isinstance(result, pathlib.Path)

    def test_get_gopath_is_pathlib_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_gopath("1.22.0")
        assert isinstance(result, pathlib.Path)

    def test_get_goroot_version_specific(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        r1 = manager.get_goroot("1.21.0")
        r2 = manager.get_goroot("1.22.0")
        assert r1 != r2

    def test_get_gopath_version_specific(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        p1 = manager.get_gopath("1.21.0")
        p2 = manager.get_gopath("1.22.0")
        assert p1 != p2


# 🧰🌍🔚
