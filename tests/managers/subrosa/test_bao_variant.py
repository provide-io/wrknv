#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.subrosa.bao module (BaoVariant)."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.subrosa.bao import BaoVariant


def _make_bao_variant(tmp_dir: pathlib.Path) -> BaoVariant:
    """Create a BaoVariant with all paths redirected to tmp_dir."""
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: default
    cfg.get_tool_version.return_value = None
    cfg.install_path = str(tmp_dir / "tools")

    with (
        mock.patch("wrknv.managers.subrosa.base.get_workenv_bin_dir", return_value=tmp_dir / "bin"),
        mock.patch.object(pathlib.Path, "mkdir"),
    ):
        mgr = BaoVariant(config=cfg)

    mgr.install_path = tmp_dir / "subrosa"
    mgr.install_path.mkdir(parents=True, exist_ok=True)
    mgr.metadata_file = mgr.install_path / "metadata.json"
    mgr.metadata = {}
    mgr.cache_dir = tmp_dir / "cache"
    mgr.cache_dir.mkdir(parents=True, exist_ok=True)
    mgr.workenv_bin_dir = tmp_dir / "bin"
    (tmp_dir / "bin").mkdir(parents=True, exist_ok=True)
    return mgr


class TestBaoVariantName(FoundationTestCase):
    """Tests for BaoVariant.variant_name."""

    def test_variant_name_is_bao(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        assert mgr.variant_name == "bao"


class TestBaoGithubClient(FoundationTestCase):
    """Tests for BaoVariant.github_client."""

    def test_github_client_lazy_creation(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        with mock.patch("wrknv.managers.subrosa.bao.GitHubReleasesClient") as mock_cls:
            mock_cls.return_value = mock.Mock()
            client = mgr.github_client
        mock_cls.assert_called_once_with("openbao/openbao")
        assert client is mock_cls.return_value

    def test_github_client_cached(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        with mock.patch("wrknv.managers.subrosa.bao.GitHubReleasesClient") as mock_cls:
            mock_cls.return_value = mock.Mock()
            first = mgr.github_client
            second = mgr.github_client
        assert first is second
        mock_cls.assert_called_once()


class TestBaoGetAvailableVersions(FoundationTestCase):
    """Tests for BaoVariant.get_available_versions."""

    def test_get_available_versions_success(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        versions = ["2.1.0", "2.0.0", "1.17.0"]
        with (
            mock.patch("wrknv.managers.subrosa.bao.GitHubReleasesClient"),
            mock.patch("wrknv.managers.subrosa.bao.asyncio.run", return_value=versions),
        ):
            result = mgr.get_available_versions()
        assert result == versions

    def test_get_available_versions_raises_on_error(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        with (
            mock.patch("wrknv.managers.subrosa.bao.GitHubReleasesClient"),
            mock.patch("wrknv.managers.subrosa.bao.asyncio.run", side_effect=RuntimeError("network")),
            pytest.raises(ToolManagerError, match="Failed to fetch OpenBao versions"),
        ):
            mgr.get_available_versions()

    def test_passes_include_prereleases_setting(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        mgr.config.get_setting.side_effect = lambda key, default=None: (
            True if key == "include_prereleases" else default
        )
        mock_client = mock.Mock()
        mock_coro = mock.AsyncMock(return_value=["2.1.0"])
        mock_client.get_versions = mock_coro

        with (
            mock.patch("wrknv.managers.subrosa.bao.asyncio.run", return_value=["2.1.0"]) as mock_run,
        ):
            mgr._github_client = mock_client
            mgr.get_available_versions()

        mock_run.assert_called_once()


class TestBaoGetDownloadUrl(FoundationTestCase):
    """Tests for BaoVariant.get_download_url."""

    def test_get_download_url_darwin_arm64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        platform_info = {"os": "darwin", "arch": "arm64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert (
            url == "https://github.com/openbao/openbao/releases/download/v2.1.0/bao_2.1.0_Darwin_arm64.tar.gz"
        )

    def test_get_download_url_linux_amd64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.1.0")
        assert (
            url == "https://github.com/openbao/openbao/releases/download/v2.1.0/bao_2.1.0_Linux_amd64.tar.gz"
        )

    def test_uses_capitalized_os_name(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("2.0.0")
        assert "Linux" in url


class TestBaoGetChecksumUrl(FoundationTestCase):
    """Tests for BaoVariant.get_checksum_url."""

    def test_get_checksum_url(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        url = mgr.get_checksum_url("2.1.0")
        assert url == "https://github.com/openbao/openbao/releases/download/v2.1.0/bao_2.1.0_SHA256SUMS"

    def test_checksum_url_contains_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_bao_variant(tmp)
        url = mgr.get_checksum_url("2.0.0")
        assert "2.0.0" in url
        assert url is not None


# 🧰🌍🔚
