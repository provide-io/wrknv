#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#


from __future__ import annotations

import platform
from pathlib import Path
import platform

import pytest
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import MagicMock, patch

from wrknv.config import WorkenvConfig
from wrknv.managers.base import BaseToolManager
from wrknv.managers.tf.ibm import IbmTfVariant


class ConcreteToolManager(BaseToolManager):
    tool_name = "test"
    executable_name = "test"

    def get_download_url(self, version: str) -> str:
        return f"https://example.com/{self.tool_name}/{version}"

    def get_available_versions(self) -> list[str]:
        return ["1.0.0", "1.1.0"]

    def _install_from_archive(self, archive_path: str, version: str) -> None:
        pass

    def get_checksum_url(self, version: str) -> str | None:
        return f"https://example.com/{self.tool_name}/{version}/checksums.txt"


class TestManagers(FoundationTestCase):
    def test_base_tool_manager_init(self) -> None:
        # Arrange
        config = WorkenvConfig()

        # Act
        manager = ConcreteToolManager(config)

        # Assert
        assert manager.config == config

    def test_get_binary_path(self) -> None:
        # Arrange
        config = WorkenvConfig()
        manager = ConcreteToolManager(config)
        executable = manager.executable_name
        if platform.system() == "Windows":
            executable += ".exe"
        expected_path = manager.install_path / manager.tool_name / "1.0.0" / "bin" / executable

        # Act
        binary_path = manager.get_binary_path("1.0.0")

        # Assert
        assert binary_path == expected_path

    @patch("pathlib.Path.iterdir")
    @patch("pathlib.Path.exists", return_value=True)
    def test_get_installed_versions(self, mock_exists, mock_iterdir) -> None:
        # Arrange
        config = WorkenvConfig()
        manager = ConcreteToolManager(config)

        # Create dummy directories for mocking
        mock_install_path = MagicMock(spec=Path)
        mock_tool_install_dir = MagicMock(spec=Path)

        # Create proper mock Path objects with name attributes
        mock_dir_1_0_0 = MagicMock(spec=Path)
        mock_dir_1_0_0.name = "1.0.0"
        mock_dir_1_0_0.is_dir.return_value = True

        mock_dir_1_1_0 = MagicMock(spec=Path)
        mock_dir_1_1_0.name = "1.1.0"
        mock_dir_1_1_0.is_dir.return_value = True

        mock_dir_invalid = MagicMock(spec=Path)
        mock_dir_invalid.name = "invalid"
        mock_dir_invalid.is_dir.return_value = True

        mock_dir_2_0_0 = MagicMock(spec=Path)
        mock_dir_2_0_0.name = "2.0.0"
        mock_dir_2_0_0.is_dir.return_value = True

        mock_tool_install_dir.iterdir.return_value = [
            mock_dir_1_0_0,
            mock_dir_1_1_0,
            mock_dir_invalid,
            mock_dir_2_0_0,
        ]
        mock_install_path.__truediv__.return_value = mock_tool_install_dir
        manager.install_path = mock_install_path

        # Act
        versions = manager.get_installed_versions()

        # Assert
        assert versions == ["2.0.0", "1.1.0", "1.0.0"]


class TestTfBaseInstallFromArchiveMultiFile(FoundationTestCase):
    """Test _install_from_archive selects the correct binary when rglob returns multiple files.

    Covers branch 186->185: the for loop iterates past a non-matching file
    before finding the correct binary.
    """

    @patch("wrknv.managers.tf.base.safe_rmtree")
    @patch("wrknv.managers.tf.base.calculate_file_hash", return_value="abc123")
    @patch("wrknv.managers.tf.base.safe_copy")
    def test_rglob_skips_non_matching_file_and_finds_binary(
        self, mock_safe_copy, mock_hash, mock_rmtree
    ) -> None:
        # Arrange
        config = WorkenvConfig()
        manager = IbmTfVariant(config)

        # Two files returned by rglob: a non-matching sig file first, then the real binary
        non_matching = MagicMock(spec=Path)
        non_matching.name = "terraform.sig"
        non_matching.is_file.return_value = True

        correct_binary = MagicMock(spec=Path)
        correct_binary.name = "terraform"
        correct_binary.is_file.return_value = True

        # mock_extract_dir controls extract_dir = self.cache_dir / "..."
        mock_extract_dir = MagicMock()
        mock_extract_dir.rglob.return_value = iter([non_matching, correct_binary])

        manager.cache_dir = MagicMock()
        manager.cache_dir.__truediv__ = MagicMock(return_value=mock_extract_dir)

        # Stub out all methods that run after the rglob loop
        mock_binary_path = MagicMock()
        manager.get_binary_path = MagicMock(return_value=mock_binary_path)
        manager.extract_archive = MagicMock()
        manager.make_executable = MagicMock()
        manager._update_install_metadata = MagicMock()
        manager._update_recent_file = MagicMock()
        manager.verify_installation = MagicMock(return_value=True)

        # Act
        manager._install_from_archive(Path("/fake/archive.zip"), "1.9.8")

        # Assert: safe_copy was called with the correct binary (not the .sig file)
        mock_safe_copy.assert_called_once()
        first_arg = mock_safe_copy.call_args[0][0]
        assert first_arg == correct_binary


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
