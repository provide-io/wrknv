#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for package.manager module."""

from __future__ import annotations

from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.config import WorkenvConfig
from wrknv.package.manager import PackageManager


def _make_config() -> WorkenvConfig:
    return WorkenvConfig(project_name="test-pkg", version="1.0.0")


class TestPackageManagerInit(FoundationTestCase):
    """Tests for PackageManager.__init__."""

    def test_stores_config(self) -> None:
        cfg = _make_config()
        manager = PackageManager(cfg)
        assert manager.config is cfg


class TestPackageManagerCheckRequiredTools(FoundationTestCase):
    """Tests for check_required_tools."""

    def test_returns_dict_with_python_and_uv(self) -> None:
        manager = PackageManager(_make_config())
        tools = manager.check_required_tools()
        assert "python" in tools
        assert "uv" in tools

    def test_returns_path_when_tool_found(self) -> None:
        manager = PackageManager(_make_config())
        with mock.patch("shutil.which", return_value="/usr/bin/python"):
            tools = manager.check_required_tools()
        assert tools["python"] == "/usr/bin/python"

    def test_returns_none_when_tool_missing(self) -> None:
        manager = PackageManager(_make_config())
        with mock.patch("shutil.which", return_value=None):
            tools = manager.check_required_tools()
        assert tools["python"] is None
        assert tools["uv"] is None


class TestPackageManagerSetupBuildEnvironment(FoundationTestCase):
    """Tests for setup_build_environment."""

    def test_returns_dict(self) -> None:
        manager = PackageManager(_make_config())
        env = manager.setup_build_environment()
        assert isinstance(env, dict)

    def test_contains_existing_env_vars(self) -> None:
        manager = PackageManager(_make_config())
        with mock.patch.dict("os.environ", {"MY_VAR": "my_val"}):
            env = manager.setup_build_environment()
        assert env["MY_VAR"] == "my_val"


class TestPackageManagerGetPackageCacheDir(FoundationTestCase):
    """Tests for get_package_cache_dir."""

    def test_returns_path_under_home(self) -> None:
        tmp = self.create_temp_dir()
        manager = PackageManager(_make_config())
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = manager.get_package_cache_dir()
        assert result == tmp / ".wrknv" / "cache" / "packages"

    def test_creates_directory(self) -> None:
        tmp = self.create_temp_dir()
        manager = PackageManager(_make_config())
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = manager.get_package_cache_dir()
        assert result.exists()


class TestPackageManagerGetPackageOutputDir(FoundationTestCase):
    """Tests for get_package_output_dir."""

    def test_returns_path_under_home(self) -> None:
        tmp = self.create_temp_dir()
        manager = PackageManager(_make_config())
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = manager.get_package_output_dir()
        assert result == tmp / ".wrknv" / "packages"

    def test_creates_directory(self) -> None:
        tmp = self.create_temp_dir()
        manager = PackageManager(_make_config())
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = manager.get_package_output_dir()
        assert result.exists()


# 🧰🌍🔚
