#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.schema - validators, converters, and basic dataclasses
===============================================================================
Covers: validate_*, convert_*, remove_none_values, ContainerConfig, ProfileConfig,
GitignoreConfig, ToolConfig, RegistryConfig, PackageConfig."""

from __future__ import annotations

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.schema import (
    ContainerConfig,
    GitignoreConfig,
    PackageConfig,
    ProfileConfig,
    RegistryConfig,
    ToolConfig,
    convert_log_level,
    convert_package_name,
    convert_registry_url,
    remove_none_values,
    validate_profile_name,
    validate_python_version,
    validate_timeout,
    validate_version,
    validate_volume_mapping,
    validate_volume_mappings,
)

# ---------------------------------------------------------------------------
# validate_version
# ---------------------------------------------------------------------------


class TestValidateVersion(FoundationTestCase):
    """Tests for validate_version validator."""

    def _call(self, value: str) -> None:
        validate_version(None, None, value)  # type: ignore[arg-type]

    def test_valid_numeric_version(self) -> None:
        self._call("1.5.0")  # no exception

    def test_valid_v_prefix_version(self) -> None:
        self._call("v1.5.0")  # no exception

    def test_empty_string_raises(self) -> None:
        with pytest.raises(ValueError, match="Version cannot be empty"):
            self._call("")

    def test_invalid_prefix_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid version format"):
            self._call("latest")

    def test_invalid_prefix_special_char_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid version format"):
            self._call("*1.0")


# ---------------------------------------------------------------------------
# validate_python_version
# ---------------------------------------------------------------------------


class TestValidatePythonVersion(FoundationTestCase):
    """Tests for validate_python_version validator."""

    def _call(self, value: str) -> None:
        validate_python_version(None, None, value)  # type: ignore[arg-type]

    def test_valid_major_minor(self) -> None:
        self._call("3.11")  # no exception

    def test_valid_major_minor_patch(self) -> None:
        self._call("3.12.1")  # no exception

    def test_only_major_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid Python version"):
            self._call("3")

    def test_too_old_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid Python version"):
            self._call("3.7")

    def test_python_2_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid Python version"):
            self._call("2.7")

    def test_non_numeric_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid Python version"):
            self._call("abc.def")

    def test_exactly_3_8_is_valid(self) -> None:
        self._call("3.8")  # no exception


# ---------------------------------------------------------------------------
# validate_profile_name
# ---------------------------------------------------------------------------


class TestValidateProfileName(FoundationTestCase):
    """Tests for validate_profile_name validator."""

    def _call(self, value: str) -> None:
        validate_profile_name(None, None, value)  # type: ignore[arg-type]

    def test_valid_name(self) -> None:
        self._call("dev")  # no exception

    def test_valid_name_with_hyphen(self) -> None:
        self._call("my-profile")  # no exception

    def test_valid_name_with_underscore(self) -> None:
        self._call("my_profile")  # no exception

    def test_empty_raises(self) -> None:
        with pytest.raises(ValueError, match="Profile name cannot be empty"):
            self._call("")

    def test_special_chars_raise(self) -> None:
        with pytest.raises(ValueError, match="Invalid profile name"):
            self._call("bad name!")


# ---------------------------------------------------------------------------
# convert_package_name
# ---------------------------------------------------------------------------


class TestConvertPackageName(FoundationTestCase):
    """Tests for convert_package_name converter."""

    def test_converts_to_lowercase(self) -> None:
        assert convert_package_name("MyPackage") == "mypackage"

    def test_valid_hyphenated_name(self) -> None:
        assert convert_package_name("my-pkg") == "my-pkg"

    def test_empty_raises(self) -> None:
        with pytest.raises(ValueError, match="Package name cannot be empty"):
            convert_package_name("")

    def test_invalid_chars_raise(self) -> None:
        with pytest.raises(ValueError, match="Invalid package name"):
            convert_package_name("bad pkg!")


# ---------------------------------------------------------------------------
# convert_registry_url
# ---------------------------------------------------------------------------


class TestConvertRegistryUrl(FoundationTestCase):
    """Tests for convert_registry_url converter."""

    def test_strips_trailing_slash(self) -> None:
        assert convert_registry_url("https://example.com/") == "https://example.com"

    def test_http_scheme_allowed(self) -> None:
        assert convert_registry_url("http://example.com") == "http://example.com"

    def test_no_trailing_slash_unchanged(self) -> None:
        assert convert_registry_url("https://example.com") == "https://example.com"

    def test_invalid_scheme_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid registry URL"):
            convert_registry_url("ftp://example.com")

    def test_plain_string_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid registry URL"):
            convert_registry_url("example.com")


# ---------------------------------------------------------------------------
# validate_timeout
# ---------------------------------------------------------------------------


class TestValidateTimeout(FoundationTestCase):
    """Tests for validate_timeout validator."""

    def _call(self, value: int) -> None:
        validate_timeout(None, None, value)  # type: ignore[arg-type]

    def test_valid_timeout(self) -> None:
        self._call(30)  # no exception

    def test_zero_raises(self) -> None:
        with pytest.raises(ValueError, match="Timeout must be positive"):
            self._call(0)

    def test_negative_raises(self) -> None:
        with pytest.raises(ValueError, match="Timeout must be positive"):
            self._call(-1)

    def test_exceeds_max_raises(self) -> None:
        with pytest.raises(ValueError, match="cannot exceed 5 minutes"):
            self._call(301)

    def test_exactly_300_is_valid(self) -> None:
        self._call(300)  # no exception


# ---------------------------------------------------------------------------
# validate_volume_mapping
# ---------------------------------------------------------------------------


class TestValidateVolumeMapping(FoundationTestCase):
    """Tests for validate_volume_mapping function."""

    def test_valid_host_container(self) -> None:
        assert validate_volume_mapping("/host:/container") is True

    def test_valid_with_ro_mode(self) -> None:
        assert validate_volume_mapping("/host:/container:ro") is True

    def test_valid_with_rw_mode(self) -> None:
        assert validate_volume_mapping("/host:/container:rw") is True

    def test_empty_string_returns_false(self) -> None:
        assert validate_volume_mapping("") is False

    def test_only_one_part_returns_false(self) -> None:
        assert validate_volume_mapping("/host") is False

    def test_four_parts_returns_false(self) -> None:
        assert validate_volume_mapping("/a:/b:ro:extra") is False

    def test_empty_host_returns_false(self) -> None:
        assert validate_volume_mapping(":/container") is False

    def test_empty_container_returns_false(self) -> None:
        assert validate_volume_mapping("/host:") is False

    def test_invalid_mode_returns_false(self) -> None:
        assert validate_volume_mapping("/host:/container:zz") is False


# ---------------------------------------------------------------------------
# validate_volume_mappings
# ---------------------------------------------------------------------------


class TestValidateVolumeMappings(FoundationTestCase):
    """Tests for validate_volume_mappings validator."""

    def _call(self, value: dict) -> None:  # type: ignore[type-arg]
        validate_volume_mappings(None, None, value)  # type: ignore[arg-type]

    def test_valid_mappings(self) -> None:
        self._call({"data": "/host:/container:ro"})  # no exception

    def test_empty_dict_is_valid(self) -> None:
        self._call({})  # no exception

    def test_invalid_mapping_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid volume mapping"):
            self._call({"bad": "/host"})


# ---------------------------------------------------------------------------
# convert_log_level
# ---------------------------------------------------------------------------


class TestConvertLogLevel(FoundationTestCase):
    """Tests for convert_log_level converter."""

    def test_converts_to_uppercase(self) -> None:
        assert convert_log_level("debug") == "DEBUG"

    def test_already_uppercase_unchanged(self) -> None:
        assert convert_log_level("INFO") == "INFO"

    def test_all_valid_levels(self) -> None:
        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            assert convert_log_level(level) == level

    def test_invalid_level_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid log level"):
            convert_log_level("VERBOSE")


# ---------------------------------------------------------------------------
# remove_none_values
# ---------------------------------------------------------------------------


class TestRemoveNoneValues(FoundationTestCase):
    """Tests for remove_none_values utility."""

    def test_removes_none_from_dict(self) -> None:
        result = remove_none_values({"a": 1, "b": None})
        assert result == {"a": 1}

    def test_removes_none_from_nested_dict(self) -> None:
        result = remove_none_values({"a": {"x": None, "y": 2}})
        assert result == {"a": {"y": 2}}

    def test_removes_none_from_list(self) -> None:
        # Lists: None items are NOT removed (only dict values are filtered)
        result = remove_none_values([1, None, 2])
        assert result == [1, None, 2]

    def test_scalar_passthrough(self) -> None:
        assert remove_none_values(42) == 42
        assert remove_none_values("hello") == "hello"

    def test_empty_dict(self) -> None:
        assert remove_none_values({}) == {}


# ---------------------------------------------------------------------------
# ContainerConfig
# ---------------------------------------------------------------------------


class TestContainerConfig(FoundationTestCase):
    """Tests for ContainerConfig."""

    def test_default_creation(self) -> None:
        cfg = ContainerConfig()
        assert cfg.enabled is False
        assert cfg.base_image == "ubuntu:22.04"
        assert cfg.python_version == "3.11"

    def test_to_dict_returns_dict(self) -> None:
        cfg = ContainerConfig()
        d = cfg.to_dict()
        assert isinstance(d, dict)
        assert "enabled" in d
        assert "base_image" in d

    def test_from_dict_roundtrip(self) -> None:
        original = ContainerConfig(enabled=True, base_image="debian:12")
        d = original.to_dict()
        restored = ContainerConfig.from_dict(d)
        assert restored.enabled is True
        assert restored.base_image == "debian:12"

    def test_invalid_python_version_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid Python version"):
            ContainerConfig(python_version="2.7")

    def test_valid_volume_mappings(self) -> None:
        cfg = ContainerConfig(volume_mappings={"data": "/host:/container:ro"})
        assert "data" in cfg.volume_mappings

    def test_invalid_volume_mappings_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid volume mapping"):
            ContainerConfig(volume_mappings={"bad": "notavalidmapping"})


# ---------------------------------------------------------------------------
# ProfileConfig
# ---------------------------------------------------------------------------


class TestProfileConfig(FoundationTestCase):
    """Tests for ProfileConfig."""

    def test_basic_creation(self) -> None:
        cfg = ProfileConfig(name="dev")
        assert cfg.name == "dev"
        assert cfg.description == ""
        assert cfg.tools == {}
        assert cfg.environment == {}

    def test_invalid_name_raises(self) -> None:
        with pytest.raises(ValueError, match="Profile name cannot be empty"):
            ProfileConfig(name="")

    def test_model_dump_returns_dict(self) -> None:
        cfg = ProfileConfig(name="staging")
        d = cfg.model_dump()
        assert isinstance(d, dict)
        assert d["name"] == "staging"

    def test_model_dump_with_tools(self) -> None:
        tool = ToolConfig(version="1.5.0")
        cfg = ProfileConfig(name="dev", tools={"terraform": tool})
        d = cfg.model_dump()
        assert "terraform" in d["tools"]


# ---------------------------------------------------------------------------
# GitignoreConfig
# ---------------------------------------------------------------------------


class TestGitignoreConfig(FoundationTestCase):
    """Tests for GitignoreConfig."""

    def test_defaults(self) -> None:
        cfg = GitignoreConfig()
        assert cfg.templates == []
        assert cfg.templates_path is None
        assert cfg.auto_detect is False
        assert cfg.custom_rules == []
        assert cfg.exclude_patterns == []

    def test_with_templates(self) -> None:
        cfg = GitignoreConfig(templates=["python", "node"])
        assert cfg.templates == ["python", "node"]


# ---------------------------------------------------------------------------
# ToolConfig
# ---------------------------------------------------------------------------


class TestToolConfig(FoundationTestCase):
    """Tests for ToolConfig."""

    def test_basic_creation(self) -> None:
        cfg = ToolConfig(version="1.5.0")
        assert cfg.version == "1.5.0"
        assert cfg.enabled is True
        assert cfg.environment == {}

    def test_disabled_tool(self) -> None:
        cfg = ToolConfig(version="1.6.0", enabled=False)
        assert cfg.enabled is False

    def test_invalid_version_raises(self) -> None:
        with pytest.raises(ValueError, match="Version cannot be empty"):
            ToolConfig(version="")

    def test_invalid_version_format_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid version format"):
            ToolConfig(version="latest")


# ---------------------------------------------------------------------------
# RegistryConfig
# ---------------------------------------------------------------------------


class TestRegistryConfig(FoundationTestCase):
    """Tests for RegistryConfig."""

    def test_defaults(self) -> None:
        cfg = RegistryConfig()
        assert cfg.verify_ssl is True
        assert cfg.timeout == 30
        assert cfg.username is None
        assert cfg.token is None

    def test_url_trailing_slash_stripped(self) -> None:
        cfg = RegistryConfig(url="https://my.registry.io/")
        assert not cfg.url.endswith("/")

    def test_invalid_url_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid registry URL"):
            RegistryConfig(url="notaurl")

    def test_invalid_timeout_raises(self) -> None:
        with pytest.raises(ValueError, match="Timeout must be positive"):
            RegistryConfig(timeout=0)


# ---------------------------------------------------------------------------
# PackageConfig
# ---------------------------------------------------------------------------


class TestPackageConfig(FoundationTestCase):
    """Tests for PackageConfig."""

    def test_basic_creation(self) -> None:
        cfg = PackageConfig(name="MyPkg", version="1.0.0", entry_point="mypkg.cli:main")
        assert cfg.name == "mypkg"  # lowercased by converter
        assert cfg.version == "1.0.0"

    def test_empty_name_raises(self) -> None:
        with pytest.raises(ValueError, match="Package name cannot be empty"):
            PackageConfig(name="", version="1.0.0", entry_point="mypkg.cli:main")

    def test_invalid_name_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid package name"):
            PackageConfig(name="bad name!", version="1.0.0", entry_point="mypkg.cli:main")

    def test_default_license(self) -> None:
        cfg = PackageConfig(name="mypkg", version="1.0.0", entry_point="mypkg.cli:main")
        assert cfg.license == "MIT"


# 🧰🌍🔚
