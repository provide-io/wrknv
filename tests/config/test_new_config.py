"""
Test the new foundation-based config system
===========================================
Tests for the WorkenvConfig implementation using provide.foundation.
"""

import os
import pathlib
import tempfile
from unittest.mock import patch

import pytest

from wrknv.config import WorkenvConfig, ConfigSource, EnvironmentConfigSource, FileConfigSource


class TestWorkenvConfig:
    """Test the new WorkenvConfig implementation."""
    
    def test_load_with_defaults(self):
        """Should load with sensible defaults."""
        config = WorkenvConfig.load()
        
        assert config.project_name == "my-project"
        assert config.version == "1.0.0"
        assert config.workenv.log_level == "WARNING"
        assert config.workenv.auto_install is True
        
    def test_load_from_file(self):
        """Should load configuration from TOML file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = pathlib.Path(tmpdir) / ".wrknv.toml"
            config_file.write_text("""
project_name = "test-project"
version = "2.0.0"

[tools]
terraform = "1.5.7"
go = "1.21.0"

[workenv]
log_level = "DEBUG"
auto_install = false
""")
            
            with patch('pathlib.Path.cwd', return_value=pathlib.Path(tmpdir)):
                config = WorkenvConfig.load()
                
                assert config.project_name == "test-project"
                assert config.version == "2.0.0"
                assert config.get_tool_version("terraform") == "1.5.7"
                assert config.get_tool_version("go") == "1.21.0"
                assert config.workenv.log_level == "DEBUG"
                assert config.workenv.auto_install is False
    
    def test_environment_variables(self):
        """Should support WRKNV_ environment variables."""
        with patch.dict('os.environ', {
            'WRKNV_PROJECT_NAME': 'env-project',
            'WRKNV_VERSION': '3.0.0',
            'WRKNV_LOG_LEVEL': 'INFO',
            'WRKNV_AUTO_INSTALL': 'false',
        }):
            config = WorkenvConfig.load()
            
            # Environment variables should override defaults
            assert config.project_name == "env-project"
            assert config.version == "3.0.0"
            assert config.workenv.log_level == "INFO"
            assert config.workenv.auto_install is False
    
    def test_tool_management(self):
        """Should manage tool versions correctly."""
        config = WorkenvConfig.load()
        
        # Initially no tools
        assert config.get_all_tools() == {}
        assert config.get_tool_version("terraform") is None
        
        # Add some tools
        config.tools = {
            "terraform": "1.5.7",
            "go": {"version": "1.21.0", "path": "/usr/local/go"},
        }
        
        # Should retrieve tool versions
        assert config.get_tool_version("terraform") == "1.5.7"
        assert config.get_tool_version("go") == "1.21.0"
        
        all_tools = config.get_all_tools()
        assert all_tools["terraform"] == "1.5.7"
        assert all_tools["go"] == "1.21.0"
    
    def test_profile_management(self):
        """Should manage profiles correctly."""
        config = WorkenvConfig.load()
        
        # Initially no profiles
        assert config.list_profiles() == []
        assert config.get_profile("dev") is None
        
        # Add profiles
        config.profiles = {
            "dev": {"terraform": "1.6.0", "go": "1.21.0"},
            "prod": {"terraform": "1.5.7", "go": "1.20.0"},
        }
        
        # Should list profiles
        profiles = config.list_profiles()
        assert "dev" in profiles
        assert "prod" in profiles
        
        # Should get profile data
        dev_profile = config.get_profile("dev")
        assert dev_profile["terraform"] == "1.6.0"
        assert dev_profile["go"] == "1.21.0"


class TestConfigSources:
    """Test the ConfigSource classes."""
    
    def test_file_config_source(self):
        """Should load from TOML files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = pathlib.Path(tmpdir) / "test.toml"
            config_file.write_text("""
[workenv.tools]
terraform = "1.5.7"
go = "1.21.0"

[workenv.profiles.dev]
terraform = "1.6.0"

[workenv.settings]
verify_checksums = true
""")
            
            source = FileConfigSource(config_file, "workenv")
            
            # Should load tools
            assert source.get_tool_version("terraform") == "1.5.7"
            assert source.get_tool_version("go") == "1.21.0"
            assert source.get_tool_version("missing") is None
            
            # Should load all tools
            tools = source.get_all_tools()
            assert tools["terraform"] == "1.5.7"
            assert tools["go"] == "1.21.0"
            
            # Should load profiles
            dev_profile = source.get_profile("dev")
            assert dev_profile["terraform"] == "1.6.0"
            
            # Should load settings
            assert source.get_setting("verify_checksums") is True
    
    def test_environment_config_source(self):
        """Should load from environment variables."""
        with patch.dict('os.environ', {
            'TEST_TERRAFORM_VERSION': '1.7.0',
            'TEST_GO_VERSION': '1.22.0',
            'TEST_VERIFY_CHECKSUMS': 'true',
            'TEST_INSTALL_PATH': '/custom/path',
        }):
            source = EnvironmentConfigSource("TEST")
            
            # Should read tool versions
            assert source.get_tool_version("terraform") == "1.7.0"
            assert source.get_tool_version("go") == "1.22.0"
            assert source.get_tool_version("missing") is None
            
            # Should read all tools
            tools = source.get_all_tools()
            assert tools["terraform"] == "1.7.0"
            assert tools["go"] == "1.22.0"
            
            # Should read settings with boolean parsing
            assert source.get_setting("verify_checksums") is True
            assert source.get_setting("install_path") == "/custom/path"
    
    def test_environment_boolean_parsing(self):
        """Should parse boolean values correctly."""
        source = EnvironmentConfigSource("TEST")
        
        with patch.dict('os.environ', {'TEST_SETTING': 'true'}):
            assert source.get_setting("setting") is True
        
        with patch.dict('os.environ', {'TEST_SETTING': 'false'}):
            assert source.get_setting("setting") is False
        
        with patch.dict('os.environ', {'TEST_SETTING': '1'}):
            assert source.get_setting("setting") is True
        
        with patch.dict('os.environ', {'TEST_SETTING': '0'}):
            assert source.get_setting("setting") is False
        
        with patch.dict('os.environ', {'TEST_SETTING': 'other'}):
            assert source.get_setting("setting") == "other"


class TestWorkenvConfigMethods:
    """Test WorkenvConfig utility methods."""
    
    def test_get_setting(self):
        """Should retrieve settings with dot notation."""
        config = WorkenvConfig.load()
        
        # Should get direct attributes
        assert config.get_setting("project_name") == "my-project"
        
        # Should get nested attributes
        assert config.get_setting("workenv.log_level") == "WARNING"
        assert config.get_setting("workenv.auto_install") is True
        
        # Should return default for missing
        assert config.get_setting("missing", "default") == "default"
    
    def test_validation(self):
        """Should validate configuration correctly."""
        config = WorkenvConfig.load()
        
        # Default config should be valid
        is_valid, errors = config.validate()
        assert is_valid
        assert errors == []
        
        # Invalid tool version should fail
        config.tools = {"terraform": {"version": "invalid.version"}}
        is_valid, errors = config.validate()
        assert not is_valid
        assert any("Invalid version" in error for error in errors)
    
    def test_to_dict(self):
        """Should convert to dictionary correctly."""
        config = WorkenvConfig.load()
        config.project_name = "test"
        config.tools = {"terraform": "1.5.7"}
        
        data = config.to_dict()
        
        assert data["project_name"] == "test"
        assert data["tools"]["terraform"] == "1.5.7"
        assert data["workenv"]["log_level"] == "WARNING"