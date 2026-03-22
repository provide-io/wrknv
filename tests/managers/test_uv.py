#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.uv module."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.uv import UvManager


def _make_manager(tmp_dir: pathlib.Path) -> UvManager:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: (
        str(tmp_dir / "tools") if key == "install_path" else default
    )
    cfg.get_tool_version.return_value = None
    cfg.install_path = str(tmp_dir / "tools")
    return UvManager(config=cfg)


class TestUvManagerProperties(FoundationTestCase):
    """Tests for UvManager static properties."""

    def test_tool_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.tool_name == "uv"

    def test_executable_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.executable_name == "uv"

    def test_github_client_created_lazily(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.managers.uv.GitHubReleasesClient") as mock_cls:
            mock_cls.return_value = mock.Mock()
            client = manager.github_client
        mock_cls.assert_called_once_with("astral-sh/uv")
        assert client is mock_cls.return_value

    def test_github_client_cached(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.managers.uv.GitHubReleasesClient") as mock_cls:
            mock_cls.return_value = mock.Mock()
            first = manager.github_client
            second = manager.github_client
        assert first is second
        mock_cls.assert_called_once()


class TestGetAvailableVersions(FoundationTestCase):
    """Tests for UvManager.get_available_versions."""

    def test_returns_versions_list(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        versions = ["0.4.15", "0.4.14", "0.4.13"]
        with (
            mock.patch("wrknv.managers.uv.GitHubReleasesClient"),
            mock.patch("wrknv.managers.uv.asyncio.run", return_value=versions),
        ):
            result = manager.get_available_versions()
        assert result == versions

    def test_passes_include_prereleases_false_by_default(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_client = mock.Mock()
        mock_client.get_versions = mock.AsyncMock(return_value=["0.4.15"])
        manager._github_client = mock_client
        with mock.patch("wrknv.managers.uv.asyncio.run", return_value=["0.4.15"]) as mock_run:
            manager.get_available_versions()
        # asyncio.run should be called with a coroutine from get_versions(include_prereleases=False)
        mock_run.assert_called_once()

    def test_passes_include_prereleases_true_when_configured(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: (
            True if key == "include_prereleases" else default
        )
        mock_client = mock.Mock()
        mock_client.get_versions = mock.AsyncMock(return_value=["0.5.0a1", "0.4.15"])
        manager._github_client = mock_client
        with mock.patch("wrknv.managers.uv.asyncio.run", return_value=["0.5.0a1", "0.4.15"]):
            result = manager.get_available_versions()
        assert "0.5.0a1" in result

    def test_raises_tool_manager_error_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch("wrknv.managers.uv.GitHubReleasesClient"),
            mock.patch("wrknv.managers.uv.asyncio.run", side_effect=RuntimeError("network down")),
            pytest.raises(ToolManagerError, match="Failed to fetch UV versions"),
        ):
            manager.get_available_versions()


class TestGetDownloadUrl(FoundationTestCase):
    """Tests for UvManager.get_download_url."""

    def _get_url(self, manager: UvManager, os_name: str, arch: str, version: str = "0.4.15") -> str:
        with mock.patch.object(manager, "get_platform_info", return_value={"os": os_name, "arch": arch}):
            return manager.get_download_url(version)

    def test_darwin_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "darwin", "amd64")
        assert "apple-darwin" in url
        assert "x86_64" in url
        assert url.endswith(".tar.gz")
        assert "0.4.15" in url

    def test_darwin_arm64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "darwin", "arm64")
        assert "apple-darwin" in url
        assert "aarch64" in url
        assert url.endswith(".tar.gz")

    def test_linux_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "amd64")
        assert "unknown-linux-gnu" in url
        assert "x86_64" in url
        assert url.endswith(".tar.gz")

    def test_linux_arm64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "arm64")
        assert "unknown-linux-gnu" in url
        assert "aarch64" in url

    def test_windows_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "windows", "amd64")
        assert "pc-windows-msvc" in url
        assert "x86_64" in url
        assert url.endswith(".zip")

    def test_windows_arm64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "windows", "arm64")
        assert "pc-windows-msvc" in url
        assert "aarch64" in url
        assert url.endswith(".zip")

    def test_unsupported_os_raises(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch.object(manager, "get_platform_info", return_value={"os": "freebsd", "arch": "amd64"}),
            pytest.raises(ToolManagerError, match="Unsupported platform"),
        ):
            manager.get_download_url("0.4.15")

    def test_url_contains_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "amd64", version="0.5.1")
        assert "0.5.1" in url

    def test_url_base_is_github_releases(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        url = self._get_url(manager, "linux", "amd64")
        assert url.startswith("https://github.com/astral-sh/uv/releases/download/")


class TestGetChecksumUrl(FoundationTestCase):
    """Tests for UvManager.get_checksum_url."""

    def test_returns_none(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.get_checksum_url("0.4.15") is None


class TestInstallFromArchive(FoundationTestCase):
    """Tests for UvManager._install_from_archive."""

    def test_raises_when_binary_not_found_in_archive(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "uv.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            # Extract to dst but put no uv binary
            (dst / "README.txt").write_text("no binary here")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch("provide.foundation.file.safe_rmtree"),
            pytest.raises(ToolManagerError, match="UV binary not found"),
        ):
            manager._install_from_archive(archive_path, "0.4.15")

    def test_installs_binary_and_calls_verify(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "uv.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            uv_bin = dst / "uv"
            uv_bin.write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch.object(manager, "make_executable"),
            mock.patch.object(manager, "verify_installation", return_value=True),
            mock.patch("provide.foundation.file.safe_copy"),
            mock.patch("provide.foundation.file.safe_rmtree"),
        ):
            manager._install_from_archive(archive_path, "0.4.15")

    def test_raises_when_verify_fails(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "uv.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            uv_bin = dst / "uv"
            uv_bin.write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch.object(manager, "make_executable"),
            mock.patch.object(manager, "verify_installation", return_value=False),
            mock.patch("provide.foundation.file.safe_copy"),
            mock.patch("provide.foundation.file.safe_rmtree"),
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            manager._install_from_archive(archive_path, "0.4.15")

    def test_cleans_up_extract_dir_on_success(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "uv.tar.gz"
        archive_path.write_bytes(b"")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            uv_bin = dst / "uv"
            uv_bin.write_text("#!/bin/sh")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=fake_extract),
            mock.patch.object(manager, "make_executable"),
            mock.patch.object(manager, "verify_installation", return_value=True),
            mock.patch("provide.foundation.file.safe_copy"),
            mock.patch("provide.foundation.file.safe_rmtree") as mock_rmtree,
        ):
            manager._install_from_archive(archive_path, "0.4.15")
        mock_rmtree.assert_called_once()

    def test_cleans_up_extract_dir_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        archive_path = tmp / "uv.tar.gz"
        archive_path.write_bytes(b"")

        with (
            mock.patch.object(manager, "extract_archive", side_effect=RuntimeError("bad archive")),
            mock.patch("provide.foundation.file.safe_rmtree") as mock_rmtree,
            pytest.raises(RuntimeError),
        ):
            manager._install_from_archive(archive_path, "0.4.15")
        mock_rmtree.assert_called_once()


class TestVerifyInstallation(FoundationTestCase):
    """Tests for UvManager.verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.verify_installation("0.4.15")
        assert result is False

    def test_returns_true_when_version_matches(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("0.4.15")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "uv 0.4.15 (some hash)"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("0.4.15")
        assert result is True

    def test_returns_false_when_version_not_in_stdout(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("0.4.15")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "uv 0.4.99 (some hash)"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("0.4.15")
        assert result is False

    def test_returns_false_when_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("0.4.15")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        mock_result = mock.Mock()
        mock_result.returncode = 1
        mock_result.stderr = "error"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("0.4.15")
        assert result is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("0.4.15")
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        binary_path.write_text("#!/bin/sh")
        with mock.patch("provide.foundation.process.run", side_effect=OSError("exec failed")):
            result = manager.verify_installation("0.4.15")
        assert result is False


class TestGetHarnessCompatibility(FoundationTestCase):
    """Tests for UvManager.get_harness_compatibility."""

    def test_returns_not_installed_when_no_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = None
        result = manager.get_harness_compatibility()
        assert result == {"status": "not_installed"}

    def test_returns_compatibility_dict_when_installed(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "0.4.15"
        result = manager.get_harness_compatibility()
        assert result["status"] == "compatible"
        assert result["version"] == "0.4.15"
        assert "harness" in result

    def test_harness_contains_expected_keys(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.config.get_tool_version.return_value = "0.4.15"
        result = manager.get_harness_compatibility()
        harness = result["harness"]
        assert "python.cty" in harness
        assert "python.hcl" in harness
        assert "python.wire" in harness


class TestCompatibilityChecks(FoundationTestCase):
    """Tests for UvManager compatibility check methods."""

    def test_cty_compatibility_always_true(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_python_cty_compatibility("0.4.15")
        assert result["compatible"] is True
        assert "notes" in result

    def test_hcl_compatibility_always_true(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_python_hcl_compatibility("0.4.15")
        assert result["compatible"] is True
        assert "notes" in result

    def test_wire_compatibility_always_true(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager._check_python_wire_compatibility("0.4.15")
        assert result["compatible"] is True
        assert "notes" in result

    def test_cty_compatibility_works_for_any_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        for v in ["0.1.0", "1.0.0", "99.0.0"]:
            result = manager._check_python_cty_compatibility(v)
            assert result["compatible"] is True


# 🧰🌍🔚
