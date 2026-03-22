#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for container.shell_commands - uncovered branches."""

from __future__ import annotations

from provide.testkit.mocking import Mock, patch
import pytest

from wrknv.config import WorkenvConfig
from wrknv.container.shell_commands import (
    exec_in_container,
    get_container_logs,
    get_container_stats,
    shell_into_container,
    stream_container_logs,
)
from wrknv.wenv.schema import ContainerConfig


def _enabled_config() -> WorkenvConfig:
    return WorkenvConfig(
        project_name="test-project",
        container=ContainerConfig(enabled=True),
    )


def _disabled_config() -> WorkenvConfig:
    return WorkenvConfig(project_name="test-project")


@pytest.mark.container
class TestShellIntoContainerCoverage:
    """Cover missing branches in shell_into_container."""

    def test_container_not_enabled_returns_false(self) -> None:
        """Line 46: return False when container not enabled."""
        result = shell_into_container(_disabled_config())
        assert result is False

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_container_does_not_exist_returns_false(self, mock_cls) -> None:
        """Line 55: return False when container doesn't exist."""
        mock_mgr = Mock()
        mock_mgr.container_running.return_value = False
        mock_mgr.container_exists.return_value = False
        mock_cls.return_value = mock_mgr

        result = shell_into_container(_enabled_config())
        assert result is False

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_auto_start_fails_returns_false(self, mock_cls) -> None:
        """Line 63: return False when auto_start is True but start() fails."""
        mock_mgr = Mock()
        mock_mgr.container_running.return_value = False
        mock_mgr.container_exists.return_value = True
        mock_mgr.start.return_value = False
        mock_cls.return_value = mock_mgr

        result = shell_into_container(_enabled_config(), auto_start=True)
        assert result is False

    @patch("wrknv.container.shell_commands.run", side_effect=KeyboardInterrupt)
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_keyboard_interrupt_returns_true(self, mock_cls, mock_run) -> None:
        """Lines 91-93: KeyboardInterrupt during shell returns True."""
        mock_mgr = Mock()
        mock_mgr.container_name = "test-project-dev"
        mock_mgr.container_running.return_value = True
        mock_cls.return_value = mock_mgr

        result = shell_into_container(_enabled_config())
        assert result is True

    @patch("wrknv.container.shell_commands.run", side_effect=RuntimeError("docker failed"))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exception_returns_false(self, mock_cls, mock_run) -> None:
        """Lines 94-97: generic exception during shell returns False."""
        mock_mgr = Mock()
        mock_mgr.container_name = "test-project-dev"
        mock_mgr.container_running.return_value = True
        mock_cls.return_value = mock_mgr

        result = shell_into_container(_enabled_config())
        assert result is False


@pytest.mark.container
class TestExecInContainerCoverage:
    """Cover missing branches in exec_in_container."""

    def test_container_not_enabled_returns_none(self) -> None:
        """Line 126: return None when container not enabled."""
        result = exec_in_container(_disabled_config(), ["echo", "hi"])
        assert result is None

    @patch("wrknv.container.shell_commands.run", side_effect=RuntimeError("exec failed"))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exception_returns_none(self, mock_cls, mock_run) -> None:
        """Lines 170-173: exception during exec returns None."""
        mock_mgr = Mock()
        mock_mgr.container_name = "test-project-dev"
        mock_mgr.container_running.return_value = True
        mock_cls.return_value = mock_mgr

        result = exec_in_container(_enabled_config(), ["echo", "hi"])
        assert result is None


@pytest.mark.container
class TestGetContainerLogsCoverage:
    """Cover missing branches in get_container_logs."""

    def test_container_not_enabled_returns_none(self) -> None:
        """Line 200: return None when container not enabled."""
        result = get_container_logs(_disabled_config())
        assert result is None

    @patch("wrknv.container.shell_commands.run")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_nonzero_exit_returns_none(self, mock_cls, mock_run) -> None:
        """Line 242: return None when docker logs returns non-zero."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr
        mock_run.return_value = Mock(returncode=1, stderr="error", stdout="")

        result = get_container_logs(_enabled_config())
        assert result is None

    @patch("wrknv.container.shell_commands.run", side_effect=RuntimeError("logs failed"))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exception_returns_none(self, mock_cls, mock_run) -> None:
        """Lines 245-248: exception during get_container_logs returns None."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = get_container_logs(_enabled_config())
        assert result is None


@pytest.mark.container
class TestStreamContainerLogsCoverage:
    """Cover missing branches in stream_container_logs."""

    def test_container_not_enabled_returns_false(self) -> None:
        """Lines 267-271: return False when container not enabled."""
        result = stream_container_logs(_disabled_config())
        assert result is False

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_container_does_not_exist_returns_false(self, mock_cls) -> None:
        """Lines 276-278: return False when container doesn't exist."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = False
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = stream_container_logs(_enabled_config())
        assert result is False

    @patch("wrknv.container.shell_commands.stream", return_value=iter(["line1\n", "match\n"]))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_streams_logs_with_filter(self, mock_cls, mock_stream) -> None:
        """Lines 283-309: stream logs with filter_pattern."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = stream_container_logs(_enabled_config(), filter_pattern="match")
        assert result is True

    @patch("wrknv.container.shell_commands.stream", return_value=iter(["highlighted\n"]))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_streams_logs_with_highlight(self, mock_cls, mock_stream) -> None:
        """Line 297: highlight_pattern re.sub is called."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = stream_container_logs(_enabled_config(), highlight_pattern="highlighted")
        assert result is True

    @patch("wrknv.container.shell_commands.stream", side_effect=KeyboardInterrupt)
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_keyboard_interrupt_returns_true(self, mock_cls, mock_stream) -> None:
        """Lines 301-303: KeyboardInterrupt during streaming returns True."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = stream_container_logs(_enabled_config())
        assert result is True

    @patch("wrknv.container.shell_commands.stream", side_effect=RuntimeError("stream failed"))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exception_returns_false(self, mock_cls, mock_stream) -> None:
        """Lines 304-307: exception during streaming returns False."""
        mock_mgr = Mock()
        mock_mgr.container_exists.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = stream_container_logs(_enabled_config())
        assert result is False


@pytest.mark.container
class TestGetContainerStatsCoverage:
    """Cover missing branches in get_container_stats."""

    def test_container_not_enabled_returns_none(self) -> None:
        """Lines 324-325: return None when container not enabled."""
        result = get_container_stats(_disabled_config())
        assert result is None

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_container_not_running_returns_none(self, mock_cls) -> None:
        """Lines 330-331: return None when container not running."""
        mock_mgr = Mock()
        mock_mgr.container_running.return_value = False
        mock_cls.return_value = mock_mgr

        result = get_container_stats(_enabled_config())
        assert result is None

    @patch("wrknv.container.shell_commands.run")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_returns_stats_dict(self, mock_cls, mock_run) -> None:
        """Lines 333-351: return parsed stats dict on success."""
        import json

        mock_mgr = Mock()
        mock_mgr.container_running.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr
        stats_json = json.dumps({
            "Name": "test-project-dev",
            "CPUPerc": "0.5%",
            "MemUsage": "100MiB / 2GiB",
            "MemPerc": "5%",
            "NetIO": "1kB / 500B",
            "BlockIO": "0B / 0B",
            "PIDs": "5",
        })
        mock_run.return_value = Mock(returncode=0, stdout=stats_json)

        result = get_container_stats(_enabled_config())
        assert result is not None
        assert result["cpu"] == "0.5%"
        assert result["pids"] == "5"

    @patch("wrknv.container.shell_commands.run", side_effect=RuntimeError("stats failed"))
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exception_returns_none(self, mock_cls, mock_run) -> None:
        """Lines 352-355: exception during get_container_stats returns None."""
        mock_mgr = Mock()
        mock_mgr.container_running.return_value = True
        mock_mgr.container_name = "test-project-dev"
        mock_cls.return_value = mock_mgr

        result = get_container_stats(_enabled_config())
        assert result is None


# 🧰🌍🔚
