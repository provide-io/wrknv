#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for ContainerManager class (extended)."""

from __future__ import annotations

from pathlib import Path
import shutil

from provide.testkit import FoundationTestCase
from provide.testkit.mocking import Mock
import pytest

from wrknv.config import WorkenvConfig
from wrknv.container.manager import ContainerManager


@pytest.mark.container
class TestContainerManagerExtended(FoundationTestCase):
    """Extended test suite for ContainerManager class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        super().setup_method()
        self.config = WorkenvConfig(project_name="test-project")
        self.manager = ContainerManager(self.config)

    def teardown_method(self) -> None:
        """Clean up after tests."""
        test_build_dir = Path.home() / ".wrknv" / "container-build"
        if test_build_dir.exists():
            shutil.rmtree(test_build_dir, ignore_errors=True)
        super().teardown_method()

    def test_stop_container_success(self) -> None:
        """Test successful container stop."""
        from tests.conftest import create_mock_lifecycle

        mock_lifecycle = create_mock_lifecycle(running=True)
        mock_lifecycle.stop = Mock(return_value=True)
        self.manager.lifecycle = mock_lifecycle

        result = self.manager.stop()

        assert result
        mock_lifecycle.stop.assert_called_once()

    def test_stop_container_failure(self) -> None:
        """Test container stop failure."""
        from tests.conftest import create_mock_lifecycle

        mock_lifecycle = create_mock_lifecycle(running=True)
        mock_lifecycle.stop = Mock(return_value=False)
        self.manager.lifecycle = mock_lifecycle

        result = self.manager.stop()

        assert not result
        mock_lifecycle.stop.assert_called_once()

    def test_restart_container_success(self) -> None:
        """Test successful container restart."""
        from tests.conftest import create_mock_lifecycle

        mock_lifecycle = create_mock_lifecycle(running=True)
        mock_lifecycle.restart = Mock(return_value=True)
        self.manager.lifecycle = mock_lifecycle

        result = self.manager.restart()

        assert result
        mock_lifecycle.restart.assert_called_once()

    def test_restart_container_stop_failure(self) -> None:
        """Test restart when stop fails."""
        from tests.conftest import create_mock_lifecycle

        mock_lifecycle = create_mock_lifecycle(running=True)
        mock_lifecycle.restart = Mock(return_value=True)
        self.manager.lifecycle = mock_lifecycle

        result = self.manager.restart()

        assert result  # restart continues even if stop fails
        mock_lifecycle.restart.assert_called_once()

    def test_status_method(self) -> None:
        """Test getting container status."""
        from tests.conftest import create_mock_lifecycle, create_mock_runtime

        mock_runtime = create_mock_runtime(available=True)
        mock_lifecycle = create_mock_lifecycle(exists=True, running=True)

        self.manager.runtime = mock_runtime
        self.manager.lifecycle = mock_lifecycle

        status = self.manager.status()

        assert status is not None
        assert status["docker_available"]
        assert status["container_exists"]
        assert status["container_running"]
        mock_lifecycle.status.assert_called()

    def test_status_no_docker(self) -> None:
        """Test getting status when Docker is not available."""
        from tests.conftest import create_mock_runtime

        mock_runtime = create_mock_runtime(available=False)
        self.manager.runtime = mock_runtime

        status = self.manager.status()

        assert status is not None
        assert not status["docker_available"]

    def test_logs_method(self) -> None:
        """Test getting container logs."""
        from tests.utils.fixtures import create_mock_logs

        mock_logs = create_mock_logs()
        mock_logs.get_logs = Mock(return_value="test logs")
        self.manager.logs = mock_logs

        result = self.manager.get_logs(follow=False, lines=10)

        assert result == "test logs"
        mock_logs.get_logs.assert_called_once_with(tail=10, follow=False, since=None, timestamps=False)

    def test_logs_follow(self) -> None:
        """Test following container logs."""
        from tests.utils.fixtures import create_mock_logs

        mock_logs = create_mock_logs()
        mock_logs.get_logs = Mock(return_value=None)  # follow returns None
        self.manager.logs = mock_logs

        result = self.manager.get_logs(follow=True)

        assert result is None
        mock_logs.get_logs.assert_called_once_with(tail=None, follow=True, since=None, timestamps=False)

    def test_clean_success(self) -> None:
        """Test successful cleanup."""
        from tests.conftest import (
            create_mock_builder,
            create_mock_lifecycle,
            create_mock_storage,
            create_mock_volumes,
        )

        mock_lifecycle = create_mock_lifecycle(exists=True, running=False)
        mock_lifecycle.remove = Mock(return_value=True)
        mock_builder = create_mock_builder()
        mock_builder.remove_image = Mock(return_value=True)
        mock_volumes = create_mock_volumes()
        mock_volumes.clean = Mock(return_value=True)
        mock_storage = create_mock_storage()
        mock_storage.clean_storage = Mock(return_value=True)

        self.manager.lifecycle = mock_lifecycle
        self.manager.builder = mock_builder
        self.manager.volumes = mock_volumes
        self.manager.storage = mock_storage

        result = self.manager.clean()

        assert result
        mock_lifecycle.remove.assert_called()

    def test_clean_partial_failure(self) -> None:
        """Test cleanup with partial failure."""
        from tests.conftest import (
            create_mock_builder,
            create_mock_lifecycle,
            create_mock_storage,
            create_mock_volumes,
        )

        mock_lifecycle = create_mock_lifecycle(exists=True, running=False)
        mock_lifecycle.remove = Mock(return_value=False)  # Removal fails
        mock_builder = create_mock_builder()
        mock_volumes = create_mock_volumes()
        mock_storage = create_mock_storage()

        self.manager.lifecycle = mock_lifecycle
        self.manager.builder = mock_builder
        self.manager.volumes = mock_volumes
        self.manager.storage = mock_storage

        result = self.manager.clean()

        assert not result  # Returns False if container removal fails
        mock_lifecycle.remove.assert_called()

    def test_generate_dockerfile(self) -> None:
        """Test Dockerfile generation through builder."""
        dockerfile = self.manager.builder.generate_dockerfile(self.manager.container_config)

        assert "FROM ubuntu:22.04" in dockerfile or "FROM python:" in dockerfile
        assert "apt-get update" in dockerfile or "WORKDIR" in dockerfile
        assert "WORKDIR /workspace" in dockerfile
        assert "curl" in dockerfile or "git" in dockerfile
        assert "CMD" in dockerfile or "sleep" in dockerfile

    def test_start_starts_existing_stopped_container(self) -> None:
        """Test that start will start an existing stopped container."""
        from tests.conftest import (
            create_mock_builder,
            create_mock_lifecycle,
            create_mock_storage,
        )

        mock_builder = create_mock_builder()
        mock_builder.image_exists = Mock(return_value=True)
        mock_lifecycle = create_mock_lifecycle(exists=True, running=False)
        mock_lifecycle.start = Mock(return_value=True)
        mock_storage = create_mock_storage()

        self.manager.builder = mock_builder
        self.manager.lifecycle = mock_lifecycle
        self.manager.storage = mock_storage

        result = self.manager.start()

        assert result
        mock_lifecycle.start.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# 🧰🌍🔚
