#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for testing.helpers module."""

from __future__ import annotations

import os
from pathlib import Path
import platform
import re
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.testing.helpers import (
    WorkenvTestRunner,
    activate_workenv,
    get_workenv_dir,
    workenv_context,
)


class TestGetWorkenvDir(FoundationTestCase):
    """Tests for get_workenv_dir."""

    def test_uses_cwd_name_by_default(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = get_workenv_dir()
        assert result.name.startswith(tmp.name + "_")

    def test_uses_provided_package_name(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = get_workenv_dir("mypkg")
        assert result.name.startswith("mypkg_")

    def test_includes_platform_system(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = get_workenv_dir("pkg")
        system = platform.system().lower()
        assert system in result.name

    def test_normalizes_x86_64_to_amd64(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            result = get_workenv_dir("pkg")
        assert "amd64" in result.name

    def test_normalizes_arm64(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="arm64"),
        ):
            result = get_workenv_dir("pkg")
        assert "arm64" in result.name

    def test_normalizes_aarch64_to_arm64(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="aarch64"),
        ):
            result = get_workenv_dir("pkg")
        assert "arm64" in result.name

    def test_unknown_arch_uses_raw_value(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="mips"),
        ):
            result = get_workenv_dir("pkg")
        assert "mips" in result.name

    def test_result_is_under_workenv_subdir(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            result = get_workenv_dir("pkg")
        assert result.parent == tmp / "workenv"


class TestActivateWorkenv(FoundationTestCase):
    """Tests for activate_workenv."""

    def test_raises_when_workenv_not_found(self) -> None:
        with (
            mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent")),
            pytest.raises(RuntimeError, match=re.escape("Workenv directory not found")),
        ):
            activate_workenv("mypkg")

    def test_sets_virtual_env(self) -> None:
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv" / "mypkg_linux_amd64"
        workenv.mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            env = activate_workenv("mypkg")
        assert env["VIRTUAL_ENV"] == str(workenv)

    def test_adds_bin_to_path_when_bin_exists(self) -> None:
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv" / "mypkg_linux_amd64"
        (workenv / "bin").mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            env = activate_workenv("mypkg")
        assert str(workenv / "bin") in env["PATH"]

    def test_removes_pythonhome(self) -> None:
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv" / "mypkg_linux_amd64"
        workenv.mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
            mock.patch.dict(os.environ, {"PYTHONHOME": "/fake"}),
        ):
            env = activate_workenv("mypkg")
        assert "PYTHONHOME" not in env


class TestWorkenvContext(FoundationTestCase):
    """Tests for workenv_context."""

    def test_raises_when_workenv_not_found(self) -> None:
        with (
            mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent")),
            pytest.raises(RuntimeError),workenv_context("mypkg")
        ):
            pass

    def test_restores_environment_after_exception(self) -> None:
        original_env = os.environ.copy()
        with mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent")):
            try:
                with workenv_context("mypkg"):
                    pass
            except RuntimeError:
                pass
        assert os.environ == original_env


class TestWorkenvTestRunner(FoundationTestCase):
    """Tests for WorkenvTestRunner."""

    def test_init_with_no_package_name(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            runner = WorkenvTestRunner()
        assert runner.package_name == tmp.name

    def test_init_with_package_name(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            runner = WorkenvTestRunner("mypkg")
        assert runner.package_name == "mypkg"

    def test_workenv_dir_set_on_init(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            runner = WorkenvTestRunner("mypkg")
        assert runner.workenv_dir is not None
        assert "mypkg" in runner.workenv_dir.name

    def test_setup_raises_when_no_env_script(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            runner = WorkenvTestRunner("mypkg")
            with pytest.raises(RuntimeError, match=re.escape("env.sh not found")):
                runner.setup()

    def test_setup_force_removes_existing_workenv(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            runner = WorkenvTestRunner("mypkg")
        # Create env.sh and workenv dir
        env_script = tmp / "env.sh"
        env_script.write_text("#!/bin/bash")
        runner.workenv_dir.mkdir(parents=True)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("wrknv.testing.helpers.run", return_value=mock_result),
        ):
            runner.setup(force=True)
        # workenv was removed then re-created by env.sh (mocked run)
        assert not runner.workenv_dir.exists()  # force removed it

    def test_run_uses_activate_workenv(self) -> None:
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv" / "mypkg_linux_amd64"
        workenv.mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            runner = WorkenvTestRunner("mypkg")
        mock_result = mock.Mock()
        with (
            mock.patch("wrknv.testing.helpers.run", return_value=mock_result) as mock_run,
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            runner.run(["echo", "hello"])
        mock_run.assert_called_once()

    def test_install_deps_calls_run(self) -> None:
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv" / "mypkg_linux_amd64"
        workenv.mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            runner = WorkenvTestRunner("mypkg")
        mock_result = mock.Mock()
        with (
            mock.patch("wrknv.testing.helpers.run", return_value=mock_result) as mock_run,
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            runner.install_deps()
        mock_run.assert_called_once()

    def test_install_deps_with_extras(self) -> None:
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv" / "mypkg_linux_amd64"
        workenv.mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            runner = WorkenvTestRunner("mypkg")
        mock_result = mock.Mock()
        with (
            mock.patch("wrknv.testing.helpers.run", return_value=mock_result) as mock_run,
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            runner.install_deps(extras="dev")
        call_args = mock_run.call_args[0][0]
        assert any(".[dev]" in arg for arg in call_args)


# 🧰🌍🔚
