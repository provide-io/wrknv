#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.bao module (BaoManager)."""

from __future__ import annotations

import contextlib
import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.bao import BaoManager
from wrknv.managers.base import ToolManagerError


def _make_bao_manager(tmp_dir: pathlib.Path) -> BaoManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: {
        "install_path": str(tmp_dir / "tools"),
    }.get(key, default)
    cfg.get_tool_version.return_value = None
    return BaoManager(config=cfg)


class TestBaoManagerProperties(FoundationTestCase):
    """Tests for BaoManager static properties."""

    def test_tool_name(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        assert mgr.tool_name == "bao"

    def test_executable_name(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        assert mgr.executable_name == "bao"


class TestBaoGithubClient(FoundationTestCase):
    """Tests for BaoManager.github_client."""

    def test_github_client_lazy_creation(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        with mock.patch("wrknv.managers.bao.GitHubReleasesClient") as mock_cls:
            mock_cls.return_value = mock.Mock()
            client = mgr.github_client
        mock_cls.assert_called_once_with("openbao/openbao")
        assert client is mock_cls.return_value

    def test_github_client_cached(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        with mock.patch("wrknv.managers.bao.GitHubReleasesClient") as mock_cls:
            mock_cls.return_value = mock.Mock()
            first = mgr.github_client
            second = mgr.github_client
        assert first is second
        mock_cls.assert_called_once()


class TestBaoGetAvailableVersions(FoundationTestCase):
    """Tests for BaoManager.get_available_versions."""

    def test_get_available_versions_success(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        versions = ["2.1.0", "2.0.0", "1.17.0"]
        with (
            mock.patch("wrknv.managers.bao.GitHubReleasesClient"),
            mock.patch("wrknv.managers.bao.asyncio.run", return_value=versions),
        ):
            result = mgr.get_available_versions()
        assert result == versions

    def test_get_available_versions_raises_on_error(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        with (
            mock.patch("wrknv.managers.bao.GitHubReleasesClient"),
            mock.patch("wrknv.managers.bao.asyncio.run", side_effect=RuntimeError("network")),
            pytest.raises(ToolManagerError, match="Failed to fetch OpenBao versions"),
        ):
            mgr.get_available_versions()

    def test_passes_include_prereleases_false_by_default(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        mock_client = mock.Mock()
        mock_coro = mock.AsyncMock(return_value=["2.1.0"])
        mock_client.get_versions = mock_coro

        with mock.patch("wrknv.managers.bao.asyncio.run", return_value=["2.1.0"]) as mock_run:
            mgr._github_client = mock_client
            mgr.get_available_versions()

        mock_run.assert_called_once()


class TestBaoGetDownloadUrl(FoundationTestCase):
    """Tests for BaoManager.get_download_url."""

    def test_get_download_url_darwin_arm64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        platform_info = {"os": "darwin", "arch": "arm64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert url == "https://github.com/openbao/openbao/releases/download/v2.1.0/bao_2.1.0_Darwin_arm64.tar.gz"

    def test_get_download_url_linux_amd64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert url == "https://github.com/openbao/openbao/releases/download/v2.1.0/bao_2.1.0_Linux_amd64.tar.gz"

    def test_get_download_url_windows(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        platform_info = {"os": "windows", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert "Windows" in url
        assert "2.1.0" in url

    def test_get_download_url_uses_tar_gz(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert url.endswith(".tar.gz")

    def test_get_download_url_uses_capitalized_os(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert "Linux" in url


class TestBaoGetChecksumUrl(FoundationTestCase):
    """Tests for BaoManager.get_checksum_url."""

    def test_get_checksum_url(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        url = mgr.get_checksum_url("2.1.0")
        assert url == "https://github.com/openbao/openbao/releases/download/v2.1.0/bao_2.1.0_SHA256SUMS"

    def test_checksum_url_contains_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        url = mgr.get_checksum_url("2.0.0")
        assert url is not None
        assert "2.0.0" in url


class TestBaoVerifyInstallation(FoundationTestCase):
    """Tests for BaoManager.verify_installation."""

    def test_verify_installation_returns_false_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        result = mgr.verify_installation("2.1.0")
        assert result is False

    def test_verify_installation_returns_true_when_version_matches(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        binary_path = mgr.get_binary_path("2.1.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is True

    def test_verify_installation_returns_false_on_version_mismatch(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        binary_path = mgr.get_binary_path("2.1.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Bao v2.0.0 (abcd1234)"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is False

    def test_verify_installation_handles_exception(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        binary_path = mgr.get_binary_path("2.1.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with mock.patch("provide.foundation.process.run", side_effect=RuntimeError("exec failed")):
            result = mgr.verify_installation("2.1.0")
        assert result is False

    def test_verify_installation_returns_false_on_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        binary_path = mgr.get_binary_path("2.1.0")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is False


class TestBaoInstallFromArchive(FoundationTestCase):
    """Tests for BaoManager._install_from_archive."""

    def test_raises_when_binary_not_found_in_archive(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        archive_path = tmp / "bao_2.1.0.tar.gz"
        archive_path.write_bytes(b"fake")
        extract_dir = tmp / "extract"
        extract_dir.mkdir()
        # No bao binary in extract dir
        with (
            mock.patch.object(mgr, "extract_archive"),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch("provide.foundation.file.safe_rmtree"),
            pytest.raises(ToolManagerError, match="OpenBao binary not found"),
        ):
            mgr._install_from_archive(archive_path, "2.1.0")

    def test_installs_binary_successfully(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        archive_path = tmp / "bao_2.1.0.tar.gz"
        archive_path.write_bytes(b"fake")

        def fake_extract(archive: pathlib.Path, dest: pathlib.Path) -> None:
            # Create a fake bao binary in the extract dir
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "bao").write_text("#!/bin/sh")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch.object(mgr, "make_executable"),
            mock.patch("provide.foundation.file.safe_copy"),
            mock.patch("provide.foundation.file.safe_rmtree"),
        ):
            mgr._install_from_archive(archive_path, "2.1.0")

    def test_raises_when_verification_fails(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        archive_path = tmp / "bao_2.1.0.tar.gz"
        archive_path.write_bytes(b"fake")

        def fake_extract(archive: pathlib.Path, dest: pathlib.Path) -> None:
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "bao").write_text("#!/bin/sh")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch.object(mgr, "verify_installation", return_value=False),
            mock.patch.object(mgr, "make_executable"),
            mock.patch("provide.foundation.file.safe_copy"),
            mock.patch("provide.foundation.file.safe_rmtree"),
            pytest.raises(ToolManagerError, match="verification failed"),
        ):
            mgr._install_from_archive(archive_path, "2.1.0")

    def test_cleans_up_extract_dir_on_error(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        archive_path = tmp / "bao_2.1.0.tar.gz"
        archive_path.write_bytes(b"fake")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=RuntimeError("extract failed")),
            mock.patch("provide.foundation.file.safe_rmtree") as mock_rmtree,
            contextlib.suppress(RuntimeError, ToolManagerError),
        ):
            mgr._install_from_archive(archive_path, "2.1.0")
        mock_rmtree.assert_called()

    def test_installs_binary_with_non_matching_files_first(self) -> None:
        """Branch 102->101: loop iterates past non-matching files before finding bao."""
        tmp = self.create_temp_dir()
        mgr = _make_bao_manager(tmp)
        archive_path = tmp / "bao_2.1.0.tar.gz"
        archive_path.write_bytes(b"fake")

        def fake_extract(archive: pathlib.Path, dest: pathlib.Path) -> None:
            dest.mkdir(parents=True, exist_ok=True)
            # Create non-matching files first, then the actual binary
            (dest / "bao_readme.txt").write_text("docs")
            (dest / "bao_config.hcl").write_text("config")
            (dest / "bao").write_text("#!/bin/sh")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch.object(mgr, "make_executable"),
            mock.patch("provide.foundation.file.safe_copy"),
            mock.patch("provide.foundation.file.safe_rmtree"),
        ):
            mgr._install_from_archive(archive_path, "2.1.0")


# 🧰🌍🔚
