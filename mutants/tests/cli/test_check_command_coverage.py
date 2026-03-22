#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for cli/commands/check.py uncovered branches."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import click.testing
from provide.testkit import FoundationTestCase

from wrknv.cli.hub_cli import create_cli


def get_test_cli():  # type: ignore[no-untyped-def]
    """Get a fresh CLI instance."""
    return create_cli()


# Minimal valid pyproject.toml (fully canonical — matches all _validate_pyproject checks)
_VALID_PYPROJECT = """\
[project]
license = "Apache-2.0"
requires-python = ">=3.11"

[tool.ruff]
line-length = 111
indent-width = 4
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "ANN", "B", "C90", "SIM", "PTH", "RUF"]
ignore = ["ANN401", "B008", "E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.mypy]
python_version = "3.11"
strict = true
pretty = true
show_error_codes = true
show_column_numbers = true
warn_unused_ignores = true
warn_unused_configs = true

[tool.pytest.ini_options]
log_cli = true
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
"""


def _make_check_spdx_runner(
    cwd: Path, pattern: str = "*.py", footer: str = "# 🧰🌍🔚"
) -> click.testing.Result:
    """Invoke check spdx with cwd mocked to the given directory."""
    cli = get_test_cli()
    runner = click.testing.CliRunner()
    with patch("wrknv.cli.commands.check.Path.cwd", return_value=cwd):
        return runner.invoke(
            cli,
            ["check", "spdx", "--footer", footer, "--pattern", pattern],
        )


class TestCheckSpdxFileNotFound(FoundationTestCase):
    """Lines 275-277: filepath.exists() is False → echo_error + error_count += 1 + continue."""

    def test_glob_returning_nonexistent_path_reports_error(self) -> None:
        """Glob result contains a path that doesn't exist → file-not-found error."""
        cwd = self.create_temp_dir()
        non_existent = cwd / "ghost.py"
        # Do NOT create the file — it exists in the glob result but not on disk
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        with (
            patch("wrknv.cli.commands.check.Path.cwd", return_value=cwd),
            # Directly patch glob to return the non-existent path
            patch.object(Path, "glob", return_value=[non_existent]),
        ):
            result = runner.invoke(
                cli,
                ["check", "spdx", "--footer", "# 🧰🌍🔚", "*.py"],
            )

        assert result.exit_code == 1
        assert "File not found" in result.output


class TestCheckSpdxNonPythonFile(FoundationTestCase):
    """Line 280: filepath.suffix != '.py' → silently continue."""

    def test_non_py_file_is_silently_skipped(self) -> None:
        """A .txt file in the glob result is skipped without error."""
        cwd = self.create_temp_dir()
        txt_file = cwd / "readme.txt"
        txt_file.write_text("some text")
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        with (
            patch("wrknv.cli.commands.check.Path.cwd", return_value=cwd),
            patch.object(Path, "glob", return_value=[txt_file]),
        ):
            result = runner.invoke(
                cli,
                ["check", "spdx", "--footer", "# 🧰🌍🔚", "*.txt"],
            )

        # No files were processed; exits 0 with "All files conform"
        assert result.exit_code == 0


class TestCheckSpdxEmptyFile(FoundationTestCase):
    """Lines 294-296: file.read_text() → empty → echo_info('Would fix') + continue."""

    def test_empty_py_file_counts_as_needs_fix(self) -> None:
        """An empty .py file triggers the 'Would fix' branch (not lines → True)."""
        cwd = self.create_temp_dir()
        empty_file = cwd / "empty.py"
        empty_file.write_text("")
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        with (
            patch("wrknv.cli.commands.check.Path.cwd", return_value=cwd),
            patch.object(Path, "glob", return_value=[empty_file]),
        ):
            result = runner.invoke(
                cli,
                ["check", "spdx", "--footer", "# 🧰🌍🔚", "*.py"],
            )

        assert result.exit_code == 1
        assert "Would fix" in result.output


class TestCheckSpdxExceptionHandler(FoundationTestCase):
    """Lines 317-319: read_text() raises → echo_error + error_count += 1."""

    def test_read_error_triggers_exception_handler(self) -> None:
        """An OSError from read_text is caught and reported."""
        cwd = self.create_temp_dir()
        py_file = cwd / "broken.py"
        py_file.write_text("content")
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        with (
            patch("wrknv.cli.commands.check.Path.cwd", return_value=cwd),
            patch.object(Path, "glob", return_value=[py_file]),
            patch.object(Path, "read_text", side_effect=OSError("perm denied")),
        ):
            result = runner.invoke(
                cli,
                ["check", "spdx", "--footer", "# 🧰🌍🔚", "*.py"],
            )

        assert result.exit_code == 1
        assert "Error processing" in result.output


class TestCheckPyprojectAutoDiscover(FoundationTestCase):
    """Line 479: no path given + pyproject.toml in cwd → filepaths = [pyproject]."""

    def test_auto_discovers_pyproject_in_cwd(self) -> None:
        """Without --path, command auto-discovers pyproject.toml in cwd."""
        cwd = self.create_temp_dir()
        pyproject = cwd / "pyproject.toml"
        pyproject.write_text(_VALID_PYPROJECT, encoding="utf-8")
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        with patch("wrknv.cli.commands.check.Path.cwd", return_value=cwd):
            result = runner.invoke(cli, ["check", "pyproject"])

        assert result.exit_code == 0
        assert "pyproject.toml" in result.output


class TestCheckPyprojectSuccessPath(FoundationTestCase):
    """Line 513->486: valid pyproject with no errors and no warnings → 'Configuration valid'."""

    def test_valid_pyproject_prints_configuration_valid(self) -> None:
        """A fully valid pyproject.toml exits 0 with the success message."""
        cwd = self.create_temp_dir()
        pyproject = cwd / "pyproject.toml"
        pyproject.write_text(_VALID_PYPROJECT, encoding="utf-8")
        cli = get_test_cli()
        runner = click.testing.CliRunner()

        result = runner.invoke(cli, ["check", "pyproject", str(pyproject)])

        assert result.exit_code == 0
        assert "Configuration valid" in result.output


# 🧰🌍🔚
