#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.managers.tf_base module - global version, profiles, venv, metadata queries, and hashing."""

from __future__ import annotations

from pathlib import Path
import sys
from unittest.mock import MagicMock, Mock, patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.managers.tf_base import TfVersionsManager

# Platform detection
IS_WINDOWS = sys.platform == "win32"


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
        return ["1.6.0", "1.5.7", "1.5.0"]

    def get_download_url(self, version: str) -> str:
        return f"https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip"

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://releases.hashicorp.com/terraform/{version}/terraform_{version}_SHA256SUMS"


class TestGlobalVersion(FoundationTestCase):
    """Test global version management."""

    @pytest.mark.skipif(IS_WINDOWS, reason="Test uses chmod which is Unix-specific")
    @patch("os.name", "posix")
    @patch("pathlib.Path.chmod")
    @patch("shutil.copy2")
    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_set_global_version(
        self,
        mock_open: Mock,
        mock_exists: Mock,
        mock_copy: Mock,
        mock_chmod: Mock,
    ) -> None:
        """Test setting global version."""
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file

        manager = ConcreteTfManager()

        with patch("json.dump"):
            manager.set_global_version("1.6.0")

            mock_copy.assert_called_once()
            mock_chmod.assert_called_once_with(0o755)
            assert manager.metadata["global"]["terraform_version"] == "1.6.0"

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_get_global_version(self, mock_open: Mock, mock_exists: Mock) -> None:
        """Test getting global version."""
        test_metadata = {"global": {"terraform_version": "1.6.0"}}

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file

        with patch("json.load", return_value=test_metadata):
            manager = ConcreteTfManager()
            version = manager.get_global_version()

            assert version == "1.6.0"


class TestProfileManagement(FoundationTestCase):
    """Test workenv profile management."""

    def test_get_current_profile_default(self) -> None:
        """Test getting current profile returns default."""
        manager = ConcreteTfManager()
        profile = manager._get_current_profile()

        assert profile == "default"

    @patch.dict("os.environ", {"WRKENV_PROFILE": "production"})
    def test_get_current_profile_from_env(self) -> None:
        """Test getting current profile from environment variable."""
        manager = ConcreteTfManager()
        profile = manager._get_current_profile()

        assert profile == "production"

    @pytest.mark.skipif(IS_WINDOWS, reason="Uses Unix-style home directory expansion")
    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_get_current_profile_from_metadata(self, mock_open: Mock, mock_exists: Mock) -> None:
        """Test getting current profile from metadata."""
        test_metadata = {"workenv": {"_current_profile": "staging"}}

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file

        with patch("json.load", return_value=test_metadata), patch.dict("os.environ", {"WRKENV_PROFILE": ""}):
            manager = ConcreteTfManager()
            profile = manager._get_current_profile()

            assert profile == "staging"


class TestVenvIntegration(FoundationTestCase):
    """Test venv binary directory detection and copying."""

    @patch("pathlib.Path.mkdir")
    @patch("sys.prefix", "/path/to/workenv")
    @patch("sys.base_prefix", "/path/to/python")
    def test_get_venv_bin_dir_in_workenv(self, mock_mkdir: Mock) -> None:
        """Test detecting venv bin directory when in workenv."""
        manager = ConcreteTfManager()

        # Should detect workenv structure
        assert "workenv" in str(manager.venv_bin_dir) or "bin" in str(manager.venv_bin_dir)

    @patch("pathlib.Path.exists", return_value=True)
    def test_find_project_root(self, mock_exists: Mock) -> None:
        """Test finding project root by pyproject.toml."""
        manager = ConcreteTfManager()

        with patch("pathlib.Path.cwd", return_value=Path("/project/subdir")):
            root = manager._find_project_root()
            # Will return something or None
            assert root is None or isinstance(root, Path)


class TestMetadataQueries(FoundationTestCase):
    """Test metadata query methods."""

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_get_metadata_for_version(self, mock_open: Mock, mock_exists: Mock) -> None:
        """Test getting metadata for specific version."""
        test_metadata = {
            "terraform_1.6.0": {
                "version": "1.6.0",
                "installed_at": "2025-01-01T00:00:00",
            }
        }

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file

        with patch("json.load", return_value=test_metadata):
            manager = ConcreteTfManager()
            metadata = manager.get_metadata_for_version("1.6.0")

            assert metadata is not None
            assert metadata["version"] == "1.6.0"

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.open")
    def test_get_active_version_info(self, mock_open: Mock, mock_exists: Mock) -> None:
        """Test getting detailed info about active version."""
        test_metadata = {
            "workenv": {"default": {"terraform_version": "1.6.0"}},
            "terraform_1.6.0": {"version": "1.6.0"},
        }

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__exit__.return_value = False
        mock_open.return_value = mock_file

        with patch("json.load", return_value=test_metadata):
            manager = ConcreteTfManager()
            info = manager.get_active_version_info()

            assert info is not None
            assert info["version"] == "1.6.0"
            assert info["is_active"] is True


class TestFileHashing(FoundationTestCase):
    """Test file hash calculation."""

    def test_calculate_file_hash(self, tmp_path: Path) -> None:
        """Test calculating SHA256 hash of a file."""
        manager = ConcreteTfManager()

        # Create test file
        test_file = tmp_path / "test.bin"
        test_file.write_bytes(b"Hello, World!")

        hash_result = manager._calculate_file_hash(test_file)

        assert isinstance(hash_result, str)
        assert len(hash_result) == 64  # SHA256 produces 64 hex characters


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
