"""
TDD Tests for soup workenv tf commands
======================================
These tests define the expected behavior for the new tf command structure:
- soup workenv tf list
- soup workenv tf install <version>
- soup workenv tf status  
- soup workenv tf clean [version]
"""

import pytest
from click.testing import CliRunner
from unittest.mock import Mock, patch, MagicMock
import pathlib

# Import will fail initially - that's expected in TDD
try:
    from wrkenv.env.cli import workenv_cli
except ImportError:
    workenv_cli = Mock()


class TestWorkenvTfCommands:
    """Test the new tf command structure."""
    
    def setup_method(self):
        """Setup for each test method."""
        self.runner = CliRunner()
    
    def test_tf_list_command(self):
        """
        TDD: `soup workenv tf list` should list available versions
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_tofu_manager = Mock()
            mock_terraform_manager = Mock()
            
            # Mock OpenTofu versions
            mock_tofu_manager.get_available_versions.return_value = ['1.6.2', '1.6.1', '1.6.0']
            mock_tofu_manager.tool_name = 'tofu'
            
            # Mock Terraform versions  
            mock_terraform_manager.get_available_versions.return_value = ['1.5.7', '1.5.6', '1.5.5']
            mock_terraform_manager.tool_name = 'terraform'
            
            def get_manager(tool_name, config):
                if tool_name == 'tofu':
                    return mock_tofu_manager
                elif tool_name == 'terraform':
                    return mock_terraform_manager
                return None
                
            mock_get_manager.side_effect = get_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'list'])
            
            assert result.exit_code == 0
            assert "OpenTofu versions:" in result.output
            assert "opentofu-1.6.2" in result.output
            assert "opentofu-1.6.1" in result.output
            assert "Terraform versions:" in result.output
            assert "terraform-1.5.7" in result.output
            assert "terraform-1.5.6" in result.output
    
    def test_tf_install_opentofu_version(self):
        """
        TDD: `soup workenv tf install opentofu-1.6.2` should install OpenTofu 1.6.2
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'install', 'opentofu-1.6.2'])
            
            assert result.exit_code == 0
            mock_get_manager.assert_called_with('tofu', mock.ANY)
            mock_manager.install_version.assert_called_once_with('1.6.2', dry_run=False)
            assert "Installing OpenTofu 1.6.2" in result.output
    
    def test_tf_install_terraform_version(self):
        """
        TDD: `soup workenv tf install terraform-1.5.7` should install Terraform 1.5.7
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'install', 'terraform-1.5.7'])
            
            assert result.exit_code == 0
            mock_get_manager.assert_called_with('terraform', mock.ANY)
            mock_manager.install_version.assert_called_once_with('1.5.7', dry_run=False)
            assert "Installing Terraform 1.5.7" in result.output
    
    def test_tf_install_latest_versions(self):
        """
        TDD: `soup workenv tf install opentofu-latest` and `terraform-latest`
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager
            
            # Test OpenTofu latest
            result = self.runner.invoke(workenv_cli, ['tf', 'install', 'opentofu-latest'])
            assert result.exit_code == 0
            mock_manager.install_latest.assert_called_with(dry_run=False)
            
            # Test Terraform latest
            result = self.runner.invoke(workenv_cli, ['tf', 'install', 'terraform-latest'])
            assert result.exit_code == 0
            assert mock_manager.install_latest.call_count == 2
    
    def test_tf_install_invalid_format(self):
        """
        TDD: Invalid version format should show error
        """
        result = self.runner.invoke(workenv_cli, ['tf', 'install', '1.6.2'])
        
        assert result.exit_code != 0
        assert "Invalid version format" in result.output
        assert "Use: opentofu-X.Y.Z or terraform-X.Y.Z" in result.output
    
    def test_tf_status_command(self):
        """
        TDD: `soup workenv tf status` should show installed versions
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_tofu_manager = Mock()
            mock_terraform_manager = Mock()
            
            # Mock installed versions
            mock_tofu_manager.get_installed_version.return_value = '1.6.2'
            mock_tofu_manager.get_current_binary_path.return_value = pathlib.Path('/path/to/tofu')
            mock_tofu_manager.tool_name = 'tofu'
            
            mock_terraform_manager.get_installed_version.return_value = '1.5.7'
            mock_terraform_manager.get_current_binary_path.return_value = pathlib.Path('/path/to/terraform')
            mock_terraform_manager.tool_name = 'terraform'
            
            def get_manager(tool_name, config):
                if tool_name == 'tofu':
                    return mock_tofu_manager
                elif tool_name == 'terraform':
                    return mock_terraform_manager
                return None
                
            mock_get_manager.side_effect = get_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'status'])
            
            assert result.exit_code == 0
            assert "OpenTofu: 1.6.2" in result.output
            assert "Terraform: 1.5.7" in result.output
    
    def test_tf_clean_all_command(self):
        """
        TDD: `soup workenv tf clean` should remove all tf tool versions
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_tofu_manager = Mock()
            mock_terraform_manager = Mock()
            
            mock_tofu_manager.get_installed_versions.return_value = ['1.6.2', '1.6.1']
            mock_terraform_manager.get_installed_versions.return_value = ['1.5.7']
            
            def get_manager(tool_name, config):
                if tool_name == 'tofu':
                    return mock_tofu_manager
                elif tool_name == 'terraform':
                    return mock_terraform_manager
                return None
                
            mock_get_manager.side_effect = get_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'clean'], input='y\n')
            
            assert result.exit_code == 0
            assert mock_tofu_manager.remove_version.call_count == 2
            assert mock_terraform_manager.remove_version.call_count == 1
            assert "Removed 3 versions" in result.output
    
    def test_tf_clean_specific_version(self):
        """
        TDD: `soup workenv tf clean --tf-version=opentofu-1.6.1` should remove specific version
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'clean', '--tf-version=opentofu-1.6.1'])
            
            assert result.exit_code == 0
            mock_get_manager.assert_called_with('tofu', mock.ANY)
            mock_manager.remove_version.assert_called_once_with('1.6.1')
            assert "Removed OpenTofu 1.6.1" in result.output
    
    def test_tf_clean_multiple_versions(self):
        """
        TDD: `soup workenv tf clean --tf-version=terraform-1.5.7 --tf-version=opentofu-1.6.1`
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_tofu_manager = Mock()
            mock_terraform_manager = Mock()
            
            def get_manager(tool_name, config):
                if tool_name == 'tofu':
                    return mock_tofu_manager
                elif tool_name == 'terraform':
                    return mock_terraform_manager
                return None
                
            mock_get_manager.side_effect = get_manager
            
            result = self.runner.invoke(workenv_cli, [
                'tf', 'clean', 
                '--tf-version=terraform-1.5.7',
                '--tf-version=opentofu-1.6.1'
            ])
            
            assert result.exit_code == 0
            mock_terraform_manager.remove_version.assert_called_once_with('1.5.7')
            mock_tofu_manager.remove_version.assert_called_once_with('1.6.1')
            assert "Removed 2 versions" in result.output
    
    def test_tf_install_with_dry_run(self):
        """
        TDD: `soup workenv tf install opentofu-1.6.2 --dry-run` should not actually install
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_manager = Mock()
            mock_get_manager.return_value = mock_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'install', 'opentofu-1.6.2', '--dry-run'])
            
            assert result.exit_code == 0
            mock_manager.install_version.assert_called_once_with('1.6.2', dry_run=True)
            assert "[DRY-RUN]" in result.output
    
    def test_tf_without_subcommand_shows_help(self):
        """
        TDD: `soup workenv tf` should show available subcommands
        """
        result = self.runner.invoke(workenv_cli, ['tf'])
        
        assert result.exit_code == 0
        assert "list" in result.output
        assert "install" in result.output
        assert "status" in result.output
        assert "clean" in result.output
    
    def test_tf_list_with_version_filter(self):
        """
        TDD: `soup workenv tf list --tf-version=opentofu-latest` filters versions
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_tofu_manager = Mock()
            mock_tofu_manager.get_available_versions.return_value = ['1.6.2', '1.6.1', '1.6.0']
            
            def get_manager(tool_name, config):
                if tool_name == 'tofu':
                    return mock_tofu_manager
                return None
                
            mock_get_manager.side_effect = get_manager
            
            result = self.runner.invoke(workenv_cli, ['tf', 'list', '--tf-version=opentofu-latest'])
            
            assert result.exit_code == 0
            assert "opentofu-1.6.2 (latest)" in result.output
            assert "terraform" not in result.output.lower() or "Terraform versions:" not in result.output
    
    def test_tf_list_with_version_comparison(self):
        """
        TDD: `soup workenv tf list --tf-version=terraform>=1.11` filters with comparison
        """
        with patch('wrkenv.env.managers.factory.get_tool_manager') as mock_get_manager:
            mock_terraform_manager = Mock()
            mock_terraform_manager.get_available_versions.return_value = ['1.12.0', '1.11.5', '1.11.0', '1.10.0', '1.9.0']
            
            def get_manager(tool_name, config):
                if tool_name == 'terraform':
                    return mock_terraform_manager
                return None
                
            mock_get_manager.side_effect = get_manager
            
            # Need to mock packaging.version
            with patch('wrkenv.env.cli.version_matches') as mock_matches:
                # Make it return True for versions >= 1.11
                def matches(version, op, target):
                    if op == '>=' and target == '1.11':
                        return version in ['1.12.0', '1.11.5', '1.11.0']
                    return False
                
                mock_matches.side_effect = matches
                
                result = self.runner.invoke(workenv_cli, ['tf', 'list', '--tf-version=terraform>=1.11'])
                
                assert result.exit_code == 0
                # Should show filtered versions
                assert "terraform-1.12.0" in result.output or "1.11" in result.output
                # Should not show older versions
                assert "terraform-1.10.0" not in result.output

# 🍲🥄🧪🪄
