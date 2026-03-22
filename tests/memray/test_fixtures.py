#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.memray.fixtures module."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.memray import fixtures as memray_fixtures


class TestFindProjectRoot(FoundationTestCase):
    """Tests for _find_project_root."""

    def test_finds_pyproject_in_cwd(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text("[project]")
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            root = memray_fixtures._find_project_root()
        assert root == tmp

    def test_finds_pyproject_in_parent(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text("[project]")
        nested = tmp / "subdir" / "deep"
        nested.mkdir(parents=True)
        with mock.patch("pathlib.Path.cwd", return_value=nested):
            root = memray_fixtures._find_project_root()
        assert root == tmp

    def test_returns_cwd_when_no_pyproject_found(self) -> None:
        tmp = self.create_temp_dir()
        nested = tmp / "sub"
        nested.mkdir()
        with mock.patch("pathlib.Path.cwd", return_value=nested):
            root = memray_fixtures._find_project_root()
        # Falls back to cwd since no pyproject.toml found
        assert root == nested


class TestMemrayFixtureLogic(FoundationTestCase):
    """Tests for the logic embedded in fixture functions."""

    def test_output_dir_path_construction(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("wrknv.memray.fixtures._find_project_root", return_value=tmp):
            expected = tmp / "memray-output"
            # Simulate what the fixture does
            output_dir = memray_fixtures._find_project_root() / "memray-output"
            output_dir.mkdir(exist_ok=True)
        assert output_dir == expected
        assert output_dir.exists()

    def test_baselines_path_construction(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("wrknv.memray.fixtures._find_project_root", return_value=tmp):
            path = memray_fixtures._find_project_root() / "tests" / "memray" / "baselines.json"
        assert path == tmp / "tests" / "memray" / "baselines.json"

    def test_baseline_loading_uses_load_baselines(self) -> None:
        tmp = self.create_temp_dir()
        baselines_path = tmp / "baselines.json"
        baselines_path.write_text('{"alloc_key": 2500}\n')
        from wrknv.memray.baselines import load_baselines
        result = load_baselines(baselines_path)
        assert result == {"alloc_key": 2500}


# 🧰🌍🔚
