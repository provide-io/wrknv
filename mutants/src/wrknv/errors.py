#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Errors
============
Centralized exception definitions using provide.foundation error hierarchy.

This module consolidates all wrknv exceptions with helpful error messages,
suggestions, and proper inheritance from foundation errors."""

from __future__ import annotations

from provide.foundation.errors import (
    AlreadyExistsError,
    FoundationError,
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

# Base Errors
# ===========


class WrkenvError(FoundationError):
    """Base exception for all wrknv errors."""

    def xǁWrkenvErrorǁ__init____mutmut_orig(self, message: str, hint: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.hint = hint
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_1(self, message: str, hint: str | None = None, exit_code: int = 2) -> None:
        super().__init__(message)
        self.message = message
        self.hint = hint
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_2(self, message: str, hint: str | None = None, exit_code: int = 1) -> None:
        super().__init__(None)
        self.message = message
        self.hint = hint
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_3(self, message: str, hint: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = None
        self.hint = hint
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_4(self, message: str, hint: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.hint = None
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_5(self, message: str, hint: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.hint = hint
        self.exit_code = None
    
    xǁWrkenvErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWrkenvErrorǁ__init____mutmut_1': xǁWrkenvErrorǁ__init____mutmut_1, 
        'xǁWrkenvErrorǁ__init____mutmut_2': xǁWrkenvErrorǁ__init____mutmut_2, 
        'xǁWrkenvErrorǁ__init____mutmut_3': xǁWrkenvErrorǁ__init____mutmut_3, 
        'xǁWrkenvErrorǁ__init____mutmut_4': xǁWrkenvErrorǁ__init____mutmut_4, 
        'xǁWrkenvErrorǁ__init____mutmut_5': xǁWrkenvErrorǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWrkenvErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWrkenvErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWrkenvErrorǁ__init____mutmut_orig)
    xǁWrkenvErrorǁ__init____mutmut_orig.__name__ = 'xǁWrkenvErrorǁ__init__'

    def __str__(self) -> str:
        if self.hint:
            return f"{self.message}\n💡 {self.hint}"
        return self.message


# Configuration Errors
# ====================


class ConfigurationError(WrkenvError):
    """Configuration file or settings errors."""

    def xǁConfigurationErrorǁ__init____mutmut_orig(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, hint)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_1(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = None
        super().__init__(message, hint)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_2(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(None, hint)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_3(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, None)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_4(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(hint)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_5(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, )
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_6(
        self,
        message: str,
        hint: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, hint)
        self.line_number = None
    
    xǁConfigurationErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConfigurationErrorǁ__init____mutmut_1': xǁConfigurationErrorǁ__init____mutmut_1, 
        'xǁConfigurationErrorǁ__init____mutmut_2': xǁConfigurationErrorǁ__init____mutmut_2, 
        'xǁConfigurationErrorǁ__init____mutmut_3': xǁConfigurationErrorǁ__init____mutmut_3, 
        'xǁConfigurationErrorǁ__init____mutmut_4': xǁConfigurationErrorǁ__init____mutmut_4, 
        'xǁConfigurationErrorǁ__init____mutmut_5': xǁConfigurationErrorǁ__init____mutmut_5, 
        'xǁConfigurationErrorǁ__init____mutmut_6': xǁConfigurationErrorǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConfigurationErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁConfigurationErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁConfigurationErrorǁ__init____mutmut_orig)
    xǁConfigurationErrorǁ__init____mutmut_orig.__name__ = 'xǁConfigurationErrorǁ__init__'


class ValidationError(ConfigurationError):
    """Configuration validation errors."""


# Profile Errors
# ==============


class ProfileError(WrkenvError):
    """Profile-related errors."""

    def xǁProfileErrorǁ__init____mutmut_orig(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_1(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_2(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = None

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_3(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = ""
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_4(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = None

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_5(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(None)}"

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_6(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {'XX, XX'.join(available_profiles)}"

        super().__init__(message, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_7(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(None, hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_8(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, None)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_9(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(hint)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_10(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, )
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_11(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        hint = None
        if available_profiles:
            hint = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, hint)
        self.profile_name = None
    
    xǁProfileErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProfileErrorǁ__init____mutmut_1': xǁProfileErrorǁ__init____mutmut_1, 
        'xǁProfileErrorǁ__init____mutmut_2': xǁProfileErrorǁ__init____mutmut_2, 
        'xǁProfileErrorǁ__init____mutmut_3': xǁProfileErrorǁ__init____mutmut_3, 
        'xǁProfileErrorǁ__init____mutmut_4': xǁProfileErrorǁ__init____mutmut_4, 
        'xǁProfileErrorǁ__init____mutmut_5': xǁProfileErrorǁ__init____mutmut_5, 
        'xǁProfileErrorǁ__init____mutmut_6': xǁProfileErrorǁ__init____mutmut_6, 
        'xǁProfileErrorǁ__init____mutmut_7': xǁProfileErrorǁ__init____mutmut_7, 
        'xǁProfileErrorǁ__init____mutmut_8': xǁProfileErrorǁ__init____mutmut_8, 
        'xǁProfileErrorǁ__init____mutmut_9': xǁProfileErrorǁ__init____mutmut_9, 
        'xǁProfileErrorǁ__init____mutmut_10': xǁProfileErrorǁ__init____mutmut_10, 
        'xǁProfileErrorǁ__init____mutmut_11': xǁProfileErrorǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProfileErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁProfileErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁProfileErrorǁ__init____mutmut_orig)
    xǁProfileErrorǁ__init____mutmut_orig.__name__ = 'xǁProfileErrorǁ__init__'


# Tool Errors
# ===========


class ToolNotFoundError(NotFoundError):
    """Tool or version not found errors."""

    def xǁToolNotFoundErrorǁ__init____mutmut_orig(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_1(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = None
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_2(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = None
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_3(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = None
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_4(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = None

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_5(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = ""
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_6(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = None
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_7(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(None)
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_8(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = "XX, XX".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_9(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:6])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_10(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) >= 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_11(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 6:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_12(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str = "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_13(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str -= "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_14(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "XX...XX"
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_15(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = None

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_16(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=None,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_17(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type=None,
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_18(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=None,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_19(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=None,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_20(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_21(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_22(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_23(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_24(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="XXtoolXX",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_25(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="TOOL",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_26(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = None
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_27(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        if version:
            message = f"{tool} version {version} not found"
            resource_id = f"{tool}@{version}"
        else:
            message = f"{tool} not found"
            resource_id = tool

        hint = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            hint = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(
            message=message,
            resource_type="tool",
            resource_id=resource_id,
            hint=hint,
        )
        self.tool = tool
        self.version = None
    
    xǁToolNotFoundErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁToolNotFoundErrorǁ__init____mutmut_1': xǁToolNotFoundErrorǁ__init____mutmut_1, 
        'xǁToolNotFoundErrorǁ__init____mutmut_2': xǁToolNotFoundErrorǁ__init____mutmut_2, 
        'xǁToolNotFoundErrorǁ__init____mutmut_3': xǁToolNotFoundErrorǁ__init____mutmut_3, 
        'xǁToolNotFoundErrorǁ__init____mutmut_4': xǁToolNotFoundErrorǁ__init____mutmut_4, 
        'xǁToolNotFoundErrorǁ__init____mutmut_5': xǁToolNotFoundErrorǁ__init____mutmut_5, 
        'xǁToolNotFoundErrorǁ__init____mutmut_6': xǁToolNotFoundErrorǁ__init____mutmut_6, 
        'xǁToolNotFoundErrorǁ__init____mutmut_7': xǁToolNotFoundErrorǁ__init____mutmut_7, 
        'xǁToolNotFoundErrorǁ__init____mutmut_8': xǁToolNotFoundErrorǁ__init____mutmut_8, 
        'xǁToolNotFoundErrorǁ__init____mutmut_9': xǁToolNotFoundErrorǁ__init____mutmut_9, 
        'xǁToolNotFoundErrorǁ__init____mutmut_10': xǁToolNotFoundErrorǁ__init____mutmut_10, 
        'xǁToolNotFoundErrorǁ__init____mutmut_11': xǁToolNotFoundErrorǁ__init____mutmut_11, 
        'xǁToolNotFoundErrorǁ__init____mutmut_12': xǁToolNotFoundErrorǁ__init____mutmut_12, 
        'xǁToolNotFoundErrorǁ__init____mutmut_13': xǁToolNotFoundErrorǁ__init____mutmut_13, 
        'xǁToolNotFoundErrorǁ__init____mutmut_14': xǁToolNotFoundErrorǁ__init____mutmut_14, 
        'xǁToolNotFoundErrorǁ__init____mutmut_15': xǁToolNotFoundErrorǁ__init____mutmut_15, 
        'xǁToolNotFoundErrorǁ__init____mutmut_16': xǁToolNotFoundErrorǁ__init____mutmut_16, 
        'xǁToolNotFoundErrorǁ__init____mutmut_17': xǁToolNotFoundErrorǁ__init____mutmut_17, 
        'xǁToolNotFoundErrorǁ__init____mutmut_18': xǁToolNotFoundErrorǁ__init____mutmut_18, 
        'xǁToolNotFoundErrorǁ__init____mutmut_19': xǁToolNotFoundErrorǁ__init____mutmut_19, 
        'xǁToolNotFoundErrorǁ__init____mutmut_20': xǁToolNotFoundErrorǁ__init____mutmut_20, 
        'xǁToolNotFoundErrorǁ__init____mutmut_21': xǁToolNotFoundErrorǁ__init____mutmut_21, 
        'xǁToolNotFoundErrorǁ__init____mutmut_22': xǁToolNotFoundErrorǁ__init____mutmut_22, 
        'xǁToolNotFoundErrorǁ__init____mutmut_23': xǁToolNotFoundErrorǁ__init____mutmut_23, 
        'xǁToolNotFoundErrorǁ__init____mutmut_24': xǁToolNotFoundErrorǁ__init____mutmut_24, 
        'xǁToolNotFoundErrorǁ__init____mutmut_25': xǁToolNotFoundErrorǁ__init____mutmut_25, 
        'xǁToolNotFoundErrorǁ__init____mutmut_26': xǁToolNotFoundErrorǁ__init____mutmut_26, 
        'xǁToolNotFoundErrorǁ__init____mutmut_27': xǁToolNotFoundErrorǁ__init____mutmut_27
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁToolNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁToolNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁToolNotFoundErrorǁ__init____mutmut_orig)
    xǁToolNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁToolNotFoundErrorǁ__init__'


# Network Errors
# ==============


class NetworkError(WrkenvError):
    """Network-related errors during downloads."""

    def xǁNetworkErrorǁ__init____mutmut_orig(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_1(self, message: str, url: str | None = None) -> None:
        hint = None
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_2(self, message: str, url: str | None = None) -> None:
        hint = "XXCheck your internet connection and proxy settingsXX"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_3(self, message: str, url: str | None = None) -> None:
        hint = "check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_4(self, message: str, url: str | None = None) -> None:
        hint = "CHECK YOUR INTERNET CONNECTION AND PROXY SETTINGS"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_5(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = None
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_6(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint = f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_7(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint -= f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_8(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(None, hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_9(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, None)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_10(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(hint)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_11(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, )
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_12(self, message: str, url: str | None = None) -> None:
        hint = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            hint += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, hint)
        self.url = None
    
    xǁNetworkErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNetworkErrorǁ__init____mutmut_1': xǁNetworkErrorǁ__init____mutmut_1, 
        'xǁNetworkErrorǁ__init____mutmut_2': xǁNetworkErrorǁ__init____mutmut_2, 
        'xǁNetworkErrorǁ__init____mutmut_3': xǁNetworkErrorǁ__init____mutmut_3, 
        'xǁNetworkErrorǁ__init____mutmut_4': xǁNetworkErrorǁ__init____mutmut_4, 
        'xǁNetworkErrorǁ__init____mutmut_5': xǁNetworkErrorǁ__init____mutmut_5, 
        'xǁNetworkErrorǁ__init____mutmut_6': xǁNetworkErrorǁ__init____mutmut_6, 
        'xǁNetworkErrorǁ__init____mutmut_7': xǁNetworkErrorǁ__init____mutmut_7, 
        'xǁNetworkErrorǁ__init____mutmut_8': xǁNetworkErrorǁ__init____mutmut_8, 
        'xǁNetworkErrorǁ__init____mutmut_9': xǁNetworkErrorǁ__init____mutmut_9, 
        'xǁNetworkErrorǁ__init____mutmut_10': xǁNetworkErrorǁ__init____mutmut_10, 
        'xǁNetworkErrorǁ__init____mutmut_11': xǁNetworkErrorǁ__init____mutmut_11, 
        'xǁNetworkErrorǁ__init____mutmut_12': xǁNetworkErrorǁ__init____mutmut_12
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNetworkErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNetworkErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNetworkErrorǁ__init____mutmut_orig)
    xǁNetworkErrorǁ__init____mutmut_orig.__name__ = 'xǁNetworkErrorǁ__init__'


# Permission Errors
# =================


class WrkenvPermissionError(WrkenvError):
    """File or directory permission errors."""

    def xǁWrkenvPermissionErrorǁ__init____mutmut_orig(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_1(self, path: str, operation: str = "XXaccessXX") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_2(self, path: str, operation: str = "ACCESS") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_3(self, path: str, operation: str = "access") -> None:
        message = None
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_4(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = None
        super().__init__(message, hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_5(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(None, hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_6(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, None)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_7(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(hint)
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_8(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, )
        self.path = path

    def xǁWrkenvPermissionErrorǁ__init____mutmut_9(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        hint = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, hint)
        self.path = None
    
    xǁWrkenvPermissionErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWrkenvPermissionErrorǁ__init____mutmut_1': xǁWrkenvPermissionErrorǁ__init____mutmut_1, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_2': xǁWrkenvPermissionErrorǁ__init____mutmut_2, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_3': xǁWrkenvPermissionErrorǁ__init____mutmut_3, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_4': xǁWrkenvPermissionErrorǁ__init____mutmut_4, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_5': xǁWrkenvPermissionErrorǁ__init____mutmut_5, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_6': xǁWrkenvPermissionErrorǁ__init____mutmut_6, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_7': xǁWrkenvPermissionErrorǁ__init____mutmut_7, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_8': xǁWrkenvPermissionErrorǁ__init____mutmut_8, 
        'xǁWrkenvPermissionErrorǁ__init____mutmut_9': xǁWrkenvPermissionErrorǁ__init____mutmut_9
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWrkenvPermissionErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWrkenvPermissionErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWrkenvPermissionErrorǁ__init____mutmut_orig)
    xǁWrkenvPermissionErrorǁ__init____mutmut_orig.__name__ = 'xǁWrkenvPermissionErrorǁ__init__'


# Dependency Errors
# =================


class DependencyError(WrkenvError):
    """Missing system dependencies."""

    def xǁDependencyErrorǁ__init____mutmut_orig(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_1(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = None
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_2(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(None)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_3(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = "XX, XX".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_4(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = None

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_5(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message = f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_6(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message -= f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_7(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = None
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_8(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "XXInstall missing dependencies:\nXX"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_9(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_10(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "INSTALL MISSING DEPENDENCIES:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_11(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep != "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_12(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "XXgitXX":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_13(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "GIT":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_14(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint = "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_15(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint -= "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_16(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "XX  • git: https://git-scm.com/downloads\nXX"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_17(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • GIT: HTTPS://GIT-SCM.COM/DOWNLOADS\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_18(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep != "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_19(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "XXcurlXX":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_20(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "CURL":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_21(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint = "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_22(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint -= "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_23(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "XX  • curl: Install via package manager (apt/brew/yum)\nXX"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_24(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_25(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • CURL: INSTALL VIA PACKAGE MANAGER (APT/BREW/YUM)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_26(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep != "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_27(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "XXdockerXX":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_28(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "DOCKER":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_29(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint = "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_30(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint -= "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_31(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "XX  • docker: https://docs.docker.com/get-docker/\nXX"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_32(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • DOCKER: HTTPS://DOCS.DOCKER.COM/GET-DOCKER/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_33(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep != "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_34(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "XXpython3XX":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_35(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "PYTHON3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_36(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint = "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_37(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint -= "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_38(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "XX  • python3: https://www.python.org/downloads/\nXX"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_39(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • PYTHON3: HTTPS://WWW.PYTHON.ORG/DOWNLOADS/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_40(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint = f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_41(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint -= f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_42(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(None, hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_43(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, None)
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_44(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(hint.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_45(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, )
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_46(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.lstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_47(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        hint = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                hint += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                hint += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                hint += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                hint += "  • python3: https://www.python.org/downloads/\n"
            else:
                hint += f"  • {dep}: Install via package manager\n"

        super().__init__(message, hint.rstrip())
        self.missing_deps = None
    
    xǁDependencyErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDependencyErrorǁ__init____mutmut_1': xǁDependencyErrorǁ__init____mutmut_1, 
        'xǁDependencyErrorǁ__init____mutmut_2': xǁDependencyErrorǁ__init____mutmut_2, 
        'xǁDependencyErrorǁ__init____mutmut_3': xǁDependencyErrorǁ__init____mutmut_3, 
        'xǁDependencyErrorǁ__init____mutmut_4': xǁDependencyErrorǁ__init____mutmut_4, 
        'xǁDependencyErrorǁ__init____mutmut_5': xǁDependencyErrorǁ__init____mutmut_5, 
        'xǁDependencyErrorǁ__init____mutmut_6': xǁDependencyErrorǁ__init____mutmut_6, 
        'xǁDependencyErrorǁ__init____mutmut_7': xǁDependencyErrorǁ__init____mutmut_7, 
        'xǁDependencyErrorǁ__init____mutmut_8': xǁDependencyErrorǁ__init____mutmut_8, 
        'xǁDependencyErrorǁ__init____mutmut_9': xǁDependencyErrorǁ__init____mutmut_9, 
        'xǁDependencyErrorǁ__init____mutmut_10': xǁDependencyErrorǁ__init____mutmut_10, 
        'xǁDependencyErrorǁ__init____mutmut_11': xǁDependencyErrorǁ__init____mutmut_11, 
        'xǁDependencyErrorǁ__init____mutmut_12': xǁDependencyErrorǁ__init____mutmut_12, 
        'xǁDependencyErrorǁ__init____mutmut_13': xǁDependencyErrorǁ__init____mutmut_13, 
        'xǁDependencyErrorǁ__init____mutmut_14': xǁDependencyErrorǁ__init____mutmut_14, 
        'xǁDependencyErrorǁ__init____mutmut_15': xǁDependencyErrorǁ__init____mutmut_15, 
        'xǁDependencyErrorǁ__init____mutmut_16': xǁDependencyErrorǁ__init____mutmut_16, 
        'xǁDependencyErrorǁ__init____mutmut_17': xǁDependencyErrorǁ__init____mutmut_17, 
        'xǁDependencyErrorǁ__init____mutmut_18': xǁDependencyErrorǁ__init____mutmut_18, 
        'xǁDependencyErrorǁ__init____mutmut_19': xǁDependencyErrorǁ__init____mutmut_19, 
        'xǁDependencyErrorǁ__init____mutmut_20': xǁDependencyErrorǁ__init____mutmut_20, 
        'xǁDependencyErrorǁ__init____mutmut_21': xǁDependencyErrorǁ__init____mutmut_21, 
        'xǁDependencyErrorǁ__init____mutmut_22': xǁDependencyErrorǁ__init____mutmut_22, 
        'xǁDependencyErrorǁ__init____mutmut_23': xǁDependencyErrorǁ__init____mutmut_23, 
        'xǁDependencyErrorǁ__init____mutmut_24': xǁDependencyErrorǁ__init____mutmut_24, 
        'xǁDependencyErrorǁ__init____mutmut_25': xǁDependencyErrorǁ__init____mutmut_25, 
        'xǁDependencyErrorǁ__init____mutmut_26': xǁDependencyErrorǁ__init____mutmut_26, 
        'xǁDependencyErrorǁ__init____mutmut_27': xǁDependencyErrorǁ__init____mutmut_27, 
        'xǁDependencyErrorǁ__init____mutmut_28': xǁDependencyErrorǁ__init____mutmut_28, 
        'xǁDependencyErrorǁ__init____mutmut_29': xǁDependencyErrorǁ__init____mutmut_29, 
        'xǁDependencyErrorǁ__init____mutmut_30': xǁDependencyErrorǁ__init____mutmut_30, 
        'xǁDependencyErrorǁ__init____mutmut_31': xǁDependencyErrorǁ__init____mutmut_31, 
        'xǁDependencyErrorǁ__init____mutmut_32': xǁDependencyErrorǁ__init____mutmut_32, 
        'xǁDependencyErrorǁ__init____mutmut_33': xǁDependencyErrorǁ__init____mutmut_33, 
        'xǁDependencyErrorǁ__init____mutmut_34': xǁDependencyErrorǁ__init____mutmut_34, 
        'xǁDependencyErrorǁ__init____mutmut_35': xǁDependencyErrorǁ__init____mutmut_35, 
        'xǁDependencyErrorǁ__init____mutmut_36': xǁDependencyErrorǁ__init____mutmut_36, 
        'xǁDependencyErrorǁ__init____mutmut_37': xǁDependencyErrorǁ__init____mutmut_37, 
        'xǁDependencyErrorǁ__init____mutmut_38': xǁDependencyErrorǁ__init____mutmut_38, 
        'xǁDependencyErrorǁ__init____mutmut_39': xǁDependencyErrorǁ__init____mutmut_39, 
        'xǁDependencyErrorǁ__init____mutmut_40': xǁDependencyErrorǁ__init____mutmut_40, 
        'xǁDependencyErrorǁ__init____mutmut_41': xǁDependencyErrorǁ__init____mutmut_41, 
        'xǁDependencyErrorǁ__init____mutmut_42': xǁDependencyErrorǁ__init____mutmut_42, 
        'xǁDependencyErrorǁ__init____mutmut_43': xǁDependencyErrorǁ__init____mutmut_43, 
        'xǁDependencyErrorǁ__init____mutmut_44': xǁDependencyErrorǁ__init____mutmut_44, 
        'xǁDependencyErrorǁ__init____mutmut_45': xǁDependencyErrorǁ__init____mutmut_45, 
        'xǁDependencyErrorǁ__init____mutmut_46': xǁDependencyErrorǁ__init____mutmut_46, 
        'xǁDependencyErrorǁ__init____mutmut_47': xǁDependencyErrorǁ__init____mutmut_47
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDependencyErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁDependencyErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁDependencyErrorǁ__init____mutmut_orig)
    xǁDependencyErrorǁ__init____mutmut_orig.__name__ = 'xǁDependencyErrorǁ__init__'


# Command Errors
# ==============


class CommandNotFoundError(WrkenvError):
    """Command or subcommand not found."""

    def xǁCommandNotFoundErrorǁ__init____mutmut_orig(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_1(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = None

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_2(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = ""
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_3(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = None

        super().__init__(message, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_4(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(None)}?"

        super().__init__(message, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_5(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {'XX, XX'.join(similar_commands)}?"

        super().__init__(message, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_6(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(None, hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_7(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, None)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_8(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(hint)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_9(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, )
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_10(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        hint = None
        if similar_commands:
            hint = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, hint)
        self.command = None
    
    xǁCommandNotFoundErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCommandNotFoundErrorǁ__init____mutmut_1': xǁCommandNotFoundErrorǁ__init____mutmut_1, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_2': xǁCommandNotFoundErrorǁ__init____mutmut_2, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_3': xǁCommandNotFoundErrorǁ__init____mutmut_3, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_4': xǁCommandNotFoundErrorǁ__init____mutmut_4, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_5': xǁCommandNotFoundErrorǁ__init____mutmut_5, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_6': xǁCommandNotFoundErrorǁ__init____mutmut_6, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_7': xǁCommandNotFoundErrorǁ__init____mutmut_7, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_8': xǁCommandNotFoundErrorǁ__init____mutmut_8, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_9': xǁCommandNotFoundErrorǁ__init____mutmut_9, 
        'xǁCommandNotFoundErrorǁ__init____mutmut_10': xǁCommandNotFoundErrorǁ__init____mutmut_10
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCommandNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCommandNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCommandNotFoundErrorǁ__init____mutmut_orig)
    xǁCommandNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁCommandNotFoundErrorǁ__init__'


# Workenv Errors
# ==============


class WorkenvError(WrkenvError):
    """Workenv environment errors."""

    def xǁWorkenvErrorǁ__init____mutmut_orig(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, hint)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_1(self, message: str, workenv_path: str | None = None) -> None:
        hint = ""
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, hint)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_2(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = None

        super().__init__(message, hint)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_3(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(None, hint)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_4(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, None)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_5(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(hint)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_6(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, )
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_7(self, message: str, workenv_path: str | None = None) -> None:
        hint = None
        if workenv_path:
            hint = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, hint)
        self.workenv_path = None
    
    xǁWorkenvErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvErrorǁ__init____mutmut_1': xǁWorkenvErrorǁ__init____mutmut_1, 
        'xǁWorkenvErrorǁ__init____mutmut_2': xǁWorkenvErrorǁ__init____mutmut_2, 
        'xǁWorkenvErrorǁ__init____mutmut_3': xǁWorkenvErrorǁ__init____mutmut_3, 
        'xǁWorkenvErrorǁ__init____mutmut_4': xǁWorkenvErrorǁ__init____mutmut_4, 
        'xǁWorkenvErrorǁ__init____mutmut_5': xǁWorkenvErrorǁ__init____mutmut_5, 
        'xǁWorkenvErrorǁ__init____mutmut_6': xǁWorkenvErrorǁ__init____mutmut_6, 
        'xǁWorkenvErrorǁ__init____mutmut_7': xǁWorkenvErrorǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkenvErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkenvErrorǁ__init____mutmut_orig)
    xǁWorkenvErrorǁ__init____mutmut_orig.__name__ = 'xǁWorkenvErrorǁ__init__'


# Package Errors
# ==============


class PackageError(ResourceError):
    """Package building or verification errors."""

    def xǁPackageErrorǁ__init____mutmut_orig(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="package",
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_1(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=None,
            resource_type="package",
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_2(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type=None,
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_3(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="package",
            resource_path=None,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_4(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="package",
            resource_path=package_name,
            hint=None,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_5(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            resource_type="package",
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_6(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_7(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="package",
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_8(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="package",
            resource_path=package_name,
            )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_9(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="XXpackageXX",
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_10(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="PACKAGE",
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = package_name

    def xǁPackageErrorǁ__init____mutmut_11(self, message: str, package_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(
            message=message,
            resource_type="package",
            resource_path=package_name,
            hint=hint,
        )
        self.package_name = None
    
    xǁPackageErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPackageErrorǁ__init____mutmut_1': xǁPackageErrorǁ__init____mutmut_1, 
        'xǁPackageErrorǁ__init____mutmut_2': xǁPackageErrorǁ__init____mutmut_2, 
        'xǁPackageErrorǁ__init____mutmut_3': xǁPackageErrorǁ__init____mutmut_3, 
        'xǁPackageErrorǁ__init____mutmut_4': xǁPackageErrorǁ__init____mutmut_4, 
        'xǁPackageErrorǁ__init____mutmut_5': xǁPackageErrorǁ__init____mutmut_5, 
        'xǁPackageErrorǁ__init____mutmut_6': xǁPackageErrorǁ__init____mutmut_6, 
        'xǁPackageErrorǁ__init____mutmut_7': xǁPackageErrorǁ__init____mutmut_7, 
        'xǁPackageErrorǁ__init____mutmut_8': xǁPackageErrorǁ__init____mutmut_8, 
        'xǁPackageErrorǁ__init____mutmut_9': xǁPackageErrorǁ__init____mutmut_9, 
        'xǁPackageErrorǁ__init____mutmut_10': xǁPackageErrorǁ__init____mutmut_10, 
        'xǁPackageErrorǁ__init____mutmut_11': xǁPackageErrorǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPackageErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPackageErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPackageErrorǁ__init____mutmut_orig)
    xǁPackageErrorǁ__init____mutmut_orig.__name__ = 'xǁPackageErrorǁ__init__'


# Container Errors
# ================


class ContainerError(WrkenvError):
    """Base container-related errors."""

    def xǁContainerErrorǁ__init____mutmut_orig(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_1(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_2(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = None
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_3(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "XXMake sure Docker is installed and runningXX"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_4(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "make sure docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_5(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "MAKE SURE DOCKER IS INSTALLED AND RUNNING"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_6(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint = f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_7(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint -= f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_8(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(None, hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_9(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, None)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_10(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(hint)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_11(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, )
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_12(self, message: str, container_name: str | None = None, hint: str | None = None) -> None:
        if not hint:
            hint = "Make sure Docker is installed and running"
            if container_name:
                hint += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, hint)
        self.container_name = None
    
    xǁContainerErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁContainerErrorǁ__init____mutmut_1': xǁContainerErrorǁ__init____mutmut_1, 
        'xǁContainerErrorǁ__init____mutmut_2': xǁContainerErrorǁ__init____mutmut_2, 
        'xǁContainerErrorǁ__init____mutmut_3': xǁContainerErrorǁ__init____mutmut_3, 
        'xǁContainerErrorǁ__init____mutmut_4': xǁContainerErrorǁ__init____mutmut_4, 
        'xǁContainerErrorǁ__init____mutmut_5': xǁContainerErrorǁ__init____mutmut_5, 
        'xǁContainerErrorǁ__init____mutmut_6': xǁContainerErrorǁ__init____mutmut_6, 
        'xǁContainerErrorǁ__init____mutmut_7': xǁContainerErrorǁ__init____mutmut_7, 
        'xǁContainerErrorǁ__init____mutmut_8': xǁContainerErrorǁ__init____mutmut_8, 
        'xǁContainerErrorǁ__init____mutmut_9': xǁContainerErrorǁ__init____mutmut_9, 
        'xǁContainerErrorǁ__init____mutmut_10': xǁContainerErrorǁ__init____mutmut_10, 
        'xǁContainerErrorǁ__init____mutmut_11': xǁContainerErrorǁ__init____mutmut_11, 
        'xǁContainerErrorǁ__init____mutmut_12': xǁContainerErrorǁ__init____mutmut_12
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerErrorǁ__init____mutmut_orig)
    xǁContainerErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerErrorǁ__init__'


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


# Task Errors
# ===========


class TaskError(WrkenvError):
    """Base exception for task-related errors."""

    def xǁTaskErrorǁ__init____mutmut_orig(self, message: str, task_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(message, hint)
        self.task_name = task_name

    def xǁTaskErrorǁ__init____mutmut_1(self, message: str, task_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(None, hint)
        self.task_name = task_name

    def xǁTaskErrorǁ__init____mutmut_2(self, message: str, task_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(message, None)
        self.task_name = task_name

    def xǁTaskErrorǁ__init____mutmut_3(self, message: str, task_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(hint)
        self.task_name = task_name

    def xǁTaskErrorǁ__init____mutmut_4(self, message: str, task_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(message, )
        self.task_name = task_name

    def xǁTaskErrorǁ__init____mutmut_5(self, message: str, task_name: str | None = None, hint: str | None = None) -> None:
        super().__init__(message, hint)
        self.task_name = None
    
    xǁTaskErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTaskErrorǁ__init____mutmut_1': xǁTaskErrorǁ__init____mutmut_1, 
        'xǁTaskErrorǁ__init____mutmut_2': xǁTaskErrorǁ__init____mutmut_2, 
        'xǁTaskErrorǁ__init____mutmut_3': xǁTaskErrorǁ__init____mutmut_3, 
        'xǁTaskErrorǁ__init____mutmut_4': xǁTaskErrorǁ__init____mutmut_4, 
        'xǁTaskErrorǁ__init____mutmut_5': xǁTaskErrorǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTaskErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTaskErrorǁ__init____mutmut_orig)
    xǁTaskErrorǁ__init____mutmut_orig.__name__ = 'xǁTaskErrorǁ__init__'


class TaskNotFoundError(NotFoundError):
    """Task not found in registry."""

    def xǁTaskNotFoundErrorǁ__init____mutmut_orig(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_1(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = None

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_2(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = ""
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_3(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = None
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_4(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(None)
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_5(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = "XX, XX".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_6(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:6])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_7(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) >= 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_8(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 6:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_9(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str = "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_10(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str -= "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_11(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "XX...XX"
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_12(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = None

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_13(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=None,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_14(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type=None,
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_15(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=None,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_16(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=None,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_17(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_18(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_19(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_20(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_21(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="XXtaskXX",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_22(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="TASK",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = task_name

    def xǁTaskNotFoundErrorǁ__init____mutmut_23(self, task_name: str, available_tasks: list[str] | None = None) -> None:
        message = f"Task '{task_name}' not found"

        hint = None
        if available_tasks:
            # Show up to 5 similar tasks
            tasks_str = ", ".join(available_tasks[:5])
            if len(available_tasks) > 5:
                tasks_str += "..."
            hint = f"Available tasks: {tasks_str}. Use 'wrknv tasks' to see all"

        super().__init__(
            message=message,
            resource_type="task",
            resource_id=task_name,
            hint=hint,
        )
        self.task_name = None
    
    xǁTaskNotFoundErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTaskNotFoundErrorǁ__init____mutmut_1': xǁTaskNotFoundErrorǁ__init____mutmut_1, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_2': xǁTaskNotFoundErrorǁ__init____mutmut_2, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_3': xǁTaskNotFoundErrorǁ__init____mutmut_3, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_4': xǁTaskNotFoundErrorǁ__init____mutmut_4, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_5': xǁTaskNotFoundErrorǁ__init____mutmut_5, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_6': xǁTaskNotFoundErrorǁ__init____mutmut_6, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_7': xǁTaskNotFoundErrorǁ__init____mutmut_7, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_8': xǁTaskNotFoundErrorǁ__init____mutmut_8, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_9': xǁTaskNotFoundErrorǁ__init____mutmut_9, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_10': xǁTaskNotFoundErrorǁ__init____mutmut_10, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_11': xǁTaskNotFoundErrorǁ__init____mutmut_11, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_12': xǁTaskNotFoundErrorǁ__init____mutmut_12, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_13': xǁTaskNotFoundErrorǁ__init____mutmut_13, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_14': xǁTaskNotFoundErrorǁ__init____mutmut_14, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_15': xǁTaskNotFoundErrorǁ__init____mutmut_15, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_16': xǁTaskNotFoundErrorǁ__init____mutmut_16, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_17': xǁTaskNotFoundErrorǁ__init____mutmut_17, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_18': xǁTaskNotFoundErrorǁ__init____mutmut_18, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_19': xǁTaskNotFoundErrorǁ__init____mutmut_19, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_20': xǁTaskNotFoundErrorǁ__init____mutmut_20, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_21': xǁTaskNotFoundErrorǁ__init____mutmut_21, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_22': xǁTaskNotFoundErrorǁ__init____mutmut_22, 
        'xǁTaskNotFoundErrorǁ__init____mutmut_23': xǁTaskNotFoundErrorǁ__init____mutmut_23
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTaskNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTaskNotFoundErrorǁ__init____mutmut_orig)
    xǁTaskNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁTaskNotFoundErrorǁ__init__'


class TaskExecutionError(RuntimeError):
    """Task execution failed."""

    def xǁTaskExecutionErrorǁ__init____mutmut_orig(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_1(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = True,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_2(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = None

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_3(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = ""
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_4(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = None
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_5(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:201]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_6(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) >= 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_7(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 201:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_8(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview = "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_9(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview -= "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_10(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "XX...XX"
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_11(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = None

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_12(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=None,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_13(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation=None,
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_14(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=None,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_15(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=None,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_16(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_17(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_18(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_19(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_20(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="XXtask_executionXX",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_21(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="TASK_EXECUTION",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_22(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = None
        self.exit_code = exit_code
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_23(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = None
        self.stderr = stderr

    def xǁTaskExecutionErrorǁ__init____mutmut_24(
        self,
        task_name: str,
        exit_code: int,
        stderr: str | None = None,
        retry_possible: bool = False,
    ) -> None:
        message = f"Task '{task_name}' failed with exit code {exit_code}"

        hint = None
        if stderr:
            # Show first 200 chars of stderr
            stderr_preview = stderr[:200]
            if len(stderr) > 200:
                stderr_preview += "..."
            hint = f"Error output: {stderr_preview}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=retry_possible,
            hint=hint,
        )
        self.task_name = task_name
        self.exit_code = exit_code
        self.stderr = None
    
    xǁTaskExecutionErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTaskExecutionErrorǁ__init____mutmut_1': xǁTaskExecutionErrorǁ__init____mutmut_1, 
        'xǁTaskExecutionErrorǁ__init____mutmut_2': xǁTaskExecutionErrorǁ__init____mutmut_2, 
        'xǁTaskExecutionErrorǁ__init____mutmut_3': xǁTaskExecutionErrorǁ__init____mutmut_3, 
        'xǁTaskExecutionErrorǁ__init____mutmut_4': xǁTaskExecutionErrorǁ__init____mutmut_4, 
        'xǁTaskExecutionErrorǁ__init____mutmut_5': xǁTaskExecutionErrorǁ__init____mutmut_5, 
        'xǁTaskExecutionErrorǁ__init____mutmut_6': xǁTaskExecutionErrorǁ__init____mutmut_6, 
        'xǁTaskExecutionErrorǁ__init____mutmut_7': xǁTaskExecutionErrorǁ__init____mutmut_7, 
        'xǁTaskExecutionErrorǁ__init____mutmut_8': xǁTaskExecutionErrorǁ__init____mutmut_8, 
        'xǁTaskExecutionErrorǁ__init____mutmut_9': xǁTaskExecutionErrorǁ__init____mutmut_9, 
        'xǁTaskExecutionErrorǁ__init____mutmut_10': xǁTaskExecutionErrorǁ__init____mutmut_10, 
        'xǁTaskExecutionErrorǁ__init____mutmut_11': xǁTaskExecutionErrorǁ__init____mutmut_11, 
        'xǁTaskExecutionErrorǁ__init____mutmut_12': xǁTaskExecutionErrorǁ__init____mutmut_12, 
        'xǁTaskExecutionErrorǁ__init____mutmut_13': xǁTaskExecutionErrorǁ__init____mutmut_13, 
        'xǁTaskExecutionErrorǁ__init____mutmut_14': xǁTaskExecutionErrorǁ__init____mutmut_14, 
        'xǁTaskExecutionErrorǁ__init____mutmut_15': xǁTaskExecutionErrorǁ__init____mutmut_15, 
        'xǁTaskExecutionErrorǁ__init____mutmut_16': xǁTaskExecutionErrorǁ__init____mutmut_16, 
        'xǁTaskExecutionErrorǁ__init____mutmut_17': xǁTaskExecutionErrorǁ__init____mutmut_17, 
        'xǁTaskExecutionErrorǁ__init____mutmut_18': xǁTaskExecutionErrorǁ__init____mutmut_18, 
        'xǁTaskExecutionErrorǁ__init____mutmut_19': xǁTaskExecutionErrorǁ__init____mutmut_19, 
        'xǁTaskExecutionErrorǁ__init____mutmut_20': xǁTaskExecutionErrorǁ__init____mutmut_20, 
        'xǁTaskExecutionErrorǁ__init____mutmut_21': xǁTaskExecutionErrorǁ__init____mutmut_21, 
        'xǁTaskExecutionErrorǁ__init____mutmut_22': xǁTaskExecutionErrorǁ__init____mutmut_22, 
        'xǁTaskExecutionErrorǁ__init____mutmut_23': xǁTaskExecutionErrorǁ__init____mutmut_23, 
        'xǁTaskExecutionErrorǁ__init____mutmut_24': xǁTaskExecutionErrorǁ__init____mutmut_24
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskExecutionErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTaskExecutionErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTaskExecutionErrorǁ__init____mutmut_orig)
    xǁTaskExecutionErrorǁ__init____mutmut_orig.__name__ = 'xǁTaskExecutionErrorǁ__init__'


class TaskTimeoutError(RuntimeError):
    """Task execution timed out."""

    def xǁTaskTimeoutErrorǁ__init____mutmut_orig(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_1(self, task_name: str, timeout: float) -> None:
        message = None
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_2(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = None

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_3(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout / 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_4(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 3}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_5(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=None,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_6(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation=None,
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_7(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=None,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_8(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=None,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_9(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_10(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_11(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_12(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_13(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="XXtask_executionXX",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_14(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="TASK_EXECUTION",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_15(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=True,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_16(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = None
        self.timeout = timeout

    def xǁTaskTimeoutErrorǁ__init____mutmut_17(self, task_name: str, timeout: float) -> None:
        message = f"Task '{task_name}' timed out after {timeout} seconds"
        hint = f"Increase timeout in wrknv.toml:\n[tasks.{task_name}]\ntimeout = {timeout * 2}"

        super().__init__(
            message=message,
            operation="task_execution",
            retry_possible=False,
            hint=hint,
        )
        self.task_name = task_name
        self.timeout = None
    
    xǁTaskTimeoutErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTaskTimeoutErrorǁ__init____mutmut_1': xǁTaskTimeoutErrorǁ__init____mutmut_1, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_2': xǁTaskTimeoutErrorǁ__init____mutmut_2, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_3': xǁTaskTimeoutErrorǁ__init____mutmut_3, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_4': xǁTaskTimeoutErrorǁ__init____mutmut_4, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_5': xǁTaskTimeoutErrorǁ__init____mutmut_5, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_6': xǁTaskTimeoutErrorǁ__init____mutmut_6, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_7': xǁTaskTimeoutErrorǁ__init____mutmut_7, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_8': xǁTaskTimeoutErrorǁ__init____mutmut_8, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_9': xǁTaskTimeoutErrorǁ__init____mutmut_9, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_10': xǁTaskTimeoutErrorǁ__init____mutmut_10, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_11': xǁTaskTimeoutErrorǁ__init____mutmut_11, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_12': xǁTaskTimeoutErrorǁ__init____mutmut_12, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_13': xǁTaskTimeoutErrorǁ__init____mutmut_13, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_14': xǁTaskTimeoutErrorǁ__init____mutmut_14, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_15': xǁTaskTimeoutErrorǁ__init____mutmut_15, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_16': xǁTaskTimeoutErrorǁ__init____mutmut_16, 
        'xǁTaskTimeoutErrorǁ__init____mutmut_17': xǁTaskTimeoutErrorǁ__init____mutmut_17
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTaskTimeoutErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTaskTimeoutErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTaskTimeoutErrorǁ__init____mutmut_orig)
    xǁTaskTimeoutErrorǁ__init____mutmut_orig.__name__ = 'xǁTaskTimeoutErrorǁ__init__'


# 🧰🌍🔚
