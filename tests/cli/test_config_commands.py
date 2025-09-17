#!/usr/bin/env python3

"""
Test suite for CLI config commands.
"""

import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import click.testing
import pytest

from wrknv.cli.hub_cli import create_cli


@pytest.mark.cli
@pytest.mark.config
class TestConfigCommands(unittest.TestCase):
    """Test config show and edit CLI commands."""

    def setUp(self):
        """Set up test fixtures."""
        self.runner = click.testing.CliRunner()
        self.cli = create_cli()
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
        self.config_file = self.temp_path / "wrknv.toml"

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_config_show_no_config(self):
        """Test showing config when no config file exists."""
        with patch("wrknv.cli.commands.config.WorkenvConfig.load") as mock_load:
            mock_config = Mock()
            mock_config.show_config.return_value = None
            mock_load.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "show"])

            self.assertEqual(result.exit_code, 0)
            mock_config.show_config.assert_called_once()

    def test_config_show_with_config(self):
        """Test showing existing configuration."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.show_config.return_value = None
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "show"])

            self.assertEqual(result.exit_code, 0)
            mock_config.show_config.assert_called_once()

    def test_config_show_json_format(self):
        """Test showing config in JSON format."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.to_dict.return_value = {
                "project_name": "test-project",
                "tools": {"terraform": {"version": "1.5.0", "enabled": True}},
            }
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "show", "--json"])

            self.assertEqual(result.exit_code, 0)
            # Output should be valid JSON
            import json

            output_data = json.loads(result.output)
            self.assertEqual(output_data["project_name"], "test-project")

    def test_config_show_with_profile_filter(self):
        """Test showing only specific profile configuration."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_profile.return_value = {"terraform": "1.5.0", "go": "1.21.0"}
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "show", "--profile", "dev"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Profile: dev", result.output)
            self.assertIn("terraform: 1.5.0", result.output)

    def test_config_edit_with_editor(self):
        """Test editing config file with default editor."""
        self.config_file.write_text('project_name = "test-project"')

        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_config_path.return_value = self.config_file
            mock_config.edit_config.return_value = None
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "edit"])

            self.assertEqual(result.exit_code, 0)
            mock_config.edit_config.assert_called_once()

    def test_config_edit_no_editor_set(self):
        """Test editing config when no EDITOR is set."""
        self.config_file.write_text('project_name = "test-project"')

        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            with patch.dict(os.environ, {}, clear=True):
                # Remove EDITOR from environment
                if "EDITOR" in os.environ:
                    del os.environ["EDITOR"]

                mock_config = Mock()
                mock_config.get_config_path.return_value = self.config_file
                mock_config.edit_config.side_effect = RuntimeError(
                    "No editor configured. Set EDITOR or VISUAL environment variable."
                )
                mock_config_class.return_value = mock_config

                result = self.runner.invoke(self.cli, ["config", "edit"])

                # The command catches the exception and shows error message
                self.assertIn("No editor configured", result.output)

    def test_config_edit_creates_file_if_missing(self):
        """Test that edit creates a config file if it doesn't exist."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            with patch("provide.foundation.process.run_command") as mock_run:
                with patch.dict(os.environ, {"EDITOR": "nano"}):
                    mock_config = Mock()
                    mock_config.get_config_path.return_value = self.config_file
                    mock_config.config_exists.return_value = False
                    mock_config.edit_config.return_value = None
                    mock_config_class.return_value = mock_config
                    mock_run.return_value = Mock(returncode=0)

                    result = self.runner.invoke(self.cli, ["config", "edit"])

                    self.assertEqual(result.exit_code, 0)
                    mock_config.edit_config.assert_called_once()

    def test_config_validate(self):
        """Test validating configuration file."""
        self.config_file.write_text("""
project_name = "test-project"
version = "1.0.0"

[tools]
terraform = { version = "1.5.0" }
""")

        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_config_path.return_value = self.config_file
            mock_config.validate.return_value = (True, [])
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "validate"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Configuration is valid", result.output)

    def test_config_validate_with_errors(self):
        """Test validating invalid configuration."""
        self.config_file.write_text("""
# Missing project_name
version = "1.0.0"
""")

        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_config_path.return_value = self.config_file
            mock_config.validate.return_value = (
                False,
                ["Missing required field: project_name", "Invalid version format"],
            )
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "validate"])

            self.assertEqual(result.exit_code, 1)
            self.assertIn("Configuration validation failed", result.output)
            self.assertIn("Missing required field: project_name", result.output)

    def test_config_init(self):
        """Test initializing a new configuration file."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_config_path.return_value = self.config_file
            mock_config.config_exists.return_value = False
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(workenv_cli, ["config", "init"], input="my-project\n1.0.0\nINFO\n")

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Created configuration file", result.output)

    def test_config_init_already_exists(self):
        """Test initializing when config already exists."""
        self.config_file.write_text('project_name = "existing"')

        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_config_path.return_value = self.config_file
            mock_config.config_exists.return_value = True
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "init"])

            self.assertEqual(result.exit_code, 1)
            self.assertIn("Configuration file already exists", result.output)

    def test_config_get_setting(self):
        """Test getting a specific configuration setting."""
        with patch("wrknv.cli.commands.config.WorkenvConfig.load") as mock_load:
            mock_config = Mock()
            mock_config.get_setting.return_value = "INFO"
            mock_load.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "get", "log_level"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("log_level: INFO", result.output)

    def test_config_set_setting(self):
        """Test setting a configuration value."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.set_setting.return_value = True
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(workenv_cli, ["config", "set", "log_level", "DEBUG"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Set log_level to DEBUG", result.output)
            mock_config.set_setting.assert_called_once_with("log_level", "DEBUG")

    def test_config_path(self):
        """Test showing configuration file path."""
        with patch("wrknv.cli.commands.config.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_config_path.return_value = self.config_file
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["config", "path"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn(str(self.config_file), result.output)


class TestConfigCommandIntegration(unittest.TestCase):
    """Integration tests for config commands."""

    def setUp(self):
        """Set up test fixtures."""
        self.runner = click.testing.CliRunner()
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_config_init_and_validate_integration(self):
        """Test creating and validating a config file."""
        config_file = self.temp_path / "wrknv.toml"

        with patch("wrknv.wenv.config.Path.cwd") as mock_cwd:
            mock_cwd.return_value = self.temp_path

            # Initialize config
            result = self.runner.invoke(workenv_cli, ["config", "init"], input="test-project\n1.0.0\nINFO\n")
            self.assertEqual(result.exit_code, 0)

            # Verify file was created
            self.assertTrue(config_file.exists())

            # Validate the config
            result = self.runner.invoke(self.cli, ["config", "validate"])
            self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
