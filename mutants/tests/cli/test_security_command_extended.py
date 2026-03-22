#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test suite for CLI security command (extended)."""

from __future__ import annotations

import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

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
# CLI tests: security preview
# ---------------------------------------------------------------------------


class TestSecurityPreview(FoundationTestCase):
    """Tests for the `security preview` CLI command."""

    def test_no_config_exits_1(self) -> None:
        """When no config is found, exits with code 1."""
        cli = get_test_cli()
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = None
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "preview"])
        assert result.exit_code == 1
        assert "No security configuration found" in result.output

    def test_with_config_shows_preview(self) -> None:
        """When config exists, shows the preview output."""
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
            result = runner.invoke(cli, ["security", "preview"])
        assert result.exit_code == 0
        assert "Preview content" in result.output
        mock_manager.preview.assert_called_once_with(tool=None)

    def test_with_config_and_tool_shows_tool_preview(self) -> None:
        """When config and tool are provided, passes tool to preview."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        mock_manager.preview.return_value = "# trufflehog config"
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "preview", "trufflehog"])
        assert result.exit_code == 0
        assert "trufflehog config" in result.output
        mock_manager.preview.assert_called_once_with(tool="trufflehog")


# ---------------------------------------------------------------------------
# CLI tests: security scan
# ---------------------------------------------------------------------------


class TestSecurityScan(FoundationTestCase):
    """Tests for the `security scan` CLI command."""

    def test_specific_tool_trufflehog_calls_runner(self) -> None:
        """Specifying tool=trufflehog calls _run_trufflehog (no config → warning, then scan)."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security._run_trufflehog") as mock_trufflehog,
            patch("wrknv.cli.commands.security._run_gitleaks") as mock_gitleaks,
        ):
            # No config → generate step warns and skips, then scan runs
            mock_load.return_value = None
            mock_trufflehog.return_value = True
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan", "trufflehog"])
        assert result.exit_code == 0
        mock_trufflehog.assert_called_once()
        mock_gitleaks.assert_not_called()

    def test_specific_tool_gitleaks_calls_runner(self) -> None:
        """Specifying tool=gitleaks calls _run_gitleaks."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security._run_trufflehog") as mock_trufflehog,
            patch("wrknv.cli.commands.security._run_gitleaks") as mock_gitleaks,
        ):
            mock_load.return_value = None
            mock_gitleaks.return_value = True
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan", "gitleaks"])
        assert result.exit_code == 0
        mock_gitleaks.assert_called_once()
        mock_trufflehog.assert_not_called()

    def test_unknown_tool_exits_1(self) -> None:
        """Specifying an unknown scanner tool exits with code 1."""
        cli = get_test_cli()
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = None
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan", "snyk"])
        assert result.exit_code == 1
        assert "Unknown scanner" in result.output
        assert "snyk" in result.output

    def test_run_all_scanners_all_succeed_exits_0(self) -> None:
        """Running all scanners with all succeeding exits 0."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security._run_trufflehog") as mock_trufflehog,
            patch("wrknv.cli.commands.security._run_gitleaks") as mock_gitleaks,
        ):
            mock_load.return_value = None
            mock_trufflehog.return_value = True
            mock_gitleaks.return_value = True
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan"])
        assert result.exit_code == 0
        mock_trufflehog.assert_called_once()
        mock_gitleaks.assert_called_once()

    def test_run_all_scanners_some_fail_exits_1(self) -> None:
        """Running all scanners with some failing exits 1."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security._run_trufflehog") as mock_trufflehog,
            patch("wrknv.cli.commands.security._run_gitleaks") as mock_gitleaks,
        ):
            mock_load.return_value = None
            mock_trufflehog.return_value = False
            mock_gitleaks.return_value = True
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan"])
        assert result.exit_code == 1

    def test_generate_true_with_config_updates_configs(self) -> None:
        """When generate=True (default) and config exists, calls write_all before scanning."""
        cli = get_test_cli()
        config = make_config()
        mock_manager = make_mock_manager()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security.SecurityAllowlistManager") as mock_cls,
            patch("wrknv.cli.commands.security._run_trufflehog") as mock_trufflehog,
            patch("wrknv.cli.commands.security._run_gitleaks") as mock_gitleaks,
        ):
            mock_load.return_value = config
            mock_cls.return_value = mock_manager
            mock_trufflehog.return_value = True
            mock_gitleaks.return_value = True
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan"])
        assert result.exit_code == 0
        mock_manager.write_all.assert_called_once()
        assert "Updated security scanner configurations" in result.output

    def test_generate_default_without_config_shows_warning(self) -> None:
        """When generate=True (default) but no config found, shows warning and continues."""
        cli = get_test_cli()
        with (
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
            patch("wrknv.cli.commands.security._run_trufflehog") as mock_trufflehog,
            patch("wrknv.cli.commands.security._run_gitleaks") as mock_gitleaks,
        ):
            mock_load.return_value = None
            mock_trufflehog.return_value = True
            mock_gitleaks.return_value = True
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "scan"])
        assert result.exit_code == 0
        assert "No security configuration found" in result.output


# ---------------------------------------------------------------------------
# CLI tests: security show
# ---------------------------------------------------------------------------


class TestSecurityShow(FoundationTestCase):
    """Tests for the `security show` CLI command."""

    def test_no_config_shows_instructions(self) -> None:
        """When no config is found, shows setup instructions and exits 0."""
        cli = get_test_cli()
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = None
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "show"])
        assert result.exit_code == 0
        assert "No security configuration found" in result.output
        assert "pyproject.toml" in result.output

    def test_with_config_few_paths_shows_all(self) -> None:
        """When config has few paths (<=10), shows all paths."""
        cli = get_test_cli()
        config = make_config(
            description="My project secrets",
            allowed_paths=["tests/certs/*.key", "docs/*.md", "fixtures/**"],
        )
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = config
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "show"])
        assert result.exit_code == 0
        assert "Security Configuration" in result.output
        assert "My project secrets" in result.output
        assert "tests/certs/*.key" in result.output
        assert "docs/*.md" in result.output
        assert "fixtures/**" in result.output

    def test_with_config_many_paths_shows_count(self) -> None:
        """When config has more than 10 paths, all are shown (show command shows all)."""
        cli = get_test_cli()
        many_paths = [f"path/to/file_{i}.key" for i in range(15)]
        config = make_config(description="Many paths", allowed_paths=many_paths)
        with patch("wrknv.cli.commands.security.load_security_config") as mock_load:
            mock_load.return_value = config
            runner = click.testing.CliRunner()
            result = runner.invoke(cli, ["security", "show"])
        assert result.exit_code == 0
        assert "Security Configuration" in result.output
        # security show iterates all paths (no truncation in show)
        assert "path/to/file_0.key" in result.output
        assert "path/to/file_14.key" in result.output


# ---------------------------------------------------------------------------
# CLI tests: security validate — paths truncation branch
# ---------------------------------------------------------------------------


class TestSecurityValidatePaths(FoundationTestCase):
    """Additional coverage for the validate command path display branches."""

    def test_valid_config_shows_description_and_paths(self) -> None:
        """Valid config output includes description and first 10 paths."""
        cli = get_test_cli()
        paths = [f"tests/file_{i}.key" for i in range(5)]
        config = make_config(description="Validate description", allowed_paths=paths)
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
        assert "Validate description" in result.output
        assert "5" in result.output

    def test_valid_config_more_than_10_paths_shows_more(self) -> None:
        """When allowed_paths > 10, validate shows '... and N more'."""
        cli = get_test_cli()
        paths = [f"tests/file_{i}.key" for i in range(12)]
        config = make_config(description="Many paths config", allowed_paths=paths)
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
        assert "and 2 more" in result.output


# 🧰🌍🔚
