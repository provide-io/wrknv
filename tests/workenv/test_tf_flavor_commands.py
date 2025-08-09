"""
Tests for Terraform Flavor Management
=====================================
Tests for the set-flavor command that controls whether 'terraform' 
command uses HashiCorp Terraform (hctf) or OpenTofu (tofu).
"""

import pytest
import pathlib
from unittest.mock import Mock, patch
from click.testing import CliRunner

from wrkenv.workenv.cli import workenv_tf
from wrkenv.workenv.config import WorkenvConfig


class TestTerraformFlavorCommands:
    """Test terraform flavor management."""

    def setup_method(self):
        """Setup for each test."""
        self.runner = CliRunner()

    def test_set_flavor_to_terraform(self, tmp_path):
        """Test setting flavor to terraform."""
        # GIVEN: A default configuration
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Setting flavor to terraform
        with patch('tofusoup.workenv.config.WorkenvConfig._find_soup_toml', return_value=soup_toml):
            with patch('tofusoup.workenv.cli.get_tool_manager') as mock_get_manager:
                mock_manager = Mock()
                mock_manager.get_installed_version.return_value = "1.9.3"
                mock_get_manager.return_value = mock_manager
                
                result = self.runner.invoke(workenv_tf, ['set-flavor', 'terraform'])

        # THEN: It should succeed
        assert result.exit_code == 0
        assert "Set terraform command to use: terraform" in result.output
        assert "terraform → HashiCorp Terraform 1.9.3" in result.output

    def test_set_flavor_to_opentofu(self, tmp_path):
        """Test setting flavor to opentofu."""
        # GIVEN: A default configuration
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Setting flavor to opentofu
        with patch('tofusoup.workenv.config.WorkenvConfig._find_soup_toml', return_value=soup_toml):
            with patch('tofusoup.workenv.cli.get_tool_manager') as mock_get_manager:
                mock_manager = Mock()
                mock_manager.get_installed_version.return_value = "1.10.5"
                mock_get_manager.return_value = mock_manager
                
                result = self.runner.invoke(workenv_tf, ['set-flavor', 'opentofu'])

        # THEN: It should succeed
        assert result.exit_code == 0
        assert "Set terraform command to use: opentofu" in result.output
        assert "terraform → OpenTofu 1.10.5" in result.output

    def test_set_flavor_no_version_installed(self, tmp_path):
        """Test setting flavor when target tool not installed."""
        # GIVEN: Default configuration
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Setting flavor to opentofu but no tofu installed
        with patch('tofusoup.workenv.config.WorkenvConfig._find_soup_toml', return_value=soup_toml):
            with patch('tofusoup.workenv.cli.get_tool_manager') as mock_get_manager:
                mock_manager = Mock()
                mock_manager.get_installed_version.return_value = None
                mock_get_manager.return_value = mock_manager
                
                result = self.runner.invoke(workenv_tf, ['set-flavor', 'opentofu'])

        # THEN: It should warn about missing installation
        assert result.exit_code == 0
        assert "No OpenTofu version installed" in result.output
        assert "soup workenv tf install opentofu-<version>" in result.output

    def test_flavor_saved_to_config(self, tmp_path):
        """Test that flavor preference is saved to config."""
        # GIVEN: A configuration file
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
tools = {}
        """)

        # WHEN: Setting flavor
        with patch('tofusoup.workenv.config.WorkenvConfig._find_soup_toml', return_value=soup_toml):
            with patch('tofusoup.workenv.cli.get_tool_manager') as mock_get_manager:
                mock_manager = Mock()
                mock_manager.get_installed_version.return_value = "1.10.5"
                mock_get_manager.return_value = mock_manager
                
                result = self.runner.invoke(workenv_tf, ['set-flavor', 'opentofu'])

        # THEN: Config should be updated
        assert result.exit_code == 0
        
        # Verify config was written
        import tomllib
        with open(soup_toml, "rb") as f:
            config = tomllib.load(f)
        
        assert "workenv" in config
        assert "terraform_flavor" in config["workenv"]
        assert config["workenv"]["terraform_flavor"] == "opentofu"

# 📦🍜🧪🪄
