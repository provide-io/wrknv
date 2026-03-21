#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Container-specific Errors
=========================
Custom exceptions for container operations using foundation error hierarchy."""

from __future__ import annotations

from provide.foundation.errors import (
    AlreadyExistsError,
    NotFoundError,
    ResourceError,
    RuntimeError,
    StateError,
)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class ContainerNotFoundError(NotFoundError):
    """Raised when a container is not found."""

    def xǁContainerNotFoundErrorǁ__init____mutmut_orig(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_1(self, container_name: str) -> None:
        super().__init__(
            message=None,
            resource_type="container",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_2(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type=None,
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_3(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=None,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_4(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            hint=None,
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_5(self, container_name: str) -> None:
        super().__init__(
            resource_type="container",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_6(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_7(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_8(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_9(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="XXcontainerXX",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_10(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="CONTAINER",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_11(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            hint="XXUse 'docker ps -a' to list all containersXX",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_12(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            hint="use 'docker ps -a' to list all containers",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_13(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            hint="USE 'DOCKER PS -A' TO LIST ALL CONTAINERS",
        )
        self.container_name = container_name

    def xǁContainerNotFoundErrorǁ__init____mutmut_14(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' not found",
            resource_type="container",
            resource_id=container_name,
            hint="Use 'docker ps -a' to list all containers",
        )
        self.container_name = None
    
    xǁContainerNotFoundErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerNotFoundErrorǁ__init____mutmut_1': xǁContainerNotFoundErrorǁ__init____mutmut_1, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_2': xǁContainerNotFoundErrorǁ__init____mutmut_2, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_3': xǁContainerNotFoundErrorǁ__init____mutmut_3, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_4': xǁContainerNotFoundErrorǁ__init____mutmut_4, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_5': xǁContainerNotFoundErrorǁ__init____mutmut_5, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_6': xǁContainerNotFoundErrorǁ__init____mutmut_6, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_7': xǁContainerNotFoundErrorǁ__init____mutmut_7, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_8': xǁContainerNotFoundErrorǁ__init____mutmut_8, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_9': xǁContainerNotFoundErrorǁ__init____mutmut_9, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_10': xǁContainerNotFoundErrorǁ__init____mutmut_10, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_11': xǁContainerNotFoundErrorǁ__init____mutmut_11, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_12': xǁContainerNotFoundErrorǁ__init____mutmut_12, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_13': xǁContainerNotFoundErrorǁ__init____mutmut_13, 
        'xǁContainerNotFoundErrorǁ__init____mutmut_14': xǁContainerNotFoundErrorǁ__init____mutmut_14
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerNotFoundErrorǁ__init____mutmut_orig)
    xǁContainerNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerNotFoundErrorǁ__init__'


class ContainerNotRunningError(StateError):
    """Raised when a container is not running but needs to be."""

    def xǁContainerNotRunningErrorǁ__init____mutmut_orig(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_1(self, container_name: str) -> None:
        super().__init__(
            message=None,
            expected_state="running",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_2(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state=None,
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_3(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state=None,
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_4(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state="stopped",
            hint=None,
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_5(self, container_name: str) -> None:
        super().__init__(
            expected_state="running",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_6(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_7(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_8(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state="stopped",
            )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_9(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="XXrunningXX",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_10(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="RUNNING",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_11(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state="XXstoppedXX",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_12(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state="STOPPED",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = container_name

    def xǁContainerNotRunningErrorǁ__init____mutmut_13(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' is not running",
            expected_state="running",
            current_state="stopped",
            hint=f"Start the container with 'docker start {container_name}'",
        )
        self.container_name = None
    
    xǁContainerNotRunningErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerNotRunningErrorǁ__init____mutmut_1': xǁContainerNotRunningErrorǁ__init____mutmut_1, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_2': xǁContainerNotRunningErrorǁ__init____mutmut_2, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_3': xǁContainerNotRunningErrorǁ__init____mutmut_3, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_4': xǁContainerNotRunningErrorǁ__init____mutmut_4, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_5': xǁContainerNotRunningErrorǁ__init____mutmut_5, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_6': xǁContainerNotRunningErrorǁ__init____mutmut_6, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_7': xǁContainerNotRunningErrorǁ__init____mutmut_7, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_8': xǁContainerNotRunningErrorǁ__init____mutmut_8, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_9': xǁContainerNotRunningErrorǁ__init____mutmut_9, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_10': xǁContainerNotRunningErrorǁ__init____mutmut_10, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_11': xǁContainerNotRunningErrorǁ__init____mutmut_11, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_12': xǁContainerNotRunningErrorǁ__init____mutmut_12, 
        'xǁContainerNotRunningErrorǁ__init____mutmut_13': xǁContainerNotRunningErrorǁ__init____mutmut_13
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerNotRunningErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerNotRunningErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerNotRunningErrorǁ__init____mutmut_orig)
    xǁContainerNotRunningErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerNotRunningErrorǁ__init__'


class ContainerAlreadyExistsError(AlreadyExistsError):
    """Raised when trying to create a container that already exists."""

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_orig(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="container",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_1(self, container_name: str) -> None:
        super().__init__(
            message=None,
            resource_type="container",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_2(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type=None,
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_3(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="container",
            resource_id=None,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_4(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="container",
            resource_id=container_name,
            hint=None,
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_5(self, container_name: str) -> None:
        super().__init__(
            resource_type="container",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_6(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_7(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="container",
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_8(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="container",
            resource_id=container_name,
            )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_9(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="XXcontainerXX",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_10(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="CONTAINER",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = container_name

    def xǁContainerAlreadyExistsErrorǁ__init____mutmut_11(self, container_name: str) -> None:
        super().__init__(
            message=f"Container '{container_name}' already exists",
            resource_type="container",
            resource_id=container_name,
            hint=f"Use 'docker rm {container_name}' to remove existing container",
        )
        self.container_name = None
    
    xǁContainerAlreadyExistsErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerAlreadyExistsErrorǁ__init____mutmut_1': xǁContainerAlreadyExistsErrorǁ__init____mutmut_1, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_2': xǁContainerAlreadyExistsErrorǁ__init____mutmut_2, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_3': xǁContainerAlreadyExistsErrorǁ__init____mutmut_3, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_4': xǁContainerAlreadyExistsErrorǁ__init____mutmut_4, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_5': xǁContainerAlreadyExistsErrorǁ__init____mutmut_5, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_6': xǁContainerAlreadyExistsErrorǁ__init____mutmut_6, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_7': xǁContainerAlreadyExistsErrorǁ__init____mutmut_7, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_8': xǁContainerAlreadyExistsErrorǁ__init____mutmut_8, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_9': xǁContainerAlreadyExistsErrorǁ__init____mutmut_9, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_10': xǁContainerAlreadyExistsErrorǁ__init____mutmut_10, 
        'xǁContainerAlreadyExistsErrorǁ__init____mutmut_11': xǁContainerAlreadyExistsErrorǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerAlreadyExistsErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerAlreadyExistsErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerAlreadyExistsErrorǁ__init____mutmut_orig)
    xǁContainerAlreadyExistsErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerAlreadyExistsErrorǁ__init__'


class ImageNotFoundError(NotFoundError):
    """Raised when a container image is not found."""

    def xǁImageNotFoundErrorǁ__init____mutmut_orig(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="image",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_1(self, image_name: str) -> None:
        super().__init__(
            message=None,
            resource_type="image",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_2(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type=None,
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_3(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="image",
            resource_id=None,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_4(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="image",
            resource_id=image_name,
            hint=None,
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_5(self, image_name: str) -> None:
        super().__init__(
            resource_type="image",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_6(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_7(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="image",
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_8(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="image",
            resource_id=image_name,
            )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_9(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="XXimageXX",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_10(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="IMAGE",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = image_name

    def xǁImageNotFoundErrorǁ__init____mutmut_11(self, image_name: str) -> None:
        super().__init__(
            message=f"Image '{image_name}' not found",
            resource_type="image",
            resource_id=image_name,
            hint=f"Pull the image with 'docker pull {image_name}'",
        )
        self.image_name = None
    
    xǁImageNotFoundErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁImageNotFoundErrorǁ__init____mutmut_1': xǁImageNotFoundErrorǁ__init____mutmut_1, 
        'xǁImageNotFoundErrorǁ__init____mutmut_2': xǁImageNotFoundErrorǁ__init____mutmut_2, 
        'xǁImageNotFoundErrorǁ__init____mutmut_3': xǁImageNotFoundErrorǁ__init____mutmut_3, 
        'xǁImageNotFoundErrorǁ__init____mutmut_4': xǁImageNotFoundErrorǁ__init____mutmut_4, 
        'xǁImageNotFoundErrorǁ__init____mutmut_5': xǁImageNotFoundErrorǁ__init____mutmut_5, 
        'xǁImageNotFoundErrorǁ__init____mutmut_6': xǁImageNotFoundErrorǁ__init____mutmut_6, 
        'xǁImageNotFoundErrorǁ__init____mutmut_7': xǁImageNotFoundErrorǁ__init____mutmut_7, 
        'xǁImageNotFoundErrorǁ__init____mutmut_8': xǁImageNotFoundErrorǁ__init____mutmut_8, 
        'xǁImageNotFoundErrorǁ__init____mutmut_9': xǁImageNotFoundErrorǁ__init____mutmut_9, 
        'xǁImageNotFoundErrorǁ__init____mutmut_10': xǁImageNotFoundErrorǁ__init____mutmut_10, 
        'xǁImageNotFoundErrorǁ__init____mutmut_11': xǁImageNotFoundErrorǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁImageNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁImageNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁImageNotFoundErrorǁ__init____mutmut_orig)
    xǁImageNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁImageNotFoundErrorǁ__init__'


class VolumeNotFoundError(NotFoundError):
    """Raised when a volume is not found."""

    def xǁVolumeNotFoundErrorǁ__init____mutmut_orig(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_1(self, volume_name: str) -> None:
        super().__init__(
            message=None,
            resource_type="volume",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_2(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type=None,
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_3(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=None,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_4(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            hint=None,
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_5(self, volume_name: str) -> None:
        super().__init__(
            resource_type="volume",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_6(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_7(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_8(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_9(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="XXvolumeXX",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_10(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="VOLUME",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_11(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            hint="XXUse 'docker volume ls' to list available volumesXX",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_12(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            hint="use 'docker volume ls' to list available volumes",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_13(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            hint="USE 'DOCKER VOLUME LS' TO LIST AVAILABLE VOLUMES",
        )
        self.volume_name = volume_name

    def xǁVolumeNotFoundErrorǁ__init____mutmut_14(self, volume_name: str) -> None:
        super().__init__(
            message=f"Volume '{volume_name}' not found",
            resource_type="volume",
            resource_id=volume_name,
            hint="Use 'docker volume ls' to list available volumes",
        )
        self.volume_name = None
    
    xǁVolumeNotFoundErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVolumeNotFoundErrorǁ__init____mutmut_1': xǁVolumeNotFoundErrorǁ__init____mutmut_1, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_2': xǁVolumeNotFoundErrorǁ__init____mutmut_2, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_3': xǁVolumeNotFoundErrorǁ__init____mutmut_3, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_4': xǁVolumeNotFoundErrorǁ__init____mutmut_4, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_5': xǁVolumeNotFoundErrorǁ__init____mutmut_5, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_6': xǁVolumeNotFoundErrorǁ__init____mutmut_6, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_7': xǁVolumeNotFoundErrorǁ__init____mutmut_7, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_8': xǁVolumeNotFoundErrorǁ__init____mutmut_8, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_9': xǁVolumeNotFoundErrorǁ__init____mutmut_9, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_10': xǁVolumeNotFoundErrorǁ__init____mutmut_10, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_11': xǁVolumeNotFoundErrorǁ__init____mutmut_11, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_12': xǁVolumeNotFoundErrorǁ__init____mutmut_12, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_13': xǁVolumeNotFoundErrorǁ__init____mutmut_13, 
        'xǁVolumeNotFoundErrorǁ__init____mutmut_14': xǁVolumeNotFoundErrorǁ__init____mutmut_14
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVolumeNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁVolumeNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁVolumeNotFoundErrorǁ__init____mutmut_orig)
    xǁVolumeNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁVolumeNotFoundErrorǁ__init__'


class ContainerRuntimeError(RuntimeError):
    """Raised when the container runtime is not available."""

    def xǁContainerRuntimeErrorǁ__init____mutmut_orig(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_1(self, runtime: str, reason: str | None = None) -> None:
        message = None
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_2(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message = f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_3(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message -= f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_4(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=None,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_5(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation=None,
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_6(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=None,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_7(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint=None,
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_8(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_9(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_10(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_11(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_12(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="XXcontainer_runtime_checkXX",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_13(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="CONTAINER_RUNTIME_CHECK",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_14(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=False,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_15(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="XXEnsure Docker is installed and runningXX",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_16(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="ensure docker is installed and running",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_17(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="ENSURE DOCKER IS INSTALLED AND RUNNING",
        )
        self.runtime = runtime
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_18(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = None
        self.reason = reason

    def xǁContainerRuntimeErrorǁ__init____mutmut_19(self, runtime: str, reason: str | None = None) -> None:
        message = f"Container runtime '{runtime}' is not available"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            operation="container_runtime_check",
            retry_possible=True,
            hint="Ensure Docker is installed and running",
        )
        self.runtime = runtime
        self.reason = None
    
    xǁContainerRuntimeErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerRuntimeErrorǁ__init____mutmut_1': xǁContainerRuntimeErrorǁ__init____mutmut_1, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_2': xǁContainerRuntimeErrorǁ__init____mutmut_2, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_3': xǁContainerRuntimeErrorǁ__init____mutmut_3, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_4': xǁContainerRuntimeErrorǁ__init____mutmut_4, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_5': xǁContainerRuntimeErrorǁ__init____mutmut_5, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_6': xǁContainerRuntimeErrorǁ__init____mutmut_6, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_7': xǁContainerRuntimeErrorǁ__init____mutmut_7, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_8': xǁContainerRuntimeErrorǁ__init____mutmut_8, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_9': xǁContainerRuntimeErrorǁ__init____mutmut_9, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_10': xǁContainerRuntimeErrorǁ__init____mutmut_10, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_11': xǁContainerRuntimeErrorǁ__init____mutmut_11, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_12': xǁContainerRuntimeErrorǁ__init____mutmut_12, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_13': xǁContainerRuntimeErrorǁ__init____mutmut_13, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_14': xǁContainerRuntimeErrorǁ__init____mutmut_14, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_15': xǁContainerRuntimeErrorǁ__init____mutmut_15, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_16': xǁContainerRuntimeErrorǁ__init____mutmut_16, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_17': xǁContainerRuntimeErrorǁ__init____mutmut_17, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_18': xǁContainerRuntimeErrorǁ__init____mutmut_18, 
        'xǁContainerRuntimeErrorǁ__init____mutmut_19': xǁContainerRuntimeErrorǁ__init____mutmut_19
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerRuntimeErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerRuntimeErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerRuntimeErrorǁ__init____mutmut_orig)
    xǁContainerRuntimeErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerRuntimeErrorǁ__init__'


class ContainerBuildError(ResourceError):
    """Raised when container build fails."""

    def xǁContainerBuildErrorǁ__init____mutmut_orig(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_1(self, image_tag: str, reason: str | None = None) -> None:
        message = None
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_2(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message = f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_3(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message -= f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_4(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=None,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_5(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type=None,
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_6(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=None,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_7(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint=None,
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_8(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_9(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_10(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_11(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_12(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="XXimageXX",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_13(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="IMAGE",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_14(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="XXCheck Dockerfile syntax and build contextXX",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_15(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="check dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_16(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="CHECK DOCKERFILE SYNTAX AND BUILD CONTEXT",
        )
        self.image_tag = image_tag
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_17(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = None
        self.reason = reason

    def xǁContainerBuildErrorǁ__init____mutmut_18(self, image_tag: str, reason: str | None = None) -> None:
        message = f"Failed to build image '{image_tag}'"
        if reason:
            message += f": {reason}"

        super().__init__(
            message=message,
            resource_type="image",
            resource_path=image_tag,
            hint="Check Dockerfile syntax and build context",
        )
        self.image_tag = image_tag
        self.reason = None
    
    xǁContainerBuildErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerBuildErrorǁ__init____mutmut_1': xǁContainerBuildErrorǁ__init____mutmut_1, 
        'xǁContainerBuildErrorǁ__init____mutmut_2': xǁContainerBuildErrorǁ__init____mutmut_2, 
        'xǁContainerBuildErrorǁ__init____mutmut_3': xǁContainerBuildErrorǁ__init____mutmut_3, 
        'xǁContainerBuildErrorǁ__init____mutmut_4': xǁContainerBuildErrorǁ__init____mutmut_4, 
        'xǁContainerBuildErrorǁ__init____mutmut_5': xǁContainerBuildErrorǁ__init____mutmut_5, 
        'xǁContainerBuildErrorǁ__init____mutmut_6': xǁContainerBuildErrorǁ__init____mutmut_6, 
        'xǁContainerBuildErrorǁ__init____mutmut_7': xǁContainerBuildErrorǁ__init____mutmut_7, 
        'xǁContainerBuildErrorǁ__init____mutmut_8': xǁContainerBuildErrorǁ__init____mutmut_8, 
        'xǁContainerBuildErrorǁ__init____mutmut_9': xǁContainerBuildErrorǁ__init____mutmut_9, 
        'xǁContainerBuildErrorǁ__init____mutmut_10': xǁContainerBuildErrorǁ__init____mutmut_10, 
        'xǁContainerBuildErrorǁ__init____mutmut_11': xǁContainerBuildErrorǁ__init____mutmut_11, 
        'xǁContainerBuildErrorǁ__init____mutmut_12': xǁContainerBuildErrorǁ__init____mutmut_12, 
        'xǁContainerBuildErrorǁ__init____mutmut_13': xǁContainerBuildErrorǁ__init____mutmut_13, 
        'xǁContainerBuildErrorǁ__init____mutmut_14': xǁContainerBuildErrorǁ__init____mutmut_14, 
        'xǁContainerBuildErrorǁ__init____mutmut_15': xǁContainerBuildErrorǁ__init____mutmut_15, 
        'xǁContainerBuildErrorǁ__init____mutmut_16': xǁContainerBuildErrorǁ__init____mutmut_16, 
        'xǁContainerBuildErrorǁ__init____mutmut_17': xǁContainerBuildErrorǁ__init____mutmut_17, 
        'xǁContainerBuildErrorǁ__init____mutmut_18': xǁContainerBuildErrorǁ__init____mutmut_18
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerBuildErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerBuildErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerBuildErrorǁ__init____mutmut_orig)
    xǁContainerBuildErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerBuildErrorǁ__init__'


# 🧰🌍🔚
