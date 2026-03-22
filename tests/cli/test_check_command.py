#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI check command."""

from __future__ import annotations

from pathlib import Path

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch
import pytest

from wrknv.cli.commands.check import (
    CANONICAL_MYPY,
    REQUIRED_PYTEST_SETTINGS,
    SPDX_BLOCK,
    _check_mypy_config,
    _check_project_metadata,
    _check_pytest_config,
    _check_ruff_config,
    _clean_header_lines,
    _conform_file,
    _construct_file_content,
    _detect_repo_name,
    _find_module_docstring_and_body_start,
    _get_footer_for_current_repo,
    _load_footer_registry,
    _remove_footer_emojis,
    _validate_pyproject,
)
from wrknv.cli.hub_cli import create_cli


def get_test_cli():
    """Get a fresh CLI instance."""
    return create_cli()


# =============================================================================
# TestDetectRepoName
# =============================================================================


class TestDetectRepoName(FoundationTestCase):
    """Tests for _detect_repo_name()."""

    def test_success_ssh_url(self) -> None:
        """Returns repo name from SSH remote URL."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "git@github.com:provide-io/wrknv.git\n"

        with patch("wrknv.cli.commands.check.process_run", return_value=mock_result):
            result = _detect_repo_name()

        assert result == "wrknv"

    def test_success_https_url(self) -> None:
        """Returns repo name from HTTPS remote URL."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "https://github.com/provide-io/my-repo.git\n"

        with patch("wrknv.cli.commands.check.process_run", return_value=mock_result):
            result = _detect_repo_name()

        assert result == "my-repo"

    def test_success_url_without_git_suffix(self) -> None:
        """Returns repo name from URL without .git suffix."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "https://github.com/provide-io/my-repo\n"

        with patch("wrknv.cli.commands.check.process_run", return_value=mock_result):
            result = _detect_repo_name()

        assert result == "my-repo"

    def test_nonzero_returncode_falls_back_to_cwd(self) -> None:
        """Falls back to cwd name when git returns non-zero exit code."""
        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stdout = ""

        with (
            patch("wrknv.cli.commands.check.process_run", return_value=mock_result),
            patch("wrknv.cli.commands.check.Path") as mock_path_cls,
        ):
            mock_path_cls.cwd.return_value.name = "my-project"
            result = _detect_repo_name()

        assert result == "my-project"

    def test_exception_falls_back_to_cwd(self) -> None:
        """Falls back to cwd name when process_run raises an exception."""
        with (
            patch("wrknv.cli.commands.check.process_run", side_effect=OSError("no git")),
            patch("wrknv.cli.commands.check.Path") as mock_path_cls,
        ):
            mock_path_cls.cwd.return_value.name = "fallback-name"
            result = _detect_repo_name()

        assert result == "fallback-name"

    def test_empty_repo_name_falls_back_to_cwd(self) -> None:
        """Falls back to cwd name when extracted repo name is empty."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "   \n"

        with (
            patch("wrknv.cli.commands.check.process_run", return_value=mock_result),
            patch("wrknv.cli.commands.check.Path") as mock_path_cls,
        ):
            mock_path_cls.cwd.return_value.name = "cwd-name"
            result = _detect_repo_name()

        assert result == "cwd-name"


# =============================================================================
# TestLoadFooterRegistry
# =============================================================================


class TestLoadFooterRegistry(FoundationTestCase):
    """Tests for _load_footer_registry()."""

    def test_success_reads_actual_file(self) -> None:
        """Loads registry from actual bundled JSON file."""
        result = _load_footer_registry()

        assert isinstance(result, dict)
        assert "wrknv" in result
        assert result["wrknv"] == "# \U0001f527\U0001f30d\U0001f51a"

    def test_file_not_found_returns_empty_dict(self) -> None:
        """Returns empty dict when registry file does not exist."""
        import wrknv.cli.commands.check as check_mod

        with patch.object(check_mod, "__file__", "/nonexistent/path/check.py"):
            result = _load_footer_registry()

        assert result == {}

    def test_invalid_json_returns_empty_dict(self) -> None:
        """Returns empty dict when registry file contains invalid JSON."""
        temp_dir = self.create_temp_dir()
        bad_file = temp_dir / "footer_registry.json"
        bad_file.write_text("{ invalid json }")

        import wrknv.cli.commands.check as check_mod

        with patch.object(check_mod, "__file__", str(temp_dir / "commands" / "check.py")):
            (temp_dir / "commands").mkdir(exist_ok=True)
            result = _load_footer_registry()

        assert result == {}

    def test_registry_contains_expected_repos(self) -> None:
        """Actual registry contains known repository entries."""
        result = _load_footer_registry()

        assert "provide-foundation" in result
        assert "provide-testkit" in result
        assert "wrknv" in result


# =============================================================================
# TestGetFooterForCurrentRepo
# =============================================================================


class TestGetFooterForCurrentRepo(FoundationTestCase):
    """Tests for _get_footer_for_current_repo()."""

    def test_known_repo_returns_registry_footer(self) -> None:
        """Returns footer from registry for a known repo name."""
        registry = {"my-repo": "# \U0001f527\U0001f51a", "other": "# \U0001f30d\U0001f51a"}

        with (
            patch("wrknv.cli.commands.check._detect_repo_name", return_value="my-repo"),
            patch("wrknv.cli.commands.check._load_footer_registry", return_value=registry),
        ):
            result = _get_footer_for_current_repo()

        assert result == "# \U0001f527\U0001f51a"

    def test_unknown_repo_returns_default_footer(self) -> None:
        """Returns default footer when repo not in registry."""
        registry = {"other-repo": "# \U0001f527\U0001f51a"}

        with (
            patch("wrknv.cli.commands.check._detect_repo_name", return_value="unknown-repo"),
            patch("wrknv.cli.commands.check._load_footer_registry", return_value=registry),
        ):
            result = _get_footer_for_current_repo()

        assert result == "# \U0001f51a"

    def test_empty_registry_returns_default_footer(self) -> None:
        """Returns default footer when registry is empty."""
        with (
            patch("wrknv.cli.commands.check._detect_repo_name", return_value="any-repo"),
            patch("wrknv.cli.commands.check._load_footer_registry", return_value={}),
        ):
            result = _get_footer_for_current_repo()

        assert result == "# \U0001f51a"


# =============================================================================
# TestFindModuleDocstringAndBodyStart
# =============================================================================


class TestFindModuleDocstringAndBodyStart(FoundationTestCase):
    """Tests for _find_module_docstring_and_body_start()."""

    def test_with_docstring(self) -> None:
        """Extracts docstring and returns body start after it."""
        content = '"""My module docstring."""\n\nimport os\n\nx = 1\n'
        docstring, body_start = _find_module_docstring_and_body_start(content)

        assert docstring == "My module docstring."
        assert body_start == 3  # import os is line 3

    def test_without_docstring(self) -> None:
        """Returns None docstring when no module docstring present."""
        content = "import os\n\nx = 1\n"
        docstring, body_start = _find_module_docstring_and_body_start(content)

        assert docstring is None
        assert body_start == 1  # import os is line 1

    def test_empty_content(self) -> None:
        """Returns None docstring and end-of-file for empty content."""
        content = ""
        docstring, _body_start = _find_module_docstring_and_body_start(content)

        assert docstring is None

    def test_only_docstring_no_body(self) -> None:
        """Returns docstring and end+1 line when only docstring present."""
        content = '"""Just a docstring."""\n'
        docstring, body_start = _find_module_docstring_and_body_start(content)

        assert docstring == "Just a docstring."
        assert body_start == 2  # past end of file

    def test_syntax_error_returns_none(self) -> None:
        """Returns None docstring and line 1 for syntactically invalid content."""
        content = "def broken(\n    x\n"  # unclosed function
        docstring, body_start = _find_module_docstring_and_body_start(content)

        assert docstring is None
        assert body_start == 1

    def test_multiline_docstring(self) -> None:
        """Handles multiline docstrings correctly."""
        content = '"""First line.\n\nSecond paragraph."""\n\nimport os\n'
        docstring, body_start = _find_module_docstring_and_body_start(content)

        assert docstring is not None
        assert "First line." in docstring
        assert body_start >= 5  # after the docstring + blank line


# =============================================================================
# TestCleanHeaderLines
# =============================================================================


class TestCleanHeaderLines(FoundationTestCase):
    """Tests for _clean_header_lines()."""

    def test_removes_shebang(self) -> None:
        """Removes shebang line from output."""
        lines = ["#!/usr/bin/env python3\n", "import os\n"]
        result = _clean_header_lines(lines)

        assert not any(line.startswith("#!") for line in result)
        assert any("import os" in line for line in result)

    def test_removes_spdx_copyright(self) -> None:
        """Removes SPDX-FileCopyrightText line."""
        lines = [
            "# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.\n",
            "import os\n",
        ]
        result = _clean_header_lines(lines)

        assert not any("SPDX-FileCopyrightText" in line for line in result)

    def test_removes_spdx_license(self) -> None:
        """Removes SPDX-License-Identifier line."""
        lines = [
            "# SPDX-License-Identifier: Apache-2.0\n",
            "import os\n",
        ]
        result = _clean_header_lines(lines)

        assert not any("SPDX-License-Identifier" in line for line in result)

    def test_removes_hash_only_line(self) -> None:
        """Removes bare '#' comment lines."""
        lines = ["#\n", "import os\n"]
        result = _clean_header_lines(lines)

        assert not any(line.strip() == "#" for line in result)

    def test_removes_placeholder_docstring(self) -> None:
        """Removes placeholder TODO docstring."""
        lines = ['"""TODO: Add module docstring."""\n', "import os\n"]
        result = _clean_header_lines(lines)

        assert not any("TODO: Add module docstring" in line for line in result)

    def test_skip_next_empty_after_shebang(self) -> None:
        """Skips the blank line immediately after a removed shebang."""
        lines = ["#!/usr/bin/env python3\n", "\n", "import os\n"]
        result = _clean_header_lines(lines)

        # The blank line after shebang should be removed
        assert result == ["import os\n"]

    def test_skip_next_empty_after_spdx(self) -> None:
        """Skips the blank line immediately after a removed SPDX line."""
        lines = ["# SPDX-License-Identifier: Apache-2.0\n", "\n", "import os\n"]
        result = _clean_header_lines(lines)

        assert result == ["import os\n"]

    def test_non_empty_line_after_removed_line_is_kept(self) -> None:
        """Does not skip a non-empty line after a removed header line."""
        lines = ["#\n", "import os\n"]
        result = _clean_header_lines(lines)

        assert "import os\n" in result

    def test_normal_lines_pass_through(self) -> None:
        """Preserves non-header lines unchanged."""
        lines = ["import os\n", "x = 1\n", "\n"]
        result = _clean_header_lines(lines)

        assert result == lines

    def test_full_spdx_block_removal(self) -> None:
        """Removes a complete SPDX block and trailing blank line."""
        lines = [
            "#\n",
            "# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.\n",
            "# SPDX-License-Identifier: Apache-2.0\n",
            "#\n",
            "\n",
            '"""My module."""\n',
        ]
        result = _clean_header_lines(lines)

        assert '"""My module."""\n' in result
        assert not any("SPDX" in line for line in result)


# =============================================================================
# TestRemoveFooterEmojis
# =============================================================================


class TestRemoveFooterEmojis(FoundationTestCase):
    """Tests for _remove_footer_emojis()."""

    def test_removes_line_with_construction_emoji(self) -> None:
        """Removes line containing 🏗️ emoji."""
        content = "import os\n\n# \U0001f3d7\ufe0f\U0001f4da\U0001f51a"
        result = _remove_footer_emojis(content)

        assert "\U0001f3d7" not in result
        assert "import os" in result

    def test_removes_line_with_toolbox_emoji(self) -> None:
        """Removes line containing 🧰 emoji."""
        content = "x = 1\n\n# \U0001f9f0\U0001f30d\U0001f51a"
        result = _remove_footer_emojis(content)

        assert "\U0001f9f0" not in result
        assert "x = 1" in result

    def test_removes_line_with_end_flag_emoji(self) -> None:
        """Removes line containing 🔚 emoji."""
        content = "def foo():\n    pass\n\n# \U0001f527\U0001f51a"
        result = _remove_footer_emojis(content)

        assert "\U0001f51a" not in result
        assert "def foo():" in result

    def test_preserves_lines_without_footer_emojis(self) -> None:
        """Preserves lines that contain no footer emojis."""
        content = "import os\nx = 1\n# normal comment"
        result = _remove_footer_emojis(content)

        assert result == content.rstrip()

    def test_strips_trailing_whitespace(self) -> None:
        """Strips trailing whitespace from result."""
        content = "import os\n\n"
        result = _remove_footer_emojis(content)

        assert result == "import os"

    def test_empty_content(self) -> None:
        """Handles empty content."""
        result = _remove_footer_emojis("")

        assert result == ""


# =============================================================================
# TestConstructFileContent
# =============================================================================


class TestConstructFileContent(FoundationTestCase):
    """Tests for _construct_file_content()."""

    def test_with_non_empty_body(self) -> None:
        """Constructs content with header, docstring, body, and footer."""
        header_first_line = "#"
        docstring_str = '"""My module."""'
        body_content = "import os\n\nx = 1"
        footer = "# \U0001f527\U0001f51a"

        result = _construct_file_content(header_first_line, docstring_str, body_content, footer)

        assert result.startswith("#\n")
        for spdx_line in SPDX_BLOCK:
            assert spdx_line in result
        assert '"""My module."""' in result
        assert "import os" in result
        assert footer in result
        assert result.endswith("\n")

    def test_with_empty_body(self) -> None:
        """Constructs content without body section when body is empty."""
        header_first_line = "#"
        docstring_str = '"""My module."""'
        body_content = ""
        footer = "# \U0001f527\U0001f51a"

        result = _construct_file_content(header_first_line, docstring_str, body_content, footer)

        assert '"""My module."""' in result
        assert footer in result
        assert result.endswith("\n")

    def test_executable_header(self) -> None:
        """Uses shebang line for executable files."""
        header_first_line = "#!/usr/bin/env python3"
        docstring_str = '"""Script."""'
        body_content = "print('hello')"
        footer = "# \U0001f51a"

        result = _construct_file_content(header_first_line, docstring_str, body_content, footer)

        assert result.startswith("#!/usr/bin/env python3\n")

    def test_spdx_block_present(self) -> None:
        """All SPDX_BLOCK lines are present in output."""
        result = _construct_file_content("#", '"""Doc."""', "pass", "# \U0001f51a")

        for line in SPDX_BLOCK:
            assert line in result


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

        # Write a file and run _conform_file to get conformant version
        filepath = temp_dir / "test.py"
        filepath.write_text('"""My module."""\n\nimport os\n', encoding="utf-8")

        # First call will modify
        result1 = _conform_file(filepath, footer)
        assert result1 is True

        # Second call should be idempotent
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
        filepath.write_text("#!/usr/bin/env python3\n\n\"\"\"Script.\"\"\"\n\nprint('hi')\n", encoding="utf-8")

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
            # pattern is the first positional argument; --footer is the option
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

        # Create a conformant file first by running conform on it
        filepath = temp_dir / "ok.py"
        filepath.write_text('"""Module."""\n\nimport os\n', encoding="utf-8")
        footer = "# \U0001f51a"
        _conform_file(filepath, footer)

        with patch("wrknv.cli.commands.check.Path") as mock_path_cls:
            mock_cwd = Mock()
            mock_cwd.glob.return_value = [filepath]
            mock_path_cls.cwd.return_value = mock_cwd

            runner = click.testing.CliRunner()
            result = runner.invoke(
                cli,
                ["check", "spdx", "*.py", "--footer", footer],
            )

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
            result = runner.invoke(
                cli,
                ["check", "spdx", "*.py", "--footer", "# \U0001f51a"],
            )

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
            result = runner.invoke(
                cli,
                ["check", "spdx", "*.py", "--footer", "# \U0001f51a", "--fix"],
            )

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
            result = runner.invoke(
                cli,
                ["check", "spdx", "*.py", "--footer", footer, "--fix"],
            )

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
        # path is the first positional argument
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

        toml_with_warnings = self._canonical_toml().replace(
            'license = "Apache-2.0"', 'license = "MIT"'
        )
        filepath = temp_dir / "pyproject.toml"
        filepath.write_text(toml_with_warnings, encoding="utf-8")

        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["check", "pyproject", str(filepath)])

        assert result.exit_code == 0

    def test_config_with_warnings_strict_mode_exits_1(self) -> None:
        """Exits 1 in strict mode when warnings are present."""
        cli = get_test_cli()
        temp_dir = self.create_temp_dir()

        toml_with_warnings = self._canonical_toml().replace(
            'license = "Apache-2.0"', 'license = "MIT"'
        )
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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
