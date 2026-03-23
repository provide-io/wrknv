#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.base module (TfManager)."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.config import WorkenvConfig
from wrknv.managers.tf.base import TfManager
from wrknv.managers.tf.metadata import TfMetadataManager


class FakeTfManager(TfManager):
    """Concrete subclass of TfManager for testing."""

    @property
    def tool_name(self) -> str:
        return "ibmtf"

    @property
    def executable_name(self) -> str:
        return "ibmtf"

    @property
    def tool_prefix(self) -> str:
        return "terraform"

    def get_available_versions(self) -> list[str]:
        return ["1.7.0", "1.6.0", "1.5.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/terraform/{version}/terraform.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://example.com/terraform/{version}/SHA256SUMS"

    def verify_installation(self, version: str) -> bool:
        return True


def _make_manager(tmp_dir: pathlib.Path) -> FakeTfManager:
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
        manager = FakeTfManager(config=cfg)
        manager.install_path = tf_versions_dir
        manager.metadata = manager.metadata_manager.metadata
    return manager


class TestTfManagerProperties(FoundationTestCase):
    """Tests for TfManager property methods."""

    def test_tool_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.tool_name == "ibmtf"

    def test_executable_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.executable_name == "ibmtf"

    def test_tool_prefix(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.tool_prefix == "terraform"


class TestGetBinaryPath(FoundationTestCase):
    """Tests for TfManager.get_binary_path."""

    def test_returns_prefixed_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_binary_path("1.7.0")
        assert result == manager.install_path / "terraform_1.7.0"

    def test_different_versions(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.get_binary_path("1.5.0").name == "terraform_1.5.0"
        assert manager.get_binary_path("1.6.0").name == "terraform_1.6.0"

    def test_path_is_under_install_path(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_binary_path("1.7.0")
        assert result.parent == manager.install_path


class TestGetInstalledVersions(FoundationTestCase):
    """Tests for TfManager.get_installed_versions."""

    def test_returns_empty_when_no_binaries(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        result = manager.get_installed_versions()
        assert result == []

    def test_returns_versions_from_prefix_files(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        (manager.install_path / "terraform_1.7.0").write_text("binary")
        (manager.install_path / "terraform_1.6.0").write_text("binary")
        result = manager.get_installed_versions()
        assert "1.7.0" in result
        assert "1.6.0" in result

    def test_excludes_non_prefix_files(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        (manager.install_path / "terraform_1.7.0").write_text("binary")
        (manager.install_path / "tofu_1.5.0").write_text("binary")
        (manager.install_path / "metadata.json").write_text("{}")
        result = manager.get_installed_versions()
        assert "1.7.0" in result
        assert len(result) == 1

    def test_excludes_directories(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        (manager.install_path / "terraform_1.7.0").mkdir()
        result = manager.get_installed_versions()
        assert result == []

    def test_returns_sorted_descending(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        for v in ["1.5.0", "1.7.0", "1.6.0"]:
            (manager.install_path / f"terraform_{v}").write_text("binary")
        result = manager.get_installed_versions()
        assert result == sorted(result, reverse=True)

    def test_excludes_non_semver_names(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        (manager.install_path / "terraform_latest").write_text("binary")
        (manager.install_path / "terraform_1.7.0").write_text("binary")
        result = manager.get_installed_versions()
        assert "latest" not in result
        assert "1.7.0" in result


class TestGetInstalledVersion(FoundationTestCase):
    """Tests for TfManager.get_installed_version."""

    def test_returns_none_when_no_metadata(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        result = manager.get_installed_version()
        assert result is None

    def test_returns_version_from_default_profile(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.7.0"}}}
        result = manager.get_installed_version()
        assert result == "1.7.0"

    def test_respects_env_profile(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {
            "workenv": {
                "default": {"ibmtf_version": "1.6.0"},
                "prod": {"ibmtf_version": "1.7.0"},
            }
        }
        with mock.patch.dict("os.environ", {"WRKENV_PROFILE": "prod"}):
            result = manager.get_installed_version()
        assert result == "1.7.0"

    def test_returns_none_when_profile_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"workenv": {"default": {}}}
        result = manager.get_installed_version()
        assert result is None

    def test_returns_none_when_no_workenv_key(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"some_other_key": "value"}
        result = manager.get_installed_version()
        assert result is None


class TestSetInstalledVersion(FoundationTestCase):
    """Tests for TfManager.set_installed_version."""

    def test_sets_version_in_default_profile(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        with (
            mock.patch.object(manager.metadata_manager, "save_metadata"),
            mock.patch.object(manager, "_update_recent_file_with_active"),
        ):
            manager.set_installed_version("1.7.0")
        assert manager.metadata["workenv"]["default"]["ibmtf_version"] == "1.7.0"

    def test_sets_version_in_current_profile(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        with (
            mock.patch.dict("os.environ", {"WRKENV_PROFILE": "staging"}),
            mock.patch.object(manager.metadata_manager, "save_metadata"),
            mock.patch.object(manager, "_update_recent_file_with_active"),
        ):
            manager.set_installed_version("1.6.0")
        assert manager.metadata["workenv"]["staging"]["ibmtf_version"] == "1.6.0"

    def test_calls_save_metadata(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        with (
            mock.patch.object(manager.metadata_manager, "save_metadata") as mock_save,
            mock.patch.object(manager, "_update_recent_file_with_active"),
        ):
            manager.set_installed_version("1.7.0")
        mock_save.assert_called_once()

    def test_calls_update_recent_file_with_active(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        with (
            mock.patch.object(manager.metadata_manager, "save_metadata"),
            mock.patch.object(manager, "_update_recent_file_with_active") as mock_update,
        ):
            manager.set_installed_version("1.7.0")
        mock_update.assert_called_once_with("1.7.0")

    def test_preserves_existing_profile_data(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"workenv": {"default": {"other_key": "other_val"}}}
        with (
            mock.patch.object(manager.metadata_manager, "save_metadata"),
            mock.patch.object(manager, "_update_recent_file_with_active"),
        ):
            manager.set_installed_version("1.7.0")
        assert manager.metadata["workenv"]["default"]["other_key"] == "other_val"


class TestGetCurrentProfile(FoundationTestCase):
    """Tests for TfManager._get_current_profile."""

    def test_returns_default_when_no_env(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        with mock.patch.dict("os.environ", {"WRKENV_PROFILE": ""}):
            result = manager._get_current_profile()
        assert result == "default"

    def test_returns_env_var_when_set(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.dict("os.environ", {"WRKENV_PROFILE": "production"}):
            result = manager._get_current_profile()
        assert result == "production"

    def test_returns_metadata_profile_when_set(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"workenv": {"_current_profile": "staging"}}
        with mock.patch.dict("os.environ", {"WRKENV_PROFILE": ""}):
            result = manager._get_current_profile()
        assert result == "staging"

    def test_env_var_takes_precedence_over_metadata(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"workenv": {"_current_profile": "staging"}}
        with mock.patch.dict("os.environ", {"WRKENV_PROFILE": "production"}):
            result = manager._get_current_profile()
        assert result == "production"


class TestGetMetadataForVersion(FoundationTestCase):
    """Tests for TfManager.get_metadata_for_version."""

    def test_returns_metadata_when_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"terraform_1.7.0": {"version": "1.7.0", "tool": "ibmtf"}}
        result = manager.get_metadata_for_version("1.7.0")
        assert result is not None
        assert result["version"] == "1.7.0"

    def test_returns_none_when_not_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        result = manager.get_metadata_for_version("9.9.9")
        assert result is None


class TestGetActiveVersionInfo(FoundationTestCase):
    """Tests for TfManager.get_active_version_info."""

    def test_returns_none_when_no_installed_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        result = manager.get_active_version_info()
        assert result is None

    def test_returns_none_when_no_metadata_for_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"workenv": {"default": {"ibmtf_version": "1.7.0"}}}
        result = manager.get_active_version_info()
        assert result is None

    def test_returns_info_with_active_flag(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {
            "workenv": {"default": {"ibmtf_version": "1.7.0"}},
            "terraform_1.7.0": {"version": "1.7.0", "tool": "ibmtf"},
        }
        result = manager.get_active_version_info()
        assert result is not None
        assert result["is_active"] is True

    def test_includes_binary_exists_flag(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {
            "workenv": {"default": {"ibmtf_version": "1.7.0"}},
            "terraform_1.7.0": {"version": "1.7.0", "tool": "ibmtf"},
        }
        result = manager.get_active_version_info()
        assert result is not None
        assert "binary_exists" in result


class TestGetGlobalVersion(FoundationTestCase):
    """Tests for TfManager.get_global_version."""

    def test_returns_none_when_no_global_key(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {}
        result = manager.get_global_version()
        assert result is None

    def test_returns_version_from_global_key(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"global": {"ibmtf_version": "1.7.0"}}
        result = manager.get_global_version()
        assert result == "1.7.0"

    def test_returns_none_when_tool_key_missing(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        manager.metadata = {"global": {"other_tool_version": "1.0.0"}}
        result = manager.get_global_version()
        assert result is None


class TestSetGlobalVersion(FoundationTestCase):
    """Tests for TfManager.set_global_version."""

    def test_skips_when_binary_not_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        # Should not raise, should log a warning
        manager.set_global_version("1.7.0")

    def test_copies_binary_to_local_bin(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary content")

        with (
            mock.patch("pathlib.Path.home", return_value=tmp),
            mock.patch.object(manager.metadata_manager, "save_metadata"),
        ):
            manager.set_global_version("1.7.0")

        assert manager.metadata.get("global", {}).get("ibmtf_version") == "1.7.0"

    def test_updates_metadata_with_version(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        binary_path = manager.get_binary_path("1.7.0")
        binary_path.write_text("binary content")
        manager.metadata = {}

        with (
            mock.patch("pathlib.Path.home", return_value=tmp),
            mock.patch.object(manager.metadata_manager, "save_metadata"),
        ):
            manager.set_global_version("1.7.0")

        assert "global" in manager.metadata
        assert manager.metadata["global"]["ibmtf_version"] == "1.7.0"


# 🧰🌍🔚
