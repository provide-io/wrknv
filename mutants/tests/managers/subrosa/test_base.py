#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.subrosa.base module."""

from __future__ import annotations

import json
import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.subrosa.bao import BaoVariant


def _make_subrosa(tmp_dir: pathlib.Path) -> BaoVariant:
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

    # Override paths after init to use tmp dir
    mgr.install_path = tmp_dir / "subrosa"
    mgr.install_path.mkdir(parents=True, exist_ok=True)
    mgr.metadata_file = mgr.install_path / "metadata.json"
    mgr.metadata = {}
    mgr.cache_dir = tmp_dir / "cache"
    mgr.cache_dir.mkdir(parents=True, exist_ok=True)
    mgr.workenv_bin_dir = tmp_dir / "bin"
    (tmp_dir / "bin").mkdir(parents=True, exist_ok=True)
    return mgr


class TestSubRosaManagerInit(FoundationTestCase):
    """Tests for SubRosaManager.__init__."""

    def test_stores_install_path(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        assert mgr.install_path == tmp / "subrosa"

    def test_stores_workenv_bin_dir(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        assert mgr.workenv_bin_dir == tmp / "bin"

    def test_stores_metadata(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        assert isinstance(mgr.metadata, dict)

    def test_tool_name_is_bao(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        assert mgr.tool_name == "bao"

    def test_executable_name_is_bao(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        assert mgr.executable_name == "bao"


class TestLoadMetadata(FoundationTestCase):
    """Tests for SubRosaManager._load_metadata."""

    def test_returns_empty_when_no_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        result = mgr._load_metadata()
        assert result == {}

    def test_loads_existing_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        data = {"active_versions": {"bao": "2.1.0"}}
        mgr.metadata_file.write_text(json.dumps(data))
        result = mgr._load_metadata()
        assert result == data

    def test_handles_corrupt_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata_file.write_text("not valid json{{{")
        result = mgr._load_metadata()
        assert result == {}


class TestSaveMetadata(FoundationTestCase):
    """Tests for SubRosaManager._save_metadata."""

    def test_writes_json_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata = {"active_versions": {"bao": "2.1.0"}}
        mgr._save_metadata()
        assert mgr.metadata_file.exists()
        loaded = json.loads(mgr.metadata_file.read_text())
        assert loaded == {"active_versions": {"bao": "2.1.0"}}

    def test_handles_write_errors(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata = {"key": "value"}
        with mock.patch.object(pathlib.Path, "open", side_effect=OSError("permission denied")):
            mgr._save_metadata()  # should not raise


class TestGetBinaryPath(FoundationTestCase):
    """Tests for SubRosaManager.get_binary_path."""

    def test_returns_correct_path_for_bao_variant(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        result = mgr.get_binary_path("2.1.0")
        assert result == mgr.install_path / "bao_2.1.0"

    def test_uses_variant_name_in_path(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        result = mgr.get_binary_path("1.0.0")
        assert result.name == "bao_1.0.0"


class TestGetInstalledVersions(FoundationTestCase):
    """Tests for SubRosaManager.get_installed_versions."""

    def test_empty_when_no_files(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        result = mgr.get_installed_versions()
        assert result == []

    def test_finds_installed_versions(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        (mgr.install_path / "bao_2.1.0").write_text("binary")
        (mgr.install_path / "bao_2.0.0").write_text("binary")
        result = mgr.get_installed_versions()
        assert "2.1.0" in result
        assert "2.0.0" in result

    def test_ignores_non_matching_files(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        (mgr.install_path / "bao_2.1.0").write_text("binary")
        (mgr.install_path / "vault_1.15.0").write_text("binary")
        (mgr.install_path / "metadata.json").write_text("{}")
        result = mgr.get_installed_versions()
        assert result == ["2.1.0"]

    def test_returns_sorted_descending(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        for v in ["1.0.0", "2.1.0", "2.0.0"]:
            (mgr.install_path / f"bao_{v}").write_text("binary")
        result = mgr.get_installed_versions()
        assert result[0] == "2.1.0"


class TestGetInstalledVersion(FoundationTestCase):
    """Tests for SubRosaManager.get_installed_version."""

    def test_returns_none_when_no_metadata(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        assert mgr.get_installed_version() is None

    def test_returns_version_from_metadata(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata = {"active_versions": {"bao": "2.1.0"}}
        assert mgr.get_installed_version() == "2.1.0"

    def test_returns_none_when_different_variant(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata = {"active_versions": {"vault": "1.15.0"}}
        assert mgr.get_installed_version() is None


class TestSetInstalledVersion(FoundationTestCase):
    """Tests for SubRosaManager.set_installed_version."""

    def test_sets_version_in_metadata(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        with mock.patch.object(mgr, "_save_metadata") as mock_save:
            mgr.set_installed_version("2.1.0")
        assert mgr.metadata["active_versions"]["bao"] == "2.1.0"
        mock_save.assert_called_once()

    def test_creates_active_versions_dict_if_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata = {}
        with mock.patch.object(mgr, "_save_metadata"):
            mgr.set_installed_version("1.0.0")
        assert "active_versions" in mgr.metadata

    def test_overwrites_existing_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.metadata = {"active_versions": {"bao": "1.0.0"}}
        with mock.patch.object(mgr, "_save_metadata"):
            mgr.set_installed_version("2.1.0")
        assert mgr.metadata["active_versions"]["bao"] == "2.1.0"


class TestUpdateWorkenvSymlink(FoundationTestCase):
    """Tests for SubRosaManager._update_workenv_symlink."""

    def test_creates_symlink(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary content")
        mgr._update_workenv_symlink("2.1.0")
        symlink = mgr.workenv_bin_dir / "bao"
        assert symlink.exists() or symlink.is_symlink()

    def test_skips_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        # Binary doesn't exist, should not raise
        mgr._update_workenv_symlink("2.1.0")

    def test_skips_when_no_workenv_bin_dir(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.workenv_bin_dir = None
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary content")
        mgr._update_workenv_symlink("2.1.0")  # should not raise

    def test_replaces_existing_symlink(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary content")
        symlink = mgr.workenv_bin_dir / "bao"
        symlink.write_text("old")
        with mock.patch("wrknv.managers.subrosa.base.safe_delete") as mock_del:
            mgr._update_workenv_symlink("2.1.0")
        mock_del.assert_called_once()


class TestRegenerateEnvScript(FoundationTestCase):
    """Tests for SubRosaManager._regenerate_env_script."""

    def test_skips_when_no_project_files(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("wrknv.wenv.env_generator.create_project_env_scripts") as mock_gen,
        ):
            # No pyproject.toml or wrknv.toml in tmp
            mgr._regenerate_env_script()
        mock_gen.assert_not_called()

    def test_calls_create_project_env_scripts_when_pyproject_toml_exists(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        (tmp / "pyproject.toml").write_text("[project]\nname = 'test'")
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("wrknv.wenv.env_generator.create_project_env_scripts") as mock_gen,
        ):
            mgr._regenerate_env_script()
        mock_gen.assert_called_once_with(tmp)


class TestSwitchVersion(FoundationTestCase):
    """Tests for SubRosaManager.switch_version."""

    def test_dry_run_logs_without_installing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        with mock.patch.object(mgr, "install_version") as mock_install:
            mgr.switch_version("2.1.0", dry_run=True)
        mock_install.assert_not_called()

    def test_installs_when_version_not_present(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        with (
            mock.patch.object(mgr, "install_version") as mock_install,
            mock.patch.object(mgr, "_update_workenv_symlink"),
            mock.patch.object(mgr, "set_installed_version"),
            mock.patch.object(mgr, "_regenerate_env_script"),
        ):
            mgr.switch_version("2.1.0")
        mock_install.assert_called_once_with("2.1.0", dry_run=False)

    def test_skips_install_when_already_present(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary")
        with (
            mock.patch.object(mgr, "install_version") as mock_install,
            mock.patch.object(mgr, "_update_workenv_symlink"),
            mock.patch.object(mgr, "set_installed_version"),
            mock.patch.object(mgr, "_regenerate_env_script"),
        ):
            mgr.switch_version("2.1.0")
        mock_install.assert_not_called()

    def test_updates_symlink_and_sets_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary")
        with (
            mock.patch.object(mgr, "_update_workenv_symlink") as mock_symlink,
            mock.patch.object(mgr, "set_installed_version") as mock_set,
            mock.patch.object(mgr, "_regenerate_env_script"),
        ):
            mgr.switch_version("2.1.0")
        mock_symlink.assert_called_once_with("2.1.0")
        mock_set.assert_called_once_with("2.1.0")


class TestRemoveVersion(FoundationTestCase):
    """Tests for SubRosaManager.remove_version."""

    def test_removes_binary(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary")
        mgr.remove_version("2.1.0")
        assert not binary.exists()

    def test_no_error_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        mgr.remove_version("9.9.9")  # should not raise

    def test_updates_metadata_when_removing_current_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("binary")
        mgr.metadata = {"active_versions": {"bao": "2.1.0"}}
        with mock.patch.object(mgr, "_save_metadata") as mock_save:
            mgr.remove_version("2.1.0")
        assert "bao" not in mgr.metadata.get("active_versions", {})
        mock_save.assert_called_once()

    def test_does_not_update_metadata_when_removing_non_current(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("1.0.0")
        binary.write_text("binary")
        mgr.metadata = {"active_versions": {"bao": "2.1.0"}}
        with mock.patch.object(mgr, "_save_metadata") as mock_save:
            mgr.remove_version("1.0.0")
        mock_save.assert_not_called()


class TestInstallFromArchive(FoundationTestCase):
    """Tests for SubRosaManager._install_from_archive."""

    def test_raises_when_binary_not_found_in_archive(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        archive = tmp / "bao_2.1.0.tar.gz"
        archive.write_text("fake archive")
        with (
            mock.patch.object(mgr, "extract_archive"),
            pytest.raises(ToolManagerError, match="binary not found"),
        ):
            mgr._install_from_archive(archive, "2.1.0")

    def test_installs_binary_from_archive(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        archive = tmp / "bao_2.1.0.tar.gz"
        archive.write_text("fake archive")

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            dst.mkdir(parents=True, exist_ok=True)
            (dst / "bao").write_text("binary content")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch("wrknv.managers.subrosa.base.safe_copy") as mock_copy,
            mock.patch.object(mgr, "make_executable"),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.subrosa.base.safe_rmtree"),
        ):
            mgr._install_from_archive(archive, "2.1.0")
        mock_copy.assert_called_once()


class TestVerifyInstallation(FoundationTestCase):
    """Tests for SubRosaManager.verify_installation."""

    def test_returns_false_when_binary_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        result = mgr.verify_installation("2.1.0")
        assert result is False

    def test_returns_true_when_version_matches(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("fake binary")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Bao v2.1.0"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is True

    def test_returns_true_when_version_matches_with_v_prefix(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("fake binary")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "bao version v2.1.0"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is True

    def test_returns_false_on_version_mismatch(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("fake binary")
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "Bao v2.0.0"
        mock_result.stderr = ""
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is False

    def test_returns_false_on_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("fake binary")
        mock_result = mock.Mock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error"
        with mock.patch("provide.foundation.process.run", return_value=mock_result):
            result = mgr.verify_installation("2.1.0")
        assert result is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        binary = mgr.get_binary_path("2.1.0")
        binary.write_text("fake binary")
        with mock.patch("provide.foundation.process.run", side_effect=RuntimeError("exec failed")):
            result = mgr.verify_installation("2.1.0")
        assert result is False


# 🧰🌍🔚
