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

import shutil
import subprocess
from pathlib import Path
from unittest.mock import Mock, patch

from wrknv.container.manager import ContainerManager
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

    @patch("provide.foundation.process.run_command")
    def test_check_docker_success(self, mock_run):
        """Test check_docker when Docker is available and running."""
        mock_run.return_value = Mock(returncode=0)

        result = self.manager.check_docker()

        assert result
        mock_run.assert_called_once_with(["docker", "info"], capture_output=True, text=True, check=False)

    @patch("provide.foundation.process.run_command")
    def test_check_docker_daemon_not_running(self, mock_run):
        """Test check_docker when Docker daemon is not running."""
        mock_run.return_value = Mock(returncode=1)

        result = self.manager.check_docker()

        assert not result

    @patch("provide.foundation.process.run_command")
    def test_check_docker_not_installed(self, mock_run):
        """Test check_docker when Docker is not installed."""
        mock_run.side_effect = FileNotFoundError()

        result = self.manager.check_docker()

        assert not result

    @patch("provide.foundation.process.run_command")
    def test_container_exists_true(self, mock_run):
        """Test container_exists when container exists."""
        mock_run.return_value = Mock(returncode=0, stdout="test-project-dev\nother-container\n")

        result = self.manager.container_exists()

        assert result
        mock_run.assert_called_once_with(
            ["docker", "ps", "-a", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("provide.foundation.process.run_command")
    def test_container_exists_false(self, mock_run):
        """Test container_exists when container doesn't exist."""
        mock_run.return_value = Mock(returncode=0, stdout="other-container\n")

        result = self.manager.container_exists()

        assert not result

    @patch("provide.foundation.process.run_command")
    def test_container_running_true(self, mock_run):
        """Test container_running when container is running."""
        mock_run.return_value = Mock(returncode=0, stdout="test-project-dev\n")

        result = self.manager.container_running()

        assert result
        mock_run.assert_called_once_with(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("provide.foundation.process.run_command")
    def test_container_running_false(self, mock_run):
        """Test container_running when container is not running."""
        mock_run.return_value = Mock(returncode=0, stdout="")

        result = self.manager.container_running()

        assert not result

    @patch("provide.foundation.process.run_command")
    def test_image_exists_true(self, mock_run):
        """Test image_exists when image exists."""
        mock_run.return_value = Mock(returncode=0, stdout="test-project-dev:latest\nother:tag\n")

        result = self.manager.image_exists()

        assert result
        mock_run.assert_called_once_with(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("provide.foundation.process.run_command")
    def test_image_exists_false(self, mock_run):
        """Test image_exists when image doesn't exist."""
        mock_run.return_value = Mock(returncode=0, stdout="other:tag\n")

        result = self.manager.image_exists()

        assert not result

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    def test_build_image_success(self, mock_mkdir, mock_write, mock_run):
        """Test successful image build."""
        mock_run.return_value = Mock(returncode=0)

        result = self.manager.build_image()

        assert result
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_write.assert_called_once()
        # Verify dockerfile content was generated
        dockerfile_content = mock_write.call_args[0][0]
        assert "FROM ubuntu:22.04" in dockerfile_content
        # Build directory is now persistent, no cleanup

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    def test_build_image_with_rebuild(self, mock_mkdir, mock_write, mock_run):
        """Test image build with rebuild flag."""
        mock_run.return_value = Mock(returncode=0)

        result = self.manager.build_image(rebuild=True)

        assert result
        # Check that --no-cache was added to the command
        build_cmd = mock_run.call_args[0][0]
        assert "--no-cache" in build_cmd

    @patch("provide.foundation.process.run_command")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    def test_build_image_failure(self, mock_mkdir, mock_write, mock_run):
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
    ):
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
    def test_start_container_docker_not_available(self, mock_check_docker):
        """Test container start when Docker is not available."""
        mock_check_docker.return_value = False

        result = self.manager.start()

        assert not result

    @patch("wrknv.container.manager.ContainerManager.check_docker")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    @patch("wrknv.container.manager.ContainerManager.build_image")
    def test_start_container_build_image_if_missing(self, mock_build, mock_image_exists, mock_check_docker):
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
    def test_start_container_already_running(self, mock_running, mock_image_exists, mock_check_docker):
        """Test start when container is already running."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = True
        mock_running.return_value = True

        result = self.manager.start()

        assert result  # Returns True but doesn't try to start again

    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("os.system")
    def test_enter_container_running(self, mock_system, mock_running):
        """Test entering a running container."""
        mock_running.return_value = True

        self.manager.enter()

        mock_system.assert_called_once_with("docker exec -it test-project-dev /bin/bash")

    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("os.system")
    def test_enter_container_with_command(self, mock_system, mock_running):
        """Test entering container with specific command."""
        mock_running.return_value = True

        self.manager.enter(["ls", "-la"])

        mock_system.assert_called_once_with("docker exec -it test-project-dev ls -la")

    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("os.system")
    def test_enter_container_not_running(self, mock_system, mock_running):
        """Test entering when container is not running."""
        mock_running.return_value = False

        self.manager.enter()

        mock_system.assert_not_called()

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    def test_stop_container_success(self, mock_running, mock_run):
        """Test successful container stop."""
        mock_running.return_value = True
        mock_run.return_value = Mock(returncode=0)

        result = self.manager.stop()

        assert result
        # Check that docker stop was called
        stop_calls = [c for c in mock_run.call_args_list if "stop" in str(c)]
        assert len(stop_calls > 0)

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    def test_stop_container_failure(self, mock_running, mock_run):
        """Test container stop failure."""
        mock_running.return_value = True
        mock_run.side_effect = subprocess.CalledProcessError(1, "docker stop")

        result = self.manager.stop()

        assert not result

    @patch("wrknv.container.manager.ContainerManager.stop")
    @patch("wrknv.container.manager.ContainerManager.start")
    def test_restart_container_success(self, mock_start, mock_stop):
        """Test successful container restart."""
        mock_stop.return_value = True
        mock_start.return_value = True

        result = self.manager.restart()

        assert result
        mock_stop.assert_called_once()
        mock_start.assert_called_once()

    @patch("wrknv.container.manager.ContainerManager.start")
    @patch("wrknv.container.manager.ContainerManager.stop")
    def test_restart_container_stop_failure(self, mock_stop, mock_start):
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
    def test_status_method(self, mock_docker, mock_image, mock_exists, mock_running, mock_run):
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
    def test_status_no_docker(self, mock_check):
        """Test getting status when Docker is not available."""
        mock_check.return_value = False

        status = self.manager.status()

        assert status is not None
        assert not status["docker_available"]
        assert not status["container_exists"]

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    def test_logs_method(self, mock_exists, mock_run):
        """Test getting container logs."""
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0, stdout="logs", stderr="")

        self.manager.logs(follow=False, tail=10)

        mock_run.assert_called_once_with(
            ["docker", "logs", "--tail", "10", "test-project-dev"], capture_output=True, text=True
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    def test_logs_follow(self, mock_exists, mock_run):
        """Test following container logs."""
        mock_exists.return_value = True
        mock_run.return_value = Mock(returncode=0)

        self.manager.logs(follow=True)

        mock_run.assert_called_once_with(["docker", "logs", "-f", "--tail", "100", "test-project-dev"])

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    def test_clean_success(self, mock_image_exists, mock_container_exists, mock_running, mock_run):
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
    def test_clean_partial_failure(self, mock_image_exists, mock_container_exists, mock_running, mock_run):
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
    ):
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
