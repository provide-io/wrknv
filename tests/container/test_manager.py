from __future__ import annotations

from provide.testkit import FoundationTestCase
import pytest

#!/usr/bin/env python3
#
# tests/test_container_manager.py
#
"""
Comprehensive tests for the ContainerManager class.
"""

from pathlib import Path
import shutil
import subprocess
from unittest.mock import Mock, patch

from wrknv.container.manager import ContainerManager
from wrknv.container.operations.lifecycle import ContainerLifecycle
from wrknv.container.runtime.docker import DockerRuntime
from wrknv.wenv.schema import WorkenvConfig


@pytest.mark.container
class TestContainerManager(FoundationTestCase):
    """Test suite for ContainerManager class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.config = WorkenvConfig(project_name="test-project")
        self.manager = ContainerManager(self.config)

    def teardown_method(self) -> None:
        """Clean up after tests."""
        # Clean up any test directories
        test_build_dir = Path.home() / ".wrknv" / "container-build"
        if test_build_dir.exists():
            shutil.rmtree(test_build_dir, ignore_errors=True)

    @patch.object(DockerRuntime, "is_available", return_value=True)
    def test_check_docker_success(self, mock_is_available) -> None:
        """Test check_docker when Docker is available and running."""
        result = self.manager.check_docker()
        assert result
        assert mock_is_available.called

    @patch.object(DockerRuntime, "is_available", return_value=False)
    def test_check_docker_daemon_not_running(self, mock_is_available) -> None:
        """Test check_docker when Docker daemon is not running."""
        result = self.manager.check_docker()
        assert not result

    @patch.object(DockerRuntime, "is_available", return_value=False)
    def test_check_docker_not_installed(self, mock_is_available) -> None:
        """Test check_docker when Docker is not installed."""
        result = self.manager.check_docker()
        assert not result

    @patch.object(ContainerLifecycle, "exists", return_value=True)
    def test_container_exists_true(self, mock_exists) -> None:
        """Test container_exists when container exists."""
        result = self.manager.container_exists()
        assert result
        assert mock_exists.called

    @patch.object(ContainerLifecycle, "exists", return_value=False)
    def test_container_exists_false(self, mock_exists) -> None:
        """Test container_exists when container doesn't exist."""
        result = self.manager.container_exists()
        assert not result

    @patch.object(ContainerLifecycle, "is_running", return_value=True)
    def test_container_running_true(self, mock_is_running) -> None:
        """Test container_running when container is running."""
        result = self.manager.container_running()
        assert result
        assert mock_is_running.called

    @patch.object(ContainerLifecycle, "is_running", return_value=False)
    def test_container_running_false(self, mock_is_running) -> None:
        """Test container_running when container is not running."""
        result = self.manager.container_running()
        assert not result

    @patch("provide.foundation.process.run_command")
    def test_image_exists_true(self, mock_run) -> None:
        """Test image_exists when image exists."""
        mock_run.return_value = Mock(returncode=0, stdout="test-project-dev:latest\nother:tag\n")

        result = self.manager.image_exists()

        assert result
        # Verify docker images was called (don't check exact kwargs)
        assert mock_run.called

    @patch("provide.foundation.process.run_command")
    def test_image_exists_false(self, mock_run) -> None:
        """Test image_exists when image doesn't exist."""
        mock_run.return_value = Mock(returncode=0, stdout="other:tag\n")

        result = self.manager.image_exists()

        assert not result

    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    def test_build_image_success(self, mock_mkdir, mock_write) -> None:
        """Test successful image build."""
        # Replace the entire builder with a mock (attrs objects are read-only)
        from tests.utils.fixtures import create_mock_builder

        mock_builder = create_mock_builder()
        self.manager.builder = mock_builder

        result = self.manager.build_image()

        assert result
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_write.assert_called_once()
        # Verify dockerfile content was generated
        dockerfile_content = mock_write.call_args[0][0]
        assert "FROM ubuntu:22.04" in dockerfile_content
        # Verify builder.build was called
        mock_builder.build.assert_called_once()

    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    def test_build_image_with_rebuild(self, mock_mkdir, mock_write) -> None:
        """Test image build with rebuild flag."""
        # Replace the entire builder with a mock (attrs objects are read-only)
        from tests.utils.fixtures import create_mock_builder

        mock_builder = create_mock_builder()
        self.manager.builder = mock_builder

        result = self.manager.build_image(rebuild=True)

        assert result
        # Verify builder.build was called
        mock_builder.build.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    def test_build_image_failure(self, mock_mkdir, mock_write, mock_run) -> None:
        """Test image build failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "docker build")

        result = self.manager.build_image()

        assert not result
        # Build directory is now persistent, no cleanup

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    @patch("wrknv.container.manager.ContainerManager.build_image")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("provide.foundation.process.run_command")
    @patch("os.getuid")
    @patch("os.getgid")
    def test_start_container_success(
        self,
        mock_getgid,
        mock_getuid,
        mock_run,
        mock_exists,
        mock_running,
        mock_build,
        mock_image_exists,
        mock_check_docker,
    ) -> None:
        """Test successful container start."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = True
        mock_running.return_value = False
        mock_exists.return_value = False
        mock_getuid.return_value = 1000
        mock_getgid.return_value = 1000

        result = self.manager.start()

        assert result
        mock_check_docker.assert_called_once()
        mock_image_exists.assert_called_once()
        mock_running.assert_called_once()
        # Verify docker run command
        docker_run_cmd = mock_run.call_args[0][0]
        assert docker_run_cmd[0] == "docker"
        assert docker_run_cmd[1] == "run"
        assert "-d" in docker_run_cmd
        assert "--name" in docker_run_cmd
        assert "test-project-dev" in docker_run_cmd

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    def test_start_container_docker_not_available(self, mock_check_docker) -> None:
        """Test container start when Docker is not available."""
        mock_check_docker.return_value = False

        result = self.manager.start()

        assert not result

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    @patch("wrknv.container.manager.ContainerManager.build_image")
    def test_start_container_build_image_if_missing(
        self, mock_build, mock_image_exists, mock_check_docker
    ) -> None:
        """Test that start builds image if it doesn't exist."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = False
        mock_build.return_value = False  # Build fails

        result = self.manager.start()

        assert not result
        mock_build.assert_called_once_with(rebuild=False)

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    def test_start_container_already_running(self, mock_running, mock_image_exists, mock_check_docker) -> None:
        """Test start when container is already running."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = True
        mock_running.return_value = True

        result = self.manager.start()

        assert result  # Returns True but doesn't try to start again

    def test_enter_container_running(self) -> None:
        """Test entering a running container."""
        mock_exec = Mock()
        mock_exec.enter = Mock(return_value=True)
        self.manager.exec = mock_exec

        result = self.manager.enter()

        assert result is True
        mock_exec.enter.assert_called_once_with(command=None, user=None, workdir=None, environment=None)

    def test_enter_container_with_command(self) -> None:
        """Test entering container with specific command."""
        mock_exec = Mock()
        mock_exec.enter = Mock(return_value=True)
        self.manager.exec = mock_exec

        result = self.manager.enter(command="ls -la")

        assert result is True
        mock_exec.enter.assert_called_once_with(command="ls -la", user=None, workdir=None, environment=None)

    def test_enter_container_not_running(self) -> None:
        """Test entering when container is not running."""
        mock_exec = Mock()
        mock_exec.enter = Mock(return_value=False)
        self.manager.exec = mock_exec

        result = self.manager.enter()

        assert result is False
        mock_exec.enter.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    def test_stop_container_success(self, mock_running, mock_run) -> None:
        """Test successful container stop."""
        mock_running.return_value = True
        mock_run.return_value = Mock(returncode=0)

        result = self.manager.stop()

        assert result
        # Check that docker stop was called
        stop_calls = [c for c in mock_run.call_args_list if "stop" in str(c)]
        assert len(stop_calls) > 0

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    def test_stop_container_failure(self, mock_running, mock_run) -> None:
        """Test container stop failure."""
        mock_running.return_value = True
        mock_run.side_effect = subprocess.CalledProcessError(1, "docker stop")

        result = self.manager.stop()

        assert not result

    @patch("wrknv.container.manager.ContainerManager.stop")
    @patch("wrknv.container.manager.ContainerManager.start")
    def test_restart_container_success(self, mock_start, mock_stop) -> None:
        """Test successful container restart."""
        mock_stop.return_value = True
        mock_start.return_value = True

        result = self.manager.restart()

        assert result
        mock_stop.assert_called_once()
        mock_start.assert_called_once()

    @patch("wrknv.container.manager.ContainerManager.start")
    @patch("wrknv.container.manager.ContainerManager.stop")
    def test_restart_container_stop_failure(self, mock_stop, mock_start) -> None:
        """Test restart when stop fails."""
        mock_stop.return_value = False

        result = self.manager.restart()

        assert result  # restart continues even if stop fails
        mock_start.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    @patch("wrknv.container.manager.ContainerManager.check_docker")
    def test_status_method(self, mock_docker, mock_image, mock_exists, mock_running, mock_run) -> None:
        """Test getting container status."""
        mock_docker.return_value = True
        mock_image.return_value = True
        mock_exists.return_value = True
        mock_running.return_value = True
        mock_run.return_value = Mock(
            returncode=0,
            stdout='[{"Id": "abc123456789", "Created": "2024-01-01", "State": {"Status": "running"}, "NetworkSettings": {"Ports": {}}}]',
        )

        status = self.manager.status()

        assert status is not None
        assert status["docker_available"]
        assert status["container_exists"]
        assert status["container_info"]["state"] == "running"
        mock_run.assert_called_once_with(
            ["docker", "inspect", "test-project-dev"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    def test_status_no_docker(self, mock_check) -> None:
        """Test getting status when Docker is not available."""
        mock_check.return_value = False

        status = self.manager.status()

        assert status is not None
        assert not status["docker_available"]
        assert not status["container_exists"]

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    def test_logs_method(self, mock_exists, mock_run) -> None:
        """Test getting container logs."""
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0, stdout="logs", stderr="")

        self.manager.get_logs(follow=False, lines=10)

        mock_run.assert_called_once_with(["docker", "logs", "--tail", "10", "test-project-dev"], check=True)

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    def test_logs_follow(self, mock_exists, mock_run) -> None:
        """Test following container logs."""
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0)

        self.manager.get_logs(follow=True)

        mock_run.assert_called_once_with(["docker", "logs", "-f", "test-project-dev"], check=True)

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    def test_clean_success(self, mock_image_exists, mock_container_exists, mock_running, mock_run) -> None:
        """Test successful cleanup."""
        mock_running.return_value = False
        mock_container_exists.side_effect = [True, False]  # Exists first, then doesn't after rm
        mock_image_exists.side_effect = [True, False]  # Exists first, then doesn't after rmi
        mock_run.return_value = Mock(returncode=0)

        result = self.manager.clean()

        assert result
        # Should call both rm and rmi
        rm_calls = [c for c in mock_run.call_args_list if "rm" in str(c)]
        rmi_calls = [c for c in mock_run.call_args_list if "rmi" in str(c)]
        assert len(rm_calls > 0)
        assert len(rmi_calls > 0)

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    def test_clean_partial_failure(
        self, mock_image_exists, mock_container_exists, mock_running, mock_run
    ) -> None:
        """Test cleanup with partial failure."""
        mock_running.return_value = False
        mock_container_exists.return_value = True
        mock_image_exists.return_value = False
        # Container removal fails
        mock_run.side_effect = subprocess.CalledProcessError(1, "docker rm")

        result = self.manager.clean()

        assert not result  # Returns False if container removal fails

    def test_generate_dockerfile(self) -> None:
        """Test Dockerfile generation."""
        dockerfile = self.manager._generate_dockerfile()

        # Check for essential components
        assert "FROM ubuntu:22.04" in dockerfile
        assert "DEBIAN_FRONTEND=noninteractive" in dockerfile
        assert "apt-get update" in dockerfile
        assert "python3" in dockerfile
        assert "curl -LsSf https://astral.sh/uv/install.sh" in dockerfile
        assert "/workspace" in dockerfile
        assert "zsh" in dockerfile

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("provide.foundation.process.run_command")
    def test_start_removes_stopped_container(
        self, mock_run, mock_exists, mock_image_exists, mock_check_docker
    ) -> None:
        """Test that start removes existing stopped container."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = True
        mock_exists.return_value = True  # Container exists but not running

        with patch("wrknv.container.manager.ContainerManager.container_running") as mock_running:
            mock_running.return_value = False

            self.manager.start()

            # Check that docker rm was called
            rm_calls = [c for c in mock_run.call_args_list if c[0][0][:2] == ["docker", "rm"]]
            assert len(rm_calls) == 1
            assert rm_calls[0][0][0] == ["docker", "rm", "test-project-dev"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
