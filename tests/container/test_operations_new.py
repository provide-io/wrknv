#!/usr/bin/env python3
"""Test container operations modules."""

import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from attrs import define
from provide.foundation.process import CompletedProcess, ProcessError
from rich.console import Console

from wrknv.container.operations.lifecycle import ContainerLifecycle
from wrknv.container.operations.exec import ContainerExec
from wrknv.container.operations.build import ContainerBuilder
from wrknv.container.operations.logs import ContainerLogs
from wrknv.container.operations.volumes import VolumeManager
from wrknv.container.runtime.docker import DockerRuntime


class TestContainerLifecycle(unittest.TestCase):
    """Test container lifecycle operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker"
        )
        self.lifecycle = ContainerLifecycle(
            runtime=self.runtime,
            container_name="test-container",
            console=Console(),
            start_emoji="🚀",
            stop_emoji="⏹️",
            restart_emoji="🔄",
            status_emoji="📊",
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_start_existing_container(self, mock_run):
        """Test starting an existing container."""
        # Container exists
        mock_run.side_effect = [
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Container not running
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="",
                stderr=""
            ),
            # Start container
            CompletedProcess(
                args=["docker", "start"],
                returncode=0,
                stdout="test-container",
                stderr=""
            )
        ]
        
        result = self.lifecycle.start(create_if_missing=False)
        
        self.assertTrue(result)
        self.assertEqual(mock_run.call_count, 3)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_start_create_new_container(self, mock_run):
        """Test creating and starting a new container."""
        # Container doesn't exist
        mock_run.side_effect = [
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="",
                stderr=""
            ),
            # Create container
            CompletedProcess(
                args=["docker", "run"],
                returncode=0,
                stdout="abc123",
                stderr=""
            )
        ]
        
        result = self.lifecycle.start(
            create_if_missing=True,
            image="ubuntu:latest",
            volumes=["/host:/container"],
            environment={"KEY": "value"}
        )
        
        self.assertTrue(result)
        self.assertEqual(mock_run.call_count, 2)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_stop_container(self, mock_run):
        """Test stopping a container."""
        # Container is running
        mock_run.side_effect = [
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Stop container
            CompletedProcess(
                args=["docker", "stop"],
                returncode=0,
                stdout="test-container",
                stderr=""
            )
        ]
        
        result = self.lifecycle.stop(timeout=10)
        
        self.assertTrue(result)
        self.assertEqual(mock_run.call_count, 2)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_restart_container(self, mock_run):
        """Test restarting a container."""
        # Container is running (for stop check)
        mock_run.side_effect = [
            # Check if running (for restart)
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Check if running again (for stop)
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Stop container
            CompletedProcess(
                args=["docker", "stop"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Check if container exists (for start)
            CompletedProcess(
                args=["docker", "ps", "-a"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Check if running (should be stopped)
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="",
                stderr=""
            ),
            # Start container
            CompletedProcess(
                args=["docker", "start"],
                returncode=0,
                stdout="test-container",
                stderr=""
            )
        ]
        
        result = self.lifecycle.restart(timeout=10)
        
        self.assertTrue(result)
        self.assertEqual(mock_run.call_count, 6)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_status(self, mock_run):
        """Test getting container status."""
        mock_run.side_effect = [
            # Container exists
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Container is running
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Container inspect
            CompletedProcess(
                args=["docker", "inspect"],
                returncode=0,
                stdout='[{"Id": "abc123", "State": {"Running": true}}]',
                stderr=""
            )
        ]
        
        status = self.lifecycle.status()
        
        self.assertTrue(status["exists"])
        self.assertTrue(status["running"])
        self.assertIn("id", status)
        self.assertEqual(mock_run.call_count, 3)


class TestContainerExec(unittest.TestCase):
    """Test container exec operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker"
        )
        self.exec = ContainerExec(
            runtime=self.runtime,
            container_name="test-container",
            console=Console(),
            available_shells=["/bin/bash", "/bin/sh"],
            default_shell="/bin/sh",
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_run_command(self, mock_run):
        """Test running a command in container."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "exec"],
            returncode=0,
            stdout="command output",
            stderr=""
        )
        
        result = self.exec.run_command(
            command=["echo", "hello"],
            capture_output=True
        )
        
        self.assertEqual(result, "command output")
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        self.assertIn("exec", cmd)
        self.assertIn("test-container", cmd)
        self.assertIn("echo", cmd)
        self.assertIn("hello", cmd)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_find_shell(self, mock_run):
        """Test finding available shell."""
        # First shell fails, second succeeds
        mock_run.side_effect = [
            ProcessError(
                message="bash not found",
                command=["docker", "exec"],
                returncode=127
            ),
            CompletedProcess(
                args=["docker", "exec"],
                returncode=0,
                stdout="/bin/sh",
                stderr=""
            )
        ]
        
        shell = self.exec._detect_shell()
        
        self.assertEqual(shell, "/bin/sh")
        self.assertEqual(mock_run.call_count, 2)
    
    @patch("wrknv.container.runtime.docker.run_command")
    @patch("os.system")
    def test_enter_container(self, mock_system, mock_run):
        """Test entering container interactively."""
        # Mock container running and shell detection
        mock_run.side_effect = [
            # Container is running check
            CompletedProcess(
                args=["docker", "ps"],
                returncode=0,
                stdout="test-container",
                stderr=""
            ),
            # Shell detection (test -f /bin/bash)
            CompletedProcess(
                args=["docker", "exec"],
                returncode=0,
                stdout="",
                stderr=""
            ),
        ]
        mock_system.return_value = 0
        
        result = self.exec.enter(shell=None)
        
        self.assertTrue(result)
        mock_run.assert_called_once()  # For find_shell
        mock_system.assert_called_once()
        system_cmd = mock_system.call_args[0][0]
        self.assertIn("docker exec", system_cmd)
        self.assertIn("-it", system_cmd)
        self.assertIn("test-container", system_cmd)
        self.assertIn("/bin/bash", system_cmd)


class TestContainerBuilder(unittest.TestCase):
    """Test container build operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker"
        )
        self.builder = ContainerBuilder(
            runtime=self.runtime,
            console=Console()
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_build_simple(self, mock_run):
        """Test simple build."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "build"],
            returncode=0,
            stdout="Successfully built abc123",
            stderr=""
        )
        
        result = self.builder.build(
            dockerfile="Dockerfile",
            tag="myapp:latest",
            context=".",
            build_args=None,
            stream_output=False
        )
        
        self.assertTrue(result)
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        self.assertIn("build", cmd)
        self.assertIn("-f", cmd)
        self.assertIn("Dockerfile", cmd)
        self.assertIn("-t", cmd)
        self.assertIn("myapp:latest", cmd)
        self.assertIn(".", cmd)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_build_with_args(self, mock_run):
        """Test build with build args."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "build"],
            returncode=0,
            stdout="Successfully built abc123",
            stderr=""
        )
        
        result = self.builder.build(
            dockerfile="Dockerfile",
            tag="myapp:latest",
            context=".",
            build_args={"VERSION": "1.0", "ENV": "production"},
            stream_output=False,
            no_cache=True,
            platform="linux/amd64"
        )
        
        self.assertTrue(result)
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        self.assertIn("--build-arg", cmd)
        self.assertIn("VERSION=1.0", cmd)
        self.assertIn("ENV=production", cmd)
        self.assertIn("--no-cache", cmd)
        self.assertIn("--platform", cmd)
        self.assertIn("linux/amd64", cmd)
    
    @patch("wrknv.container.operations.build.stream_command")
    def test_build_with_stream(self, mock_stream):
        """Test build with streaming output."""
        mock_stream.return_value = iter([
            "Step 1/5 : FROM ubuntu:latest",
            "Step 2/5 : RUN apt-get update",
            "Successfully built abc123"
        ])
        
        result = self.builder.build(
            dockerfile="Dockerfile",
            tag="myapp:latest",
            context=".",
            build_args=None,
            stream_output=True
        )
        
        self.assertTrue(result)
        mock_stream.assert_called_once()


class TestContainerLogs(unittest.TestCase):
    """Test container logs operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker"
        )
        self.logs = ContainerLogs(
            runtime=self.runtime,
            container_name="test-container",
            console=Console()
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_get_logs(self, mock_run):
        """Test getting container logs."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "logs"],
            returncode=0,
            stdout="Log line 1\nLog line 2\nLog line 3",
            stderr=""
        )
        
        result = self.logs.get_logs(
            follow=False,
            tail=10,
            since="5m",
            timestamps=True
        )
        
        self.assertEqual(result, "Log line 1\nLog line 2\nLog line 3")
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        self.assertIn("logs", cmd)
        self.assertIn("--tail", cmd)
        self.assertIn("10", cmd)
        self.assertIn("--since", cmd)
        self.assertIn("5m", cmd)
        # Note: timestamps is handled in stream_logs, not get_logs
        self.assertIn("test-container", cmd)
    
    @patch("wrknv.container.operations.logs.stream_command")
    def test_stream_logs(self, mock_stream):
        """Test streaming container logs."""
        mock_stream.return_value = iter([
            "2024-01-01T00:00:00 Log line 1",
            "2024-01-01T00:00:01 Log line 2",
            "2024-01-01T00:00:02 Log line 3"
        ])
        
        lines = list(self.logs.stream_logs(
            tail=10,
            since=None,
            timestamps=False
        ))
        
        self.assertEqual(len(lines), 3)
        self.assertIn("Log line 1", lines[0])
        mock_stream.assert_called_once()


class TestVolumeManager(unittest.TestCase):
    """Test volume management operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker"
        )
        self.volumes = VolumeManager(
            runtime=self.runtime,
            console=Console(),
            backup_dir=Path("/tmp/backups")
        )
    
    @patch("wrknv.container.operations.volumes.run_command")
    def test_create_volume(self, mock_run):
        """Test creating a volume."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "create"],
            returncode=0,
            stdout="test-volume",
            stderr=""
        )
        
        result = self.volumes.create_volume(
            name="test-volume",
            driver="local",
            options={"type": "tmpfs", "device": "tmpfs"}
        )
        
        self.assertTrue(result)
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        self.assertIn("volume", cmd)
        self.assertIn("create", cmd)
        self.assertIn("--driver", cmd)
        self.assertIn("local", cmd)
        self.assertIn("--opt", cmd)
        self.assertIn("type=tmpfs", cmd)
        self.assertIn("test-volume", cmd)
    
    @patch("wrknv.container.operations.volumes.run_command")
    def test_list_volumes(self, mock_run):
        """Test listing volumes."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"],
            returncode=0,
            stdout='{"Name":"vol1","Driver":"local"}\n{"Name":"vol2","Driver":"local"}',
            stderr=""
        )
        
        volumes = self.volumes.list_volumes(filter_label=None)
        
        self.assertEqual(len(volumes), 2)
        self.assertEqual(volumes[0]["Name"], "vol1")
        self.assertEqual(volumes[1]["Name"], "vol2")
        mock_run.assert_called_once()
    
    @patch("wrknv.container.operations.volumes.run_command")
    def test_backup_volume(self, mock_run):
        """Test backing up a volume."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "run"],
            returncode=0,
            stdout="",
            stderr=""
        )
        
        backup_file = self.volumes.backup_volume(
            volume_name="test-volume",
            container_name="test-container",
            mount_path="/data"
        )
        
        self.assertIsNotNone(backup_file)
        self.assertTrue(str(backup_file).startswith("/tmp/backups"))
        self.assertIn("test-volume", str(backup_file))
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        self.assertIn("run", cmd)
        self.assertIn("--rm", cmd)
        self.assertIn("-v", cmd)
        self.assertIn("test-volume:/data", cmd)
        self.assertIn("alpine", cmd)
        self.assertIn("tar", cmd)


if __name__ == "__main__":
    unittest.main()