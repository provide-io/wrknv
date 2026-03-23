#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for TaskExecutor streaming, error handling, and edge case branches."""

from __future__ import annotations

from unittest import mock

from provide.foundation.errors import ProcessError, ProcessTimeoutError
from provide.testkit import FoundationTestCase
import pytest

from wrknv.errors import TaskTimeoutError
from wrknv.tasks.executor import TaskExecutor, _should_stream_output
from wrknv.tasks.schema import TaskConfig


class TestShouldStreamOutput(FoundationTestCase):
    """Tests for _should_stream_output."""

    def test_returns_true_when_stream_output_set(self) -> None:
        task = TaskConfig(name="t", run="echo hi", stream_output=True)
        assert _should_stream_output(task) is True

    def test_returns_false_when_not_tty_and_not_configured(self) -> None:
        task = TaskConfig(name="t", run="echo hi", stream_output=False)
        with mock.patch("sys.stdout") as mock_stdout:
            mock_stdout.isatty.return_value = False
            result = _should_stream_output(task)
        assert result is False

    def test_returns_true_when_tty_and_not_configured(self) -> None:
        task = TaskConfig(name="t", run="echo hi", stream_output=False)
        with mock.patch("sys.stdout") as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = _should_stream_output(task)
        assert result is True


class TestCompositeTaskRaisesNotImplemented(FoundationTestCase):
    """Tests that composite tasks raise NotImplementedError."""

    @pytest.mark.asyncio
    async def test_composite_task_raises(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="composite", run=["subtask1", "subtask2"])
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        with pytest.raises(NotImplementedError, match="Composite tasks"):
            await executor.execute(task)


class TestStreamingMode(FoundationTestCase):
    """Tests for the streaming execution path."""

    @pytest.mark.asyncio
    async def test_streaming_mode_collects_chunks(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="stream", run="echo hello", stream_output=True)
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        async def mock_async_stream(*args: object, **kwargs: object):  # type: ignore[misc]
            yield "hello\n"
            yield "world\n"

        with mock.patch("wrknv.tasks.executor.async_stream", side_effect=mock_async_stream):
            result = await executor.execute(task)

        assert result.success is True
        assert result.exit_code == 0
        assert "hello\n" in result.stdout
        assert "world\n" in result.stdout
        assert result.stderr == ""
        assert result.duration >= 0

    @pytest.mark.asyncio
    async def test_streaming_mode_empty_output(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="stream", run="true", stream_output=True)
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        async def mock_async_stream(*args: object, **kwargs: object):  # type: ignore[misc]
            return
            yield  # make it an async generator

        with mock.patch("wrknv.tasks.executor.async_stream", side_effect=mock_async_stream):
            result = await executor.execute(task)

        assert result.success is True
        assert result.stdout == ""

    @pytest.mark.asyncio
    async def test_streaming_mode_uses_shlex_fallback(self) -> None:
        """Complex shell commands fall back to sh -c when shlex fails."""
        tmp = self.create_temp_dir()
        # Use a command with quotes that might cause shlex issues
        task = TaskConfig(name="stream", run="echo 'hello world'", stream_output=True)
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        captured_cmd = []

        async def mock_async_stream(*args: object, **kwargs: object):  # type: ignore[misc]
            captured_cmd.append(kwargs.get("cmd") or (args[0] if args else None))
            yield "output\n"

        with (
            mock.patch("wrknv.tasks.executor.async_stream", side_effect=mock_async_stream),
            mock.patch("shlex.split", side_effect=ValueError("shlex failed")),
        ):
            result = await executor.execute(task)

        assert result.success is True
        # When shlex fails, should use sh -c
        assert captured_cmd[0] == ["/bin/sh", "-c", "echo 'hello world'"]


class TestProcessErrorHandling(FoundationTestCase):
    """Tests for ProcessError exception handling in execute()."""

    @pytest.mark.asyncio
    async def test_process_error_returns_failure_result(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="fail", run="exit 1")
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        error = ProcessError("process failed", return_code=42)

        with mock.patch("wrknv.tasks.executor.async_run", side_effect=error):
            result = await executor.execute(task)

        assert result.success is False
        assert result.exit_code == 1  # Falls back to 1 since ProcessError has no exit_code attr
        assert "process failed" in result.stderr

    @pytest.mark.asyncio
    async def test_process_error_has_duration(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="fail", run="exit 1")
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        error = ProcessError("failed", return_code=1)

        with mock.patch("wrknv.tasks.executor.async_run", side_effect=error):
            result = await executor.execute(task)

        assert result.duration >= 0


class TestKeyboardInterruptHandling(FoundationTestCase):
    """Tests for KeyboardInterrupt propagation in execute()."""

    @pytest.mark.asyncio
    async def test_keyboard_interrupt_reraises(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="interrupted", run="sleep 10")
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        with (
            mock.patch("wrknv.tasks.executor.async_run", side_effect=KeyboardInterrupt),
            pytest.raises(KeyboardInterrupt),
        ):
            await executor.execute(task)


class TestProcessTimeoutErrorHandling(FoundationTestCase):
    """Tests for ProcessTimeoutError → TaskTimeoutError conversion."""

    @pytest.mark.asyncio
    async def test_process_timeout_raises_task_timeout_error(self) -> None:
        tmp = self.create_temp_dir()
        task = TaskConfig(name="slow", run="sleep 10", timeout=0.1)
        executor = TaskExecutor(repo_path=tmp, auto_detect_env=False)

        timeout_error = ProcessTimeoutError("timed out", timeout_seconds=0.1)

        with (
            mock.patch("wrknv.tasks.executor.async_run", side_effect=timeout_error),
            pytest.raises(TaskTimeoutError) as exc_info,
        ):
            await executor.execute(task)

        assert exc_info.value.task_name == "slow"
        assert exc_info.value.timeout == 0.1


# 🧰🌍🔚
