"""
TDD Tests for pyvider-cty Integration in wrkenv
===============================================
Test-driven development for type-safe configuration.
"""

import pytest
from pathlib import Path
from click.testing import CliRunner

from wrkenv.env.cli import workenv_cli


class TestCtyConfigIntegration:
    """Test cty-based configuration system."""
    
    def test_config_supports_cty_types(self):
        """Configuration should support cty type validation."""
        from wrkenv.config.types import ToolConfigType
        from pyvider.cty import CtyObject, CtyString, CtyList, validate_value
        
        # Define expected schema
        expected_type = CtyObject({
            "version": CtyString(),
            "constraints": CtyObject({
                "min": CtyString(),
                "max": CtyString(),
            }, optional_attributes={"min", "max"}),
            "features": CtyList(CtyString()),
        }, optional_attributes={"constraints", "features"})
        
        # Should match the expected type
        assert ToolConfigType.terraform == expected_type
    
    def test_config_validates_with_cty(self, tmp_path):
        """Configuration loading should validate against cty types."""
        config_file = tmp_path / "wrkenv.toml"
        config_file.write_text("""
[workenv.tools]
terraform = { version = "1.5.7", constraints = { min = "1.5.0" } }
go = { version = "1.21.5" }

[workenv.tools.uv]
version = "0.4.15"
features = ["pip-compile", "workspace"]
        """)
        
        from wrkenv.config.loader import load_config_with_validation
        
        config = load_config_with_validation(config_file)
        
        # Should have validated types
        assert config.tools.terraform.version == "1.5.7"
        assert config.tools.terraform.constraints.min == "1.5.0"
        assert config.tools.uv.features == ["pip-compile", "workspace"]
    
    def test_config_validation_errors(self, tmp_path):
        """Invalid configuration should produce clear cty errors."""
        config_file = tmp_path / "wrkenv.toml"
        config_file.write_text("""
[workenv.tools]
terraform = { version = 123 }  # Should be string
go = { invalid_field = "test" }  # Unknown field
        """)
        
        from wrkenv.config.loader import load_config_with_validation
        from pyvider.cty.exceptions import CtyValidationError
        
        with pytest.raises(CtyValidationError) as exc_info:
            load_config_with_validation(config_file)
        
        error = str(exc_info.value)
        assert "version" in error
        assert "string" in error.lower()
    
    def test_config_schema_command(self):
        """Config schema command should show cty types."""
        runner = CliRunner()
        result = runner.invoke(workenv_cli, ["config", "schema"])
        
        assert result.exit_code == 0
        assert "CtyObject" in result.output
        assert "tools" in result.output
        assert "profiles" in result.output
    
    def test_config_validate_command(self, tmp_path):
        """Config validate command should check against schema."""
        config_file = tmp_path / "wrkenv.toml"
        config_file.write_text("""
[workenv.tools]
terraform = "1.5.7"
        """)
        
        runner = CliRunner()
        result = runner.invoke(
            workenv_cli, 
            ["config", "validate", "--file", str(config_file)]
        )
        
        assert result.exit_code == 0
        assert "valid" in result.output.lower()


class TestHclConfigSupport:
    """Test HCL configuration file support."""
    
    def test_hcl_config_loading(self, tmp_path):
        """Should support HCL configuration files."""
        config_file = tmp_path / "wrkenv.hcl"
        config_file.write_text("""
workenv {
  tools {
    terraform = {
      version = "1.5.7"
      constraints = {
        min = "1.5.0"
        max = "1.6.0"
      }
    }
    
    go = {
      version = "1.21.5"
    }
  }
  
  profiles {
    development = {
      tools = {
        terraform = { version = "1.5.7-dev" }
      }
    }
  }
}
        """)
        
        from wrkenv.config.loader import load_config
        
        config = load_config(config_file)
        
        assert config.get_tool_version("terraform") == "1.5.7"
        assert config.get_profile("development") is not None
    
    def test_hcl_config_with_functions(self, tmp_path):
        """HCL config should support built-in functions."""
        config_file = tmp_path / "wrkenv.hcl"
        config_file.write_text("""
locals {
  base_version = "1.5"
}

workenv {
  tools {
    terraform = {
      version = "${local.base_version}.7"
    }
  }
}
        """)
        
        from wrkenv.config.loader import load_config
        
        config = load_config(config_file)
        assert config.get_tool_version("terraform") == "1.5.7"
    
    def test_config_format_detection(self, tmp_path):
        """Should auto-detect config format (TOML vs HCL)."""
        # Test TOML
        toml_file = tmp_path / "wrkenv.toml"
        toml_file.write_text('[workenv.tools]\nterraform = "1.5.7"')
        
        # Test HCL
        hcl_file = tmp_path / "wrkenv.hcl"
        hcl_file.write_text('workenv { tools { terraform = "1.5.7" } }')
        
        from wrkenv.config.loader import load_config
        
        toml_config = load_config(toml_file)
        hcl_config = load_config(hcl_file)
        
        assert toml_config.get_tool_version("terraform") == "1.5.7"
        assert hcl_config.get_tool_version("terraform") == "1.5.7"


class TestProviderIntegration:
    """Test integration with provider development workflow."""
    
    def test_provider_config_schema(self):
        """Provider configurations should use cty types."""
        from wrkenv.provider.config import ProviderConfigType
        from pyvider.cty import CtyObject, CtyString, CtyBool
        
        expected = CtyObject({
            "name": CtyString(),
            "namespace": CtyString(),
            "version": CtyString(),
            "protocols": CtyList(CtyString()),
            "features": CtyObject({
                "mux": CtyBool(),
                "debug": CtyBool(),
            }, optional_attributes={"mux", "debug"}),
        })
        
        # Provider config should match expected schema
        assert ProviderConfigType == expected
    
    def test_provider_validation_in_package(self, tmp_path):
        """Package build should validate provider config with cty."""
        manifest = tmp_path / "pyproject.toml"
        manifest.write_text("""
[project]
name = "provider-example"
version = "1.0.0"

[tool.wrkenv.provider]
name = "example"
namespace = "custom"
protocols = ["6"]
features = { mux = true }
        """)
        
        runner = CliRunner()
        result = runner.invoke(
            workenv_cli,
            ["package", "build", "--manifest", str(manifest), "--validate-provider"]
        )
        
        # Should validate provider config
        assert "provider config: valid" in result.output.lower()


class TestAIAgentAPI:
    """Test API design for AI agent consumption."""
    
    def test_config_schema_export(self):
        """Should export config schema for AI agents."""
        from wrkenv.config.schema import export_schema
        
        schema = export_schema(format="json")
        
        # Should be machine-readable
        assert isinstance(schema, dict)
        assert "workenv" in schema
        assert "tools" in schema["workenv"]
        assert "type" in schema["workenv"]["tools"]
    
    def test_config_schema_openapi(self):
        """Should provide OpenAPI-compatible schema."""
        from wrkenv.config.schema import export_openapi_schema
        
        schema = export_openapi_schema()
        
        assert "components" in schema
        assert "schemas" in schema["components"]
        assert "WorkenvConfig" in schema["components"]["schemas"]
    
    def test_validation_error_structure(self, tmp_path):
        """Validation errors should be structured for AI parsing."""
        config_file = tmp_path / "wrkenv.toml"
        config_file.write_text("""
[workenv.tools]
terraform = { version = 123, invalid = true }
        """)
        
        from wrkenv.config.loader import load_config_with_validation
        from wrkenv.config.errors import ValidationError
        
        try:
            load_config_with_validation(config_file)
        except ValidationError as e:
            error_dict = e.to_dict()
            
            assert "errors" in error_dict
            assert len(error_dict["errors"]) > 0
            assert "path" in error_dict["errors"][0]
            assert "message" in error_dict["errors"][0]
            assert error_dict["errors"][0]["path"] == ["workenv", "tools", "terraform", "version"]


# 🧰🌍🖥️🪄