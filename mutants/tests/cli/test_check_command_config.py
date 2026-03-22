#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI check command (config validation)."""

from __future__ import annotations

from pathlib import Path

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.commands.check import (
    REQUIRED_PYTEST_SETTINGS,
    _check_project_metadata,
    _check_pytest_config,
    _validate_pyproject,
)
from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    """Get a fresh CLI instance."""
    return create_cli()


# =============================================================================
# TestCheckPytestConfig
# =============================================================================


class TestCheckPytestConfig(FoundationTestCase):
    """Tests for _check_pytest_config()."""

    def _canonical_pytest_config(self) -> dict:
        """Build a fully canonical pytest config dict."""
        return {
            "tool": {
                "pytest": {
                    "ini_options": {
                        "log_cli": True,
                        "testpaths": ["tests"],
                        "python_files": ["test_*.py", "*_test.py"],
                    }
                }
            }
        }

    def test_canonical_config_returns_no_errors(self) -> None:
        """Canonical pytest config produces zero errors."""
        config = self._canonical_pytest_config()
        errors = _check_pytest_config(config)

        assert errors == []

    def test_wrong_log_cli_returns_error(self) -> None:
        """Wrong log_cli value produces an error."""
        config = self._canonical_pytest_config()
        config["tool"]["pytest"]["ini_options"]["log_cli"] = False

        errors = _check_pytest_config(config)

        assert any("log_cli" in e for e in errors)

    def test_wrong_testpaths_returns_error(self) -> None:
        """Wrong testpaths produces an error."""
        config = self._canonical_pytest_config()
        config["tool"]["pytest"]["ini_options"]["testpaths"] = ["src"]

        errors = _check_pytest_config(config)

        assert any("testpaths" in e for e in errors)

    def test_wrong_python_files_returns_error(self) -> None:
        """Wrong python_files produces an error."""
        config = self._canonical_pytest_config()
        config["tool"]["pytest"]["ini_options"]["python_files"] = ["test_*.py"]

        errors = _check_pytest_config(config)

        assert any("python_files" in e for e in errors)

    def test_missing_pytest_section_returns_errors(self) -> None:
        """Missing pytest section causes all checks to fail."""
        config: dict = {}
        errors = _check_pytest_config(config)

        assert len(errors) == len(REQUIRED_PYTEST_SETTINGS)


# =============================================================================
# TestCheckProjectMetadata
# =============================================================================


class TestCheckProjectMetadata(FoundationTestCase):
    """Tests for _check_project_metadata()."""

    def test_canonical_metadata_returns_no_warnings(self) -> None:
        """Canonical metadata produces zero warnings."""
        config = {
            "project": {
                "license": "Apache-2.0",
                "requires-python": ">=3.11",
            }
        }
        warnings = _check_project_metadata(config)

        assert warnings == []

    def test_wrong_license_returns_warning(self) -> None:
        """Non-Apache license produces a warning."""
        config = {
            "project": {
                "license": "MIT",
                "requires-python": ">=3.11",
            }
        }
        warnings = _check_project_metadata(config)

        assert any("license" in w for w in warnings)

    def test_wrong_requires_python_returns_warning(self) -> None:
        """requires-python below 3.11 produces a warning."""
        config = {
            "project": {
                "license": "Apache-2.0",
                "requires-python": ">=3.9",
            }
        }
        warnings = _check_project_metadata(config)

        assert any("requires-python" in w for w in warnings)

    def test_missing_project_section_returns_warnings(self) -> None:
        """Missing project section triggers both warnings."""
        config: dict = {}
        warnings = _check_project_metadata(config)

        assert len(warnings) == 2

    def test_requires_python_311_passes(self) -> None:
        """requires-python exactly >=3.11 passes."""
        config = {
            "project": {
                "license": "Apache-2.0",
                "requires-python": ">=3.11",
            }
        }
        warnings = _check_project_metadata(config)

        assert warnings == []

    def test_requires_python_312_triggers_warning(self) -> None:
        """requires-python >=3.12 triggers a warning (check is exact startswith '>=3.11')."""
        config = {
            "project": {
                "license": "Apache-2.0",
                "requires-python": ">=3.12",
            }
        }
        warnings = _check_project_metadata(config)

        # The implementation does startswith(">=3.11"), so >=3.12 does NOT match
        assert any("requires-python" in w for w in warnings)


# =============================================================================
# TestValidatePyproject
# =============================================================================


class TestValidatePyproject(FoundationTestCase):
    """Tests for _validate_pyproject()."""

    def _write_pyproject(self, directory: Path, content: str) -> Path:
        """Write a pyproject.toml file and return its path."""
        filepath = directory / "pyproject.toml"
        filepath.write_text(content, encoding="utf-8")
        return filepath

    def _canonical_toml(self) -> str:
        """Return a fully canonical pyproject.toml string."""
        return """\
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

    def test_valid_toml_no_errors(self) -> None:
        """Valid canonical TOML returns no errors or warnings."""
        temp_dir = self.create_temp_dir()
        filepath = self._write_pyproject(temp_dir, self._canonical_toml())

        errors, warnings = _validate_pyproject(filepath)

        assert errors == []
        assert warnings == []

    def test_parse_error_returns_error(self) -> None:
        """Returns error tuple when TOML is unparseable."""
        temp_dir = self.create_temp_dir()
        filepath = self._write_pyproject(temp_dir, "this is not valid toml ][")

        errors, warnings = _validate_pyproject(filepath)

        assert len(errors) == 1
        assert "Failed to parse" in errors[0]
        assert warnings == []

    def test_missing_file_returns_error(self) -> None:
        """Returns error tuple when file does not exist."""
        nonexistent = Path("/nonexistent/path/pyproject.toml")

        errors, _warnings = _validate_pyproject(nonexistent)

        assert len(errors) == 1
        assert "Failed to parse" in errors[0]

    def test_config_with_errors(self) -> None:
        """Returns errors for config with violations."""
        temp_dir = self.create_temp_dir()
        toml_content = """\
[tool.ruff]
line-length = 88
"""
        filepath = self._write_pyproject(temp_dir, toml_content)

        errors, _warnings = _validate_pyproject(filepath)

        assert any("line-length" in e for e in errors)

    def test_config_with_warnings(self) -> None:
        """Returns warnings for config with metadata issues."""
        temp_dir = self.create_temp_dir()
        toml_content = """\
[project]
license = "MIT"
requires-python = ">=3.9"

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
        filepath = self._write_pyproject(temp_dir, toml_content)

        errors, warnings = _validate_pyproject(filepath)

        assert errors == []
        assert len(warnings) > 0


# =============================================================================
# TestCheckPyprojectCommand
# =============================================================================


class TestCheckPyprojectCommand(FoundationTestCase):
    """Tests for check_pyproject_command CLI."""

    def _canonical_toml(self) -> str:
        """Return a fully canonical pyproject.toml string."""
        return """\
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

    def test_no_pyproject_in_cwd_exits_1(self) -> None:
        """Exits 1 when no pyproject.toml in cwd and no --path given."""
        cli = get_test_cli()

        with patch("wrknv.cli.commands.check.Path") as mock_path_cls:
            mock_cwd_path = Mock()
            mock_cwd_path.exists.return_value = False
            mock_path_cls.cwd.return_value.__truediv__ = Mock(return_value=mock_cwd_path)

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["check", "pyproject"])

        assert result.exit_code == 1

    def test_missing_explicit_path_exits_1(self) -> None:
        """Exits 1 when positional path points to non-existent file."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()
        nonexistent = temp_dir / "pyproject.toml"

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(nonexistent)])

        assert result.exit_code == 1
        assert "not found" in result.output.lower() or "error" in result.output.lower()

    def test_valid_config_exits_0(self) -> None:
        """Exits 0 for a fully valid canonical pyproject.toml."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "pyproject.toml"
        filepath.write_text(self._canonical_toml(), encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath)])

        assert result.exit_code == 0
        assert "valid" in result.output.lower()

    def test_config_with_errors_exits_1(self) -> None:
        """Exits 1 when pyproject.toml has errors."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "pyproject.toml"
        filepath.write_text("[tool.ruff]\nline-length = 88\n", encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath)])

        assert result.exit_code == 1
        assert "error" in result.output.lower()

    def test_config_with_warnings_exits_0_no_strict(self) -> None:
        """Exits 0 with warnings but no errors in non-strict mode."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        toml_with_warnings = self._canonical_toml().replace('license = "Apache-2.0"', 'license = "MIT"')
        filepath = temp_dir / "pyproject.toml"
        filepath.write_text(toml_with_warnings, encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath)])

        assert result.exit_code == 0

    def test_config_with_warnings_strict_mode_exits_1(self) -> None:
        """Exits 1 in strict mode when warnings are present."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        toml_with_warnings = self._canonical_toml().replace('license = "Apache-2.0"', 'license = "MIT"')
        filepath = temp_dir / "pyproject.toml"
        filepath.write_text(toml_with_warnings, encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath), "--strict"])

        assert result.exit_code == 1

    def test_non_pyproject_filename_is_skipped(self) -> None:
        """Files not named pyproject.toml are skipped."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "other.toml"
        filepath.write_text(self._canonical_toml(), encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath)])

        # Skipped file means all_valid stays True, exits 0
        assert result.exit_code == 0

    def test_path_positional_overrides_cwd(self) -> None:
        """Positional path is used instead of cwd/pyproject.toml."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "pyproject.toml"
        filepath.write_text(self._canonical_toml(), encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath)])

        assert result.exit_code == 0
        assert str(filepath) in result.output


# 🧰🌍🔚
