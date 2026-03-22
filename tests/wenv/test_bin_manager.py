#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.bin_manager."""

from __future__ import annotations

import os
import pathlib
import sys
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.bin_manager import copy_tool_binary, find_project_root, get_workenv_bin_dir


class TestGetWorkenvBinDirInVenv(FoundationTestCase):
    """Tests for get_workenv_bin_dir when inside a virtual environment."""

    def test_returns_venv_bin_when_in_venv(self) -> None:
        tmp = self.create_temp_dir()
        bin_dir = tmp / "bin"
        bin_dir.mkdir()
        with (
            mock.patch.object(sys, "prefix", str(tmp)),
            mock.patch.object(sys, "base_prefix", "/real/python"),
        ):
            result = get_workenv_bin_dir(config=None)
        assert result == bin_dir

    @pytest.mark.skipif(os.name != "nt", reason="WindowsPath only instantiable on Windows")
    def test_returns_scripts_dir_on_windows_in_venv(self) -> None:
        tmp = self.create_temp_dir()
        scripts_dir = tmp / "Scripts"
        scripts_dir.mkdir()
        with (
            mock.patch.object(sys, "prefix", str(tmp)),
            mock.patch.object(sys, "base_prefix", "/real/python"),
        ):
            result = get_workenv_bin_dir(config=None)
        assert result == scripts_dir

    def test_creates_bin_dir_when_missing_in_venv(self) -> None:
        tmp = self.create_temp_dir()
        expected_bin = tmp / "bin"
        # Do NOT pre-create bin dir; get_workenv_bin_dir should create it
        with (
            mock.patch.object(sys, "prefix", str(tmp)),
            mock.patch.object(sys, "base_prefix", "/real/python"),
        ):
            result = get_workenv_bin_dir(config=None)
        assert result == expected_bin
        assert expected_bin.is_dir()

    def test_uses_real_prefix_attr_when_present(self) -> None:
        """sys.real_prefix (virtualenv, not venv) also triggers the venv branch."""
        tmp = self.create_temp_dir()
        with (
            mock.patch.object(sys, "prefix", str(tmp)),
            mock.patch.object(sys, "base_prefix", str(tmp)),  # same → no base_prefix trigger
            mock.patch.object(sys, "real_prefix", "/real/python", create=True),
        ):
            result = get_workenv_bin_dir(config=None)
        assert result.parent == tmp


class TestGetWorkenvBinDirNotInVenv(FoundationTestCase):
    """Tests for get_workenv_bin_dir when NOT inside a virtual environment."""

    def _same_prefix_patches(self, prefix: str) -> tuple[mock._patch, mock._patch]:  # type: ignore[type-arg]
        p1 = mock.patch.object(sys, "prefix", prefix)
        p2 = mock.patch.object(sys, "base_prefix", prefix)
        return p1, p2

    def test_returns_workenv_bin_when_project_root_found_with_dir_name_method(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')
        workenv_bin = tmp / "myenv" / "bin"
        workenv_bin.mkdir(parents=True)

        config = mock.Mock()
        config.get_workenv_dir_name.return_value = "myenv"

        p1, p2 = self._same_prefix_patches("/real/python")
        with p1, p2, mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = get_workenv_bin_dir(config=config)
        assert result == workenv_bin

    def test_returns_workenv_bin_when_project_root_found_with_attr(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')
        workenv_bin = tmp / "myenv" / "bin"
        workenv_bin.mkdir(parents=True)

        config = mock.Mock(spec=[])
        config.workenv_dir_name = "myenv"

        p1, p2 = self._same_prefix_patches("/real/python")
        with p1, p2, mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = get_workenv_bin_dir(config=config)
        assert result == workenv_bin

    def test_falls_back_to_local_bin_when_workenv_bin_does_not_exist(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')
        # workenv/myenv/bin does NOT exist

        config = mock.Mock()
        config.get_workenv_dir_name.return_value = "myenv"

        home_tmp = self.create_temp_dir()
        p1, p2 = self._same_prefix_patches("/real/python")
        with p1, p2, mock.patch("pathlib.Path.cwd", return_value=tmp), mock.patch(
            "pathlib.Path.home", return_value=home_tmp
        ):
            result = get_workenv_bin_dir(config=config)
        assert result == home_tmp / ".local" / "bin"

    def test_falls_back_to_local_bin_when_no_project_root(self) -> None:
        home_tmp = self.create_temp_dir()
        p1, p2 = self._same_prefix_patches("/real/python")
        with p1, p2, mock.patch("pathlib.Path.cwd", return_value=pathlib.Path("/tmp/no-project-here")), mock.patch(
            "pathlib.Path.home", return_value=home_tmp
        ):
            result = get_workenv_bin_dir(config=None)
        assert result == home_tmp / ".local" / "bin"

    def test_falls_back_to_local_bin_when_config_is_none(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')

        home_tmp = self.create_temp_dir()
        p1, p2 = self._same_prefix_patches("/real/python")
        with p1, p2, mock.patch("pathlib.Path.cwd", return_value=tmp), mock.patch(
            "pathlib.Path.home", return_value=home_tmp
        ):
            result = get_workenv_bin_dir(config=None)
        assert result == home_tmp / ".local" / "bin"

    def test_falls_back_when_config_has_no_dir_name(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')

        config_plain = type("C", (), {})()  # no workenv_dir_name attr

        home_tmp = self.create_temp_dir()
        p1, p2 = self._same_prefix_patches("/real/python")
        with p1, p2, mock.patch("pathlib.Path.cwd", return_value=tmp), mock.patch(
            "pathlib.Path.home", return_value=home_tmp
        ):
            result = get_workenv_bin_dir(config=config_plain)
        assert result == home_tmp / ".local" / "bin"


class TestFindProjectRoot(FoundationTestCase):
    """Tests for find_project_root traversal."""

    def test_finds_pyproject_in_cwd(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = find_project_root()
        assert result == tmp

    def test_finds_pyproject_in_parent_directory(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "test"\n')
        child = tmp / "subdir" / "nested"
        child.mkdir(parents=True)
        with mock.patch("pathlib.Path.cwd", return_value=child):
            result = find_project_root()
        assert result == tmp

    def test_returns_none_when_no_pyproject_found(self) -> None:
        with mock.patch("pathlib.Path.cwd", return_value=pathlib.Path("/tmp/no-pyproject-here-xyz")):
            result = find_project_root()
        assert result is None


class TestCopyToolBinary(FoundationTestCase):
    """Tests for copy_tool_binary."""

    def test_copies_binary_and_returns_true(self) -> None:
        tmp = self.create_temp_dir()
        source = tmp / "mytool"
        source.write_bytes(b"\x7fELF")
        bin_dir = tmp / "bin"
        bin_dir.mkdir()

        result = copy_tool_binary(source, "mytool", bin_dir)

        assert result is True
        assert (bin_dir / "mytool").exists()

    def test_sets_executable_permission_on_unix(self) -> None:
        tmp = self.create_temp_dir()
        source = tmp / "mytool"
        source.write_bytes(b"\x7fELF")
        bin_dir = tmp / "bin"
        bin_dir.mkdir()

        with mock.patch("wrknv.wenv.bin_manager.os.name", "posix"):
            result = copy_tool_binary(source, "mytool", bin_dir)

        assert result is True
        target = bin_dir / "mytool"
        assert target.stat().st_mode & 0o111  # executable bits set

    @pytest.mark.skipif(os.name != "nt", reason="Windows path semantics only valid on Windows")
    def test_adds_exe_extension_on_windows(self) -> None:
        """On Windows the target binary name gets '.exe' appended before copying."""
        tmp = self.create_temp_dir()
        source = tmp / "mytool"
        source.write_bytes(b"MZ")
        bin_dir = tmp / "bin"
        bin_dir.mkdir()

        result = copy_tool_binary(source, "mytool", bin_dir)

        assert result is True
        assert (bin_dir / "mytool.exe").exists()

    def test_returns_false_when_source_does_not_exist(self) -> None:
        tmp = self.create_temp_dir()
        bin_dir = tmp / "bin"
        bin_dir.mkdir()

        result = copy_tool_binary(tmp / "nonexistent_tool", "mytool", bin_dir)

        assert result is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        source = tmp / "mytool"
        source.write_bytes(b"\x7fELF")
        bin_dir = tmp / "bin"
        bin_dir.mkdir()

        with mock.patch("shutil.copy2", side_effect=OSError("permission denied")):
            result = copy_tool_binary(source, "mytool", bin_dir)

        assert result is False

    def test_does_not_add_exe_on_posix(self) -> None:
        tmp = self.create_temp_dir()
        source = tmp / "mytool"
        source.write_bytes(b"\x7fELF")
        bin_dir = tmp / "bin"
        bin_dir.mkdir()

        with mock.patch("wrknv.wenv.bin_manager.os.name", "posix"):
            copy_tool_binary(source, "mytool", bin_dir)

        assert (bin_dir / "mytool").exists()
        assert not (bin_dir / "mytool.exe").exists()


# 🧰🌍🔚
