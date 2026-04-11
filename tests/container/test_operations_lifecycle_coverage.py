# SPDX-FileCopyrightText: Copyright (c) 2026 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from unittest.mock import MagicMock, patch

from provide.foundation.process import CompletedProcess, ProcessError
import pytest
from rich.console import Console

from wrknv.container.operations.lifecycle import ContainerLifecycle
from wrknv.container.runtime.docker import DockerRuntime


def make_runtime():
    return DockerRuntime(runtime_name="docker", runtime_command="docker")


def make_lifecycle(runtime=None, container_name="test-container"):
    if runtime is None:
        runtime = make_runtime()
    return ContainerLifecycle(
        runtime=runtime,
        container_name=container_name,
        console=Console(quiet=True),
        start_emoji="[S]",
        stop_emoji="[X]",
        restart_emoji="[R]",
        status_emoji="[?]",
    )


# ---------------------------------------------------------------------------
# exists() and is_running() (lines 36, 40)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerLifecycleBasicChecks:
    def test_exists_true(self):
        """exists() returns True when container_exists returns True (line 36)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout="test-container", stderr=""
            )
            assert lc.exists() is True

    def test_exists_false(self):
        """exists() returns False when container not listed."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            assert lc.exists() is False

    def test_is_running_true(self):
        """is_running() returns True when container_running returns True (line 40)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout="test-container", stderr=""
            )
            assert lc.is_running() is True

    def test_is_running_false(self):
        """is_running() returns False when not running."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            assert lc.is_running() is False


# ---------------------------------------------------------------------------
# start() — already-running branch (line 60)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerLifecycleStart:
    def test_start_already_running(self):
        """start() returns True when container is already running (line 60)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
            ]
            result = lc.start(create_if_missing=False)

        assert result is True

    def test_start_container_no_image_no_create(self):
        """start() returns False when container missing and create_if_missing=False (lines 97-98)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            # container_exists -> False
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = lc.start(create_if_missing=False)

        assert result is False

    def test_start_container_create_missing_no_image_key(self):
        """start() returns False when create_if_missing=True but no 'image' in run_options."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = lc.start(create_if_missing=True)

        assert result is False

    def test_start_process_error(self):
        """start() catches ProcessError and returns False (lines 100-108)."""
        lc = make_lifecycle()
        err = ProcessError(message="start failed", stderr="permission denied")
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running -> False
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # start_container raises
                err,
            ]
            result = lc.start(create_if_missing=False)

        assert result is False

    def test_start_create_with_volumes_dict(self):
        """start() converts dict volumes to list format (line 78)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> False
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # run_container
                CompletedProcess(args=[], returncode=0, stdout="abc123", stderr=""),
            ]
            result = lc.start(
                create_if_missing=True,
                image="ubuntu:latest",
                volumes={"/host/path": "/container/path"},
            )

        assert result is True

    def test_start_create_with_volumes_list(self):
        """start() passes list volumes as-is (elif volumes_dict: True branch)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                CompletedProcess(args=[], returncode=0, stdout="abc123", stderr=""),
            ]
            result = lc.start(
                create_if_missing=True,
                image="ubuntu:latest",
                volumes=["/host:/container"],
            )

        assert result is True

    def test_start_create_with_volumes_none(self):
        """start() with volumes=None — elif volumes_dict: False, volumes_list stays None (line 79->82)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> False
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # run_container
                CompletedProcess(args=[], returncode=0, stdout="abc123", stderr=""),
            ]
            result = lc.start(
                create_if_missing=True,
                image="ubuntu:latest",
                volumes=None,
            )

        assert result is True

    def test_start_create_no_volumes_key(self):
        """start() with no volumes kwarg — volumes_dict defaults to {} (empty dict branch)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                CompletedProcess(args=[], returncode=0, stdout="abc123", stderr=""),
            ]
            result = lc.start(
                create_if_missing=True,
                image="ubuntu:latest",
            )

        assert result is True


# ---------------------------------------------------------------------------
# stop() — not running (line 122)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerLifecycleStop:
    def test_stop_not_running(self):
        """stop() returns True when container is not running (line 122)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = lc.stop(timeout=10)

        assert result is True

    def test_stop_process_error(self):
        """stop() catches ProcessError and returns False (lines 130-137)."""
        lc = make_lifecycle()
        err = ProcessError(message="stop failed")
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_running -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # stop_container raises
                err,
            ]
            result = lc.stop(timeout=10)

        assert result is False


# ---------------------------------------------------------------------------
# restart() — stop fails (line 152)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerLifecycleRestart:
    def test_restart_stop_fails(self):
        """restart() returns False when stop fails (line 152)."""
        lc = make_lifecycle()
        err = ProcessError(message="stop failed")
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_running check in restart -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running check in stop -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # stop_container raises
                err,
            ]
            result = lc.restart(timeout=10)

        assert result is False

    def test_restart_not_running(self):
        """restart() skips stop when container not running, then starts (line 151 False branch)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_running check in restart -> False (skip stop)
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # container_exists in start -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running in start -> False
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # start_container
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
            ]
            result = lc.restart(timeout=10)

        assert result is True


# ---------------------------------------------------------------------------
# status() — missing container and error paths (lines 184->189, 191-197)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerLifecycleStatus:
    def test_status_container_not_exists(self):
        """status() with non-existent container (line 184->189 False branch)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            # container_exists -> False
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = lc.status()

        assert result["exists"] is False
        assert result["running"] is False
        assert result["status"] == "not found"

    def test_status_process_error(self):
        """status() catches ProcessError and returns error dict (lines 191-197)."""
        runtime = MagicMock()
        runtime.container_exists.side_effect = ProcessError(message="inspect failed")
        lc = ContainerLifecycle(
            runtime=runtime,
            container_name="test-container",
            console=Console(quiet=True),
            start_emoji="[S]",
            stop_emoji="[X]",
            restart_emoji="[R]",
            status_emoji="[?]",
        )
        result = lc.status()

        assert result["exists"] is False
        assert result["status"] == "error"
        assert "error" in result

    def test_status_with_info_no_state(self):
        """status() with container info but no State key (line 184->189 partial)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # inspect_container -> info without State
                CompletedProcess(
                    args=[],
                    returncode=0,
                    stdout='[{"Id": "abc123def456", "Config": {"Image": "ubuntu:22.04"}}]',
                    stderr="",
                ),
            ]
            result = lc.status()

        assert result["exists"] is True
        assert result["id"] == "abc123def456"
        assert result["image"] == "ubuntu:22.04"
        assert "started_at" not in result


# ---------------------------------------------------------------------------
# remove() (lines 214-240)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerLifecycleRemove:
    def test_remove_not_existing(self):
        """remove() returns True when container doesn't exist (lines 215-217)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = lc.remove(force=False)

        assert result is True

    def test_remove_force_running(self):
        """remove() with force=True removes without stopping (lines 220-229)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # remove_container (force=True, skip running check)
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
            ]
            result = lc.remove(force=True)

        assert result is True

    def test_remove_not_force_not_running(self):
        """remove() with force=False and container not running (skip stop path)."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running -> False (no stop needed)
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # remove_container
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
            ]
            result = lc.remove(force=False)

        assert result is True

    def test_remove_not_force_running_stop_succeeds(self):
        """remove() with force=False, running container — stop() is called then removal proceeds."""
        lc = make_lifecycle()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running (remove's check) -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running (inside stop()) -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # stop_container succeeds
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # remove_container
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
            ]
            result = lc.remove(force=False)

        assert result is True

    def test_remove_not_force_running_stop_fails(self):
        """remove() returns False when container is running and stop() fails (line 225)."""
        lc = make_lifecycle()
        err = ProcessError(message="stop failed")
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running (remove's check) -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # container_running (inside stop()) -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # stop_container raises
                err,
            ]
            result = lc.remove(force=False)

        assert result is False

    def test_remove_process_error(self):
        """remove() catches ProcessError and returns False (lines 233-240)."""
        lc = make_lifecycle()
        err = ProcessError(message="rm failed")
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_exists -> True
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # remove_container raises (force=True skips running check)
                err,
            ]
            result = lc.remove(force=True)

        assert result is False
