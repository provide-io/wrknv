#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for nested_commands module."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import click
from provide.testkit import FoundationTestCase

from wrknv.cli.nested_commands import (
    CommandGroup,
    NestedCommandRegistry,
    _extract_click_type,
    get_nested_registry,
)


class TestExtractClickType(FoundationTestCase):
    """Tests for _extract_click_type."""

    def test_none_annotation_returns_str(self) -> None:
        assert _extract_click_type(None) is str

    def test_nonetype_returns_str(self) -> None:
        assert _extract_click_type(type(None)) is str

    def test_str_returns_str(self) -> None:
        assert _extract_click_type(str) is str

    def test_int_returns_int(self) -> None:
        assert _extract_click_type(int) is int

    def test_float_returns_float(self) -> None:
        assert _extract_click_type(float) is float

    def test_bool_returns_bool(self) -> None:
        assert _extract_click_type(bool) is bool

    def test_path_returns_click_path(self) -> None:
        result = _extract_click_type(Path)
        assert isinstance(result, click.Path)

    def test_list_returns_str(self) -> None:
        assert _extract_click_type(list) is str

    def test_optional_str_returns_str(self) -> None:
        assert _extract_click_type(Optional[str]) is str  # noqa: UP007

    def test_optional_int_returns_int(self) -> None:
        assert _extract_click_type(Optional[int]) is int  # noqa: UP007

    def test_unknown_type_returns_str(self) -> None:
        class CustomType:
            pass

        assert _extract_click_type(CustomType) is str


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

    def test_get_command_single_level(self) -> None:
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        info = CommandInfo(name="sub", func=lambda: None, description="sub")
        group.add_command("sub", info)
        assert group.get_command(["sub"]) is info

    def test_get_command_nested(self) -> None:
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


class TestCommandGroupToClickGroup(FoundationTestCase):
    """Tests for CommandGroup.to_click_group."""

    def test_empty_group_creates_click_group(self) -> None:
        group = CommandGroup(name="mygroup", description="My group")
        click_group = group.to_click_group()
        assert isinstance(click_group, click.Group)
        assert click_group.name == "mygroup"

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

    def test_command_added_via_build(self) -> None:
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        def my_cmd() -> None:
            pass

        info = CommandInfo(name="mycmd", func=my_cmd, description="my cmd")
        group.add_command("mycmd", info)
        click_group = group.to_click_group()
        assert "mycmd" in click_group.commands

    def test_existing_click_command_used_directly(self) -> None:
        group = CommandGroup(name="root")
        from provide.foundation.hub.commands import CommandInfo

        @click.command("directcmd")
        def direct_cmd() -> None:
            pass

        info = CommandInfo(name="directcmd", func=direct_cmd, click_command=direct_cmd)
        group.add_command("directcmd", info)
        click_group = group.to_click_group()
        assert "directcmd" in click_group.commands


class TestCommandGroupBuildClickCommand(FoundationTestCase):
    """Tests for CommandGroup._build_click_command."""

    def _group(self) -> CommandGroup:
        return CommandGroup(name="g")

    def test_returns_none_for_non_callable(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        info = CommandInfo(name="bad", func="not_callable", description="bad")  # type: ignore[arg-type]
        result = self._group()._build_click_command(info)
        assert result is None

    def test_param_with_bool_annotation_is_flag(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(verbose: bool = False) -> None:
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None
        param_names = [p.name for p in click_cmd.params]
        assert "verbose" in param_names

    def test_param_with_string_annotation_is_option(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(name: str = "default") -> None:
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None

    def test_param_without_default_is_argument(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(target: str) -> None:
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None
        # Arguments don't have '--' prefix
        arg_names = [p.name for p in click_cmd.params if isinstance(p, click.Argument)]
        assert "target" in arg_names

    def test_param_no_annotation_no_default_is_argument(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(x) -> None:  # type: ignore[no-untyped-def]
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None

    def test_skips_self_cls_ctx_params(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(ctx: click.Context, x: str) -> None:
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None
        param_names = [p.name for p in click_cmd.params]
        assert "ctx" not in param_names

    def test_param_with_no_annotation_with_default(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(x=None) -> None:  # type: ignore[no-untyped-def]
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None

    def test_param_with_path_annotation(self) -> None:
        from provide.foundation.hub.commands import CommandInfo

        def cmd(target: Path) -> None:
            pass

        info = CommandInfo(name="cmd", func=cmd, description="cmd")
        click_cmd = self._group()._build_click_command(info)
        assert click_cmd is not None


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
        # Intermediate group 'a' and 'b' should be auto-created
        assert reg.get_command("a b c") is not None

    def test_register_raises_when_nesting_under_non_group(self) -> None:
        reg = self._registry()

        def cmd() -> None:
            pass

        def nested() -> None:
            pass

        reg.register_command("cmd", func=cmd)
        import pytest

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

        reg.register_command("hidden-cmd", func=hcmd, hidden=True)
        result = reg.get_command("hidden-cmd")
        assert result is not None

    def test_register_with_aliases(self) -> None:
        reg = self._registry()

        def acmd() -> None:
            pass

        reg.register_command("main-cmd", func=acmd, aliases=["mc", "m"])
        result = reg.get_command("main-cmd")
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
