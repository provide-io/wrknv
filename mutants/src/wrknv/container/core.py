#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Container Core Management
=========================
Core container management functionality for wrknv."""

from __future__ import annotations

from pathlib import Path

from provide.foundation import logger
from provide.foundation.process import run
from rich.console import Console

from wrknv.config import WorkenvConfig
from wrknv.wenv.schema import ContainerConfig, get_default_config
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


class ContainerManager:
    """Manages Docker containers for wrknv development environments."""

    # Default values (can be overridden by config)
    DEFAULT_CONTAINER_NAME = "wrknv-dev"
    DEFAULT_IMAGE_NAME = "wrknv-dev"
    DEFAULT_IMAGE_TAG = "latest"

    # Emoji constants for visual feedback
    CONTAINER_EMOJI = "🐳"
    BUILD_EMOJI = "🔨"
    START_EMOJI = "🚀"
    STOP_EMOJI = "⏹️"
    CLEAN_EMOJI = "🧹"
    STATUS_EMOJI = "📊"

    def xǁContainerManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        self.config = None
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        self.config = config and get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_3(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = None

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_4(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = None

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_5(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container and ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_6(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = None
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_7(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").upper()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_8(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(None, "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_9(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", None).lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_10(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace("-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_11(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", ).lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_12(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace("XX XX", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_13(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "XX-XX").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_14(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name == "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_15(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "XXmy-projectXX":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_16(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "MY-PROJECT":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_17(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = None
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_18(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = None
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_19(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = None
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_20(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = None
        self.full_image = f"{self.IMAGE_NAME}:{self.IMAGE_TAG}"

        # Initialize storage on creation
        self._setup_storage()

    def xǁContainerManagerǁ__init____mutmut_21(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or get_default_config()
        self.console = Console()

        # Get container configuration
        self.container_config = self.config.container or ContainerConfig()

        # Set container and image names (can be customized in config)
        project_name = self.config.project_name.replace(" ", "-").lower()
        if project_name != "my-project":
            self.CONTAINER_NAME = f"{project_name}-dev"
        else:
            self.CONTAINER_NAME = self.DEFAULT_CONTAINER_NAME
        self.IMAGE_NAME = self.CONTAINER_NAME
        self.IMAGE_TAG = self.DEFAULT_IMAGE_TAG
        self.full_image = None

        # Initialize storage on creation
        self._setup_storage()
    
    xǁContainerManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁ__init____mutmut_1': xǁContainerManagerǁ__init____mutmut_1, 
        'xǁContainerManagerǁ__init____mutmut_2': xǁContainerManagerǁ__init____mutmut_2, 
        'xǁContainerManagerǁ__init____mutmut_3': xǁContainerManagerǁ__init____mutmut_3, 
        'xǁContainerManagerǁ__init____mutmut_4': xǁContainerManagerǁ__init____mutmut_4, 
        'xǁContainerManagerǁ__init____mutmut_5': xǁContainerManagerǁ__init____mutmut_5, 
        'xǁContainerManagerǁ__init____mutmut_6': xǁContainerManagerǁ__init____mutmut_6, 
        'xǁContainerManagerǁ__init____mutmut_7': xǁContainerManagerǁ__init____mutmut_7, 
        'xǁContainerManagerǁ__init____mutmut_8': xǁContainerManagerǁ__init____mutmut_8, 
        'xǁContainerManagerǁ__init____mutmut_9': xǁContainerManagerǁ__init____mutmut_9, 
        'xǁContainerManagerǁ__init____mutmut_10': xǁContainerManagerǁ__init____mutmut_10, 
        'xǁContainerManagerǁ__init____mutmut_11': xǁContainerManagerǁ__init____mutmut_11, 
        'xǁContainerManagerǁ__init____mutmut_12': xǁContainerManagerǁ__init____mutmut_12, 
        'xǁContainerManagerǁ__init____mutmut_13': xǁContainerManagerǁ__init____mutmut_13, 
        'xǁContainerManagerǁ__init____mutmut_14': xǁContainerManagerǁ__init____mutmut_14, 
        'xǁContainerManagerǁ__init____mutmut_15': xǁContainerManagerǁ__init____mutmut_15, 
        'xǁContainerManagerǁ__init____mutmut_16': xǁContainerManagerǁ__init____mutmut_16, 
        'xǁContainerManagerǁ__init____mutmut_17': xǁContainerManagerǁ__init____mutmut_17, 
        'xǁContainerManagerǁ__init____mutmut_18': xǁContainerManagerǁ__init____mutmut_18, 
        'xǁContainerManagerǁ__init____mutmut_19': xǁContainerManagerǁ__init____mutmut_19, 
        'xǁContainerManagerǁ__init____mutmut_20': xǁContainerManagerǁ__init____mutmut_20, 
        'xǁContainerManagerǁ__init____mutmut_21': xǁContainerManagerǁ__init____mutmut_21
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerManagerǁ__init____mutmut_orig)
    xǁContainerManagerǁ__init____mutmut_orig.__name__ = 'xǁContainerManagerǁ__init__'

    def xǁContainerManagerǁ_setup_storage__mutmut_orig(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_1(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = None

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_2(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(None).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_3(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=None, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_4(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=None)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_5(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_6(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, )

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_7(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=False, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_8(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=False)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_9(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = None
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_10(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base * "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_11(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "XXsharedXX"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_12(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "SHARED"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_13(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=None)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_14(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=False)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_15(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=None)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_16(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir * "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_17(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "XXdownloadsXX").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_18(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "DOWNLOADS").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_19(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=False)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_20(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = None
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_21(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base * self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_22(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=None)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_23(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=False)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_24(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = None
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_25(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir * "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_26(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "XXvolumesXX"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_27(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "VOLUMES"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_28(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=None)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_29(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=False)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_30(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=None)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_31(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir * volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_32(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=False)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_33(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=None)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_34(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir * "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_35(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "XXbuildXX").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_36(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "BUILD").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_37(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=False)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_38(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=None)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_39(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir * "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_40(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "XXlogsXX").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_41(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "LOGS").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_42(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=False)
        (container_dir / "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_43(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=None)

    def xǁContainerManagerǁ_setup_storage__mutmut_44(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir * "backups").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_45(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "XXbackupsXX").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_46(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "BACKUPS").mkdir(exist_ok=True)

    def xǁContainerManagerǁ_setup_storage__mutmut_47(self) -> None:
        """Set up the container storage directory structure."""
        # Expand storage path
        storage_base = Path(self.container_config.storage_path).expanduser()

        # Create base directories
        storage_base.mkdir(parents=True, exist_ok=True)

        # Create shared directories
        shared_dir = storage_base / "shared"
        shared_dir.mkdir(exist_ok=True)
        (shared_dir / "downloads").mkdir(exist_ok=True)

        # Create container-specific directories
        container_dir = storage_base / self.CONTAINER_NAME
        container_dir.mkdir(exist_ok=True)

        # Create subdirectories
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)

        # Create persistent volume directories
        for volume_name in self.container_config.persistent_volumes:
            (volumes_dir / volume_name).mkdir(exist_ok=True)

        (container_dir / "build").mkdir(exist_ok=True)
        (container_dir / "logs").mkdir(exist_ok=True)
        (container_dir / "backups").mkdir(exist_ok=False)
    
    xǁContainerManagerǁ_setup_storage__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁ_setup_storage__mutmut_1': xǁContainerManagerǁ_setup_storage__mutmut_1, 
        'xǁContainerManagerǁ_setup_storage__mutmut_2': xǁContainerManagerǁ_setup_storage__mutmut_2, 
        'xǁContainerManagerǁ_setup_storage__mutmut_3': xǁContainerManagerǁ_setup_storage__mutmut_3, 
        'xǁContainerManagerǁ_setup_storage__mutmut_4': xǁContainerManagerǁ_setup_storage__mutmut_4, 
        'xǁContainerManagerǁ_setup_storage__mutmut_5': xǁContainerManagerǁ_setup_storage__mutmut_5, 
        'xǁContainerManagerǁ_setup_storage__mutmut_6': xǁContainerManagerǁ_setup_storage__mutmut_6, 
        'xǁContainerManagerǁ_setup_storage__mutmut_7': xǁContainerManagerǁ_setup_storage__mutmut_7, 
        'xǁContainerManagerǁ_setup_storage__mutmut_8': xǁContainerManagerǁ_setup_storage__mutmut_8, 
        'xǁContainerManagerǁ_setup_storage__mutmut_9': xǁContainerManagerǁ_setup_storage__mutmut_9, 
        'xǁContainerManagerǁ_setup_storage__mutmut_10': xǁContainerManagerǁ_setup_storage__mutmut_10, 
        'xǁContainerManagerǁ_setup_storage__mutmut_11': xǁContainerManagerǁ_setup_storage__mutmut_11, 
        'xǁContainerManagerǁ_setup_storage__mutmut_12': xǁContainerManagerǁ_setup_storage__mutmut_12, 
        'xǁContainerManagerǁ_setup_storage__mutmut_13': xǁContainerManagerǁ_setup_storage__mutmut_13, 
        'xǁContainerManagerǁ_setup_storage__mutmut_14': xǁContainerManagerǁ_setup_storage__mutmut_14, 
        'xǁContainerManagerǁ_setup_storage__mutmut_15': xǁContainerManagerǁ_setup_storage__mutmut_15, 
        'xǁContainerManagerǁ_setup_storage__mutmut_16': xǁContainerManagerǁ_setup_storage__mutmut_16, 
        'xǁContainerManagerǁ_setup_storage__mutmut_17': xǁContainerManagerǁ_setup_storage__mutmut_17, 
        'xǁContainerManagerǁ_setup_storage__mutmut_18': xǁContainerManagerǁ_setup_storage__mutmut_18, 
        'xǁContainerManagerǁ_setup_storage__mutmut_19': xǁContainerManagerǁ_setup_storage__mutmut_19, 
        'xǁContainerManagerǁ_setup_storage__mutmut_20': xǁContainerManagerǁ_setup_storage__mutmut_20, 
        'xǁContainerManagerǁ_setup_storage__mutmut_21': xǁContainerManagerǁ_setup_storage__mutmut_21, 
        'xǁContainerManagerǁ_setup_storage__mutmut_22': xǁContainerManagerǁ_setup_storage__mutmut_22, 
        'xǁContainerManagerǁ_setup_storage__mutmut_23': xǁContainerManagerǁ_setup_storage__mutmut_23, 
        'xǁContainerManagerǁ_setup_storage__mutmut_24': xǁContainerManagerǁ_setup_storage__mutmut_24, 
        'xǁContainerManagerǁ_setup_storage__mutmut_25': xǁContainerManagerǁ_setup_storage__mutmut_25, 
        'xǁContainerManagerǁ_setup_storage__mutmut_26': xǁContainerManagerǁ_setup_storage__mutmut_26, 
        'xǁContainerManagerǁ_setup_storage__mutmut_27': xǁContainerManagerǁ_setup_storage__mutmut_27, 
        'xǁContainerManagerǁ_setup_storage__mutmut_28': xǁContainerManagerǁ_setup_storage__mutmut_28, 
        'xǁContainerManagerǁ_setup_storage__mutmut_29': xǁContainerManagerǁ_setup_storage__mutmut_29, 
        'xǁContainerManagerǁ_setup_storage__mutmut_30': xǁContainerManagerǁ_setup_storage__mutmut_30, 
        'xǁContainerManagerǁ_setup_storage__mutmut_31': xǁContainerManagerǁ_setup_storage__mutmut_31, 
        'xǁContainerManagerǁ_setup_storage__mutmut_32': xǁContainerManagerǁ_setup_storage__mutmut_32, 
        'xǁContainerManagerǁ_setup_storage__mutmut_33': xǁContainerManagerǁ_setup_storage__mutmut_33, 
        'xǁContainerManagerǁ_setup_storage__mutmut_34': xǁContainerManagerǁ_setup_storage__mutmut_34, 
        'xǁContainerManagerǁ_setup_storage__mutmut_35': xǁContainerManagerǁ_setup_storage__mutmut_35, 
        'xǁContainerManagerǁ_setup_storage__mutmut_36': xǁContainerManagerǁ_setup_storage__mutmut_36, 
        'xǁContainerManagerǁ_setup_storage__mutmut_37': xǁContainerManagerǁ_setup_storage__mutmut_37, 
        'xǁContainerManagerǁ_setup_storage__mutmut_38': xǁContainerManagerǁ_setup_storage__mutmut_38, 
        'xǁContainerManagerǁ_setup_storage__mutmut_39': xǁContainerManagerǁ_setup_storage__mutmut_39, 
        'xǁContainerManagerǁ_setup_storage__mutmut_40': xǁContainerManagerǁ_setup_storage__mutmut_40, 
        'xǁContainerManagerǁ_setup_storage__mutmut_41': xǁContainerManagerǁ_setup_storage__mutmut_41, 
        'xǁContainerManagerǁ_setup_storage__mutmut_42': xǁContainerManagerǁ_setup_storage__mutmut_42, 
        'xǁContainerManagerǁ_setup_storage__mutmut_43': xǁContainerManagerǁ_setup_storage__mutmut_43, 
        'xǁContainerManagerǁ_setup_storage__mutmut_44': xǁContainerManagerǁ_setup_storage__mutmut_44, 
        'xǁContainerManagerǁ_setup_storage__mutmut_45': xǁContainerManagerǁ_setup_storage__mutmut_45, 
        'xǁContainerManagerǁ_setup_storage__mutmut_46': xǁContainerManagerǁ_setup_storage__mutmut_46, 
        'xǁContainerManagerǁ_setup_storage__mutmut_47': xǁContainerManagerǁ_setup_storage__mutmut_47
    }
    
    def _setup_storage(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁ_setup_storage__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁ_setup_storage__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _setup_storage.__signature__ = _mutmut_signature(xǁContainerManagerǁ_setup_storage__mutmut_orig)
    xǁContainerManagerǁ_setup_storage__mutmut_orig.__name__ = 'xǁContainerManagerǁ_setup_storage'

    def xǁContainerManagerǁget_container_path__mutmut_orig(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(self.container_config.storage_path).expanduser()
        container_path = storage_base / self.CONTAINER_NAME

        if subpath:
            return container_path / subpath
        return container_path

    def xǁContainerManagerǁget_container_path__mutmut_1(self, subpath: str = "XXXX") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(self.container_config.storage_path).expanduser()
        container_path = storage_base / self.CONTAINER_NAME

        if subpath:
            return container_path / subpath
        return container_path

    def xǁContainerManagerǁget_container_path__mutmut_2(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = None
        container_path = storage_base / self.CONTAINER_NAME

        if subpath:
            return container_path / subpath
        return container_path

    def xǁContainerManagerǁget_container_path__mutmut_3(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(None).expanduser()
        container_path = storage_base / self.CONTAINER_NAME

        if subpath:
            return container_path / subpath
        return container_path

    def xǁContainerManagerǁget_container_path__mutmut_4(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(self.container_config.storage_path).expanduser()
        container_path = None

        if subpath:
            return container_path / subpath
        return container_path

    def xǁContainerManagerǁget_container_path__mutmut_5(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(self.container_config.storage_path).expanduser()
        container_path = storage_base * self.CONTAINER_NAME

        if subpath:
            return container_path / subpath
        return container_path

    def xǁContainerManagerǁget_container_path__mutmut_6(self, subpath: str = "") -> Path:
        """Get path to container-specific directory or file.

        Args:
            subpath: Relative path within the container directory

        Returns:
            Path object pointing to the requested location
        """
        storage_base = Path(self.container_config.storage_path).expanduser()
        container_path = storage_base / self.CONTAINER_NAME

        if subpath:
            return container_path * subpath
        return container_path
    
    xǁContainerManagerǁget_container_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁget_container_path__mutmut_1': xǁContainerManagerǁget_container_path__mutmut_1, 
        'xǁContainerManagerǁget_container_path__mutmut_2': xǁContainerManagerǁget_container_path__mutmut_2, 
        'xǁContainerManagerǁget_container_path__mutmut_3': xǁContainerManagerǁget_container_path__mutmut_3, 
        'xǁContainerManagerǁget_container_path__mutmut_4': xǁContainerManagerǁget_container_path__mutmut_4, 
        'xǁContainerManagerǁget_container_path__mutmut_5': xǁContainerManagerǁget_container_path__mutmut_5, 
        'xǁContainerManagerǁget_container_path__mutmut_6': xǁContainerManagerǁget_container_path__mutmut_6
    }
    
    def get_container_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁget_container_path__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁget_container_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_container_path.__signature__ = _mutmut_signature(xǁContainerManagerǁget_container_path__mutmut_orig)
    xǁContainerManagerǁget_container_path__mutmut_orig.__name__ = 'xǁContainerManagerǁget_container_path'

    def xǁContainerManagerǁcheck_docker__mutmut_orig(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_1(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = None
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_2(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                None,
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_3(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=None,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_4(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=None,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_5(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=None,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_6(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_7(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_8(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_9(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_10(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["XXdockerXX", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_11(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["DOCKER", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_12(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "XXversionXX", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_13(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "VERSION", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_14(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "XX--formatXX", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_15(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--FORMAT", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_16(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "XX{{.Server.Version}}XX"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_17(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.server.version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_18(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.SERVER.VERSION}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_19(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=False,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_20(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=False,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_21(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=6,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_22(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode != 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_23(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 1
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_24(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(None)
            return False

    def xǁContainerManagerǁcheck_docker__mutmut_25(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            result = run(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Docker check failed: {e}")
            return True
    
    xǁContainerManagerǁcheck_docker__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁcheck_docker__mutmut_1': xǁContainerManagerǁcheck_docker__mutmut_1, 
        'xǁContainerManagerǁcheck_docker__mutmut_2': xǁContainerManagerǁcheck_docker__mutmut_2, 
        'xǁContainerManagerǁcheck_docker__mutmut_3': xǁContainerManagerǁcheck_docker__mutmut_3, 
        'xǁContainerManagerǁcheck_docker__mutmut_4': xǁContainerManagerǁcheck_docker__mutmut_4, 
        'xǁContainerManagerǁcheck_docker__mutmut_5': xǁContainerManagerǁcheck_docker__mutmut_5, 
        'xǁContainerManagerǁcheck_docker__mutmut_6': xǁContainerManagerǁcheck_docker__mutmut_6, 
        'xǁContainerManagerǁcheck_docker__mutmut_7': xǁContainerManagerǁcheck_docker__mutmut_7, 
        'xǁContainerManagerǁcheck_docker__mutmut_8': xǁContainerManagerǁcheck_docker__mutmut_8, 
        'xǁContainerManagerǁcheck_docker__mutmut_9': xǁContainerManagerǁcheck_docker__mutmut_9, 
        'xǁContainerManagerǁcheck_docker__mutmut_10': xǁContainerManagerǁcheck_docker__mutmut_10, 
        'xǁContainerManagerǁcheck_docker__mutmut_11': xǁContainerManagerǁcheck_docker__mutmut_11, 
        'xǁContainerManagerǁcheck_docker__mutmut_12': xǁContainerManagerǁcheck_docker__mutmut_12, 
        'xǁContainerManagerǁcheck_docker__mutmut_13': xǁContainerManagerǁcheck_docker__mutmut_13, 
        'xǁContainerManagerǁcheck_docker__mutmut_14': xǁContainerManagerǁcheck_docker__mutmut_14, 
        'xǁContainerManagerǁcheck_docker__mutmut_15': xǁContainerManagerǁcheck_docker__mutmut_15, 
        'xǁContainerManagerǁcheck_docker__mutmut_16': xǁContainerManagerǁcheck_docker__mutmut_16, 
        'xǁContainerManagerǁcheck_docker__mutmut_17': xǁContainerManagerǁcheck_docker__mutmut_17, 
        'xǁContainerManagerǁcheck_docker__mutmut_18': xǁContainerManagerǁcheck_docker__mutmut_18, 
        'xǁContainerManagerǁcheck_docker__mutmut_19': xǁContainerManagerǁcheck_docker__mutmut_19, 
        'xǁContainerManagerǁcheck_docker__mutmut_20': xǁContainerManagerǁcheck_docker__mutmut_20, 
        'xǁContainerManagerǁcheck_docker__mutmut_21': xǁContainerManagerǁcheck_docker__mutmut_21, 
        'xǁContainerManagerǁcheck_docker__mutmut_22': xǁContainerManagerǁcheck_docker__mutmut_22, 
        'xǁContainerManagerǁcheck_docker__mutmut_23': xǁContainerManagerǁcheck_docker__mutmut_23, 
        'xǁContainerManagerǁcheck_docker__mutmut_24': xǁContainerManagerǁcheck_docker__mutmut_24, 
        'xǁContainerManagerǁcheck_docker__mutmut_25': xǁContainerManagerǁcheck_docker__mutmut_25
    }
    
    def check_docker(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁcheck_docker__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁcheck_docker__mutmut_mutants"), args, kwargs, self)
        return result 
    
    check_docker.__signature__ = _mutmut_signature(xǁContainerManagerǁcheck_docker__mutmut_orig)
    xǁContainerManagerǁcheck_docker__mutmut_orig.__name__ = 'xǁContainerManagerǁcheck_docker'

    def xǁContainerManagerǁcontainer_exists__mutmut_orig(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_1(self) -> bool:
        """Check if the container exists."""
        try:
            result = None
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_2(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                None,
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_3(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=None,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_4(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=None,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_5(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_6(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_7(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_8(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["XXdockerXX", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_9(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["DOCKER", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_10(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "XXcontainerXX", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_11(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "CONTAINER", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_12(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "XXinspectXX", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_13(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "INSPECT", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_14(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=False,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_15(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=6,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_16(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode != 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_17(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 1
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_18(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(None)
            return False

    def xǁContainerManagerǁcontainer_exists__mutmut_19(self) -> bool:
        """Check if the container exists."""
        try:
            result = run(
                ["docker", "container", "inspect", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Container exists check failed: {e}")
            return True
    
    xǁContainerManagerǁcontainer_exists__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁcontainer_exists__mutmut_1': xǁContainerManagerǁcontainer_exists__mutmut_1, 
        'xǁContainerManagerǁcontainer_exists__mutmut_2': xǁContainerManagerǁcontainer_exists__mutmut_2, 
        'xǁContainerManagerǁcontainer_exists__mutmut_3': xǁContainerManagerǁcontainer_exists__mutmut_3, 
        'xǁContainerManagerǁcontainer_exists__mutmut_4': xǁContainerManagerǁcontainer_exists__mutmut_4, 
        'xǁContainerManagerǁcontainer_exists__mutmut_5': xǁContainerManagerǁcontainer_exists__mutmut_5, 
        'xǁContainerManagerǁcontainer_exists__mutmut_6': xǁContainerManagerǁcontainer_exists__mutmut_6, 
        'xǁContainerManagerǁcontainer_exists__mutmut_7': xǁContainerManagerǁcontainer_exists__mutmut_7, 
        'xǁContainerManagerǁcontainer_exists__mutmut_8': xǁContainerManagerǁcontainer_exists__mutmut_8, 
        'xǁContainerManagerǁcontainer_exists__mutmut_9': xǁContainerManagerǁcontainer_exists__mutmut_9, 
        'xǁContainerManagerǁcontainer_exists__mutmut_10': xǁContainerManagerǁcontainer_exists__mutmut_10, 
        'xǁContainerManagerǁcontainer_exists__mutmut_11': xǁContainerManagerǁcontainer_exists__mutmut_11, 
        'xǁContainerManagerǁcontainer_exists__mutmut_12': xǁContainerManagerǁcontainer_exists__mutmut_12, 
        'xǁContainerManagerǁcontainer_exists__mutmut_13': xǁContainerManagerǁcontainer_exists__mutmut_13, 
        'xǁContainerManagerǁcontainer_exists__mutmut_14': xǁContainerManagerǁcontainer_exists__mutmut_14, 
        'xǁContainerManagerǁcontainer_exists__mutmut_15': xǁContainerManagerǁcontainer_exists__mutmut_15, 
        'xǁContainerManagerǁcontainer_exists__mutmut_16': xǁContainerManagerǁcontainer_exists__mutmut_16, 
        'xǁContainerManagerǁcontainer_exists__mutmut_17': xǁContainerManagerǁcontainer_exists__mutmut_17, 
        'xǁContainerManagerǁcontainer_exists__mutmut_18': xǁContainerManagerǁcontainer_exists__mutmut_18, 
        'xǁContainerManagerǁcontainer_exists__mutmut_19': xǁContainerManagerǁcontainer_exists__mutmut_19
    }
    
    def container_exists(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁcontainer_exists__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁcontainer_exists__mutmut_mutants"), args, kwargs, self)
        return result 
    
    container_exists.__signature__ = _mutmut_signature(xǁContainerManagerǁcontainer_exists__mutmut_orig)
    xǁContainerManagerǁcontainer_exists__mutmut_orig.__name__ = 'xǁContainerManagerǁcontainer_exists'

    def xǁContainerManagerǁcontainer_running__mutmut_orig(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_1(self) -> bool:
        """Check if the container is currently running."""
        if self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_2(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return True

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_3(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = None
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_4(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                None,
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_5(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=None,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_6(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=None,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_7(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=None,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_8(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_9(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_10(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_11(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_12(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["XXdockerXX", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_13(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["DOCKER", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_14(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "XXcontainerXX", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_15(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "CONTAINER", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_16(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "XXinspectXX", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_17(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "INSPECT", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_18(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "XX-fXX", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_19(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-F", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_20(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "XX{{.State.Running}}XX", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_21(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.state.running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_22(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.STATE.RUNNING}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_23(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=False,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_24(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=False,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_25(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=6,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_26(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 or result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_27(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode != 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_28(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 1 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_29(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() != "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_30(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "XXtrueXX"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_31(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "TRUE"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_32(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(None)
            return False

    def xǁContainerManagerǁcontainer_running__mutmut_33(self) -> bool:
        """Check if the container is currently running."""
        if not self.container_exists():
            return False

        try:
            result = run(
                ["docker", "container", "inspect", "-f", "{{.State.Running}}", self.CONTAINER_NAME],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0 and result.stdout.strip() == "true"
        except Exception as e:
            logger.debug(f"Container running check failed: {e}")
            return True
    
    xǁContainerManagerǁcontainer_running__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁcontainer_running__mutmut_1': xǁContainerManagerǁcontainer_running__mutmut_1, 
        'xǁContainerManagerǁcontainer_running__mutmut_2': xǁContainerManagerǁcontainer_running__mutmut_2, 
        'xǁContainerManagerǁcontainer_running__mutmut_3': xǁContainerManagerǁcontainer_running__mutmut_3, 
        'xǁContainerManagerǁcontainer_running__mutmut_4': xǁContainerManagerǁcontainer_running__mutmut_4, 
        'xǁContainerManagerǁcontainer_running__mutmut_5': xǁContainerManagerǁcontainer_running__mutmut_5, 
        'xǁContainerManagerǁcontainer_running__mutmut_6': xǁContainerManagerǁcontainer_running__mutmut_6, 
        'xǁContainerManagerǁcontainer_running__mutmut_7': xǁContainerManagerǁcontainer_running__mutmut_7, 
        'xǁContainerManagerǁcontainer_running__mutmut_8': xǁContainerManagerǁcontainer_running__mutmut_8, 
        'xǁContainerManagerǁcontainer_running__mutmut_9': xǁContainerManagerǁcontainer_running__mutmut_9, 
        'xǁContainerManagerǁcontainer_running__mutmut_10': xǁContainerManagerǁcontainer_running__mutmut_10, 
        'xǁContainerManagerǁcontainer_running__mutmut_11': xǁContainerManagerǁcontainer_running__mutmut_11, 
        'xǁContainerManagerǁcontainer_running__mutmut_12': xǁContainerManagerǁcontainer_running__mutmut_12, 
        'xǁContainerManagerǁcontainer_running__mutmut_13': xǁContainerManagerǁcontainer_running__mutmut_13, 
        'xǁContainerManagerǁcontainer_running__mutmut_14': xǁContainerManagerǁcontainer_running__mutmut_14, 
        'xǁContainerManagerǁcontainer_running__mutmut_15': xǁContainerManagerǁcontainer_running__mutmut_15, 
        'xǁContainerManagerǁcontainer_running__mutmut_16': xǁContainerManagerǁcontainer_running__mutmut_16, 
        'xǁContainerManagerǁcontainer_running__mutmut_17': xǁContainerManagerǁcontainer_running__mutmut_17, 
        'xǁContainerManagerǁcontainer_running__mutmut_18': xǁContainerManagerǁcontainer_running__mutmut_18, 
        'xǁContainerManagerǁcontainer_running__mutmut_19': xǁContainerManagerǁcontainer_running__mutmut_19, 
        'xǁContainerManagerǁcontainer_running__mutmut_20': xǁContainerManagerǁcontainer_running__mutmut_20, 
        'xǁContainerManagerǁcontainer_running__mutmut_21': xǁContainerManagerǁcontainer_running__mutmut_21, 
        'xǁContainerManagerǁcontainer_running__mutmut_22': xǁContainerManagerǁcontainer_running__mutmut_22, 
        'xǁContainerManagerǁcontainer_running__mutmut_23': xǁContainerManagerǁcontainer_running__mutmut_23, 
        'xǁContainerManagerǁcontainer_running__mutmut_24': xǁContainerManagerǁcontainer_running__mutmut_24, 
        'xǁContainerManagerǁcontainer_running__mutmut_25': xǁContainerManagerǁcontainer_running__mutmut_25, 
        'xǁContainerManagerǁcontainer_running__mutmut_26': xǁContainerManagerǁcontainer_running__mutmut_26, 
        'xǁContainerManagerǁcontainer_running__mutmut_27': xǁContainerManagerǁcontainer_running__mutmut_27, 
        'xǁContainerManagerǁcontainer_running__mutmut_28': xǁContainerManagerǁcontainer_running__mutmut_28, 
        'xǁContainerManagerǁcontainer_running__mutmut_29': xǁContainerManagerǁcontainer_running__mutmut_29, 
        'xǁContainerManagerǁcontainer_running__mutmut_30': xǁContainerManagerǁcontainer_running__mutmut_30, 
        'xǁContainerManagerǁcontainer_running__mutmut_31': xǁContainerManagerǁcontainer_running__mutmut_31, 
        'xǁContainerManagerǁcontainer_running__mutmut_32': xǁContainerManagerǁcontainer_running__mutmut_32, 
        'xǁContainerManagerǁcontainer_running__mutmut_33': xǁContainerManagerǁcontainer_running__mutmut_33
    }
    
    def container_running(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁcontainer_running__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁcontainer_running__mutmut_mutants"), args, kwargs, self)
        return result 
    
    container_running.__signature__ = _mutmut_signature(xǁContainerManagerǁcontainer_running__mutmut_orig)
    xǁContainerManagerǁcontainer_running__mutmut_orig.__name__ = 'xǁContainerManagerǁcontainer_running'

    def xǁContainerManagerǁimage_exists__mutmut_orig(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_1(self) -> bool:
        """Check if the container image exists."""
        try:
            result = None
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_2(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                None,
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_3(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=None,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_4(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=None,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_5(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_6(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_7(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_8(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["XXdockerXX", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_9(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["DOCKER", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_10(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "XXimageXX", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_11(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "IMAGE", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_12(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "XXinspectXX", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_13(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "INSPECT", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_14(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=False,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_15(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=6,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_16(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode != 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_17(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 1
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return False

    def xǁContainerManagerǁimage_exists__mutmut_18(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(None)
            return False

    def xǁContainerManagerǁimage_exists__mutmut_19(self) -> bool:
        """Check if the container image exists."""
        try:
            result = run(
                ["docker", "image", "inspect", self.full_image],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Image exists check failed: {e}")
            return True
    
    xǁContainerManagerǁimage_exists__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁimage_exists__mutmut_1': xǁContainerManagerǁimage_exists__mutmut_1, 
        'xǁContainerManagerǁimage_exists__mutmut_2': xǁContainerManagerǁimage_exists__mutmut_2, 
        'xǁContainerManagerǁimage_exists__mutmut_3': xǁContainerManagerǁimage_exists__mutmut_3, 
        'xǁContainerManagerǁimage_exists__mutmut_4': xǁContainerManagerǁimage_exists__mutmut_4, 
        'xǁContainerManagerǁimage_exists__mutmut_5': xǁContainerManagerǁimage_exists__mutmut_5, 
        'xǁContainerManagerǁimage_exists__mutmut_6': xǁContainerManagerǁimage_exists__mutmut_6, 
        'xǁContainerManagerǁimage_exists__mutmut_7': xǁContainerManagerǁimage_exists__mutmut_7, 
        'xǁContainerManagerǁimage_exists__mutmut_8': xǁContainerManagerǁimage_exists__mutmut_8, 
        'xǁContainerManagerǁimage_exists__mutmut_9': xǁContainerManagerǁimage_exists__mutmut_9, 
        'xǁContainerManagerǁimage_exists__mutmut_10': xǁContainerManagerǁimage_exists__mutmut_10, 
        'xǁContainerManagerǁimage_exists__mutmut_11': xǁContainerManagerǁimage_exists__mutmut_11, 
        'xǁContainerManagerǁimage_exists__mutmut_12': xǁContainerManagerǁimage_exists__mutmut_12, 
        'xǁContainerManagerǁimage_exists__mutmut_13': xǁContainerManagerǁimage_exists__mutmut_13, 
        'xǁContainerManagerǁimage_exists__mutmut_14': xǁContainerManagerǁimage_exists__mutmut_14, 
        'xǁContainerManagerǁimage_exists__mutmut_15': xǁContainerManagerǁimage_exists__mutmut_15, 
        'xǁContainerManagerǁimage_exists__mutmut_16': xǁContainerManagerǁimage_exists__mutmut_16, 
        'xǁContainerManagerǁimage_exists__mutmut_17': xǁContainerManagerǁimage_exists__mutmut_17, 
        'xǁContainerManagerǁimage_exists__mutmut_18': xǁContainerManagerǁimage_exists__mutmut_18, 
        'xǁContainerManagerǁimage_exists__mutmut_19': xǁContainerManagerǁimage_exists__mutmut_19
    }
    
    def image_exists(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁimage_exists__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁimage_exists__mutmut_mutants"), args, kwargs, self)
        return result 
    
    image_exists.__signature__ = _mutmut_signature(xǁContainerManagerǁimage_exists__mutmut_orig)
    xǁContainerManagerǁimage_exists__mutmut_orig.__name__ = 'xǁContainerManagerǁimage_exists'

    def xǁContainerManagerǁget_volume_mappings__mutmut_orig(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_1(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = None
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_2(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path(None)
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_3(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("XXvolumesXX")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_4(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("VOLUMES")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_5(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = None

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_6(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = None
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_7(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base * volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_8(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = None
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_9(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = None

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_10(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(None)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_11(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = None

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_12(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(None)] = "/workspace"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_13(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "XX/workspaceXX"

        return mappings

    def xǁContainerManagerǁget_volume_mappings__mutmut_14(self) -> dict[str, str]:
        """Get volume mappings for the container."""
        # Use configured volume mappings if available
        if self.container_config.volume_mappings:
            return self.container_config.volume_mappings.copy()

        # Default volume mappings
        volumes_base = self.get_container_path("volumes")
        mappings = {}

        # Map persistent volumes
        for volume_name in self.container_config.persistent_volumes:
            host_path = volumes_base / volume_name
            container_path = f"/wrknv/{volume_name}"
            mappings[str(host_path)] = container_path

        # Add current working directory mapping
        mappings[str(Path.cwd())] = "/WORKSPACE"

        return mappings
    
    xǁContainerManagerǁget_volume_mappings__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerManagerǁget_volume_mappings__mutmut_1': xǁContainerManagerǁget_volume_mappings__mutmut_1, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_2': xǁContainerManagerǁget_volume_mappings__mutmut_2, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_3': xǁContainerManagerǁget_volume_mappings__mutmut_3, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_4': xǁContainerManagerǁget_volume_mappings__mutmut_4, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_5': xǁContainerManagerǁget_volume_mappings__mutmut_5, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_6': xǁContainerManagerǁget_volume_mappings__mutmut_6, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_7': xǁContainerManagerǁget_volume_mappings__mutmut_7, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_8': xǁContainerManagerǁget_volume_mappings__mutmut_8, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_9': xǁContainerManagerǁget_volume_mappings__mutmut_9, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_10': xǁContainerManagerǁget_volume_mappings__mutmut_10, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_11': xǁContainerManagerǁget_volume_mappings__mutmut_11, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_12': xǁContainerManagerǁget_volume_mappings__mutmut_12, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_13': xǁContainerManagerǁget_volume_mappings__mutmut_13, 
        'xǁContainerManagerǁget_volume_mappings__mutmut_14': xǁContainerManagerǁget_volume_mappings__mutmut_14
    }
    
    def get_volume_mappings(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerManagerǁget_volume_mappings__mutmut_orig"), object.__getattribute__(self, "xǁContainerManagerǁget_volume_mappings__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_volume_mappings.__signature__ = _mutmut_signature(xǁContainerManagerǁget_volume_mappings__mutmut_orig)
    xǁContainerManagerǁget_volume_mappings__mutmut_orig.__name__ = 'xǁContainerManagerǁget_volume_mappings'


# 🧰🌍🔚
