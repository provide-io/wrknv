"""
TDD Tests for soup.toml Workenv Integration
===========================================
Tests that define how workenv should integrate with the existing soup.toml configuration.
"""

import pytest
import tempfile
import pathlib
from unittest.mock import Mock, patch

# TDD imports - will fail initially
try:
    from wrkenv.env.config import WorkenvConfig
    from tofusoup.common.config import load_tofusoup_config
except ImportError:
    WorkenvConfig = Mock
    load_tofusoup_config = Mock


class TestSoupTomlWorkenvIntegration:
    """Test workenv integration with existing soup.toml structure."""
    
    def test_workenv_extends_existing_soup_toml_structure(self):
        """
        TDD: Workenv should extend soup.toml without breaking existing structure
        """
        soup_toml_content = """
# Existing TofuSoup configuration
[global_settings]
default_python_log_level = "INFO"
default_harness_log_level = "INFO"

[harness_defaults.go]
build_flags = ["-v"]

# NEW: Workenv configuration section
[workenv.tools]
terraform = "1.5.7"
tofu = "1.6.2"
go = "1.21.5"
uv = "0.4.15"

[workenv.profiles.dev]
terraform = "1.5.7"
tofu = "1.6.2"

[workenv.profiles.conformance]
terraform = ["1.5.7", "1.6.0"]  # Multiple versions for matrix testing
tofu = ["1.6.2", "1.7.0"]

[workenv.settings]
verify_checksums = true
cache_downloads = true
install_path = "~/.tofusoup/tools"
auto_install_deps = true

[workenv.matrix_testing]
parallel_jobs = 4
timeout_minutes = 30
"""
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = pathlib.Path(tmpdir) / "soup.toml"
            config_path.write_text(soup_toml_content)
            
            # Should load both TofuSoup and workenv config
            config = WorkenvConfig(config_path)
            
            # TofuSoup config should still work
            assert config.get_setting("default_python_log_level") == "INFO"
            
            # Workenv config should work
            assert config.get_tool_version("terraform") == "1.5.7"
            assert config.get_tool_version("tofu") == "1.6.2"
            
            # Profile config should work
            dev_profile = config.get_profile("dev")
            assert dev_profile["terraform"] == "1.5.7"
            assert dev_profile["tofu"] == "1.6.2"
            
            # Matrix testing config should work
            conformance_profile = config.get_profile("conformance")
            assert "1.5.7" in conformance_profile["terraform"]
            assert "1.6.0" in conformance_profile["terraform"]
    
    def test_workenv_environment_variable_support(self):
        """
        TDD: Workenv should support TOFUSOUP_WORKENV_* environment variables
        """
        with patch.dict('os.environ', {
            'TOFUSOUP_WORKENV_TERRAFORM_VERSION': '1.6.0',
            'TOFUSOUP_WORKENV_VERIFY_CHECKSUMS': 'false',
            'TOFUSOUP_WORKENV_INSTALL_PATH': '/custom/path'
        }):
            config = WorkenvConfig()
            
            # Environment variables should override file config
            assert config.get_tool_version("terraform") == "1.6.0"
            assert config.get_setting("verify_checksums") is False
            assert config.get_setting("install_path") == "/custom/path"
    
    def test_workenv_harness_tool_requirements_integration(self):
        """
        TDD: Workenv should integrate with harness tool requirements
        """
        soup_toml_content = """
[harness.go.cty]
required_tools = { go = "1.21.5", terraform = "1.5.7" }

[harness.go.rpc]  
required_tools = { go = "1.21.5" }

[workenv.tools]
go = "1.21.5"
terraform = "1.5.7"
"""
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = pathlib.Path(tmpdir) / "soup.toml"
            config_path.write_text(soup_toml_content)
            
            config = WorkenvConfig(config_path)
            
            # Should be able to get harness requirements
            cty_requirements = config.get_harness_requirements("go.cty")
            assert cty_requirements["go"] == "1.21.5"
            assert cty_requirements["terraform"] == "1.5.7"
            
            # Should verify all requirements are met
            assert config.verify_harness_requirements("go.cty") is True


class TestWorkenvConfigDefaults:
    """Test workenv configuration defaults and validation."""
    
    def test_workenv_config_defaults(self):
        """
        TDD: Workenv should provide sensible defaults when no config exists
        """
        config = WorkenvConfig()
        
        # Should have sensible defaults
        assert config.get_setting("verify_checksums") is True
        assert config.get_setting("cache_downloads") is True
        assert config.get_setting("auto_install_deps") is False
        assert config.get_setting("parallel_jobs") == 1
        assert config.get_setting("timeout_minutes") == 10
    
    def test_workenv_config_validation(self):
        """
        TDD: Workenv should validate configuration values
        """
        config = WorkenvConfig()
        
        # Valid tool versions
        assert config.validate_tool_version("terraform", "1.5.7") is True
        assert config.validate_tool_version("terraform", "latest") is True
        
        # Invalid tool versions
        assert config.validate_tool_version("terraform", "invalid") is False
        assert config.validate_tool_version("terraform", "") is False
        
        # Valid settings
        assert config.validate_setting("parallel_jobs", 4) is True
        assert config.validate_setting("verify_checksums", True) is True
        
        # Invalid settings
        assert config.validate_setting("parallel_jobs", -1) is False
        assert config.validate_setting("parallel_jobs", "invalid") is False


class TestWorkenvTofuSoupHarmonization:
    """Test how workenv harmonizes with TofuSoup patterns."""
    
    def test_workenv_uses_tofusoup_logging_patterns(self):
        """
        TDD: Workenv should use TofuSoup's logging patterns and configuration
        """
        soup_toml_content = """
[global_settings]
default_python_log_level = "DEBUG"

[workenv.settings]
log_tool_installations = true
"""
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = pathlib.Path(tmpdir) / "soup.toml"
            config_path.write_text(soup_toml_content)
            
            config = WorkenvConfig(config_path)
            
            # Should respect TofuSoup logging level
            assert config.get_setting("default_python_log_level") == "DEBUG"
            
            # Should have workenv-specific logging settings
            assert config.get_setting("log_tool_installations") is True
    
    def test_workenv_respects_tofusoup_timeout_patterns(self):
        """
        TDD: Workenv should respect TofuSoup's timeout patterns
        """
        soup_toml_content = """
[global_settings]
default_harness_timeout = 120

[workenv.settings]
download_timeout = 300
install_timeout = 600
"""
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = pathlib.Path(tmpdir) / "soup.toml"
            config_path.write_text(soup_toml_content)
            
            config = WorkenvConfig(config_path)
            
            # Should have appropriate timeouts
            assert config.get_setting("download_timeout") == 300
            assert config.get_setting("install_timeout") == 600
            assert config.get_setting("default_harness_timeout") == 120


class TestWorkenvCommandOptionsIntegration:
    """Test workenv integration with TofuSoup command options pattern."""
    
    def test_workenv_command_options_structure(self):
        """
        TDD: Workenv should follow TofuSoup's command_options pattern
        """
        soup_toml_content = """
# Existing TofuSoup command options
[command_options.cty.convert]
default_input_format = "json"

# NEW: Workenv command options
[command_options.workenv.terraform]
default_install_path = "~/.tofusoup/tools/terraform"
verify_gpg = true

[command_options.workenv.tofu]
default_install_path = "~/.tofusoup/tools/tofu"  
verify_signatures = true

[command_options.workenv.matrix-test]
default_parallel_jobs = 2
default_timeout = "20m"
"""
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = pathlib.Path(tmpdir) / "soup.toml"
            config_path.write_text(soup_toml_content)
            
            config = WorkenvConfig(config_path)
            
            # Should get command-specific defaults
            assert config.get_command_option("workenv.terraform", "verify_gpg") is True
            assert config.get_command_option("workenv.tofu", "verify_signatures") is True
            assert config.get_command_option("workenv.matrix-test", "default_parallel_jobs") == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

# 🍲🥄🧪🪄
