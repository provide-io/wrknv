"""
TDD Tests for TofuSoup Workenv CLI Behavior
===========================================
These tests define the exact CLI behavior expected from workenv commands.
"""

from __future__ import annotations

from unittest.mock import Mock, patch

from click.testing import CliRunner
import pytest

# These will fail initially - expected in TDD
try:
    from wrknv.cli.hub_cli import create_cli
    from wrknv.config import WorkenvConfig
except ImportError:
    create_cli = Mock()
    WorkenvConfig = Mock()


class TestWorkenvCLIBehavior:
    """Test the exact behavior of workenv CLI commands."""

    def setup_method(self) -> None:
        """Setup for each test method."""
        self.runner = CliRunner()

    def test_workenv_terraform_install_command(self) -> None:
        """
        TDD: `wrknv tf 1.6.2` should switch to OpenTofu 1.6.2
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "1.6.2"])

            # Should succeed
            if result.exit_code != 0:
                print(f"Exit code: {result.exit_code}")
                print(f"Output: {result.output}")
                print(f"Exception: {result.exception}")
            assert result.exit_code == 0

            # Should call switch_version with correct version (not install_version)
            mock_instance.switch_version.assert_called_once_with("1.6.2", dry_run=False)

            # Should show switching message
            assert "Switching to" in result.output or "OpenTofu" in result.output

    @pytest.mark.skip(reason="--latest flag not implemented yet")
    def test_workenv_terraform_latest_flag(self) -> None:
        """
        TDD: `wrknv tf --latest` should install latest OpenTofu version
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "--latest"])

            assert result.exit_code == 0
            mock_instance.install_latest.assert_called_once_with(dry_run=False)

    @pytest.mark.skip(reason="TDD spec - command not fully implemented")
    def test_workenv_terraform_list_versions(self) -> None:
        """
        TDD: `soup workenv tf --list` should show available OpenTofu versions
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_instance.get_available_versions.return_value = ["1.6.2", "1.6.1", "1.6.0"]

            # Make list_versions print the versions
            def mock_list_versions():
                for version in ["1.6.2", "1.6.1", "1.6.0"]:
                    print(f"   {version}")

            mock_instance.list_versions = mock_list_versions
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "--list"])

            assert result.exit_code == 0
            assert "1.6.2" in result.output
            assert "1.6.1" in result.output
            assert "available opentofu versions" in result.output.lower()

    @pytest.mark.skip(reason="TDD spec - command not fully implemented")
    def test_workenv_status_command(self) -> None:
        """
        TDD: `soup workenv status` should show installed tools
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_all_tools.return_value = {
                "terraform": "1.5.7",
                "tofu": "1.6.2",
                "uv": "0.4.15",
            }
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(create_cli(), ["status"])

            assert result.exit_code == 0
            # The new output uses a Rich table format, not plain text
            assert "1.5.7" in result.output  # terraform version
            assert "1.6.2" in result.output  # tofu version
            assert "0.4.15" in result.output  # uv version

    @pytest.mark.skip(reason="TDD spec - command not fully implemented")
    def test_workenv_sync_command(self) -> None:
        """
        TDD: `soup workenv sync` should install tools from soup.toml
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_all_tools.return_value = {"terraform": "1.5.7", "tofu": "1.6.2"}
            mock_config.return_value = mock_config_instance

            with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
                mock_tf_manager = Mock()
                mock_tofu_manager = Mock()
                mock_factory.side_effect = [mock_tf_manager, mock_tofu_manager]

                result = self.runner.invoke(create_cli(), ["sync"])

                assert result.exit_code == 0
                mock_tf_manager.install_version.assert_called_once_with("1.5.7", dry_run=False)
                mock_tofu_manager.install_version.assert_called_once_with("1.6.2", dry_run=False)

    @pytest.mark.skip(reason="TDD spec - dry-run flag not implemented")
    def test_workenv_dry_run_flag(self) -> None:
        """
        TDD: `--dry-run` flag should show what would be done without doing it
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "1.5.7", "--dry-run"])

            assert result.exit_code == 0
            mock_instance.switch_version.assert_called_once_with("1.5.7", dry_run=True)
            assert "[DRY-RUN]" in result.output or "Would" in result.output


class TestWorkenvProfileManagement:
    """Test workenv profile management CLI behavior."""

    def setup_method(self) -> None:
        self.runner = CliRunner()

    @pytest.mark.skip(reason="TDD spec - profile commands not implemented")
    def test_profile_save_command(self) -> None:
        """
        TDD: `soup workenv profile save dev` should save current state as profile
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.profile_exists.return_value = False
            mock_config_instance.get_all_tools.return_value = {}
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(create_cli(), ["profile", "save", "dev"])

            if result.exit_code != 0:
                print(f"Exit code: {result.exit_code}")
                print(f"Output: {result.output}")
                print(f"Exception: {result.exception}")
            assert result.exit_code == 0
            mock_config_instance.save_profile.assert_called_once_with("dev", {})

    @pytest.mark.skip(reason="TDD spec - profile commands not implemented")
    def test_profile_load_command(self) -> None:
        """
        TDD: `soup workenv profile load dev` should switch to dev profile
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_profile.return_value = {"terraform": "1.5.7", "tofu": "1.6.2"}
            mock_config.return_value = mock_config_instance

            with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
                mock_tf_manager = Mock()
                mock_tofu_manager = Mock()
                mock_factory.side_effect = [mock_tf_manager, mock_tofu_manager]

                result = self.runner.invoke(create_cli(), ["profile", "load", "dev"])

                assert result.exit_code == 0
                mock_tf_manager.install_version.assert_called_once_with("1.5.7", dry_run=False)
                mock_tofu_manager.install_version.assert_called_once_with("1.6.2", dry_run=False)

    @pytest.mark.skip(reason="TDD spec - profile commands not implemented")
    def test_profile_list_command(self) -> None:
        """
        TDD: `soup workenv profile list` should show available profiles
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.list_profiles.return_value = ["dev", "prod", "testing"]
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(create_cli(), ["profile", "list"])

            assert result.exit_code == 0
            assert "dev" in result.output
            assert "prod" in result.output
            assert "testing" in result.output


class TestWorkenvErrorHandling:
    """Test error handling behavior in workenv CLI."""

    def setup_method(self) -> None:
        self.runner = CliRunner()

    @pytest.mark.skip(reason="TDD spec - error handling not standardized")
    def test_invalid_version_error(self) -> None:
        """
        TDD: Invalid version should show helpful error message
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_instance.switch_version.side_effect = ValueError("Invalid version: invalid")
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "invalid"])

            assert result.exit_code != 0
            assert "Invalid version" in result.output or "Error" in result.output

    @pytest.mark.skip(reason="TDD spec - error handling not standardized")
    def test_network_error_handling(self) -> None:
        """
        TDD: Network errors should show helpful error message
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_instance.switch_version.side_effect = ConnectionError("Network unreachable")
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "1.5.7"])

            assert result.exit_code != 0
            assert "network" in result.output.lower() or "connection" in result.output.lower() or "Error" in result.output

    @pytest.mark.skip(reason="TDD spec - error handling not standardized")
    def test_permission_error_handling(self) -> None:
        """
        TDD: Permission errors should show helpful error message
        """
        with patch("wrknv.managers.factory.get_tool_manager") as mock_factory:
            mock_instance = Mock()
            mock_instance.switch_version.side_effect = PermissionError("Permission denied")
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(create_cli(), ["tf", "1.5.7"])

            assert result.exit_code != 0
            assert "permission" in result.output.lower() or "Error" in result.output


class TestWorkenvConfiguration:
    """Test workenv configuration CLI behavior."""

    def setup_method(self) -> None:
        self.runner = CliRunner()

    @pytest.mark.skip(reason="TDD spec - config commands changed")
    def test_config_show_command(self) -> None:
        """
        TDD: `soup workenv config show` should display current configuration
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.show_config.return_value = None  # Prints to console
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(create_cli(), ["config", "show"])

            assert result.exit_code == 0
            mock_config_instance.show_config.assert_called_once()

    @pytest.mark.skip(reason="TDD spec - config commands changed")
    def test_config_edit_command(self) -> None:
        """
        TDD: `soup workenv config edit` should open configuration for editing
        """
        with patch("wrknv.config.WorkenvConfig") as mock_config:
            mock_config_instance = Mock()
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(create_cli(), ["config", "edit"])

            assert result.exit_code == 0
            mock_config_instance.edit_config.assert_called_once()


# Integration test contracts
class TestWorkenvIntegrationBehavior:
    """Test integration behavior with TofuSoup ecosystem."""

    def test_harness_tool_requirements(self) -> None:
        """
        TDD: Workenv should install tools required by TofuSoup harness
        """
        # When running `soup harness build go-cty`, it should ensure Go is installed
        # When running conformance tests, it should ensure required TF/Tofu versions
        pass

    def test_soup_toml_integration(self) -> None:
        """
        TDD: Workenv should read from soup.toml and respect TofuSoup config patterns
        """
        pass


if __name__ == "__main__":
    # Run CLI behavior tests
    pytest.main([__file__, "-v", "--tb=short"])

# 🍲🥄🧪🪄
