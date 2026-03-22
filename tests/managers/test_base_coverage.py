#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for managers.base module - uncovered branches."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase

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


def _make_manager(tmp_dir: pathlib.Path, settings: dict | None = None) -> FakeToolManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    base_settings = {"install_path": str(tmp_dir / "tools")}
    if settings:
        base_settings.update(settings)
    cfg.get_setting.side_effect = lambda key, default=None: base_settings.get(key, default)
    cfg.get_tool_version.return_value = None
    return FakeToolManager(config=cfg)


class TestInstallVersionCreateSymlink(FoundationTestCase):
    """Cover create_symlink branch in install_version."""

    def test_already_installed_creates_symlink_when_enabled(self) -> None:
        """Line 205: create_symlink called when already installed and create_symlinks=True."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, {"create_symlinks": True})
        version = "1.0.0"
        binary_path = manager.get_binary_path(version)
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with (
            mock.patch.object(manager, "set_installed_version"),
            mock.patch.object(manager, "create_symlink") as mock_symlink,
        ):
            manager.install_version(version)
        mock_symlink.assert_called_once_with(version)

    def test_install_creates_symlink_when_enabled(self) -> None:
        """Lines 231-232: create_symlink called after successful install when create_symlinks=True."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, {"create_symlinks": True, "cache_downloads": False})
        version = "1.0.0"
        with (
            mock.patch.object(manager, "download_file"),
            mock.patch.object(manager, "get_checksum_url", return_value=None),
            mock.patch.object(manager, "_install_from_archive"),
            mock.patch.object(manager, "set_installed_version"),
            mock.patch.object(manager, "create_symlink") as mock_symlink,
        ):
            manager.install_version(version)
        mock_symlink.assert_called_once_with(version)

    def test_install_calls_verify_checksum_when_url_exists(self) -> None:
        """Lines 220-222: _verify_download_checksum called when checksum_url + verify_checksums=True."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, {"create_symlinks": False, "cache_downloads": False, "verify_checksums": True})
        version = "1.0.0"
        with (
            mock.patch.object(manager, "download_file"),
            mock.patch.object(manager, "get_checksum_url", return_value="https://example.com/checksums.txt"),
            mock.patch.object(manager, "_verify_download_checksum") as mock_vdc,
            mock.patch.object(manager, "_install_from_archive"),
            mock.patch.object(manager, "set_installed_version"),
        ):
            manager.install_version(version)
        mock_vdc.assert_called_once()


class TestVerifyDownloadChecksum(FoundationTestCase):
    """Cover _verify_download_checksum method body."""

    def test_no_checksum_path_logs_warning_and_returns(self) -> None:
        """Line 251: when download_checksum_file returns None, log warning and return."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        download_path = tmp / "file.tar.gz"
        download_path.write_text("data")
        with mock.patch("wrknv.wenv.operations.download.download_checksum_file", return_value=None):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")
        # No exception means success

    def test_checksum_found_and_verified(self) -> None:
        """Lines 258-260: expected_checksum found and verify passes."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, {"verify_checksums": True})
        download_path = tmp / "file.tar.gz"
        download_path.write_text("data")
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("abc123  file.tar.gz\n")
        with (
            mock.patch("wrknv.wenv.operations.download.download_checksum_file", return_value=checksum_file),
            mock.patch("wrknv.wenv.operations.download.parse_checksum_file", return_value="abc123"),
            mock.patch.object(manager, "verify_checksum", return_value=True),
        ):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")

    def test_checksum_not_found_logs_warning(self) -> None:
        """Lines 262-263: expected_checksum is None → log warning."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        download_path = tmp / "file.tar.gz"
        download_path.write_text("data")
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("other-file.tar.gz: abc123\n")
        with (
            mock.patch("wrknv.wenv.operations.download.download_checksum_file", return_value=checksum_file),
            mock.patch("wrknv.wenv.operations.download.parse_checksum_file", return_value=None),
        ):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")

    def test_checksum_mismatch_raises(self) -> None:
        """Lines 260-261: verify fails → ToolManagerError raised."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, {"verify_checksums": True})
        download_path = tmp / "file.tar.gz"
        download_path.write_text("data")
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("badchecksum  file.tar.gz\n")
        import pytest

        with (
            mock.patch("wrknv.wenv.operations.download.download_checksum_file", return_value=checksum_file),
            mock.patch("wrknv.wenv.operations.download.parse_checksum_file", return_value="expected"),
            mock.patch.object(manager, "verify_checksum", return_value=False),
            pytest.raises(ToolManagerError, match="Checksum verification failed"),
        ):
            manager._verify_download_checksum(download_path, "https://example.com/checksums.txt")


class TestListVersionsExtraEntries(FoundationTestCase):
    """Cover list_versions pagination."""

    def test_shows_truncation_message_when_more_versions_exist(self) -> None:
        """Line 300: shows '... and N more' when len(versions) > limit."""
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        # FakeToolManager.get_available_versions returns 3 versions, limit=2 → shows truncation
        with mock.patch("wrknv.managers.base.pout") as mock_pout:
            manager.list_versions(limit=2)
        calls = " ".join(str(c) for c in mock_pout.call_args_list)
        assert "more" in calls


class TestRemoveVersionBinaryElsewhere(FoundationTestCase):
    """Cover remove_version when binary is in different dir."""

    def test_deletes_binary_when_outside_version_dir(self) -> None:
        """Line 349: safe_delete called when binary exists outside version_dir.

        Must mock get_binary_path to return a path NOT inside version_dir,
        otherwise mkdir(parents=True) also creates version_dir and rmtree deletes it.
        """
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        version = "1.0.0"
        # Create a binary in a separate location (not inside version_dir)
        external_binary = tmp / "bin" / "faketool"
        external_binary.parent.mkdir(parents=True, exist_ok=True)
        external_binary.write_text("#!/bin/sh")
        with (
            mock.patch.object(manager, "get_binary_path", return_value=external_binary),
            mock.patch.object(manager, "get_installed_version", return_value="other"),
        ):
            manager.remove_version(version)
        assert not external_binary.exists()


class TestDownloadFileAsync(FoundationTestCase):
    """Cover async download_file method (lines 142-144)."""

    def test_async_download_delegates(self) -> None:
        """Lines 142-144: download_file_async import and await."""
        import asyncio

        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        dest = tmp / "archive.tar.gz"

        async def fake_async(*_args: object, **_kwargs: object) -> None:
            pass

        with mock.patch("wrknv.wenv.operations.download.download_file_async", side_effect=fake_async) as mock_async:

            async def _run() -> None:
                await manager.download_file_async("https://example.com/f.tar.gz", dest)

            asyncio.run(_run())
        mock_async.assert_called_once()


# 🧰🌍🔚
