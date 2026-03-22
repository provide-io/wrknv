#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for gitignore CLI commands (list, search, detect, show, update, build branches)."""

from __future__ import annotations

from click.testing import CliRunner
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock, patch

from wrknv.cli.hub_cli import create_cli


def get_test_cli() -> object:
    """Create a fresh CLI for each test."""
    return create_cli()


def _make_mock_config(templates: list[str] | None = None) -> Mock:
    """Create a mock WorkenvConfig with optional gitignore templates."""
    mock_config = Mock()
    gitignore_cfg: dict[str, object] = {}
    if templates is not None:
        gitignore_cfg["templates"] = templates
    mock_config.get_setting.side_effect = lambda key, default=None: (
        gitignore_cfg if key == "gitignore" else default
    )
    return mock_config


class TestGitignoreList(FoundationTestCase):
    """Tests for gitignore list command."""

    def test_list_returns_templates(self) -> None:
        """Test listing available templates."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.list_available_templates.return_value = ["Python", "Node", "Go"]

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "list"])

        assert result.exit_code == 0
        assert "Python" in result.output
        assert "Node" in result.output
        assert "Go" in result.output
        assert "3 templates" in result.output

    def test_list_with_category(self) -> None:
        """Test listing templates filtered by category."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.list_available_templates.return_value = ["Python", "Ruby"]

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "list", "languages"])

        assert result.exit_code == 0
        assert "languages" in result.output
        mock_manager.list_available_templates.assert_called_once_with(category="languages")

    def test_list_no_templates_no_category(self) -> None:
        """Test listing when no templates are available."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.list_available_templates.return_value = []

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "list"])

        assert result.exit_code == 0
        assert "No templates found" in result.output

    def test_list_no_templates_with_category(self) -> None:
        """Test listing when no templates match a category."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.list_available_templates.return_value = []

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "list", "missing"])

        assert result.exit_code == 0
        assert "missing" in result.output

    def test_list_exception_exits_1(self) -> None:
        """Test that exceptions result in exit code 1."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", side_effect=RuntimeError("config error")),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "list"])

        assert result.exit_code == 1


class TestGitignoreSearch(FoundationTestCase):
    """Tests for gitignore search command."""

    def test_search_returns_results(self) -> None:
        """Test searching with matching results."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.search_templates.return_value = ["Python", "Python3"]

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "search", "pyth"])

        assert result.exit_code == 0
        assert "Python" in result.output
        assert "2 templates" in result.output

    def test_search_no_results(self) -> None:
        """Test searching with no matching results."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.search_templates.return_value = []

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "search", "xyz"])

        assert result.exit_code == 0
        assert "No templates found matching" in result.output

    def test_search_exception_exits_1(self) -> None:
        """Test that exceptions result in exit code 1."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.search_templates.side_effect = RuntimeError("network error")

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "search", "python"])

        assert result.exit_code == 1


class TestGitignoreDetect(FoundationTestCase):
    """Tests for gitignore detect command."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.temp_dir = self.create_temp_dir()

    def test_detect_with_project_types(self) -> None:
        """Test detecting project types that have matching templates."""
        cli = get_test_cli()
        mock_detector = Mock()
        mock_detector.detect_project_types.return_value = ["Python", "Node"]
        mock_manager = Mock()
        mock_manager.search_templates.return_value = ["Python"]

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.ProjectDetector", return_value=mock_detector),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "detect", str(self.temp_dir)])

        assert result.exit_code == 0
        assert "Python" in result.output

    def test_detect_no_project_types(self) -> None:
        """Test detecting when no project types are found."""
        cli = get_test_cli()
        mock_detector = Mock()
        mock_detector.detect_project_types.return_value = []

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.ProjectDetector", return_value=mock_detector),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "detect", str(self.temp_dir)])

        assert result.exit_code == 0
        assert "No specific project types detected" in result.output

    def test_detect_path_not_exists(self) -> None:
        """Test detect with non-existent path."""
        cli = get_test_cli()

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "detect", "/nonexistent/path/xyz"])

        assert result.exit_code == 1
        assert "does not exist" in result.output

    def test_detect_type_with_no_template(self) -> None:
        """Test detecting project type that has no template."""
        cli = get_test_cli()
        mock_detector = Mock()
        mock_detector.detect_project_types.return_value = ["ObscureFramework"]
        mock_manager = Mock()
        mock_manager.search_templates.return_value = []

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.ProjectDetector", return_value=mock_detector),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "detect", str(self.temp_dir)])

        assert result.exit_code == 0
        assert "ObscureFramework" in result.output

    def test_detect_exception_exits_1(self) -> None:
        """Test that exceptions result in exit code 1."""
        cli = get_test_cli()
        mock_detector = Mock()
        mock_detector.detect_project_types.side_effect = RuntimeError("detection error")

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.ProjectDetector", return_value=mock_detector),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "detect", str(self.temp_dir)])

        assert result.exit_code == 1


class TestGitignoreShow(FoundationTestCase):
    """Tests for gitignore show command."""

    def test_show_existing_template(self) -> None:
        """Test showing an existing template."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.template_handler.get_template.return_value = "*.pyc\n__pycache__/"

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "show", "Python"])

        assert result.exit_code == 0
        assert "Python" in result.output
        assert "*.pyc" in result.output

    def test_show_missing_template_without_suggestions(self) -> None:
        """Test showing a non-existent template with no suggestions."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.template_handler.get_template.return_value = None
        mock_manager.search_templates.return_value = []

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "show", "NonExistent"])

        assert result.exit_code == 1
        assert "Template not found" in result.output

    def test_show_missing_template_with_suggestions(self) -> None:
        """Test showing a non-existent template with similar suggestions."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.template_handler.get_template.return_value = None
        mock_manager.search_templates.return_value = ["Python", "Python3"]

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "show", "Pythn"])

        assert result.exit_code == 1
        assert "Did you mean" in result.output

    def test_show_exception_exits_1(self) -> None:
        """Test that exceptions result in exit code 1."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.template_handler.get_template.side_effect = RuntimeError("error")

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "show", "Python"])

        assert result.exit_code == 1


class TestGitignoreUpdate(FoundationTestCase):
    """Tests for gitignore update command."""

    def test_update_success(self) -> None:
        """Test successful template cache update."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.update_templates.return_value = True

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "update"])

        assert result.exit_code == 0
        assert "updated successfully" in result.output

    def test_update_already_current(self) -> None:
        """Test update when templates are already up to date."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.update_templates.return_value = False

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "update"])

        assert result.exit_code == 0
        assert "up to date" in result.output

    def test_update_exception_exits_1(self) -> None:
        """Test that exceptions result in exit code 1."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.update_templates.side_effect = RuntimeError("network error")

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "update"])

        assert result.exit_code == 1


class TestGitignoreBuildExtraBranches(FoundationTestCase):
    """Tests for uncovered branches in gitignore_build command."""

    def test_build_with_comma_separated_templates(self) -> None:
        """Test building with comma-separated template names."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.build_from_templates.return_value = True

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "build", "Python,Node,Go"])

        assert result.exit_code == 0
        mock_manager.build_from_templates.assert_called_once()
        call_args = mock_manager.build_from_templates.call_args
        templates = call_args[1]["templates"] if call_args[1] else call_args[0][0]
        assert "Python" in templates
        assert "Node" in templates
        assert "Go" in templates

    def test_build_failure_exits_1(self) -> None:
        """Test that build failure results in exit code 1."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.build_from_templates.return_value = False

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "build", "Python"])

        assert result.exit_code == 1
        assert "Failed to build" in result.output

    def test_build_with_auto_detect(self) -> None:
        """Test building with auto-detect option."""
        cli = get_test_cli()
        mock_detector = Mock()
        mock_detector.detect_project_types.return_value = ["Python"]
        mock_manager = Mock()
        mock_manager.build_from_templates.return_value = True

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.ProjectDetector", return_value=mock_detector),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "build", "--auto-detect"])

        assert result.exit_code == 0
        assert "Auto-detected" in result.output

    def test_build_exception_exits_1(self) -> None:
        """Test that build exceptions result in exit code 1."""
        cli = get_test_cli()
        mock_manager = Mock()
        mock_manager.build_from_templates.side_effect = RuntimeError("build error")

        with (
            patch("wrknv.cli.hub_cli.WrknvContext.get_config", return_value=_make_mock_config()),
            patch("wrknv.cli.commands.gitignore.GitignoreManager", return_value=mock_manager),
        ):
            runner = CliRunner()
            result = runner.invoke(cli, ["gitignore", "build", "Python"])

        assert result.exit_code == 1


# 🧰🌍🔚
