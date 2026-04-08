#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for WrknvDoctor - summary, recommendations, run, and run_doctor."""

from __future__ import annotations

import tomllib
import types
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.wenv.doctor import WrknvDoctor, run_doctor


def _make_tomli_mock() -> types.ModuleType:
    """Build a mock 'tomli' module backed by stdlib tomllib."""
    m = types.ModuleType("tomli")
    m.load = tomllib.load  # type: ignore[attr-defined]
    return m


_TOMLI_MOCK = _make_tomli_mock()


class TestPrintSummary(FoundationTestCase):
    """Tests for _print_summary."""

    def test_prints_with_all_check_types(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_passed = [("Check A", "OK")]
        doctor.checks_failed = [("Check B", "Failed")]
        doctor.checks_warning = [("Check C", "Warning")]
        printed_calls = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed_calls.append(str(x))):
            doctor._print_summary(verbose=False)
        # Just verify it ran without error; Table/Panel content is not easily inspectable
        assert len(printed_calls) > 0

    def test_print_summary_with_failures_triggers_recommendations(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_failed = [("env.sh", "Missing")]
        with (
            mock.patch.object(doctor.console, "print"),
            mock.patch.object(doctor, "_print_recommendations") as mock_rec,
        ):
            doctor._print_summary(verbose=False)
        mock_rec.assert_called_once()

    def test_print_summary_no_issues_no_recommendations(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_passed = [("Check A", "OK")]
        with (
            mock.patch.object(doctor.console, "print"),
            mock.patch.object(doctor, "_print_recommendations") as mock_rec,
        ):
            doctor._print_summary(verbose=False)
        mock_rec.assert_not_called()


class TestPrintRecommendations(FoundationTestCase):
    """Tests for _print_recommendations."""

    def test_env_sh_failure_recommends_regenerate(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_failed = [("env.sh", "Invalid")]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert "generate" in combined.lower() or "Regenerate" in combined

    def test_uv_missing_recommends_install(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_failed = [("uv", "Required but not found")]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert "uv" in combined

    def test_wrknv_reinstall_recommendation(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_failed = [("wrknv Installation", "Module not found")]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert "wrknv" in combined

    def test_venv_directory_recommendation(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_warning = [(".venv Directory", "Found")]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert ".venv" in combined or "venv" in combined

    def test_virtual_env_recommendation(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_warning = [("Virtual Environment", "Already activated")]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert "deactivate" in combined or "Exit" in combined

    def test_multiple_env_failures_shows_bug_report(self) -> None:
        doctor = WrknvDoctor()
        doctor.checks_failed = [
            ("env.sh", "Missing"),
            ("env.sh Content", "Invalid"),
            ("env.sh Execution", "Failed"),
        ]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert "issues" in combined or "bug" in combined.lower()

    def test_no_duplicate_commands(self) -> None:
        doctor = WrknvDoctor()
        # Two env.sh failures that would both trigger "regenerate" → only one command shown
        doctor.checks_failed = [
            ("env.sh", "Missing"),
            ("env.sh Content", "Also missing"),
        ]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        regen_count = sum(1 for p in printed if "wrknv generate --force" in p)
        assert regen_count == 1


_ALL_CHECK_METHODS = [
    "_check_system_info",
    "_check_wrknv_installation",
    "_check_dependencies",
    "_check_workenv_structure",
    "_check_env_script",
    "_check_config_files",
    "_check_sibling_packages",
    "_check_common_issues",
    "_print_summary",
]


class TestRunMethod(FoundationTestCase):
    """Tests for WrknvDoctor.run()."""

    def test_returns_zero_when_no_failures(self) -> None:
        doctor = WrknvDoctor()
        patches = [mock.patch.object(doctor, m) for m in _ALL_CHECK_METHODS]
        for p in patches:
            p.start()
        try:
            result = doctor.run()
        finally:
            for p in patches:
                p.stop()
        assert result == 0

    def test_returns_one_when_failures(self) -> None:
        doctor = WrknvDoctor()
        patches = [mock.patch.object(doctor, m) for m in _ALL_CHECK_METHODS]
        for p in patches:
            p.start()
        try:
            doctor.checks_failed = [("Something", "Failed")]
            result = doctor.run()
        finally:
            for p in patches:
                p.stop()
        assert result == 1


class TestRunDoctorFunction(FoundationTestCase):
    """Tests for run_doctor() module-level function."""

    def test_returns_exit_code(self) -> None:
        with mock.patch.object(WrknvDoctor, "run", return_value=0) as mock_run:
            result = run_doctor()
        assert result == 0
        mock_run.assert_called_once_with(False)

    def test_passes_verbose_flag(self) -> None:
        with mock.patch.object(WrknvDoctor, "run", return_value=0) as mock_run:
            run_doctor(verbose=True)
        mock_run.assert_called_once_with(True)


class TestDoctorCoverageBranches(FoundationTestCase):
    """Cover uncovered branches in doctor.py."""

    def test_env_script_not_executable_warning(self) -> None:
        """Line 174: env.sh exists but is not executable → warning."""
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        import platform

        machine = platform.machine().lower()
        arch = (
            "amd64"
            if machine in ["x86_64", "amd64"]
            else ("arm64" if machine in ["arm64", "aarch64"] else machine)
        )
        system = platform.system().lower()
        pkg = tmp.name
        env_script = tmp / "env.sh"
        content = (
            f"# Generated by wrknv\n"
            f"WORKENV_DIR=workenv/{pkg}_{system}_{arch}\n"
            f"UV_INSTALLER_URL=https://example.com\n"
            f"uv venv\n"
        )
        env_script.write_text(content)
        env_script.chmod(0o644)  # not executable
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            doctor._check_env_script()
        assert any("Not executable" in msg for _, msg in doctor.checks_warning)

    def test_env_script_x86_64_arch_amd64(self) -> None:
        """Line 180: x86_64 machine maps to amd64 arch in env.sh check."""
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        pkg = tmp.name
        env_script = tmp / "env.sh"
        content = (
            f"# Generated by wrknv\n"
            f"WORKENV_DIR=workenv/{pkg}_linux_amd64\n"
            f"UV_INSTALLER_URL=https://example.com\n"
        )
        env_script.write_text(content)
        env_script.chmod(0o755)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            doctor._check_env_script()
        # Should check for workenv/pkg_linux_amd64 in content
        assert not any("Incorrect pattern" in msg for _, msg in doctor.checks_failed)

    def test_env_script_unknown_arch(self) -> None:
        """Line 184: unknown arch (mips) uses raw machine name."""
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        pkg = tmp.name
        env_script = tmp / "env.sh"
        content = (
            f"# Generated by wrknv\n"
            f"WORKENV_DIR=workenv/{pkg}_linux_mips\n"
            f"UV_INSTALLER_URL=https://example.com\n"
        )
        env_script.write_text(content)
        env_script.chmod(0o755)
        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("platform.machine", return_value="mips"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            doctor._check_env_script()
        assert not any("Incorrect pattern" in msg for _, msg in doctor.checks_failed)

    def test_check_sibling_packages_tomli_exception_is_swallowed(self) -> None:
        """Line 315: exception in _check_sibling_packages is caught and swallowed."""
        doctor = WrknvDoctor()
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[siblings]\npatterns = ["sibling-*"]\n')
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            # Should not raise - tomli ImportError is caught at line 315
            doctor._check_sibling_packages()

    def test_workenv_directory_warning_recommendation(self) -> None:
        """Line 405: workenv Directory warning without env issues → check workenv rec."""
        doctor = WrknvDoctor()
        doctor.checks_warning = [("workenv Directory", "Missing or empty")]
        printed = []
        with mock.patch.object(doctor.console, "print", side_effect=lambda x: printed.append(str(x))):
            doctor._print_recommendations()
        combined = " ".join(printed)
        assert "workenv" in combined.lower() or "doctor" in combined.lower()


# 🧰🌍🔚
