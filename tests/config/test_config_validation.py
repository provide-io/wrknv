#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for WorkenvConfigValidator."""

from __future__ import annotations

from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock

from wrknv.config.core import WorkenvSettings
from wrknv.config.validation import WorkenvConfigValidator


def _make_config(**kwargs: object) -> Mock:
    """Build a mock WorkenvConfig with valid defaults."""
    config = Mock()
    config.project_name = kwargs.get("project_name", "my-project")
    config.version = kwargs.get("version", "1.0.0")
    config.tools = kwargs.get("tools", {})
    config.profiles = kwargs.get("profiles", {})
    config.env = kwargs.get("env", {})

    workenv = kwargs.get("workenv", WorkenvSettings())
    config.workenv = workenv
    return config


class TestWorkenvConfigValidatorBasic(FoundationTestCase):
    """Tests for basic validate() functionality."""

    def test_valid_config_passes(self) -> None:
        config = _make_config()
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert is_valid
        assert errors == []

    def test_invalid_project_name_not_string(self) -> None:
        config = _make_config(project_name=123)
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("project_name" in e for e in errors)

    def test_invalid_project_name_empty(self) -> None:
        config = _make_config(project_name="   ")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("empty" in e for e in errors)

    def test_invalid_project_name_bad_chars(self) -> None:
        config = _make_config(project_name="my project!")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Invalid project_name" in e for e in errors)

    def test_invalid_version_not_string(self) -> None:
        config = _make_config(version=1)
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("version" in e for e in errors)

    def test_invalid_version_bad_format(self) -> None:
        config = _make_config(version="not_a_version")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Invalid version" in e for e in errors)

    def test_valid_special_versions(self) -> None:
        for ver in ("latest", "stable", "dev", "main", "master"):
            config = _make_config(version=ver)
            v = WorkenvConfigValidator(config)
            is_valid, _ = v.validate()
            assert is_valid, f"Expected {ver!r} to be valid"

    def test_tools_not_dict(self) -> None:
        config = _make_config(tools="not_a_dict")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("tools must be dictionary" in e for e in errors)

    def test_profiles_not_dict(self) -> None:
        config = _make_config(profiles="not_a_dict")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("profiles must be dictionary" in e for e in errors)

    def test_env_not_dict(self) -> None:
        config = _make_config(env="not_a_dict")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("env must be dictionary" in e for e in errors)


class TestValidateToolConfig(FoundationTestCase):
    """Tests for _validate_tool_config."""

    def _v(self, tools: object) -> tuple[bool, list[str]]:
        config = _make_config(tools=tools)
        return WorkenvConfigValidator(config).validate()

    def test_tool_string_version_valid(self) -> None:
        is_valid, errors = self._v({"terraform": "1.5.0"})
        assert is_valid
        assert errors == []

    def test_tool_string_version_invalid(self) -> None:
        is_valid, errors = self._v({"terraform": "not_version"})
        assert not is_valid
        assert any("Invalid version" in e for e in errors)

    def test_tool_list_versions_valid(self) -> None:
        is_valid, _ = self._v({"terraform": ["1.4.0", "1.5.0"]})
        assert is_valid

    def test_tool_list_versions_empty(self) -> None:
        is_valid, errors = self._v({"terraform": []})
        assert not is_valid
        assert any("empty version list" in e for e in errors)

    def test_tool_list_versions_non_string(self) -> None:
        is_valid, errors = self._v({"terraform": [1, 2]})
        assert not is_valid
        assert any("must be string" in e for e in errors)

    def test_tool_dict_with_version(self) -> None:
        is_valid, _ = self._v({"terraform": {"version": "1.5.0"}})
        assert is_valid

    def test_tool_dict_with_invalid_version(self) -> None:
        is_valid, errors = self._v({"terraform": {"version": 123}})
        assert not is_valid
        assert any("must be string" in e for e in errors)

    def test_tool_dict_with_invalid_path(self) -> None:
        is_valid, errors = self._v({"terraform": {"path": 123}})
        assert not is_valid
        assert any("Path for tool" in e for e in errors)

    def test_tool_dict_with_env_valid(self) -> None:
        is_valid, _ = self._v({"terraform": {"env": {"KEY": "value"}}})
        assert is_valid

    def test_tool_dict_with_env_not_dict(self) -> None:
        is_valid, errors = self._v({"terraform": {"env": "not_dict"}})
        assert not is_valid
        assert any("must be dictionary" in e for e in errors)

    def test_tool_dict_with_env_non_string_value(self) -> None:
        is_valid, errors = self._v({"terraform": {"env": {"KEY": 123}}})
        assert not is_valid
        assert any("must be string" in e for e in errors)

    def test_tool_invalid_type(self) -> None:
        is_valid, errors = self._v({"terraform": 123})
        assert not is_valid
        assert any("must be string, list, or dictionary" in e for e in errors)


class TestValidateProfileConfig(FoundationTestCase):
    """Tests for _validate_profile_config."""

    def _v(self, profiles: object) -> tuple[bool, list[str]]:
        config = _make_config(profiles=profiles)
        return WorkenvConfigValidator(config).validate()

    def test_valid_profile(self) -> None:
        is_valid, _ = self._v({"dev": {"terraform": "1.5.0"}})
        assert is_valid

    def test_profile_not_dict(self) -> None:
        is_valid, errors = self._v({"dev": "not_dict"})
        assert not is_valid
        assert any("must be a dictionary" in e for e in errors)

    def test_profile_with_invalid_version(self) -> None:
        is_valid, errors = self._v({"dev": {"terraform": "not_ver"}})
        assert not is_valid
        assert any("Invalid version" in e for e in errors)

    def test_profile_with_non_string_version(self) -> None:
        is_valid, errors = self._v({"dev": {"terraform": 123}})
        assert not is_valid
        assert any("must be string" in e for e in errors)


class TestValidateVersion(FoundationTestCase):
    """Tests for _is_valid_version."""

    def _valid(self, version: str) -> bool:
        v = WorkenvConfigValidator(_make_config(version=version))
        _, errors = v.validate()
        # Only check version-related errors
        return not any("Invalid version" in e or "version must be" in e for e in errors)

    def test_valid_semver_xyz(self) -> None:
        assert self._valid("1.2.3")

    def test_valid_semver_xy(self) -> None:
        assert self._valid("1.2")

    def test_valid_semver_with_v_prefix(self) -> None:
        assert self._valid("v1.2.3")

    def test_valid_semver_with_prerelease(self) -> None:
        assert self._valid("1.2.3-beta.1")

    def test_invalid_single_number(self) -> None:
        assert not self._valid("1")

    def test_invalid_non_numeric_major(self) -> None:
        assert not self._valid("a.b.c")


class TestValidateWorkenvSettings(FoundationTestCase):
    """Tests for _validate_workenv_settings."""

    def test_valid_workenv_settings(self) -> None:
        config = _make_config()
        v = WorkenvConfigValidator(config)
        is_valid, _ = v.validate()
        assert is_valid

    def test_invalid_container_runtime(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "container_runtime", "invalid")
        config = _make_config(workenv=ws)
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("container_runtime" in e for e in errors)

    def test_invalid_log_level(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "log_level", "VERBOSE")
        config = _make_config(workenv=ws)
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("log_level" in e for e in errors)

    def test_invalid_cache_ttl(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "cache_ttl", "not_duration")
        config = _make_config(workenv=ws)
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("cache_ttl" in e for e in errors)

    def test_workenv_not_settings_instance(self) -> None:
        config = _make_config(workenv="not_workenv")
        v = WorkenvConfigValidator(config)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("WorkenvSettings" in e for e in errors)


class TestValidateEnvConfig(FoundationTestCase):
    """Tests for _validate_env_config."""

    def _v(self, env: object) -> tuple[bool, list[str]]:
        config = _make_config(env=env)
        return WorkenvConfigValidator(config).validate()

    def test_valid_env(self) -> None:
        is_valid, _ = self._v({"PATH": "/usr/bin", "DEBUG": "true"})
        assert is_valid

    def test_env_invalid_value_type(self) -> None:
        is_valid, errors = self._v({"KEY": object()})
        assert not is_valid
        assert any("must be string" in e for e in errors)

    def test_env_list_value_valid(self) -> None:
        is_valid, _ = self._v({"FLAGS": ["--verbose", "--debug"]})
        assert is_valid

    def test_env_list_value_invalid_item(self) -> None:
        is_valid, errors = self._v({"FLAGS": [object()]})
        assert not is_valid
        assert any("list item" in e for e in errors)

    def test_env_empty_key(self) -> None:
        is_valid, errors = self._v({"": "value"})
        assert not is_valid
        assert any("cannot be empty" in e for e in errors)

    def test_env_key_with_invalid_chars(self) -> None:
        is_valid, errors = self._v({"MY KEY": "value"})
        assert not is_valid
        assert any("Invalid environment key" in e for e in errors)


class TestValidationBranchCoverage(FoundationTestCase):
    """Tests for uncovered branches in validation.py."""

    def _validator(self, **kwargs) -> WorkenvConfigValidator:
        return WorkenvConfigValidator(_make_config(**kwargs))

    # _is_valid_version: non-string input
    def test_is_valid_version_non_string_returns_false(self) -> None:
        v = self._validator()
        assert v._is_valid_version(123) is False  # type: ignore[arg-type]

    # _is_valid_version: 5-part version where part[2] has non-alnum chars
    def test_is_valid_version_part_non_alnum(self) -> None:
        v = self._validator()
        # 3-part version where patch part has only symbols
        assert v._is_valid_version("1.2.!!!") is False

    # _validate_tool_config: non-string tool_name
    def test_tool_name_not_string(self) -> None:
        v = self._validator(tools={123: "1.0.0"})  # type: ignore[dict-item]
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Tool name must be string" in e for e in errors)

    # _validate_tool_config: empty tool_name
    def test_tool_name_empty(self) -> None:
        v = self._validator(tools={"": "1.0.0"})
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Tool name cannot be empty" in e for e in errors)

    # _validate_tool_config: list with invalid version string
    def test_tool_list_invalid_version_string(self) -> None:
        v = self._validator(tools={"go": ["1.21", "bad!!!"]})
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Invalid version" in e for e in errors)

    # _validate_tool_config: dict with invalid version string
    def test_tool_dict_version_invalid_string(self) -> None:
        v = self._validator(tools={"go": {"version": "bad!!!"}})
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Invalid version" in e for e in errors)

    # _validate_tool_config: env value not string
    def test_tool_dict_env_value_not_string(self) -> None:
        v = self._validator(tools={"go": {"env": {"MY_VAR": 123}}})
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("must be string" in e for e in errors)

    # _validate_profile_config: non-string profile_name
    def test_profile_name_not_string(self) -> None:
        v = self._validator(profiles={123: {"go": "1.21"}})  # type: ignore[dict-item]
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Profile name must be string" in e for e in errors)

    # _validate_profile_config: empty profile_name
    def test_profile_name_empty(self) -> None:
        v = self._validator(profiles={"": {"go": "1.21"}})
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Profile name cannot be empty" in e for e in errors)

    # _validate_profile_config: tool name in profile not string
    def test_profile_tool_name_not_string(self) -> None:
        v = self._validator(profiles={"dev": {123: "1.21"}})  # type: ignore[dict-item]
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Tool name in profile" in e for e in errors)

    # _validate_workenv_settings: bool fields not bool
    def test_workenv_auto_install_not_bool(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "auto_install", "yes")  # type: ignore[arg-type]
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("auto_install must be boolean" in e for e in errors)

    def test_workenv_use_cache_not_bool(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "use_cache", 1)  # type: ignore[arg-type]
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("use_cache must be boolean" in e for e in errors)

    def test_workenv_cache_ttl_not_string(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "cache_ttl", 7)  # type: ignore[arg-type]
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("cache_ttl must be string" in e for e in errors)

    def test_workenv_log_level_not_string(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "log_level", 10)  # type: ignore[arg-type]
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("log_level must be string" in e for e in errors)

    def test_workenv_container_runtime_not_string(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "container_runtime", None)  # type: ignore[arg-type]
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("container_runtime must be string" in e for e in errors)

    def test_workenv_container_registry_not_string(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "container_registry", 42)  # type: ignore[arg-type]
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("container_registry must be string" in e for e in errors)

    def test_workenv_container_registry_invalid_url(self) -> None:
        ws = WorkenvSettings()
        object.__setattr__(ws, "container_registry", "not a valid url!!!")
        v = self._validator(workenv=ws)
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Invalid container_registry" in e for e in errors)

    # env: key not string
    def test_env_key_not_string(self) -> None:
        v = self._validator(env={123: "value"})  # type: ignore[dict-item]
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("Environment key must be string" in e for e in errors)

    # _validate_tool_config: tool dict env key not string (line 161)
    def test_tool_dict_env_key_not_string(self) -> None:
        v = self._validator(tools={"go": {"env": {123: "value"}}})  # type: ignore[dict-item]
        is_valid, errors = v.validate()
        assert not is_valid
        assert any("must be string" in e for e in errors)


# 🧰🌍🔚
