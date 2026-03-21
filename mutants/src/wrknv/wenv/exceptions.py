#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Custom Exceptions
========================
Centralized exception definitions with helpful error messages and suggestions.

Requires Python 3.11+ for native type hint support with pipe operators."""

from __future__ import annotations

from provide.foundation.errors import FoundationError
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


class WrkenvError(FoundationError):
    """Base exception for all wrknv errors."""

    def xǁWrkenvErrorǁ__init____mutmut_orig(self, message: str, suggestion: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.suggestion = suggestion
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_1(self, message: str, suggestion: str | None = None, exit_code: int = 2) -> None:
        super().__init__(message)
        self.message = message
        self.suggestion = suggestion
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_2(self, message: str, suggestion: str | None = None, exit_code: int = 1) -> None:
        super().__init__(None)
        self.message = message
        self.suggestion = suggestion
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_3(self, message: str, suggestion: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = None
        self.suggestion = suggestion
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_4(self, message: str, suggestion: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.suggestion = None
        self.exit_code = exit_code

    def xǁWrkenvErrorǁ__init____mutmut_5(self, message: str, suggestion: str | None = None, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.suggestion = suggestion
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
        if self.suggestion:
            return f"{self.message}\n💡 {self.suggestion}"
        return self.message


class ConfigurationError(WrkenvError):
    """Configuration file or settings errors."""

    def xǁConfigurationErrorǁ__init____mutmut_orig(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, suggestion)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_1(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = None
        super().__init__(message, suggestion)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_2(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(None, suggestion)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_3(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, None)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_4(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(suggestion)
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_5(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, )
        self.line_number = line_number

    def xǁConfigurationErrorǁ__init____mutmut_6(
        self,
        message: str,
        suggestion: str | None = None,
        line_number: int | None = None,
    ) -> None:
        if line_number:
            message = f"Line {line_number}: {message}"
        super().__init__(message, suggestion)
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

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_1(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_2(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = None

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_3(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = ""
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_4(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = None

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_5(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(None)}"

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_6(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {'XX, XX'.join(available_profiles)}"

        super().__init__(message, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_7(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(None, suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_8(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

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

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(suggestion)
        self.profile_name = profile_name

    def xǁProfileErrorǁ__init____mutmut_10(
        self,
        profile_name: str,
        message: str | None = None,
        available_profiles: list[str] | None = None,
    ) -> None:
        if not message:
            message = f"Profile '{profile_name}' not found"

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

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

        suggestion = None
        if available_profiles:
            suggestion = f"Available profiles: {', '.join(available_profiles)}"

        super().__init__(message, suggestion)
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


class ToolNotFoundError(WrkenvError):
    """Tool or version not found errors."""

    def xǁToolNotFoundErrorǁ__init____mutmut_orig(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_1(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = None

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_2(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = ""
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_3(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = None
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_4(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(None)
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_5(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = "XX, XX".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_6(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:6])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_7(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) >= 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_8(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 6:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_9(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str = "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_10(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str -= "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_11(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "XX...XX"
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_12(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = None

        super().__init__(message, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_13(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(None, suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_14(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, None)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_15(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(suggestion)
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_16(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, )
        self.tool = tool
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_17(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
        self.tool = None
        self.version = version

    def xǁToolNotFoundErrorǁ__init____mutmut_18(
        self, tool: str, version: str | None = None, available_versions: list[str] | None = None
    ) -> None:
        message = f"{tool} version {version} not found" if version else f"{tool} not found"

        suggestion = None
        if available_versions:
            # Show up to 5 closest versions
            versions_str = ", ".join(available_versions[:5])
            if len(available_versions) > 5:
                versions_str += "..."
            suggestion = f"Available versions: {versions_str}. Use 'wrknv {tool} --list' to see all"

        super().__init__(message, suggestion)
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
        'xǁToolNotFoundErrorǁ__init____mutmut_18': xǁToolNotFoundErrorǁ__init____mutmut_18
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁToolNotFoundErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁToolNotFoundErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁToolNotFoundErrorǁ__init____mutmut_orig)
    xǁToolNotFoundErrorǁ__init____mutmut_orig.__name__ = 'xǁToolNotFoundErrorǁ__init__'


class NetworkError(WrkenvError):
    """Network-related errors during downloads."""

    def xǁNetworkErrorǁ__init____mutmut_orig(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_1(self, message: str, url: str | None = None) -> None:
        suggestion = None
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_2(self, message: str, url: str | None = None) -> None:
        suggestion = "XXCheck your internet connection and proxy settingsXX"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_3(self, message: str, url: str | None = None) -> None:
        suggestion = "check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_4(self, message: str, url: str | None = None) -> None:
        suggestion = "CHECK YOUR INTERNET CONNECTION AND PROXY SETTINGS"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_5(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = None
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_6(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion = f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_7(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion -= f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_8(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(None, suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_9(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, None)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_10(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(suggestion)
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_11(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, )
        self.url = url

    def xǁNetworkErrorǁ__init____mutmut_12(self, message: str, url: str | None = None) -> None:
        suggestion = "Check your internet connection and proxy settings"
        if url:
            message = f"Failed to download from {url}: {message}"
            suggestion += f"\nTry downloading manually: curl -LO {url}"

        super().__init__(message, suggestion)
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


class PermissionError(WrkenvError):
    """File or directory permission errors."""

    def xǁPermissionErrorǁ__init____mutmut_orig(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_1(self, path: str, operation: str = "XXaccessXX") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_2(self, path: str, operation: str = "ACCESS") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_3(self, path: str, operation: str = "access") -> None:
        message = None
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_4(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = None
        super().__init__(message, suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_5(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(None, suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_6(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, None)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_7(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(suggestion)
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_8(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, )
        self.path = path

    def xǁPermissionErrorǁ__init____mutmut_9(self, path: str, operation: str = "access") -> None:
        message = f"Permission denied: Cannot {operation} {path}"
        suggestion = f"Try running with sudo or check file ownership: ls -la {path}"
        super().__init__(message, suggestion)
        self.path = None
    
    xǁPermissionErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPermissionErrorǁ__init____mutmut_1': xǁPermissionErrorǁ__init____mutmut_1, 
        'xǁPermissionErrorǁ__init____mutmut_2': xǁPermissionErrorǁ__init____mutmut_2, 
        'xǁPermissionErrorǁ__init____mutmut_3': xǁPermissionErrorǁ__init____mutmut_3, 
        'xǁPermissionErrorǁ__init____mutmut_4': xǁPermissionErrorǁ__init____mutmut_4, 
        'xǁPermissionErrorǁ__init____mutmut_5': xǁPermissionErrorǁ__init____mutmut_5, 
        'xǁPermissionErrorǁ__init____mutmut_6': xǁPermissionErrorǁ__init____mutmut_6, 
        'xǁPermissionErrorǁ__init____mutmut_7': xǁPermissionErrorǁ__init____mutmut_7, 
        'xǁPermissionErrorǁ__init____mutmut_8': xǁPermissionErrorǁ__init____mutmut_8, 
        'xǁPermissionErrorǁ__init____mutmut_9': xǁPermissionErrorǁ__init____mutmut_9
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPermissionErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPermissionErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPermissionErrorǁ__init____mutmut_orig)
    xǁPermissionErrorǁ__init____mutmut_orig.__name__ = 'xǁPermissionErrorǁ__init__'


class DependencyError(WrkenvError):
    """Missing system dependencies."""

    def xǁDependencyErrorǁ__init____mutmut_orig(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_1(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = None
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_2(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(None)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_3(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = "XX, XX".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_4(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = None

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_5(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message = f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_6(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message -= f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_7(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = None
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_8(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "XXInstall missing dependencies:\nXX"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_9(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_10(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "INSTALL MISSING DEPENDENCIES:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_11(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep != "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_12(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "XXgitXX":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_13(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "GIT":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_14(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion = "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_15(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion -= "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_16(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "XX  • git: https://git-scm.com/downloads\nXX"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_17(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • GIT: HTTPS://GIT-SCM.COM/DOWNLOADS\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_18(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep != "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_19(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "XXcurlXX":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_20(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "CURL":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_21(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion = "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_22(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion -= "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_23(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "XX  • curl: Install via package manager (apt/brew/yum)\nXX"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_24(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_25(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • CURL: INSTALL VIA PACKAGE MANAGER (APT/BREW/YUM)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_26(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep != "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_27(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "XXdockerXX":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_28(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "DOCKER":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_29(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion = "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_30(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion -= "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_31(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "XX  • docker: https://docs.docker.com/get-docker/\nXX"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_32(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • DOCKER: HTTPS://DOCS.DOCKER.COM/GET-DOCKER/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_33(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep != "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_34(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "XXpython3XX":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_35(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "PYTHON3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_36(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion = "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_37(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion -= "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_38(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "XX  • python3: https://www.python.org/downloads/\nXX"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_39(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • PYTHON3: HTTPS://WWW.PYTHON.ORG/DOWNLOADS/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_40(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion = f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_41(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion -= f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_42(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(None, suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_43(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, None)
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_44(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(suggestion.rstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_45(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, )
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_46(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.lstrip())
        self.missing_deps = missing_deps

    def xǁDependencyErrorǁ__init____mutmut_47(self, missing_deps: list[str], required_for: str | None = None) -> None:
        deps_str = ", ".join(missing_deps)
        message = f"Missing required dependencies: {deps_str}"

        if required_for:
            message += f" (required for {required_for})"

        suggestion = "Install missing dependencies:\n"
        for dep in missing_deps:
            if dep == "git":
                suggestion += "  • git: https://git-scm.com/downloads\n"
            elif dep == "curl":
                suggestion += "  • curl: Install via package manager (apt/brew/yum)\n"
            elif dep == "docker":
                suggestion += "  • docker: https://docs.docker.com/get-docker/\n"
            elif dep == "python3":
                suggestion += "  • python3: https://www.python.org/downloads/\n"
            else:
                suggestion += f"  • {dep}: Install via package manager\n"

        super().__init__(message, suggestion.rstrip())
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


class CommandNotFoundError(WrkenvError):
    """Command or subcommand not found."""

    def xǁCommandNotFoundErrorǁ__init____mutmut_orig(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_1(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = None

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_2(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = ""
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_3(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = None

        super().__init__(message, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_4(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(None)}?"

        super().__init__(message, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_5(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {'XX, XX'.join(similar_commands)}?"

        super().__init__(message, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_6(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(None, suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_7(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, None)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_8(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(suggestion)
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_9(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, )
        self.command = command

    def xǁCommandNotFoundErrorǁ__init____mutmut_10(self, command: str, similar_commands: list[str] | None = None) -> None:
        message = f"Command '{command}' not found"

        suggestion = None
        if similar_commands:
            suggestion = f"Did you mean: {', '.join(similar_commands)}?"

        super().__init__(message, suggestion)
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


class WorkenvError(WrkenvError):
    """Workenv environment errors."""

    def xǁWorkenvErrorǁ__init____mutmut_orig(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, suggestion)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_1(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = ""
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, suggestion)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_2(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = None

        super().__init__(message, suggestion)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_3(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(None, suggestion)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_4(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, None)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_5(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(suggestion)
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_6(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, )
        self.workenv_path = workenv_path

    def xǁWorkenvErrorǁ__init____mutmut_7(self, message: str, workenv_path: str | None = None) -> None:
        suggestion = None
        if workenv_path:
            suggestion = f"Try recreating the workenv: rm -rf {workenv_path} && wrknv setup --init"

        super().__init__(message, suggestion)
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


class ContainerError(WrkenvError):
    """Container-related errors."""

    def xǁContainerErrorǁ__init____mutmut_orig(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_1(self, message: str, container_name: str | None = None) -> None:
        suggestion = None
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_2(self, message: str, container_name: str | None = None) -> None:
        suggestion = "XXMake sure Docker is installed and runningXX"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_3(self, message: str, container_name: str | None = None) -> None:
        suggestion = "make sure docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_4(self, message: str, container_name: str | None = None) -> None:
        suggestion = "MAKE SURE DOCKER IS INSTALLED AND RUNNING"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_5(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion = f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_6(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion -= f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_7(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(None, suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_8(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, None)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_9(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(suggestion)
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_10(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, )
        self.container_name = container_name

    def xǁContainerErrorǁ__init____mutmut_11(self, message: str, container_name: str | None = None) -> None:
        suggestion = "Make sure Docker is installed and running"
        if container_name:
            suggestion += f"\nCheck container status: docker ps -a | grep {container_name}"

        super().__init__(message, suggestion)
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
        'xǁContainerErrorǁ__init____mutmut_11': xǁContainerErrorǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁContainerErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁContainerErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁContainerErrorǁ__init____mutmut_orig)
    xǁContainerErrorǁ__init____mutmut_orig.__name__ = 'xǁContainerErrorǁ__init__'


class PackageError(WrkenvError):
    """Package building or verification errors."""


# 🧰🌍🔚
