"""
TDD Tests for wrkenv Configuration Integration
==============================================
These tests define the expected behavior for wrkenv's flexible configuration system.
"""

import pathlib
import tempfile
from unittest.mock import Mock, patch

import pytest

from wrkenv import WorkenvConfig
from wrkenv.wenv.config import (
    ConfigSource,
    EnvironmentConfigSource,
    FileConfigSource,
)


class TestConfigSourceContracts:
    """TDD contracts for configuration sources."""
    
    def test_config_source_base_interface(self):
        """
        CONTRACT: ConfigSource should define the base interface
        """
        source = ConfigSource()
        
        # Should return None/empty by default
        assert source.get_tool_version("terraform") is None
        assert source.get_all_tools() == {}
        assert source.get_profile("dev") == {}
        assert source.get_setting("verify_checksums") is None
        assert source.get_setting("verify_checksums", True) is True
    
    def test_file_config_source_loads_toml(self):
        """
        CONTRACT: FileConfigSource should load configuration from TOML files
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = pathlib.Path(tmpdir) / "wrkenv.toml"
            config_file.write_text("""
[workenv.tools]
terraform = "1.5.7"
tofu = "1.6.2"

[workenv.profiles.dev]
terraform = "1.6.0"
tofu = "1.7.0"

[workenv.settings]
verify_checksums = true
install_path = "~/.wrkenv/tools"
""")
            
            source = FileConfigSource(config_file, "workenv")
            
            # Should load tool versions
            assert source.get_tool_version("terraform") == "1.5.7"
            assert source.get_tool_version("tofu") == "1.6.2"
            
            # Should load all tools
            tools = source.get_all_tools()
            assert tools["terraform"] == "1.5.7"
            assert tools["tofu"] == "1.6.2"
            
            # Should load profiles
            dev_profile = source.get_profile("dev")
            assert dev_profile["terraform"] == "1.6.0"
            assert dev_profile["tofu"] == "1.7.0"
            
            # Should load settings
            assert source.get_setting("verify_checksums") is True
            assert source.get_setting("install_path") == "~/.wrkenv/tools"
    
    def test_environment_config_source(self):
        """
        CONTRACT: EnvironmentConfigSource should read from environment variables
        """
        with patch.dict('os.environ', {
            'WRKENV_TERRAFORM_VERSION': '1.7.0',
            'WRKENV_VERIFY_CHECKSUMS': 'true',
            'WRKENV_INSTALL_PATH': '/custom/path'
        }):
            source = EnvironmentConfigSource("WRKENV")
            
            # Should read tool versions
            assert source.get_tool_version("terraform") == "1.7.0"
            assert source.get_tool_version("tofu") is None
            
            # Should read settings with boolean parsing
            assert source.get_setting("verify_checksums") is True
            assert source.get_setting("install_path") == "/custom/path"
    
    def test_environment_boolean_parsing(self):
        """
        CONTRACT: Environment source should parse boolean values correctly
        """
        source = EnvironmentConfigSource("TEST")
        
        test_cases = [
            ("true", True), ("TRUE", True), ("1", True), ("yes", True), ("on", True),
            ("false", False), ("FALSE", False), ("0", False), ("no", False), ("off", False),
            ("something", "something"),  # Non-boolean returns as string
        ]
        
        for env_value, expected in test_cases:
            with patch.dict('os.environ', {'TEST_SETTING': env_value}):
                assert source.get_setting("setting") == expected


class TestWorkenvConfigIntegration:
    """TDD contracts for WorkenvConfig integration."""
    
    def test_default_configuration_sources(self):
        """
        CONTRACT: WorkenvConfig should have sensible defaults
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a wrkenv.toml to have multiple sources
            wrkenv_toml = pathlib.Path(tmpdir) / "wrkenv.toml"
            wrkenv_toml.write_text("""
[workenv.tools]
terraform = "1.5.0"
""")
            
            with patch('pathlib.Path.cwd', return_value=pathlib.Path(tmpdir)):
                config = WorkenvConfig()
                
                # Should have multiple sources (env + file)
                assert len(config.sources) >= 2
                
                # Should prioritize WRKENV_ env vars
                assert any(
                    isinstance(s, EnvironmentConfigSource) and s.prefix == "WRKENV"
                    for s in config.sources
                )
                
                # Should NOT have TOFUSOUP_WORKENV_ env vars
                assert not any(
                    isinstance(s, EnvironmentConfigSource) and s.prefix == "TOFUSOUP_WORKENV"
                    for s in config.sources
                )
    
    def test_config_priority_ordering(self):
        """
        CONTRACT: Configuration sources should be checked in priority order
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create config files
            wrkenv_toml = pathlib.Path(tmpdir) / "wrkenv.toml"
            wrkenv_toml.write_text("""
[workenv.tools]
terraform = "1.5.0"
tofu = "1.6.0"
""")
            
            # Set environment variables
            with patch.dict('os.environ', {
                'WRKENV_TERRAFORM_VERSION': '1.7.0',
                'WRKENV_GO_VERSION': '1.22.0'
            }):
                with patch('pathlib.Path.cwd', return_value=pathlib.Path(tmpdir)):
                    config = WorkenvConfig()
                    
                    # WRKENV_ env var should win for terraform
                    assert config.get_tool_version("terraform") == "1.7.0"
                    
                    # File config should be used for tofu (no env var)
                    assert config.get_tool_version("tofu") == "1.6.0"
                    
                    # WRKENV_ env var should win for go
                    assert config.get_tool_version("go") == "1.22.0"
    
    def test_custom_configuration_sources(self):
        """
        CONTRACT: WorkenvConfig should accept custom configuration sources
        """
        # Create mock sources
        source1 = Mock(spec=ConfigSource)
        source1.get_tool_version.side_effect = lambda t: "1.0.0" if t == "terraform" else None
        
        source2 = Mock(spec=ConfigSource)
        source2.get_tool_version.side_effect = lambda t: "2.0.0" if t == "terraform" else None
        
        # Source order matters - first source wins
        config = WorkenvConfig(sources=[source1, source2])
        
        assert config.get_tool_version("terraform") == "1.0.0"
        source1.get_tool_version.assert_called_with("terraform")
        source2.get_tool_version.assert_not_called()  # Should stop at first match
    
    def test_get_all_tools_merges_sources(self):
        """
        CONTRACT: get_all_tools should merge from all sources with proper priority
        """
        source1 = Mock(spec=ConfigSource)
        source1.get_all_tools.return_value = {"terraform": "1.7.0", "go": "1.21.0"}
        
        source2 = Mock(spec=ConfigSource)
        source2.get_all_tools.return_value = {"terraform": "1.6.0", "tofu": "1.8.0"}
        
        # First source should override second
        config = WorkenvConfig(sources=[source1, source2])
        tools = config.get_all_tools()
        
        assert tools == {
            "terraform": "1.7.0",  # From source1
            "go": "1.21.0",        # From source1
            "tofu": "1.8.0"        # From source2
        }



class TestPlatformSpecificBehavior:
    """TDD contracts for platform-specific behavior."""
    
    def test_workenv_dir_name_generation(self):
        """
        CONTRACT: Workenv directory names should be platform-specific
        """
        config = WorkenvConfig(sources=[])
        
        with patch('platform.system', return_value='Linux'):
            with patch('platform.machine', return_value='x86_64'):
                assert config.get_workenv_dir_name() == "workenv/wrkenv_linux_amd64"
        
        with patch('platform.system', return_value='Darwin'):
            with patch('platform.machine', return_value='arm64'):
                assert config.get_workenv_dir_name() == "workenv/wrkenv_darwin_arm64"
    
    def test_workenv_dir_with_profile(self):
        """
        CONTRACT: Workenv directory should include profile name if not default
        """
        source = Mock(spec=ConfigSource)
        source.get_setting.side_effect = lambda k, d=None: "development" if k == "current_profile" else d
        
        config = WorkenvConfig(sources=[source])
        
        with patch('platform.system', return_value='Linux'):
            with patch('platform.machine', return_value='x86_64'):
                assert config.get_workenv_dir_name() == "workenv/development_wrkenv_linux_amd64"


class TestVersionValidation:
    """TDD contracts for version validation."""
    
    def test_validate_version_patterns(self):
        """
        CONTRACT: Version validation should accept common version formats
        """
        config = WorkenvConfig(sources=[])
        
        # Valid versions
        assert config.validate_version("terraform", "1.5.7") is True
        assert config.validate_version("terraform", "1.5.7-alpha1") is True
        assert config.validate_version("terraform", "2.0.0-beta.1") is True
        assert config.validate_version("terraform", "1.5.7+metadata") is True
        assert config.validate_version("terraform", "latest") is True
        
        # Invalid versions
        assert config.validate_version("terraform", "") is False
        assert config.validate_version("terraform", "invalid") is False
        assert config.validate_version("terraform", "v1.5.7") is False  # No 'v' prefix


if __name__ == "__main__":
    # Run TDD tests
    pytest.main([__file__, "-v", "--tb=short"])


# 🧰🌍🖥️🪄