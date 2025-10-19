"""
Tests for wrknv.container.errors
=================================
Comprehensive tests for all container error classes.
"""

from __future__ import annotations

import pytest

from wrknv.container.errors import (
    ContainerAlreadyExistsError,
    ContainerBuildError,
    ContainerNotFoundError,
    ContainerNotRunningError,
    ContainerRuntimeError,
    ImageNotFoundError,
    VolumeNotFoundError,
)


class TestContainerNotFoundError:
    """Tests for ContainerNotFoundError exception."""

    def test_container_not_found_basic(self):
        """Test basic container not found error."""
        error = ContainerNotFoundError("my-container")
        assert "Container 'my-container' not found" in str(error)
        assert error.container_name == "my-container"
        # Hint is stored as an attribute, not in string representation
        assert hasattr(error, 'hint')
        assert "docker ps -a" in error.hint

    def test_container_not_found_has_resource_info(self):
        """Test that error includes resource type and ID."""
        error = ContainerNotFoundError("test-container")
        # These attributes come from NotFoundError base class
        assert hasattr(error, 'resource_type')
        assert hasattr(error, 'resource_id')
        assert error.resource_type == "container"
        assert error.resource_id == "test-container"

    def test_container_not_found_hint(self):
        """Test that error includes helpful hint."""
        error = ContainerNotFoundError("missing-container")
        # Hint comes from the parent class
        assert hasattr(error, 'hint')
        assert "docker ps -a" in error.hint


class TestContainerNotRunningError:
    """Tests for ContainerNotRunningError exception."""

    def test_container_not_running_basic(self):
        """Test basic container not running error."""
        error = ContainerNotRunningError("stopped-container")
        assert "Container 'stopped-container' is not running" in str(error)
        assert error.container_name == "stopped-container"

    def test_container_not_running_state_info(self):
        """Test that error includes state information."""
        error = ContainerNotRunningError("idle-container")
        # These attributes come from StateError base class
        assert hasattr(error, 'expected_state')
        assert hasattr(error, 'current_state')
        assert error.expected_state == "running"
        assert error.current_state == "stopped"

    def test_container_not_running_hint(self):
        """Test that error includes start command in hint."""
        error = ContainerNotRunningError("my-container")
        assert hasattr(error, 'hint')
        assert "docker start my-container" in error.hint


class TestContainerAlreadyExistsError:
    """Tests for ContainerAlreadyExistsError exception."""

    def test_container_already_exists_basic(self):
        """Test basic container already exists error."""
        error = ContainerAlreadyExistsError("duplicate-container")
        assert "Container 'duplicate-container' already exists" in str(error)
        assert error.container_name == "duplicate-container"

    def test_container_already_exists_resource_info(self):
        """Test that error includes resource type and ID."""
        error = ContainerAlreadyExistsError("existing-container")
        assert hasattr(error, 'resource_type')
        assert hasattr(error, 'resource_id')
        assert error.resource_type == "container"
        assert error.resource_id == "existing-container"

    def test_container_already_exists_hint(self):
        """Test that error includes removal hint."""
        error = ContainerAlreadyExistsError("my-container")
        assert hasattr(error, 'hint')
        assert "docker rm my-container" in error.hint


class TestImageNotFoundError:
    """Tests for ImageNotFoundError exception."""

    def test_image_not_found_basic(self):
        """Test basic image not found error."""
        error = ImageNotFoundError("ubuntu:22.04")
        assert "Image 'ubuntu:22.04' not found" in str(error)
        assert error.image_name == "ubuntu:22.04"

    def test_image_not_found_resource_info(self):
        """Test that error includes resource type and ID."""
        error = ImageNotFoundError("nginx:latest")
        assert hasattr(error, 'resource_type')
        assert hasattr(error, 'resource_id')
        assert error.resource_type == "image"
        assert error.resource_id == "nginx:latest"

    def test_image_not_found_hint(self):
        """Test that error includes pull command hint."""
        error = ImageNotFoundError("alpine:3.18")
        assert hasattr(error, 'hint')
        assert "docker pull alpine:3.18" in error.hint


class TestVolumeNotFoundError:
    """Tests for VolumeNotFoundError exception."""

    def test_volume_not_found_basic(self):
        """Test basic volume not found error."""
        error = VolumeNotFoundError("my-volume")
        assert "Volume 'my-volume' not found" in str(error)
        assert error.volume_name == "my-volume"

    def test_volume_not_found_resource_info(self):
        """Test that error includes resource type and ID."""
        error = VolumeNotFoundError("data-volume")
        assert hasattr(error, 'resource_type')
        assert hasattr(error, 'resource_id')
        assert error.resource_type == "volume"
        assert error.resource_id == "data-volume"

    def test_volume_not_found_hint(self):
        """Test that error includes volume list hint."""
        error = VolumeNotFoundError("missing-volume")
        assert hasattr(error, 'hint')
        assert "docker volume ls" in error.hint


class TestContainerRuntimeError:
    """Tests for ContainerRuntimeError exception."""

    def test_runtime_error_without_reason(self):
        """Test runtime error without specific reason."""
        error = ContainerRuntimeError("docker")
        assert "Container runtime 'docker' is not available" in str(error)
        assert error.runtime == "docker"
        assert error.reason is None

    def test_runtime_error_with_reason(self):
        """Test runtime error with specific reason."""
        error = ContainerRuntimeError("docker", reason="daemon not running")
        assert "Container runtime 'docker' is not available: daemon not running" in str(error)
        assert error.runtime == "docker"
        assert error.reason == "daemon not running"

    def test_runtime_error_retry_possible(self):
        """Test that runtime error indicates retry is possible."""
        error = ContainerRuntimeError("docker")
        # This attribute comes from RuntimeError base class
        assert hasattr(error, 'retry_possible')
        assert error.retry_possible is True

    def test_runtime_error_hint(self):
        """Test that runtime error includes installation hint."""
        error = ContainerRuntimeError("docker")
        assert hasattr(error, 'hint')
        assert "Ensure Docker is installed and running" in error.hint

    def test_runtime_error_operation(self):
        """Test that runtime error includes operation name."""
        error = ContainerRuntimeError("podman")
        assert hasattr(error, 'operation')
        assert error.operation == "container_runtime_check"


class TestContainerBuildError:
    """Tests for ContainerBuildError exception."""

    def test_build_error_without_reason(self):
        """Test build error without specific reason."""
        error = ContainerBuildError("myapp:latest")
        assert "Failed to build image 'myapp:latest'" in str(error)
        assert error.image_tag == "myapp:latest"
        assert error.reason is None

    def test_build_error_with_reason(self):
        """Test build error with specific reason."""
        error = ContainerBuildError("myapp:v1.0", reason="invalid Dockerfile syntax")
        assert "Failed to build image 'myapp:v1.0': invalid Dockerfile syntax" in str(error)
        assert error.image_tag == "myapp:v1.0"
        assert error.reason == "invalid Dockerfile syntax"

    def test_build_error_resource_info(self):
        """Test that build error includes resource information."""
        error = ContainerBuildError("webapp:dev")
        assert hasattr(error, 'resource_type')
        assert hasattr(error, 'resource_path')
        assert error.resource_type == "image"
        assert error.resource_path == "webapp:dev"

    def test_build_error_hint(self):
        """Test that build error includes helpful hint."""
        error = ContainerBuildError("broken:latest")
        assert hasattr(error, 'hint')
        assert "Check Dockerfile syntax and build context" in error.hint


class TestErrorInheritance:
    """Tests for error class inheritance and hierarchy."""

    def test_all_errors_import(self):
        """Test that all error classes can be imported."""
        from wrknv.container.errors import (
            ContainerAlreadyExistsError,
            ContainerBuildError,
            ContainerNotFoundError,
            ContainerNotRunningError,
            ContainerRuntimeError,
            ImageNotFoundError,
            VolumeNotFoundError,
        )
        # If we got here, all imports succeeded
        assert True

    def test_error_base_classes(self):
        """Test that errors inherit from correct foundation classes."""
        from provide.foundation.errors import (
            AlreadyExistsError,
            NotFoundError,
            ResourceError,
            RuntimeError,
            StateError,
        )

        # Check inheritance
        assert issubclass(ContainerNotFoundError, NotFoundError)
        assert issubclass(ContainerNotRunningError, StateError)
        assert issubclass(ContainerAlreadyExistsError, AlreadyExistsError)
        assert issubclass(ImageNotFoundError, NotFoundError)
        assert issubclass(VolumeNotFoundError, NotFoundError)
        assert issubclass(ContainerRuntimeError, RuntimeError)
        assert issubclass(ContainerBuildError, ResourceError)
