#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.base module - cleanup, install_latest, list, show_current, versions, verify."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import BaseToolManager, ToolManagerError


class FakeToolManager(BaseToolManager):
    """Concrete subclass for testing BaseToolManager."""

    @property
    def tool_name(self) -> str:
        return "faketool"

    @property
    def executable_name(self) -> str:
        return "faketool"

    def get_available_versions(self) -> list[str]:
        return ["2.0.0", "1.1.0", "1.0.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://fake.example.com/faketool/{version}/faketool.tar.gz"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://fake.example.com/faketool/{version}/checksums.txt"

    def _install_from_archive(self, archive_path: pathlib.Path, version: str) -> None:
        pass


def _make_manager(tmp_dir: pathlib.Path) -> FakeToolManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: {
        "install_path": str(tmp_dir / "tools"),
    }.get(key, default)
    cfg.get_tool_version.return_value = None
    return FakeToolManager(config=cfg)


class TestCleanupFailedInstallation(FoundationTestCase):
    """Tests for _cleanup_failed_installation."""

    def test_removes_tool_dir_if_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        tool_dir = manager.install_path / "faketool" / "1.0.0"
        tool_dir.mkdir(parents=True)
        manager._cleanup_failed_installation("1.0.0")
        assert not tool_dir.exists()

    def test_no_error_when_dir_not_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager._cleanup_failed_installation("1.0.0")  # Should not raise


class TestInstallLatest(FoundationTestCase):
    """Tests for install_latest."""

    def test_installs_first_available_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager, "install_version") as mock_iv:
            manager.install_latest()
        mock_iv.assert_called_once_with("2.0.0", dry_run=False)

    def test_raises_when_no_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch.object(manager, "get_available_versions", return_value=[]),
            pytest.raises(ToolManagerError, match="No versions available"),
        ):
            manager.install_latest()

    def test_dry_run_passed_through(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager, "install_version") as mock_iv:
            manager.install_latest(dry_run=True)
        mock_iv.assert_called_once_with("2.0.0", dry_run=True)


class TestListVersions(FoundationTestCase):
    """Tests for list_versions."""

    def test_lists_available_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.managers.base.pout"):
            manager.list_versions()  # Should not raise

    def test_raises_on_fetch_failure(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch.object(manager, "get_available_versions", side_effect=RuntimeError("network")),
            pytest.raises(ToolManagerError, match="Failed to fetch versions"),
        ):
            manager.list_versions()

    def test_shows_current_marker(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "2.0.0"
        with mock.patch("wrknv.managers.base.pout") as mock_pout:
            manager.list_versions()
        # At least one call should include "(current)"
        calls = [str(c) for c in mock_pout.call_args_list]
        assert any("current" in c for c in calls)


class TestShowCurrent(FoundationTestCase):
    """Tests for show_current."""

    def test_shows_not_installed_when_no_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = None
        with mock.patch("wrknv.managers.base.pout") as mock_pout:
            manager.show_current()
        calls = [str(c) for c in mock_pout.call_args_list]
        assert any("not installed" in c for c in calls)

    def test_shows_version_and_missing_binary(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "1.0.0"
        with mock.patch("wrknv.managers.base.pout") as mock_pout:
            manager.show_current()
        calls = [str(c) for c in mock_pout.call_args_list]
        assert any("1.0.0" in c for c in calls)

    def test_shows_installed_path_when_binary_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "1.0.0"
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with mock.patch("wrknv.managers.base.pout") as mock_pout:
            manager.show_current()
        calls = [str(c) for c in mock_pout.call_args_list]
        assert any("1.0.0" in c for c in calls)


class TestGetInstalledVersions(FoundationTestCase):
    """Tests for get_installed_versions."""

    def test_returns_empty_when_no_tool_dir(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_installed_versions()
        assert result == []

    def test_returns_version_dirs(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        tool_dir = manager.install_path / "faketool"
        (tool_dir / "1.0.0").mkdir(parents=True)
        (tool_dir / "2.0.0").mkdir(parents=True)
        result = manager.get_installed_versions()
        assert "1.0.0" in result
        assert "2.0.0" in result

    def test_excludes_non_version_dirs(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        tool_dir = manager.install_path / "faketool"
        (tool_dir / "1.0.0").mkdir(parents=True)
        (tool_dir / "cache").mkdir(parents=True)
        result = manager.get_installed_versions()
        assert "cache" not in result

    def test_returns_sorted_descending(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        tool_dir = manager.install_path / "faketool"
        for v in ["1.0.0", "2.0.0", "1.5.0"]:
            (tool_dir / v).mkdir(parents=True)
        result = manager.get_installed_versions()
        assert result == sorted(result, reverse=True)


class TestIsVersionDir(FoundationTestCase):
    """Tests for _is_version_dir."""

    def test_returns_true_for_semver(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._is_version_dir("1.0.0") is True
        assert manager._is_version_dir("10.20.300") is True

    def test_returns_false_for_non_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager._is_version_dir("cache") is False
        assert manager._is_version_dir("bin") is False
        assert manager._is_version_dir("v1.0") is False


class TestRemoveVersion(FoundationTestCase):
    """Tests for remove_version."""

    def test_removes_version_dir(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version_dir = manager.install_path / "faketool" / "1.0.0"
        version_dir.mkdir(parents=True)
        manager.remove_version("1.0.0")
        assert not version_dir.exists()

    def test_no_error_when_version_dir_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.remove_version("9.9.9")  # Should not raise

    def test_clears_current_version_when_removing_current(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "1.0.0"
        with mock.patch.object(manager, "set_installed_version") as mock_siv:
            manager.remove_version("1.0.0")
        mock_siv.assert_called_with("")


class TestVerifyInstallation(FoundationTestCase):
    """Tests for verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.verify_installation("1.0.0")
        assert result is False

    def test_returns_true_when_binary_runs_successfully(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh\necho 'faketool 1.0.0'")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        with mock.patch("wrknv.managers.base.run", return_value=mock_result):
            result = manager.verify_installation("1.0.0")
        assert result is True

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with mock.patch("wrknv.managers.base.run", side_effect=RuntimeError("exec failed")):
            result = manager.verify_installation("1.0.0")
        assert result is False

    def test_returns_false_when_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 1
        with mock.patch("wrknv.managers.base.run", return_value=mock_result):
            result = manager.verify_installation("1.0.0")
        assert result is False


# 🧰🌍🔚
