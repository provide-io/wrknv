#!/usr/bin/env python3
"""Test container runtime implementations."""

import json
import unittest
from unittest.mock import Mock, patch

from provide.foundation.process import CompletedProcess, ProcessError

from wrknv.container.runtime.docker import DockerRuntime


class TestDockerRuntime(unittest.TestCase):
    """Test Docker runtime implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.runtime = DockerRuntime(
            runtime_name="docker",
            runtime_command="docker"
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_run_container(self, mock_run):
        """Test starting a new container."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "run"],
            returncode=0,
            stdout="abc123container",
            stderr=""
        )
        
        result = self.runtime.run_container(
            image="ubuntu:latest",
            name="test-container",
            detach=True,
            volumes=["/host:/container"],
            environment={"KEY": "value"},
            ports=["8080:80"],
            workdir="/app",
            command=["echo", "hello"]
        )
        
        self.assertEqual(result.stdout, "abc123container")
        mock_run.assert_called_once()
        
        # Check command construction
        cmd = mock_run.call_args[0][0]
        self.assertEqual(cmd[0], "docker")
        self.assertEqual(cmd[1], "run")
        self.assertIn("-d", cmd)
        self.assertIn("--name", cmd)
        self.assertIn("test-container", cmd)
        self.assertIn("-v", cmd)
        self.assertIn("/host:/container", cmd)
        self.assertIn("-e", cmd)
        self.assertIn("KEY=value", cmd)
        self.assertIn("-p", cmd)
        self.assertIn("8080:80", cmd)
        self.assertIn("--workdir", cmd)
        self.assertIn("/app", cmd)
        self.assertIn("ubuntu:latest", cmd)
        self.assertIn("echo", cmd)
        self.assertIn("hello", cmd)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_start_container(self, mock_run):
        """Test starting an existing container."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "start"],
            returncode=0,
            stdout="test-container",
            stderr=""
        )
        
        result = self.runtime.start_container("test-container")
        
        self.assertEqual(result.stdout, "test-container")
        mock_run.assert_called_once_with(
            ["docker", "start", "test-container"],
            check=True
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_stop_container(self, mock_run):
        """Test stopping a container."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "stop"],
            returncode=0,
            stdout="test-container",
            stderr=""
        )
        
        result = self.runtime.stop_container("test-container", timeout=15)
        
        mock_run.assert_called_once_with(
            ["docker", "stop", "-t", "15", "test-container"],
            check=True
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_container_exists_true(self, mock_run):
        """Test checking if container exists - found case."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "ps"],
            returncode=0,
            stdout="container1\ntest-container\ncontainer3",
            stderr=""
        )
        
        exists = self.runtime.container_exists("test-container")
        
        self.assertTrue(exists)
        mock_run.assert_called_once_with(
            ["docker", "ps", "-a", "--format", "{{.Names}}"],
            check=False
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_container_exists_false(self, mock_run):
        """Test checking if container exists - not found case."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "ps"],
            returncode=0,
            stdout="container1\ncontainer2",
            stderr=""
        )
        
        exists = self.runtime.container_exists("test-container")
        
        self.assertFalse(exists)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_container_running(self, mock_run):
        """Test checking if container is running."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "ps"],
            returncode=0,
            stdout="test-container\nother-container",
            stderr=""
        )
        
        running = self.runtime.container_running("test-container")
        
        self.assertTrue(running)
        mock_run.assert_called_once_with(
            ["docker", "ps", "--format", "{{.Names}}"],
            check=False
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_exec_in_container(self, mock_run):
        """Test executing command in container."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "exec"],
            returncode=0,
            stdout="command output",
            stderr=""
        )
        
        result = self.runtime.exec_in_container(
            name="test-container",
            command=["ls", "-la"],
            interactive=True,
            tty=True,
            user="root",
            workdir="/app",
            environment={"VAR": "value"}
        )
        
        self.assertEqual(result.stdout, "command output")
        
        cmd = mock_run.call_args[0][0]
        self.assertIn("-i", cmd)
        self.assertIn("-t", cmd)
        self.assertIn("-u", cmd)
        self.assertIn("root", cmd)
        self.assertIn("-w", cmd)
        self.assertIn("/app", cmd)
        self.assertIn("-e", cmd)
        self.assertIn("VAR=value", cmd)
        self.assertIn("test-container", cmd)
        self.assertIn("ls", cmd)
        self.assertIn("-la", cmd)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_build_image(self, mock_run):
        """Test building a Docker image."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "build"],
            returncode=0,
            stdout="Successfully built abc123",
            stderr=""
        )
        
        result = self.runtime.build_image(
            dockerfile="Dockerfile",
            tag="myapp:latest",
            context=".",
            build_args={"VERSION": "1.0"},
            no_cache=True,
            platform="linux/amd64"
        )
        
        self.assertIn("Successfully built", result.stdout)
        
        cmd = mock_run.call_args[0][0]
        self.assertEqual(cmd[0], "docker")
        self.assertEqual(cmd[1], "build")
        self.assertIn("-f", cmd)
        self.assertIn("Dockerfile", cmd)
        self.assertIn("-t", cmd)
        self.assertIn("myapp:latest", cmd)
        self.assertIn("--build-arg", cmd)
        self.assertIn("VERSION=1.0", cmd)
        self.assertIn("--no-cache", cmd)
        self.assertIn("--platform", cmd)
        self.assertIn("linux/amd64", cmd)
        self.assertIn(".", cmd)
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_list_containers(self, mock_run):
        """Test listing containers."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "ps"],
            returncode=0,
            stdout='{"Name":"container1","Status":"running"}\n{"Name":"container2","Status":"stopped"}',
            stderr=""
        )
        
        containers = self.runtime.list_containers(all=True)
        
        self.assertEqual(len(containers), 2)
        self.assertEqual(containers[0]["Name"], "container1")
        self.assertEqual(containers[1]["Name"], "container2")
        
        mock_run.assert_called_once_with(
            ["docker", "ps", "--format", "json", "-a"],
            check=True
        )
    
    @patch("wrknv.container.runtime.docker.run_command")
    def test_error_handling(self, mock_run):
        """Test error handling when command fails."""
        mock_run.side_effect = ProcessError(
            cmd=["docker", "start", "nonexistent"],
            returncode=1,
            stdout="",
            stderr="Error: No such container: nonexistent"
        )
        
        with self.assertRaises(ProcessError) as ctx:
            self.runtime.start_container("nonexistent")
        
        self.assertIn("nonexistent", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()