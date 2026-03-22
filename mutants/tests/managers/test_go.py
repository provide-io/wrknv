#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.go module."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.go import GoManager


def _make_manager(tmp_dir: pathlib.Path) -> GoManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: (
        str(tmp_dir / "tools") if key == "install_path" else default
    )
    cfg.get_tool_version.return_value = None
    cfg.install_path = str(tmp_dir / "tools")
    return GoManager(config=cfg)


class TestGoManagerProperties(FoundationTestCase):
    """Tests for GoManager static properties."""

    def test_tool_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.tool_name == "go"

    def test_executable_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.executable_name == "go"


class TestGetAvailableVersions(FoundationTestCase):
    """Tests for GoManager.get_available_versions."""

    def test_returns_stable_versions_by_default(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        api_data = [
            {"version": "go1.22.0", "stable": True},
            {"version": "go1.21.5", "stable": True},
        ]
        mock_response = mock.Mock()
        mock_response.json.return_value = api_data
        with mock.patch("wrknv.managers.go.asyncio.run", return_value=mock_response):
            result = manager.get_available_versions()
        assert result == ["1.22.0", "1.21.5"]

    def test_strips_go_prefix(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        api_data = [{"version": "go1.22.3", "stable": True}]
        mock_response = mock.Mock()
        mock_response.json.return_value = api_data
        with mock.patch("wrknv.managers.go.asyncio.run", return_value=mock_response):
            result = manager.get_available_versions()
        assert "1.22.3" in result
        assert "go1.22.3" not in result

    def test_skips_unstable_by_default(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        api_data = [
            {"version": "go1.23rc1", "stable": False},
            {"version": "go1.22.0", "stable": True},
        ]
        mock_response = mock.Mock()
        mock_response.json.return_value = api_data
        with mock.patch("wrknv.managers.go.asyncio.run", return_value=mock_response):
            result = manager.get_available_versions()
        assert "1.22.0" in result
        assert "1.23rc1" not in result

    def test_includes_unstable_when_configured(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: (
            True if key == "include_prereleases" else default
        )
        api_data = [
            {"version": "go1.23rc1", "stable": False},
            {"version": "go1.22.0", "stable": True},
        ]
        mock_response = mock.Mock()
        mock_response.json.return_value = api_data
        with mock.patch("wrknv.managers.go.asyncio.run", return_value=mock_response):
            result = manager.get_available_versions()
        assert "1.23rc1" in result
        assert "1.22.0" in result

    def test_raises_tool_manager_error_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch("wrknv.managers.go.asyncio.run", side_effect=RuntimeError("connection refused")),
            pytest.raises(ToolManagerError, match="Failed to fetch Go versions"),
        ):
            manager.get_available_versions()

    def test_skips_entries_without_go_prefix(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        api_data = [
            {"version": "go1.22.0", "stable": True},
            {"version": "v1.0.0", "stable": True},  # no "go" prefix
        ]
        mock_response = mock.Mock()
        mock_response.json.return_value = api_data
        with mock.patch("wrknv.managers.go.asyncio.run", return_value=mock_response):
            result = manager.get_available_versions()
        assert "1.22.0" in result
        # v1.0.0 doesn't start with "go" so it's skipped
        assert "v1.0.0" not in result


class TestGetDownloadUrl(FoundationTestCase):
    """Tests for GoManager.get_download_url."""

    def _get_url(self, manager: GoManager, os_name: str, arch: str, version: str = "1.22.0") -> str:
        with mock.patch.object(manager, "get_platform_info", return_value={"os": os_name, "arch": arch}):
            return manager.get_download_url(version)

    def test_linux_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "amd64")
        assert "go1.22.0.linux-amd64.tar.gz" in url

    def test_darwin_arm64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "darwin", "arm64")
        assert "go1.22.0.darwin-arm64.tar.gz" in url

    def test_windows_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "windows", "amd64")
        assert "go1.22.0.windows-amd64.tar.gz" in url

    def test_default_mirror_is_go_dev(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "amd64")
        assert url.startswith("https://go.dev/dl/")

    def test_custom_mirror_used_when_configured(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: (
            "https://mirror.example.com/go" if key == "go_mirror" else default
        )
        url = self._get_url(manager, "linux", "amd64")
        assert url.startswith("https://mirror.example.com/go/")

    def test_custom_mirror_trailing_slash_normalized(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: (
            "https://mirror.example.com/go/" if key == "go_mirror" else default
        )
        url = self._get_url(manager, "linux", "amd64")
        # Should not produce double slashes
        assert "//" not in url.replace("https://", "")

    def test_url_contains_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "amd64", version="1.21.5")
        assert "1.21.5" in url


class TestGetChecksumUrl(FoundationTestCase):
    """Tests for GoManager.get_checksum_url."""

    def test_returns_none(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.get_checksum_url("1.22.0") is None


class TestInstallFromArchive(FoundationTestCase):
    """Tests for GoManager._install_from_archive."""

    def test_raises_when_go_dir_not_in_archive(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "go1.22.0.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            (dst / "something_else").mkdir()

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch("provide.foundation.file.safe_rmtree"),
            pytest.raises(ToolManagerError, match="Go directory not found"),
        ):
            manager._install_from_archive(archive_path, "1.22.0")

    def test_raises_when_go_binary_not_in_extracted_go_dir(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "go1.22.0.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            go_dir = dst / "go"
            go_dir.mkdir()
            (go_dir / "bin").mkdir()
            # no go binary inside bin/

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch("provide.foundation.file.safe_move"),
            mock.patch("provide.foundation.file.safe_rmtree"),
            pytest.raises(ToolManagerError, match="Go binary not found"),
        ):
            manager._install_from_archive(archive_path, "1.22.0")

    def test_installs_and_verifies_successfully(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "go1.22.0.tar.gz"
        archive_path.write_bytes(b"")

        extract_dir_holder: list[pathlib.Path] = []

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            extract_dir_holder.append(dst)
            go_dir = dst / "go"
            go_bin = go_dir / "bin"
            go_bin.mkdir(parents=True)
            (go_bin / "go").write_text("#!/bin/sh")

        def fake_move(src: pathlib.Path, dst: pathlib.Path) -> None:
            # simulate move: create dst with go binary
            (dst / "bin").mkdir(parents=True, exist_ok=True)
            (dst / "bin" / "go").write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch("provide.foundation.file.safe_move", side_effect=fake_move),
            mock.patch("provide.foundation.file.safe_rmtree"),
            mock.patch.object(manager, "verify_installation", return_value=True),
        ):
            manager._install_from_archive(archive_path, "1.22.0")

    def test_raises_when_verify_fails(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "go1.22.0.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            go_dir = dst / "go"
            go_bin = go_dir / "bin"
            go_bin.mkdir(parents=True)
            (go_bin / "go").write_text("#!/bin/sh")

        def fake_move(src: pathlib.Path, dst: pathlib.Path) -> None:
            (dst / "bin").mkdir(parents=True, exist_ok=True)
            (dst / "bin" / "go").write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch("provide.foundation.file.safe_move", side_effect=fake_move),
            mock.patch("provide.foundation.file.safe_rmtree"),
            mock.patch.object(manager, "verify_installation", return_value=False),
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            manager._install_from_archive(archive_path, "1.22.0")

    def test_cleans_up_extract_dir_on_success(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "go1.22.0.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            go_dir = dst / "go"
            go_bin = go_dir / "bin"
            go_bin.mkdir(parents=True)
            (go_bin / "go").write_text("#!/bin/sh")

        def fake_move(src: pathlib.Path, dst: pathlib.Path) -> None:
            (dst / "bin").mkdir(parents=True, exist_ok=True)
            (dst / "bin" / "go").write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch("provide.foundation.file.safe_move", side_effect=fake_move),
            mock.patch("provide.foundation.file.safe_rmtree") as mock_rmtree,
            mock.patch.object(manager, "verify_installation", return_value=True),
        ):
            manager._install_from_archive(archive_path, "1.22.0")
        mock_rmtree.assert_called_once()

    def test_cleans_up_extract_dir_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "go1.22.0.tar.gz"
        archive_path.write_bytes(b"")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=RuntimeError("corrupt archive")),
            mock.patch("provide.foundation.file.safe_rmtree") as mock_rmtree,
            pytest.raises(RuntimeError),
        ):
            manager._install_from_archive(archive_path, "1.22.0")
        mock_rmtree.assert_called_once()


# 🧰🌍🔚
