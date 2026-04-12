from __future__ import annotations

from unittest.mock import patch

from provide.foundation.process import CompletedProcess, ProcessError
import pytest
from rich.console import Console

from wrknv.container.operations.exec import ContainerExec
from wrknv.container.runtime.docker import DockerRuntime


def make_runtime():
    return DockerRuntime(runtime_name="docker", runtime_command="docker")


def make_exec(runtime=None, container_name="test-container"):
    if runtime is None:
        runtime = make_runtime()
    return ContainerExec(
        runtime=runtime,
        container_name=container_name,
        console=Console(quiet=True),
        available_shells=["/bin/bash", "/bin/sh"],
        default_shell="/bin/sh",
    )


# ---------------------------------------------------------------------------
# exec() — container not running (line 63)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerExecNotRunning:
    def test_exec_container_not_running(self):
        """Returns False when container is not running (line 63)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = ex.exec(command=["ls"], interactive=False, tty=False)

        assert result is False

    def test_exec_container_not_running_no_command(self):
        """Returns False immediately when not running, even without command (line 66->77 branch)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = ex.exec(command=None, shell=None, interactive=False, tty=False)

        assert result is False


# ---------------------------------------------------------------------------
# exec() — non-interactive path (lines 94-118)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerExecNonInteractive:
    def test_exec_non_interactive_with_stdout(self):
        """Non-interactive exec prints stdout (lines 94-107)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_running check
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # exec_in_container
                CompletedProcess(args=[], returncode=0, stdout="hello output", stderr=""),
            ]
            result = ex.exec(command=["echo", "hello"], interactive=False, tty=False)

        assert result is True

    def test_exec_non_interactive_no_stdout(self):
        """Non-interactive exec with empty stdout (line 104 False branch)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
            ]
            result = ex.exec(command=["true"], interactive=False, tty=False)

        assert result is True

    def test_exec_non_interactive_process_error(self):
        """Non-interactive exec raises ProcessError (lines 109-118)."""
        ex = make_exec()
        err = ProcessError(message="exec failed", stderr="container error")
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_running
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # exec fails
                err,
            ]
            result = ex.exec(command=["bad-cmd"], interactive=False, tty=False)

        assert result is False

    def test_exec_with_shell_specified(self):
        """exec() with explicit shell but command=None (line 66->77)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
            ]
            result = ex.exec(command=None, shell="/bin/bash", interactive=False, tty=False)

        assert result is True

    def test_exec_command_none_no_shell_detects_shell(self):
        """exec() with command=None and shell=None triggers _detect_shell (line 68->71)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.side_effect = [
                # container_running
                CompletedProcess(args=[], returncode=0, stdout="test-container", stderr=""),
                # _detect_shell: test -f /bin/bash succeeds
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
                # exec_in_container call with ['/bin/bash']
                CompletedProcess(args=[], returncode=0, stdout="", stderr=""),
            ]
            result = ex.exec(command=None, shell=None, interactive=False, tty=False)

        assert result is True


# ---------------------------------------------------------------------------
# run_command() — capture_output=False and error paths (lines 165-180)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerExecRunCommand:
    def test_run_command_no_capture_with_stdout(self):
        """run_command with capture_output=False prints stdout (lines 165-168)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="some output", stderr="")
            result = ex.run_command(command=["ls"], capture_output=False)

        assert result is None

    def test_run_command_no_capture_no_stdout(self):
        """run_command with capture_output=False and no stdout (line 165 False branch)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = ex.run_command(command=["true"], capture_output=False)

        assert result is None

    def test_run_command_process_error_with_capture(self):
        """run_command ProcessError when capture_output=True returns None (lines 170-178)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="fail")):
            result = ex.run_command(command=["bad"], capture_output=True)

        assert result is None

    def test_run_command_process_error_no_capture(self):
        """run_command ProcessError when capture_output=False prints error (lines 170-180)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="fail")):
            result = ex.run_command(command=["bad"], capture_output=False)

        assert result is None


# ---------------------------------------------------------------------------
# _detect_shell() — fallback to default (line 206)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerExecDetectShell:
    def test_detect_shell_all_fail_returns_default(self):
        """_detect_shell returns default_shell when all shells fail (line 206)."""
        ex = make_exec()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="not found")):
            result = ex._detect_shell()

        assert result == "/bin/sh"


# ---------------------------------------------------------------------------
# _build_exec_command_list() — optional args (lines 232-242)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerExecBuildCommandList:
    def test_build_exec_command_list_all_options(self):
        """Covers user, workdir, environment branches (lines 237, 239, 242)."""
        ex = make_exec()
        cmd = ex._build_exec_command_list(
            command=["bash"],
            interactive=True,
            tty=True,
            user="root",
            workdir="/app",
            environment={"KEY": "VAL"},
        )

        assert "-i" in cmd
        assert "-t" in cmd
        assert "-u" in cmd
        assert "root" in cmd
        assert "-w" in cmd
        assert "/app" in cmd
        assert "-e" in cmd
        assert "KEY=VAL" in cmd
        assert "test-container" in cmd
        assert "bash" in cmd

    def test_build_exec_command_list_no_optional(self):
        """Covers False branches for user, workdir, environment."""
        ex = make_exec()
        cmd = ex._build_exec_command_list(
            command=["ls"],
            interactive=False,
            tty=False,
            user=None,
            workdir=None,
            environment=None,
        )

        assert "-i" not in cmd
        assert "-t" not in cmd
        assert "-u" not in cmd
        assert "-w" not in cmd
        assert "-e" not in cmd
        assert "ls" in cmd
