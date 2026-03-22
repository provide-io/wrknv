#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for tf_base.py uncovered branches: metadata, recent file, symlink, copy."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from provide.testkit import FoundationTestCase

from wrknv.wenv.managers.tf_base import TfVersionsManager


class ConcreteTfManager(TfVersionsManager):
    """Concrete implementation for testing."""

    @property
    def tool_name(self) -> str:
        return "terraform"

    @property
    def executable_name(self) -> str:
        return "terraform"

    @property
    def tool_prefix(self) -> str:
        return "terraform"

    def get_available_versions(self) -> list[str]:
        return ["1.6.0", "1.5.7"]

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/terraform_{version}.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://example.com/terraform_{version}_SHA256SUMS"


class TestMigrateMetadataWorkenvExists(FoundationTestCase):
    """Test _migrate_metadata_format when workenv/default already exists."""

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_migrate_workenv_already_exists(self, mock_open: Mock, mock_exists: Mock) -> None:
        """Test migration when workenv and default already exist (lines 89->91, 91->96)."""
        old_metadata = {"active_tofu": "1.6.0", "workenv": {"default": {"other_key": "v"}}}

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file

        with patch("json.load", return_value=old_metadata), patch("json.dump"):
            manager = ConcreteTfManager()
            assert "workenv" in manager.metadata
            assert "default" in manager.metadata["workenv"]
            assert manager.metadata["workenv"]["default"]["opentofu_version"] == "1.6.0"


class TestSaveMetadataException(FoundationTestCase):
    """Test _save_metadata exception branch."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_save_metadata_exception_is_swallowed(self, mock_exists: Mock) -> None:
        """Test that _save_metadata swallows exceptions (line 109)."""
        manager = ConcreteTfManager()
        with patch("pathlib.Path.open", side_effect=OSError("disk full")):
            manager._save_metadata()


class TestUpdateRecentFileBranches(FoundationTestCase):
    """Test _update_recent_file uncovered branches."""

    @patch("pathlib.Path.exists", return_value=False)
    @patch.object(ConcreteTfManager, "get_installed_versions", return_value=["1.6.0"])
    def test_update_recent_file_no_existing_file(
        self, mock_versions: Mock, mock_exists: Mock
    ) -> None:
        """Test RECENT file update when file does not exist (skip read branch)."""
        manager = ConcreteTfManager()
        with patch("pathlib.Path.open") as mock_open, patch("json.dump") as mock_dump:
            mock_file = MagicMock()
            mock_file.__enter__.return_value = mock_file
            mock_file.__exit__.return_value = False
            mock_open.return_value = mock_file
            manager._update_recent_file()
        mock_dump.assert_called()

    @patch("pathlib.Path.exists", return_value=True)
    @patch.object(ConcreteTfManager, "get_installed_versions", return_value=["1.6.0"])
    def test_update_recent_file_read_exception(
        self, mock_versions: Mock, mock_exists: Mock
    ) -> None:
        """Test RECENT file read exception resets to empty dict (lines 122-123)."""
        manager = ConcreteTfManager()
        mock_read_file = MagicMock()
        mock_read_file.__enter__.side_effect = ValueError("corrupt json")
        mock_write_file = MagicMock()
        mock_write_file.__enter__.return_value = mock_write_file
        mock_write_file.__exit__.return_value = False
        call_count = [0]

        def open_side_effect(*args, **kwargs):
            call_count[0] += 1
            return mock_read_file if call_count[0] == 1 else mock_write_file

        with patch("pathlib.Path.open", side_effect=open_side_effect), patch("json.dump"):
            manager._update_recent_file()

    @patch("pathlib.Path.exists", return_value=True)
    @patch.object(ConcreteTfManager, "get_installed_versions", return_value=[])
    def test_update_recent_file_removes_empty_tool(
        self, mock_versions: Mock, mock_exists: Mock
    ) -> None:
        """Test RECENT file removes tool when no versions installed (lines 132-134)."""
        manager = ConcreteTfManager()
        existing = {"terraform": ["1.5.0"]}
        with (
            patch("pathlib.Path.open"),
            patch("json.load", return_value=existing),
            patch("json.dump") as mock_dump,
        ):
            manager._update_recent_file()
            assert "terraform" not in mock_dump.call_args[0][0]

    @patch("pathlib.Path.exists", return_value=True)
    @patch.object(ConcreteTfManager, "get_installed_versions", return_value=["1.6.0"])
    def test_update_recent_file_write_exception(
        self, mock_versions: Mock, mock_exists: Mock
    ) -> None:
        """Test RECENT file write exception is swallowed (line 140)."""
        manager = ConcreteTfManager()
        read_file = MagicMock()
        read_file.__enter__.return_value = read_file
        read_file.__exit__.return_value = False
        write_file = MagicMock()
        write_file.__enter__.side_effect = OSError("write error")
        call_count = [0]

        def open_side_effect(*args, **kwargs):
            call_count[0] += 1
            return read_file if call_count[0] == 1 else write_file

        with (
            patch("pathlib.Path.open", side_effect=open_side_effect),
            patch("json.load", return_value={}),
        ):
            manager._update_recent_file()


class TestUpdateRecentFileWithActiveBranches(FoundationTestCase):
    """Test _update_recent_file_with_active uncovered branches."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_update_with_active_no_recent_file(self, mock_exists: Mock) -> None:
        """Test update when RECENT file does not exist (lines 149->157)."""
        manager = ConcreteTfManager()
        with patch("pathlib.Path.open") as mock_open, patch("json.dump"):
            mock_file = MagicMock()
            mock_file.__enter__.return_value = mock_file
            mock_file.__exit__.return_value = False
            mock_open.return_value = mock_file
            manager._update_recent_file_with_active("1.6.0")

    @patch("pathlib.Path.exists", return_value=True)
    def test_update_with_active_read_exception(self, mock_exists: Mock) -> None:
        """Test RECENT file read exception resets to empty dict (lines 153-154)."""
        manager = ConcreteTfManager()
        broken_read = MagicMock()
        broken_read.__enter__.side_effect = ValueError("bad json")
        write_file = MagicMock()
        write_file.__enter__.return_value = write_file
        write_file.__exit__.return_value = False
        call_count = [0]

        def open_side_effect(*args, **kwargs):
            call_count[0] += 1
            return broken_read if call_count[0] == 1 else write_file

        with patch("pathlib.Path.open", side_effect=open_side_effect), patch("json.dump"):
            manager._update_recent_file_with_active("1.6.0")

    @patch("pathlib.Path.exists", return_value=True)
    def test_update_with_active_moves_existing_version_to_front(
        self, mock_exists: Mock
    ) -> None:
        """Test version is moved from existing list to front (line 164)."""
        manager = ConcreteTfManager()
        existing = {"terraform": ["1.5.0", "1.6.0", "1.4.0"]}
        with (
            patch("pathlib.Path.open"),
            patch("json.load", return_value=existing),
            patch("json.dump") as mock_dump,
        ):
            manager._update_recent_file_with_active("1.6.0")
            result = mock_dump.call_args[0][0]["terraform"]
            assert result[0] == "1.6.0"
            assert result.count("1.6.0") == 1

    @patch("pathlib.Path.exists", return_value=True)
    def test_update_with_active_write_exception(self, mock_exists: Mock) -> None:
        """Test RECENT file write exception is swallowed (line 176)."""
        manager = ConcreteTfManager()
        read_file = MagicMock()
        read_file.__enter__.return_value = read_file
        read_file.__exit__.return_value = False
        write_file = MagicMock()
        write_file.__enter__.side_effect = OSError("no space")
        call_count = [0]

        def open_side_effect(*args, **kwargs):
            call_count[0] += 1
            return read_file if call_count[0] == 1 else write_file

        with (
            patch("pathlib.Path.open", side_effect=open_side_effect),
            patch("json.load", return_value={}),
        ):
            manager._update_recent_file_with_active("1.6.0")


class TestGetInstalledVersionBranches(FoundationTestCase):
    """Test get_installed_version uncovered branches."""

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_tool_key_not_in_profile_data(self, mock_open: Mock, mock_exists: Mock) -> None:
        """Test returns None when tool_key not in profile (lines 228->232)."""
        metadata = {"workenv": {"default": {"other_key": "some_value"}}}
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file
        with patch("json.load", return_value=metadata):
            manager = ConcreteTfManager()
            assert manager.get_installed_version() is None


class TestSetInstalledVersionBranches(FoundationTestCase):
    """Test set_installed_version uncovered branches."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_set_version_workenv_already_exists(self, mock_exists: Mock) -> None:
        """Test set when workenv and profile already in metadata (lines 240->242, 242->247)."""
        manager = ConcreteTfManager()
        manager.metadata = {"workenv": {"default": {}}}
        with (
            patch.object(manager, "_save_metadata"),
            patch.object(manager, "_update_recent_file_with_active"),
        ):
            manager.set_installed_version("1.6.0")
            assert manager.metadata["workenv"]["default"]["terraform_version"] == "1.6.0"


class TestRemoveVersionBranches(FoundationTestCase):
    """Test remove_version uncovered branches."""

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.unlink")
    def test_remove_version_deletes_metadata_key(
        self, mock_unlink: Mock, mock_exists: Mock
    ) -> None:
        """Test remove deletes version_key from metadata (lines 263-274)."""
        manager = ConcreteTfManager()
        manager.metadata = {"terraform_1.6.0": {"version": "1.6.0"}}
        with (
            patch.object(manager, "_save_metadata") as mock_save,
            patch.object(manager, "_update_recent_file"),
            patch.object(manager, "get_installed_version", return_value="1.5.0"),
        ):
            manager.remove_version("1.6.0")
            assert "terraform_1.6.0" not in manager.metadata
            mock_save.assert_called()
            mock_unlink.assert_called()

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.unlink")
    def test_remove_version_config_exception_swallowed(
        self, mock_unlink: Mock, mock_exists: Mock
    ) -> None:
        """Test config clear exception is swallowed (lines 278-281)."""
        manager = ConcreteTfManager()
        manager.metadata = {}
        with (
            patch.object(manager, "_save_metadata"),
            patch.object(manager, "_update_recent_file"),
            patch.object(manager, "get_installed_version", return_value="1.6.0"),
            patch.object(manager.config, "set_tool_version", side_effect=Exception("err")),
        ):
            manager.remove_version("1.6.0")


class TestGetGlobalVersionNoGlobal(FoundationTestCase):
    """Test get_global_version when no global key exists."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_get_global_version_no_global(self, mock_exists: Mock) -> None:
        """Test returns None when global not in metadata (line 443)."""
        manager = ConcreteTfManager()
        manager.metadata = {}
        assert manager.get_global_version() is None


class TestGetActiveVersionInfoNone(FoundationTestCase):
    """Test get_active_version_info when no active version."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_get_active_version_info_no_version(self, mock_exists: Mock) -> None:
        """Test returns None when no active version (line 465)."""
        manager = ConcreteTfManager()
        manager.metadata = {}
        assert manager.get_active_version_info() is None

    @patch("pathlib.Path.exists", return_value=False)
    def test_get_active_version_info_no_metadata_entry(self, mock_exists: Mock) -> None:
        """Test returns None when version exists but no metadata entry."""
        manager = ConcreteTfManager()
        manager.metadata = {"workenv": {"default": {"terraform_version": "1.6.0"}}}
        assert manager.get_active_version_info() is None


class TestCreateSymlinkBranches(FoundationTestCase):
    """Test create_symlink branches."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_create_symlink_binary_not_found(self, mock_exists: Mock) -> None:
        """Test create_symlink logs warning when binary missing."""
        manager = ConcreteTfManager()
        with patch.object(manager, "set_installed_version") as mock_set:
            manager.create_symlink("1.6.0")
            mock_set.assert_not_called()

    @patch("pathlib.Path.exists", return_value=True)
    def test_create_symlink_binary_exists(self, mock_exists: Mock) -> None:
        """Test create_symlink calls set_installed_version and copy (lines 390-401)."""
        manager = ConcreteTfManager()
        with (
            patch.object(manager, "set_installed_version") as mock_set,
            patch.object(manager, "_copy_active_binaries_to_venv") as mock_copy,
        ):
            manager.create_symlink("1.6.0")
            mock_set.assert_called_once_with("1.6.0")
            mock_copy.assert_called_once()


class TestUpdateInstallMetadata(FoundationTestCase):
    """Test _update_install_metadata method."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_update_install_metadata(self, mock_exists: Mock, tmp_path: Path) -> None:
        """Test _update_install_metadata populates metadata dict (lines 345-381)."""
        manager = ConcreteTfManager()
        manager.metadata = {}
        archive = tmp_path / "terraform_1.6.0.zip"
        archive.write_bytes(b"fake archive")
        binary = tmp_path / "terraform_1.6.0"
        binary.write_bytes(b"fake binary")
        with (
            patch.object(manager, "get_binary_path", return_value=binary),
            patch.object(manager, "_save_metadata") as mock_save,
            patch.object(manager, "get_platform_info", return_value={"os": "linux"}),
            patch("wrknv.wenv.managers.tf_base.datetime") as mock_dt,
        ):
            mock_dt.now.return_value.isoformat.return_value = "2025-01-01T00:00:00"
            manager._update_install_metadata("1.6.0", archive, "deadbeef")
        assert "terraform_1.6.0" in manager.metadata
        entry = manager.metadata["terraform_1.6.0"]
        assert entry["version"] == "1.6.0"
        assert entry["binary_sha256"] == "deadbeef"
        mock_save.assert_called_once()


class TestCopyActiveBinariesToVenv(FoundationTestCase):
    """Test _copy_active_binaries_to_venv method."""

    @patch("pathlib.Path.exists", return_value=False)
    def test_copy_no_venv_bin_dir(self, mock_exists: Mock) -> None:
        """Test skips copy when venv_bin_dir is None (lines 524-525)."""
        manager = ConcreteTfManager()
        manager.venv_bin_dir = None  # type: ignore[assignment]
        manager._copy_active_binaries_to_venv()

    @patch("pathlib.Path.exists", return_value=False)
    def test_copy_exception_is_swallowed(self, mock_exists: Mock, tmp_path: Path) -> None:
        """Test exception in loop is swallowed (line 562)."""
        import wrknv.wenv.managers.tofu as tofu_mod

        manager = ConcreteTfManager()
        manager.venv_bin_dir = tmp_path / "bin"
        manager.venv_bin_dir.mkdir()
        with patch.object(tofu_mod, "TofuManager", side_effect=Exception("manager error")):
            manager._copy_active_binaries_to_venv()

    @patch("shutil.copy2")
    def test_copy_active_versions_to_venv(self, mock_copy: Mock, tmp_path: Path) -> None:
        """Test copy logic when active tofu version exists (lines 541-560)."""
        import wrknv.wenv.managers.tofu as tofu_mod

        manager = ConcreteTfManager()
        manager.venv_bin_dir = tmp_path / "bin"
        manager.venv_bin_dir.mkdir()
        source = tmp_path / "opentofu_1.6.0"
        source.write_bytes(b"binary")
        mock_tofu_manager = MagicMock()
        mock_tofu_manager.get_installed_version.return_value = "1.6.0"
        mock_tofu_manager.get_binary_path.return_value = source
        with (
            patch.object(tofu_mod, "TofuManager", return_value=mock_tofu_manager),
            patch("pathlib.Path.chmod"),
        ):
            manager._copy_active_binaries_to_venv()
        mock_copy.assert_called()


# 🧰🌍🔚
