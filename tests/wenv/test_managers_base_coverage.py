#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.wenv.managers.base - uncovered branches."""

from __future__ import annotations

import pathlib
from unittest.mock import Mock, patch

from provide.testkit import FoundationTestCase

from wrknv.config import WorkenvConfig
from wrknv.wenv.managers.base import BaseToolManager


class FakeWenvToolManager(BaseToolManager):
    """Minimal concrete subclass for testing BaseToolManager."""

    @property
    def tool_name(self) -> str:
        return "faketool"

    @property
    def executable_name(self) -> str:
        return "faketool"

    def get_available_versions(self) -> list[str]:
        return ["1.0.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/faketool/{version}/faketool.tar.gz"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://example.com/faketool/{version}/checksums.txt"

    def _install_from_archive(self, archive_path: pathlib.Path, version: str) -> None:
        pass


def _make_mgr(tmp: pathlib.Path, cmd_option: bool = False) -> FakeWenvToolManager:
    cfg = Mock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda k, d=None: {
        "install_path": str(tmp / "tools"),
        "cache_downloads": False,
        "verify_checksums": False,
        "clean_on_failure": False,
    }.get(k, d)
    cfg.get_tool_version.return_value = None
    cfg.get_command_option = Mock(return_value=cmd_option)
    return FakeWenvToolManager(config=cfg)


class TestInstallVersionSymlinkBranches(FoundationTestCase):
    """Cover lines 193 and 220: create_symlink called when get_command_option=True."""

    def test_already_installed_calls_symlink_when_enabled(self) -> None:
        """Line 193: binary exists + create_symlinks=True → create_symlink called."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp, cmd_option=True)
        binary_path = mgr.get_binary_path("1.0.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")

        with (
            patch.object(mgr, "set_installed_version"),
            patch.object(mgr, "create_symlink") as mock_sym,
        ):
            mgr.install_version("1.0.0")

        mock_sym.assert_called_once_with("1.0.0")

    def test_fresh_install_calls_symlink_when_enabled(self) -> None:
        """Line 220: fresh install + create_symlinks=True → create_symlink called."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp, cmd_option=True)

        with (
            patch.object(mgr, "download_file"),
            patch.object(mgr, "_install_from_archive"),
            patch.object(mgr, "set_installed_version"),
            patch.object(mgr, "create_symlink") as mock_sym,
        ):
            mgr.install_version("1.0.0")

        mock_sym.assert_called_once_with("1.0.0")


class TestVerifyChecksumBranches(FoundationTestCase):
    """Cover lines 210 and 248->245 in _verify_download_checksum."""

    def test_verify_checksum_called_when_url_and_setting_true(self) -> None:
        """Line 210: checksum_url present + verify_checksums=True → _verify called."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        mgr.config.get_setting.side_effect = lambda k, d=None: {
            "install_path": str(tmp / "tools"),
            "cache_downloads": False,
            "verify_checksums": True,
            "clean_on_failure": False,
        }.get(k, d)

        with (
            patch.object(mgr, "download_file"),
            patch.object(mgr, "_verify_download_checksum") as mock_vdc,
            patch.object(mgr, "_install_from_archive"),
            patch.object(mgr, "set_installed_version"),
        ):
            mgr.install_version("1.0.0")

        mock_vdc.assert_called_once()

    def test_checksum_line_with_single_token_skipped(self) -> None:
        """Line 248->245: checksum file line has filename but only 1 token → loop continues."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        download_path = tmp / "faketool.tar.gz"
        download_path.write_bytes(b"data")
        # Create the checksum file in the manager's cache_dir (where the code will open it)
        checksum_path = mgr.cache_dir / "checksums.txt"
        # Line has only the filename (no checksum value) → parts splits to 1 element
        checksum_path.write_text("faketool.tar.gz\n")

        with patch.object(mgr, "download_file"):  # no-op: file already created above
            mgr._verify_download_checksum(download_path, "https://example.com/checksums.txt")
        # No exception means success (no checksum found → warning logged)


class TestRemoveVersionBranches(FoundationTestCase):
    """Cover lines 342 and 350 in remove_version."""

    def test_binary_outside_version_dir_is_unlinked(self) -> None:
        """Line 342: binary exists and is outside version_dir → unlinked."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        external_binary = tmp / "bin" / "faketool"
        external_binary.parent.mkdir(parents=True, exist_ok=True)
        external_binary.write_text("#!/bin/sh")

        with (
            patch.object(mgr, "get_binary_path", return_value=external_binary),
            patch.object(mgr, "get_installed_version", return_value="other"),
        ):
            mgr.remove_version("1.0.0")

        assert not external_binary.exists()

    def test_set_tool_version_exception_is_caught(self) -> None:
        """Line 350: config.set_tool_version raises → exception silently caught."""
        tmp = self.create_temp_dir()
        mgr = _make_mgr(tmp)
        mgr.config.set_tool_version = Mock(side_effect=AttributeError("no method"))

        with patch.object(mgr, "get_installed_version", return_value="1.0.0"):
            mgr.remove_version("1.0.0")  # Should not raise


# 🧰🌍🔚
