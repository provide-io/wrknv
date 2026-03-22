#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""Test suite for CLI security command."""

from __future__ import annotations

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.commands.security import _run_gitleaks, _run_trufflehog
from wrknv.cli.hub_cli import create_cli
from wrknv.security.config import SecurityConfig


def get_test_cli():
    """Get or create the test CLI instance."""
    return create_cli()


def make_config(
    description: str = "Test config",
    allowed_paths: list[str] | None = None,
) -> SecurityConfig:
    """Create a SecurityConfig for tests."""
    if allowed_paths is None:
        allowed_paths = ["tests/*.key", "docs/*.md"]
    return SecurityConfig(description=description, allowed_paths=allowed_paths)


def make_mock_manager(
    is_valid: bool = True,
    errors: list[str] | None = None,
    write_all_results: dict[str, bool] | None = None,
) -> Mock:
    """Create a standard SecurityAllowlistManager mock."""
    mock_manager = Mock()
    mock_manager.validate.return_value = (is_valid, errors or [])
    mock_manager.generate_trufflehog.return_value = "# trufflehog config"
    mock_manager.generate_gitleaks.return_value = "# gitleaks config"
    mock_manager.generate_gitguardian.return_value = "gitguardian: config"
    if write_all_results is None:
        write_all_results = {
            ".trufflehog-exclude-paths.txt": True,
            ".gitleaks.toml": True,
            ".gitguardian.yaml": True,
        }
    mock_manager.write_all.return_value = write_all_results
    mock_manager.preview.return_value = "Preview content"
    return mock_manager


# ---------------------------------------------------------------------------
# Unit tests: _run_trufflehog
# ---------------------------------------------------------------------------


class TestRunTrufflehog(FoundationTestCase):
    """Unit tests for the _run_trufflehog helper function."""

    def test_not_installed_returns_true(self) -> None:
        """When trufflehog is not installed, returns True (non-blocking)."""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
        ):
            mock_which.return_value = None
            result = _run_trufflehog()
        assert result is True

    def test_installed_success_returns_true(self) -> None:
        """When trufflehog runs successfully (returncode 0), returns True."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        mock_result.stderr = ""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/trufflehog"
            mock_run.return_value = mock_result
            result = _run_trufflehog()
        assert result is True

    def test_installed_failure_returns_false(self) -> None:
        """When trufflehog exits with non-zero code, returns False."""
        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stdout = "found secret"
        mock_result.stderr = ""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/trufflehog"
            mock_run.return_value = mock_result
            result = _run_trufflehog()
        assert result is False

    def test_failure_with_stdout_and_stderr(self) -> None:
        """When trufflehog fails with both stdout and stderr, returns False."""
        mock_result = Mock()
        mock_result.returncode = 2
        mock_result.stdout = "stdout: found secrets"
        mock_result.stderr = "stderr: error details"
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/trufflehog"
            mock_run.return_value = mock_result
            result = _run_trufflehog()
        assert result is False

    def test_file_not_found_returns_true(self) -> None:
        """When subprocess raises FileNotFoundError, returns True (non-blocking)."""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/trufflehog"
            mock_run.side_effect = FileNotFoundError("trufflehog not found")
            result = _run_trufflehog()
        assert result is True


# ---------------------------------------------------------------------------
# Unit tests: _run_gitleaks
# ---------------------------------------------------------------------------


class TestRunGitleaks(FoundationTestCase):
    """Unit tests for the _run_gitleaks helper function."""

    def test_not_installed_returns_true(self) -> None:
        """When gitleaks is not installed, returns True (non-blocking)."""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
        ):
            mock_which.return_value = None
            result = _run_gitleaks()
        assert result is True

    def test_installed_success_returns_true(self) -> None:
        """When gitleaks runs successfully (returncode 0), returns True."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        mock_result.stderr = ""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/gitleaks"
            mock_run.return_value = mock_result
            result = _run_gitleaks()
        assert result is True

    def test_installed_failure_returns_false(self) -> None:
        """When gitleaks exits with non-zero code, returns False."""
        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stdout = "found secret"
        mock_result.stderr = ""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/gitleaks"
            mock_run.return_value = mock_result
            result = _run_gitleaks()
        assert result is False

    def test_file_not_found_returns_true(self) -> None:
        """When subprocess raises FileNotFoundError, returns True (non-blocking)."""
        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
        ):
            mock_which.return_value = "/usr/local/bin/gitleaks"
            mock_run.side_effect = FileNotFoundError("gitleaks not found")
            result = _run_gitleaks()
        assert result is True

    def test_with_config_file_existing(self) -> None:
        """When .gitleaks.toml exists, the --config flag is added to cmd."""
        temp_dir = self.create_temp_dir()
        config_file = temp_dir / ".gitleaks.toml"
        config_file.write_text("[extend]\nuseDefault = true\n")

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        mock_result.stderr = ""

        captured_cmd: list[list[str]] = []

        def fake_run(cmd: list[str], **kwargs: object) -> Mock:
            captured_cmd.append(list(cmd))
            return mock_result

        with (
            patch("wrknv.cli.commands.security.shutil.which") as mock_which,
            patch("wrknv.cli.commands.security.subprocess.run") as mock_run,
            patch("wrknv.cli.commands.security.Path.cwd") as mock_cwd,
        ):
            mock_which.return_value = "/usr/local/bin/gitleaks"
            mock_cwd.return_value = temp_dir
            mock_run.side_effect = fake_run
            result = _run_gitleaks()

        assert result is True
        assert len(captured_cmd) == 1
        assert "--config" in captured_cmd[0]


# ---------------------------------------------------------------------------
# CLI tests: security generate
# ---------------------------------------------------------------------------


class TestSecurityGenerate(FoundationTestCase):
    """Tests for the `security generate` CLI command."""

    def test_no_config_found_exits_1(self) -> None:
        """When no config is found, exits with code 1."""
        cli = get_test_cli()
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = None
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate"])
        assert result.exit_code == 1
        assert "No security configuration found" in result.output

    def test_invalid_config_exits_1(self) -> None:
        """When config is invalid, exits with code 1 showing errors."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager(is_valid=False, errors=["Empty path in allowed_paths"])
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate"])
        assert result.exit_code == 1
        assert "Invalid security configuration" in result.output
        assert "Empty path in allowed_paths" in result.output

    def test_dry_run_no_tool_shows_info(self) -> None:
        """dry_run=True, no tool: shows dry-run info without writing files."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate", "--dry-run"])
        assert result.exit_code == 0
        assert "DRY-RUN" in result.output
        mock_manager.write_all.assert_called_once_with(dry_run=True)

    def test_no_dry_run_no_tool_calls_write_all(self) -> None:
        """dry_run=False, no tool: calls write_all and shows success."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate"])
        assert result.exit_code == 0
        mock_manager.write_all.assert_called_once_with(dry_run=False)
        assert "Generated 3 configuration files" in result.output

    def test_specific_tool_trufflehog_calls_generate(self) -> None:
        """Specifying tool=trufflehog calls generate_trufflehog and writes file."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        temp_dir = self.create_temp_dir()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
            patch("wrknv.cli.commands.security.Path.cwd") as mock_cwd,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            mock_cwd.return_value = temp_dir
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate", "--tool", "trufflehog"])
        assert result.exit_code == 0
        mock_manager.generate_trufflehog.assert_called_once()
        assert "Generated" in result.output

    def test_specific_tool_with_dry_run_shows_content(self) -> None:
        """Specifying tool + dry_run: shows the generated content without writing."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate", "--tool", "gitleaks", "--dry-run"])
        assert result.exit_code == 0
        assert "gitleaks config" in result.output
        mock_manager.generate_gitleaks.assert_called_once()

    def test_unknown_tool_exits_1(self) -> None:
        """Specifying an unknown tool exits with code 1."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate", "--tool", "unknowntool"])
        assert result.exit_code == 1
        assert "Unknown tool" in result.output
        assert "unknowntool" in result.output

    def test_partial_success_shows_warning(self) -> None:
        """When some files fail to generate, shows a warning."""
        cli = get_test_cli()
        config = make_config()
        partial_results = {
            ".trufflehog-exclude-paths.txt": True,
            ".gitleaks.toml": False,
            ".gitguardian.yaml": True,
        }
        mock_manager = make_mock_manager(write_all_results=partial_results)
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "generate"])
        assert result.exit_code == 0
        assert "2/3" in result.output
        assert ".gitleaks.toml" in result.output


# ---------------------------------------------------------------------------
# CLI tests: security validate
# ---------------------------------------------------------------------------


class TestSecurityValidate(FoundationTestCase):
    """Tests for the `security validate` CLI command."""

    def test_no_config_exits_1(self) -> None:
        """When no config is found, exits with code 1."""
        cli = get_test_cli()
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = None
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "validate"])
        assert result.exit_code == 1
        assert "No security configuration found" in result.output

    def test_valid_config_exits_0(self) -> None:
        """When config is valid, exits with code 0 and shows success."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "validate"])
        assert result.exit_code == 0
        assert "valid" in result.output.lower()

    def test_invalid_config_exits_1(self) -> None:
        """When config has validation errors, exits with code 1."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager(
            is_valid=False, errors=["No allowed_paths defined in security configuration"]
        )
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "validate"])
        assert result.exit_code == 1
        assert "No allowed_paths defined" in result.output


# 🧰🌍🔚
