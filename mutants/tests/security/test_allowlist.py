#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""Tests for SecurityAllowlistManager."""

from __future__ import annotations

from pathlib import Path
import re
from unittest.mock import patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.security.allowlist import SecurityAllowlistManager, glob_to_regex
from wrknv.security.config import SecurityConfig


def make_config(
    description: str = "Test allowlist",
    allowed_paths: list[str] | None = None,
) -> SecurityConfig:
    """Create a SecurityConfig for tests."""
    if allowed_paths is None:
        allowed_paths = ["tests/certs/*.key", "docs/**/*.md"]
    return SecurityConfig(description=description, allowed_paths=allowed_paths)


# ---------------------------------------------------------------------------
# TestGlobToRegex
# ---------------------------------------------------------------------------


class TestGlobToRegex(FoundationTestCase):
    """Tests for glob_to_regex()."""

    def test_single_star_does_not_match_slash(self) -> None:
        """* matches one directory level but not path separators."""
        pattern = "tests/certs/*.key"
        regex = glob_to_regex(pattern)
        # should match a file directly in tests/certs/
        assert re.search(regex, "tests/certs/mykey.key")
        # should NOT match across a directory boundary
        assert not re.search(regex, "tests/certs/sub/mykey.key")

    def test_double_star_matches_across_dirs(self) -> None:
        """** matches across directory boundaries."""
        pattern = "docs/**/*.md"
        regex = glob_to_regex(pattern)
        # direct child
        assert re.search(regex, "docs/README.md")
        # nested
        assert re.search(regex, "docs/api/reference/guide.md")

    def test_double_star_prefix_matches_anywhere(self) -> None:
        """**/*.py matches a .py file at any depth."""
        pattern = "**/*.py"
        regex = glob_to_regex(pattern)
        assert re.search(regex, "src/wrknv/main.py")
        assert re.search(regex, "tests/unit/test_foo.py")
        assert re.search(regex, "setup.py")

    def test_exact_filename_matches_itself(self) -> None:
        """An exact filename pattern matches the file and has a $ anchor."""
        pattern = "config.json"
        regex = glob_to_regex(pattern)
        assert re.search(regex, "config.json")
        # The regex ends with $, so it doesn't match strings with extra chars after
        assert not re.search(regex, "config.json.bak")

    def test_dot_is_escaped(self) -> None:
        """A literal . in the pattern is treated as a literal dot, not any char."""
        pattern = "file.txt"
        regex = glob_to_regex(pattern)
        # literal dot should match
        assert re.search(regex, "file.txt")
        # character class wildcard (.) should NOT match when dot is escaped
        assert not re.search(regex, "fileXtxt")

    def test_empty_pattern(self) -> None:
        """An empty pattern produces a valid regex that matches an empty string."""
        regex = glob_to_regex("")
        assert isinstance(regex, str)
        assert re.search(regex, "")

    def test_result_ends_with_dollar(self) -> None:
        """The returned pattern is anchored at the end with $."""
        regex = glob_to_regex("foo/bar")
        assert regex.endswith("$")

    def test_question_mark_matches_single_char(self) -> None:
        """? matches exactly one character (but not /)."""
        pattern = "file?.txt"
        regex = glob_to_regex(pattern)
        assert re.search(regex, "fileA.txt")
        assert re.search(regex, "file1.txt")
        assert not re.search(regex, "file.txt")  # no char to match
        assert not re.search(regex, "fileAB.txt")  # two chars, not one


# ---------------------------------------------------------------------------
# TestSecurityAllowlistManagerValidate
# ---------------------------------------------------------------------------


class TestSecurityAllowlistManagerValidate(FoundationTestCase):
    """Tests for SecurityAllowlistManager.validate()."""

    def test_no_config_returns_false_with_message(self) -> None:
        """When no config is set, validate returns (False, ['No security configuration set'])."""
        manager = SecurityAllowlistManager()
        valid, errors = manager.validate()
        assert valid is False
        assert "No security configuration set" in errors

    def test_empty_allowed_paths_returns_false(self) -> None:
        """Config with empty allowed_paths list returns (False, error)."""
        config = SecurityConfig(description="Test", allowed_paths=[])
        manager = SecurityAllowlistManager(config=config)
        valid, errors = manager.validate()
        assert valid is False
        assert any("allowed_paths" in e for e in errors)

    def test_valid_config_returns_true(self) -> None:
        """Config with valid paths returns (True, [])."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        valid, errors = manager.validate()
        assert valid is True
        assert errors == []

    def test_empty_string_path_returns_false(self) -> None:
        """Config with an empty string in allowed_paths returns (False, error)."""
        config = SecurityConfig(description="Test", allowed_paths=["valid/path/*.key", ""])
        manager = SecurityAllowlistManager(config=config)
        valid, errors = manager.validate()
        assert valid is False
        assert any("Empty path" in e for e in errors)

    def test_path_with_newline_returns_false(self) -> None:
        """Config with a path containing a newline character returns (False, error)."""
        config = SecurityConfig(description="Test", allowed_paths=["path/with\nnewline"])
        manager = SecurityAllowlistManager(config=config)
        valid, errors = manager.validate()
        assert valid is False
        assert any("Invalid characters" in e for e in errors)

    def test_path_with_carriage_return_returns_false(self) -> None:
        """Config with a path containing \\r returns (False, error)."""
        config = SecurityConfig(description="Test", allowed_paths=["path/with\rbad"])
        manager = SecurityAllowlistManager(config=config)
        valid, errors = manager.validate()
        assert valid is False
        assert any("Invalid characters" in e for e in errors)


# ---------------------------------------------------------------------------
# TestSecurityAllowlistManagerGenerate
# ---------------------------------------------------------------------------


class TestSecurityAllowlistManagerGenerate(FoundationTestCase):
    """Tests for generate_trufflehog(), generate_gitleaks(), generate_gitguardian()."""

    # --- TruffleHog ---

    def test_generate_trufflehog_includes_description(self) -> None:
        """generate_trufflehog() output includes the config description."""
        config = make_config(description="My project secrets")
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_trufflehog()
        assert "My project secrets" in result

    def test_generate_trufflehog_includes_paths_as_regex(self) -> None:
        """generate_trufflehog() contains a regex line for each allowed path."""
        config = make_config(allowed_paths=["tests/certs/*.key"])
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_trufflehog()
        expected_regex = glob_to_regex("tests/certs/*.key")
        assert expected_regex in result

    def test_generate_trufflehog_without_config_raises(self) -> None:
        """generate_trufflehog() raises ValueError when no config is set."""
        manager = SecurityAllowlistManager()
        with pytest.raises(ValueError):
            manager.generate_trufflehog()

    def test_generate_trufflehog_ends_with_newline(self) -> None:
        """generate_trufflehog() output ends with a newline."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_trufflehog()
        assert result.endswith("\n")

    # --- Gitleaks ---

    def test_generate_gitleaks_includes_use_default(self) -> None:
        """generate_gitleaks() output includes 'useDefault = true'."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitleaks()
        assert "useDefault = true" in result

    def test_generate_gitleaks_includes_description(self) -> None:
        """generate_gitleaks() output includes the config description."""
        config = make_config(description="Gitleaks test config")
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitleaks()
        assert "Gitleaks test config" in result

    def test_generate_gitleaks_includes_paths(self) -> None:
        """generate_gitleaks() output contains each allowed path as a regex."""
        config = make_config(allowed_paths=["docs/**/*.md"])
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitleaks()
        expected_regex = glob_to_regex("docs/**/*.md")
        assert expected_regex in result

    def test_generate_gitleaks_without_config_raises(self) -> None:
        """generate_gitleaks() raises ValueError when no config is set."""
        manager = SecurityAllowlistManager()
        with pytest.raises(ValueError):
            manager.generate_gitleaks()

    def test_generate_gitleaks_ends_with_newline(self) -> None:
        """generate_gitleaks() output ends with a newline."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitleaks()
        assert result.endswith("\n")

    # --- GitGuardian ---

    def test_generate_gitguardian_includes_ignored_paths(self) -> None:
        """generate_gitguardian() YAML content includes the ignored_paths key."""
        config = make_config(allowed_paths=["secrets/*.env"])
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitguardian()
        assert "ignored_paths" in result
        assert "secrets/*.env" in result

    def test_generate_gitguardian_includes_description_in_header(self) -> None:
        """generate_gitguardian() header contains the config description."""
        config = make_config(description="GitGuardian test")
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitguardian()
        assert "GitGuardian test" in result

    def test_generate_gitguardian_without_config_raises(self) -> None:
        """generate_gitguardian() raises ValueError when no config is set."""
        manager = SecurityAllowlistManager()
        with pytest.raises(ValueError):
            manager.generate_gitguardian()

    def test_generate_gitguardian_is_valid_yaml(self) -> None:
        """generate_gitguardian() produces valid YAML."""
        import yaml

        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.generate_gitguardian()
        # Strip the comment header lines before parsing
        yaml_lines = [line for line in result.splitlines() if not line.startswith("#")]
        parsed = yaml.safe_load("\n".join(yaml_lines))
        assert parsed is not None
        assert "secret" in parsed
        assert "ignored_paths" in parsed["secret"]


# ---------------------------------------------------------------------------
# TestSecurityAllowlistManagerWriteAll
# ---------------------------------------------------------------------------


class TestSecurityAllowlistManagerWriteAll(FoundationTestCase):
    """Tests for SecurityAllowlistManager.write_all()."""

    def test_dry_run_returns_all_true_no_files_written(self) -> None:
        """write_all(dry_run=True) returns {file: True} for all files without writing."""
        temp_dir = self.create_temp_dir()
        config = make_config()
        manager = SecurityAllowlistManager(project_dir=temp_dir, config=config)
        results = manager.write_all(dry_run=True)
        assert all(results.values())
        assert len(results) == 3
        # No files should be written
        assert not (temp_dir / ".trufflehog-exclude-paths.txt").exists()
        assert not (temp_dir / ".gitleaks.toml").exists()
        assert not (temp_dir / ".gitguardian.yaml").exists()

    def test_write_all_creates_files_in_project_dir(self) -> None:
        """write_all(dry_run=False) creates all three config files on disk."""
        temp_dir = self.create_temp_dir()
        config = make_config()
        manager = SecurityAllowlistManager(project_dir=temp_dir, config=config)
        results = manager.write_all(dry_run=False)
        assert all(results.values())
        assert (temp_dir / ".trufflehog-exclude-paths.txt").exists()
        assert (temp_dir / ".gitleaks.toml").exists()
        assert (temp_dir / ".gitguardian.yaml").exists()

    def test_write_all_without_config_raises(self) -> None:
        """write_all() raises ValueError when no config is set."""
        temp_dir = self.create_temp_dir()
        manager = SecurityAllowlistManager(project_dir=temp_dir)
        with pytest.raises(ValueError):
            manager.write_all()

    def test_write_all_oserror_returns_false_for_that_file(self) -> None:
        """When write_text raises OSError, the affected file maps to False in results."""
        temp_dir = self.create_temp_dir()
        config = make_config()
        manager = SecurityAllowlistManager(project_dir=temp_dir, config=config)

        original_write_text = Path.write_text
        call_count = 0

        def patched_write_text(self_path: Path, content: str, **kwargs: object) -> None:
            nonlocal call_count
            call_count += 1
            if self_path.name == ".gitleaks.toml":
                raise OSError("Disk full")
            original_write_text(self_path, content, **kwargs)

        with patch.object(Path, "write_text", patched_write_text):
            results = manager.write_all(dry_run=False)

        assert results[".trufflehog-exclude-paths.txt"] is True
        assert results[".gitleaks.toml"] is False
        assert results[".gitguardian.yaml"] is True

    def test_write_all_file_contents_are_not_empty(self) -> None:
        """Files written by write_all() are non-empty."""
        temp_dir = self.create_temp_dir()
        config = make_config()
        manager = SecurityAllowlistManager(project_dir=temp_dir, config=config)
        manager.write_all(dry_run=False)
        assert (temp_dir / ".trufflehog-exclude-paths.txt").stat().st_size > 0
        assert (temp_dir / ".gitleaks.toml").stat().st_size > 0
        assert (temp_dir / ".gitguardian.yaml").stat().st_size > 0


# ---------------------------------------------------------------------------
# TestSecurityAllowlistManagerPreview
# ---------------------------------------------------------------------------


class TestSecurityAllowlistManagerPreview(FoundationTestCase):
    """Tests for SecurityAllowlistManager.preview()."""

    def test_preview_without_config_returns_message(self) -> None:
        """preview() without config returns 'No security configuration set'."""
        manager = SecurityAllowlistManager()
        result = manager.preview()
        assert result == "No security configuration set"

    def test_preview_all_tools_returns_all_sections(self) -> None:
        """preview() with no tool argument returns content for all three tools."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.preview()
        assert ".trufflehog-exclude-paths.txt" in result
        assert ".gitleaks.toml" in result
        assert ".gitguardian.yaml" in result

    def test_preview_trufflehog_returns_trufflehog_content(self) -> None:
        """preview('trufflehog') returns trufflehog config content."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.preview("trufflehog")
        assert "TruffleHog" in result

    def test_preview_gitleaks_returns_gitleaks_content(self) -> None:
        """preview('gitleaks') returns gitleaks config content."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.preview("gitleaks")
        assert "useDefault = true" in result

    def test_preview_gitguardian_returns_gitguardian_content(self) -> None:
        """preview('gitguardian') returns gitguardian config content."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.preview("gitguardian")
        assert "ignored_paths" in result

    def test_preview_unknown_tool_returns_unknown_message(self) -> None:
        """preview('unknown') returns an 'Unknown tool:' message."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result = manager.preview("unknown")
        assert "Unknown tool:" in result
        assert "unknown" in result

    def test_preview_tool_name_is_case_insensitive(self) -> None:
        """preview() tool argument is matched case-insensitively."""
        config = make_config()
        manager = SecurityAllowlistManager(config=config)
        result_lower = manager.preview("trufflehog")
        result_upper = manager.preview("TruffleHog")
        assert result_lower == result_upper


# ---------------------------------------------------------------------------
# TestSecurityAllowlistManagerSetConfig
# ---------------------------------------------------------------------------


class TestSecurityAllowlistManagerSetConfig(FoundationTestCase):
    """Tests for SecurityAllowlistManager.set_config()."""

    def test_set_config_updates_config_attribute(self) -> None:
        """set_config() replaces the manager's config with the new one."""
        manager = SecurityAllowlistManager()
        assert manager.config is None

        config = make_config()
        manager.set_config(config)
        assert manager.config is config

    def test_set_config_enables_generate(self) -> None:
        """After set_config(), generate methods succeed without raising."""
        manager = SecurityAllowlistManager()
        config = make_config()
        manager.set_config(config)
        # Should not raise
        result = manager.generate_trufflehog()
        assert result

    def test_set_config_replaces_existing_config(self) -> None:
        """set_config() replaces a previously set config."""
        old_config = make_config(description="Old config")
        manager = SecurityAllowlistManager(config=old_config)

        new_config = make_config(description="New config")
        manager.set_config(new_config)

        assert manager.config is new_config
        assert manager.config.description == "New config"

    def test_init_with_no_args_uses_cwd(self) -> None:
        """SecurityAllowlistManager() with no args defaults project_dir to cwd."""
        manager = SecurityAllowlistManager()
        assert manager.project_dir == Path.cwd()

    def test_init_with_project_dir_sets_path(self) -> None:
        """SecurityAllowlistManager(project_dir=...) sets project_dir correctly."""
        temp_dir = self.create_temp_dir()
        manager = SecurityAllowlistManager(project_dir=temp_dir)
        assert manager.project_dir == Path(temp_dir)

    def test_init_with_string_project_dir_converts_to_path(self) -> None:
        """SecurityAllowlistManager accepts a string project_dir and converts to Path."""
        temp_dir = self.create_temp_dir()
        manager = SecurityAllowlistManager(project_dir=str(temp_dir))
        assert isinstance(manager.project_dir, Path)
        assert manager.project_dir == Path(str(temp_dir))


# 🧰🌍🔚
