#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI check command (extended)."""

from __future__ import annotations

from pathlib import Path

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.commands.check import (
    CANONICAL_MYPY,
    _check_mypy_config,
    _check_ruff_config,
    _conform_file,
)
from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    """Get a fresh CLI instance."""
    return create_cli()


# =============================================================================
# TestConformFile
# =============================================================================


class TestConformFile(FoundationTestCase):
    """Tests for _conform_file()."""

    def _make_conformant_file(self, directory: Path, footer: str = "# \U0001f527\U0001f30d\U0001f51a") -> Path:
        """Create a file that is already conformant."""
        filepath = directory / "conformant.py"
        content = (
            "#\n"
            "# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.\n"
            "# SPDX-License-Identifier: Apache-2.0\n"
            "#\n"
            "\n"
            '"""My module."""\n'
            "\n"
            "import os\n"
            "\n"
            f"{footer}\n"
        )
        filepath.write_text(content, encoding="utf-8")
        return filepath

    def test_already_conformant_returns_false(self) -> None:
        """Returns False when file already matches expected content."""
        temp_dir = self.create_temp_dir()
        footer = "# \U0001f527\U0001f30d\U0001f51a"

        filepath = temp_dir / "test.py"
        filepath.write_text('"""My module."""\n\nimport os\n', encoding="utf-8")

        result1 = _conform_file(filepath, footer)
        assert result1 is True

        result2 = _conform_file(filepath, footer)
        assert result2 is False

    def test_nonconformant_file_returns_true(self) -> None:
        """Returns True and modifies file when it needs changes."""
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "needs_fix.py"
        filepath.write_text('"""My module."""\n\nimport os\n', encoding="utf-8")

        result = _conform_file(filepath, "# \U0001f527\U0001f51a")

        assert result is True

    def test_empty_file_gets_placeholder(self) -> None:
        """Creates placeholder content for empty files."""
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "empty.py"
        filepath.write_text("", encoding="utf-8")

        result = _conform_file(filepath, "# \U0001f51a")

        assert result is True
        content = filepath.read_text(encoding="utf-8")
        assert "TODO: Add module docstring" in content
        assert "# \U0001f51a" in content

    def test_read_error_returns_false(self) -> None:
        """Returns False when file cannot be read."""
        temp_dir = self.create_temp_dir()
        nonexistent = temp_dir / "nonexistent.py"

        result = _conform_file(nonexistent, "# \U0001f51a")

        assert result is False

    def test_write_error_returns_false(self) -> None:
        """Returns False when file cannot be written."""
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "readonly.py"
        filepath.write_text('"""Module."""\n\nimport os\n', encoding="utf-8")

        with patch.object(Path, "write_text", side_effect=OSError("permission denied")):
            result = _conform_file(filepath, "# \U0001f51a")

        assert result is False

    def test_executable_file_gets_shebang(self) -> None:
        """Executable files (starting with shebang) keep shebang header."""
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "script.py"
        filepath.write_text('#!/usr/bin/env python3\n\n"""Script."""\n\nprint(\'hi\')\n', encoding="utf-8")

        _conform_file(filepath, "# \U0001f51a")

        content = filepath.read_text(encoding="utf-8")
        assert content.startswith("#!/usr/bin/env python3\n")

    def test_footer_emoji_removed_from_existing_footer(self) -> None:
        """Existing footer emojis are replaced with the new footer."""
        temp_dir = self.create_temp_dir()
        filepath = temp_dir / "has_old_footer.py"
        filepath.write_text(
            '"""Module."""\n\nimport os\n\n# \U0001f527\U0001f30d\U0001f51a\n',
            encoding="utf-8",
        )

        new_footer = "# \U0001f9f0\U0001f51a"
        _conform_file(filepath, new_footer)

        content = filepath.read_text(encoding="utf-8")
        assert new_footer in content


# =============================================================================
# TestCheckSpdxCommand
# =============================================================================


class TestCheckSpdxCommand(FoundationTestCase):
    """Tests for check_spdx_command CLI."""

    def test_no_files_found(self) -> None:
        """Exits 0 with info message when no Python files are found."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.check._get_footer_for_current_repo", return_value="# \U0001f51a"),
            patch("wrknv.cli.commands.check._detect_repo_name", return_value="test-repo"),
            patch("wrknv.cli.commands.check.Path") as mock_path_cls,
        ):
            mock_cwd = Mock()
            mock_cwd.glob.return_value = []
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(
                cli,
                ["check", "spdx", "nonexistent/**/*.py", "--footer", "# \U0001f51a"],
            )

        assert result.exit_code == 0
        assert "No Python files found" in result.output

    def test_check_mode_all_ok(self) -> None:
        """Check mode exits 0 when all files are conformant."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        filepath = temp_dir / "ok.py"
        filepath.write_text('"""Module."""\n\nimport os\n', encoding="utf-8")
        footer = "# \U0001f51a"
        _conform_file(filepath, footer)

        with patch("wrknv.cli.commands.check.Path") as mock_path_cls:
            mock_cwd = Mock()
            mock_cwd.glob.return_value = [filepath]
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["check", "spdx", "*.py", "--footer", footer])

        assert result.exit_code == 0
        assert "All files conform" in result.output

    def test_check_mode_finds_violations(self) -> None:
        """Check mode exits 1 when files need fixes."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        filepath = temp_dir / "bad.py"
        filepath.write_text('"""Module."""\n\nimport os\n', encoding="utf-8")

        with patch("wrknv.cli.commands.check.Path") as mock_path_cls:
            mock_cwd = Mock()
            mock_cwd.glob.return_value = [filepath]
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["check", "spdx", "*.py", "--footer", "# \U0001f51a"])

        assert result.exit_code == 1
        assert "need fixes" in result.output

    def test_fix_mode_modifies_files(self) -> None:
        """Fix mode exits 0 and reports fixed files."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        filepath = temp_dir / "fix_me.py"
        filepath.write_text('"""Module."""\n\nimport os\n', encoding="utf-8")

        with patch("wrknv.cli.commands.check.Path") as mock_path_cls:
            mock_cwd = Mock()
            mock_cwd.glob.return_value = [filepath]
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["check", "spdx", "*.py", "--footer", "# \U0001f51a", "--fix"])

        assert result.exit_code == 0
        assert "fixed" in result.output.lower()

    def test_fix_mode_already_conformant(self) -> None:
        """Fix mode reports OK for already conformant files."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        filepath = temp_dir / "already_ok.py"
        filepath.write_text('"""Module."""\n\nimport os\n', encoding="utf-8")
        footer = "# \U0001f51a"
        _conform_file(filepath, footer)

        with patch("wrknv.cli.commands.check.Path") as mock_path_cls:
            mock_cwd = Mock()
            mock_cwd.glob.return_value = [filepath]
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["check", "spdx", "*.py", "--footer", footer, "--fix"])

        assert result.exit_code == 0
        assert "All files conform" in result.output

    def test_auto_detect_footer_when_not_provided(self) -> None:
        """Auto-detects footer and shows repo name when --footer not given."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.commands.check._get_footer_for_current_repo", return_value="# \U0001f51a"),
            patch("wrknv.cli.commands.check._detect_repo_name", return_value="test-repo"),
            patch("wrknv.cli.commands.check.Path") as mock_path_cls,
        ):
            mock_cwd = Mock()
            mock_cwd.glob.return_value = []
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["check", "spdx"])

        assert "test-repo" in result.output

    def test_error_count_causes_exit_1(self) -> None:
        """Exits 1 when processing errors occur."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        filepath = temp_dir / "error_file.py"
        filepath.write_text('"""Module."""\n', encoding="utf-8")

        with patch("wrknv.cli.commands.check._conform_file", side_effect=RuntimeError("unexpected")):
            runner = click.testing.CliRunner()
            result = runner.invoke(
                cli,
                ["check", "spdx", str(filepath), "--footer", "# \U0001f51a", "--fix"],
            )

        assert result.exit_code == 1


# =============================================================================
# TestCheckRuffConfig
# =============================================================================


class TestCheckRuffConfig(FoundationTestCase):
    """Tests for _check_ruff_config()."""

    def _canonical_ruff_config(self) -> dict:
        """Build a fully canonical ruff config dict."""
        return {
            "tool": {
                "ruff": {
                    "line-length": 111,
                    "indent-width": 4,
                    "target-version": "py311",
                    "lint": {
                        "select": ["E", "F", "W", "I", "UP", "ANN", "B", "C90", "SIM", "PTH", "RUF"],
                        "ignore": ["ANN401", "B008", "E501"],
                    },
                    "format": {
                        "quote-style": "double",
                        "indent-style": "space",
                        "skip-magic-trailing-comma": False,
                        "line-ending": "auto",
                    },
                }
            }
        }

    def test_canonical_config_returns_no_errors(self) -> None:
        """Canonical config produces zero errors."""
        config = self._canonical_ruff_config()
        errors = _check_ruff_config(config)

        assert errors == []

    def test_wrong_line_length_returns_error(self) -> None:
        """Wrong line-length produces an error."""
        config = self._canonical_ruff_config()
        config["tool"]["ruff"]["line-length"] = 88

        errors = _check_ruff_config(config)

        assert any("line-length" in e for e in errors)

    def test_wrong_indent_width_returns_error(self) -> None:
        """Wrong indent-width produces an error."""
        config = self._canonical_ruff_config()
        config["tool"]["ruff"]["indent-width"] = 2

        errors = _check_ruff_config(config)

        assert any("indent-width" in e for e in errors)

    def test_wrong_target_version_returns_error(self) -> None:
        """Wrong target-version produces an error."""
        config = self._canonical_ruff_config()
        config["tool"]["ruff"]["target-version"] = "py39"

        errors = _check_ruff_config(config)

        assert any("target-version" in e for e in errors)

    def test_wrong_lint_select_returns_error(self) -> None:
        """Wrong lint.select produces an error."""
        config = self._canonical_ruff_config()
        config["tool"]["ruff"]["lint"]["select"] = ["E", "F"]

        errors = _check_ruff_config(config)

        assert any("select" in e for e in errors)

    def test_wrong_lint_ignore_returns_error(self) -> None:
        """Wrong lint.ignore produces an error."""
        config = self._canonical_ruff_config()
        config["tool"]["ruff"]["lint"]["ignore"] = []

        errors = _check_ruff_config(config)

        assert any("ignore" in e for e in errors)

    def test_wrong_format_quote_style_returns_error(self) -> None:
        """Wrong format.quote-style produces an error."""
        config = self._canonical_ruff_config()
        config["tool"]["ruff"]["format"]["quote-style"] = "single"

        errors = _check_ruff_config(config)

        assert any("quote-style" in e for e in errors)

    def test_missing_ruff_section_returns_errors(self) -> None:
        """Missing ruff section causes all checks to fail."""
        config: dict = {"tool": {}}
        errors = _check_ruff_config(config)

        assert len(errors) > 0

    def test_empty_config_returns_errors(self) -> None:
        """Empty config causes all checks to fail."""
        errors = _check_ruff_config({})

        assert len(errors) > 0


# =============================================================================
# TestCheckMypyConfig
# =============================================================================


class TestCheckMypyConfig(FoundationTestCase):
    """Tests for _check_mypy_config()."""

    def _canonical_mypy_config(self) -> dict:
        """Build a fully canonical mypy config dict."""
        return {
            "tool": {
                "mypy": {
                    "python_version": "3.11",
                    "strict": True,
                    "pretty": True,
                    "show_error_codes": True,
                    "show_column_numbers": True,
                    "warn_unused_ignores": True,
                    "warn_unused_configs": True,
                }
            }
        }

    def test_canonical_config_returns_no_errors(self) -> None:
        """Canonical mypy config produces zero errors."""
        config = self._canonical_mypy_config()
        errors = _check_mypy_config(config)

        assert errors == []

    def test_wrong_python_version_returns_error(self) -> None:
        """Wrong python_version produces an error."""
        config = self._canonical_mypy_config()
        config["tool"]["mypy"]["python_version"] = "3.9"

        errors = _check_mypy_config(config)

        assert any("python_version" in e for e in errors)

    def test_strict_false_returns_error(self) -> None:
        """strict=False produces an error."""
        config = self._canonical_mypy_config()
        config["tool"]["mypy"]["strict"] = False

        errors = _check_mypy_config(config)

        assert any("strict" in e for e in errors)

    def test_missing_mypy_section_returns_errors(self) -> None:
        """Missing mypy section causes all checks to fail."""
        config: dict = {"tool": {}}
        errors = _check_mypy_config(config)

        assert len(errors) == len(CANONICAL_MYPY)

    def test_all_canonical_keys_checked(self) -> None:
        """All keys in CANONICAL_MYPY are validated."""
        config: dict = {}
        errors = _check_mypy_config(config)

        for key in CANONICAL_MYPY:
            assert any(key in e for e in errors)


# 🧰🌍🔚
