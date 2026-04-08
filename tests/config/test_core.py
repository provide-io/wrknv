#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for config.core module - covering uncovered branches."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config.core import WorkenvConfig, WorkenvConfigError


def _make_config() -> WorkenvConfig:
    """Create a config with mocked persistence/display/validator."""
    with mock.patch.object(
        WorkenvConfig, "_find_config_file", return_value=pathlib.Path("/nonexistent/wrknv.toml")
    ):
        cfg = WorkenvConfig.load()
    return cfg


class TestGetToolVersion(FoundationTestCase):
    """Tests for get_tool_version."""

    def test_returns_version_from_dict(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": {"version": "1.5.7"}}
        assert cfg.get_tool_version("terraform") == "1.5.7"

    def test_returns_none_when_no_version_key(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": {}}
        assert cfg.get_tool_version("terraform") is None

    def test_returns_string_tool_directly(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": "1.5.7"}  # type: ignore[dict-item]
        assert cfg.get_tool_version("terraform") == "1.5.7"

    def test_returns_none_for_missing_tool(self) -> None:
        cfg = _make_config()
        cfg.tools = {}
        assert cfg.get_tool_version("nope") is None


class TestSetToolVersion(FoundationTestCase):
    """Tests for set_tool_version."""

    def test_creates_new_tool_entry(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.tools = {}
        cfg.set_tool_version("terraform", "1.5.7")
        assert cfg.tools["terraform"]["version"] == "1.5.7"

    def test_updates_existing_dict_entry(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.tools = {"terraform": {"version": "1.5.0"}}
        cfg.set_tool_version("terraform", "1.5.7")
        assert cfg.tools["terraform"]["version"] == "1.5.7"

    def test_replaces_string_with_dict(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.tools = {"terraform": "1.5.0"}  # type: ignore[dict-item]
        cfg.set_tool_version("terraform", "1.5.7")
        assert cfg.tools["terraform"] == {"version": "1.5.7"}


class TestGetAllTools(FoundationTestCase):
    """Tests for get_all_tools."""

    def test_returns_dict_versions(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": {"version": "1.5.7"}, "go": {"version": "1.21.0"}}
        result = cfg.get_all_tools()
        assert result["terraform"] == "1.5.7"
        assert result["go"] == "1.21.0"

    def test_returns_string_versions(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": "1.5.7"}  # type: ignore[dict-item]
        result = cfg.get_all_tools()
        assert result["terraform"] == "1.5.7"

    def test_skips_tools_without_version(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": {}}
        result = cfg.get_all_tools()
        assert "terraform" not in result


class TestProfiles(FoundationTestCase):
    """Tests for profile methods."""

    def test_get_profile_returns_none_when_missing(self) -> None:
        cfg = _make_config()
        assert cfg.get_profile("nope") is None

    def test_get_profile_returns_profile(self) -> None:
        cfg = _make_config()
        cfg.profiles = {"dev": {"terraform": "1.5.7"}}
        assert cfg.get_profile("dev") == {"terraform": "1.5.7"}

    def test_list_profiles(self) -> None:
        cfg = _make_config()
        cfg.profiles = {"dev": {}, "prod": {}}
        assert sorted(cfg.list_profiles()) == ["dev", "prod"]

    def test_profile_exists(self) -> None:
        cfg = _make_config()
        cfg.profiles = {"dev": {}}
        assert cfg.profile_exists("dev") is True
        assert cfg.profile_exists("nope") is False

    def test_save_profile(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.save_profile("dev", {"terraform": "1.5.7"})
        assert cfg.profiles["dev"] == {"terraform": "1.5.7"}

    def test_delete_profile_success(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.profiles = {"dev": {"terraform": "1.5.7"}}
        result = cfg.delete_profile("dev")
        assert result is True
        assert "dev" not in cfg.profiles

    def test_delete_profile_not_found(self) -> None:
        cfg = _make_config()
        result = cfg.delete_profile("nope")
        assert result is False

    def test_get_current_profile(self) -> None:
        cfg = _make_config()
        assert cfg.get_current_profile() == "default"


class TestGetSetting(FoundationTestCase):
    """Tests for get_setting."""

    def test_simple_attribute(self) -> None:
        cfg = _make_config()
        result = cfg.get_setting("project_name")
        assert result == "my-project"

    def test_nested_attribute(self) -> None:
        cfg = _make_config()
        result = cfg.get_setting("workenv.log_level")
        assert result == "WARNING"

    def test_missing_key_returns_default(self) -> None:
        cfg = _make_config()
        assert cfg.get_setting("nope", "fallback") == "fallback"

    def test_dict_nested_access(self) -> None:
        cfg = _make_config()
        cfg.tools = {"terraform": {"version": "1.5.7"}}
        result = cfg.get_setting("tools.terraform.version")
        assert result == "1.5.7"


class TestSetSetting(FoundationTestCase):
    """Tests for set_setting."""

    def test_sets_simple_attribute(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.set_setting("project_name", "new-project")
        assert cfg.project_name == "new-project"

    def test_sets_nested_dict_value(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.tools = {"terraform": {}}
        cfg.set_setting("tools.terraform.version", "1.5.7")
        assert cfg.tools["terraform"]["version"] == "1.5.7"

    def test_creates_nested_dict_path(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.tools = {}
        cfg.set_setting("tools.newkey", "value")
        assert cfg.tools["newkey"] == "value"

    def test_raises_when_parent_invalid(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        # project_name is a string, not a dict or object with sub-attributes
        with pytest.raises(WorkenvConfigError):
            cfg.set_setting("project_name.sub.key", "value")


class TestDelegationMethods(FoundationTestCase):
    """Tests for delegation methods."""

    def test_save_config_delegates(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.save_config()
        cfg._persistence.save_config.assert_called_once()

    def test_to_dict_when_persistence_is_none(self) -> None:
        cfg = _make_config()
        cfg._persistence = None
        assert cfg.to_dict() == {}

    def test_to_dict_delegates(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg._persistence.to_dict.return_value = {"key": "val"}
        assert cfg.to_dict() == {"key": "val"}

    def test_write_config_delegates(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.write_config({"key": "val"})
        cfg._persistence.write_config.assert_called_once_with({"key": "val"})

    def test_edit_config_delegates(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg.edit_config()
        cfg._persistence.edit_config.assert_called_once()

    def test_show_config_delegates(self) -> None:
        cfg = _make_config()
        cfg._display = mock.Mock()
        cfg.show_config()
        cfg._display.show_config.assert_called_once()

    def test_validate_config_when_validator_is_none(self) -> None:
        cfg = _make_config()
        cfg._validator = None
        result, errors = cfg.validate_config()
        assert result is True
        assert errors == []

    def test_validate_config_delegates(self) -> None:
        cfg = _make_config()
        cfg._validator = mock.Mock()
        cfg._validator.validate.return_value = (False, ["bad"])
        result, errors = cfg.validate_config()
        assert result is False
        assert errors == ["bad"]

    def test_validate_alias(self) -> None:
        cfg = _make_config()
        cfg._validator = mock.Mock()
        cfg._validator.validate.return_value = (True, [])
        assert cfg.validate() == cfg.validate_config()

    def test_config_exists_when_persistence_is_none(self) -> None:
        cfg = _make_config()
        cfg._persistence = None
        assert cfg.config_exists() is False

    def test_config_exists_delegates(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg._persistence.config_exists.return_value = True
        assert cfg.config_exists() is True

    def test_get_config_path_raises_when_persistence_is_none(self) -> None:
        cfg = _make_config()
        cfg._persistence = None
        with pytest.raises(RuntimeError):
            cfg.get_config_path()

    def test_get_config_path_delegates(self) -> None:
        cfg = _make_config()
        cfg._persistence = mock.Mock()
        cfg._persistence.get_config_path.return_value = pathlib.Path("/foo/bar.toml")
        assert cfg.get_config_path() == pathlib.Path("/foo/bar.toml")


class TestValidateVersion(FoundationTestCase):
    """Tests for validate_version."""

    def test_empty_version_is_invalid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "") is False

    def test_none_version_is_invalid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", None) is False  # type: ignore[arg-type]

    def test_latest_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "latest") is True

    def test_stable_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "stable") is True

    def test_semver_xyz_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "1.5.7") is True

    def test_semver_xy_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "1.5") is True

    def test_semver_with_prerelease_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "1.5.7-rc1") is True

    def test_wildcard_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "1.*") is True

    def test_tilde_constraint_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "~1.5") is True

    def test_caret_constraint_is_valid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "^1.5") is True

    def test_arbitrary_string_is_invalid(self) -> None:
        cfg = _make_config()
        assert cfg.validate_version("terraform", "not-a-version") is False


class TestSetSettingBranches(FoundationTestCase):
    """Cover set_setting branches in config/core.py."""

    def test_set_setting_nested_dict_creates_path(self) -> None:
        """Line 286: nested key where parent is dict and part not in it."""
        cfg = _make_config()
        # Set a key that involves dict traversal
        with mock.patch.object(cfg, "save_config"):
            cfg.tools = {}
            cfg.set_setting("tools.mykey.subkey", "value")
        assert cfg.tools.get("mykey", {}).get("subkey") == "value"

    def test_set_setting_invalid_target_raises(self) -> None:
        """Line 298: set_setting on non-dict, non-object target -> error."""
        cfg = _make_config()
        # Set a string attribute then try to set a sub-attribute of it
        cfg.project_name = "myproject"
        with pytest.raises(WorkenvConfigError):
            cfg.set_setting("project_name.subfield", "value")

    def test_merge_env_description(self) -> None:
        """Line 134: WRKNV_DESCRIPTION env var merges into config."""
        import os

        with (
            mock.patch.dict(os.environ, {"WRKNV_DESCRIPTION": "env-set-desc"}),
            mock.patch.object(
                WorkenvConfig, "_find_config_file", return_value=pathlib.Path("/nonexistent/wrknv.toml")
            ),
        ):
            cfg = WorkenvConfig.load()
        assert cfg.description == "env-set-desc"


# 🧰🌍🔚
