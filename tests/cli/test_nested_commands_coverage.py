#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for nested_commands uncovered branches."""

from __future__ import annotations

from typing import Optional

import click
import click.testing
from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock

from wrknv.cli.nested_commands import (
    CommandGroup,
    _extract_click_type,
    create_nested_cli,
)


class TestExtractClickTypeBranches(FoundationTestCase):
    """Cover uncovered branches in _extract_click_type."""

    def test_optional_int_covers_union_loop_body(self) -> None:
        """Lines 54-55: Union with non-None arg iterates and recurses."""
        # Optional[int] = Union[int, None], first arg is int (not NoneType)
        # so line 54's condition is True and line 55 (return) executes
        result = _extract_click_type(Optional[int])  # noqa: UP045
        assert result is str  # int falls through union bug → str

    def test_union_all_none_args_returns_str(self) -> None:
        """Line 56: Union where all args are NoneType -> return str at line 56."""
        # type(None) = NoneType; get_args(NoneType) = () so the for loop
        # at line 53 never executes and we fall through to line 56
        result = _extract_click_type(type(None))
        assert result is str


class TestBuildClickCommandBranches(FoundationTestCase):
    """Cover uncovered branches in CommandGroup._build_click_command."""

    def _make_group(self, name: str = "mygroup") -> CommandGroup:
        return CommandGroup(name=name, description="test group")

    def _mock_info(self, func=None, name: str = "cmd") -> Mock:
        """Create a mock CommandInfo with click_command=None."""
        info = Mock()
        info.click_command = None
        info.name = name
        info.description = "test"
        info.hidden = False
        info.func = func
        return info

    def test_non_callable_func_returns_none(self) -> None:
        """Line 139-140: func is not callable -> return None (line 149 is continue)."""
        info = self._mock_info(func="not_callable")
        group = self._make_group()
        result = group._build_click_command(info)
        assert result is None

    def test_ctx_param_is_skipped(self) -> None:
        """Line 149: continue when param_name is 'ctx'."""

        def my_cmd(ctx: click.Context, name: str = "world") -> None:
            pass

        info = self._mock_info(func=my_cmd, name="my-cmd")
        group = self._make_group()
        cmd = group._build_click_command(info)
        assert cmd is not None
        # ctx param was skipped, only 'name' param processed
        param_names = [p.name for p in cmd.params] if cmd.params else []
        assert "ctx" not in param_names

    def test_bool_param_builds_command(self) -> None:
        """Bool annotation: _extract_click_type returns str (not bool) due to
        the union-bug, so is_flag branch (line 160) is dead code.
        Verifies the command is still built (via the else branch)."""

        def my_cmd(verbose: bool = False) -> None:
            pass

        info = self._mock_info(func=my_cmd, name="my-cmd")
        group = self._make_group()
        cmd = group._build_click_command(info)
        assert cmd is not None

    def test_option_without_annotation(self) -> None:
        """Line 174: option with no annotation -> plain option (cmd built)."""

        def my_cmd(value="default") -> None:  # type: ignore[no-untyped-def]
            pass

        info = self._mock_info(func=my_cmd, name="my-cmd")
        group = self._make_group()
        cmd = group._build_click_command(info)
        assert cmd is not None


class TestToClickGroupWithSubgroup(FoundationTestCase):
    """Cover lines 121-124 and 128->120: to_click_group with CommandGroup subcommand."""

    def _mock_cmd(self, func=None, name: str = "cmd") -> Mock:
        info = Mock()
        info.click_command = None
        info.name = name
        info.description = "test"
        info.hidden = False
        info.func = func or (lambda: None)
        return info

    def test_nested_command_group_added_as_subgroup(self) -> None:
        """Lines 121-124: CommandGroup child -> add subgroup recursively."""
        parent = CommandGroup(name="parent", description="parent group")
        child = CommandGroup(name="child", description="child group")

        def child_cmd(name: str) -> None:
            click.echo(name)

        child.add_command("greet", self._mock_cmd(func=child_cmd, name="greet"))
        parent.add_command("child", child)

        click_group = parent.to_click_group()
        assert "child" in click_group.commands

    def test_non_callable_cmd_skipped_in_loop(self) -> None:
        """Branch 128->120: loop continues when _build_click_command returns None."""
        group = CommandGroup(name="mygroup", description="test group")
        # Non-callable func → _build_click_command returns None → loop skips add
        group.add_command("bad", self._mock_cmd(func="not_callable", name="bad"))

        click_group = group.to_click_group()
        # 'bad' command was not added (click_cmd was None/falsy)
        assert "bad" not in click_group.commands


class TestCreateNestedCli(FoundationTestCase):
    """Cover lines 392-393: version_cmd inside create_nested_cli."""

    def test_version_cmd_with_version_flag(self) -> None:
        """Line 393: version flag True -> echo version string."""
        cli = create_nested_cli(name="testcli", help="test")
        runner = click.testing.CliRunner()
        # Invoke the version command with --version to cover line 393
        cmd_names = list(cli.commands.keys())
        assert len(cmd_names) > 0
        result = runner.invoke(cli, [cmd_names[0], "--version"])
        assert result.exit_code == 0

    def test_version_cmd_without_flag(self) -> None:
        """Branch 392->exit: version flag False -> no output (covers false branch)."""
        cli = create_nested_cli(name="testcli", help="test")
        runner = click.testing.CliRunner()
        cmd_names = list(cli.commands.keys())
        assert len(cmd_names) > 0
        result = runner.invoke(cli, [cmd_names[0]])
        assert result.exit_code == 0
        assert result.output == ""


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])

# 🧰🌍🔚
