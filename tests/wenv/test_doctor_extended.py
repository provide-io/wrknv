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


# 🧰🌍🔚
