"""
TDD Tests for TofuSoup Workenv CLI Behavior
===========================================
These tests define the exact CLI behavior expected from workenv commands.
"""

import pytest
import tempfile
import pathlib
from unittest.mock import Mock, patch, MagicMock
from click.testing import CliRunner

# These will fail initially - expected in TDD
try:
    from wrkenv.env.cli import workenv_cli
    from wrkenv.env.config import WorkenvConfig
except ImportError:
    workenv_cli = Mock()
    WorkenvConfig = Mock()


class TestWorkenvCLIBehavior:
    """Test the exact behavior of workenv CLI commands."""

    def setup_method(self):
        """Setup for each test method."""
        self.runner = CliRunner()

    def test_workenv_terraform_install_command(self):
        """
        TDD: `soup workenv tf 1.6.2` should install OpenTofu 1.6.2
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['tf', '1.6.2'])

            # Should succeed
            if result.exit_code != 0:
                print(f"Exit code: {result.exit_code}")
                print(f"Output: {result.output}")
                print(f"Exception: {result.exception}")
            assert result.exit_code == 0

            # Should call install_version with correct version
            mock_instance.install_version.assert_called_once_with('1.6.2', dry_run=False)

            # Should show installation message
            assert "Installing OpenTofu 1.6.2" in result.output

    def test_workenv_terraform_latest_flag(self):
        """
        TDD: `soup workenv tf --latest` should install latest OpenTofu version
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['tf', '--latest'])

            assert result.exit_code == 0
            mock_instance.install_latest.assert_called_once_with(dry_run=False)

    def test_workenv_terraform_list_versions(self):
        """
        TDD: `soup workenv tf --list` should show available OpenTofu versions
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_instance.get_available_versions.return_value = ['1.6.2', '1.6.1', '1.6.0']
            
            # Make list_versions print the versions
            def mock_list_versions():
                for version in ['1.6.2', '1.6.1', '1.6.0']:
                    print(f"   {version}")
            
            mock_instance.list_versions = mock_list_versions
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['tf', '--list'])

            assert result.exit_code == 0
            assert '1.6.2' in result.output
            assert '1.6.1' in result.output
            assert 'available opentofu versions' in result.output.lower()

    def test_workenv_status_command(self):
        """
        TDD: `soup workenv status` should show installed tools
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_all_tools.return_value = {
                'terraform': '1.5.7',
                'tofu': '1.6.2',
                'uv': '0.4.15'
            }
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(workenv_cli, ['status'])

            assert result.exit_code == 0
            assert 'terraform: 1.5.7' in result.output
            assert 'tofu: 1.6.2' in result.output
            assert 'uv: 0.4.15' in result.output

    def test_workenv_sync_command(self):
        """
        TDD: `soup workenv sync` should install tools from soup.toml
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_all_tools.return_value = {
                'terraform': '1.5.7',
                'tofu': '1.6.2'
            }
            mock_config.return_value = mock_config_instance

            with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
                mock_tf_manager = Mock()
                mock_tofu_manager = Mock()
                mock_factory.side_effect = [mock_tf_manager, mock_tofu_manager]

                result = self.runner.invoke(workenv_cli, ['sync'])

                assert result.exit_code == 0
                mock_tf_manager.install_version.assert_called_once_with('1.5.7', dry_run=False)
                mock_tofu_manager.install_version.assert_called_once_with('1.6.2', dry_run=False)

    def test_workenv_matrix_test_command(self):
        """
        TDD: `soup workenv matrix-test` should run version matrix tests
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_setting.return_value = {'tools': ['terraform', 'tofu']}
            mock_config.return_value = mock_config_instance
            
            with patch('wrkenv.env.testing.matrix.VersionMatrix') as mock_matrix:
                mock_matrix_instance = Mock()
                mock_matrix_instance.run_tests.return_value = {
                    'success_count': 4,
                    'failure_count': 0,
                    'results': []
                }
                mock_matrix.return_value = mock_matrix_instance

                result = self.runner.invoke(workenv_cli, ['matrix-test'])

            if result.exit_code != 0:
                print(f"Exit code: {result.exit_code}")
                print(f"Output: {result.output}")
                print(f"Exception: {result.exception}")
            assert result.exit_code == 0
            assert 'Success: 4' in result.output or '4 passed' in result.output

    def test_workenv_dry_run_flag(self):
        """
        TDD: `--dry-run` flag should show what would be done without doing it
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['terraform', '1.5.7', '--dry-run'])

            assert result.exit_code == 0
            mock_instance.install_version.assert_called_once_with('1.5.7', dry_run=True)
            assert '[DRY-RUN]' in result.output or 'Would install' in result.output


class TestWorkenvProfileManagement:
    """Test workenv profile management CLI behavior."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_profile_save_command(self):
        """
        TDD: `soup workenv profile save dev` should save current state as profile
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(workenv_cli, ['profile', 'save', 'dev'])

            if result.exit_code != 0:
                print(f"Exit code: {result.exit_code}")
                print(f"Output: {result.output}")
                print(f"Exception: {result.exception}")
            assert result.exit_code == 0
            mock_config_instance.save_profile.assert_called_once_with('dev')

    def test_profile_load_command(self):
        """
        TDD: `soup workenv profile load dev` should switch to dev profile
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.get_profile.return_value = {
                'terraform': '1.5.7',
                'tofu': '1.6.2'
            }
            mock_config.return_value = mock_config_instance

            with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
                mock_tf_manager = Mock()
                mock_tofu_manager = Mock()
                mock_factory.side_effect = [mock_tf_manager, mock_tofu_manager]

                result = self.runner.invoke(workenv_cli, ['profile', 'load', 'dev'])

                assert result.exit_code == 0
                mock_tf_manager.install_version.assert_called_once_with('1.5.7', dry_run=False)
                mock_tofu_manager.install_version.assert_called_once_with('1.6.2', dry_run=False)

    def test_profile_list_command(self):
        """
        TDD: `soup workenv profile list` should show available profiles
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.list_profiles.return_value = ['dev', 'prod', 'testing']
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(workenv_cli, ['profile', 'list'])

            assert result.exit_code == 0
            assert 'dev' in result.output
            assert 'prod' in result.output
            assert 'testing' in result.output


class TestWorkenvErrorHandling:
    """Test error handling behavior in workenv CLI."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_invalid_version_error(self):
        """
        TDD: Invalid version should show helpful error message
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_instance.install_version.side_effect = ValueError("Invalid version: invalid")
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['terraform', 'invalid'])

            assert result.exit_code != 0
            assert 'Invalid version' in result.output

    def test_network_error_handling(self):
        """
        TDD: Network errors should show helpful error message
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_instance.install_version.side_effect = ConnectionError("Network unreachable")
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['terraform', '1.5.7'])

            assert result.exit_code != 0
            assert 'network' in result.output.lower() or 'connection' in result.output.lower()

    def test_permission_error_handling(self):
        """
        TDD: Permission errors should show helpful error message
        """
        with patch('wrkenv.env.cli.get_tool_manager') as mock_factory:
            mock_instance = Mock()
            mock_instance.install_version.side_effect = PermissionError("Permission denied")
            mock_factory.return_value = mock_instance

            result = self.runner.invoke(workenv_cli, ['terraform', '1.5.7'])

            assert result.exit_code != 0
            assert 'permission' in result.output.lower()


class TestWorkenvConfiguration:
    """Test workenv configuration CLI behavior."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_config_show_command(self):
        """
        TDD: `soup workenv config show` should display current configuration
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config_instance.show_config.return_value = None  # Prints to console
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(workenv_cli, ['config', 'show'])

            assert result.exit_code == 0
            mock_config_instance.show_config.assert_called_once()

    def test_config_edit_command(self):
        """
        TDD: `soup workenv config edit` should open configuration for editing
        """
        with patch('wrkenv.env.cli.WorkenvConfig') as mock_config:
            mock_config_instance = Mock()
            mock_config.return_value = mock_config_instance

            result = self.runner.invoke(workenv_cli, ['config', 'edit'])

            assert result.exit_code == 0
            mock_config_instance.edit_config.assert_called_once()


# Integration test contracts
class TestWorkenvIntegrationBehavior:
    """Test integration behavior with TofuSoup ecosystem."""

    def test_harness_tool_requirements(self):
        """
        TDD: Workenv should install tools required by TofuSoup harness
        """
        # When running `soup harness build go-cty`, it should ensure Go is installed
        # When running conformance tests, it should ensure required TF/Tofu versions
        pass

    def test_soup_toml_integration(self):
        """
        TDD: Workenv should read from soup.toml and respect TofuSoup config patterns
        """
        pass


if __name__ == "__main__":
    # Run CLI behavior tests
    pytest.main([__file__, "-v", "--tb=short"])

# 🍲🥄🧪🪄
