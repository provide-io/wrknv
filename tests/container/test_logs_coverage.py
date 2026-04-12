#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for ContainerLogs coverage gaps.

Targets missing lines: 53-59, 70-77, 97→99, 100, 102, 108, 130-156, 167-191
"""

from __future__ import annotations

from datetime import UTC

from provide.foundation.process import ProcessError
from provide.testkit.mocking import MagicMock, patch
import pytest
from rich.console import Console

from wrknv.container.operations.logs import ContainerLogs
from wrknv.container.runtime.docker import DockerRuntime


@pytest.mark.container
class TestContainerLogsFollow:
    """Test get_logs with follow=True (lines 53-59)."""

    def setup_method(self) -> None:
        self.runtime = DockerRuntime(runtime_name="docker", runtime_command="docker")
        self.console = MagicMock(spec=Console)
        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name="test-container",
            console=self.console,
        )

    @patch("wrknv.container.operations.logs.stream")
    def test_get_logs_follow_streams_and_prints(self, mock_stream) -> None:
        """Test get_logs with follow=True streams each line to console (lines 53-59)."""
        mock_stream.return_value = iter(["line1\n", "line2\n", "line3\n"])

        result = self.logs.get_logs(follow=True, tail=None, since=None, timestamps=False)

        assert result is None
        assert self.console.print.call_count == 3
        # Verify each line was printed with end=""
        calls = self.console.print.call_args_list
        assert calls[0][0][0] == "line1\n"
        assert calls[0][1] == {"end": ""}

    @patch("wrknv.container.operations.logs.stream")
    def test_get_logs_follow_with_tail_and_since(self, mock_stream) -> None:
        """Test get_logs follow=True passes tail and since to stream_logs."""
        mock_stream.return_value = iter(["log line\n"])

        result = self.logs.get_logs(follow=True, tail=50, since="5m", timestamps=True)

        assert result is None
        # stream is called with a command list containing the args
        mock_stream.assert_called_once()
        cmd = mock_stream.call_args[0][0]
        assert "--tail" in cmd
        assert "50" in cmd
        assert "--since" in cmd
        assert "5m" in cmd
        assert "-t" in cmd

    @patch("wrknv.container.operations.logs.stream")
    def test_get_logs_follow_empty_stream(self, mock_stream) -> None:
        """Test get_logs follow=True with empty stream returns None."""
        mock_stream.return_value = iter([])

        result = self.logs.get_logs(follow=True, tail=None, since=None, timestamps=False)

        assert result is None
        self.console.print.assert_not_called()


@pytest.mark.container
class TestContainerLogsGetLogsError:
    """Test get_logs error handling (lines 70-77)."""

    def setup_method(self) -> None:
        self.runtime = DockerRuntime(runtime_name="docker", runtime_command="docker")
        self.console = MagicMock(spec=Console)
        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name="test-container",
            console=self.console,
        )

    @patch("wrknv.container.runtime.docker.run")
    def test_get_logs_process_error_returns_none(self, mock_run) -> None:
        """Test get_logs returns None and prints error on ProcessError (lines 70-77)."""
        mock_run.side_effect = ProcessError(
            message="container not found",
            command=["docker", "logs"],
            returncode=1,
        )

        result = self.logs.get_logs(follow=False, tail=None, since=None, timestamps=False)

        assert result is None
        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "Failed to get logs" in printed

    @patch("wrknv.container.operations.logs.stream")
    def test_get_logs_follow_process_error_returns_none(self, mock_stream) -> None:
        """Test get_logs follow=True returns None when stream raises ProcessError."""
        mock_stream.side_effect = ProcessError(
            message="streaming failed",
            command=["docker", "logs"],
            returncode=1,
        )

        result = self.logs.get_logs(follow=True, tail=None, since=None, timestamps=False)

        assert result is None


@pytest.mark.container
class TestStreamLogs:
    """Test stream_logs command construction (lines 97→99, 100, 102, 108)."""

    def setup_method(self) -> None:
        self.runtime = DockerRuntime(runtime_name="docker", runtime_command="docker")
        self.console = MagicMock(spec=Console)
        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name="test-container",
            console=self.console,
        )

    @patch("wrknv.container.operations.logs.stream")
    def test_stream_logs_with_tail(self, mock_stream) -> None:
        """Test stream_logs adds --tail when tail is provided (line 97→99)."""
        mock_stream.return_value = iter([])

        list(self.logs.stream_logs(tail=100, since=None, timestamps=False))

        cmd = mock_stream.call_args[0][0]
        assert "--tail" in cmd
        assert "100" in cmd

    @patch("wrknv.container.operations.logs.stream")
    def test_stream_logs_without_tail(self, mock_stream) -> None:
        """Test stream_logs skips --tail when tail is None."""
        mock_stream.return_value = iter([])

        list(self.logs.stream_logs(tail=None, since=None, timestamps=False))

        cmd = mock_stream.call_args[0][0]
        assert "--tail" not in cmd

    @patch("wrknv.container.operations.logs.stream")
    def test_stream_logs_with_since(self, mock_stream) -> None:
        """Test stream_logs adds --since when since is provided (line 100)."""
        mock_stream.return_value = iter([])

        list(self.logs.stream_logs(tail=None, since="10m", timestamps=False))

        cmd = mock_stream.call_args[0][0]
        assert "--since" in cmd
        assert "10m" in cmd

    @patch("wrknv.container.operations.logs.stream")
    def test_stream_logs_with_timestamps(self, mock_stream) -> None:
        """Test stream_logs adds -t when timestamps is True (line 102)."""
        mock_stream.return_value = iter([])

        list(self.logs.stream_logs(tail=None, since=None, timestamps=True))

        cmd = mock_stream.call_args[0][0]
        assert "-t" in cmd

    @patch("wrknv.container.operations.logs.stream")
    def test_stream_logs_process_error_prints_message(self, mock_stream) -> None:
        """Test stream_logs catches ProcessError and prints warning (line 108)."""
        mock_stream.side_effect = ProcessError(
            message="connection reset",
            command=["docker", "logs"],
            returncode=1,
        )

        lines = list(self.logs.stream_logs(tail=None, since=None, timestamps=False))

        assert lines == []
        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "Log streaming failed" in printed


@pytest.mark.container
class TestShowLogs:
    """Test show_logs method (lines 130-156)."""

    def setup_method(self) -> None:
        self.runtime = DockerRuntime(runtime_name="docker", runtime_command="docker")
        self.console = MagicMock(spec=Console)
        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name="test-container",
            console=self.console,
        )

    @patch("wrknv.container.runtime.docker.run")
    def test_show_logs_no_output_prints_no_logs_message(self, mock_run) -> None:
        """Test show_logs with empty result prints 'No logs found' (lines 143-145)."""
        from provide.foundation.process import CompletedProcess

        mock_run.return_value = CompletedProcess(args=["docker", "logs"], returncode=0, stdout="", stderr="")

        self.logs.show_logs(lines=None, since_minutes=None, grep=None)

        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "No logs found" in printed

    @patch("wrknv.container.runtime.docker.run")
    def test_show_logs_with_content_prints_logs(self, mock_run) -> None:
        """Test show_logs displays log content when available (lines 155-157)."""
        from provide.foundation.process import CompletedProcess

        mock_run.return_value = CompletedProcess(
            args=["docker", "logs"], returncode=0, stdout="log line 1\nlog line 2", stderr=""
        )

        self.logs.show_logs(lines=None, since_minutes=None, grep=None)

        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "log line 1" in printed

    @patch("wrknv.container.runtime.docker.run")
    def test_show_logs_with_grep_filters_lines(self, mock_run) -> None:
        """Test show_logs with grep filters matching lines (lines 148-153)."""
        from provide.foundation.process import CompletedProcess

        mock_run.return_value = CompletedProcess(
            args=["docker", "logs"],
            returncode=0,
            stdout="ERROR: something failed\nINFO: all good\nERROR: another error",
            stderr="",
        )

        self.logs.show_logs(lines=None, since_minutes=None, grep="error")

        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "ERROR: something failed" in printed
        assert "INFO: all good" not in printed

    @patch("wrknv.container.runtime.docker.run")
    def test_show_logs_grep_no_matches_prints_no_matching_message(self, mock_run) -> None:
        """Test show_logs with grep that matches nothing prints 'No matching logs' (lines 158-159)."""
        from provide.foundation.process import CompletedProcess

        mock_run.return_value = CompletedProcess(
            args=["docker", "logs"],
            returncode=0,
            stdout="INFO: all good\nDEBUG: verbose output",
            stderr="",
        )

        self.logs.show_logs(lines=None, since_minutes=None, grep="NOTPRESENT")

        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "No matching logs found" in printed

    @patch("wrknv.container.operations.logs.provide_now")
    @patch("wrknv.container.runtime.docker.run")
    def test_show_logs_with_since_minutes(self, mock_run, mock_now) -> None:
        """Test show_logs computes since timestamp when since_minutes is set (lines 131-133)."""
        from datetime import datetime

        from provide.foundation.process import CompletedProcess

        mock_now.return_value = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        mock_run.return_value = CompletedProcess(
            args=["docker", "logs"], returncode=0, stdout="recent log", stderr=""
        )

        self.logs.show_logs(lines=50, since_minutes=30, grep=None)

        # run was called with --since in the command
        cmd_args = mock_run.call_args[0][0]
        assert "--since" in cmd_args
        # Verify tail is also passed
        assert "--tail" in cmd_args
        assert "50" in cmd_args


@pytest.mark.container
class TestClearLogs:
    """Test clear_logs method (lines 167-191)."""

    def setup_method(self) -> None:
        self.runtime = DockerRuntime(runtime_name="docker", runtime_command="docker")
        self.console = MagicMock(spec=Console)
        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name="test-container",
            console=self.console,
        )

    @patch("provide.foundation.process.run")
    def test_clear_logs_success_returns_true(self, mock_run) -> None:
        """Test clear_logs returns True on success (lines 167-182)."""
        from provide.foundation.process import CompletedProcess

        mock_run.return_value = CompletedProcess(args=["sh"], returncode=0, stdout="", stderr="")

        result = self.logs.clear_logs()

        assert result is True
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        assert "sh" in cmd
        assert "-c" in cmd
        # The command should contain truncate and docker inspect
        truncate_cmd = cmd[2]
        assert "truncate" in truncate_cmd
        assert "test-container" in truncate_cmd

    @patch("provide.foundation.process.run")
    def test_clear_logs_process_error_returns_false(self, mock_run) -> None:
        """Test clear_logs returns False and prints warning on ProcessError (lines 184-191)."""
        mock_run.side_effect = ProcessError(
            message="permission denied",
            command=["sh"],
            returncode=1,
        )

        result = self.logs.clear_logs()

        assert result is False
        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "Log clearing not supported" in printed


# 🧰🌍🔚
