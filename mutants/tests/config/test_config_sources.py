#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for configuration sources."""

from __future__ import annotations

import os
from pathlib import Path

from provide.testkit import FoundationTestCase

from wrknv.config.sources import ConfigSource, EnvironmentConfigSource, FileConfigSource


class TestConfigSourceBase(FoundationTestCase):
    """Tests for the base ConfigSource class."""

    def test_base_get_tool_version_returns_none(self) -> None:
        source = ConfigSource()
        assert source.get_tool_version("terraform") is None

    def test_base_get_all_tools_returns_empty(self) -> None:
        source = ConfigSource()
        assert source.get_all_tools() == {}

    def test_base_get_profile_returns_empty(self) -> None:
        source = ConfigSource()
        assert source.get_profile("dev") == {}

    def test_base_get_setting_returns_default(self) -> None:
        source = ConfigSource()
        assert source.get_setting("key") is None
        assert source.get_setting("key", "default") == "default"


class TestFileConfigSource(FoundationTestCase):
    """Tests for FileConfigSource."""

    def setup_method(self) -> None:
        super().setup_method()
        self.temp_dir = self.create_temp_dir()

    def _write_toml(self, name: str, content: str) -> Path:
        p = self.temp_dir / name
        p.write_text(content)
        return p

    def test_load_existing_file(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv.tools]
terraform = "1.5.0"
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_tool_version("terraform") == "1.5.0"

    def test_load_nonexistent_file(self) -> None:
        source = FileConfigSource(self.temp_dir / "nonexistent.toml")
        assert source.get_tool_version("terraform") is None
        assert source.get_all_tools() == {}

    def test_get_all_tools(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv.tools]
terraform = "1.5.0"
go = "1.21.0"
""",
        )
        source = FileConfigSource(toml_path)
        tools = source.get_all_tools()
        assert tools["terraform"] == "1.5.0"
        assert tools["go"] == "1.21.0"

    def test_get_tool_version_missing_tool(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv.tools]
terraform = "1.5.0"
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_tool_version("missing") is None

    def test_get_profile(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv.profiles.dev]
terraform = "1.5.0"
""",
        )
        source = FileConfigSource(toml_path)
        profile = source.get_profile("dev")
        assert profile["terraform"] == "1.5.0"

    def test_get_profile_missing(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv]
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_profile("missing") == {}

    def test_get_setting_from_section_settings(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv.settings]
auto_install = true
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_setting("auto_install") is True

    def test_get_setting_nested_path(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[project]
name = "myapp"
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_setting("project.name") == "myapp"

    def test_get_setting_missing_returns_default(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv]
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_setting("nonexistent") is None
        assert source.get_setting("nonexistent", "fallback") == "fallback"

    def test_get_setting_nested_path_intermediate_missing(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv]
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_setting("missing.key.deep") is None

    def test_get_setting_nested_path_non_dict_intermediate(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv]
name = "test"
""",
        )
        source = FileConfigSource(toml_path)
        # workenv.name is a string, so .key.deep would fail
        assert source.get_setting("workenv.name.deep") is None

    def test_custom_section(self) -> None:
        toml_path = self._write_toml(
            "pyproject.toml",
            """
[tool.tools]
terraform = "1.5.0"
""",
        )
        source = FileConfigSource(toml_path, section="tool")
        assert source.get_tool_version("terraform") == "1.5.0"

    def test_all_tools_no_tools_section(self) -> None:
        toml_path = self._write_toml(
            "wrknv.toml",
            """
[workenv]
auto_install = true
""",
        )
        source = FileConfigSource(toml_path)
        assert source.get_all_tools() == {}


class TestEnvironmentConfigSource(FoundationTestCase):
    """Tests for EnvironmentConfigSource."""

    def test_get_tool_version_from_env(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_TERRAFORM_VERSION="1.5.0"):
            assert source.get_tool_version("terraform") == "1.5.0"

    def test_get_tool_version_tool_prefix_format(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_TOOL_TERRAFORM_VERSION="1.6.0"):
            assert source.get_tool_version("terraform") == "1.6.0"

    def test_get_tool_version_not_set(self) -> None:
        source = EnvironmentConfigSource()
        assert source.get_tool_version("notset_tool") is None

    def test_get_all_tools_with_env_vars(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_TERRAFORM_VERSION="1.5.0", WRKNV_GO_VERSION="1.21.0"):
            tools = source.get_all_tools()
            assert "terraform" in tools
            assert tools["terraform"] == "1.5.0"
            assert "go" in tools

    def test_get_all_tools_skips_project_version(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_PROJECT_VERSION="1.0.0"):
            tools = source.get_all_tools()
            assert "project" not in tools

    def test_get_all_tools_includes_tool_prefix(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_TOOL_UV_VERSION="0.1.0"):
            tools = source.get_all_tools()
            assert "uv" in tools

    def test_get_profile(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_PROFILE_DEV_TERRAFORM="1.5.0"):
            profile = source.get_profile("dev")
            assert "terraform" in profile
            assert profile["terraform"] == "1.5.0"

    def test_get_profile_empty_when_no_env(self) -> None:
        source = EnvironmentConfigSource()
        assert source.get_profile("dev") == {}

    def test_get_setting_true_values(self) -> None:
        source = EnvironmentConfigSource()
        for val in ("true", "1", "yes", "on"):
            with self._env(WRKNV_AUTO_INSTALL=val):
                assert source.get_setting("auto_install") is True

    def test_get_setting_false_values(self) -> None:
        source = EnvironmentConfigSource()
        for val in ("false", "0", "no", "off"):
            with self._env(WRKNV_AUTO_INSTALL=val):
                assert source.get_setting("auto_install") is False

    def test_get_setting_string_value(self) -> None:
        source = EnvironmentConfigSource()
        with self._env(WRKNV_LOG_LEVEL="DEBUG"):
            assert source.get_setting("log_level") == "DEBUG"

    def test_get_setting_not_set(self) -> None:
        source = EnvironmentConfigSource()
        assert source.get_setting("unset_key_xyz") is None
        assert source.get_setting("unset_key_xyz", "default") == "default"

    def test_custom_prefix(self) -> None:
        source = EnvironmentConfigSource(prefix="MYAPP")
        with self._env(MYAPP_TERRAFORM_VERSION="1.5.0"):
            assert source.get_tool_version("terraform") == "1.5.0"

    def test_get_setting_dotted_key(self) -> None:
        """Dotted keys are converted to underscores in env var name."""
        source = EnvironmentConfigSource()
        with self._env(WRKNV_WORKENV_LOG_LEVEL="INFO"):
            assert source.get_setting("workenv.log_level") == "INFO"

    def _env(self, **kwargs: str) -> _EnvContext:
        return _EnvContext(**kwargs)


class _EnvContext:
    """Context manager for setting/restoring env vars."""

    def __init__(self, **kwargs: str) -> None:
        self.kwargs = kwargs
        self.original: dict[str, str | None] = {}

    def __enter__(self) -> _EnvContext:
        for key, val in self.kwargs.items():
            self.original[key] = os.environ.get(key)
            os.environ[key] = val
        return self

    def __exit__(self, *_: object) -> None:
        for key, orig in self.original.items():
            if orig is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = orig


# 🧰🌍🔚
