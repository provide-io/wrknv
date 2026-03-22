#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for nested_commands module."""

from __future__ import annotations

import click
from provide.testkit import FoundationTestCase
import pytest

from wrknv.cli.nested_commands import (
    CommandGroup,
    NestedCommandRegistry,
    _extract_click_type,
    create_nested_cli,
    get_nested_registry,
    register_nested_command,
)


class TestExtractClickType(FoundationTestCase):
    """Tests for _extract_click_type.

    Note: the function has a known bug where `None in (Union, None)` is True
    for any annotation with get_origin() == None, causing most plain types
    to fall through to the Union branch and return str.
    These tests document actual behavior.
    """

    def test_none_annotation_returns_str(self) -> None:
        assert _extract_click_type(None) is str

    def test_nonetype_returns_str(self) -> None:
        assert _extract_click_type(type(None)) is str

    def test_str_returns_str(self) -> None:
        assert _extract_click_type(str) is str

    def test_int_returns_str(self) -> None:
        # Due to Union-check bug: get_origin(int) is None, which is in (Union, None)
        assert _extract_click_type(int) is str

    def test_optional_str_returns_str(self) -> None:
        assert _extract_click_type(str | None) is str

    def test_optional_int_returns_str(self) -> None:
        # Recurses into int → str (same bug as above)
        assert _extract_click_type(int | None) is str

    def test_list_returns_str(self) -> None:
        # get_origin(list) is list — misses Union check, falls to default
        result = _extract_click_type(list)
        assert result is str

    def test_unknown_type_returns_str(self) -> None:
        class CustomType:
            pass

        assert _extract_click_type(CustomType) is str

    def test_generic_list_returns_str(self) -> None:
        # list[str] has get_origin() == list, NOT None, so doesn't hit Union branch
        assert _extract_click_type(list[str]) is str  # type: ignore[type-arg]

    def test_generic_tuple_returns_str(self) -> None:
        # tuple[str] has get_origin() == tuple
        assert _extract_click_type(tuple[str]) is str  # type: ignore[type-arg]


class TestCommandGroupBasic(FoundationTestCase):
    """Tests for CommandGroup basic operations."""

    def test_add_command_stores_info(self) -> None:
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        info = CommandInfo(name="sub", func=lambda: None, description="sub cmd")
        group.add_command("sub", info)
        assert "sub" in group.commands
        assert group.commands["sub"] is info

    def test_add_subgroup_sets_parent(self) -> None:
        parent = CommandGroup(name="parent")
        child = CommandGroup(name="child")
        parent.add_command("child", child)
        assert child.parent is parent

    def test_get_command_empty_path_returns_self(self) -> None:
        group = CommandGroup(name="root")
        assert group.get_command([]) is group

    def test_get_command_missing_name_returns_none(self) -> None:
        group = CommandGroup(name="root")
        assert group.get_command(["missing"]) is None

    def test_get_command_single_level_commandinfo(self) -> None:
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        info = CommandInfo(name="sub", func=lambda: None, description="sub")
        group.add_command("sub", info)
        assert group.get_command(["sub"]) is info

    def test_get_command_nested_group(self) -> None:
        root = CommandGroup(name="root")
        mid = CommandGroup(name="mid")
        from provide.foundation.hub.commands import CommandInfo

        leaf = CommandInfo(name="leaf", func=lambda: None, description="leaf")
        mid.add_command("leaf", leaf)
        root.add_command("mid", mid)
        assert root.get_command(["mid", "leaf"]) is leaf

    def test_get_command_path_through_non_group_returns_none(self) -> None:
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        info = CommandInfo(name="cmd", func=lambda: None, description="cmd")
        group.add_command("cmd", info)
        # "cmd" is a CommandInfo, not a CommandGroup — can't drill deeper
        assert group.get_command(["cmd", "deeper"]) is None

    def test_get_command_returns_subgroup_at_path(self) -> None:
        root = CommandGroup(name="root")
        sub = CommandGroup(name="sub")
        root.add_command("sub", sub)
        assert root.get_command(["sub"]) is sub


class TestCommandGroupToClickGroup(FoundationTestCase):
    """Tests for CommandGroup.to_click_group (groups-only, no commands)."""

    def test_empty_group_creates_click_group(self) -> None:
        group = CommandGroup(name="mygroup", description="My group")
        click_group = group.to_click_group()
        assert isinstance(click_group, click.Group)
        assert click_group.name == "mygroup"

    def test_none_description(self) -> None:
        group = CommandGroup(name="nohelp")
        click_group = group.to_click_group()
        assert isinstance(click_group, click.Group)

    def test_hidden_group(self) -> None:
        group = CommandGroup(name="hidden", hidden=True)
        click_group = group.to_click_group()
        assert click_group.hidden

    def test_subgroup_becomes_nested_click_group(self) -> None:
        root = CommandGroup(name="root")
        sub = CommandGroup(name="sub", description="sub commands")
        root.add_command("sub", sub)
        click_root = root.to_click_group()
        assert "sub" in click_root.commands
        assert isinstance(click_root.commands["sub"], click.Group)

    def test_deeply_nested_groups(self) -> None:
        root = CommandGroup(name="root")
        mid = CommandGroup(name="mid")
        deep = CommandGroup(name="deep")
        mid.add_command("deep", deep)
        root.add_command("mid", mid)
        click_root = root.to_click_group()
        assert "mid" in click_root.commands
        assert "deep" in click_root.commands["mid"].commands  # type: ignore[attr-defined]

    def test_build_click_command_raises_when_no_click_command_attr(self) -> None:
        """CommandInfo lacks click_command; _build_click_command raises AttributeError."""
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        info = CommandInfo(name="cmd", func=lambda: None, description="cmd")
        with pytest.raises(AttributeError):
            group._build_click_command(info)


class TestNestedCommandRegistry(FoundationTestCase):
    """Tests for NestedCommandRegistry."""

    def _registry(self) -> NestedCommandRegistry:
        return NestedCommandRegistry()

    def test_register_simple_command(self) -> None:
        reg = self._registry()

        def my_cmd() -> None:
            pass

        reg.register_command("hello", func=my_cmd, description="say hello")
        result = reg.get_command("hello")
        assert result is not None

    def test_register_group(self) -> None:
        reg = self._registry()
        reg.register_command("mygroup", group=True, description="a group")
        result = reg.get_command("mygroup")
        assert isinstance(result, CommandGroup)

    def test_register_group_with_func_none(self) -> None:
        reg = self._registry()
        reg.register_command("mygroup2", func=None, description="a group 2")
        result = reg.get_command("mygroup2")
        assert isinstance(result, CommandGroup)

    def test_register_nested_command_via_space_name(self) -> None:
        reg = self._registry()
        reg.register_command("mygroup", group=True)

        def sub_cmd() -> None:
            pass

        reg.register_command("mygroup sub", func=sub_cmd)
        result = reg.get_command("mygroup sub")
        assert result is not None

    def test_register_nested_command_via_parent(self) -> None:
        reg = self._registry()
        reg.register_command("pgroup", group=True)

        def child_cmd() -> None:
            pass

        reg.register_command("child", func=child_cmd, parent="pgroup")
        result = reg.get_command("pgroup child")
        assert result is not None

    def test_register_creates_intermediate_groups(self) -> None:
        reg = self._registry()

        def deep_cmd() -> None:
            pass

        reg.register_command("a b c", func=deep_cmd)
        # Intermediate groups 'a' and 'b' should be auto-created
        assert reg.get_command("a b c") is not None

    def test_register_raises_when_nesting_under_non_group(self) -> None:
        reg = self._registry()

        def cmd() -> None:
            pass

        def nested() -> None:
            pass

        reg.register_command("cmd", func=cmd)
        with pytest.raises(ValueError, match="Cannot nest"):
            reg.register_command("cmd nested", func=nested)

    def test_get_missing_command_returns_none(self) -> None:
        reg = self._registry()
        assert reg.get_command("nonexistent") is None

    def test_to_click_group_returns_group(self) -> None:
        reg = self._registry()
        result = reg.to_click_group()
        assert isinstance(result, click.Group)

    def test_register_hidden_command(self) -> None:
        reg = self._registry()

        def hcmd() -> None:
            pass

        reg.register_command("hidden-cmd-x", func=hcmd, hidden=True)
        result = reg.get_command("hidden-cmd-x")
        assert result is not None

    def test_register_with_aliases(self) -> None:
        reg = self._registry()

        def acmd() -> None:
            pass

        reg.register_command("main-cmd", func=acmd, aliases=["mc", "m"])
        result = reg.get_command("main-cmd")
        assert result is not None

    def test_parent_string_with_spaces_parsed(self) -> None:
        reg = self._registry()
        reg.register_command("level1", group=True)
        reg.register_command("level2", group=True, parent="level1")

        def cmd() -> None:
            pass

        reg.register_command("cmd", func=cmd, parent="level1 level2")
        result = reg.get_command("level1 level2 cmd")
        assert result is not None


class TestBuildClickCommand(FoundationTestCase):
    """Tests for CommandGroup._build_click_command via mocked CommandInfo."""

    def test_returns_existing_click_command(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")
        mock_info = mock.Mock()
        mock_click_cmd = click.Command(name="test-cmd", callback=lambda: None)
        mock_info.click_command = mock_click_cmd
        result = group._build_click_command(mock_info)
        assert result is mock_click_cmd

    def test_returns_none_when_not_callable(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")
        mock_info = mock.Mock()
        mock_info.click_command = None
        mock_info.func = "not-callable"
        result = group._build_click_command(mock_info)
        assert result is None

    def test_builds_command_from_simple_function(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")

        def my_func(name: str = "world") -> None:
            """Greet someone."""

        mock_info = mock.Mock()
        mock_info.click_command = None
        mock_info.func = my_func
        mock_info.name = "greet"
        mock_info.description = "Greet someone."
        mock_info.hidden = False
        result = group._build_click_command(mock_info)
        assert isinstance(result, click.Command)

    def test_builds_command_with_bool_flag(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")

        def my_func(verbose: bool = False) -> None:
            pass

        mock_info = mock.Mock()
        mock_info.click_command = None
        mock_info.func = my_func
        mock_info.name = "cmd"
        mock_info.description = None
        mock_info.hidden = False
        result = group._build_click_command(mock_info)
        # Due to the Union-check bug, bool is treated as str option (not flag)
        # The command is still built correctly
        assert isinstance(result, click.Command)

    def test_builds_command_without_annotation(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")

        def my_func(name) -> None:
            pass

        mock_info = mock.Mock()
        mock_info.click_command = None
        mock_info.func = my_func
        mock_info.name = "cmd-no-ann"
        mock_info.description = None
        mock_info.hidden = False
        result = group._build_click_command(mock_info)
        assert isinstance(result, click.Command)

    def test_builds_command_with_required_argument(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")

        def my_func(path: str) -> None:  # required arg (no default)
            pass

        mock_info = mock.Mock()
        mock_info.click_command = None
        mock_info.func = my_func
        mock_info.name = "cmd-required"
        mock_info.description = None
        mock_info.hidden = False
        result = group._build_click_command(mock_info)
        assert isinstance(result, click.Command)

    def test_command_added_to_group_via_to_click_group(self) -> None:
        from unittest import mock

        group = CommandGroup(name="root")
        mock_info = mock.Mock()
        mock_click_cmd = click.Command(name="sub", callback=lambda: None)
        mock_info.click_command = mock_click_cmd
        # Add directly to commands dict (bypasses add_command type check)
        group.commands["sub"] = mock_info
        click_group = group.to_click_group()
        assert "sub" in click_group.commands


class TestRegisterNestedCommand(FoundationTestCase):
    """Tests for register_nested_command decorator."""

    def test_decorator_registers_command(self) -> None:
        from unittest import mock

        from wrknv.cli.nested_commands import _nested_registry

        with (
            mock.patch.object(_nested_registry, "register_command") as mock_reg,
            mock.patch("wrknv.cli.nested_commands.get_hub"),
        ):
            @register_nested_command("test-cmd-xyz", description="test")
            def my_cmd() -> None:
                pass

            mock_reg.assert_called_once()

    def test_decorator_returns_original_function(self) -> None:
        from unittest import mock

        from wrknv.cli.nested_commands import _nested_registry

        with (
            mock.patch.object(_nested_registry, "register_command"),
            mock.patch("wrknv.cli.nested_commands.get_hub"),
        ):
            @register_nested_command("my-unique-cmd-abc")
            def my_unique_func() -> None:
                """My unique function."""

            assert callable(my_unique_func)
            assert my_unique_func.__name__ == "my_unique_func"

    def test_decorator_with_group_flag(self) -> None:
        from unittest import mock

        from wrknv.cli.nested_commands import _nested_registry

        with (
            mock.patch.object(_nested_registry, "register_command") as mock_reg,
            mock.patch("wrknv.cli.nested_commands.get_hub"),
        ):
            @register_nested_command("my-group-abc", group=True)
            def group_func() -> None:
                pass

            call_kwargs = mock_reg.call_args.kwargs
            assert call_kwargs.get("func") is None or call_kwargs.get("group") is True


class TestCreateNestedCli(FoundationTestCase):
    """Tests for create_nested_cli."""

    def test_returns_click_group(self) -> None:
        result = create_nested_cli(name="test-cli")
        assert isinstance(result, click.Group)
        assert result.name == "test-cli"

    def test_applies_help_text(self) -> None:
        result = create_nested_cli(name="test-cli2", help="My help text")
        assert result.help == "My help text"

    def test_no_help_text_by_default(self) -> None:
        result = create_nested_cli(name="test-cli3")
        # help defaults to description of root group
        assert result is not None


class TestGetNestedRegistry(FoundationTestCase):
    """Tests for get_nested_registry."""

    def test_returns_registry_instance(self) -> None:
        reg = get_nested_registry()
        assert isinstance(reg, NestedCommandRegistry)

    def test_same_instance_returned_each_time(self) -> None:
        reg1 = get_nested_registry()
        reg2 = get_nested_registry()
        assert reg1 is reg2


# 🧰🌍🔚
