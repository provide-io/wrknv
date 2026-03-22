#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#


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

from provide.testkit.mocking import Mock, patch

# Test utilities - available from conftest
from tests.conftest import create_mock_builder
from wrknv.config import WorkenvConfig
from wrknv.container.manager import ContainerManager
from wrknv.container.operations.lifecycle import ContainerLifecycle
from wrknv.container.runtime.docker import DockerRuntime


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

    @patch("provide.foundation.process.run")
    def test_image_exists_true(self, mock_run) -> None:
        """Test image_exists when image exists."""
        mock_run.return_value = Mock(returncode=0, stdout="test-project-dev:latest\nother:tag\n")

        result = self.manager.image_exists()

        assert result
        # Verify docker images was called (don't check exact kwargs)
        assert mock_run.called

    @patch("provide.foundation.process.run")
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
        mock_builder = create_mock_builder()
        self.manager.builder = mock_builder

        result = self.manager.build_image(rebuild=True)

        assert result
        # Verify builder.build was called
        mock_builder.build.assert_called_once()

    def test_build_image_failure(self) -> None:
        """Test image build failure."""
        from tests.conftest import create_mock_builder, create_mock_storage

        # Replace builder with one that fails to build
        mock_builder = create_mock_builder()
        mock_builder.build = Mock(return_value=False)  # Build fails
        mock_storage = create_mock_storage()

        self.manager.builder = mock_builder
        self.manager.storage = mock_storage

        result = self.manager.build_image()

        assert not result
        mock_builder.build.assert_called_once()

    def test_start_container_success(self) -> None:
        """Test successful container start."""
        from tests.conftest import (
            create_mock_builder,
            create_mock_lifecycle,
            create_mock_storage,
        )

        # Replace dependencies with mocks that control behavior
        mock_lifecycle = create_mock_lifecycle(exists=False, running=False)
        mock_builder = create_mock_builder()
        mock_builder.image_exists = Mock(return_value=True)
        mock_storage = create_mock_storage()

        # Mock lifecycle.start to return success
        mock_lifecycle.start = Mock(return_value=True)

        self.manager.lifecycle = mock_lifecycle
        self.manager.builder = mock_builder
        self.manager.storage = mock_storage

        result = self.manager.start()

        assert result
        # Verify image existence was checked
        mock_builder.image_exists.assert_called()
        # Verify container was started
        mock_lifecycle.start.assert_called_once()

    def test_start_container_docker_not_available(self) -> None:
        """Test container start when lifecycle start fails."""
        from tests.conftest import (
            create_mock_builder,
            create_mock_lifecycle,
            create_mock_storage,
        )

        # Replace dependencies - lifecycle start fails
        mock_lifecycle = create_mock_lifecycle(exists=False, running=False)
        mock_lifecycle.start = Mock(return_value=False)  # Start fails
        mock_builder = create_mock_builder()
        mock_builder.image_exists = Mock(return_value=True)
        mock_storage = create_mock_storage()

        self.manager.lifecycle = mock_lifecycle
        self.manager.builder = mock_builder
        self.manager.storage = mock_storage

        result = self.manager.start()

        assert not result
        mock_lifecycle.start.assert_called()

    def test_start_container_build_image_if_missing(self) -> None:
        """Test that start builds image if it doesn't exist."""
        from tests.conftest import create_mock_builder, create_mock_storage

        # Replace dependencies with mocks
        mock_builder = create_mock_builder()
        mock_builder.image_exists = Mock(return_value=False)
        mock_builder.build = Mock(return_value=False)  # Build fails
        mock_storage = create_mock_storage()

        self.manager.builder = mock_builder
        self.manager.storage = mock_storage

        result = self.manager.start()

        assert not result
        # Verify build was called (via build_image method)
        mock_storage.get_container_path.assert_called()

    def test_start_container_already_running(self) -> None:
        """Test start when container is already running."""
        from tests.conftest import (
            create_mock_builder,
            create_mock_lifecycle,
            create_mock_runtime,
        )

        # Replace dependencies with mocks
        mock_runtime = create_mock_runtime(available=True)
        mock_builder = create_mock_builder()
        mock_builder.image_exists = Mock(return_value=True)
        mock_lifecycle = create_mock_lifecycle(running=True)  # Already running

        self.manager.runtime = mock_runtime
        self.manager.builder = mock_builder
        self.manager.lifecycle = mock_lifecycle

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

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
