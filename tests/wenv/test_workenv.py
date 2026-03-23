#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.workenv module."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.wenv.workenv import WorkenvManager


class TestGetWorkenvName(FoundationTestCase):
    """Tests for WorkenvManager.get_workenv_name."""

    def test_x86_64_normalized_to_amd64(self) -> None:
        with mock.patch("platform.machine", return_value="x86_64"):
            name = WorkenvManager.get_workenv_name()
        assert "amd64" in name

    def test_amd64_stays_amd64(self) -> None:
        with mock.patch("platform.machine", return_value="amd64"):
            name = WorkenvManager.get_workenv_name()
        assert "amd64" in name

    def test_arm64_stays_arm64(self) -> None:
        with mock.patch("platform.machine", return_value="arm64"):
            name = WorkenvManager.get_workenv_name()
        assert "arm64" in name

    def test_aarch64_normalized_to_arm64(self) -> None:
        with mock.patch("platform.machine", return_value="aarch64"):
            name = WorkenvManager.get_workenv_name()
        assert "arm64" in name

    def test_includes_system(self) -> None:
        with mock.patch("platform.system", return_value="Darwin"):
            name = WorkenvManager.get_workenv_name()
        assert "darwin" in name

    def test_format_is_wrknv_system_arch(self) -> None:
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            name = WorkenvManager.get_workenv_name()
        assert name == "wrknv_linux_amd64"


class TestGetWorkenvPath(FoundationTestCase):
    """Tests for WorkenvManager.get_workenv_path."""

    def test_uses_provided_base_path(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            path = WorkenvManager.get_workenv_path(tmp)
        assert path == tmp / "workenv" / "wrknv_linux_amd64"

    def test_uses_cwd_when_no_base_path(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            path = WorkenvManager.get_workenv_path()
        assert path.parent.parent == tmp


class TestGetPipPath(FoundationTestCase):
    """Tests for WorkenvManager._get_pip_path."""

    def test_returns_bin_pip_on_unix(self) -> None:
        with mock.patch("platform.system", return_value="Linux"):
            path = WorkenvManager._get_pip_path(Path("/workenv"))
        assert path == Path("/workenv/bin/pip")

    def test_returns_scripts_pip_exe_on_windows(self) -> None:
        with mock.patch("platform.system", return_value="Windows"):
            path = WorkenvManager._get_pip_path(Path("/workenv"))
        assert path == Path("/workenv/Scripts/pip.exe")


class TestGetPythonPath(FoundationTestCase):
    """Tests for WorkenvManager._get_python_path."""

    def test_returns_bin_python_on_unix(self) -> None:
        with mock.patch("platform.system", return_value="Linux"):
            path = WorkenvManager._get_python_path(Path("/workenv"))
        assert path == Path("/workenv/bin/python")

    def test_returns_scripts_python_exe_on_windows(self) -> None:
        with mock.patch("platform.system", return_value="Windows"):
            path = WorkenvManager._get_python_path(Path("/workenv"))
        assert path == Path("/workenv/Scripts/python.exe")


class TestCreateWorkenv(FoundationTestCase):
    """Tests for WorkenvManager.create_workenv."""

    def test_returns_existing_path_when_already_exists(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            workenv_path = WorkenvManager.get_workenv_path(tmp)
            workenv_path.mkdir(parents=True)
            with mock.patch("wrknv.wenv.workenv.print_info"):
                result = WorkenvManager.create_workenv(tmp)
        assert result == workenv_path

    def test_removes_existing_when_force(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            workenv_path = WorkenvManager.get_workenv_path(tmp)
            workenv_path.mkdir(parents=True)
            mock_result = mock.Mock()
            mock_result.returncode = 0
            with (
                mock.patch("wrknv.wenv.workenv.run", return_value=mock_result),
                mock.patch("wrknv.wenv.workenv.print_info"),
                mock.patch("wrknv.wenv.workenv.print_success"),
            ):
                WorkenvManager.create_workenv(tmp, force=True)
        assert not workenv_path.exists()

    def test_calls_venv_and_pip_install(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
        ):
            mock_result = mock.Mock()
            mock_result.returncode = 0
            with (
                mock.patch("wrknv.wenv.workenv.run", return_value=mock_result) as mock_run,
                mock.patch("wrknv.wenv.workenv.print_info"),
                mock.patch("wrknv.wenv.workenv.print_success"),
            ):
                WorkenvManager.create_workenv(tmp)
        assert mock_run.call_count == 3  # venv, pip install -e, pip install -e [dev]


class TestGenerateEnvScripts(FoundationTestCase):
    """Tests for WorkenvManager.generate_env_scripts."""

    def test_creates_env_sh_and_env_ps1(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("wrknv.wenv.workenv.print_info"),
            mock.patch("wrknv.wenv.workenv.print_success"),
        ):
            scripts = WorkenvManager.generate_env_scripts(tmp)
        assert "env.sh" in scripts
        assert "env.ps1" in scripts
        assert scripts["env.sh"].exists()
        assert scripts["env.ps1"].exists()

    def test_does_not_overwrite_existing_env_sh(self) -> None:
        tmp = self.create_temp_dir()
        env_sh = tmp / "env.sh"
        env_sh.write_text("# custom content")
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("wrknv.wenv.workenv.print_info"),
            mock.patch("wrknv.wenv.workenv.print_success"),
        ):
            WorkenvManager.generate_env_scripts(tmp)
        assert env_sh.read_text() == "# custom content"

    def test_uses_cwd_when_no_base_path(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("wrknv.wenv.workenv.print_info"),
            mock.patch("wrknv.wenv.workenv.print_success"),
        ):
            scripts = WorkenvManager.generate_env_scripts()
        assert "env.sh" in scripts


class TestSetupWorkenv(FoundationTestCase):
    """Tests for WorkenvManager.setup_workenv."""

    def test_calls_create_and_generate(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch.object(WorkenvManager, "create_workenv") as mock_create,
            mock.patch.object(WorkenvManager, "generate_env_scripts") as mock_gen,
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("wrknv.wenv.workenv.print_info"),
        ):
            WorkenvManager.setup_workenv(tmp)
        mock_create.assert_called_once_with(tmp, False)
        mock_gen.assert_called_once_with(tmp)

    def test_shows_windows_instructions_on_windows(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch.object(WorkenvManager, "create_workenv"),
            mock.patch.object(WorkenvManager, "generate_env_scripts"),
            mock.patch("platform.system", return_value="Windows"),
            mock.patch("wrknv.wenv.workenv.print_info") as mock_info,
        ):
            WorkenvManager.setup_workenv(tmp)
        calls = [str(c) for c in mock_info.call_args_list]
        assert any("PowerShell" in c for c in calls)

    def test_shows_unix_instructions_on_linux(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch.object(WorkenvManager, "create_workenv"),
            mock.patch.object(WorkenvManager, "generate_env_scripts"),
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("wrknv.wenv.workenv.print_info") as mock_info,
        ):
            WorkenvManager.setup_workenv(tmp)
        calls = [str(c) for c in mock_info.call_args_list]
        assert any("Bash" in c or "source" in c for c in calls)


class TestGetWorkenvNameArchNormalization(FoundationTestCase):
    """Tests for WorkenvManager.get_workenv_name arch normalization branches."""

    def test_unknown_arch_passes_through_unchanged(self) -> None:
        """Line 34->38: machine not arm64/aarch64/x86_64/amd64 → passed through as-is."""
        with (
            mock.patch("platform.system", return_value="Linux"),
            mock.patch("platform.machine", return_value="ppc64le"),
        ):
            name = WorkenvManager.get_workenv_name()
        assert "ppc64le" in name


# 🧰🌍🔚
