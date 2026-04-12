#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.schema - WorkenvSchema, merge_with_profile, and config functions
=========================================================================================
Covers: WorkenvSchema, merge_with_profile, validate_config_dict, load_config_from_dict,
get_default_config, config_to_toml."""

from __future__ import annotations

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.schema import (
    ContainerConfig,
    ProfileConfig,
    ToolConfig,
    WorkenvSchema,
    config_to_toml,
    get_default_config,
    load_config_from_dict,
    validate_config_dict,
)

# ---------------------------------------------------------------------------
# WorkenvSchema
# ---------------------------------------------------------------------------


class TestWorkenvSchema(FoundationTestCase):
    """Tests for WorkenvSchema."""

    def test_minimal_creation(self) -> None:
        schema = WorkenvSchema(project_name="my-project")
        assert schema.project_name == "my-project"
        assert schema.tools == {}
        assert schema.profiles == {}

    def test_post_init_expands_install_dir(self) -> None:
        schema = WorkenvSchema(project_name="test", install_dir="~/.wrknv")
        assert "~" not in schema.install_dir

    def test_post_init_expands_cache_dir(self) -> None:
        schema = WorkenvSchema(project_name="test", cache_dir="~/.wrknv/cache")
        assert "~" not in schema.cache_dir

    def test_log_level_converted_to_uppercase(self) -> None:
        schema = WorkenvSchema(project_name="test", log_level="debug")
        assert schema.log_level == "DEBUG"

    def test_empty_project_name_raises(self) -> None:
        with pytest.raises(ValueError, match="Project name cannot be empty"):
            WorkenvSchema(project_name="")

    def test_get_tool_config_returns_none_when_missing(self) -> None:
        schema = WorkenvSchema(project_name="test")
        assert schema.get_tool_config("unknown") is None

    def test_get_tool_config_returns_config(self) -> None:
        tool = ToolConfig(version="1.5.0")
        schema = WorkenvSchema(project_name="test", tools={"terraform": tool})
        result = schema.get_tool_config("terraform")
        assert result is not None
        assert result.version == "1.5.0"

    def test_get_profile_returns_none_when_missing(self) -> None:
        schema = WorkenvSchema(project_name="test")
        assert schema.get_profile("nonexistent") is None

    def test_get_profile_returns_profile(self) -> None:
        profile = ProfileConfig(name="dev")
        schema = WorkenvSchema(project_name="test", profiles={"dev": profile})
        result = schema.get_profile("dev")
        assert result is not None
        assert result.name == "dev"

    def test_model_dump_returns_dict(self) -> None:
        schema = WorkenvSchema(project_name="test")
        d = schema.model_dump()
        assert isinstance(d, dict)
        assert d["project_name"] == "test"

    def test_model_dump_exclude_none(self) -> None:
        schema = WorkenvSchema(project_name="test")
        d = schema.model_dump(exclude_none=True)
        # container, package, registry are None by default and should be removed
        assert "container" not in d
        assert "package" not in d
        assert "registry" not in d

    def test_model_dump_include_none_by_default(self) -> None:
        schema = WorkenvSchema(project_name="test")
        d = schema.model_dump()
        assert "container" in d  # key present (value is None)


# ---------------------------------------------------------------------------
# merge_with_profile
# ---------------------------------------------------------------------------


class TestMergeWithProfile(FoundationTestCase):
    """Tests for WorkenvSchema.merge_with_profile."""

    def test_merge_with_nonexistent_profile_returns_self(self) -> None:
        schema = WorkenvSchema(project_name="test")
        result = schema.merge_with_profile("nonexistent")
        assert result is schema

    def test_merge_with_profile_merges_tools(self) -> None:
        tool = ToolConfig(version="1.9.0")
        profile = ProfileConfig(name="prod", tools={"terraform": tool})
        schema = WorkenvSchema(project_name="test", profiles={"prod": profile})
        merged = schema.merge_with_profile("prod")
        assert "terraform" in merged.tools
        assert merged.tools["terraform"].version == "1.9.0"

    def test_merge_with_profile_merges_environment(self) -> None:
        profile = ProfileConfig(name="dev", environment={"FOO": "bar"})
        schema = WorkenvSchema(project_name="test", profiles={"dev": profile})
        merged = schema.merge_with_profile("dev")
        assert merged.environment.get("FOO") == "bar"

    def test_merge_with_profile_merges_scripts(self) -> None:
        profile = ProfileConfig(name="dev", scripts={"build": "make build"})
        schema = WorkenvSchema(project_name="test", profiles={"dev": profile})
        merged = schema.merge_with_profile("dev")
        assert merged.scripts.get("build") == "make build"

    def test_merge_with_profile_merges_container(self) -> None:
        container = ContainerConfig(enabled=True, base_image="debian:12")
        profile = ProfileConfig(name="dev", container=container)
        schema = WorkenvSchema(project_name="test", profiles={"dev": profile})
        merged = schema.merge_with_profile("dev")
        assert merged.container is not None
        assert merged.container.base_image == "debian:12"


# ---------------------------------------------------------------------------
# validate_config_dict
# ---------------------------------------------------------------------------


class TestValidateConfigDict(FoundationTestCase):
    """Tests for validate_config_dict function."""

    def test_valid_config_returns_true(self) -> None:
        config = {"project_name": "myproject"}
        is_valid, errors = validate_config_dict(config)
        assert is_valid is True
        assert errors == []

    def test_missing_project_name_returns_false(self) -> None:
        config = {}
        is_valid, errors = validate_config_dict(config)
        assert is_valid is False
        assert len(errors) > 0

    def test_invalid_log_level_returns_false(self) -> None:
        config = {"project_name": "test", "log_level": "INVALID_LEVEL"}
        is_valid, _errors = validate_config_dict(config)
        assert is_valid is False


# ---------------------------------------------------------------------------
# load_config_from_dict
# ---------------------------------------------------------------------------


class TestLoadConfigFromDict(FoundationTestCase):
    """Tests for load_config_from_dict function."""

    def test_loads_valid_config(self) -> None:
        config = {"project_name": "myproject"}
        result = load_config_from_dict(config)
        assert result.project_name == "myproject"

    def test_raises_on_invalid_config(self) -> None:
        with pytest.raises(ValueError, match="Configuration validation failed"):
            load_config_from_dict({})

    def test_loads_with_tool_config(self) -> None:
        config = {
            "project_name": "test",
            "tools": {
                "terraform": {"version": "1.5.0", "enabled": True},
            },
        }
        result = load_config_from_dict(config)
        assert "terraform" in result.tools
        assert result.tools["terraform"].version == "1.5.0"


# ---------------------------------------------------------------------------
# get_default_config
# ---------------------------------------------------------------------------


class TestGetDefaultConfig(FoundationTestCase):
    """Tests for get_default_config function."""

    def test_returns_workenv_schema(self) -> None:
        result = get_default_config()
        assert isinstance(result, WorkenvSchema)

    def test_default_project_name(self) -> None:
        result = get_default_config()
        assert result.project_name == "wrknv"

    def test_custom_project_name(self) -> None:
        result = get_default_config("acme")
        assert result.project_name == "acme"

    def test_has_default_tools(self) -> None:
        result = get_default_config()
        assert "terraform" in result.tools
        assert "tofu" in result.tools
        assert "go" in result.tools
        assert "uv" in result.tools

    def test_container_disabled_by_default(self) -> None:
        result = get_default_config()
        assert result.container is not None
        assert result.container.enabled is False


# ---------------------------------------------------------------------------
# config_to_toml
# ---------------------------------------------------------------------------


class TestConfigToToml(FoundationTestCase):
    """Tests for config_to_toml function."""

    def test_returns_string(self) -> None:
        config = get_default_config("toml-test")
        result = config_to_toml(config)  # type: ignore[arg-type]
        assert isinstance(result, str)

    def test_contains_project_name(self) -> None:
        config = get_default_config("my-toml-project")
        result = config_to_toml(config)  # type: ignore[arg-type]
        assert "my-toml-project" in result


class TestSchemaCoverage(FoundationTestCase):
    """Cover uncovered branches in schema.py."""

    def test_validate_package_name_empty_raises(self) -> None:
        """Lines 74-75: validate_package_name_validator raises on empty value."""
        from wrknv.wenv.schema import validate_package_name_validator

        with pytest.raises(ValueError, match="cannot be empty"):
            validate_package_name_validator(None, None, "")  # type: ignore[arg-type]

    def test_validate_package_name_invalid_chars_raises(self) -> None:
        """Lines 77-78: validate_package_name_validator raises on invalid chars."""
        from wrknv.wenv.schema import validate_package_name_validator

        with pytest.raises(ValueError, match="Invalid package name"):
            validate_package_name_validator(None, None, "bad@name!")  # type: ignore[arg-type]

    def test_validate_package_name_valid_returns_none(self) -> None:
        """Line 77->exit: valid package name → no ValueError, function returns None."""
        from wrknv.wenv.schema import validate_package_name_validator

        # Should not raise — "my-package" is valid (alphanumeric after replacements)
        result = validate_package_name_validator(None, None, "my-package")  # type: ignore[arg-type]
        assert result is None

    def test_validate_config_dict_exception_with_cause(self) -> None:
        """Line 387: exception with __cause__ appends cause message."""
        from unittest.mock import patch

        from wrknv.wenv.schema import validate_config_dict

        exc = Exception("outer error")
        exc.__cause__ = ValueError("inner cause")

        with patch("wrknv.wenv.schema.cattrs.Converter") as mock_converter_cls:
            mock_converter_cls.return_value.structure.side_effect = exc
            valid, errors = validate_config_dict({})

        assert valid is False
        assert "inner cause" in errors[0]


# 🧰🌍🔚
