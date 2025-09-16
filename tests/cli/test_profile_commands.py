#!/usr/bin/env python3

"""
Test suite for CLI profile commands.
"""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import click.testing
import tomli_w

from wrknv.cli.hub_cli import create_cli


class TestProfileCommands(unittest.TestCase):
    """Test profile save and load CLI commands."""

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

    def test_profile_list_empty(self):
        """Test listing profiles when none exist."""
        # Create empty config file
        self.config_file.write_text("""
project_name = "test-project"
""")

        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.list_profiles.return_value = []
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["profile-list"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("No profiles found", result.output)

    def test_profile_list_with_profiles(self):
        """Test listing profiles when they exist."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.list_profiles.return_value = ["dev", "prod", "staging"]
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["profile-list"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("dev", result.output)
            self.assertIn("prod", result.output)
            self.assertIn("staging", result.output)

    def test_profile_save_current_tools(self):
        """Test saving current tool versions as a profile."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_all_tools.return_value = {"terraform": "1.5.0", "go": "1.21.0", "uv": "0.4.0"}
            mock_config.save_profile.return_value = None
            mock_config.profile_exists.return_value = False
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["profile-save", "dev"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Saved profile 'dev'", result.output)
            mock_config.save_profile.assert_called_once_with(
                "dev", {"terraform": "1.5.0", "go": "1.21.0", "uv": "0.4.0"}
            )

    def test_profile_save_overwrites_existing(self):
        """Test that saving a profile overwrites an existing one."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_all_tools.return_value = {"terraform": "1.6.0"}
            mock_config.profile_exists.return_value = True
            mock_config.save_profile.return_value = None
            mock_config_class.return_value = mock_config

            # Should prompt for confirmation
            result = self.runner.invoke(workenv_cli, ["profile-save", "dev", "--force"], input="y\n")

            self.assertEqual(result.exit_code, 0)
            mock_config.save_profile.assert_called_once()

    def test_profile_load_not_found(self):
        """Test loading a profile that doesn't exist."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_profile.return_value = None
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["profile-load", "nonexistent"])

            self.assertEqual(result.exit_code, 1)
            self.assertIn("Profile 'nonexistent' not found", result.output)

    def test_profile_load_success(self):
        """Test successfully loading a profile."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            with patch("wrknv.cli.commands.profile.get_tool_manager") as mock_get_manager:
                mock_config = Mock()
                mock_config.get_profile.return_value = {"terraform": "1.5.0", "go": "1.21.0"}
                mock_config_class.return_value = mock_config

                mock_manager = Mock()
                mock_manager.install_version.return_value = None
                mock_get_manager.return_value = mock_manager

                result = self.runner.invoke(self.cli, ["profile-load", "dev"])

                self.assertEqual(result.exit_code, 0)
                self.assertIn("Loading profile 'dev'", result.output)
                self.assertIn("Successfully installed terraform 1.5.0", result.output)
                self.assertIn("Successfully installed go 1.21.0", result.output)

                # Verify install was called for each tool
                self.assertEqual(mock_manager.install_version.call_count, 2)

    def test_profile_load_partial_failure(self):
        """Test loading a profile when some tools fail to install."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            with patch("wrknv.cli.commands.profile.get_tool_manager") as mock_get_manager:
                mock_config = Mock()
                mock_config.get_profile.return_value = {"terraform": "1.5.0", "go": "1.21.0"}
                mock_config_class.return_value = mock_config

                # First tool succeeds, second fails
                mock_manager = Mock()
                mock_manager.install_version.side_effect = [
                    None,  # terraform succeeds
                    Exception("Failed to download Go"),  # go fails
                ]
                mock_get_manager.return_value = mock_manager

                result = self.runner.invoke(self.cli, ["profile-load", "dev"])

                # Should not exit with error, but show error message
                self.assertEqual(result.exit_code, 0)
                self.assertIn("Successfully installed terraform 1.5.0", result.output)
                self.assertIn("Error installing go 1.21.0", result.output)

    def test_profile_delete(self):
        """Test deleting a profile."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.profile_exists.return_value = True
            mock_config.delete_profile.return_value = True
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(
                workenv_cli,
                ["profile-delete", "dev"],
                input="y\n",  # Confirm deletion
            )

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Profile 'dev' deleted", result.output)
            mock_config.delete_profile.assert_called_once_with("dev")

    def test_profile_show(self):
        """Test showing details of a profile."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_profile.return_value = {"terraform": "1.5.0", "go": "1.21.0", "uv": "0.4.0"}
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(self.cli, ["profile-show", "dev"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Profile: dev", result.output)
            self.assertIn("terraform: 1.5.0", result.output)
            self.assertIn("go: 1.21.0", result.output)
            self.assertIn("uv: 0.4.0", result.output)

    def test_profile_export(self):
        """Test exporting a profile to a file."""
        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.get_profile.return_value = {"terraform": "1.5.0", "go": "1.21.0"}
            mock_config_class.return_value = mock_config

            output_file = self.temp_path / "profile.toml"

            result = self.runner.invoke(
                workenv_cli, ["profile", "export", "dev", "--output", str(output_file)]
            )

            self.assertEqual(result.exit_code, 0)
            self.assertIn(f"Exported profile 'dev' to {output_file}", result.output)

            # Verify file was created with correct content
            self.assertTrue(output_file.exists())
            content = output_file.read_text()
            self.assertIn("terraform", content)
            self.assertIn("1.5.0", content)

    def test_profile_import(self):
        """Test importing a profile from a file."""
        # Create a profile file
        profile_file = self.temp_path / "profile.toml"
        profile_data = {"name": "imported", "tools": {"terraform": "1.6.0", "go": "1.22.0"}}
        profile_file.write_text(tomli_w.dumps(profile_data))

        with patch("wrknv.cli.commands.profile.WorkenvConfig") as mock_config_class:
            mock_config = Mock()
            mock_config.save_profile.return_value = None
            mock_config_class.return_value = mock_config

            result = self.runner.invoke(workenv_cli, ["profile", "import", str(profile_file)])

            self.assertEqual(result.exit_code, 0)
            self.assertIn("Imported profile 'imported'", result.output)
            mock_config.save_profile.assert_called_once_with(
                "imported", {"terraform": "1.6.0", "go": "1.22.0"}
            )


class TestProfileCommandIntegration(unittest.TestCase):
    """Integration tests for profile commands with real config files."""

    def setUp(self):
        """Set up test fixtures."""
        self.runner = click.testing.CliRunner()
        self.cli = create_cli()
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_profile_save_and_load_integration(self):
        """Test full save and load cycle with real config file."""
        config_file = self.temp_path / "wrknv.toml"
        config_file.write_text("""
project_name = "test-project"

[tools]
terraform = { version = "1.5.0" }
go = { version = "1.21.0" }
""")

        # Mock the config file location
        with patch("wrknv.wenv.config.Path.cwd") as mock_cwd:
            mock_cwd.return_value = self.temp_path

            # Save profile
            result = self.runner.invoke(self.cli, ["profile", "save", "test-profile"])
            self.assertEqual(result.exit_code, 0)

            # Verify profile was saved to file
            config_content = config_file.read_text()
            self.assertIn("profiles", config_content)
            self.assertIn("test-profile", config_content)

            # Load profile
            with patch("wrknv.cli.commands.profile.get_tool_manager") as mock_get_manager:
                mock_manager = Mock()
                mock_manager.install_version.return_value = None
                mock_get_manager.return_value = mock_manager

                result = self.runner.invoke(self.cli, ["profile", "load", "test-profile"])
                self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
