#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Configuration Validation for wrknv
===================================
Validation methods for configuration data."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from wrknv.config.core import WorkenvConfig
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


class WorkenvConfigValidator:
    """Validator for WorkenvConfig instances."""

    def xǁWorkenvConfigValidatorǁ__init____mutmut_orig(self, config: WorkenvConfig) -> None:
        """Initialize validator with config instance."""
        self.config = config

    def xǁWorkenvConfigValidatorǁ__init____mutmut_1(self, config: WorkenvConfig) -> None:
        """Initialize validator with config instance."""
        self.config = None
    
    xǁWorkenvConfigValidatorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ__init____mutmut_1': xǁWorkenvConfigValidatorǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ__init____mutmut_orig)
    xǁWorkenvConfigValidatorǁ__init____mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ__init__'

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_orig(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_1(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = None

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_2(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_3(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(None)
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_4(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(None)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_5(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_6(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append(None)
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_7(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("XXproject_name cannot be emptyXX")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_8(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("PROJECT_NAME CANNOT BE EMPTY")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_9(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_10(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(None):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_11(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(None)

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_12(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_13(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(None)
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_14(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(None)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_15(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_16(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(None):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_17(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(None)

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_18(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_19(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(None)
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_20(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(None)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_21(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = None
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_22(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(None, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_23(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, None)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_24(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_25(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, )
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_26(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(None)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_27(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_28(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(None)
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_29(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(None)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_30(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = None
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_31(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(None, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_32(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, None)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_33(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_34(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, )
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_35(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(None)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_36(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = None
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_37(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(None)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_38(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_39(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(None)
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_40(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(None)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_41(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = None
            errors.extend(env_errors)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_42(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(None)

        return len(errors) == 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_43(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) != 0, errors

    def xǁWorkenvConfigValidatorǁvalidate__mutmut_44(self) -> tuple[bool, list[str]]:
        """Validate the entire configuration.

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Basic validation
        if not isinstance(self.config.project_name, str):
            errors.append(f"project_name must be string, got {type(self.config.project_name)}")
        elif not self.config.project_name.strip():
            errors.append("project_name cannot be empty")
        elif not self._is_valid_project_name(self.config.project_name):
            errors.append(f"Invalid project_name: {self.config.project_name}")

        if not isinstance(self.config.version, str):
            errors.append(f"version must be string, got {type(self.config.version)}")
        elif not self._is_valid_version(self.config.version):
            errors.append(f"Invalid version: {self.config.version}")

        # Validate tools
        if not isinstance(self.config.tools, dict):
            errors.append(f"tools must be dictionary, got {type(self.config.tools)}")
        else:
            for tool_name, tool_config in self.config.tools.items():
                tool_errors = self._validate_tool_config(tool_name, tool_config)
                errors.extend(tool_errors)

        # Validate profiles
        if not isinstance(self.config.profiles, dict):
            errors.append(f"profiles must be dictionary, got {type(self.config.profiles)}")
        else:
            for profile_name, profile_config in self.config.profiles.items():
                profile_errors = self._validate_profile_config(profile_name, profile_config)
                errors.extend(profile_errors)

        # Validate workenv settings
        workenv_errors = self._validate_workenv_settings()
        errors.extend(workenv_errors)

        # Validate env configuration
        if not isinstance(self.config.env, dict):
            errors.append(f"env must be dictionary, got {type(self.config.env)}")
        else:
            env_errors = self._validate_env_config()
            errors.extend(env_errors)

        return len(errors) == 1, errors
    
    xǁWorkenvConfigValidatorǁvalidate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁvalidate__mutmut_1': xǁWorkenvConfigValidatorǁvalidate__mutmut_1, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_2': xǁWorkenvConfigValidatorǁvalidate__mutmut_2, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_3': xǁWorkenvConfigValidatorǁvalidate__mutmut_3, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_4': xǁWorkenvConfigValidatorǁvalidate__mutmut_4, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_5': xǁWorkenvConfigValidatorǁvalidate__mutmut_5, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_6': xǁWorkenvConfigValidatorǁvalidate__mutmut_6, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_7': xǁWorkenvConfigValidatorǁvalidate__mutmut_7, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_8': xǁWorkenvConfigValidatorǁvalidate__mutmut_8, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_9': xǁWorkenvConfigValidatorǁvalidate__mutmut_9, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_10': xǁWorkenvConfigValidatorǁvalidate__mutmut_10, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_11': xǁWorkenvConfigValidatorǁvalidate__mutmut_11, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_12': xǁWorkenvConfigValidatorǁvalidate__mutmut_12, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_13': xǁWorkenvConfigValidatorǁvalidate__mutmut_13, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_14': xǁWorkenvConfigValidatorǁvalidate__mutmut_14, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_15': xǁWorkenvConfigValidatorǁvalidate__mutmut_15, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_16': xǁWorkenvConfigValidatorǁvalidate__mutmut_16, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_17': xǁWorkenvConfigValidatorǁvalidate__mutmut_17, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_18': xǁWorkenvConfigValidatorǁvalidate__mutmut_18, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_19': xǁWorkenvConfigValidatorǁvalidate__mutmut_19, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_20': xǁWorkenvConfigValidatorǁvalidate__mutmut_20, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_21': xǁWorkenvConfigValidatorǁvalidate__mutmut_21, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_22': xǁWorkenvConfigValidatorǁvalidate__mutmut_22, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_23': xǁWorkenvConfigValidatorǁvalidate__mutmut_23, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_24': xǁWorkenvConfigValidatorǁvalidate__mutmut_24, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_25': xǁWorkenvConfigValidatorǁvalidate__mutmut_25, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_26': xǁWorkenvConfigValidatorǁvalidate__mutmut_26, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_27': xǁWorkenvConfigValidatorǁvalidate__mutmut_27, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_28': xǁWorkenvConfigValidatorǁvalidate__mutmut_28, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_29': xǁWorkenvConfigValidatorǁvalidate__mutmut_29, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_30': xǁWorkenvConfigValidatorǁvalidate__mutmut_30, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_31': xǁWorkenvConfigValidatorǁvalidate__mutmut_31, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_32': xǁWorkenvConfigValidatorǁvalidate__mutmut_32, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_33': xǁWorkenvConfigValidatorǁvalidate__mutmut_33, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_34': xǁWorkenvConfigValidatorǁvalidate__mutmut_34, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_35': xǁWorkenvConfigValidatorǁvalidate__mutmut_35, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_36': xǁWorkenvConfigValidatorǁvalidate__mutmut_36, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_37': xǁWorkenvConfigValidatorǁvalidate__mutmut_37, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_38': xǁWorkenvConfigValidatorǁvalidate__mutmut_38, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_39': xǁWorkenvConfigValidatorǁvalidate__mutmut_39, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_40': xǁWorkenvConfigValidatorǁvalidate__mutmut_40, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_41': xǁWorkenvConfigValidatorǁvalidate__mutmut_41, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_42': xǁWorkenvConfigValidatorǁvalidate__mutmut_42, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_43': xǁWorkenvConfigValidatorǁvalidate__mutmut_43, 
        'xǁWorkenvConfigValidatorǁvalidate__mutmut_44': xǁWorkenvConfigValidatorǁvalidate__mutmut_44
    }
    
    def validate(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁvalidate__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁvalidate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    validate.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁvalidate__mutmut_orig)
    xǁWorkenvConfigValidatorǁvalidate__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁvalidate'

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_orig(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_1(self, version: str) -> bool:
        """Check if version string is valid."""
        if isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_2(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return True

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_3(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version not in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_4(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("XXlatestXX", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_5(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("LATEST", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_6(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "XXstableXX", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_7(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "STABLE", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_8(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "XXdevXX", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_9(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "DEV", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_10(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "XXmainXX", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_11(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "MAIN", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_12(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "XXmasterXX"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_13(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "MASTER"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_14(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return False

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_15(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith(None):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_16(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("XXvXX"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_17(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("V"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_18(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = None  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_19(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[2:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_20(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = None
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_21(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split(None)[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_22(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("XX-XX")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_23(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[1]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_24(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = None

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_25(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(None)

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_26(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split("XX.XX")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_27(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 and len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_28(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) <= 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_29(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 3 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_30(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) >= 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_31(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 5:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_32(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return True

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_33(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(None):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_34(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i <= 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_35(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 3:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_36(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(None)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_37(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_38(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() and part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_39(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace(None, "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_40(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", None).isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_41(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_42(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", ).isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_43(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace(None, "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_44(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", None).replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_45(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_46(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", ).replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_47(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("XX_XX", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_48(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "XXXX").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_49(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("XX-XX", "").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_50(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "XXXX").isalnum()):
                    return False
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_51(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return True
            return True
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_52(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return False
        except ValueError:
            return False

    def xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_53(self, version: str) -> bool:
        """Check if version string is valid."""
        if not isinstance(version, str):
            return False

        if version in ("latest", "stable", "dev", "main", "master"):
            return True

        # Basic semver check (supports X.Y, X.Y.Z, X.Y.Z-suffix)
        if version.startswith("v"):
            version = version[1:]  # Remove 'v' prefix

        # Handle pre-release versions (e.g., 1.2.3-beta.1)
        base_version = version.split("-")[0]
        parts = base_version.split(".")

        if len(parts) < 2 or len(parts) > 4:
            return False

        # Check that major and minor versions are numeric
        try:
            for i, part in enumerate(parts):
                if i < 2:  # Major and minor must be numeric
                    int(part)
                elif not (part.isdigit() or part.replace("_", "").replace("-", "").isalnum()):
                    return False
            return True
        except ValueError:
            return True
    
    xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_1': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_2': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_3': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_4': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_5': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_6': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_7': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_8': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_9': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_9, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_10': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_10, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_11': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_11, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_12': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_12, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_13': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_13, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_14': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_14, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_15': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_15, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_16': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_16, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_17': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_17, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_18': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_18, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_19': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_19, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_20': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_20, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_21': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_21, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_22': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_22, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_23': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_23, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_24': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_24, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_25': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_25, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_26': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_26, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_27': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_27, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_28': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_28, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_29': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_29, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_30': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_30, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_31': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_31, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_32': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_32, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_33': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_33, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_34': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_34, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_35': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_35, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_36': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_36, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_37': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_37, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_38': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_38, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_39': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_39, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_40': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_40, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_41': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_41, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_42': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_42, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_43': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_43, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_44': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_44, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_45': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_45, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_46': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_46, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_47': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_47, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_48': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_48, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_49': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_49, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_50': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_50, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_51': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_51, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_52': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_52, 
        'xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_53': xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_53
    }
    
    def _is_valid_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_valid_version.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_is_valid_version__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_is_valid_version'

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_orig(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(pattern, name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_1(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = None
        return bool(re.match(pattern, name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_2(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"XX^[a-zA-Z0-9._-]+$XX"
        return bool(re.match(pattern, name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_3(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-za-z0-9._-]+$"
        return bool(re.match(pattern, name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_4(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[A-ZA-Z0-9._-]+$"
        return bool(re.match(pattern, name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_5(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(pattern, name)) or len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_6(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(None) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_7(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(None, name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_8(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(pattern, None)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_9(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(name)) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_10(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(pattern, )) and len(name) <= 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_11(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(pattern, name)) and len(name) < 100

    def xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_12(self, name: str) -> bool:
        """Check if project name follows valid naming conventions."""
        import re

        # Allow letters, numbers, hyphens, underscores, and dots
        pattern = r"^[a-zA-Z0-9._-]+$"
        return bool(re.match(pattern, name)) and len(name) <= 101
    
    xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_1': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_2': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_3': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_4': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_5': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_6': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_7': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_8': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_9': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_9, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_10': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_10, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_11': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_11, 
        'xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_12': xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_12
    }
    
    def _is_valid_project_name(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_valid_project_name.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_is_valid_project_name__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_is_valid_project_name'

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_orig(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_1(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = None

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_2(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_3(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(None)
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_4(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(None)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_5(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_6(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append(None)
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_7(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("XXTool name cannot be emptyXX")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_8(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_9(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("TOOL NAME CANNOT BE EMPTY")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_10(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_11(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(None):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_12(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(None)
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_13(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_14(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(None)
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_15(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(None):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_16(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_17(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(None)
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_18(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_19(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(None):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_20(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(None)
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_21(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = None
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_22(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get(None)
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_23(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("XXversionXX")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_24(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("VERSION")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_25(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_26(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_27(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(None)
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_28(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_29(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(None):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_30(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(None)

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_31(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = None
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_32(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get(None)
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_33(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("XXpathXX")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_34(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("PATH")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_35(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None or not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_36(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_37(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_38(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(None)

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_39(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = None
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_40(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get(None)
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_41(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("XXenvXX")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_42(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("ENV")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_43(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_44(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_45(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(None)
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_46(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_47(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(None)
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_48(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_49(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(None)
        else:
            errors.append(f"Tool configuration for '{tool_name}' must be string, list, or dictionary")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_50(self, tool_name: str, tool_config: Any) -> list[str]:
        """Validate individual tool configuration."""
        errors = []

        if not isinstance(tool_name, str):
            errors.append(f"Tool name must be string, got {type(tool_name)}")
            return errors

        if not tool_name.strip():
            errors.append("Tool name cannot be empty")
            return errors

        # Tool config can be string (version), dict (detailed config), or list (matrix config)
        if isinstance(tool_config, str):
            if not self._is_valid_version(tool_config):
                errors.append(f"Invalid version for tool '{tool_name}': {tool_config}")
        elif isinstance(tool_config, list):
            # Matrix configuration - validate each version in the list
            if not tool_config:
                errors.append(f"Tool '{tool_name}' has empty version list")
            else:
                for i, version in enumerate(tool_config):
                    if not isinstance(version, str):
                        errors.append(f"Version {i} for tool '{tool_name}' must be string")
                    elif not self._is_valid_version(version):
                        errors.append(f"Invalid version {i} for tool '{tool_name}': {version}")
        elif isinstance(tool_config, dict):
            # Validate version if present
            version = tool_config.get("version")
            if version is not None:
                if not isinstance(version, str):
                    errors.append(f"Version for tool '{tool_name}' must be string")
                elif not self._is_valid_version(version):
                    errors.append(f"Invalid version for tool '{tool_name}': {version}")

            # Validate path if present
            path = tool_config.get("path")
            if path is not None and not isinstance(path, str):
                errors.append(f"Path for tool '{tool_name}' must be string")

            # Validate env if present
            env = tool_config.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    errors.append(f"Environment for tool '{tool_name}' must be dictionary")
                else:
                    for env_key, env_value in env.items():
                        if not isinstance(env_key, str):
                            errors.append(f"Environment key for tool '{tool_name}' must be string")
                        if not isinstance(env_value, str):
                            errors.append(f"Environment value for tool '{tool_name}' must be string")
        else:
            errors.append(None)

        return errors
    
    xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_1': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_2': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_3': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_4': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_5': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_6': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_7': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_8': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_9': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_9, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_10': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_10, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_11': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_11, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_12': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_12, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_13': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_13, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_14': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_14, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_15': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_15, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_16': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_16, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_17': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_17, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_18': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_18, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_19': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_19, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_20': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_20, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_21': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_21, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_22': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_22, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_23': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_23, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_24': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_24, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_25': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_25, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_26': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_26, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_27': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_27, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_28': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_28, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_29': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_29, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_30': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_30, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_31': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_31, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_32': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_32, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_33': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_33, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_34': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_34, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_35': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_35, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_36': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_36, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_37': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_37, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_38': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_38, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_39': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_39, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_40': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_40, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_41': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_41, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_42': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_42, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_43': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_43, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_44': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_44, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_45': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_45, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_46': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_46, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_47': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_47, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_48': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_48, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_49': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_49, 
        'xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_50': xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_50
    }
    
    def _validate_tool_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _validate_tool_config.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_validate_tool_config__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_validate_tool_config'

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_orig(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_1(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = None

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_2(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_3(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(None)
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_4(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(None)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_5(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_6(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append(None)
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_7(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("XXProfile name cannot be emptyXX")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_8(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_9(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("PROFILE NAME CANNOT BE EMPTY")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_10(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_11(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(None)
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_12(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_13(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(None)
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_14(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_15(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(None)
            elif not self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_16(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif self._is_valid_version(tool_version):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_17(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(None):
                errors.append(
                    f"Invalid version '{tool_version}' for tool '{tool_name}' in profile '{profile_name}'"
                )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_18(self, profile_name: str, profile_config: Any) -> list[str]:
        """Validate individual profile configuration."""
        errors = []

        if not isinstance(profile_name, str):
            errors.append(f"Profile name must be string, got {type(profile_name)}")
            return errors

        if not profile_name.strip():
            errors.append("Profile name cannot be empty")
            return errors

        if not isinstance(profile_config, dict):
            errors.append(f"Profile '{profile_name}' must be a dictionary")
            return errors

        # Validate profile tools
        for tool_name, tool_version in profile_config.items():
            if not isinstance(tool_name, str):
                errors.append(f"Tool name in profile '{profile_name}' must be string")
            elif not isinstance(tool_version, str):
                errors.append(f"Tool version for '{tool_name}' in profile '{profile_name}' must be string")
            elif not self._is_valid_version(tool_version):
                errors.append(
                    None
                )

        return errors
    
    xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_1': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_2': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_3': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_4': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_5': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_6': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_7': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_8': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_9': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_9, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_10': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_10, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_11': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_11, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_12': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_12, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_13': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_13, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_14': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_14, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_15': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_15, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_16': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_16, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_17': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_17, 
        'xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_18': xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_18
    }
    
    def _validate_profile_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _validate_profile_config.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_validate_profile_config__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_validate_profile_config'

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_orig(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_1(self) -> list[str]:
        """Validate workenv settings."""
        errors = None

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_2(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_3(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append(None)
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_4(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("XXworkenv must be WorkenvSettings instanceXX")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_5(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be workenvsettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_6(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("WORKENV MUST BE WORKENVSETTINGS INSTANCE")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_7(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_8(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append(None)

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_9(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("XXworkenv.auto_install must be booleanXX")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_10(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("WORKENV.AUTO_INSTALL MUST BE BOOLEAN")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_11(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_12(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append(None)

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_13(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("XXworkenv.use_cache must be booleanXX")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_14(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("WORKENV.USE_CACHE MUST BE BOOLEAN")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_15(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_16(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append(None)
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_17(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("XXworkenv.cache_ttl must be stringXX")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_18(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("WORKENV.CACHE_TTL MUST BE STRING")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_19(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_20(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(None):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_21(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(None)

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_22(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_23(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append(None)
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_24(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("XXworkenv.log_level must be stringXX")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_25(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("WORKENV.LOG_LEVEL MUST BE STRING")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_26(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_27(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("XXDEBUGXX", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_28(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("debug", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_29(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "XXINFOXX", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_30(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "info", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_31(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "XXWARNINGXX", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_32(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "warning", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_33(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "XXERRORXX", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_34(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "error", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_35(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "XXCRITICALXX"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_36(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "critical"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_37(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(None)

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_38(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_39(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append(None)
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_40(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("XXworkenv.container_runtime must be stringXX")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_41(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("WORKENV.CONTAINER_RUNTIME MUST BE STRING")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_42(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_43(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("XXdockerXX", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_44(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("DOCKER", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_45(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "XXpodmanXX", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_46(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "PODMAN", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_47(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "XXnerdctlXX"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_48(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "NERDCTL"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_49(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(None)

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_50(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_51(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append(None)
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_52(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("XXworkenv.container_registry must be stringXX")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_53(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("WORKENV.CONTAINER_REGISTRY MUST BE STRING")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_54(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_55(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(None):
            errors.append(f"Invalid container_registry URL: {self.config.workenv.container_registry}")

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_56(self) -> list[str]:
        """Validate workenv settings."""
        errors = []

        # Import here to avoid circular import
        from wrknv.config.core import WorkenvSettings

        if not isinstance(self.config.workenv, WorkenvSettings):
            errors.append("workenv must be WorkenvSettings instance")
            return errors

        # Validate boolean settings
        if not isinstance(self.config.workenv.auto_install, bool):
            errors.append("workenv.auto_install must be boolean")

        if not isinstance(self.config.workenv.use_cache, bool):
            errors.append("workenv.use_cache must be boolean")

        # Validate string settings
        if not isinstance(self.config.workenv.cache_ttl, str):
            errors.append("workenv.cache_ttl must be string")
        elif not self._is_valid_duration(self.config.workenv.cache_ttl):
            errors.append(f"Invalid cache_ttl format: {self.config.workenv.cache_ttl}")

        if not isinstance(self.config.workenv.log_level, str):
            errors.append("workenv.log_level must be string")
        elif self.config.workenv.log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            errors.append(f"Invalid log_level: {self.config.workenv.log_level}")

        if not isinstance(self.config.workenv.container_runtime, str):
            errors.append("workenv.container_runtime must be string")
        elif self.config.workenv.container_runtime not in ("docker", "podman", "nerdctl"):
            errors.append(f"Unsupported container_runtime: {self.config.workenv.container_runtime}")

        if not isinstance(self.config.workenv.container_registry, str):
            errors.append("workenv.container_registry must be string")
        elif not self._is_valid_registry_url(self.config.workenv.container_registry):
            errors.append(None)

        return errors
    
    xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_1': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_2': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_3': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_4': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_5': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_6': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_7': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_8': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_9': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_9, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_10': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_10, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_11': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_11, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_12': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_12, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_13': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_13, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_14': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_14, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_15': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_15, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_16': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_16, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_17': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_17, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_18': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_18, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_19': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_19, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_20': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_20, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_21': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_21, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_22': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_22, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_23': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_23, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_24': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_24, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_25': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_25, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_26': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_26, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_27': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_27, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_28': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_28, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_29': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_29, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_30': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_30, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_31': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_31, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_32': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_32, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_33': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_33, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_34': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_34, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_35': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_35, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_36': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_36, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_37': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_37, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_38': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_38, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_39': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_39, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_40': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_40, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_41': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_41, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_42': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_42, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_43': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_43, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_44': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_44, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_45': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_45, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_46': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_46, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_47': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_47, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_48': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_48, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_49': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_49, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_50': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_50, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_51': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_51, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_52': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_52, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_53': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_53, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_54': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_54, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_55': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_55, 
        'xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_56': xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_56
    }
    
    def _validate_workenv_settings(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _validate_workenv_settings.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_validate_workenv_settings__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_validate_workenv_settings'

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_orig(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_1(self) -> list[str]:
        """Validate environment configuration."""
        errors = None

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_2(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_3(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(None)
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_4(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(None)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_5(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_6(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append(None)
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_7(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("XXEnvironment key cannot be emptyXX")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_8(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_9(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("ENVIRONMENT KEY CANNOT BE EMPTY")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_10(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_11(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace(None, "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_12(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", None).isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_13(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_14(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", ).isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_15(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("XX_XX", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_16(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "XXXX").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_17(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    None
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_18(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_19(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(None)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_20(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(None):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_21(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, (str, int, float, bool)):
                        errors.append(
                            f"Environment list item {i} for '{key}' must be string, number, or boolean"
                        )

        return errors

    def xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_22(self) -> list[str]:
        """Validate environment configuration."""
        errors = []

        for key, value in self.config.env.items():
            if not isinstance(key, str):
                errors.append(f"Environment key must be string, got {type(key)}")
            elif not key.strip():
                errors.append("Environment key cannot be empty")
            elif not key.replace("_", "").isalnum():
                errors.append(
                    f"Invalid environment key '{key}': must contain only letters, numbers, and underscores"
                )

            # Values can be string, number, boolean, or list
            if not isinstance(value, (str, int, float, bool, list)):
                errors.append(f"Environment value for '{key}' must be string, number, boolean, or list")
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if not isinstance(item, (str, int, float, bool)):
                        errors.append(
                            None
                        )

        return errors
    
    xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_1': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_2': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_3': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_4': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_5': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_6': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_7': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_8': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_9': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_9, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_10': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_10, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_11': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_11, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_12': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_12, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_13': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_13, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_14': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_14, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_15': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_15, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_16': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_16, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_17': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_17, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_18': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_18, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_19': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_19, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_20': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_20, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_21': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_21, 
        'xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_22': xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_22
    }
    
    def _validate_env_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _validate_env_config.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_validate_env_config__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_validate_env_config'

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_orig(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[smhdw]$"
        return bool(re.match(pattern, duration))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_1(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = None
        return bool(re.match(pattern, duration))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_2(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"XX^\d+[smhdw]$XX"
        return bool(re.match(pattern, duration))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_3(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[SMHDW]$"
        return bool(re.match(pattern, duration))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_4(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[smhdw]$"
        return bool(None)

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_5(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[smhdw]$"
        return bool(re.match(None, duration))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_6(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[smhdw]$"
        return bool(re.match(pattern, None))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_7(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[smhdw]$"
        return bool(re.match(duration))

    def xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_8(self, duration: str) -> bool:
        """Check if duration string is valid (e.g., '7d', '2h', '30m')."""
        import re

        pattern = r"^\d+[smhdw]$"
        return bool(re.match(pattern, ))
    
    xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_1': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_2': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_3': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_4': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_5': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_6': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_7': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_8': xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_8
    }
    
    def _is_valid_duration(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_valid_duration.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_is_valid_duration__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_is_valid_duration'

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_orig(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$"
        return bool(re.match(pattern, url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_1(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = None
        return bool(re.match(pattern, url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_2(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"XX^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$XX"
        return bool(re.match(pattern, url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_3(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-za-z0-9.-]+(\.[a-za-z]{2,})?(/[a-za-z0-9._-]+)*$"
        return bool(re.match(pattern, url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_4(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[A-ZA-Z0-9.-]+(\.[A-ZA-Z]{2,})?(/[A-ZA-Z0-9._-]+)*$"
        return bool(re.match(pattern, url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_5(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$"
        return bool(None)

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_6(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$"
        return bool(re.match(None, url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_7(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$"
        return bool(re.match(pattern, None))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_8(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$"
        return bool(re.match(url))

    def xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_9(self, url: str) -> bool:
        """Check if registry URL is valid."""
        import re

        # Basic URL validation for container registries
        pattern = r"^[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/[a-zA-Z0-9._-]+)*$"
        return bool(re.match(pattern, ))
    
    xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_1': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_1, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_2': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_2, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_3': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_3, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_4': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_4, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_5': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_5, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_6': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_6, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_7': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_7, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_8': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_8, 
        'xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_9': xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_9
    }
    
    def _is_valid_registry_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_valid_registry_url.__signature__ = _mutmut_signature(xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_orig)
    xǁWorkenvConfigValidatorǁ_is_valid_registry_url__mutmut_orig.__name__ = 'xǁWorkenvConfigValidatorǁ_is_valid_registry_url'


# 🧰🌍🔚
