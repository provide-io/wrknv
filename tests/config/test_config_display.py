#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for WorkenvConfigDisplay."""

from __future__ import annotations

from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock

from wrknv.config.display import WorkenvConfigDisplay


def _make_config(**kwargs: object) -> Mock:
    """Build a mock WorkenvConfig with sensible defaults."""
    config = Mock()
    config.config_path = "/project/wrknv.toml"
    config.project_name = kwargs.get("project_name", "my-project")
    config.version = kwargs.get("version", "1.0.0")
    config.description = kwargs.get("description")
    config.tools = kwargs.get("tools", {})
    config.profiles = kwargs.get("profiles", {})
    config.container = kwargs.get("container")
    config.env = kwargs.get("env", {})
    config.gitignore = kwargs.get("gitignore", {})

    workenv = Mock()
    workenv.auto_install = True
    workenv.use_cache = True
    workenv.cache_ttl = "7d"
    workenv.log_level = "WARNING"
    workenv.container_runtime = "docker"
    workenv.container_registry = "ghcr.io"
    config.workenv = kwargs.get("workenv", workenv)

    return config


class TestWorkenvConfigDisplay(FoundationTestCase):
    """Tests for WorkenvConfigDisplay.show_config()."""

    def test_show_minimal_config(self) -> None:
        """Test display with minimal config."""
        config = _make_config()
        display = WorkenvConfigDisplay(config)
        # Should not raise; just runs echo_info/echo_success
        display.show_config()

    def test_show_with_no_project_name(self) -> None:
        """Test display when project_name is None."""
        config = _make_config(project_name=None)
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_no_version(self) -> None:
        """Test display when version is None."""
        config = _make_config(version=None)
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_description(self) -> None:
        """Test display with a description."""
        config = _make_config(description="A useful project")
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_tools_as_dict(self) -> None:
        """Test display when tools is a dict with version keys."""
        config = _make_config(tools={"terraform": {"version": "1.5.0"}, "go": "1.21.0"})
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_tools_non_dict_value(self) -> None:
        """Test display when a tool value is a plain string."""
        config = _make_config(tools={"terraform": "1.5.0"})
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_profiles(self) -> None:
        """Test display with profiles."""
        config = _make_config(profiles={"dev": {}, "prod": {}})
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_container_no_volumes_no_env(self) -> None:
        """Test display with container config without volumes/environment."""
        container = Mock()
        container.enabled = True
        container.base_image = "python:3.11"
        container.python_version = "3.11"
        container.volumes = []
        container.environment = {}
        config = _make_config(container=container)
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_container_volumes_and_env(self) -> None:
        """Test display with container having volumes and environment vars."""
        container = Mock()
        container.enabled = True
        container.base_image = "python:3.11"
        container.python_version = "3.11"
        container.volumes = ["/host:/container"]
        container.environment = {"KEY": "value"}
        config = _make_config(container=container)
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_env_dict_values(self) -> None:
        """Test display when env values include dicts."""
        config = _make_config(env={"PATH": "/usr/bin", "OPTIONS": {"key": "val"}})
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_show_with_gitignore_list_values(self) -> None:
        """Test display when gitignore has list values."""
        config = _make_config(gitignore={"templates": ["Python", "Node"], "output": ".gitignore"})
        display = WorkenvConfigDisplay(config)
        display.show_config()

    def test_display_stores_config_reference(self) -> None:
        """Test that display stores config reference."""
        config = _make_config()
        display = WorkenvConfigDisplay(config)
        assert display.config is config


# 🧰🌍🔚
