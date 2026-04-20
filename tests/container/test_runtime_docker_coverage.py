from __future__ import annotations

from provide.foundation.process import CompletedProcess, ProcessError
import pytest

from wrknv.container.runtime.docker import DockerRuntime


def make_runtime():
    return DockerRuntime(runtime_name="docker", runtime_command="docker")


# ---------------------------------------------------------------------------
# run_container() — extra Docker options and error path (lines 72, 74, 76, 94-102)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeRunContainer:
    def test_run_container_with_extra_options(self):
        """Covers restart, network, hostname extra options (lines 72, 74, 76)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="abc123", stderr="")
            rt.run_container(
                image="ubuntu:latest",
                name="test-c",
                detach=False,
                volumes=None,
                environment=None,
                ports=None,
                workdir=None,
                command=None,
                restart="always",
                network="host",
                hostname="myhost",
            )

        cmd = mock_run.call_args[0][0]
        assert "--restart" in cmd
        assert "always" in cmd
        assert "--network" in cmd
        assert "host" in cmd
        assert "--hostname" in cmd
        assert "myhost" in cmd

    def test_run_container_no_detach(self):
        """Covers detach=False branch (line 49->52 False path)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="abc123", stderr="")
            rt.run_container(
                image="ubuntu:latest",
                name="test-c",
                detach=False,
                volumes=None,
                environment=None,
                ports=None,
                workdir=None,
                command=None,
            )

        cmd = mock_run.call_args[0][0]
        assert "-d" not in cmd

    def test_run_container_process_error(self):
        """run_container logs and re-raises ProcessError (lines 94-102)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="no image", stderr="pull failed")
        with patch("wrknv.container.runtime.docker.run", side_effect=err), pytest.raises(ProcessError):
            rt.run_container(
                image="bad:image",
                name="test-c",
                detach=True,
                volumes=None,
                environment=None,
                ports=None,
                workdir=None,
                command=None,
            )


# ---------------------------------------------------------------------------
# start_container() — error path (lines 120-122)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeStartContainer:
    def test_start_container_process_error(self):
        """start_container logs and re-raises ProcessError (lines 110-112)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="no such container")
        with patch("wrknv.container.runtime.docker.run", side_effect=err), pytest.raises(ProcessError):
            rt.start_container("nonexistent")


# ---------------------------------------------------------------------------
# stop_container() — error path (lines 120-122)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeStopContainer:
    def test_stop_container_process_error(self):
        """stop_container logs and re-raises ProcessError (lines 120-122)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="stop failed")
        with patch("wrknv.container.runtime.docker.run", side_effect=err), pytest.raises(ProcessError):
            rt.stop_container("test-c", timeout=10)


# ---------------------------------------------------------------------------
# remove_container() — force/no-force and error (lines 126-137)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeRemoveContainer:
    def test_remove_container_no_force(self):
        """remove_container without -f flag (line 126->127 False path)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="test-c", stderr="")
            rt.remove_container("test-c", force=False)

        cmd = mock_run.call_args[0][0]
        assert "-f" not in cmd
        assert "rm" in cmd

    def test_remove_container_force(self):
        """remove_container with -f flag."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="test-c", stderr="")
            rt.remove_container("test-c", force=True)

        cmd = mock_run.call_args[0][0]
        assert "-f" in cmd

    def test_remove_container_process_error(self):
        """remove_container logs and re-raises ProcessError (lines 135-137)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="rm failed")
        with patch("wrknv.container.runtime.docker.run", side_effect=err), pytest.raises(ProcessError):
            rt.remove_container("test-c", force=False)


# ---------------------------------------------------------------------------
# container_exists() / container_running() — error path (lines 192-193, 200-201)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeContainerChecks:
    def test_container_exists_process_error(self):
        """container_exists returns False on ProcessError (lines 192-193)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="docker gone")):
            result = rt.container_exists("test-c")

        assert result is False

    def test_container_running_process_error(self):
        """container_running returns False on ProcessError (lines 200-201)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="docker gone")):
            result = rt.container_running("test-c")

        assert result is False

    def test_container_exists_empty_stdout(self):
        """container_exists returns False when stdout is None/empty."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout=None, stderr="")
            result = rt.container_exists("test-c")

        assert result is False

    def test_container_running_empty_stdout(self):
        """container_running returns False when stdout is None/empty."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout=None, stderr="")
            result = rt.container_running("test-c")

        assert result is False


# ---------------------------------------------------------------------------
# get_container_logs() — flags and error (lines 214, 215->217, 217->220, 225-227)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeGetLogs:
    def test_get_logs_all_flags(self):
        """get_container_logs with follow, tail, since (lines 214, 215->217, 217->220)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="log line", stderr="")
            rt.get_container_logs(name="test-c", follow=True, tail=50, since="5m")

        cmd = mock_run.call_args[0][0]
        assert "-f" in cmd
        assert "--tail" in cmd
        assert "50" in cmd
        assert "--since" in cmd
        assert "5m" in cmd

    def test_get_logs_no_flags(self):
        """get_container_logs with no optional flags."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="log", stderr="")
            rt.get_container_logs(name="test-c", follow=False, tail=None, since=None)

        cmd = mock_run.call_args[0][0]
        assert "-f" not in cmd
        assert "--tail" not in cmd
        assert "--since" not in cmd

    def test_get_logs_process_error(self):
        """get_container_logs logs and re-raises ProcessError (lines 225-227)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="logs failed")
        with patch("wrknv.container.runtime.docker.run", side_effect=err), pytest.raises(ProcessError):
            rt.get_container_logs(name="test-c", follow=False, tail=None, since=None)


# ---------------------------------------------------------------------------
# build_image() — error path (lines 254-261)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeBuildImage:
    def test_build_image_process_error(self):
        """build_image logs and re-raises ProcessError (lines 254-261)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="build failed")
        with patch("wrknv.container.runtime.docker.run", side_effect=err), pytest.raises(ProcessError):
            rt.build_image(
                dockerfile="Dockerfile",
                tag="myapp:latest",
                context=".",
                build_args=None,
            )


# ---------------------------------------------------------------------------
# list_containers() — error paths (lines 266->269, 272->276, 274->273, 277-279)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeListContainers:
    def test_list_containers_process_error(self):
        """list_containers returns [] on ProcessError (lines 277-279)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="fail")):
            result = rt.list_containers(all=False)

        assert result == []

    def test_list_containers_json_decode_error(self):
        """list_containers returns [] on JSONDecodeError (lines 277-279)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout="not-valid-json\nalso-not-json", stderr=""
            )
            result = rt.list_containers(all=True)

        assert result == []

    def test_list_containers_empty_lines(self):
        """list_containers skips empty lines (lines 272->276, 274->273)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout='\n{"Name":"c1"}\n\n{"Name":"c2"}\n', stderr=""
            )
            result = rt.list_containers(all=False)

        assert len(result) == 2

    def test_list_containers_no_stdout(self):
        """list_containers returns [] when stdout is empty (line 266->269 False branch)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = rt.list_containers(all=False)

        assert result == []


# ---------------------------------------------------------------------------
# inspect_container() — error paths (lines 288-291)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeInspectContainer:
    def test_inspect_process_error(self):
        """inspect_container returns {} on ProcessError (lines 288-291)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run", side_effect=ProcessError(message="inspect fail")):
            result = rt.inspect_container("test-c")

        assert result == {}

    def test_inspect_json_decode_error(self):
        """inspect_container returns {} on JSONDecodeError."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="not-json", stderr="")
            result = rt.inspect_container("test-c")

        assert result == {}

    def test_inspect_empty_list(self):
        """inspect_container returns {} when Docker returns empty JSON array."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="[]", stderr="")
            result = rt.inspect_container("test-c")

        assert result == {}

    def test_inspect_no_stdout(self):
        """inspect_container returns {} when stdout is empty."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = rt.inspect_container("test-c")

        assert result == {}


# ---------------------------------------------------------------------------
# is_available() — success and failure (lines 304-318)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestDockerRuntimeIsAvailable:
    def test_is_available_success(self):
        """is_available returns True when docker version succeeds (lines 304-315)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout="Docker version 24.0", stderr=""
            )
            result = rt.is_available()

        assert result is True

    def test_is_available_non_zero_returncode(self):
        """is_available raises ProcessError when returncode != 0 (lines 307-314)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        with patch("wrknv.container.runtime.docker.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=1, stdout="", stderr="daemon not running"
            )
            with pytest.raises((ProcessError, RuntimeError)):
                rt.is_available()

    def test_is_available_process_error(self):
        """is_available re-raises ProcessError (lines 316-318)."""
        from provide.testkit.mocking import patch

        rt = make_runtime()
        err = ProcessError(message="docker not found")
        with (
            patch("wrknv.container.runtime.docker.run", side_effect=err),
            pytest.raises((ProcessError, RuntimeError)),
        ):
            rt.is_available()
