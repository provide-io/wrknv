import pytest
#!/usr/bin/env python3

"""
Test suite for dynamic container configuration.
"""

import unittest
from unittest.mock import MagicMock, patch

from wrknv.container.manager import ContainerManager
from wrknv.wenv.schema import ContainerConfig, WorkenvConfig


@pytest.mark.container
class TestDynamicContainerConfiguration(unittest.TestCase):
    """Test that container manager uses dynamic configuration from wrknv.toml."""

    def test_default_container_config(self):
        """Test container manager with default configuration."""
        manager = ContainerManager()
        
        self.assertEqual(manager.CONTAINER_NAME, "wrknv-dev")
        self.assertEqual(manager.IMAGE_NAME, "wrknv-dev")
        self.assertIsNotNone(manager.container_config)
        self.assertFalse(manager.container_config.enabled)

    def test_custom_project_name(self):
        """Test container manager with custom project name."""
        config = WorkenvConfig(
            project_name="my-awesome-project",
            container=ContainerConfig(enabled=True)
        )
        
        manager = ContainerManager(config)
        
        self.assertEqual(manager.CONTAINER_NAME, "my-awesome-project-dev")
        self.assertEqual(manager.IMAGE_NAME, "my-awesome-project-dev")

    def test_dockerfile_with_default_config(self):
        """Test Dockerfile generation with default configuration."""
        manager = ContainerManager()
        dockerfile = manager._generate_dockerfile()
        
        self.assertIn("FROM ubuntu:22.04", dockerfile)
        self.assertIn("python3.11", dockerfile)
        self.assertIn("curl", dockerfile)
        self.assertIn("git", dockerfile)

    def test_dockerfile_with_custom_config(self):
        """Test Dockerfile generation with custom configuration."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                base_image="python:3.12-slim",
                python_version="3.12",
                additional_packages=["nodejs", "npm", "postgresql-client"],
                environment={"NODE_ENV": "development", "DEBUG": "true"}
            )
        )
        
        manager = ContainerManager(config)
        dockerfile = manager._generate_dockerfile()
        
        # Check base image
        self.assertIn("FROM python:3.12-slim", dockerfile)
        
        # Python packages are not installed when using Python base image
        
        # Check additional packages
        self.assertIn("nodejs", dockerfile)
        self.assertIn("npm", dockerfile)
        self.assertIn("postgresql-client", dockerfile)
        
        # Check environment variables
        self.assertIn("ENV NODE_ENV=development", dockerfile)
        self.assertIn("ENV DEBUG=true", dockerfile)

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.manager.ContainerManager.container_running")
    @patch("wrknv.container.manager.ContainerManager.container_exists")
    @patch("wrknv.container.manager.ContainerManager.image_exists")
    def test_start_with_custom_volumes_and_ports(
        self, mock_image_exists, mock_container_exists, mock_container_running, mock_run
    ):
        """Test container start with custom volumes and ports."""
        mock_image_exists.return_value = True
        mock_container_exists.return_value = False
        mock_container_running.return_value = False
        mock_run.return_value = MagicMock(returncode=0)
        
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                volumes=["/data:/data", "/logs:/logs"],
                ports=["8080:80", "5432:5432"],
                environment={"API_KEY": "secret123"}
            )
        )
        
        manager = ContainerManager(config)
        manager.start()
        
        # Check that docker run was called
        self.assertTrue(mock_run.called)
        
        # Get the command that was executed
        cmd = mock_run.call_args[0][0]
        
        # Check container name
        self.assertIn("test-project-dev", cmd)
        
        # Check custom volumes
        self.assertIn("/data:/data", cmd)
        self.assertIn("/logs:/logs", cmd)
        
        # Check custom ports
        self.assertIn("8080:80", cmd)
        self.assertIn("5432:5432", cmd)
        
        # Check custom environment variable
        self.assertIn("API_KEY=secret123", cmd)
        
        # Check default volumes are still included
        self.assertIn("/host-home", " ".join(cmd))
        self.assertIn("/var/run/docker.sock:/var/run/docker.sock", " ".join(cmd))

    def test_container_config_from_toml(self):
        """Test loading container configuration from TOML-like structure."""
        config_dict = {
            "project_name": "web-app",
            "container": {
                "enabled": True,
                "base_image": "node:18-alpine",
                "python_version": "3.11",
                "additional_packages": ["redis-tools", "mysql-client"],
                "environment": {
                    "DATABASE_URL": "postgresql://localhost/mydb",
                    "REDIS_URL": "redis://localhost:6379"
                },
                "volumes": ["/app/data:/data"],
                "ports": ["3000:3000", "5000:5000"]
            }
        }
        
        # This would normally come from loading a TOML file
        import cattrs
        converter = cattrs.Converter()
        config = converter.structure(config_dict, WorkenvConfig)
        
        manager = ContainerManager(config)
        
        self.assertEqual(manager.CONTAINER_NAME, "web-app-dev")
        self.assertTrue(manager.container_config.enabled)
        self.assertEqual(manager.container_config.base_image, "node:18-alpine")
        self.assertEqual(len(manager.container_config.additional_packages), 2)
        self.assertEqual(len(manager.container_config.environment), 2)
        self.assertEqual(len(manager.container_config.volumes), 1)
        self.assertEqual(len(manager.container_config.ports), 2)

    def test_dockerfile_python_version_formatting(self):
        """Test that Python version is correctly formatted in Dockerfile."""
        test_cases = [
            ("3.11", "python3.11"),
            ("3.12", "python3.12"),
            ("3.10", "python3.10"),
        ]
        
        for py_version, expected_package in test_cases:
            config = WorkenvConfig(
                project_name="test",
                container=ContainerConfig(python_version=py_version)
            )
            
            manager = ContainerManager(config)
            dockerfile = manager._generate_dockerfile()
            
            self.assertIn(expected_package, dockerfile)
            self.assertIn(f"{expected_package}-pip", dockerfile)
            self.assertIn(f"{expected_package}-venv", dockerfile)


if __name__ == "__main__":
    unittest.main()