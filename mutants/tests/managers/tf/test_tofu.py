#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.tofu module (TofuTfVariant)."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.tf.metadata import TfMetadataManager
from wrknv.managers.tf.tofu import TofuTfVariant


def _make_tofu_manager(tmp_dir: pathlib.Path) -> TofuTfVariant:
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
        manager = TofuTfVariant(config=cfg)
        manager.install_path = tf_versions_dir
        manager.metadata = manager.metadata_manager.metadata
    return manager


class TestTofuTfVariantProperties(FoundationTestCase):
    """Test TofuTfVariant property methods."""

    def test_tool_name(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        assert manager.tool_name == "tofu"

    def test_executable_name(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        assert manager.executable_name == "tofu"

    def test_tool_prefix(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        assert manager.tool_prefix == "opentofu"

    def test_github_client_lazy_init(self) -> None:
        """Test github_client property creates client on first access."""
        from wrknv.managers.github import GitHubReleasesClient

        manager = _make_tofu_manager(self.create_temp_dir())
        assert manager._github_client is None
        client = manager.github_client
        assert isinstance(client, GitHubReleasesClient)
        assert client is manager.github_client  # same instance on second access

    def test_github_client_targets_opentofu_repo(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        assert manager.github_client.repo == "opentofu/opentofu"


class TestTofuGetAvailableVersions(FoundationTestCase):
    """Test get_available_versions."""

    def test_returns_versions_from_github(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        mock_client = mock.MagicMock()
        mock_client.get_versions = mock.AsyncMock(return_value=["1.8.0", "1.7.0"])
        manager._github_client = mock_client

        versions = manager.get_available_versions()
        assert "1.8.0" in versions
        assert "1.7.0" in versions

    def test_passes_include_prereleases_setting(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        # Override side_effect so include_prereleases returns True
        manager.config.get_setting.side_effect = None
        manager.config.get_setting.return_value = True
        mock_client = mock.MagicMock()
        mock_client.get_versions = mock.AsyncMock(return_value=["1.9.0-alpha"])
        manager._github_client = mock_client

        manager.get_available_versions()
        mock_client.get_versions.assert_awaited_once_with(include_prereleases=True)

    def test_raises_tool_manager_error_on_failure(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        mock_client = mock.MagicMock()
        mock_client.get_versions = mock.AsyncMock(side_effect=Exception("network error"))
        manager._github_client = mock_client

        with pytest.raises(ToolManagerError):
            manager.get_available_versions()


class TestTofuGetDownloadUrl(FoundationTestCase):
    """Test get_download_url."""

    def test_url_includes_version_and_platform(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        with mock.patch.object(
            manager,
            "get_platform_info",
            return_value={"os": "linux", "arch": "amd64"},
        ):
            url = manager.get_download_url("1.7.0")
        assert "1.7.0" in url
        assert "linux" in url
        assert "amd64" in url
        assert url.endswith(".zip")

    def test_checksum_url_includes_version(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        url = manager.get_checksum_url("1.7.0")
        assert url is not None
        assert "1.7.0" in url
        assert "SHA256SUMS" in url


class TestTofuVerifyInstallation(FoundationTestCase):
    """Test verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        with mock.patch.object(
            manager.install_path.__class__,
            "exists",
            return_value=False,
        ):
            result = manager.verify_installation("1.7.0")
        assert result is False

    def test_returns_true_when_version_matches(self, tmp_path: pathlib.Path) -> None:
        manager = _make_tofu_manager(tmp_path)
        binary = tmp_path / ".terraform.versions" / "opentofu_1.7.0"
        binary.write_bytes(b"fake")

        mock_result = mock.MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "OpenTofu v1.7.0"
        mock_result.stderr = ""

        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.7.0")
        assert result is True

    def test_returns_false_when_version_mismatch(self, tmp_path: pathlib.Path) -> None:
        manager = _make_tofu_manager(tmp_path)
        binary = tmp_path / ".terraform.versions" / "opentofu_1.7.0"
        binary.write_bytes(b"fake")

        mock_result = mock.MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "OpenTofu v1.6.0"
        mock_result.stderr = ""

        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.7.0")
        assert result is False

    def test_returns_false_when_command_fails(self, tmp_path: pathlib.Path) -> None:
        manager = _make_tofu_manager(tmp_path)
        binary = tmp_path / ".terraform.versions" / "opentofu_1.7.0"
        binary.write_bytes(b"fake")

        mock_result = mock.MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error"

        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = manager.verify_installation("1.7.0")
        assert result is False

    def test_returns_false_on_exception(self, tmp_path: pathlib.Path) -> None:
        manager = _make_tofu_manager(tmp_path)
        binary = tmp_path / ".terraform.versions" / "opentofu_1.7.0"
        binary.write_bytes(b"fake")

        with mock.patch("provide.foundation.process.run", side_effect=OSError("exec failed")):
            result = manager.verify_installation("1.7.0")
        assert result is False


class TestTofuHarnessCompatibility(FoundationTestCase):
    """Test get_harness_compatibility and compatibility checks."""

    def test_returns_not_installed_when_no_version(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        with mock.patch.object(manager, "get_installed_version", return_value=None):
            result = manager.get_harness_compatibility()
        assert result == {"status": "not_installed"}

    def test_returns_compatible_dict_when_installed(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        with mock.patch.object(manager, "get_installed_version", return_value="1.7.0"):
            result = manager.get_harness_compatibility()
        assert result["status"] == "compatible"
        assert result["version"] == "1.7.0"
        assert "harness" in result
        assert "go.cty" in result["harness"]
        assert "go.wire" in result["harness"]
        assert "conformance" in result["harness"]

    def test_check_cty_compatibility_returns_compatible(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        result = manager._check_cty_compatibility("1.7.0")
        assert result["compatible"] is True

    def test_check_wire_compatibility_compatible_version(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        result = manager._check_wire_compatibility("1.6.0")
        assert result["compatible"] is True

    def test_check_wire_compatibility_incompatible_version(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        result = manager._check_wire_compatibility("1.5.0")
        assert result["compatible"] is False

    def test_check_wire_compatibility_invalid_version(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        result = manager._check_wire_compatibility("invalid")
        assert result["compatible"] is False

    def test_check_conformance_compatibility_returns_compatible(self) -> None:
        manager = _make_tofu_manager(self.create_temp_dir())
        result = manager._check_conformance_compatibility("1.7.0")
        assert result["compatible"] is True


# 🧰🌍🔚
