#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for WrknvDoctor."""

from __future__ import annotations

import os
from pathlib import Path
import sys
import tomllib
import types
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.wenv.doctor import WrknvDoctor


def _make_tomli_mock() -> types.ModuleType:
    """Build a mock 'tomli' module backed by stdlib tomllib."""
    m = types.ModuleType("tomli")
    m.load = tomllib.load  # type: ignore[attr-defined]
    return m


_TOMLI_MOCK = _make_tomli_mock()


class TestWrknvDoctorInit(FoundationTestCase):
    """Tests for WrknvDoctor.__init__."""

    def test_init_creates_empty_check_lists(self) -> None:
        doctor = WrknvDoctor()
        assert doctor.checks_passed == []
        assert doctor.checks_failed == []
        assert doctor.checks_warning == []

    def test_init_creates_console(self) -> None:
        doctor = WrknvDoctor()
        assert doctor.console is not None


class TestCheckSystemInfo(FoundationTestCase):
    """Tests for _check_system_info."""

    def test_appends_to_passed(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch.object(doctor.console, "print"):
            doctor._check_system_info()
        assert any("System Info" in check[0] for check in doctor.checks_passed)

    def test_handles_exception(self) -> None:
        doctor = WrknvDoctor()
        with (
            mock.patch("platform.platform", side_effect=RuntimeError("boom")),
            mock.patch.object(doctor.console, "print"),
        ):
            doctor._check_system_info()
        assert any("System Info" in check[0] for check in doctor.checks_failed)


class TestCheckWrknvInstallation(FoundationTestCase):
    """Tests for _check_wrknv_installation."""

    def test_passes_when_installed_and_cli_available(self) -> None:
        doctor = WrknvDoctor()
        mock_result = mock.Mock()
        mock_result.returncode = 0
        with (
            mock.patch("wrknv.wenv.doctor.run", return_value=mock_result),
            mock.patch.object(doctor.console, "print"),
        ):
            doctor._check_wrknv_installation()
        assert any("wrknv Installation" in c[0] for c in doctor.checks_passed)
        assert any("wrknv CLI" in c[0] for c in doctor.checks_passed)

    def test_warns_when_cli_not_in_path(self) -> None:
        doctor = WrknvDoctor()
        mock_result = mock.Mock()
        mock_result.returncode = 1
        with (
            mock.patch("wrknv.wenv.doctor.run", return_value=mock_result),
            mock.patch.object(doctor.console, "print"),
        ):
            doctor._check_wrknv_installation()
        assert any("wrknv CLI" in c[0] for c in doctor.checks_warning)

    def test_warns_on_file_not_found(self) -> None:
        doctor = WrknvDoctor()
        with (
            mock.patch("wrknv.wenv.doctor.run", side_effect=FileNotFoundError),
            mock.patch.object(doctor.console, "print"),
        ):
            doctor._check_wrknv_installation()
        assert any("wrknv CLI" in c[0] for c in doctor.checks_warning)

    def test_fails_on_import_error(self) -> None:
        doctor = WrknvDoctor()
        # Temporarily hide wrknv from sys.modules
        wrknv_mod = sys.modules.get("wrknv")
        try:
            sys.modules["wrknv"] = None  # type: ignore[assignment]
            with mock.patch.object(doctor.console, "print"):
                doctor._check_wrknv_installation()
        finally:
            if wrknv_mod is not None:
                sys.modules["wrknv"] = wrknv_mod
        assert any("wrknv Installation" in c[0] for c in doctor.checks_failed)

    def test_fails_on_unexpected_exception(self) -> None:
        doctor = WrknvDoctor()
        with (
            mock.patch("wrknv.wenv.doctor.run", side_effect=OSError("nope")),
            mock.patch.object(doctor.console, "print"),
        ):
            doctor._check_wrknv_installation()
        assert any("wrknv Installation" in c[0] for c in doctor.checks_failed)


class TestCheckDependencies(FoundationTestCase):
    """Tests for _check_dependencies."""

    def test_all_found(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch("shutil.which", return_value="/usr/bin/something"):
            doctor._check_dependencies()
        assert len(doctor.checks_passed) == 4
        assert len(doctor.checks_failed) == 0
        assert len(doctor.checks_warning) == 0

    def test_uv_not_found_goes_to_failed(self) -> None:
        doctor = WrknvDoctor()

        def which_side(cmd: str) -> str | None:
            return None if cmd == "uv" else "/usr/bin/cmd"

        with mock.patch("shutil.which", side_effect=which_side):
            doctor._check_dependencies()
        assert any("uv" in c[0] for c in doctor.checks_failed)

    def test_optional_dep_not_found_goes_to_warning(self) -> None:
        doctor = WrknvDoctor()

        def which_side(cmd: str) -> str | None:
            return None if cmd == "git" else "/usr/bin/cmd"

        with mock.patch("shutil.which", side_effect=which_side):
            doctor._check_dependencies()
        assert any("git" in c[0] for c in doctor.checks_warning)


class TestCheckWorkenvStructure(FoundationTestCase):
    """Tests for _check_workenv_structure."""

    def test_no_workenv_dir_warns(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent/path")):
            doctor._check_workenv_structure()
        assert any("workenv" in c[0] for c in doctor.checks_warning)

    def test_empty_workenv_warns(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv"
        workenv.mkdir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_workenv_structure()
        assert any("workenv" in c[0] for c in doctor.checks_warning)

    def test_valid_workenv_passes(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv"
        subenv = workenv / "myenv"
        for d in ["bin", "lib", "include"]:
            (subenv / d).mkdir(parents=True)
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_workenv_structure()
        assert any("workenv" in c[0] for c in doctor.checks_passed)

    def test_workenv_with_missing_dirs_warns(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv"
        subenv = workenv / "myenv"
        subenv.mkdir(parents=True)
        # Only create "bin", not "lib" or "include"
        (subenv / "bin").mkdir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_workenv_structure()
        assert any("workenv" in c[0] for c in doctor.checks_warning)

    def test_non_directory_entry_in_workenv_skipped(self) -> None:
        """File entries in workenv/ are skipped (only dirs processed)."""
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        workenv = tmp / "workenv"
        workenv.mkdir()
        (workenv / "somefile.txt").write_text("data")
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_workenv_structure()
        # No passes since first entry is a file, not a dir
        assert not any("workenv/" in c[0] for c in doctor.checks_passed)


class TestCheckEnvScript(FoundationTestCase):
    """Tests for _check_env_script."""

    def test_no_env_script_fails(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent")):
            doctor._check_env_script()
        assert any("env.sh" in c[0] for c in doctor.checks_failed)

    def test_env_script_not_generated_by_wrknv_fails(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "env.sh").write_text("#!/bin/bash\necho hello\n")
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_env_script()
        assert any("env.sh" in c[0] for c in doctor.checks_failed)

    def test_valid_env_script_with_correct_content(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        import platform

        machine = platform.machine().lower()
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine
        system = platform.system().lower()
        pkg = tmp.name
        env_script = tmp / "env.sh"
        content = (
            f"# Generated by wrknv\n"
            f"WORKENV_DIR=workenv/{pkg}_{system}_{arch}\n"
            f"UV_INSTALLER_URL=https://example.com\n"
            f"uv venv\n"
            f"uv sync\n"
        )
        env_script.write_text(content)
        env_script.chmod(0o755)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = str(tmp / "workenv" / f"{pkg}_{system}_{arch}") + "\n"
        # Create the workenv path
        (tmp / "workenv" / f"{pkg}_{system}_{arch}").mkdir(parents=True)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("wrknv.wenv.doctor.run", return_value=mock_result),
        ):
            doctor._check_env_script()
        assert any("env.sh" in c[0] for c in doctor.checks_passed)

    def test_env_script_missing_patterns_fails(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        import platform

        machine = platform.machine().lower()
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine
        system = platform.system().lower()
        pkg = tmp.name
        env_script = tmp / "env.sh"
        # Has the workenv path but missing WORKENV_DIR=
        content = f"# Generated by wrknv\nworkenv/{pkg}_{system}_{arch}\n"
        env_script.write_text(content)
        env_script.chmod(0o755)
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_env_script()
        assert any("env.sh" in c[0] for c in doctor.checks_failed)

    def test_env_script_wrong_workenv_path_fails(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        env_script = tmp / "env.sh"
        content = (
            "# Generated by wrknv\nWORKENV_DIR=workenv/wrong_path_here\nUV_INSTALLER_URL=https://example.com\n"
        )
        env_script.write_text(content)
        env_script.chmod(0o755)
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_env_script()
        assert any("Workenv Path" in c[0] or "env.sh" in c[0] for c in doctor.checks_failed)


class TestTestEnvScriptExecution(FoundationTestCase):
    """Tests for _test_env_script_execution."""

    def test_execution_fails_appends_failed(self) -> None:
        doctor = WrknvDoctor()
        mock_result = mock.Mock()
        mock_result.returncode = 1
        mock_result.stderr = "error!"
        with mock.patch("wrknv.wenv.doctor.run", return_value=mock_result):
            doctor._test_env_script_execution(Path("/fake/env.sh"))
        assert any("env.sh" in c[0] for c in doctor.checks_failed)

    def test_empty_virtual_env_output_fails(self) -> None:
        doctor = WrknvDoctor()
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        with mock.patch("wrknv.wenv.doctor.run", return_value=mock_result):
            doctor._test_env_script_execution(Path("/fake/env.sh"))
        assert any("VIRTUAL_ENV" in c[1] for c in doctor.checks_failed)

    def test_nonexistent_workenv_warns(self) -> None:
        doctor = WrknvDoctor()
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "/nonexistent/path"
        with mock.patch("wrknv.wenv.doctor.run", return_value=mock_result):
            doctor._test_env_script_execution(Path("/fake/env.sh"))
        assert any("Execution" in c[0] for c in doctor.checks_warning)

    def test_timeout_error_appends_failed(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch("wrknv.wenv.doctor.run", side_effect=TimeoutError):
            doctor._test_env_script_execution(Path("/fake/env.sh"))
        assert any("Execution" in c[0] for c in doctor.checks_failed)

    def test_unexpected_exception_appends_failed(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch("wrknv.wenv.doctor.run", side_effect=RuntimeError("weird")):
            doctor._test_env_script_execution(Path("/fake/env.sh"))
        assert any("Execution" in c[0] for c in doctor.checks_failed)


class TestCheckConfigFiles(FoundationTestCase):
    """Tests for _check_config_files."""

    def _with_tomli(self) -> mock._patch[types.ModuleType]:  # type: ignore[type-arg]
        return mock.patch.dict(sys.modules, {"tomli": _TOMLI_MOCK})

    def test_no_config_warns(self) -> None:
        doctor = WrknvDoctor()
        with mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent")), self._with_tomli():
            doctor._check_config_files()
        assert any("wrknv.toml" in c[0] for c in doctor.checks_warning)

    def test_dotfile_fallback_found(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        # Only create .wrknv.toml (not wrknv.toml)
        (tmp / ".wrknv.toml").write_text('[project]\nname = "test"\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp), self._with_tomli():
            doctor._check_config_files()
        assert any("wrknv.toml" in c[0] for c in doctor.checks_passed)

    def test_valid_config_with_project_passes(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[project]\nname = "test"\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp), self._with_tomli():
            doctor._check_config_files()
        assert any("wrknv.toml" in c[0] for c in doctor.checks_passed)

    def test_config_without_project_warns(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[tools]\nterraform = "1.5.0"\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp), self._with_tomli():
            doctor._check_config_files()
        assert any("project" in c[1] for c in doctor.checks_warning)

    def test_config_with_tools_passes(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[project]\nname = "x"\n[tools]\nterraform = "1.5.0"\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp), self._with_tomli():
            doctor._check_config_files()
        assert any("Tools" in c[0] for c in doctor.checks_passed)

    def test_config_with_siblings_passes(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[project]\nname = "x"\n[siblings]\npatterns = ["mypkg"]\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp), self._with_tomli():
            doctor._check_config_files()
        assert any("Sibling" in c[0] for c in doctor.checks_passed)

    def test_invalid_toml_fails(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text("this is not valid TOML !!!")
        with mock.patch("pathlib.Path.cwd", return_value=tmp), self._with_tomli():
            doctor._check_config_files()
        assert any("wrknv.toml" in c[0] for c in doctor.checks_failed)


class TestCheckSiblingPackages(FoundationTestCase):
    """Tests for _check_sibling_packages."""

    def test_no_config_returns_silently(self) -> None:
        doctor = WrknvDoctor()
        with (
            mock.patch("pathlib.Path.cwd", return_value=Path("/nonexistent")),
            mock.patch.dict(sys.modules, {"tomli": _TOMLI_MOCK}),
        ):
            doctor._check_sibling_packages()
        assert len(doctor.checks_passed) == 0
        assert len(doctor.checks_failed) == 0

    def test_sibling_found_passes(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        parent = tmp.parent
        sibling_name = "mysibling"
        # Create the sibling dir
        sibling_path = parent / sibling_name
        sibling_path.mkdir(exist_ok=True)
        (tmp / "wrknv.toml").write_text(f'[siblings]\npatterns = ["{sibling_name}"]\n')
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch.dict(sys.modules, {"tomli": _TOMLI_MOCK}),
        ):
            doctor._check_sibling_packages()
        assert any("Sibling" in c[0] for c in doctor.checks_passed)

    def test_sibling_not_found_warns(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[siblings]\npatterns = ["nonexistent_sibling_xyz"]\n')
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch.dict(sys.modules, {"tomli": _TOMLI_MOCK}),
        ):
            doctor._check_sibling_packages()
        assert any("Sibling" in c[0] for c in doctor.checks_warning)


class TestCheckCommonIssues(FoundationTestCase):
    """Tests for _check_common_issues."""

    def test_venv_directory_warns(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / ".venv").mkdir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_common_issues()
        assert any(".venv" in c[0] for c in doctor.checks_warning)

    def test_conflicting_env_vars_warn(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch.dict(os.environ, {"VIRTUAL_ENV": "/some/venv"}, clear=False),
        ):
            doctor._check_common_issues()
        assert any("Environment Variables" in c[0] for c in doctor.checks_warning)

    def test_no_issues_adds_nothing(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        # No .venv, no conflicting vars, not inside a venv
        with mock.patch("pathlib.Path.cwd", return_value=tmp), mock.patch.dict(os.environ, {}, clear=False):
            env_keys = ["VIRTUAL_ENV", "PYTHONPATH", "PYTHONHOME"]
            saved = {k: os.environ.pop(k) for k in env_keys if k in os.environ}
            with mock.patch.object(sys, "prefix", sys.base_prefix):
                doctor._check_common_issues()
            os.environ.update(saved)
        assert len(doctor.checks_warning) == 0 or all(
            "Virtual" not in c[0] and "Environment" not in c[0] for c in doctor.checks_warning
        )

    def test_inside_venv_warns(self) -> None:
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch.object(sys, "prefix", "/fake/venv"),
            mock.patch.object(sys, "base_prefix", "/real/python"),
        ):
            doctor._check_common_issues()
        assert any("Virtual Environment" in c[0] for c in doctor.checks_warning)


# 🧰🌍🔚
