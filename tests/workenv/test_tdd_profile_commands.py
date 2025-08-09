"""
TDD Tests for TofuSoup Workenv Profile Commands
===============================================
Test-driven development for profile management functionality.
"""

import json
import pathlib
import pytest
from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from wrkenv.workenv.cli import workenv_profile
from wrkenv.workenv.config import WorkenvConfig


class TestWorkenvProfileCommands:
    """Test profile management commands."""

    def test_profile_list_shows_default_when_no_profiles(self, tmp_path):
        """When no profiles are defined, list should show 'default' profile."""
        # GIVEN: A configuration with no profiles defined
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Running profile list
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            result = runner.invoke(workenv_profile, ["list"])

        # THEN: It should show default profile with proper naming
        assert result.exit_code == 0
        assert (
            "default (soup_<os>_<arch>)" in result.output or "default" in result.output
        )
        assert "Available Profiles:" in result.output

    def test_profile_list_shows_custom_profiles(self, tmp_path):
        """Profile list should show all defined profiles plus default."""
        # GIVEN: A configuration with custom profiles
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.development]
terraform = "1.5.7"
tofu = "1.8.0"

[workenv.profiles.production]
terraform = "1.4.0"
tofu = "1.7.0"
        """)

        # WHEN: Running profile list
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            result = runner.invoke(workenv_profile, ["list"])

        # THEN: It should show all profiles including default
        assert result.exit_code == 0
        assert "default" in result.output
        assert "development" in result.output
        assert "production" in result.output

    def test_profile_save_creates_new_profile(self, tmp_path, monkeypatch):
        """Profile save should create a new profile with current tool versions."""
        # GIVEN: A working environment with tools installed
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # Mock metadata showing installed versions
        metadata_file = tmp_path / ".terraform.versions" / "metadata.json"
        metadata_file.parent.mkdir(parents=True)
        metadata_file.write_text(
            json.dumps(
                {
                    "workenv": {
                        "default": {
                            "terraform_version": "1.9.3",
                            "opentofu_version": "1.10.5",
                        }
                    }
                }
            )
        )

        # WHEN: Saving current state as a profile
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("pathlib.Path.home", return_value=tmp_path):
                with patch("wrkenv.workenv.config.tomli_w"):  # Mock the writer
                    result = runner.invoke(workenv_profile, ["save", "testing"])

        # THEN: It should succeed
        assert result.exit_code == 0
        assert "Saved profile 'testing'" in result.output

    def test_profile_load_switches_to_profile(self, tmp_path):
        """Profile load should install tools from the specified profile."""
        # GIVEN: A configuration with a saved profile
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.staging]
terraform = "1.8.5"
tofu = "1.9.0"
        """)

        # WHEN: Loading the profile
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("wrkenv.workenv.cli.get_tool_manager") as mock_manager:
                # Mock the tool manager
                mock_tm = MagicMock()
                mock_manager.return_value = mock_tm

                result = runner.invoke(workenv_profile, ["load", "staging"])

        # THEN: It should attempt to install the profile's tools
        assert result.exit_code == 0
        assert "Loading profile 'staging'" in result.output
        # Verify install was called for each tool
        assert mock_tm.install_version.call_count >= 1

    def test_profile_load_nonexistent_profile(self, tmp_path):
        """Loading a non-existent profile should fail gracefully."""
        # GIVEN: A configuration without the requested profile
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Trying to load a non-existent profile
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            result = runner.invoke(workenv_profile, ["load", "nonexistent"])

        # THEN: It should fail with clear error
        assert result.exit_code == 1
        assert "Profile 'nonexistent' not found" in result.output

    def test_profile_delete_removes_profile(self, tmp_path):
        """Profile delete should remove the specified profile."""
        # GIVEN: A configuration with profiles
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.temporary]
terraform = "1.7.0"
        """)

        # WHEN: Deleting a profile with --force
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("wrkenv.workenv.config.tomli_w"):  # Mock the writer
                result = runner.invoke(
                    workenv_profile, ["delete", "temporary", "--force"]
                )

        # THEN: It should succeed
        assert result.exit_code == 0
        assert "Deleted profile 'temporary'" in result.output

    def test_profile_delete_requires_confirmation(self, tmp_path):
        """Profile delete should ask for confirmation without --force."""
        # GIVEN: A configuration with profiles
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.sensitive]
terraform = "1.7.0"
        """)

        # WHEN: Deleting without --force and declining
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            result = runner.invoke(
                workenv_profile, ["delete", "sensitive"], input="n\n"
            )

        # THEN: It should cancel
        assert result.exit_code == 0
        assert "Cancelled" in result.output

    def test_profile_list_shows_tool_count(self, tmp_path):
        """Profile list should show the number of tools in each profile."""
        # GIVEN: Profiles with different numbers of tools
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.minimal]
terraform = "1.9.0"

[workenv.profiles.full]
terraform = "1.9.0"
tofu = "1.10.0"
go = "1.21.0"
uv = "0.1.0"
        """)

        # WHEN: Listing profiles
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            result = runner.invoke(workenv_profile, ["list"])

        # THEN: It should show tool counts
        assert result.exit_code == 0
        assert "minimal (1 tool)" in result.output
        assert "full (4 tools)" in result.output

    def test_profile_save_without_tools_shows_warning(self, tmp_path):
        """Saving a profile when no tools are installed should show a warning."""
        # GIVEN: No tools installed
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # Empty metadata
        metadata_file = tmp_path / ".terraform.versions" / "metadata.json"
        metadata_file.parent.mkdir(parents=True)
        metadata_file.write_text(json.dumps({"workenv": {"default": {}}}))

        # WHEN: Trying to save a profile
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("pathlib.Path.home", return_value=tmp_path):
                with patch("wrkenv.workenv.cli.get_tool_manager") as mock_manager:
                    # Mock tool managers returning no installed versions
                    mock_tm = MagicMock()
                    mock_tm.get_installed_version.return_value = None
                    mock_manager.return_value = mock_tm

                    result = runner.invoke(workenv_profile, ["save", "empty"])

        # THEN: It should show a warning
        assert result.exit_code == 0
        assert "No tools installed to save" in result.output

    def test_profile_save_overwrites_existing(self, tmp_path):
        """Saving a profile with the same name should overwrite the existing one."""
        # GIVEN: An existing profile
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.myprofile]
terraform = "1.5.0"
tofu = "1.7.0"
        """)

        # WHEN: Saving with the same name
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("wrkenv.workenv.cli.get_tool_manager") as mock_manager:
                # Mock tool managers returning new versions
                mock_tm = MagicMock()
                # Return a version for any tool
                mock_tm.get_installed_version.return_value = "1.9.3"
                mock_manager.return_value = mock_tm

                with patch("wrkenv.workenv.config.tomli_w"):
                    result = runner.invoke(workenv_profile, ["save", "myprofile"])

        # THEN: It should succeed
        assert result.exit_code == 0
        assert "Saved profile 'myprofile'" in result.output

    def test_profile_delete_nonexistent_fails(self, tmp_path):
        """Deleting a non-existent profile should fail gracefully."""
        # GIVEN: No profile exists
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Trying to delete non-existent profile
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            result = runner.invoke(
                workenv_profile, ["delete", "nonexistent", "--force"]
            )

        # THEN: It should fail with clear error
        assert result.exit_code == 1
        assert "Profile 'nonexistent' not found" in result.output

    def test_profile_load_with_dry_run(self, tmp_path):
        """Profile load --dry-run should show what would be done without installing."""
        # GIVEN: A profile
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv.profiles.testing]
terraform = "1.9.0"
tofu = "1.10.0"
        """)

        # WHEN: Loading with --dry-run
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("wrkenv.workenv.cli.get_tool_manager") as mock_manager:
                mock_tm = MagicMock()
                mock_manager.return_value = mock_tm

                result = runner.invoke(
                    workenv_profile, ["load", "testing", "--dry-run"]
                )

        # THEN: It should show dry-run messages
        assert result.exit_code == 0
        assert "[DRY-RUN]" in result.output
        assert "Would install terraform 1.9.0" in result.output
        assert "Would install tofu 1.10.0" in result.output
        # Verify install was called with dry_run=True
        mock_tm.install_version.assert_called_with("1.10.0", dry_run=True)

    def test_profile_with_special_characters(self, tmp_path):
        """Profile names with special characters should be handled properly."""
        # GIVEN: A configuration
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Saving with special characters
        runner = CliRunner()
        with patch(
            "wrkenv.workenv.config.WorkenvConfig._find_soup_toml",
            return_value=soup_toml,
        ):
            with patch("wrkenv.workenv.cli.get_tool_manager") as mock_manager:
                mock_tm = MagicMock()
                mock_tm.get_installed_version.return_value = "1.9.0"
                mock_manager.return_value = mock_tm

                with patch("wrkenv.workenv.config.tomli_w"):
                    result = runner.invoke(
                        workenv_profile, ["save", "my-test_profile.v1"]
                    )

        # THEN: It should handle the name properly
        assert result.exit_code == 0
        assert "Saved profile 'my-test_profile.v1'" in result.output

# 🍲🥄🧪🪄
