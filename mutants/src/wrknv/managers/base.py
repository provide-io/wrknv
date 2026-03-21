#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Base Tool Manager for wrknv
=============================
Common functionality for all tool managers."""

from __future__ import annotations

from abc import ABC, abstractmethod
import pathlib
import platform
from urllib.parse import urlparse

from provide.foundation.console.output import pout
from provide.foundation.file import safe_delete, safe_rmtree
from provide.foundation.logger import get_logger
from provide.foundation.process import run

from wrknv.config import WorkenvConfig
from wrknv.errors import WrkenvError

logger = get_logger(__name__)
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


class ToolManagerError(WrkenvError):
    """Raised when there's an error in tool management."""


class BaseToolManager(ABC):
    """Base class for all tool managers in wrknv."""

    def xǁBaseToolManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        self.config = None
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        self.config = config and WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_3(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = None
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_4(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            None
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_5(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting(None, "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_6(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", None)
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_7(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_8(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", )
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_9(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("XXinstall_pathXX", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_10(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("INSTALL_PATH", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_11(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "XX~/.wrknv/toolsXX")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_12(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.WRKNV/TOOLS")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_13(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = None

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_14(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent * "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_15(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "XXcacheXX"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_16(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "CACHE"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_17(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=None, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_18(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=None)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_19(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_20(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, )
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_21(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=False, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_22(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=False)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_23(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=None, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_24(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=None)

    def xǁBaseToolManagerǁ__init____mutmut_25(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_26(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, )

    def xǁBaseToolManagerǁ__init____mutmut_27(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=False, exist_ok=True)

    def xǁBaseToolManagerǁ__init____mutmut_28(self, config: WorkenvConfig | None = None) -> None:
        self.config = config or WorkenvConfig.load()
        self.install_path = pathlib.Path(
            self.config.get_setting("install_path", "~/.wrknv/tools")
        ).expanduser()
        self.cache_dir = self.install_path.parent / "cache"

        # Ensure directories exist
        self.install_path.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=False)
    
    xǁBaseToolManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁ__init____mutmut_1': xǁBaseToolManagerǁ__init____mutmut_1, 
        'xǁBaseToolManagerǁ__init____mutmut_2': xǁBaseToolManagerǁ__init____mutmut_2, 
        'xǁBaseToolManagerǁ__init____mutmut_3': xǁBaseToolManagerǁ__init____mutmut_3, 
        'xǁBaseToolManagerǁ__init____mutmut_4': xǁBaseToolManagerǁ__init____mutmut_4, 
        'xǁBaseToolManagerǁ__init____mutmut_5': xǁBaseToolManagerǁ__init____mutmut_5, 
        'xǁBaseToolManagerǁ__init____mutmut_6': xǁBaseToolManagerǁ__init____mutmut_6, 
        'xǁBaseToolManagerǁ__init____mutmut_7': xǁBaseToolManagerǁ__init____mutmut_7, 
        'xǁBaseToolManagerǁ__init____mutmut_8': xǁBaseToolManagerǁ__init____mutmut_8, 
        'xǁBaseToolManagerǁ__init____mutmut_9': xǁBaseToolManagerǁ__init____mutmut_9, 
        'xǁBaseToolManagerǁ__init____mutmut_10': xǁBaseToolManagerǁ__init____mutmut_10, 
        'xǁBaseToolManagerǁ__init____mutmut_11': xǁBaseToolManagerǁ__init____mutmut_11, 
        'xǁBaseToolManagerǁ__init____mutmut_12': xǁBaseToolManagerǁ__init____mutmut_12, 
        'xǁBaseToolManagerǁ__init____mutmut_13': xǁBaseToolManagerǁ__init____mutmut_13, 
        'xǁBaseToolManagerǁ__init____mutmut_14': xǁBaseToolManagerǁ__init____mutmut_14, 
        'xǁBaseToolManagerǁ__init____mutmut_15': xǁBaseToolManagerǁ__init____mutmut_15, 
        'xǁBaseToolManagerǁ__init____mutmut_16': xǁBaseToolManagerǁ__init____mutmut_16, 
        'xǁBaseToolManagerǁ__init____mutmut_17': xǁBaseToolManagerǁ__init____mutmut_17, 
        'xǁBaseToolManagerǁ__init____mutmut_18': xǁBaseToolManagerǁ__init____mutmut_18, 
        'xǁBaseToolManagerǁ__init____mutmut_19': xǁBaseToolManagerǁ__init____mutmut_19, 
        'xǁBaseToolManagerǁ__init____mutmut_20': xǁBaseToolManagerǁ__init____mutmut_20, 
        'xǁBaseToolManagerǁ__init____mutmut_21': xǁBaseToolManagerǁ__init____mutmut_21, 
        'xǁBaseToolManagerǁ__init____mutmut_22': xǁBaseToolManagerǁ__init____mutmut_22, 
        'xǁBaseToolManagerǁ__init____mutmut_23': xǁBaseToolManagerǁ__init____mutmut_23, 
        'xǁBaseToolManagerǁ__init____mutmut_24': xǁBaseToolManagerǁ__init____mutmut_24, 
        'xǁBaseToolManagerǁ__init____mutmut_25': xǁBaseToolManagerǁ__init____mutmut_25, 
        'xǁBaseToolManagerǁ__init____mutmut_26': xǁBaseToolManagerǁ__init____mutmut_26, 
        'xǁBaseToolManagerǁ__init____mutmut_27': xǁBaseToolManagerǁ__init____mutmut_27, 
        'xǁBaseToolManagerǁ__init____mutmut_28': xǁBaseToolManagerǁ__init____mutmut_28
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBaseToolManagerǁ__init____mutmut_orig)
    xǁBaseToolManagerǁ__init____mutmut_orig.__name__ = 'xǁBaseToolManagerǁ__init__'

    @property
    @abstractmethod
    def tool_name(self) -> str:
        """Name of the tool being managed."""

    @property
    @abstractmethod
    def executable_name(self) -> str:
        """Name of the executable binary."""

    @abstractmethod
    def get_available_versions(self) -> list[str]:
        """Get list of available versions from upstream."""

    @abstractmethod
    def get_download_url(self, version: str) -> str:
        """Get download URL for a specific version."""

    @abstractmethod
    def get_checksum_url(self, version: str) -> str | None:
        """Get checksum URL for verification (if available)."""

    def get_platform_info(self) -> dict[str, str]:
        """Get current platform information."""
        from wrknv.wenv.operations.platform import get_platform_info

        return get_platform_info()

    def xǁBaseToolManagerǁget_installed_version__mutmut_orig(self) -> str | None:
        """Get currently installed version from config."""
        return self.config.get_tool_version(self.tool_name)

    def xǁBaseToolManagerǁget_installed_version__mutmut_1(self) -> str | None:
        """Get currently installed version from config."""
        return self.config.get_tool_version(None)
    
    xǁBaseToolManagerǁget_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁget_installed_version__mutmut_1': xǁBaseToolManagerǁget_installed_version__mutmut_1
    }
    
    def get_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁget_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁget_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_version.__signature__ = _mutmut_signature(xǁBaseToolManagerǁget_installed_version__mutmut_orig)
    xǁBaseToolManagerǁget_installed_version__mutmut_orig.__name__ = 'xǁBaseToolManagerǁget_installed_version'

    def xǁBaseToolManagerǁset_installed_version__mutmut_orig(self, version: str) -> None:
        """Set the installed version in config.

        Base implementation is a no-op since config doesn't support writing.
        Subclasses should override this to persist version information.
        """
        if logger.is_debug_enabled():
            logger.debug(
                f"Would set {self.tool_name} version to {version} (base implementation - no persistence)"
            )

    def xǁBaseToolManagerǁset_installed_version__mutmut_1(self, version: str) -> None:
        """Set the installed version in config.

        Base implementation is a no-op since config doesn't support writing.
        Subclasses should override this to persist version information.
        """
        if logger.is_debug_enabled():
            logger.debug(
                None
            )
    
    xǁBaseToolManagerǁset_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁset_installed_version__mutmut_1': xǁBaseToolManagerǁset_installed_version__mutmut_1
    }
    
    def set_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁset_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁset_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_installed_version.__signature__ = _mutmut_signature(xǁBaseToolManagerǁset_installed_version__mutmut_orig)
    xǁBaseToolManagerǁset_installed_version__mutmut_orig.__name__ = 'xǁBaseToolManagerǁset_installed_version'

    def xǁBaseToolManagerǁget_binary_path__mutmut_orig(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_1(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = None

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_2(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name * version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_3(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path * self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_4(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = None
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_5(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() != "Windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_6(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "XXWindowsXX":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_7(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "windows":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_8(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "WINDOWS":
            executable += ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_9(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable = ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_10(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable -= ".exe"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_11(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += "XX.exeXX"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_12(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".EXE"

        return tool_dir / "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_13(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "bin" * executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_14(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir * "bin" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_15(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "XXbinXX" / executable

    def xǁBaseToolManagerǁget_binary_path__mutmut_16(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        tool_dir = self.install_path / self.tool_name / version

        # Handle platform-specific executable names
        executable = self.executable_name
        if platform.system() == "Windows":
            executable += ".exe"

        return tool_dir / "BIN" / executable
    
    xǁBaseToolManagerǁget_binary_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁget_binary_path__mutmut_1': xǁBaseToolManagerǁget_binary_path__mutmut_1, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_2': xǁBaseToolManagerǁget_binary_path__mutmut_2, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_3': xǁBaseToolManagerǁget_binary_path__mutmut_3, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_4': xǁBaseToolManagerǁget_binary_path__mutmut_4, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_5': xǁBaseToolManagerǁget_binary_path__mutmut_5, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_6': xǁBaseToolManagerǁget_binary_path__mutmut_6, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_7': xǁBaseToolManagerǁget_binary_path__mutmut_7, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_8': xǁBaseToolManagerǁget_binary_path__mutmut_8, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_9': xǁBaseToolManagerǁget_binary_path__mutmut_9, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_10': xǁBaseToolManagerǁget_binary_path__mutmut_10, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_11': xǁBaseToolManagerǁget_binary_path__mutmut_11, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_12': xǁBaseToolManagerǁget_binary_path__mutmut_12, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_13': xǁBaseToolManagerǁget_binary_path__mutmut_13, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_14': xǁBaseToolManagerǁget_binary_path__mutmut_14, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_15': xǁBaseToolManagerǁget_binary_path__mutmut_15, 
        'xǁBaseToolManagerǁget_binary_path__mutmut_16': xǁBaseToolManagerǁget_binary_path__mutmut_16
    }
    
    def get_binary_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁget_binary_path__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁget_binary_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_binary_path.__signature__ = _mutmut_signature(xǁBaseToolManagerǁget_binary_path__mutmut_orig)
    xǁBaseToolManagerǁget_binary_path__mutmut_orig.__name__ = 'xǁBaseToolManagerǁget_binary_path'

    def xǁBaseToolManagerǁget_current_binary_path__mutmut_orig(self) -> pathlib.Path | None:
        """Get path to the currently active binary."""
        version = self.get_installed_version()
        if version:
            return self.get_binary_path(version)
        return None

    def xǁBaseToolManagerǁget_current_binary_path__mutmut_1(self) -> pathlib.Path | None:
        """Get path to the currently active binary."""
        version = None
        if version:
            return self.get_binary_path(version)
        return None

    def xǁBaseToolManagerǁget_current_binary_path__mutmut_2(self) -> pathlib.Path | None:
        """Get path to the currently active binary."""
        version = self.get_installed_version()
        if version:
            return self.get_binary_path(None)
        return None
    
    xǁBaseToolManagerǁget_current_binary_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁget_current_binary_path__mutmut_1': xǁBaseToolManagerǁget_current_binary_path__mutmut_1, 
        'xǁBaseToolManagerǁget_current_binary_path__mutmut_2': xǁBaseToolManagerǁget_current_binary_path__mutmut_2
    }
    
    def get_current_binary_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁget_current_binary_path__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁget_current_binary_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_current_binary_path.__signature__ = _mutmut_signature(xǁBaseToolManagerǁget_current_binary_path__mutmut_orig)
    xǁBaseToolManagerǁget_current_binary_path__mutmut_orig.__name__ = 'xǁBaseToolManagerǁget_current_binary_path'

    def xǁBaseToolManagerǁcreate_symlink__mutmut_orig(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_1(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = None
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_2(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_3(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_4(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(None)
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_5(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = None
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_6(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path * "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_7(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "XXbinXX"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_8(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "BIN"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_9(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=None)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_10(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=False)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_11(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = None

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_12(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir * self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_13(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() and symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_14(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(None, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_15(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=None)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_16(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_17(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, )

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_18(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=False)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_19(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(None)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_20(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(None)
        except OSError as e:
            logger.warning(f"Could not create symlink: {e}")

    def xǁBaseToolManagerǁcreate_symlink__mutmut_21(self, version: str) -> None:
        """Create symlink to make tool available in PATH."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping symlink creation")
            return

        # Create symlink in ~/.wrknv/tools/bin/
        bin_dir = self.install_path / "bin"
        bin_dir.mkdir(exist_ok=True)

        symlink_path = bin_dir / self.executable_name

        # Remove existing symlink
        if symlink_path.exists() or symlink_path.is_symlink():
            safe_delete(symlink_path, missing_ok=True)

        try:
            symlink_path.symlink_to(binary_path)
            logger.info(f"Created symlink: {symlink_path} -> {binary_path}")
        except OSError as e:
            logger.warning(None)
    
    xǁBaseToolManagerǁcreate_symlink__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁcreate_symlink__mutmut_1': xǁBaseToolManagerǁcreate_symlink__mutmut_1, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_2': xǁBaseToolManagerǁcreate_symlink__mutmut_2, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_3': xǁBaseToolManagerǁcreate_symlink__mutmut_3, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_4': xǁBaseToolManagerǁcreate_symlink__mutmut_4, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_5': xǁBaseToolManagerǁcreate_symlink__mutmut_5, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_6': xǁBaseToolManagerǁcreate_symlink__mutmut_6, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_7': xǁBaseToolManagerǁcreate_symlink__mutmut_7, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_8': xǁBaseToolManagerǁcreate_symlink__mutmut_8, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_9': xǁBaseToolManagerǁcreate_symlink__mutmut_9, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_10': xǁBaseToolManagerǁcreate_symlink__mutmut_10, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_11': xǁBaseToolManagerǁcreate_symlink__mutmut_11, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_12': xǁBaseToolManagerǁcreate_symlink__mutmut_12, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_13': xǁBaseToolManagerǁcreate_symlink__mutmut_13, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_14': xǁBaseToolManagerǁcreate_symlink__mutmut_14, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_15': xǁBaseToolManagerǁcreate_symlink__mutmut_15, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_16': xǁBaseToolManagerǁcreate_symlink__mutmut_16, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_17': xǁBaseToolManagerǁcreate_symlink__mutmut_17, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_18': xǁBaseToolManagerǁcreate_symlink__mutmut_18, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_19': xǁBaseToolManagerǁcreate_symlink__mutmut_19, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_20': xǁBaseToolManagerǁcreate_symlink__mutmut_20, 
        'xǁBaseToolManagerǁcreate_symlink__mutmut_21': xǁBaseToolManagerǁcreate_symlink__mutmut_21
    }
    
    def create_symlink(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁcreate_symlink__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁcreate_symlink__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_symlink.__signature__ = _mutmut_signature(xǁBaseToolManagerǁcreate_symlink__mutmut_orig)
    xǁBaseToolManagerǁcreate_symlink__mutmut_orig.__name__ = 'xǁBaseToolManagerǁcreate_symlink'

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_orig(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, destination, show_progress, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_1(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = False,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, destination, show_progress, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_2(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(None, destination, show_progress, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_3(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, None, show_progress, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_4(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, destination, None, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_5(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, destination, show_progress, None)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_6(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(destination, show_progress, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_7(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, show_progress, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_8(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, destination, headers)

    async def xǁBaseToolManagerǁdownload_file_async__mutmut_9(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file asynchronously using foundation transport.

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file_async

        await download_file_async(url, destination, show_progress, )
    
    xǁBaseToolManagerǁdownload_file_async__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁdownload_file_async__mutmut_1': xǁBaseToolManagerǁdownload_file_async__mutmut_1, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_2': xǁBaseToolManagerǁdownload_file_async__mutmut_2, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_3': xǁBaseToolManagerǁdownload_file_async__mutmut_3, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_4': xǁBaseToolManagerǁdownload_file_async__mutmut_4, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_5': xǁBaseToolManagerǁdownload_file_async__mutmut_5, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_6': xǁBaseToolManagerǁdownload_file_async__mutmut_6, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_7': xǁBaseToolManagerǁdownload_file_async__mutmut_7, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_8': xǁBaseToolManagerǁdownload_file_async__mutmut_8, 
        'xǁBaseToolManagerǁdownload_file_async__mutmut_9': xǁBaseToolManagerǁdownload_file_async__mutmut_9
    }
    
    def download_file_async(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁdownload_file_async__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁdownload_file_async__mutmut_mutants"), args, kwargs, self)
        return result 
    
    download_file_async.__signature__ = _mutmut_signature(xǁBaseToolManagerǁdownload_file_async__mutmut_orig)
    xǁBaseToolManagerǁdownload_file_async__mutmut_orig.__name__ = 'xǁBaseToolManagerǁdownload_file_async'

    def xǁBaseToolManagerǁdownload_file__mutmut_orig(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, destination, show_progress, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_1(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = False,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, destination, show_progress, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_2(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(None, destination, show_progress, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_3(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, None, show_progress, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_4(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, destination, None, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_5(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, destination, show_progress, None)

    def xǁBaseToolManagerǁdownload_file__mutmut_6(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(destination, show_progress, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_7(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, show_progress, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_8(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, destination, headers)

    def xǁBaseToolManagerǁdownload_file__mutmut_9(
        self,
        url: str,
        destination: pathlib.Path,
        show_progress: bool = True,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Download a file with optional progress display (sync wrapper).

        Args:
            url: URL to download from
            destination: Where to save the file
            show_progress: Whether to log progress
            headers: Optional custom headers
        """
        from wrknv.wenv.operations.download import download_file

        download_file(url, destination, show_progress, )
    
    xǁBaseToolManagerǁdownload_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁdownload_file__mutmut_1': xǁBaseToolManagerǁdownload_file__mutmut_1, 
        'xǁBaseToolManagerǁdownload_file__mutmut_2': xǁBaseToolManagerǁdownload_file__mutmut_2, 
        'xǁBaseToolManagerǁdownload_file__mutmut_3': xǁBaseToolManagerǁdownload_file__mutmut_3, 
        'xǁBaseToolManagerǁdownload_file__mutmut_4': xǁBaseToolManagerǁdownload_file__mutmut_4, 
        'xǁBaseToolManagerǁdownload_file__mutmut_5': xǁBaseToolManagerǁdownload_file__mutmut_5, 
        'xǁBaseToolManagerǁdownload_file__mutmut_6': xǁBaseToolManagerǁdownload_file__mutmut_6, 
        'xǁBaseToolManagerǁdownload_file__mutmut_7': xǁBaseToolManagerǁdownload_file__mutmut_7, 
        'xǁBaseToolManagerǁdownload_file__mutmut_8': xǁBaseToolManagerǁdownload_file__mutmut_8, 
        'xǁBaseToolManagerǁdownload_file__mutmut_9': xǁBaseToolManagerǁdownload_file__mutmut_9
    }
    
    def download_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁdownload_file__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁdownload_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    download_file.__signature__ = _mutmut_signature(xǁBaseToolManagerǁdownload_file__mutmut_orig)
    xǁBaseToolManagerǁdownload_file__mutmut_orig.__name__ = 'xǁBaseToolManagerǁdownload_file'

    def xǁBaseToolManagerǁverify_checksum__mutmut_orig(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_1(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "XXsha256XX"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_2(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "SHA256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_3(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_4(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting(None, True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_5(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", None):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_6(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting(True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_7(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", ):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_8(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("XXverify_checksumsXX", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_9(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("VERIFY_CHECKSUMS", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_10(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", False):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_11(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug(None)
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_12(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("XXChecksum verification disabledXX")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_13(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_14(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("CHECKSUM VERIFICATION DISABLED")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_15(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return False

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_16(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(None, expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_17(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, None, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_18(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, None)

    def xǁBaseToolManagerǁverify_checksum__mutmut_19(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(expected_checksum, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_20(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, algorithm)

    def xǁBaseToolManagerǁverify_checksum__mutmut_21(
        self, file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify file checksum."""
        if not self.config.get_setting("verify_checksums", True):
            logger.debug("Checksum verification disabled")
            return True

        from wrknv.wenv.operations.download import verify_checksum

        return verify_checksum(file_path, expected_checksum, )
    
    xǁBaseToolManagerǁverify_checksum__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁverify_checksum__mutmut_1': xǁBaseToolManagerǁverify_checksum__mutmut_1, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_2': xǁBaseToolManagerǁverify_checksum__mutmut_2, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_3': xǁBaseToolManagerǁverify_checksum__mutmut_3, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_4': xǁBaseToolManagerǁverify_checksum__mutmut_4, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_5': xǁBaseToolManagerǁverify_checksum__mutmut_5, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_6': xǁBaseToolManagerǁverify_checksum__mutmut_6, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_7': xǁBaseToolManagerǁverify_checksum__mutmut_7, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_8': xǁBaseToolManagerǁverify_checksum__mutmut_8, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_9': xǁBaseToolManagerǁverify_checksum__mutmut_9, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_10': xǁBaseToolManagerǁverify_checksum__mutmut_10, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_11': xǁBaseToolManagerǁverify_checksum__mutmut_11, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_12': xǁBaseToolManagerǁverify_checksum__mutmut_12, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_13': xǁBaseToolManagerǁverify_checksum__mutmut_13, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_14': xǁBaseToolManagerǁverify_checksum__mutmut_14, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_15': xǁBaseToolManagerǁverify_checksum__mutmut_15, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_16': xǁBaseToolManagerǁverify_checksum__mutmut_16, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_17': xǁBaseToolManagerǁverify_checksum__mutmut_17, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_18': xǁBaseToolManagerǁverify_checksum__mutmut_18, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_19': xǁBaseToolManagerǁverify_checksum__mutmut_19, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_20': xǁBaseToolManagerǁverify_checksum__mutmut_20, 
        'xǁBaseToolManagerǁverify_checksum__mutmut_21': xǁBaseToolManagerǁverify_checksum__mutmut_21
    }
    
    def verify_checksum(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁverify_checksum__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁverify_checksum__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_checksum.__signature__ = _mutmut_signature(xǁBaseToolManagerǁverify_checksum__mutmut_orig)
    xǁBaseToolManagerǁverify_checksum__mutmut_orig.__name__ = 'xǁBaseToolManagerǁverify_checksum'

    def xǁBaseToolManagerǁextract_archive__mutmut_orig(self, archive_path: pathlib.Path, extract_to: pathlib.Path) -> None:
        """Extract an archive file."""
        from wrknv.wenv.operations.install import extract_archive

        extract_archive(archive_path, extract_to)

    def xǁBaseToolManagerǁextract_archive__mutmut_1(self, archive_path: pathlib.Path, extract_to: pathlib.Path) -> None:
        """Extract an archive file."""
        from wrknv.wenv.operations.install import extract_archive

        extract_archive(None, extract_to)

    def xǁBaseToolManagerǁextract_archive__mutmut_2(self, archive_path: pathlib.Path, extract_to: pathlib.Path) -> None:
        """Extract an archive file."""
        from wrknv.wenv.operations.install import extract_archive

        extract_archive(archive_path, None)

    def xǁBaseToolManagerǁextract_archive__mutmut_3(self, archive_path: pathlib.Path, extract_to: pathlib.Path) -> None:
        """Extract an archive file."""
        from wrknv.wenv.operations.install import extract_archive

        extract_archive(extract_to)

    def xǁBaseToolManagerǁextract_archive__mutmut_4(self, archive_path: pathlib.Path, extract_to: pathlib.Path) -> None:
        """Extract an archive file."""
        from wrknv.wenv.operations.install import extract_archive

        extract_archive(archive_path, )
    
    xǁBaseToolManagerǁextract_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁextract_archive__mutmut_1': xǁBaseToolManagerǁextract_archive__mutmut_1, 
        'xǁBaseToolManagerǁextract_archive__mutmut_2': xǁBaseToolManagerǁextract_archive__mutmut_2, 
        'xǁBaseToolManagerǁextract_archive__mutmut_3': xǁBaseToolManagerǁextract_archive__mutmut_3, 
        'xǁBaseToolManagerǁextract_archive__mutmut_4': xǁBaseToolManagerǁextract_archive__mutmut_4
    }
    
    def extract_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁextract_archive__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁextract_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    extract_archive.__signature__ = _mutmut_signature(xǁBaseToolManagerǁextract_archive__mutmut_orig)
    xǁBaseToolManagerǁextract_archive__mutmut_orig.__name__ = 'xǁBaseToolManagerǁextract_archive'

    def xǁBaseToolManagerǁmake_executable__mutmut_orig(self, file_path: pathlib.Path) -> None:
        """Make a file executable (Unix systems)."""
        from wrknv.wenv.operations.install import make_executable

        make_executable(file_path)

    def xǁBaseToolManagerǁmake_executable__mutmut_1(self, file_path: pathlib.Path) -> None:
        """Make a file executable (Unix systems)."""
        from wrknv.wenv.operations.install import make_executable

        make_executable(None)
    
    xǁBaseToolManagerǁmake_executable__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁmake_executable__mutmut_1': xǁBaseToolManagerǁmake_executable__mutmut_1
    }
    
    def make_executable(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁmake_executable__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁmake_executable__mutmut_mutants"), args, kwargs, self)
        return result 
    
    make_executable.__signature__ = _mutmut_signature(xǁBaseToolManagerǁmake_executable__mutmut_orig)
    xǁBaseToolManagerǁmake_executable__mutmut_orig.__name__ = 'xǁBaseToolManagerǁmake_executable'

    def xǁBaseToolManagerǁinstall_version__mutmut_orig(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_1(self, version: str, dry_run: bool = True) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_2(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(None)
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_3(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(None)

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_4(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = None
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_5(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(None)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_6(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(None)
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_7(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(None)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_8(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting(None, True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_9(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", None):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_10(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting(True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_11(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", ):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_12(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("XXcreate_symlinksXX", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_13(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("CREATE_SYMLINKS", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_14(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", False):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_15(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(None)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_16(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = None
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_17(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(None)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_18(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = None
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_19(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(None).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_20(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(None).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_21(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = None

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_22(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir * filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_23(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() and not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_24(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_25(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_26(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting(None, True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_27(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", None):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_28(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting(True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_29(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", ):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_30(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("XXcache_downloadsXX", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_31(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("CACHE_DOWNLOADS", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_32(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", False):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_33(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(None, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_34(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, None)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_35(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_36(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, )
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_37(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(None)

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_38(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = None
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_39(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(None)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_40(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url or self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_41(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting(None, True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_42(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", None):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_43(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting(True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_44(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", ):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_45(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("XXverify_checksumsXX", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_46(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("VERIFY_CHECKSUMS", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_47(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", False):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_48(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(None, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_49(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, None)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_50(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_51(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, )

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_52(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(None, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_53(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, None)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_54(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_55(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, )

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_56(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(None)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_57(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting(None, True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_58(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", None):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_59(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting(True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_60(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", ):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_61(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("XXcreate_symlinksXX", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_62(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("CREATE_SYMLINKS", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_63(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", False):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_64(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(None)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_65(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting(None, True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_66(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", None):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_67(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting(True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_68(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", ):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_69(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("XXclean_on_failureXX", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_70(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("CLEAN_ON_FAILURE", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_71(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", False):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_72(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(None)

            raise ToolManagerError(f"Failed to install {self.tool_name} {version}: {e}") from e

    def xǁBaseToolManagerǁinstall_version__mutmut_73(self, version: str, dry_run: bool = False) -> None:
        """Install a specific version of the tool."""
        if dry_run:
            logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        logger.info(f"Installing {self.tool_name} {version}")

        # Check if already installed
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.info(f"{self.tool_name} {version} is already installed at {binary_path}")
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)
            return

        try:
            # Download
            download_url = self.get_download_url(version)
            filename = pathlib.Path(urlparse(download_url).path).name
            download_path = self.cache_dir / filename

            if not download_path.exists() or not self.config.get_setting("cache_downloads", True):
                self.download_file(download_url, download_path)
            else:
                logger.info(f"Using cached download: {download_path}")

            # Verify checksum if available and enabled
            checksum_url = self.get_checksum_url(version)
            if checksum_url and self.config.get_setting("verify_checksums", True):
                self._verify_download_checksum(download_path, checksum_url)

            # Extract and install
            self._install_from_archive(download_path, version)

            # Update configuration
            self.set_installed_version(version)

            # Create symlink if configured
            if self.config.get_setting("create_symlinks", True):
                self.create_symlink(version)

        except Exception as e:
            # Clean up on failure if configured
            if self.config.get_setting("clean_on_failure", True):
                self._cleanup_failed_installation(version)

            raise ToolManagerError(None) from e
    
    xǁBaseToolManagerǁinstall_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁinstall_version__mutmut_1': xǁBaseToolManagerǁinstall_version__mutmut_1, 
        'xǁBaseToolManagerǁinstall_version__mutmut_2': xǁBaseToolManagerǁinstall_version__mutmut_2, 
        'xǁBaseToolManagerǁinstall_version__mutmut_3': xǁBaseToolManagerǁinstall_version__mutmut_3, 
        'xǁBaseToolManagerǁinstall_version__mutmut_4': xǁBaseToolManagerǁinstall_version__mutmut_4, 
        'xǁBaseToolManagerǁinstall_version__mutmut_5': xǁBaseToolManagerǁinstall_version__mutmut_5, 
        'xǁBaseToolManagerǁinstall_version__mutmut_6': xǁBaseToolManagerǁinstall_version__mutmut_6, 
        'xǁBaseToolManagerǁinstall_version__mutmut_7': xǁBaseToolManagerǁinstall_version__mutmut_7, 
        'xǁBaseToolManagerǁinstall_version__mutmut_8': xǁBaseToolManagerǁinstall_version__mutmut_8, 
        'xǁBaseToolManagerǁinstall_version__mutmut_9': xǁBaseToolManagerǁinstall_version__mutmut_9, 
        'xǁBaseToolManagerǁinstall_version__mutmut_10': xǁBaseToolManagerǁinstall_version__mutmut_10, 
        'xǁBaseToolManagerǁinstall_version__mutmut_11': xǁBaseToolManagerǁinstall_version__mutmut_11, 
        'xǁBaseToolManagerǁinstall_version__mutmut_12': xǁBaseToolManagerǁinstall_version__mutmut_12, 
        'xǁBaseToolManagerǁinstall_version__mutmut_13': xǁBaseToolManagerǁinstall_version__mutmut_13, 
        'xǁBaseToolManagerǁinstall_version__mutmut_14': xǁBaseToolManagerǁinstall_version__mutmut_14, 
        'xǁBaseToolManagerǁinstall_version__mutmut_15': xǁBaseToolManagerǁinstall_version__mutmut_15, 
        'xǁBaseToolManagerǁinstall_version__mutmut_16': xǁBaseToolManagerǁinstall_version__mutmut_16, 
        'xǁBaseToolManagerǁinstall_version__mutmut_17': xǁBaseToolManagerǁinstall_version__mutmut_17, 
        'xǁBaseToolManagerǁinstall_version__mutmut_18': xǁBaseToolManagerǁinstall_version__mutmut_18, 
        'xǁBaseToolManagerǁinstall_version__mutmut_19': xǁBaseToolManagerǁinstall_version__mutmut_19, 
        'xǁBaseToolManagerǁinstall_version__mutmut_20': xǁBaseToolManagerǁinstall_version__mutmut_20, 
        'xǁBaseToolManagerǁinstall_version__mutmut_21': xǁBaseToolManagerǁinstall_version__mutmut_21, 
        'xǁBaseToolManagerǁinstall_version__mutmut_22': xǁBaseToolManagerǁinstall_version__mutmut_22, 
        'xǁBaseToolManagerǁinstall_version__mutmut_23': xǁBaseToolManagerǁinstall_version__mutmut_23, 
        'xǁBaseToolManagerǁinstall_version__mutmut_24': xǁBaseToolManagerǁinstall_version__mutmut_24, 
        'xǁBaseToolManagerǁinstall_version__mutmut_25': xǁBaseToolManagerǁinstall_version__mutmut_25, 
        'xǁBaseToolManagerǁinstall_version__mutmut_26': xǁBaseToolManagerǁinstall_version__mutmut_26, 
        'xǁBaseToolManagerǁinstall_version__mutmut_27': xǁBaseToolManagerǁinstall_version__mutmut_27, 
        'xǁBaseToolManagerǁinstall_version__mutmut_28': xǁBaseToolManagerǁinstall_version__mutmut_28, 
        'xǁBaseToolManagerǁinstall_version__mutmut_29': xǁBaseToolManagerǁinstall_version__mutmut_29, 
        'xǁBaseToolManagerǁinstall_version__mutmut_30': xǁBaseToolManagerǁinstall_version__mutmut_30, 
        'xǁBaseToolManagerǁinstall_version__mutmut_31': xǁBaseToolManagerǁinstall_version__mutmut_31, 
        'xǁBaseToolManagerǁinstall_version__mutmut_32': xǁBaseToolManagerǁinstall_version__mutmut_32, 
        'xǁBaseToolManagerǁinstall_version__mutmut_33': xǁBaseToolManagerǁinstall_version__mutmut_33, 
        'xǁBaseToolManagerǁinstall_version__mutmut_34': xǁBaseToolManagerǁinstall_version__mutmut_34, 
        'xǁBaseToolManagerǁinstall_version__mutmut_35': xǁBaseToolManagerǁinstall_version__mutmut_35, 
        'xǁBaseToolManagerǁinstall_version__mutmut_36': xǁBaseToolManagerǁinstall_version__mutmut_36, 
        'xǁBaseToolManagerǁinstall_version__mutmut_37': xǁBaseToolManagerǁinstall_version__mutmut_37, 
        'xǁBaseToolManagerǁinstall_version__mutmut_38': xǁBaseToolManagerǁinstall_version__mutmut_38, 
        'xǁBaseToolManagerǁinstall_version__mutmut_39': xǁBaseToolManagerǁinstall_version__mutmut_39, 
        'xǁBaseToolManagerǁinstall_version__mutmut_40': xǁBaseToolManagerǁinstall_version__mutmut_40, 
        'xǁBaseToolManagerǁinstall_version__mutmut_41': xǁBaseToolManagerǁinstall_version__mutmut_41, 
        'xǁBaseToolManagerǁinstall_version__mutmut_42': xǁBaseToolManagerǁinstall_version__mutmut_42, 
        'xǁBaseToolManagerǁinstall_version__mutmut_43': xǁBaseToolManagerǁinstall_version__mutmut_43, 
        'xǁBaseToolManagerǁinstall_version__mutmut_44': xǁBaseToolManagerǁinstall_version__mutmut_44, 
        'xǁBaseToolManagerǁinstall_version__mutmut_45': xǁBaseToolManagerǁinstall_version__mutmut_45, 
        'xǁBaseToolManagerǁinstall_version__mutmut_46': xǁBaseToolManagerǁinstall_version__mutmut_46, 
        'xǁBaseToolManagerǁinstall_version__mutmut_47': xǁBaseToolManagerǁinstall_version__mutmut_47, 
        'xǁBaseToolManagerǁinstall_version__mutmut_48': xǁBaseToolManagerǁinstall_version__mutmut_48, 
        'xǁBaseToolManagerǁinstall_version__mutmut_49': xǁBaseToolManagerǁinstall_version__mutmut_49, 
        'xǁBaseToolManagerǁinstall_version__mutmut_50': xǁBaseToolManagerǁinstall_version__mutmut_50, 
        'xǁBaseToolManagerǁinstall_version__mutmut_51': xǁBaseToolManagerǁinstall_version__mutmut_51, 
        'xǁBaseToolManagerǁinstall_version__mutmut_52': xǁBaseToolManagerǁinstall_version__mutmut_52, 
        'xǁBaseToolManagerǁinstall_version__mutmut_53': xǁBaseToolManagerǁinstall_version__mutmut_53, 
        'xǁBaseToolManagerǁinstall_version__mutmut_54': xǁBaseToolManagerǁinstall_version__mutmut_54, 
        'xǁBaseToolManagerǁinstall_version__mutmut_55': xǁBaseToolManagerǁinstall_version__mutmut_55, 
        'xǁBaseToolManagerǁinstall_version__mutmut_56': xǁBaseToolManagerǁinstall_version__mutmut_56, 
        'xǁBaseToolManagerǁinstall_version__mutmut_57': xǁBaseToolManagerǁinstall_version__mutmut_57, 
        'xǁBaseToolManagerǁinstall_version__mutmut_58': xǁBaseToolManagerǁinstall_version__mutmut_58, 
        'xǁBaseToolManagerǁinstall_version__mutmut_59': xǁBaseToolManagerǁinstall_version__mutmut_59, 
        'xǁBaseToolManagerǁinstall_version__mutmut_60': xǁBaseToolManagerǁinstall_version__mutmut_60, 
        'xǁBaseToolManagerǁinstall_version__mutmut_61': xǁBaseToolManagerǁinstall_version__mutmut_61, 
        'xǁBaseToolManagerǁinstall_version__mutmut_62': xǁBaseToolManagerǁinstall_version__mutmut_62, 
        'xǁBaseToolManagerǁinstall_version__mutmut_63': xǁBaseToolManagerǁinstall_version__mutmut_63, 
        'xǁBaseToolManagerǁinstall_version__mutmut_64': xǁBaseToolManagerǁinstall_version__mutmut_64, 
        'xǁBaseToolManagerǁinstall_version__mutmut_65': xǁBaseToolManagerǁinstall_version__mutmut_65, 
        'xǁBaseToolManagerǁinstall_version__mutmut_66': xǁBaseToolManagerǁinstall_version__mutmut_66, 
        'xǁBaseToolManagerǁinstall_version__mutmut_67': xǁBaseToolManagerǁinstall_version__mutmut_67, 
        'xǁBaseToolManagerǁinstall_version__mutmut_68': xǁBaseToolManagerǁinstall_version__mutmut_68, 
        'xǁBaseToolManagerǁinstall_version__mutmut_69': xǁBaseToolManagerǁinstall_version__mutmut_69, 
        'xǁBaseToolManagerǁinstall_version__mutmut_70': xǁBaseToolManagerǁinstall_version__mutmut_70, 
        'xǁBaseToolManagerǁinstall_version__mutmut_71': xǁBaseToolManagerǁinstall_version__mutmut_71, 
        'xǁBaseToolManagerǁinstall_version__mutmut_72': xǁBaseToolManagerǁinstall_version__mutmut_72, 
        'xǁBaseToolManagerǁinstall_version__mutmut_73': xǁBaseToolManagerǁinstall_version__mutmut_73
    }
    
    def install_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁinstall_version__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁinstall_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    install_version.__signature__ = _mutmut_signature(xǁBaseToolManagerǁinstall_version__mutmut_orig)
    xǁBaseToolManagerǁinstall_version__mutmut_orig.__name__ = 'xǁBaseToolManagerǁinstall_version'

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_orig(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_1(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = None
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_2(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(None, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_3(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, None)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_4(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_5(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, )
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_6(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_7(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(None)
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_8(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = None
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_9(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = None

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_10(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(None, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_11(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, None)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_12(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_13(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, )

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_14(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_15(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(None, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_16(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, None):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_17(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_18(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, ):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_19(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(None)
        else:
            logger.warning(f"No checksum found for {download_filename} in {checksum_path.name}")

    def xǁBaseToolManagerǁ_verify_download_checksum__mutmut_20(self, download_path: pathlib.Path, checksum_url: str) -> None:
        """Download and verify checksum file using Foundation helpers."""
        from wrknv.wenv.operations.download import (
            download_checksum_file,
            parse_checksum_file,
        )

        # Download checksum file using helper
        checksum_path = download_checksum_file(checksum_url, self.cache_dir)
        if not checksum_path:
            logger.warning(f"Failed to download checksum file from {checksum_url}")
            return

        # Parse checksum file using helper
        download_filename = download_path.name
        expected_checksum = parse_checksum_file(checksum_path, download_filename)

        if expected_checksum:
            # Verify using Foundation's verify method
            if not self.verify_checksum(download_path, expected_checksum):
                raise ToolManagerError(f"Checksum verification failed for {download_path}")
        else:
            logger.warning(None)
    
    xǁBaseToolManagerǁ_verify_download_checksum__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_1': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_1, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_2': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_2, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_3': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_3, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_4': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_4, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_5': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_5, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_6': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_6, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_7': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_7, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_8': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_8, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_9': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_9, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_10': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_10, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_11': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_11, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_12': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_12, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_13': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_13, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_14': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_14, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_15': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_15, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_16': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_16, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_17': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_17, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_18': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_18, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_19': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_19, 
        'xǁBaseToolManagerǁ_verify_download_checksum__mutmut_20': xǁBaseToolManagerǁ_verify_download_checksum__mutmut_20
    }
    
    def _verify_download_checksum(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁ_verify_download_checksum__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁ_verify_download_checksum__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _verify_download_checksum.__signature__ = _mutmut_signature(xǁBaseToolManagerǁ_verify_download_checksum__mutmut_orig)
    xǁBaseToolManagerǁ_verify_download_checksum__mutmut_orig.__name__ = 'xǁBaseToolManagerǁ_verify_download_checksum'

    @abstractmethod
    def _install_from_archive(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive. Tool-specific implementation."""

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_orig(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=True)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_1(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = None
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=True)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_2(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name * version
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=True)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_3(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path * self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=True)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_4(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(None, missing_ok=True)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_5(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=None)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_6(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(missing_ok=True)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_7(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(tool_dir, )
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_8(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=False)
            logger.info(f"Cleaned up failed installation: {tool_dir}")

    def xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_9(self, version: str) -> None:
        """Clean up failed installation."""
        tool_dir = self.install_path / self.tool_name / version
        if tool_dir.exists():
            safe_rmtree(tool_dir, missing_ok=True)
            logger.info(None)
    
    xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_1': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_1, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_2': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_2, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_3': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_3, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_4': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_4, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_5': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_5, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_6': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_6, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_7': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_7, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_8': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_8, 
        'xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_9': xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_9
    }
    
    def _cleanup_failed_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _cleanup_failed_installation.__signature__ = _mutmut_signature(xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_orig)
    xǁBaseToolManagerǁ_cleanup_failed_installation__mutmut_orig.__name__ = 'xǁBaseToolManagerǁ_cleanup_failed_installation'

    def xǁBaseToolManagerǁinstall_latest__mutmut_orig(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_1(self, dry_run: bool = True) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_2(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = None
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_3(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_4(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(None)

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_5(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = None  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_6(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[1]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_7(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(None)
        self.install_version(latest, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_8(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(None, dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_9(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, dry_run=None)

    def xǁBaseToolManagerǁinstall_latest__mutmut_10(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(dry_run=dry_run)

    def xǁBaseToolManagerǁinstall_latest__mutmut_11(self, dry_run: bool = False) -> None:
        """Install the latest stable version."""
        versions = self.get_available_versions()
        if not versions:
            raise ToolManagerError(f"No versions available for {self.tool_name}")

        latest = versions[0]  # Assume first is latest
        logger.info(f"Latest {self.tool_name} version: {latest}")
        self.install_version(latest, )
    
    xǁBaseToolManagerǁinstall_latest__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁinstall_latest__mutmut_1': xǁBaseToolManagerǁinstall_latest__mutmut_1, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_2': xǁBaseToolManagerǁinstall_latest__mutmut_2, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_3': xǁBaseToolManagerǁinstall_latest__mutmut_3, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_4': xǁBaseToolManagerǁinstall_latest__mutmut_4, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_5': xǁBaseToolManagerǁinstall_latest__mutmut_5, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_6': xǁBaseToolManagerǁinstall_latest__mutmut_6, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_7': xǁBaseToolManagerǁinstall_latest__mutmut_7, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_8': xǁBaseToolManagerǁinstall_latest__mutmut_8, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_9': xǁBaseToolManagerǁinstall_latest__mutmut_9, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_10': xǁBaseToolManagerǁinstall_latest__mutmut_10, 
        'xǁBaseToolManagerǁinstall_latest__mutmut_11': xǁBaseToolManagerǁinstall_latest__mutmut_11
    }
    
    def install_latest(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁinstall_latest__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁinstall_latest__mutmut_mutants"), args, kwargs, self)
        return result 
    
    install_latest.__signature__ = _mutmut_signature(xǁBaseToolManagerǁinstall_latest__mutmut_orig)
    xǁBaseToolManagerǁinstall_latest__mutmut_orig.__name__ = 'xǁBaseToolManagerǁinstall_latest'

    def xǁBaseToolManagerǁlist_versions__mutmut_orig(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_1(self, limit: int = 21) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_2(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(None)

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_3(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = None
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_4(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = None

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_5(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(None):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_6(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = None
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_7(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = "XX (current)XX" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_8(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (CURRENT)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_9(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version != current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_10(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else "XXXX"
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_11(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = None
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_12(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = "XXXX"
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_13(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(None)

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_14(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) >= limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_15(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(None)

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_16(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) + limit} more versions available")

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch versions for {self.tool_name}: {e}") from e

    def xǁBaseToolManagerǁlist_versions__mutmut_17(self, limit: int = 20) -> None:
        """List available versions."""
        logger.info(f"Available {self.tool_name} versions:")

        try:
            versions = self.get_available_versions()
            current = self.get_installed_version()

            for _i, version in enumerate(versions[:limit]):
                marker = " (current)" if version == current else ""
                status = ""
                pout(f"{status} {version}{marker}")

            if len(versions) > limit:
                pout(f"... and {len(versions) - limit} more versions available")

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁBaseToolManagerǁlist_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁlist_versions__mutmut_1': xǁBaseToolManagerǁlist_versions__mutmut_1, 
        'xǁBaseToolManagerǁlist_versions__mutmut_2': xǁBaseToolManagerǁlist_versions__mutmut_2, 
        'xǁBaseToolManagerǁlist_versions__mutmut_3': xǁBaseToolManagerǁlist_versions__mutmut_3, 
        'xǁBaseToolManagerǁlist_versions__mutmut_4': xǁBaseToolManagerǁlist_versions__mutmut_4, 
        'xǁBaseToolManagerǁlist_versions__mutmut_5': xǁBaseToolManagerǁlist_versions__mutmut_5, 
        'xǁBaseToolManagerǁlist_versions__mutmut_6': xǁBaseToolManagerǁlist_versions__mutmut_6, 
        'xǁBaseToolManagerǁlist_versions__mutmut_7': xǁBaseToolManagerǁlist_versions__mutmut_7, 
        'xǁBaseToolManagerǁlist_versions__mutmut_8': xǁBaseToolManagerǁlist_versions__mutmut_8, 
        'xǁBaseToolManagerǁlist_versions__mutmut_9': xǁBaseToolManagerǁlist_versions__mutmut_9, 
        'xǁBaseToolManagerǁlist_versions__mutmut_10': xǁBaseToolManagerǁlist_versions__mutmut_10, 
        'xǁBaseToolManagerǁlist_versions__mutmut_11': xǁBaseToolManagerǁlist_versions__mutmut_11, 
        'xǁBaseToolManagerǁlist_versions__mutmut_12': xǁBaseToolManagerǁlist_versions__mutmut_12, 
        'xǁBaseToolManagerǁlist_versions__mutmut_13': xǁBaseToolManagerǁlist_versions__mutmut_13, 
        'xǁBaseToolManagerǁlist_versions__mutmut_14': xǁBaseToolManagerǁlist_versions__mutmut_14, 
        'xǁBaseToolManagerǁlist_versions__mutmut_15': xǁBaseToolManagerǁlist_versions__mutmut_15, 
        'xǁBaseToolManagerǁlist_versions__mutmut_16': xǁBaseToolManagerǁlist_versions__mutmut_16, 
        'xǁBaseToolManagerǁlist_versions__mutmut_17': xǁBaseToolManagerǁlist_versions__mutmut_17
    }
    
    def list_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁlist_versions__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁlist_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_versions.__signature__ = _mutmut_signature(xǁBaseToolManagerǁlist_versions__mutmut_orig)
    xǁBaseToolManagerǁlist_versions__mutmut_orig.__name__ = 'xǁBaseToolManagerǁlist_versions'

    def xǁBaseToolManagerǁshow_current__mutmut_orig(self) -> None:
        """Show current installed version."""
        version = self.get_installed_version()
        if version:
            binary_path = self.get_current_binary_path()
            if binary_path and binary_path.exists():
                pout(f"{self.tool_name}: {version} (installed at {binary_path})")
            else:
                pout(f"{self.tool_name}: {version} (binary missing)")
        else:
            pout(f"{self.tool_name}: not installed")

    def xǁBaseToolManagerǁshow_current__mutmut_1(self) -> None:
        """Show current installed version."""
        version = None
        if version:
            binary_path = self.get_current_binary_path()
            if binary_path and binary_path.exists():
                pout(f"{self.tool_name}: {version} (installed at {binary_path})")
            else:
                pout(f"{self.tool_name}: {version} (binary missing)")
        else:
            pout(f"{self.tool_name}: not installed")

    def xǁBaseToolManagerǁshow_current__mutmut_2(self) -> None:
        """Show current installed version."""
        version = self.get_installed_version()
        if version:
            binary_path = None
            if binary_path and binary_path.exists():
                pout(f"{self.tool_name}: {version} (installed at {binary_path})")
            else:
                pout(f"{self.tool_name}: {version} (binary missing)")
        else:
            pout(f"{self.tool_name}: not installed")

    def xǁBaseToolManagerǁshow_current__mutmut_3(self) -> None:
        """Show current installed version."""
        version = self.get_installed_version()
        if version:
            binary_path = self.get_current_binary_path()
            if binary_path or binary_path.exists():
                pout(f"{self.tool_name}: {version} (installed at {binary_path})")
            else:
                pout(f"{self.tool_name}: {version} (binary missing)")
        else:
            pout(f"{self.tool_name}: not installed")

    def xǁBaseToolManagerǁshow_current__mutmut_4(self) -> None:
        """Show current installed version."""
        version = self.get_installed_version()
        if version:
            binary_path = self.get_current_binary_path()
            if binary_path and binary_path.exists():
                pout(None)
            else:
                pout(f"{self.tool_name}: {version} (binary missing)")
        else:
            pout(f"{self.tool_name}: not installed")

    def xǁBaseToolManagerǁshow_current__mutmut_5(self) -> None:
        """Show current installed version."""
        version = self.get_installed_version()
        if version:
            binary_path = self.get_current_binary_path()
            if binary_path and binary_path.exists():
                pout(f"{self.tool_name}: {version} (installed at {binary_path})")
            else:
                pout(None)
        else:
            pout(f"{self.tool_name}: not installed")

    def xǁBaseToolManagerǁshow_current__mutmut_6(self) -> None:
        """Show current installed version."""
        version = self.get_installed_version()
        if version:
            binary_path = self.get_current_binary_path()
            if binary_path and binary_path.exists():
                pout(f"{self.tool_name}: {version} (installed at {binary_path})")
            else:
                pout(f"{self.tool_name}: {version} (binary missing)")
        else:
            pout(None)
    
    xǁBaseToolManagerǁshow_current__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁshow_current__mutmut_1': xǁBaseToolManagerǁshow_current__mutmut_1, 
        'xǁBaseToolManagerǁshow_current__mutmut_2': xǁBaseToolManagerǁshow_current__mutmut_2, 
        'xǁBaseToolManagerǁshow_current__mutmut_3': xǁBaseToolManagerǁshow_current__mutmut_3, 
        'xǁBaseToolManagerǁshow_current__mutmut_4': xǁBaseToolManagerǁshow_current__mutmut_4, 
        'xǁBaseToolManagerǁshow_current__mutmut_5': xǁBaseToolManagerǁshow_current__mutmut_5, 
        'xǁBaseToolManagerǁshow_current__mutmut_6': xǁBaseToolManagerǁshow_current__mutmut_6
    }
    
    def show_current(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁshow_current__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁshow_current__mutmut_mutants"), args, kwargs, self)
        return result 
    
    show_current.__signature__ = _mutmut_signature(xǁBaseToolManagerǁshow_current__mutmut_orig)
    xǁBaseToolManagerǁshow_current__mutmut_orig.__name__ = 'xǁBaseToolManagerǁshow_current'

    def xǁBaseToolManagerǁget_installed_versions__mutmut_orig(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_1(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = None

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_2(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = None
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_3(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path * self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_4(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() or self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_5(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(None):
                    versions.append(item.name)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_6(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(None)

        return sorted(versions, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_7(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(None, reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_8(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=None)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_9(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(reverse=True)

    def xǁBaseToolManagerǁget_installed_versions__mutmut_10(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, )

    def xǁBaseToolManagerǁget_installed_versions__mutmut_11(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        # Check install directory for all versions
        tool_install_dir = self.install_path / self.tool_name
        if tool_install_dir.exists():
            for item in tool_install_dir.iterdir():
                if item.is_dir() and self._is_version_dir(item.name):
                    versions.append(item.name)

        return sorted(versions, reverse=False)
    
    xǁBaseToolManagerǁget_installed_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁget_installed_versions__mutmut_1': xǁBaseToolManagerǁget_installed_versions__mutmut_1, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_2': xǁBaseToolManagerǁget_installed_versions__mutmut_2, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_3': xǁBaseToolManagerǁget_installed_versions__mutmut_3, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_4': xǁBaseToolManagerǁget_installed_versions__mutmut_4, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_5': xǁBaseToolManagerǁget_installed_versions__mutmut_5, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_6': xǁBaseToolManagerǁget_installed_versions__mutmut_6, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_7': xǁBaseToolManagerǁget_installed_versions__mutmut_7, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_8': xǁBaseToolManagerǁget_installed_versions__mutmut_8, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_9': xǁBaseToolManagerǁget_installed_versions__mutmut_9, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_10': xǁBaseToolManagerǁget_installed_versions__mutmut_10, 
        'xǁBaseToolManagerǁget_installed_versions__mutmut_11': xǁBaseToolManagerǁget_installed_versions__mutmut_11
    }
    
    def get_installed_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁget_installed_versions__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁget_installed_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_versions.__signature__ = _mutmut_signature(xǁBaseToolManagerǁget_installed_versions__mutmut_orig)
    xǁBaseToolManagerǁget_installed_versions__mutmut_orig.__name__ = 'xǁBaseToolManagerǁget_installed_versions'

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_orig(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(re.match(r"^\d+\.\d+\.\d+", name))

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_1(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(None)

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_2(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(re.match(None, name))

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_3(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(re.match(r"^\d+\.\d+\.\d+", None))

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_4(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(re.match(name))

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_5(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(re.match(r"^\d+\.\d+\.\d+", ))

    def xǁBaseToolManagerǁ_is_version_dir__mutmut_6(self, name: str) -> bool:
        """Check if a directory name looks like a version."""
        # Basic semantic version check
        import re

        return bool(re.match(r"XX^\d+\.\d+\.\d+XX", name))
    
    xǁBaseToolManagerǁ_is_version_dir__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁ_is_version_dir__mutmut_1': xǁBaseToolManagerǁ_is_version_dir__mutmut_1, 
        'xǁBaseToolManagerǁ_is_version_dir__mutmut_2': xǁBaseToolManagerǁ_is_version_dir__mutmut_2, 
        'xǁBaseToolManagerǁ_is_version_dir__mutmut_3': xǁBaseToolManagerǁ_is_version_dir__mutmut_3, 
        'xǁBaseToolManagerǁ_is_version_dir__mutmut_4': xǁBaseToolManagerǁ_is_version_dir__mutmut_4, 
        'xǁBaseToolManagerǁ_is_version_dir__mutmut_5': xǁBaseToolManagerǁ_is_version_dir__mutmut_5, 
        'xǁBaseToolManagerǁ_is_version_dir__mutmut_6': xǁBaseToolManagerǁ_is_version_dir__mutmut_6
    }
    
    def _is_version_dir(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁ_is_version_dir__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁ_is_version_dir__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_version_dir.__signature__ = _mutmut_signature(xǁBaseToolManagerǁ_is_version_dir__mutmut_orig)
    xǁBaseToolManagerǁ_is_version_dir__mutmut_orig.__name__ = 'xǁBaseToolManagerǁ_is_version_dir'

    def xǁBaseToolManagerǁremove_version__mutmut_orig(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_1(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = None
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_2(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name * version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_3(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path * self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_4(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = None

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_5(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(None)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_6(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(None, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_7(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=None)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_8(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_9(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, )
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_10(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=False)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_11(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(None)

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_12(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() or binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_13(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent == version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_14(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(None, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_15(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=None)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_16(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_17(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, )
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_18(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=False)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_19(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(None)

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_20(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() != version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("")

    def xǁBaseToolManagerǁremove_version__mutmut_21(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version(None)

    def xǁBaseToolManagerǁremove_version__mutmut_22(self, version: str) -> None:
        """Remove a specific version of the tool."""
        version_dir = self.install_path / self.tool_name / version
        binary_path = self.get_binary_path(version)

        # Remove the version directory
        if version_dir.exists():
            safe_rmtree(version_dir, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} directory")

        # Remove the binary if it exists elsewhere
        if binary_path.exists() and binary_path.parent != version_dir:
            safe_delete(binary_path, missing_ok=True)
            logger.info(f"Removed {self.tool_name} {version} binary")

        # Update config if this was the current version
        if self.get_installed_version() == version:
            # Clear the version (subclasses should override set_installed_version to persist)
            self.set_installed_version("XXXX")
    
    xǁBaseToolManagerǁremove_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁremove_version__mutmut_1': xǁBaseToolManagerǁremove_version__mutmut_1, 
        'xǁBaseToolManagerǁremove_version__mutmut_2': xǁBaseToolManagerǁremove_version__mutmut_2, 
        'xǁBaseToolManagerǁremove_version__mutmut_3': xǁBaseToolManagerǁremove_version__mutmut_3, 
        'xǁBaseToolManagerǁremove_version__mutmut_4': xǁBaseToolManagerǁremove_version__mutmut_4, 
        'xǁBaseToolManagerǁremove_version__mutmut_5': xǁBaseToolManagerǁremove_version__mutmut_5, 
        'xǁBaseToolManagerǁremove_version__mutmut_6': xǁBaseToolManagerǁremove_version__mutmut_6, 
        'xǁBaseToolManagerǁremove_version__mutmut_7': xǁBaseToolManagerǁremove_version__mutmut_7, 
        'xǁBaseToolManagerǁremove_version__mutmut_8': xǁBaseToolManagerǁremove_version__mutmut_8, 
        'xǁBaseToolManagerǁremove_version__mutmut_9': xǁBaseToolManagerǁremove_version__mutmut_9, 
        'xǁBaseToolManagerǁremove_version__mutmut_10': xǁBaseToolManagerǁremove_version__mutmut_10, 
        'xǁBaseToolManagerǁremove_version__mutmut_11': xǁBaseToolManagerǁremove_version__mutmut_11, 
        'xǁBaseToolManagerǁremove_version__mutmut_12': xǁBaseToolManagerǁremove_version__mutmut_12, 
        'xǁBaseToolManagerǁremove_version__mutmut_13': xǁBaseToolManagerǁremove_version__mutmut_13, 
        'xǁBaseToolManagerǁremove_version__mutmut_14': xǁBaseToolManagerǁremove_version__mutmut_14, 
        'xǁBaseToolManagerǁremove_version__mutmut_15': xǁBaseToolManagerǁremove_version__mutmut_15, 
        'xǁBaseToolManagerǁremove_version__mutmut_16': xǁBaseToolManagerǁremove_version__mutmut_16, 
        'xǁBaseToolManagerǁremove_version__mutmut_17': xǁBaseToolManagerǁremove_version__mutmut_17, 
        'xǁBaseToolManagerǁremove_version__mutmut_18': xǁBaseToolManagerǁremove_version__mutmut_18, 
        'xǁBaseToolManagerǁremove_version__mutmut_19': xǁBaseToolManagerǁremove_version__mutmut_19, 
        'xǁBaseToolManagerǁremove_version__mutmut_20': xǁBaseToolManagerǁremove_version__mutmut_20, 
        'xǁBaseToolManagerǁremove_version__mutmut_21': xǁBaseToolManagerǁremove_version__mutmut_21, 
        'xǁBaseToolManagerǁremove_version__mutmut_22': xǁBaseToolManagerǁremove_version__mutmut_22
    }
    
    def remove_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁremove_version__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁremove_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    remove_version.__signature__ = _mutmut_signature(xǁBaseToolManagerǁremove_version__mutmut_orig)
    xǁBaseToolManagerǁremove_version__mutmut_orig.__name__ = 'xǁBaseToolManagerǁremove_version'

    def xǁBaseToolManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = None
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return True

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = None

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                None,
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=None,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(None), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "XX--versionXX"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--VERSION"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=11,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode != 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 1

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(None)
            return False

    def xǁBaseToolManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that installation works correctly."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            return False

        try:
            # Try to run the tool with version flag
            result = run(
                [str(binary_path), "--version"],
                timeout=10,
            )

            return result.returncode == 0

        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Verification failed for {self.tool_name} {version}: {e}")
            return True
    
    xǁBaseToolManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaseToolManagerǁverify_installation__mutmut_1': xǁBaseToolManagerǁverify_installation__mutmut_1, 
        'xǁBaseToolManagerǁverify_installation__mutmut_2': xǁBaseToolManagerǁverify_installation__mutmut_2, 
        'xǁBaseToolManagerǁverify_installation__mutmut_3': xǁBaseToolManagerǁverify_installation__mutmut_3, 
        'xǁBaseToolManagerǁverify_installation__mutmut_4': xǁBaseToolManagerǁverify_installation__mutmut_4, 
        'xǁBaseToolManagerǁverify_installation__mutmut_5': xǁBaseToolManagerǁverify_installation__mutmut_5, 
        'xǁBaseToolManagerǁverify_installation__mutmut_6': xǁBaseToolManagerǁverify_installation__mutmut_6, 
        'xǁBaseToolManagerǁverify_installation__mutmut_7': xǁBaseToolManagerǁverify_installation__mutmut_7, 
        'xǁBaseToolManagerǁverify_installation__mutmut_8': xǁBaseToolManagerǁverify_installation__mutmut_8, 
        'xǁBaseToolManagerǁverify_installation__mutmut_9': xǁBaseToolManagerǁverify_installation__mutmut_9, 
        'xǁBaseToolManagerǁverify_installation__mutmut_10': xǁBaseToolManagerǁverify_installation__mutmut_10, 
        'xǁBaseToolManagerǁverify_installation__mutmut_11': xǁBaseToolManagerǁverify_installation__mutmut_11, 
        'xǁBaseToolManagerǁverify_installation__mutmut_12': xǁBaseToolManagerǁverify_installation__mutmut_12, 
        'xǁBaseToolManagerǁverify_installation__mutmut_13': xǁBaseToolManagerǁverify_installation__mutmut_13, 
        'xǁBaseToolManagerǁverify_installation__mutmut_14': xǁBaseToolManagerǁverify_installation__mutmut_14, 
        'xǁBaseToolManagerǁverify_installation__mutmut_15': xǁBaseToolManagerǁverify_installation__mutmut_15, 
        'xǁBaseToolManagerǁverify_installation__mutmut_16': xǁBaseToolManagerǁverify_installation__mutmut_16, 
        'xǁBaseToolManagerǁverify_installation__mutmut_17': xǁBaseToolManagerǁverify_installation__mutmut_17
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaseToolManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁBaseToolManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁBaseToolManagerǁverify_installation__mutmut_orig)
    xǁBaseToolManagerǁverify_installation__mutmut_orig.__name__ = 'xǁBaseToolManagerǁverify_installation'


# 🧰🌍🔚
