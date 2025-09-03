#!/usr/bin/env python3
#
# wrknv/container/errors.py
#
"""
Container-specific Errors
=========================
Custom exceptions for container operations.
"""

from wrknv.wenv.exceptions import ContainerError as BaseContainerError


class ContainerNotFoundError(BaseContainerError):
    """Raised when a container is not found."""
    
    def __init__(self, container_name: str):
        super().__init__(f"Container '{container_name}' not found")
        self.container_name = container_name


class ContainerNotRunningError(BaseContainerError):
    """Raised when a container is not running but needs to be."""
    
    def __init__(self, container_name: str):
        super().__init__(f"Container '{container_name}' is not running")
        self.container_name = container_name


class ContainerAlreadyExistsError(BaseContainerError):
    """Raised when trying to create a container that already exists."""
    
    def __init__(self, container_name: str):
        super().__init__(f"Container '{container_name}' already exists")
        self.container_name = container_name


class ImageNotFoundError(BaseContainerError):
    """Raised when a container image is not found."""
    
    def __init__(self, image_name: str):
        super().__init__(f"Image '{image_name}' not found")
        self.image_name = image_name


class VolumeNotFoundError(BaseContainerError):
    """Raised when a volume is not found."""
    
    def __init__(self, volume_name: str):
        super().__init__(f"Volume '{volume_name}' not found")
        self.volume_name = volume_name


class ContainerRuntimeError(BaseContainerError):
    """Raised when the container runtime is not available."""
    
    def __init__(self, runtime: str, reason: str | None):
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.runtime = runtime
        self.reason = reason


class ContainerBuildError(BaseContainerError):
    """Raised when container build fails."""
    
    def __init__(self, image_tag: str, reason: str | None):
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"
        super().__init__(message)
        self.image_tag = image_tag
        self.reason = reason