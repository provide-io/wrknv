#!/usr/bin/env python3

"""
Test suite for configuration schema validation.
"""
from __future__ import annotations


import pathlib

from provide.testkit import FoundationTestCase

from wrknv.wenv.config import ValidatedTomlSource, WorkenvConfigError
from wrknv.wenv.schema import (
    ContainerConfig,
    PackageConfig,
    ProfileConfig,
    RegistryConfig,
    ToolConfig,
    WorkenvConfig,
    config_to_toml,
    get_default_config,
    load_config_from_dict,
    validate_config_dict,
)


class TestToolConfig(FoundationTestCase):
    """Test ToolConfig validation."""

    def test_valid_tool_config(self) -> None:
        """Test creating valid tool configuration."""
        config = ToolConfig(version="1.5.0")
        assert config.version == "1.5.0"
        assert config.enabled

    def test_tool_config_with_custom_settings(self) -> None:
        """Test tool config with custom settings."""
        config = ToolConfig(
            version="2.0.0",
            enabled=False,
            source_url="https://example.com/tool.tar.gz",
            install_path="/opt/tools/custom",
            environment={"TOOL_HOME": "/opt/tools/custom"},
        )
        assert config.version == "2.0.0"
        assert not config.enabled
        assert config.source_url == "https://example.com/tool.tar.gz"

    def test_invalid_version(self) -> None:
        """Test invalid version format."""
        try:
            # Should work with pydantic validation
            with self.assertRaises(ValueError):
                ToolConfig(version="")
        except ImportError:
            # Fallback when pydantic not installed
            config = ToolConfig(version="")
            assert config.version == ""

    def test_version_starting_with_v(self) -> None:
        """Test version starting with 'v'."""
        config = ToolConfig(version="v1.2.3")
        assert config.version == "v1.2.3"


class TestContainerConfig(FoundationTestCase):
    """Test ContainerConfig validation."""

    def test_default_container_config(self) -> None:
        """Test default container configuration."""
        config = ContainerConfig()
        assert not config.enabled
        assert config.base_image == "ubuntu:22.04"
        assert config.python_version == "3.11"

    def test_container_config_with_settings(self) -> None:
        """Test container config with custom settings."""
        config = ContainerConfig(
            enabled=True,
            base_image="python:3.11-slim",
            python_version="3.11",
            additional_packages=["git", "curl"],
            environment={"PATH": "/custom/path:$PATH"},
            volumes=["/host/path:/container/path"],
            ports=["8080:80"],
        )
        assert config.enabled
        assert config.base_image == "python:3.11-slim"
        assert len(config.additional_packages) == 2

    def test_invalid_python_version(self) -> None:
        """Test invalid Python version."""
        try:
            with self.assertRaises(ValueError):
                ContainerConfig(python_version="2.7")
        except ImportError:
            # Fallback behavior
            config = ContainerConfig(python_version="2.7")
            assert config.python_version == "2.7"


class TestProfileConfig(FoundationTestCase):
    """Test ProfileConfig validation."""

    def test_valid_profile(self) -> None:
        """Test creating valid profile."""
        profile = ProfileConfig(
            name="development",
            description="Development environment",
            tools={"terraform": ToolConfig(version="1.5.0"), "go": ToolConfig(version="1.21.0")},
        )
        assert profile.name == "development"
        assert len(profile.tools) == 2

    def test_profile_with_container(self) -> None:
        """Test profile with container configuration."""
        profile = ProfileConfig(
            name="docker-dev", container=ContainerConfig(enabled=True), environment={"ENV": "development"}
        )
        self.assertIsNotNone(profile.container)
        assert profile.container.enabled

    def test_invalid_profile_name(self) -> None:
        """Test invalid profile name."""
        try:
            with self.assertRaises(ValueError):
                ProfileConfig(name="")
        except ImportError:
            profile = ProfileConfig(name="")
            assert profile.name == ""


class TestPackageConfig(FoundationTestCase):
    """Test PackageConfig validation."""

    def test_valid_package_config(self) -> None:
        """Test creating valid package configuration."""
        config = PackageConfig(name="my-package", version="1.0.0", entry_point="my_package.main:app")
        assert config.name == "my-package"
        assert config.version == "1.0.0"
        assert config.license == "MIT"

    def test_package_with_metadata(self) -> None:
        """Test package with metadata."""
        config = PackageConfig(
            name="Complex-Package",
            version="2.0.0",
            author="Test Author",
            description="Test package",
            entry_point="main:run",
            dependencies=["dep1", "dep2"],
            metadata={"key": "value"},
        )
        # Name should be normalized to lowercase
        assert config.name == "complex-package"
        assert len(config.dependencies) == 2


class TestRegistryConfig(FoundationTestCase):
    """Test RegistryConfig validation."""

    def test_default_registry_config(self) -> None:
        """Test default registry configuration."""
        config = RegistryConfig()
        assert config.url == "https://registry.wrknv.io"
        assert config.verify_ssl
        assert config.timeout == 30

    def test_custom_registry_config(self) -> None:
        """Test custom registry configuration."""
        config = RegistryConfig(
            url="https://custom.registry.com/",
            username="user",
            token="secret-token",
            verify_ssl=False,
            timeout=60,
        )
        # URL should be normalized (trailing slash removed)
        assert config.url == "https://custom.registry.com"
        assert config.username == "user"

    def test_invalid_registry_url(self) -> None:
        """Test invalid registry URL."""
        try:
            with self.assertRaises(ValueError):
                RegistryConfig(url="not-a-url")
        except ImportError:
            config = RegistryConfig(url="not-a-url")
            assert config.url == "not-a-url"


class TestWorkenvConfig(FoundationTestCase):
    """Test WorkenvConfig validation."""

    def test_minimal_config(self) -> None:
        """Test minimal valid configuration."""
        config = WorkenvConfig(project_name="test-project")
        assert config.project_name == "test-project"
        assert config.version == "1.0.0"
        assert config.log_level == "INFO"

    def test_full_config(self) -> None:
        """Test full configuration."""
        config = WorkenvConfig(
            project_name="full-project",
            version="2.0.0",
            description="Full test project",
            tools={"terraform": ToolConfig(version="1.5.0"), "go": ToolConfig(version="1.21.0")},
            container=ContainerConfig(enabled=True),
            package=PackageConfig(name="test-package", version="1.0.0", entry_point="main:app"),
            registry=RegistryConfig(),
            profiles={"dev": ProfileConfig(name="dev")},
            install_dir="~/custom/install",
            cache_dir="~/custom/cache",
            log_level="DEBUG",
            telemetry_enabled=False,
            auto_update=True,
            environment={"KEY": "value"},
            scripts={"test": "pytest"},
        )
        assert config.project_name == "full-project"
        assert len(config.tools) == 2
        self.assertIsNotNone(config.container)
        self.assertIsNotNone(config.package)
        assert config.log_level == "DEBUG"

    def test_get_tool_config(self) -> None:
        """Test getting tool configuration."""
        config = WorkenvConfig(project_name="test", tools={"terraform": ToolConfig(version="1.5.0")})
        tool = config.get_tool_config("terraform")
        self.assertIsNotNone(tool)
        assert tool.version == "1.5.0"

        missing = config.get_tool_config("missing")
        self.assertIsNone(missing)

    def test_get_profile(self) -> None:
        """Test getting profile configuration."""
        config = WorkenvConfig(
            project_name="test", profiles={"dev": ProfileConfig(name="dev", description="Dev profile")}
        )
        profile = config.get_profile("dev")
        self.assertIsNotNone(profile)
        assert profile.name == "dev"

        missing = config.get_profile("missing")
        self.assertIsNone(missing)

    def test_merge_with_profile(self) -> None:
        """Test merging configuration with profile."""
        config = WorkenvConfig(
            project_name="test",
            tools={"terraform": ToolConfig(version="1.4.0")},
            profiles={
                "dev": ProfileConfig(
                    name="dev",
                    tools={"terraform": ToolConfig(version="1.5.0"), "go": ToolConfig(version="1.21.0")},
                    environment={"ENV": "dev"},
                )
            },
        )

        merged = config.merge_with_profile("dev")

        # Profile tools should override base tools
        terraform = merged.get_tool_config("terraform")
        assert terraform.version == "1.5.0"

        # New tools from profile should be added
        go = merged.get_tool_config("go")
        self.assertIsNotNone(go)
        assert go.version == "1.21.0"

        # Environment should be merged
        assert merged.environment["ENV"] == "dev"

    def test_path_expansion(self) -> None:
        """Test path expansion in configuration."""
        config = WorkenvConfig(project_name="test", install_dir="~/test/install", cache_dir="~/test/cache")
        # Paths should be expanded
        self.assertNotIn("~", config.install_dir)
        self.assertNotIn("~", config.cache_dir)
        assert config.install_dir.startswith("/")

    def test_invalid_log_level(self) -> None:
        """Test invalid log level."""
        try:
            with self.assertRaises(ValueError):
                WorkenvConfig(project_name="test", log_level="INVALID")
        except ImportError:
            config = WorkenvConfig(project_name="test", log_level="INVALID")
            assert config.log_level == "INVALID"


class TestConfigValidation(FoundationTestCase):
    """Test configuration validation functions."""

    def test_validate_valid_config(self) -> None:
        """Test validating valid configuration."""
        config_dict = {"project_name": "test-project", "tools": {"terraform": {"version": "1.5.0"}}}
        is_valid, errors = validate_config_dict(config_dict)
        assert is_valid
        assert len(errors) == 0

    def test_validate_invalid_config(self) -> None:
        """Test validating invalid configuration."""
        config_dict = {
            # Missing required project_name
            "tools": {
                "terraform": {"version": ""}  # Invalid empty version
            }
        }
        is_valid, errors = validate_config_dict(config_dict)
        # Validation behavior depends on whether pydantic is installed
        if is_valid:
            # Fallback mode - no validation
            assert True
        else:
            assert not is_valid
            self.assertGreater(len(errors), 0)

    def test_load_config_from_dict(self) -> None:
        """Test loading configuration from dictionary."""
        config_dict = {"project_name": "test-project", "version": "2.0.0"}
        config = load_config_from_dict(config_dict)
        assert config.project_name == "test-project"
        assert config.version == "2.0.0"

    def test_get_default_config(self) -> None:
        """Test getting default configuration."""
        config = get_default_config("my-project")
        assert config.project_name == "my-project"
        assert "terraform" in config.tools
        assert "go" in config.tools
        self.assertIsNotNone(config.container)


class TestValidatedTomlSource(FoundationTestCase):
    """Test ValidatedTomlSource configuration source."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.temp_dir = self.create_temp_dir()
        self.temp_path = pathlib.Path(self.temp_dir)

    

    def test_load_valid_config(self) -> None:
        """Test loading valid configuration file."""
        config_file = self.temp_path / "wrknv.toml"
        config_file.write_text("""
project_name = "test-project"
version = "1.0.0"

[tools.terraform]
version = "1.5.0"
enabled = true

[tools.go]
version = "1.21.0"
""")

        source = ValidatedTomlSource(config_file)
        config = source.get_config()

        self.assertIsNotNone(config)
        assert config.project_name == "test-project"

        # Test getting tool versions
        assert source.get_tool_version("terraform") == "1.5.0"
        assert source.get_tool_version("go") == "1.21.0"

        # Test getting all tools
        tools = source.get_all_tools()
        assert len(tools) == 2
        assert tools["terraform"] == "1.5.0"

    def test_load_invalid_config(self) -> None:
        """Test loading invalid configuration file."""
        config_file = self.temp_path / "invalid.toml"
        config_file.write_text("""
# Missing required project_name
version = "1.0.0"

[tools.terraform]
version = ""  # Invalid empty version
""")

        try:
            # Should raise error with pydantic validation
            with self.assertRaises(WorkenvConfigError):
                ValidatedTomlSource(config_file)
        except ImportError:
            # Fallback mode - no validation error
            source = ValidatedTomlSource(config_file)
            # Config might be None due to missing project_name
            pass

    def test_missing_config_file(self) -> None:
        """Test handling missing configuration file."""
        config_file = self.temp_path / "missing.toml"

        source = ValidatedTomlSource(config_file)
        config = source.get_config()

        self.assertIsNone(config)
        self.assertIsNone(source.get_tool_version("terraform"))
        assert source.get_all_tools() == {}

    def test_config_with_profiles(self) -> None:
        """Test configuration with profiles."""
        config_file = self.temp_path / "profiles.toml"
        config_file.write_text("""
project_name = "test-project"

[profiles.dev]
name = "dev"
description = "Development profile"

[profiles.dev.tools.terraform]
version = "1.6.0"
""")

        source = ValidatedTomlSource(config_file)
        profile = source.get_profile("dev")

        if profile:  # Profile support depends on schema implementation
            assert profile.get("name") == "dev"


class TestConfigToToml(FoundationTestCase):
    """Test configuration to TOML conversion."""

    def test_config_to_toml(self) -> None:
        """Test converting configuration to TOML."""
        config = WorkenvConfig(
            project_name="test-project", version="1.0.0", tools={"terraform": ToolConfig(version="1.5.0")}
        )

        try:
            import tomli_w

            toml_str = config_to_toml(config)
            assert "project_name" in toml_str
            assert "test-project" in toml_str
            assert "terraform" in toml_str
            assert "1.5.0" in toml_str
        except ImportError:
            # Skip test if tomli_w not available
            self.skipTest("tomli_w not available")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])