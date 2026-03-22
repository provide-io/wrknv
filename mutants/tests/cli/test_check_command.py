#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI check command."""

from __future__ import annotations

from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.commands.check import (
    SPDX_BLOCK,
    _clean_header_lines,
    _construct_file_content,
    _detect_repo_name,
    _find_module_docstring_and_body_start,
    _get_footer_for_current_repo,
    _load_footer_registry,
    _remove_footer_emojis,
)

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

# 🧰🌍🔚
