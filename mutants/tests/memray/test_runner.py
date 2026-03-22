#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.memray.runner module."""

from __future__ import annotations

from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.memray.runner import run_memray_stress


def _make_stats_output(total: int = 1000) -> str:
    return f"Total allocations:\n    {total}\nOther stats: ignored\n"


def _mock_run(returncode: int = 0, stdout: str = "", stderr: str = "") -> mock.Mock:
    result = mock.Mock()
    result.returncode = returncode
    result.stdout = stdout
    result.stderr = stderr
    return result


class TestRunMemrayStress(FoundationTestCase):
    """Tests for run_memray_stress."""

    def _make_baselines(self, key: str = "test_allocs", value: int = 2000) -> dict:
        return {key: value}

    def test_runs_with_absolute_script_path(self) -> None:
        tmp = self.create_temp_dir()
        script = tmp / "stress_test.py"
        script.write_text("# stub")
        output_dir = self.create_temp_dir()

        with mock.patch("subprocess.run") as mock_subproc:
            mock_subproc.side_effect = [
                _mock_run(returncode=0),
                _mock_run(returncode=0, stdout=_make_stats_output(500)),
            ]
            result = run_memray_stress(
                script=str(script),
                baseline_key="test_allocs",
                output_dir=output_dir,
                baselines=self._make_baselines("test_allocs", 1000),
                baselines_path=output_dir / "baselines.json",
                threshold=0.5,
            )

        assert result == 500
        assert mock_subproc.call_count == 2

    def test_resolves_relative_script_path(self) -> None:
        tmp = self.create_temp_dir()
        output_dir = self.create_temp_dir()
        script_rel = "scripts/memray_stress.py"

        with (
            mock.patch("pathlib.Path.cwd", return_value=tmp),
            mock.patch("pathlib.Path.exists", return_value=True),
            mock.patch("subprocess.run") as mock_subproc,
        ):
            mock_subproc.side_effect = [
                _mock_run(returncode=0),
                _mock_run(returncode=0, stdout=_make_stats_output(300)),
            ]
            result = run_memray_stress(
                script=script_rel,
                baseline_key="test_allocs",
                output_dir=output_dir,
                baselines=self._make_baselines("test_allocs", 1000),
                baselines_path=output_dir / "baselines.json",
                threshold=0.5,
            )

        assert result == 300

    def test_uses_default_output_name_from_script_stem(self) -> None:
        tmp = self.create_temp_dir()
        script = tmp / "memray_mymodule_stress.py"
        script.write_text("# stub")
        output_dir = self.create_temp_dir()

        with mock.patch("subprocess.run") as mock_subproc:
            mock_subproc.side_effect = [
                _mock_run(returncode=0),
                _mock_run(returncode=0, stdout=_make_stats_output(100)),
            ]
            run_memray_stress(
                script=str(script),
                baseline_key="mymodule",
                output_dir=output_dir,
                baselines=self._make_baselines("mymodule", 500),
                baselines_path=output_dir / "baselines.json",
                threshold=0.5,
            )

        # Check that output_file name was derived from script stem
        run_call = mock_subproc.call_args_list[0]
        cmd = run_call[0][0]
        output_arg = cmd[cmd.index("--output") + 1]
        assert "mymodule" in output_arg

    def test_uses_explicit_output_name(self) -> None:
        tmp = self.create_temp_dir()
        script = tmp / "stress.py"
        script.write_text("# stub")
        output_dir = self.create_temp_dir()

        with mock.patch("subprocess.run") as mock_subproc:
            mock_subproc.side_effect = [
                _mock_run(returncode=0),
                _mock_run(returncode=0, stdout=_make_stats_output(100)),
            ]
            run_memray_stress(
                script=str(script),
                baseline_key="custom",
                output_dir=output_dir,
                baselines=self._make_baselines("custom", 500),
                baselines_path=output_dir / "baselines.json",
                output_name="explicit_name",
                threshold=0.5,
            )

        run_call = mock_subproc.call_args_list[0]
        cmd = run_call[0][0]
        output_arg = cmd[cmd.index("--output") + 1]
        assert "explicit_name" in output_arg

    def test_raises_assertion_error_on_memray_run_failure(self) -> None:
        tmp = self.create_temp_dir()
        script = tmp / "stress.py"
        script.write_text("# stub")
        output_dir = self.create_temp_dir()

        with (
            mock.patch("subprocess.run", return_value=_mock_run(returncode=1, stderr="fatal error")),
            pytest.raises(AssertionError, match="Stress script failed"),
        ):
            run_memray_stress(
                script=str(script),
                baseline_key="test",
                output_dir=output_dir,
                baselines={},
                baselines_path=output_dir / "baselines.json",
            )

    def test_raises_assertion_error_on_stats_failure(self) -> None:
        tmp = self.create_temp_dir()
        script = tmp / "stress.py"
        script.write_text("# stub")
        output_dir = self.create_temp_dir()

        with (
            mock.patch("subprocess.run") as mock_subproc,
            pytest.raises(AssertionError, match="memray stats failed"),
        ):
            mock_subproc.side_effect = [
                _mock_run(returncode=0),
                _mock_run(returncode=1, stderr="stats failed"),
            ]
            run_memray_stress(
                script=str(script),
                baseline_key="test",
                output_dir=output_dir,
                baselines={},
                baselines_path=output_dir / "baselines.json",
            )


class TestRelativeScriptPathResolution(FoundationTestCase):
    """Cover lines 69->74 and 70->69: relative script path candidate iteration."""

    @mock.patch("subprocess.run")
    def test_relative_path_resolved_via_parent(self, mock_subproc: mock.Mock) -> None:
        """Line 70->69: first candidate doesn't exist, second (parent) does → resolved."""
        tmp = self.create_temp_dir()
        output_dir = tmp / "output"
        output_dir.mkdir()

        # Put the script in parent of cwd so second candidate matches
        script_name = "memray_relative_stress.py"
        parent_script = tmp / script_name
        parent_script.write_text("# stress script")

        mock_subproc.side_effect = [
            _mock_run(returncode=0),
            _mock_run(returncode=0, stdout=_make_stats_output(500)),
        ]

        with mock.patch("wrknv.memray.runner.Path.cwd", return_value=tmp / "subdir"):
            run_memray_stress(
                script=script_name,
                baseline_key="relative",
                output_dir=output_dir,
                baselines={},
                baselines_path=output_dir / "baselines.json",
            )

    @mock.patch("subprocess.run")
    def test_relative_path_not_found_falls_through(self, mock_subproc: mock.Mock) -> None:
        """Line 69->74: no candidate exists, loop exits without match, uses original path."""
        tmp = self.create_temp_dir()
        output_dir = tmp / "output"
        output_dir.mkdir()

        mock_subproc.side_effect = [
            _mock_run(returncode=0),
            _mock_run(returncode=0, stdout=_make_stats_output(500)),
        ]

        with mock.patch("wrknv.memray.runner.Path.cwd", return_value=tmp / "subdir"):
            # script doesn't exist anywhere → loop exits, uses original relative path
            run_memray_stress(
                script="nonexistent_stress.py",
                baseline_key="notfound",
                output_dir=output_dir,
                baselines={},
                baselines_path=output_dir / "baselines.json",
            )


# 🧰🌍🔚
