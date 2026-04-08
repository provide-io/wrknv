#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.subrosa.ibm module (IbmVaultVariant)."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.subrosa.ibm import IbmVaultVariant


def _make_ibm_vault(tmp_dir: pathlib.Path) -> IbmVaultVariant:
    """Create an IbmVaultVariant with all paths redirected to tmp_dir."""
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: default
    cfg.get_tool_version.return_value = None
    cfg.install_path = str(tmp_dir / "tools")

    with (
        mock.patch("wrknv.managers.subrosa.base.get_workenv_bin_dir", return_value=tmp_dir / "bin"),
        mock.patch.object(pathlib.Path, "mkdir"),
    ):
        mgr = IbmVaultVariant(config=cfg)

    mgr.install_path = tmp_dir / "subrosa"
    mgr.install_path.mkdir(parents=True, exist_ok=True)
    mgr.metadata_file = mgr.install_path / "metadata.json"
    mgr.metadata = {}
    mgr.cache_dir = tmp_dir / "cache"
    mgr.cache_dir.mkdir(parents=True, exist_ok=True)
    mgr.workenv_bin_dir = tmp_dir / "bin"
    (tmp_dir / "bin").mkdir(parents=True, exist_ok=True)
    return mgr


class TestIbmVaultVariantName(FoundationTestCase):
    """Tests for IbmVaultVariant.variant_name."""

    def test_variant_name_is_vault(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        assert mgr.variant_name == "vault"


class TestIbmVaultGetAvailableVersions(FoundationTestCase):
    """Tests for IbmVaultVariant.get_available_versions."""

    def _make_mock_response(self, versions: dict) -> mock.Mock:
        response = mock.Mock()
        response.json.return_value = {"versions": versions}
        return response

    def test_get_available_versions_filters_prereleases(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        versions_data = {
            "1.15.0": {},
            "1.15.0-rc1": {},
            "1.14.0": {},
            "1.15.0-beta1": {},
        }
        response = self._make_mock_response(versions_data)
        with mock.patch("wrknv.managers.subrosa.ibm.asyncio.run", return_value=response):
            result = mgr.get_available_versions()
        assert "1.15.0" in result
        assert "1.14.0" in result
        assert "1.15.0-rc1" not in result
        assert "1.15.0-beta1" not in result

    def test_get_available_versions_includes_prereleases_when_configured(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        mgr.config.get_setting.side_effect = lambda key, default=None: (
            True if key == "include_prereleases" else default
        )
        versions_data = {
            "1.15.0": {},
            "1.15.0-rc1": {},
        }
        response = self._make_mock_response(versions_data)
        with mock.patch("wrknv.managers.subrosa.ibm.asyncio.run", return_value=response):
            result = mgr.get_available_versions()
        assert "1.15.0" in result
        assert "1.15.0-rc1" in result

    def test_get_available_versions_raises_on_error(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        with (
            mock.patch("wrknv.managers.subrosa.ibm.asyncio.run", side_effect=RuntimeError("network")),
            pytest.raises(ToolManagerError, match="Failed to fetch Vault versions"),
        ):
            mgr.get_available_versions()

    def test_get_available_versions_filters_alpha(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        versions_data = {
            "1.15.0": {},
            "1.15.0-alpha1": {},
            "1.15.0-dev": {},
        }
        response = self._make_mock_response(versions_data)
        with mock.patch("wrknv.managers.subrosa.ibm.asyncio.run", return_value=response):
            result = mgr.get_available_versions()
        assert "1.15.0" in result
        assert "1.15.0-alpha1" not in result
        assert "1.15.0-dev" not in result


class TestIbmVaultGetDownloadUrl(FoundationTestCase):
    """Tests for IbmVaultVariant.get_download_url."""

    def test_get_download_url_darwin_arm64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        platform_info = {"os": "darwin", "arch": "arm64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("1.15.0")
        assert url == "https://releases.hashicorp.com/vault/1.15.0/vault_1.15.0_darwin_arm64.zip"

    def test_get_download_url_linux_amd64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("1.15.0")
        assert url == "https://releases.hashicorp.com/vault/1.15.0/vault_1.15.0_linux_amd64.zip"

    def test_get_download_url_amd64_maps_to_amd64(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        platform_info = {"os": "linux", "arch": "x86_64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("1.15.0")
        assert "amd64" in url

    def test_get_download_url_uses_zip_extension(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        platform_info = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(mgr, "get_platform_info", return_value=platform_info):
            url = mgr.get_download_url("1.15.0")
        assert url.endswith(".zip")


class TestIbmVaultGetChecksumUrl(FoundationTestCase):
    """Tests for IbmVaultVariant.get_checksum_url."""

    def test_get_checksum_url(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        url = mgr.get_checksum_url("1.15.0")
        assert url == "https://releases.hashicorp.com/vault/1.15.0/vault_1.15.0_SHA256SUMS"

    def test_checksum_url_contains_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        url = mgr.get_checksum_url("1.14.0")
        assert "1.14.0" in url
        assert url is not None


class TestIbmVaultInstallFromArchive(FoundationTestCase):
    """Tests for IbmVaultVariant._install_from_archive."""

    def test_install_from_archive_raises_when_binary_not_found(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        archive = tmp / "vault_1.15.0.zip"
        archive.write_text("fake archive")
        with (
            mock.patch.object(mgr, "extract_archive"),
            pytest.raises(ToolManagerError, match="Vault binary not found in archive"),
        ):
            mgr._install_from_archive(archive, "1.15.0")

    def test_install_from_archive_success(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        archive = tmp / "vault_1.15.0.zip"
        archive.write_text("fake archive")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            dst.mkdir(parents=True, exist_ok=True)
            (dst / "vault").write_text("vault binary content")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch("wrknv.managers.subrosa.ibm.safe_copy") as mock_copy,
            mock.patch.object(mgr, "make_executable"),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.subrosa.ibm.safe_rmtree"),
        ):
            mgr._install_from_archive(archive, "1.15.0")
        mock_copy.assert_called_once()

    def test_install_from_archive_cleans_up_on_error(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        archive = tmp / "vault_1.15.0.zip"
        archive.write_text("fake archive")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            dst.mkdir(parents=True, exist_ok=True)
            (dst / "vault").write_text("binary")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch("wrknv.managers.subrosa.ibm.safe_copy"),
            mock.patch.object(mgr, "make_executable"),
            mock.patch.object(mgr, "verify_installation", return_value=False),
            mock.patch("wrknv.managers.subrosa.ibm.safe_rmtree") as mock_rmtree,
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            mgr._install_from_archive(archive, "1.15.0")
        mock_rmtree.assert_called_once()


class TestIbmVaultVariantCoverageBranches(FoundationTestCase):
    """Cover uncovered branches in ibm.py."""

    def test_get_available_versions_sort_fallback(self) -> None:
        """Lines 62-63: when packaging.version import fails, falls back to string sort."""
        import sys

        mgr = IbmVaultVariant(WorkenvConfig())
        mock_response = mock.MagicMock()
        mock_response.json.return_value = {"versions": {"1.15.0": {}, "1.16.0": {}, "1.14.5": {}}}
        # Force `from packaging.version import parse` to fail by hiding the module
        real_packaging = sys.modules.get("packaging.version")
        sys.modules["packaging.version"] = None  # type: ignore[assignment]
        try:
            with mock.patch("wrknv.managers.subrosa.ibm.asyncio.run", return_value=mock_response):
                versions = mgr.get_available_versions()
        finally:
            if real_packaging is not None:
                sys.modules["packaging.version"] = real_packaging
            elif "packaging.version" in sys.modules:
                del sys.modules["packaging.version"]
        assert isinstance(versions, list)
        assert len(versions) > 0

    def test_get_download_url_unknown_arch(self) -> None:
        """Line 82: arch not arm64/amd64/x86_64 falls through to else branch."""
        mgr = IbmVaultVariant(WorkenvConfig())
        with mock.patch.object(mgr, "get_platform_info", return_value={"os": "linux", "arch": "riscv64"}):
            url = mgr.get_download_url("1.15.0")
        assert "riscv64" in url

    def test_install_loop_skips_non_vault_files(self) -> None:
        """Line 108->107: files like 'vault_license' match rglob but are skipped in loop."""
        tmp = self.create_temp_dir()
        mgr = _make_ibm_vault(tmp)
        archive = tmp / "vault_1.15.0.zip"
        archive.write_text("fake archive")

        def fake_extract(src, dst) -> None:  # type: ignore[no-untyped-def]
            dst.mkdir(parents=True, exist_ok=True)
            (dst / "vault_license").write_text("license")  # matches vault* but not "vault"
            (dst / "vault").write_text("vault binary")  # the real binary

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch("wrknv.managers.subrosa.ibm.safe_copy"),
            mock.patch.object(mgr, "make_executable"),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.subrosa.ibm.safe_rmtree"),
        ):
            mgr._install_from_archive(archive, "1.15.0")


# 🧰🌍🔚
