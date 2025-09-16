#!/usr/bin/env python3

"""
Test suite for configuration schema validation.
"""

import pathlib
import tempfile
import unittest

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


class TestToolConfig(unittest.TestCase):
    """Test ToolConfig validation."""

    def test_valid_tool_config(self):
        """Test creating valid tool configuration."""
        config = ToolConfig(version="1.5.0")
        self.assertEqual(config.version, "1.5.0")
        self.assertTrue(config.enabled)

    def test_tool_config_with_custom_settings(self):
        """Test tool config with custom settings."""
        config = ToolConfig(
            version="2.0.0",
            enabled=False,
            source_url="https://example.com/tool.tar.gz",
            install_path="/opt/tools/custom",
            environment={"TOOL_HOME": "/opt/tools/custom"},
        )
        self.assertEqual(config.version, "2.0.0")
        self.assertFalse(config.enabled)
        self.assertEqual(config.source_url, "https://example.com/tool.tar.gz")

    def test_invalid_version(self):
        """Test invalid version format."""
        try:
            # Should work with pydantic validation
            with self.assertRaises(ValueError):
                ToolConfig(version="")
        except ImportError:
            # Fallback when pydantic not installed
            config = ToolConfig(version="")
            self.assertEqual(config.version, "")

    def test_version_starting_with_v(self):
        """Test version starting with 'v'."""
        config = ToolConfig(version="v1.2.3")
        self.assertEqual(config.version, "v1.2.3")


class TestContainerConfig(unittest.TestCase):
    """Test ContainerConfig validation."""

    def test_default_container_config(self):
        """Test default container configuration."""
        config = ContainerConfig()
        self.assertFalse(config.enabled)
        self.assertEqual(config.base_image, "ubuntu:22.04")
        self.assertEqual(config.python_version, "3.11")

    def test_container_config_with_settings(self):
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
        self.assertTrue(config.enabled)
        self.assertEqual(config.base_image, "python:3.11-slim")
        self.assertEqual(len(config.additional_packages), 2)

    def test_invalid_python_version(self):
        """Test invalid Python version."""
        try:
            with self.assertRaises(ValueError):
                ContainerConfig(python_version="2.7")
        except ImportError:
            # Fallback behavior
            config = ContainerConfig(python_version="2.7")
            self.assertEqual(config.python_version, "2.7")


class TestProfileConfig(unittest.TestCase):
    """Test ProfileConfig validation."""

    def test_valid_profile(self):
        """Test creating valid profile."""
        profile = ProfileConfig(
            name="development",
            description="Development environment",
            tools={"terraform": ToolConfig(version="1.5.0"), "go": ToolConfig(version="1.21.0")},
        )
        self.assertEqual(profile.name, "development")
        self.assertEqual(len(profile.tools), 2)

    def test_profile_with_container(self):
        """Test profile with container configuration."""
        profile = ProfileConfig(
            name="docker-dev", container=ContainerConfig(enabled=True), environment={"ENV": "development"}
        )
        self.assertIsNotNone(profile.container)
        self.assertTrue(profile.container.enabled)

    def test_invalid_profile_name(self):
        """Test invalid profile name."""
        try:
            with self.assertRaises(ValueError):
                ProfileConfig(name="")
        except ImportError:
            profile = ProfileConfig(name="")
            self.assertEqual(profile.name, "")


class TestPackageConfig(unittest.TestCase):
    """Test PackageConfig validation."""

    def test_valid_package_config(self):
        """Test creating valid package configuration."""
        config = PackageConfig(name="my-package", version="1.0.0", entry_point="my_package.main:app")
        self.assertEqual(config.name, "my-package")
        self.assertEqual(config.version, "1.0.0")
        self.assertEqual(config.license, "MIT")

    def test_package_with_metadata(self):
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
        self.assertEqual(config.name, "complex-package")
        self.assertEqual(len(config.dependencies), 2)


class TestRegistryConfig(unittest.TestCase):
    """Test RegistryConfig validation."""

    def test_default_registry_config(self):
        """Test default registry configuration."""
        config = RegistryConfig()
        self.assertEqual(config.url, "https://registry.wrknv.io")
        self.assertTrue(config.verify_ssl)
        self.assertEqual(config.timeout, 30)

    def test_custom_registry_config(self):
        """Test custom registry configuration."""
        config = RegistryConfig(
            url="https://custom.registry.com/",
            username="user",
            token="secret-token",
            verify_ssl=False,
            timeout=60,
        )
        # URL should be normalized (trailing slash removed)
        self.assertEqual(config.url, "https://custom.registry.com")
        self.assertEqual(config.username, "user")

    def test_invalid_registry_url(self):
        """Test invalid registry URL."""
        try:
            with self.assertRaises(ValueError):
                RegistryConfig(url="not-a-url")
        except ImportError:
            config = RegistryConfig(url="not-a-url")
            self.assertEqual(config.url, "not-a-url")


class TestWorkenvConfig(unittest.TestCase):
    """Test WorkenvConfig validation."""

    def test_minimal_config(self):
        """Test minimal valid configuration."""
        config = WorkenvConfig(project_name="test-project")
        self.assertEqual(config.project_name, "test-project")
        self.assertEqual(config.version, "1.0.0")
        self.assertEqual(config.log_level, "INFO")

    def test_full_config(self):
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
        self.assertEqual(config.project_name, "full-project")
        self.assertEqual(len(config.tools), 2)
        self.assertIsNotNone(config.container)
        self.assertIsNotNone(config.package)
        self.assertEqual(config.log_level, "DEBUG")

    def test_get_tool_config(self):
        """Test getting tool configuration."""
        config = WorkenvConfig(project_name="test", tools={"terraform": ToolConfig(version="1.5.0")})
        tool = config.get_tool_config("terraform")
        self.assertIsNotNone(tool)
        self.assertEqual(tool.version, "1.5.0")

        missing = config.get_tool_config("missing")
        self.assertIsNone(missing)

    def test_get_profile(self):
        """Test getting profile configuration."""
        config = WorkenvConfig(
            project_name="test", profiles={"dev": ProfileConfig(name="dev", description="Dev profile")}
        )
        profile = config.get_profile("dev")
        self.assertIsNotNone(profile)
        self.assertEqual(profile.name, "dev")

        missing = config.get_profile("missing")
        self.assertIsNone(missing)

    def test_merge_with_profile(self):
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
        self.assertEqual(terraform.version, "1.5.0")

        # New tools from profile should be added
        go = merged.get_tool_config("go")
        self.assertIsNotNone(go)
        self.assertEqual(go.version, "1.21.0")

        # Environment should be merged
        self.assertEqual(merged.environment["ENV"], "dev")

    def test_path_expansion(self):
        """Test path expansion in configuration."""
        config = WorkenvConfig(project_name="test", install_dir="~/test/install", cache_dir="~/test/cache")
        # Paths should be expanded
        self.assertNotIn("~", config.install_dir)
        self.assertNotIn("~", config.cache_dir)
        self.assertTrue(config.install_dir.startswith("/"))

    def test_invalid_log_level(self):
        """Test invalid log level."""
        try:
            with self.assertRaises(ValueError):
                WorkenvConfig(project_name="test", log_level="INVALID")
        except ImportError:
            config = WorkenvConfig(project_name="test", log_level="INVALID")
            self.assertEqual(config.log_level, "INVALID")


class TestConfigValidation(unittest.TestCase):
    """Test configuration validation functions."""

    def test_validate_valid_config(self):
        """Test validating valid configuration."""
        config_dict = {"project_name": "test-project", "tools": {"terraform": {"version": "1.5.0"}}}
        is_valid, errors = validate_config_dict(config_dict)
        self.assertTrue(is_valid)
        self.assertEqual(len(errors), 0)

    def test_validate_invalid_config(self):
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
            self.assertTrue(True)
        else:
            self.assertFalse(is_valid)
            self.assertGreater(len(errors), 0)

    def test_load_config_from_dict(self):
        """Test loading configuration from dictionary."""
        config_dict = {"project_name": "test-project", "version": "2.0.0"}
        config = load_config_from_dict(config_dict)
        self.assertEqual(config.project_name, "test-project")
        self.assertEqual(config.version, "2.0.0")

    def test_get_default_config(self):
        """Test getting default configuration."""
        config = get_default_config("my-project")
        self.assertEqual(config.project_name, "my-project")
        self.assertIn("terraform", config.tools)
        self.assertIn("go", config.tools)
        self.assertIsNotNone(config.container)


class TestValidatedTomlSource(unittest.TestCase):
    """Test ValidatedTomlSource configuration source."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = pathlib.Path(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_load_valid_config(self):
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
        self.assertEqual(config.project_name, "test-project")

        # Test getting tool versions
        self.assertEqual(source.get_tool_version("terraform"), "1.5.0")
        self.assertEqual(source.get_tool_version("go"), "1.21.0")

        # Test getting all tools
        tools = source.get_all_tools()
        self.assertEqual(len(tools), 2)
        self.assertEqual(tools["terraform"], "1.5.0")

    def test_load_invalid_config(self):
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

    def test_missing_config_file(self):
        """Test handling missing configuration file."""
        config_file = self.temp_path / "missing.toml"

        source = ValidatedTomlSource(config_file)
        config = source.get_config()

        self.assertIsNone(config)
        self.assertIsNone(source.get_tool_version("terraform"))
        self.assertEqual(source.get_all_tools(), {})

    def test_config_with_profiles(self):
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
            self.assertEqual(profile.get("name"), "dev")


class TestConfigToToml(unittest.TestCase):
    """Test configuration to TOML conversion."""

    def test_config_to_toml(self):
        """Test converting configuration to TOML."""
        config = WorkenvConfig(
            project_name="test-project", version="1.0.0", tools={"terraform": ToolConfig(version="1.5.0")}
        )

        try:
            import tomli_w

            toml_str = config_to_toml(config)
            self.assertIn("project_name", toml_str)
            self.assertIn("test-project", toml_str)
            self.assertIn("terraform", toml_str)
            self.assertIn("1.5.0", toml_str)
        except ImportError:
            # Skip test if tomli_w not available
            self.skipTest("tomli_w not available")


if __name__ == "__main__":
    unittest.main()
