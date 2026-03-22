#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.ibm module (IbmTfVariant)."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.tf.ibm import IbmTfVariant
from wrknv.managers.tf.metadata import TfMetadataManager


def _make_ibmtf(tmp_dir: pathlib.Path) -> IbmTfVariant:
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: {
        "install_path": str(tmp_dir / "tools"),
    }.get(key, default)
    cfg.get_tool_version.return_value = None

    tf_versions_dir = tmp_dir / ".terraform.versions"
    tf_versions_dir.mkdir(parents=True, exist_ok=True)

    with (
        mock.patch("wrknv.managers.tf.base.get_workenv_bin_dir", return_value=tmp_dir / "bin"),
        mock.patch.object(TfMetadataManager, "load_metadata"),
        mock.patch(
            "wrknv.managers.tf.base.pathlib.Path.expanduser",
            return_value=tf_versions_dir,
        ),
    ):
        manager = IbmTfVariant(config=cfg)
        manager.install_path = tf_versions_dir
        manager.metadata = manager.metadata_manager.metadata
    return manager


class TestIbmTfVariantProperties(FoundationTestCase):
    """Tests for IbmTfVariant properties."""

    def test_tool_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        assert manager.tool_name == "ibmtf"

    def test_executable_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        assert manager.executable_name == "ibmtf"

    def test_tool_prefix(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        assert manager.tool_prefix == "terraform"


class TestGetDownloadUrl(FoundationTestCase):
    """Tests for IbmTfVariant.get_download_url."""

    def test_default_mirror_url(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_platform = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.7.0")
        assert "releases.hashicorp.com/terraform" in url
        assert "1.7.0" in url
        assert "linux" in url
        assert "amd64" in url

    def test_url_format(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_platform = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.7.0")
        assert url == "https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_linux_amd64.zip"

    def test_darwin_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_platform = {"os": "darwin", "arch": "amd64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.6.5")
        assert "darwin_amd64" in url
        assert "1.6.5" in url

    def test_darwin_arm64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_platform = {"os": "darwin", "arch": "arm64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.7.0")
        assert "darwin_arm64" in url

    def test_windows_amd64(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_platform = {"os": "windows", "arch": "amd64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.7.0")
        assert "windows_amd64" in url
        assert url.endswith(".zip")

    def test_custom_mirror_url(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "terraform_mirror": "https://my-mirror.example.com/tf",
        }.get(key, default)
        fake_platform = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.7.0")
        assert url.startswith("https://my-mirror.example.com/tf/")

    def test_mirror_url_trailing_slash_stripped(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "terraform_mirror": "https://my-mirror.example.com/tf/",
        }.get(key, default)
        fake_platform = {"os": "linux", "arch": "amd64"}
        with mock.patch.object(manager, "get_platform_info", return_value=fake_platform):
            url = manager.get_download_url("1.7.0")
        assert "//" not in url.replace("https://", "")


class TestGetChecksumUrl(FoundationTestCase):
    """Tests for IbmTfVariant.get_checksum_url."""

    def test_default_checksum_url(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        url = manager.get_checksum_url("1.7.0")
        assert url is not None
        assert "releases.hashicorp.com/terraform" in url
        assert "1.7.0" in url
        assert "SHA256SUMS" in url

    def test_checksum_url_format(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        url = manager.get_checksum_url("1.7.0")
        assert url == "https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_SHA256SUMS"

    def test_custom_mirror_checksum_url(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "terraform_mirror": "https://my-mirror.example.com/tf",
        }.get(key, default)
        url = manager.get_checksum_url("1.7.0")
        assert url is not None
        assert url.startswith("https://my-mirror.example.com/tf/")

    def test_checksum_url_trailing_slash_stripped(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "terraform_mirror": "https://my-mirror.example.com/tf/",
        }.get(key, default)
        url = manager.get_checksum_url("1.7.0")
        assert url is not None
        assert "//" not in url.replace("https://", "")


class TestGetAvailableVersions(FoundationTestCase):
    """Tests for IbmTfVariant.get_available_versions."""

    def test_returns_sorted_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_response = mock.MagicMock()
        fake_response.json.return_value = {
            "versions": {
                "1.5.0": {"version": "1.5.0"},
                "1.7.0": {"version": "1.7.0"},
                "1.6.0": {"version": "1.6.0"},
            }
        }
        with mock.patch("wrknv.managers.tf.ibm.asyncio.run", return_value=fake_response):
            versions = manager.get_available_versions()
        assert versions[0] == "1.7.0"
        assert versions == sorted(versions, reverse=True)

    def test_excludes_prerelease_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "include_prereleases": False,
        }.get(key, default)
        fake_response = mock.MagicMock()
        fake_response.json.return_value = {
            "versions": {
                "1.7.0": {"version": "1.7.0"},
                "1.8.0-alpha1": {"version": "1.8.0-alpha1"},
                "1.8.0-beta1": {"version": "1.8.0-beta1"},
                "1.8.0-rc1": {"version": "1.8.0-rc1"},
            }
        }
        with mock.patch("wrknv.managers.tf.ibm.asyncio.run", return_value=fake_response):
            versions = manager.get_available_versions()
        assert "1.7.0" in versions
        assert not any("alpha" in v or "beta" in v or "rc" in v for v in versions)

    def test_includes_prereleases_when_configured(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "include_prereleases": True,
        }.get(key, default)
        fake_response = mock.MagicMock()
        fake_response.json.return_value = {
            "versions": {
                "1.7.0": {"version": "1.7.0"},
                "1.8.0-alpha1": {"version": "1.8.0-alpha1"},
            }
        }
        with mock.patch("wrknv.managers.tf.ibm.asyncio.run", return_value=fake_response):
            versions = manager.get_available_versions()
        assert "1.8.0-alpha1" in versions

    def test_raises_on_network_failure(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        with (
            mock.patch("wrknv.managers.tf.ibm.asyncio.run", side_effect=RuntimeError("network error")),
            pytest.raises(ToolManagerError, match="Failed to fetch IBM Terraform versions"),
        ):
            manager.get_available_versions()

    def test_uses_custom_mirror_for_api_url(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "terraform_mirror": "https://my-mirror.example.com/tf",
        }.get(key, default)
        fake_response = mock.MagicMock()
        fake_response.json.return_value = {"versions": {}}

        with mock.patch("wrknv.managers.tf.ibm.asyncio.run", return_value=fake_response) as mock_run:
            manager.get_available_versions()
            # Verify get was called exactly once (with the mirror-based URL)
            mock_run.assert_called_once()

    def test_handles_empty_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_response = mock.MagicMock()
        fake_response.json.return_value = {"versions": {}}
        with mock.patch("wrknv.managers.tf.ibm.asyncio.run", return_value=fake_response):
            versions = manager.get_available_versions()
        assert versions == []

    def test_skips_versions_without_version_key(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        fake_response = mock.MagicMock()
        fake_response.json.return_value = {
            "versions": {
                "1.7.0": {"version": "1.7.0"},
                "broken": {},  # No "version" key
            }
        }
        with mock.patch("wrknv.managers.tf.ibm.asyncio.run", return_value=fake_response):
            versions = manager.get_available_versions()
        assert "1.7.0" in versions
        assert len(versions) == 1


class TestIsPrerelease(FoundationTestCase):
    """Tests for IbmTfVariant._is_prerelease."""

    def test_stable_version_not_prerelease(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: default
        assert manager._is_prerelease("1.7.0") is False

    def test_alpha_is_prerelease(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: default
        assert manager._is_prerelease("1.8.0-alpha1") is True

    def test_beta_is_prerelease(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: default
        assert manager._is_prerelease("1.8.0-beta1") is True

    def test_rc_is_prerelease(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: default
        assert manager._is_prerelease("1.8.0-rc1") is True

    def test_when_include_prereleases_true(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.config.get_setting.side_effect = lambda key, default=None: {
            "include_prereleases": True,
        }.get(key, default)
        # Even prereleases return False (not filtered out) when flag is True
        assert manager._is_prerelease("1.8.0-alpha1") is False


class TestVerifyInstallation(FoundationTestCase):
    """Tests for IbmTfVariant.verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        result = manager.verify_installation("1.7.0")
        assert result is False

    def test_returns_true_when_version_matches(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Terraform v1.7.0\non linux"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.7.0")
        assert result is True

    def test_returns_false_when_version_mismatch(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Terraform v1.6.0\non linux"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.7.0")
        assert result is False

    def test_returns_false_when_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        mock_result = mock.Mock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.7.0")
        assert result is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary")
        with mock.patch("provide.foundation.process.run", side_effect=RuntimeError("exec failed")):
            result = manager.verify_installation("1.7.0")
        assert result is False


class TestGetHarnessCompatibility(FoundationTestCase):
    """Tests for IbmTfVariant.get_harness_compatibility."""

    def test_returns_not_installed_when_no_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {}
        result = manager.get_harness_compatibility()
        assert result == {"status": "not_installed"}

    def test_returns_compatibility_dict_when_version_set(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.7.0"}}}
        result = manager.get_harness_compatibility()
        assert result["status"] == "compatible"
        assert result["version"] == "1.7.0"
        assert "harness" in result

    def test_harness_has_expected_keys(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.7.0"}}}
        result = manager.get_harness_compatibility()
        harness = result["harness"]
        assert "go.cty" in harness
        assert "go.wire" in harness
        assert "conformance" in harness

    def test_wire_compatible_for_1_5_plus(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.5.0"}}}
        result = manager.get_harness_compatibility()
        assert result["harness"]["go.wire"]["compatible"] is True

    def test_wire_incompatible_for_older_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.4.0"}}}
        result = manager.get_harness_compatibility()
        assert result["harness"]["go.wire"]["compatible"] is False

    def test_cty_always_compatible(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.3.0"}}}
        result = manager.get_harness_compatibility()
        assert result["harness"]["go.cty"]["compatible"] is True

    def test_conformance_always_compatible(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_ibmtf(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.3.0"}}}
        result = manager.get_harness_compatibility()
        assert result["harness"]["conformance"]["compatible"] is True


# 🧰🌍🔚
