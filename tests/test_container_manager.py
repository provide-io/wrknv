#!/usr/bin/env python3
#
# tests/test_container_manager.py
#
"""
Comprehensive tests for the ContainerManager class.
"""

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, Mock, call, patch

from wrkenv.container.manager import ContainerManager
from wrkenv.env.config import WorkenvConfig


class TestContainerManager(unittest.TestCase):
    """Test suite for ContainerManager class."""

    def setUp(self):
        """Set up test fixtures."""
        self.config = WorkenvConfig()
        self.manager = ContainerManager(self.config)

    def tearDown(self):
        """Clean up after tests."""
        # Clean up any test directories
        test_build_dir = Path.home() / ".wrkenv" / "container-build"
        if test_build_dir.exists():
            shutil.rmtree(test_build_dir, ignore_errors=True)

    @patch("subprocess.run")
    def test_check_docker_success(self, mock_run):
        """Test check_docker when Docker is available and running."""
        mock_run.return_value = Mock(returncode=0)
        
        result = self.manager.check_docker()
        
        self.assertTrue(result)
        mock_run.assert_called_once_with(
            ["docker", "info"], capture_output=True, text=True, check=False
        )

    @patch("subprocess.run")
    def test_check_docker_daemon_not_running(self, mock_run):
        """Test check_docker when Docker daemon is not running."""
        mock_run.return_value = Mock(returncode=1)
        
        result = self.manager.check_docker()
        
        self.assertFalse(result)

    @patch("subprocess.run")
    def test_check_docker_not_installed(self, mock_run):
        """Test check_docker when Docker is not installed."""
        mock_run.side_effect = FileNotFoundError()
        
        result = self.manager.check_docker()
        
        self.assertFalse(result)

    @patch("subprocess.run")
    def test_container_exists_true(self, mock_run):
        """Test container_exists when container exists."""
        mock_run.return_value = Mock(
            returncode=0, stdout="wrkenv-dev\nother-container\n"
        )
        
        result = self.manager.container_exists()
        
        self.assertTrue(result)
        mock_run.assert_called_once_with(
            ["docker", "ps", "-a", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("subprocess.run")
    def test_container_exists_false(self, mock_run):
        """Test container_exists when container doesn't exist."""
        mock_run.return_value = Mock(returncode=0, stdout="other-container\n")
        
        result = self.manager.container_exists()
        
        self.assertFalse(result)

    @patch("subprocess.run")
    def test_container_running_true(self, mock_run):
        """Test container_running when container is running."""
        mock_run.return_value = Mock(returncode=0, stdout="wrkenv-dev\n")
        
        result = self.manager.container_running()
        
        self.assertTrue(result)
        mock_run.assert_called_once_with(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("subprocess.run")
    def test_container_running_false(self, mock_run):
        """Test container_running when container is not running."""
        mock_run.return_value = Mock(returncode=0, stdout="")
        
        result = self.manager.container_running()
        
        self.assertFalse(result)

    @patch("subprocess.run")
    def test_image_exists_true(self, mock_run):
        """Test image_exists when image exists."""
        mock_run.return_value = Mock(
            returncode=0, stdout="wrkenv-dev:latest\nother:tag\n"
        )
        
        result = self.manager.image_exists()
        
        self.assertTrue(result)
        mock_run.assert_called_once_with(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("subprocess.run")
    def test_image_exists_false(self, mock_run):
        """Test image_exists when image doesn't exist."""
        mock_run.return_value = Mock(returncode=0, stdout="other:tag\n")
        
        result = self.manager.image_exists()
        
        self.assertFalse(result)

    @patch("subprocess.run")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    @patch("shutil.rmtree")
    def test_build_image_success(self, mock_rmtree, mock_mkdir, mock_write, mock_run):
        """Test successful image build."""
        mock_run.return_value = Mock(returncode=0)
        
        result = self.manager.build_image()
        
        self.assertTrue(result)
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_write.assert_called_once()
        # Verify dockerfile content was generated
        dockerfile_content = mock_write.call_args[0][0]
        self.assertIn("FROM ubuntu:22.04", dockerfile_content)
        self.assertIn("docker.io", dockerfile_content)
        # Verify cleanup was called
        mock_rmtree.assert_called_once()

    @patch("subprocess.run")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    @patch("shutil.rmtree")
    def test_build_image_with_rebuild(self, mock_rmtree, mock_mkdir, mock_write, mock_run):
        """Test image build with rebuild flag."""
        mock_run.return_value = Mock(returncode=0)
        
        result = self.manager.build_image(rebuild=True)
        
        self.assertTrue(result)
        # Check that --no-cache was added to the command
        build_cmd = mock_run.call_args[0][0]
        self.assertIn("--no-cache", build_cmd)

    @patch("subprocess.run")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.mkdir")
    @patch("shutil.rmtree")
    def test_build_image_failure(self, mock_rmtree, mock_mkdir, mock_write, mock_run):
        """Test image build failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "docker build")
        
        result = self.manager.build_image()
        
        self.assertFalse(result)
        # Ensure cleanup still happens
        mock_rmtree.assert_called_once()

    @patch("wrkenv.container.manager.ContainerManager.check_docker")
    @patch("wrkenv.container.manager.ContainerManager.image_exists")
    @patch("wrkenv.container.manager.ContainerManager.build_image")
    @patch("wrkenv.container.manager.ContainerManager.container_running")
    @patch("wrkenv.container.manager.ContainerManager.container_exists")
    @patch("subprocess.run")
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
        
        self.assertTrue(result)
        mock_check_docker.assert_called_once()
        mock_image_exists.assert_called_once()
        mock_running.assert_called_once()
        # Verify docker run command
        docker_run_cmd = mock_run.call_args[0][0]
        self.assertEqual(docker_run_cmd[0], "docker")
        self.assertEqual(docker_run_cmd[1], "run")
        self.assertIn("-d", docker_run_cmd)
        self.assertIn("--name", docker_run_cmd)
        self.assertIn("wrkenv-dev", docker_run_cmd)

    @patch("wrkenv.container.manager.ContainerManager.check_docker")
    def test_start_container_docker_not_available(self, mock_check_docker):
        """Test container start when Docker is not available."""
        mock_check_docker.return_value = False
        
        result = self.manager.start()
        
        self.assertFalse(result)

    @patch("wrkenv.container.manager.ContainerManager.check_docker")
    @patch("wrkenv.container.manager.ContainerManager.image_exists")
    @patch("wrkenv.container.manager.ContainerManager.build_image")
    def test_start_container_build_image_if_missing(
        self, mock_build, mock_image_exists, mock_check_docker
    ):
        """Test that start builds image if it doesn't exist."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = False
        mock_build.return_value = False  # Build fails
        
        result = self.manager.start()
        
        self.assertFalse(result)
        mock_build.assert_called_once_with(rebuild=False)

    @patch("wrkenv.container.manager.ContainerManager.check_docker")
    @patch("wrkenv.container.manager.ContainerManager.container_running")
    def test_start_container_already_running(self, mock_running, mock_check_docker):
        """Test start when container is already running."""
        mock_check_docker.return_value = True
        mock_running.return_value = True
        
        result = self.manager.start()
        
        self.assertTrue(result)  # Returns True but doesn't try to start again

    @patch("wrkenv.container.manager.ContainerManager.container_running")
    @patch("os.system")
    def test_enter_container_running(self, mock_system, mock_running):
        """Test entering a running container."""
        mock_running.return_value = True
        
        self.manager.enter()
        
        mock_system.assert_called_once_with(
            "docker exec -it wrkenv-dev /bin/bash"
        )

    @patch("wrkenv.container.manager.ContainerManager.container_running")
    @patch("os.system")
    def test_enter_container_with_command(self, mock_system, mock_running):
        """Test entering container with specific command."""
        mock_running.return_value = True
        
        self.manager.enter(["ls", "-la"])
        
        mock_system.assert_called_once_with(
            "docker exec -it wrkenv-dev ls -la"
        )

    @patch("wrkenv.container.manager.ContainerManager.container_running")
    @patch("os.system")
    def test_enter_container_not_running(self, mock_system, mock_running):
        """Test entering when container is not running."""
        mock_running.return_value = False
        
        self.manager.enter()
        
        mock_system.assert_not_called()

    @patch("subprocess.run")
    @patch("wrkenv.container.manager.ContainerManager.container_running")
    def test_stop_container_success(self, mock_running, mock_run):
        """Test successful container stop."""
        mock_running.return_value = True
        mock_run.return_value = Mock(returncode=0)
        
        result = self.manager.stop()
        
        self.assertTrue(result)
        # Check that docker stop was called
        stop_calls = [c for c in mock_run.call_args_list if "stop" in str(c)]
        self.assertTrue(len(stop_calls) > 0)

    @patch("subprocess.run")
    @patch("wrkenv.container.manager.ContainerManager.container_running")
    def test_stop_container_failure(self, mock_running, mock_run):
        """Test container stop failure."""
        mock_running.return_value = True
        mock_run.side_effect = subprocess.CalledProcessError(1, "docker stop")
        
        result = self.manager.stop()
        
        self.assertFalse(result)

    @patch("wrkenv.container.manager.ContainerManager.stop")
    @patch("wrkenv.container.manager.ContainerManager.start")
    def test_restart_container_success(self, mock_start, mock_stop):
        """Test successful container restart."""
        mock_stop.return_value = True
        mock_start.return_value = True
        
        result = self.manager.restart()
        
        self.assertTrue(result)
        mock_stop.assert_called_once()
        mock_start.assert_called_once()

    @patch("wrkenv.container.manager.ContainerManager.stop")
    def test_restart_container_stop_failure(self, mock_stop):
        """Test restart when stop fails."""
        mock_stop.return_value = False
        
        result = self.manager.restart()
        
        self.assertFalse(result)

    @patch("subprocess.run")
    def test_status_method(self, mock_run):
        """Test getting container status."""
        mock_run.return_value = Mock(
            returncode=0,
            stdout='[{"Status": "Up 2 hours", "State": {"Status": "running"}}]',
        )
        
        status = self.manager.status()
        
        self.assertIsNotNone(status)
        self.assertIn("Status", status)
        mock_run.assert_called_once_with(
            ["docker", "inspect", "wrkenv-dev"],
            capture_output=True,
            text=True,
            check=False,
        )

    @patch("subprocess.run")
    def test_status_no_container(self, mock_run):
        """Test getting status when container doesn't exist."""
        mock_run.return_value = Mock(returncode=1, stdout="")
        
        status = self.manager.status()
        
        self.assertIsNone(status)

    @patch("os.system")
    def test_logs_method(self, mock_system):
        """Test getting container logs."""
        self.manager.logs(follow=False, tail=10)
        
        mock_system.assert_called_once_with(
            "docker logs --tail 10 wrkenv-dev"
        )

    @patch("os.system")
    def test_logs_follow(self, mock_system):
        """Test following container logs."""
        self.manager.logs(follow=True)
        
        mock_system.assert_called_once_with("docker logs -f wrkenv-dev")

    @patch("subprocess.run")
    def test_clean_success(self, mock_run):
        """Test successful cleanup."""
        mock_run.return_value = Mock(returncode=0)
        
        result = self.manager.clean()
        
        self.assertTrue(result)
        # Should call both rm and rmi
        calls = mock_run.call_args_list
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][0][0], ["docker", "rm", "-f", "wrkenv-dev"])
        self.assertEqual(calls[1][0][0], ["docker", "rmi", "wrkenv-dev:latest"])

    @patch("subprocess.run")
    def test_clean_partial_failure(self, mock_run):
        """Test cleanup with partial failure."""
        # First call succeeds, second fails
        mock_run.side_effect = [
            Mock(returncode=0),
            subprocess.CalledProcessError(1, "docker rmi"),
        ]
        
        result = self.manager.clean()
        
        self.assertFalse(result)  # Returns False if any step fails

    def test_generate_dockerfile(self):
        """Test Dockerfile generation."""
        dockerfile = self.manager._generate_dockerfile()
        
        # Check for essential components
        self.assertIn("FROM ubuntu:22.04", dockerfile)
        self.assertIn("DEBIAN_FRONTEND=noninteractive", dockerfile)
        self.assertIn("apt-get update", dockerfile)
        self.assertIn("docker.io", dockerfile)
        self.assertIn("python3", dockerfile)
        self.assertIn("curl -LsSf https://astral.sh/uv/install.sh", dockerfile)
        self.assertIn("/workspace", dockerfile)
        self.assertIn("zsh", dockerfile)

    @patch("wrkenv.container.manager.ContainerManager.check_docker")
    @patch("wrkenv.container.manager.ContainerManager.image_exists")
    @patch("wrkenv.container.manager.ContainerManager.container_exists")
    @patch("subprocess.run")
    def test_start_removes_stopped_container(
        self, mock_run, mock_exists, mock_image_exists, mock_check_docker
    ):
        """Test that start removes existing stopped container."""
        mock_check_docker.return_value = True
        mock_image_exists.return_value = True
        mock_exists.return_value = True  # Container exists but not running
        
        with patch("wrkenv.container.manager.ContainerManager.container_running") as mock_running:
            mock_running.return_value = False
            
            self.manager.start()
            
            # Check that docker rm was called
            rm_calls = [c for c in mock_run.call_args_list if c[0][0][:2] == ["docker", "rm"]]
            self.assertEqual(len(rm_calls), 1)
            self.assertEqual(rm_calls[0][0][0], ["docker", "rm", "wrkenv-dev"])


if __name__ == "__main__":
    unittest.main()