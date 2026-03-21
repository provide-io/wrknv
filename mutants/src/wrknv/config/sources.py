#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Configuration Sources for wrknv
================================
Different sources for loading configuration."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from provide.foundation.file import read_toml
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


class ConfigSource:
    """Base interface for configuration sources."""

    def get_tool_version(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        return None

    def get_all_tools(self) -> dict[str, str]:
        """Get all tool versions."""
        return {}

    def get_profile(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        return {}

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        return default


class FileConfigSource(ConfigSource):
    """Configuration source that loads from TOML files."""

    def xǁFileConfigSourceǁ__init____mutmut_orig(self, path: Path, section: str = "workenv") -> None:
        """Initialize with file path and optional section."""
        self.path = path
        self.section = section
        self._data: dict[str, Any] = {}
        self._load()

    def xǁFileConfigSourceǁ__init____mutmut_1(self, path: Path, section: str = "XXworkenvXX") -> None:
        """Initialize with file path and optional section."""
        self.path = path
        self.section = section
        self._data: dict[str, Any] = {}
        self._load()

    def xǁFileConfigSourceǁ__init____mutmut_2(self, path: Path, section: str = "WORKENV") -> None:
        """Initialize with file path and optional section."""
        self.path = path
        self.section = section
        self._data: dict[str, Any] = {}
        self._load()

    def xǁFileConfigSourceǁ__init____mutmut_3(self, path: Path, section: str = "workenv") -> None:
        """Initialize with file path and optional section."""
        self.path = None
        self.section = section
        self._data: dict[str, Any] = {}
        self._load()

    def xǁFileConfigSourceǁ__init____mutmut_4(self, path: Path, section: str = "workenv") -> None:
        """Initialize with file path and optional section."""
        self.path = path
        self.section = None
        self._data: dict[str, Any] = {}
        self._load()

    def xǁFileConfigSourceǁ__init____mutmut_5(self, path: Path, section: str = "workenv") -> None:
        """Initialize with file path and optional section."""
        self.path = path
        self.section = section
        self._data: dict[str, Any] = None
        self._load()
    
    xǁFileConfigSourceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileConfigSourceǁ__init____mutmut_1': xǁFileConfigSourceǁ__init____mutmut_1, 
        'xǁFileConfigSourceǁ__init____mutmut_2': xǁFileConfigSourceǁ__init____mutmut_2, 
        'xǁFileConfigSourceǁ__init____mutmut_3': xǁFileConfigSourceǁ__init____mutmut_3, 
        'xǁFileConfigSourceǁ__init____mutmut_4': xǁFileConfigSourceǁ__init____mutmut_4, 
        'xǁFileConfigSourceǁ__init____mutmut_5': xǁFileConfigSourceǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileConfigSourceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFileConfigSourceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFileConfigSourceǁ__init____mutmut_orig)
    xǁFileConfigSourceǁ__init____mutmut_orig.__name__ = 'xǁFileConfigSourceǁ__init__'

    def xǁFileConfigSourceǁ_load__mutmut_orig(self) -> None:
        """Load configuration from file."""
        if self.path.exists():
            self._data = read_toml(self.path, default={})

    def xǁFileConfigSourceǁ_load__mutmut_1(self) -> None:
        """Load configuration from file."""
        if self.path.exists():
            self._data = None

    def xǁFileConfigSourceǁ_load__mutmut_2(self) -> None:
        """Load configuration from file."""
        if self.path.exists():
            self._data = read_toml(None, default={})

    def xǁFileConfigSourceǁ_load__mutmut_3(self) -> None:
        """Load configuration from file."""
        if self.path.exists():
            self._data = read_toml(self.path, default=None)

    def xǁFileConfigSourceǁ_load__mutmut_4(self) -> None:
        """Load configuration from file."""
        if self.path.exists():
            self._data = read_toml(default={})

    def xǁFileConfigSourceǁ_load__mutmut_5(self) -> None:
        """Load configuration from file."""
        if self.path.exists():
            self._data = read_toml(self.path, )
    
    xǁFileConfigSourceǁ_load__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileConfigSourceǁ_load__mutmut_1': xǁFileConfigSourceǁ_load__mutmut_1, 
        'xǁFileConfigSourceǁ_load__mutmut_2': xǁFileConfigSourceǁ_load__mutmut_2, 
        'xǁFileConfigSourceǁ_load__mutmut_3': xǁFileConfigSourceǁ_load__mutmut_3, 
        'xǁFileConfigSourceǁ_load__mutmut_4': xǁFileConfigSourceǁ_load__mutmut_4, 
        'xǁFileConfigSourceǁ_load__mutmut_5': xǁFileConfigSourceǁ_load__mutmut_5
    }
    
    def _load(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileConfigSourceǁ_load__mutmut_orig"), object.__getattribute__(self, "xǁFileConfigSourceǁ_load__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _load.__signature__ = _mutmut_signature(xǁFileConfigSourceǁ_load__mutmut_orig)
    xǁFileConfigSourceǁ_load__mutmut_orig.__name__ = 'xǁFileConfigSourceǁ_load'

    def xǁFileConfigSourceǁget_tool_version__mutmut_orig(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("tools", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_1(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = None
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_2(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get(None, {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_3(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("tools", None)
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_4(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get({})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_5(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("tools", )
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_6(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(None, {}).get("tools", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_7(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, None).get("tools", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_8(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get({}).get("tools", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_9(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, ).get("tools", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_10(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("XXtoolsXX", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_11(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("TOOLS", {})
        result: str | None = tools.get(tool_name)
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_12(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("tools", {})
        result: str | None = None
        return result

    def xǁFileConfigSourceǁget_tool_version__mutmut_13(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        tools = self._data.get(self.section, {}).get("tools", {})
        result: str | None = tools.get(None)
        return result
    
    xǁFileConfigSourceǁget_tool_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileConfigSourceǁget_tool_version__mutmut_1': xǁFileConfigSourceǁget_tool_version__mutmut_1, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_2': xǁFileConfigSourceǁget_tool_version__mutmut_2, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_3': xǁFileConfigSourceǁget_tool_version__mutmut_3, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_4': xǁFileConfigSourceǁget_tool_version__mutmut_4, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_5': xǁFileConfigSourceǁget_tool_version__mutmut_5, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_6': xǁFileConfigSourceǁget_tool_version__mutmut_6, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_7': xǁFileConfigSourceǁget_tool_version__mutmut_7, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_8': xǁFileConfigSourceǁget_tool_version__mutmut_8, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_9': xǁFileConfigSourceǁget_tool_version__mutmut_9, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_10': xǁFileConfigSourceǁget_tool_version__mutmut_10, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_11': xǁFileConfigSourceǁget_tool_version__mutmut_11, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_12': xǁFileConfigSourceǁget_tool_version__mutmut_12, 
        'xǁFileConfigSourceǁget_tool_version__mutmut_13': xǁFileConfigSourceǁget_tool_version__mutmut_13
    }
    
    def get_tool_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileConfigSourceǁget_tool_version__mutmut_orig"), object.__getattribute__(self, "xǁFileConfigSourceǁget_tool_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_tool_version.__signature__ = _mutmut_signature(xǁFileConfigSourceǁget_tool_version__mutmut_orig)
    xǁFileConfigSourceǁget_tool_version__mutmut_orig.__name__ = 'xǁFileConfigSourceǁget_tool_version'

    def xǁFileConfigSourceǁget_all_tools__mutmut_orig(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get("tools", {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_1(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = None
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_2(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get(None, {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_3(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get("tools", None)
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_4(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get({})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_5(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get("tools", )
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_6(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(None, {}).get("tools", {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_7(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, None).get("tools", {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_8(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get({}).get("tools", {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_9(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, ).get("tools", {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_10(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get("XXtoolsXX", {})
        return tools

    def xǁFileConfigSourceǁget_all_tools__mutmut_11(self) -> dict[str, str]:
        """Get all tool versions."""
        tools: dict[str, str] = self._data.get(self.section, {}).get("TOOLS", {})
        return tools
    
    xǁFileConfigSourceǁget_all_tools__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileConfigSourceǁget_all_tools__mutmut_1': xǁFileConfigSourceǁget_all_tools__mutmut_1, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_2': xǁFileConfigSourceǁget_all_tools__mutmut_2, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_3': xǁFileConfigSourceǁget_all_tools__mutmut_3, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_4': xǁFileConfigSourceǁget_all_tools__mutmut_4, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_5': xǁFileConfigSourceǁget_all_tools__mutmut_5, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_6': xǁFileConfigSourceǁget_all_tools__mutmut_6, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_7': xǁFileConfigSourceǁget_all_tools__mutmut_7, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_8': xǁFileConfigSourceǁget_all_tools__mutmut_8, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_9': xǁFileConfigSourceǁget_all_tools__mutmut_9, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_10': xǁFileConfigSourceǁget_all_tools__mutmut_10, 
        'xǁFileConfigSourceǁget_all_tools__mutmut_11': xǁFileConfigSourceǁget_all_tools__mutmut_11
    }
    
    def get_all_tools(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileConfigSourceǁget_all_tools__mutmut_orig"), object.__getattribute__(self, "xǁFileConfigSourceǁget_all_tools__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_all_tools.__signature__ = _mutmut_signature(xǁFileConfigSourceǁget_all_tools__mutmut_orig)
    xǁFileConfigSourceǁget_all_tools__mutmut_orig.__name__ = 'xǁFileConfigSourceǁget_all_tools'

    def xǁFileConfigSourceǁget_profile__mutmut_orig(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_1(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = None
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_2(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get(None, {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_3(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", None)
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_4(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get({})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_5(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", )
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_6(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(None, {}).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_7(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, None).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_8(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get({}).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_9(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, ).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_10(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("XXprofilesXX", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_11(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("PROFILES", {})
        profile: dict[str, str] = profiles.get(profile_name, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_12(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", {})
        profile: dict[str, str] = None
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_13(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", {})
        profile: dict[str, str] = profiles.get(None, {})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_14(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, None)
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_15(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", {})
        profile: dict[str, str] = profiles.get({})
        return profile

    def xǁFileConfigSourceǁget_profile__mutmut_16(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile."""
        profiles = self._data.get(self.section, {}).get("profiles", {})
        profile: dict[str, str] = profiles.get(profile_name, )
        return profile
    
    xǁFileConfigSourceǁget_profile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileConfigSourceǁget_profile__mutmut_1': xǁFileConfigSourceǁget_profile__mutmut_1, 
        'xǁFileConfigSourceǁget_profile__mutmut_2': xǁFileConfigSourceǁget_profile__mutmut_2, 
        'xǁFileConfigSourceǁget_profile__mutmut_3': xǁFileConfigSourceǁget_profile__mutmut_3, 
        'xǁFileConfigSourceǁget_profile__mutmut_4': xǁFileConfigSourceǁget_profile__mutmut_4, 
        'xǁFileConfigSourceǁget_profile__mutmut_5': xǁFileConfigSourceǁget_profile__mutmut_5, 
        'xǁFileConfigSourceǁget_profile__mutmut_6': xǁFileConfigSourceǁget_profile__mutmut_6, 
        'xǁFileConfigSourceǁget_profile__mutmut_7': xǁFileConfigSourceǁget_profile__mutmut_7, 
        'xǁFileConfigSourceǁget_profile__mutmut_8': xǁFileConfigSourceǁget_profile__mutmut_8, 
        'xǁFileConfigSourceǁget_profile__mutmut_9': xǁFileConfigSourceǁget_profile__mutmut_9, 
        'xǁFileConfigSourceǁget_profile__mutmut_10': xǁFileConfigSourceǁget_profile__mutmut_10, 
        'xǁFileConfigSourceǁget_profile__mutmut_11': xǁFileConfigSourceǁget_profile__mutmut_11, 
        'xǁFileConfigSourceǁget_profile__mutmut_12': xǁFileConfigSourceǁget_profile__mutmut_12, 
        'xǁFileConfigSourceǁget_profile__mutmut_13': xǁFileConfigSourceǁget_profile__mutmut_13, 
        'xǁFileConfigSourceǁget_profile__mutmut_14': xǁFileConfigSourceǁget_profile__mutmut_14, 
        'xǁFileConfigSourceǁget_profile__mutmut_15': xǁFileConfigSourceǁget_profile__mutmut_15, 
        'xǁFileConfigSourceǁget_profile__mutmut_16': xǁFileConfigSourceǁget_profile__mutmut_16
    }
    
    def get_profile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileConfigSourceǁget_profile__mutmut_orig"), object.__getattribute__(self, "xǁFileConfigSourceǁget_profile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_profile.__signature__ = _mutmut_signature(xǁFileConfigSourceǁget_profile__mutmut_orig)
    xǁFileConfigSourceǁget_profile__mutmut_orig.__name__ = 'xǁFileConfigSourceǁget_profile'

    def xǁFileConfigSourceǁget_setting__mutmut_orig(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_1(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = None
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_2(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get(None, {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_3(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", None)
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_4(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get({})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_5(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", )
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_6(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(None, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_7(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, None).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_8(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get({}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_9(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, ).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_10(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("XXsettingsXX", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_11(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("SETTINGS", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_12(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key not in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_13(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = None
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_14(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(None)
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_15(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split("XX.XX")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_16(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = None
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_17(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = None
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_18(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(None)
                if current is None:
                    return default
            else:
                return default
        return current

    def xǁFileConfigSourceǁget_setting__mutmut_19(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting."""
        # First check in the section's settings
        settings = self._data.get(self.section, {}).get("settings", {})
        if key in settings:
            return settings[key]

        # Then try navigating from root
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
                if current is not None:
                    return default
            else:
                return default
        return current
    
    xǁFileConfigSourceǁget_setting__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileConfigSourceǁget_setting__mutmut_1': xǁFileConfigSourceǁget_setting__mutmut_1, 
        'xǁFileConfigSourceǁget_setting__mutmut_2': xǁFileConfigSourceǁget_setting__mutmut_2, 
        'xǁFileConfigSourceǁget_setting__mutmut_3': xǁFileConfigSourceǁget_setting__mutmut_3, 
        'xǁFileConfigSourceǁget_setting__mutmut_4': xǁFileConfigSourceǁget_setting__mutmut_4, 
        'xǁFileConfigSourceǁget_setting__mutmut_5': xǁFileConfigSourceǁget_setting__mutmut_5, 
        'xǁFileConfigSourceǁget_setting__mutmut_6': xǁFileConfigSourceǁget_setting__mutmut_6, 
        'xǁFileConfigSourceǁget_setting__mutmut_7': xǁFileConfigSourceǁget_setting__mutmut_7, 
        'xǁFileConfigSourceǁget_setting__mutmut_8': xǁFileConfigSourceǁget_setting__mutmut_8, 
        'xǁFileConfigSourceǁget_setting__mutmut_9': xǁFileConfigSourceǁget_setting__mutmut_9, 
        'xǁFileConfigSourceǁget_setting__mutmut_10': xǁFileConfigSourceǁget_setting__mutmut_10, 
        'xǁFileConfigSourceǁget_setting__mutmut_11': xǁFileConfigSourceǁget_setting__mutmut_11, 
        'xǁFileConfigSourceǁget_setting__mutmut_12': xǁFileConfigSourceǁget_setting__mutmut_12, 
        'xǁFileConfigSourceǁget_setting__mutmut_13': xǁFileConfigSourceǁget_setting__mutmut_13, 
        'xǁFileConfigSourceǁget_setting__mutmut_14': xǁFileConfigSourceǁget_setting__mutmut_14, 
        'xǁFileConfigSourceǁget_setting__mutmut_15': xǁFileConfigSourceǁget_setting__mutmut_15, 
        'xǁFileConfigSourceǁget_setting__mutmut_16': xǁFileConfigSourceǁget_setting__mutmut_16, 
        'xǁFileConfigSourceǁget_setting__mutmut_17': xǁFileConfigSourceǁget_setting__mutmut_17, 
        'xǁFileConfigSourceǁget_setting__mutmut_18': xǁFileConfigSourceǁget_setting__mutmut_18, 
        'xǁFileConfigSourceǁget_setting__mutmut_19': xǁFileConfigSourceǁget_setting__mutmut_19
    }
    
    def get_setting(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileConfigSourceǁget_setting__mutmut_orig"), object.__getattribute__(self, "xǁFileConfigSourceǁget_setting__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_setting.__signature__ = _mutmut_signature(xǁFileConfigSourceǁget_setting__mutmut_orig)
    xǁFileConfigSourceǁget_setting__mutmut_orig.__name__ = 'xǁFileConfigSourceǁget_setting'


class EnvironmentConfigSource(ConfigSource):
    """Configuration source that loads from environment variables."""

    def xǁEnvironmentConfigSourceǁ__init____mutmut_orig(self, prefix: str = "WRKNV") -> None:
        """Initialize with environment variable prefix."""
        self.prefix = prefix

    def xǁEnvironmentConfigSourceǁ__init____mutmut_1(self, prefix: str = "XXWRKNVXX") -> None:
        """Initialize with environment variable prefix."""
        self.prefix = prefix

    def xǁEnvironmentConfigSourceǁ__init____mutmut_2(self, prefix: str = "wrknv") -> None:
        """Initialize with environment variable prefix."""
        self.prefix = prefix

    def xǁEnvironmentConfigSourceǁ__init____mutmut_3(self, prefix: str = "WRKNV") -> None:
        """Initialize with environment variable prefix."""
        self.prefix = None
    
    xǁEnvironmentConfigSourceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEnvironmentConfigSourceǁ__init____mutmut_1': xǁEnvironmentConfigSourceǁ__init____mutmut_1, 
        'xǁEnvironmentConfigSourceǁ__init____mutmut_2': xǁEnvironmentConfigSourceǁ__init____mutmut_2, 
        'xǁEnvironmentConfigSourceǁ__init____mutmut_3': xǁEnvironmentConfigSourceǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEnvironmentConfigSourceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁEnvironmentConfigSourceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁEnvironmentConfigSourceǁ__init____mutmut_orig)
    xǁEnvironmentConfigSourceǁ__init____mutmut_orig.__name__ = 'xǁEnvironmentConfigSourceǁ__init__'

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_orig(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_1(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = None
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_2(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.lower()}_VERSION"
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_3(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = None
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_4(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(None)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_5(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(env_var)
        if value is not None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_6(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = None
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_7(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.lower()}_VERSION"
            value = os.environ.get(env_var)
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_8(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = None
        return value

    def xǁEnvironmentConfigSourceǁget_tool_version__mutmut_9(self, tool_name: str) -> str | None:
        """Get version for a specific tool."""
        # Try both formats for compatibility
        env_var = f"{self.prefix}_{tool_name.upper()}_VERSION"
        value = os.environ.get(env_var)
        if value is None:
            # Also try with TOOL_ prefix
            env_var = f"{self.prefix}_TOOL_{tool_name.upper()}_VERSION"
            value = os.environ.get(None)
        return value
    
    xǁEnvironmentConfigSourceǁget_tool_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_1': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_1, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_2': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_2, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_3': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_3, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_4': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_4, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_5': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_5, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_6': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_6, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_7': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_7, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_8': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_8, 
        'xǁEnvironmentConfigSourceǁget_tool_version__mutmut_9': xǁEnvironmentConfigSourceǁget_tool_version__mutmut_9
    }
    
    def get_tool_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_tool_version__mutmut_orig"), object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_tool_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_tool_version.__signature__ = _mutmut_signature(xǁEnvironmentConfigSourceǁget_tool_version__mutmut_orig)
    xǁEnvironmentConfigSourceǁget_tool_version__mutmut_orig.__name__ = 'xǁEnvironmentConfigSourceǁget_tool_version'

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_orig(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_1(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = None
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_2(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) or key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_3(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(None) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_4(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith(None):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_5(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("XX_VERSIONXX"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_6(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_version"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_7(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" not in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_8(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = None
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_9(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = None
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_10(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].upper()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_11(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : +8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_12(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -9].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_13(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = None
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_14(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = None
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_15(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].upper()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_16(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : +8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_17(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -9].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_18(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name not in ("project", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_19(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("XXprojectXX", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_20(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("PROJECT", "wrknv"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_21(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "XXwrknvXX"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_22(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "WRKNV"):
                        continue
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_23(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        break
                tools[tool_name] = value
        return tools

    def xǁEnvironmentConfigSourceǁget_all_tools__mutmut_24(self) -> dict[str, str]:
        """Get all tool versions from environment."""
        tools = {}
        # Check both formats
        for key, value in os.environ.items():
            if key.startswith(self.prefix) and key.endswith("_VERSION"):
                # Try to extract tool name from both formats
                if f"{self.prefix}_TOOL_" in key:
                    # Format: PREFIX_TOOL_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_TOOL_"
                    tool_name = key[len(prefix) : -8].lower()
                else:
                    # Format: PREFIX_TOOLNAME_VERSION
                    prefix = f"{self.prefix}_"
                    tool_name = key[len(prefix) : -8].lower()
                    # Skip if it's not a tool (e.g., PROJECT_VERSION)
                    if tool_name in ("project", "wrknv"):
                        continue
                tools[tool_name] = None
        return tools
    
    xǁEnvironmentConfigSourceǁget_all_tools__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_1': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_1, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_2': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_2, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_3': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_3, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_4': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_4, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_5': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_5, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_6': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_6, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_7': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_7, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_8': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_8, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_9': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_9, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_10': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_10, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_11': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_11, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_12': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_12, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_13': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_13, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_14': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_14, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_15': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_15, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_16': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_16, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_17': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_17, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_18': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_18, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_19': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_19, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_20': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_20, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_21': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_21, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_22': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_22, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_23': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_23, 
        'xǁEnvironmentConfigSourceǁget_all_tools__mutmut_24': xǁEnvironmentConfigSourceǁget_all_tools__mutmut_24
    }
    
    def get_all_tools(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_all_tools__mutmut_orig"), object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_all_tools__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_all_tools.__signature__ = _mutmut_signature(xǁEnvironmentConfigSourceǁget_all_tools__mutmut_orig)
    xǁEnvironmentConfigSourceǁget_all_tools__mutmut_orig.__name__ = 'xǁEnvironmentConfigSourceǁget_all_tools'

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_orig(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = f"{self.prefix}_PROFILE_{profile_name.upper()}_"
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = key[len(prefix) :].lower()
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_1(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = None
        prefix = f"{self.prefix}_PROFILE_{profile_name.upper()}_"
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = key[len(prefix) :].lower()
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_2(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = None
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = key[len(prefix) :].lower()
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_3(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = f"{self.prefix}_PROFILE_{profile_name.lower()}_"
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = key[len(prefix) :].lower()
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_4(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = f"{self.prefix}_PROFILE_{profile_name.upper()}_"
        for key, value in os.environ.items():
            if key.startswith(None):
                tool_name = key[len(prefix) :].lower()
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_5(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = f"{self.prefix}_PROFILE_{profile_name.upper()}_"
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = None
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_6(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = f"{self.prefix}_PROFILE_{profile_name.upper()}_"
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = key[len(prefix) :].upper()
                profile[tool_name] = value
        return profile

    def xǁEnvironmentConfigSourceǁget_profile__mutmut_7(self, profile_name: str) -> dict[str, str]:
        """Get a configuration profile from environment."""
        # Profiles from env vars are tool-specific overrides
        profile = {}
        prefix = f"{self.prefix}_PROFILE_{profile_name.upper()}_"
        for key, value in os.environ.items():
            if key.startswith(prefix):
                tool_name = key[len(prefix) :].lower()
                profile[tool_name] = None
        return profile
    
    xǁEnvironmentConfigSourceǁget_profile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEnvironmentConfigSourceǁget_profile__mutmut_1': xǁEnvironmentConfigSourceǁget_profile__mutmut_1, 
        'xǁEnvironmentConfigSourceǁget_profile__mutmut_2': xǁEnvironmentConfigSourceǁget_profile__mutmut_2, 
        'xǁEnvironmentConfigSourceǁget_profile__mutmut_3': xǁEnvironmentConfigSourceǁget_profile__mutmut_3, 
        'xǁEnvironmentConfigSourceǁget_profile__mutmut_4': xǁEnvironmentConfigSourceǁget_profile__mutmut_4, 
        'xǁEnvironmentConfigSourceǁget_profile__mutmut_5': xǁEnvironmentConfigSourceǁget_profile__mutmut_5, 
        'xǁEnvironmentConfigSourceǁget_profile__mutmut_6': xǁEnvironmentConfigSourceǁget_profile__mutmut_6, 
        'xǁEnvironmentConfigSourceǁget_profile__mutmut_7': xǁEnvironmentConfigSourceǁget_profile__mutmut_7
    }
    
    def get_profile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_profile__mutmut_orig"), object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_profile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_profile.__signature__ = _mutmut_signature(xǁEnvironmentConfigSourceǁget_profile__mutmut_orig)
    xǁEnvironmentConfigSourceǁget_profile__mutmut_orig.__name__ = 'xǁEnvironmentConfigSourceǁget_profile'

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_orig(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_1(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = None
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_2(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace(None, '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_3(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', None)}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_4(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_5(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', )}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_6(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.lower().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_7(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('XX.XX', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_8(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', 'XX_XX')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_9(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = None
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_10(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(None)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_11(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is not None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_12(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.upper() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_13(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() not in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_14(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("XXtrueXX", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_15(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("TRUE", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_16(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "XX1XX", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_17(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "XXyesXX", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_18(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "YES", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_19(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "XXonXX"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_20(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "ON"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_21(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return False
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_22(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.upper() in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_23(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() not in ("false", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_24(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("XXfalseXX", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_25(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("FALSE", "0", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_26(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "XX0XX", "no", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_27(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "XXnoXX", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_28(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "NO", "off"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_29(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "XXoffXX"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_30(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "OFF"):
            return False
        return value

    def xǁEnvironmentConfigSourceǁget_setting__mutmut_31(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting from environment."""
        env_var = f"{self.prefix}_{key.upper().replace('.', '_')}"
        value = os.environ.get(env_var)
        if value is None:
            return default
        # Try to parse boolean values
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return True
        return value
    
    xǁEnvironmentConfigSourceǁget_setting__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEnvironmentConfigSourceǁget_setting__mutmut_1': xǁEnvironmentConfigSourceǁget_setting__mutmut_1, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_2': xǁEnvironmentConfigSourceǁget_setting__mutmut_2, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_3': xǁEnvironmentConfigSourceǁget_setting__mutmut_3, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_4': xǁEnvironmentConfigSourceǁget_setting__mutmut_4, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_5': xǁEnvironmentConfigSourceǁget_setting__mutmut_5, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_6': xǁEnvironmentConfigSourceǁget_setting__mutmut_6, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_7': xǁEnvironmentConfigSourceǁget_setting__mutmut_7, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_8': xǁEnvironmentConfigSourceǁget_setting__mutmut_8, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_9': xǁEnvironmentConfigSourceǁget_setting__mutmut_9, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_10': xǁEnvironmentConfigSourceǁget_setting__mutmut_10, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_11': xǁEnvironmentConfigSourceǁget_setting__mutmut_11, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_12': xǁEnvironmentConfigSourceǁget_setting__mutmut_12, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_13': xǁEnvironmentConfigSourceǁget_setting__mutmut_13, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_14': xǁEnvironmentConfigSourceǁget_setting__mutmut_14, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_15': xǁEnvironmentConfigSourceǁget_setting__mutmut_15, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_16': xǁEnvironmentConfigSourceǁget_setting__mutmut_16, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_17': xǁEnvironmentConfigSourceǁget_setting__mutmut_17, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_18': xǁEnvironmentConfigSourceǁget_setting__mutmut_18, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_19': xǁEnvironmentConfigSourceǁget_setting__mutmut_19, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_20': xǁEnvironmentConfigSourceǁget_setting__mutmut_20, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_21': xǁEnvironmentConfigSourceǁget_setting__mutmut_21, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_22': xǁEnvironmentConfigSourceǁget_setting__mutmut_22, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_23': xǁEnvironmentConfigSourceǁget_setting__mutmut_23, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_24': xǁEnvironmentConfigSourceǁget_setting__mutmut_24, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_25': xǁEnvironmentConfigSourceǁget_setting__mutmut_25, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_26': xǁEnvironmentConfigSourceǁget_setting__mutmut_26, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_27': xǁEnvironmentConfigSourceǁget_setting__mutmut_27, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_28': xǁEnvironmentConfigSourceǁget_setting__mutmut_28, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_29': xǁEnvironmentConfigSourceǁget_setting__mutmut_29, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_30': xǁEnvironmentConfigSourceǁget_setting__mutmut_30, 
        'xǁEnvironmentConfigSourceǁget_setting__mutmut_31': xǁEnvironmentConfigSourceǁget_setting__mutmut_31
    }
    
    def get_setting(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_setting__mutmut_orig"), object.__getattribute__(self, "xǁEnvironmentConfigSourceǁget_setting__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_setting.__signature__ = _mutmut_signature(xǁEnvironmentConfigSourceǁget_setting__mutmut_orig)
    xǁEnvironmentConfigSourceǁget_setting__mutmut_orig.__name__ = 'xǁEnvironmentConfigSourceǁget_setting'


# 🧰🌍🔚
