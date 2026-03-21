#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Configuration Schema
===========================
Type-safe configuration models with validation for wrknv.toml using attrs."""

from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING, Any

from attrs import Attribute, define, field, validators
import cattrs

from wrknv.config.defaults import (
    DEFAULT_AUTO_UPDATE,
    DEFAULT_CONTAINER_BASE_IMAGE,
    DEFAULT_CONTAINER_ENABLED,
    DEFAULT_CONTAINER_STORAGE_PATH,
    DEFAULT_LOG_LEVEL,
    DEFAULT_PACKAGE_LICENSE,
    DEFAULT_PYTHON_VERSION,
    DEFAULT_REGISTRY_TIMEOUT,
    DEFAULT_REGISTRY_VERIFY_SSL,
    DEFAULT_REGISTRY_WRKNV_URL,
    DEFAULT_TELEMETRY_ENABLED,
    DEFAULT_TOOL_AUTO_DETECT,
    DEFAULT_TOOL_ENABLED,
    DEFAULT_VERSION,
    DEFAULT_WORKENV_CACHE_DIR,
    DEFAULT_WORKENV_INSTALL_DIR,
)

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


def x_validate_version__mutmut_orig(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_1(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_2(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError(None)
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_3(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("XXVersion cannot be emptyXX")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_4(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_5(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("VERSION CANNOT BE EMPTY")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_6(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if (value[0].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_7(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() and value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_8(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[1].isdigit() or value.startswith("v")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_9(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith(None)):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_10(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("XXvXX")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_11(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("V")):
        raise ValueError(f"Invalid version format: {value}")


def x_validate_version__mutmut_12(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate version format."""
    if not value:
        raise ValueError("Version cannot be empty")
    # Basic version validation - must start with number or 'v'
    if not (value[0].isdigit() or value.startswith("v")):
        raise ValueError(None)

x_validate_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_version__mutmut_1': x_validate_version__mutmut_1, 
    'x_validate_version__mutmut_2': x_validate_version__mutmut_2, 
    'x_validate_version__mutmut_3': x_validate_version__mutmut_3, 
    'x_validate_version__mutmut_4': x_validate_version__mutmut_4, 
    'x_validate_version__mutmut_5': x_validate_version__mutmut_5, 
    'x_validate_version__mutmut_6': x_validate_version__mutmut_6, 
    'x_validate_version__mutmut_7': x_validate_version__mutmut_7, 
    'x_validate_version__mutmut_8': x_validate_version__mutmut_8, 
    'x_validate_version__mutmut_9': x_validate_version__mutmut_9, 
    'x_validate_version__mutmut_10': x_validate_version__mutmut_10, 
    'x_validate_version__mutmut_11': x_validate_version__mutmut_11, 
    'x_validate_version__mutmut_12': x_validate_version__mutmut_12
}

def validate_version(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_version__mutmut_orig, x_validate_version__mutmut_mutants, args, kwargs)
    return result 

validate_version.__signature__ = _mutmut_signature(x_validate_version__mutmut_orig)
x_validate_version__mutmut_orig.__name__ = 'x_validate_version'


def x_validate_python_version__mutmut_orig(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_1(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = None
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_2(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(None)
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_3(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split("XX.XX")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_4(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) <= 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_5(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 3:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_6(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(None)
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_7(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = None
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_8(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(None)
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_9(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[1])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_10(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = None
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_11(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(None)
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_12(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[2])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_13(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 and (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_14(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major <= 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_15(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 4 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_16(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 or minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_17(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major != 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_18(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 4 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_19(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor <= 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_20(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 9):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_21(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(None)
    except ValueError as e:
        raise ValueError(f"Invalid Python version format: {value}") from e


def x_validate_python_version__mutmut_22(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate Python version format."""
    parts = value.split(".")
    if len(parts) < 2:
        raise ValueError(f"Invalid Python version: {value}")
    try:
        major = int(parts[0])
        minor = int(parts[1])
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError(f"Python version must be 3.8 or higher: {value}")
    except ValueError as e:
        raise ValueError(None) from e

x_validate_python_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_python_version__mutmut_1': x_validate_python_version__mutmut_1, 
    'x_validate_python_version__mutmut_2': x_validate_python_version__mutmut_2, 
    'x_validate_python_version__mutmut_3': x_validate_python_version__mutmut_3, 
    'x_validate_python_version__mutmut_4': x_validate_python_version__mutmut_4, 
    'x_validate_python_version__mutmut_5': x_validate_python_version__mutmut_5, 
    'x_validate_python_version__mutmut_6': x_validate_python_version__mutmut_6, 
    'x_validate_python_version__mutmut_7': x_validate_python_version__mutmut_7, 
    'x_validate_python_version__mutmut_8': x_validate_python_version__mutmut_8, 
    'x_validate_python_version__mutmut_9': x_validate_python_version__mutmut_9, 
    'x_validate_python_version__mutmut_10': x_validate_python_version__mutmut_10, 
    'x_validate_python_version__mutmut_11': x_validate_python_version__mutmut_11, 
    'x_validate_python_version__mutmut_12': x_validate_python_version__mutmut_12, 
    'x_validate_python_version__mutmut_13': x_validate_python_version__mutmut_13, 
    'x_validate_python_version__mutmut_14': x_validate_python_version__mutmut_14, 
    'x_validate_python_version__mutmut_15': x_validate_python_version__mutmut_15, 
    'x_validate_python_version__mutmut_16': x_validate_python_version__mutmut_16, 
    'x_validate_python_version__mutmut_17': x_validate_python_version__mutmut_17, 
    'x_validate_python_version__mutmut_18': x_validate_python_version__mutmut_18, 
    'x_validate_python_version__mutmut_19': x_validate_python_version__mutmut_19, 
    'x_validate_python_version__mutmut_20': x_validate_python_version__mutmut_20, 
    'x_validate_python_version__mutmut_21': x_validate_python_version__mutmut_21, 
    'x_validate_python_version__mutmut_22': x_validate_python_version__mutmut_22
}

def validate_python_version(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_python_version__mutmut_orig, x_validate_python_version__mutmut_mutants, args, kwargs)
    return result 

validate_python_version.__signature__ = _mutmut_signature(x_validate_python_version__mutmut_orig)
x_validate_python_version__mutmut_orig.__name__ = 'x_validate_python_version'


def x_validate_profile_name__mutmut_orig(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_1(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_2(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError(None)
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_3(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("XXProfile name cannot be emptyXX")
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_4(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("profile name cannot be empty")
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_5(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("PROFILE NAME CANNOT BE EMPTY")
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_6(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_7(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace(None, "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_8(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("_", None).isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_9(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_10(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("_", ).isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_11(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace(None, "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_12(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", None).replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_13(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_14(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", ).replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_15(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("XX-XX", "").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_16(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "XXXX").replace("_", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_17(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("XX_XX", "").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_18(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("_", "XXXX").isalnum():
        raise ValueError(f"Invalid profile name: {value}")


def x_validate_profile_name__mutmut_19(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate profile name."""
    if not value:
        raise ValueError("Profile name cannot be empty")
    if not value.replace("-", "").replace("_", "").isalnum():
        raise ValueError(None)

x_validate_profile_name__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_profile_name__mutmut_1': x_validate_profile_name__mutmut_1, 
    'x_validate_profile_name__mutmut_2': x_validate_profile_name__mutmut_2, 
    'x_validate_profile_name__mutmut_3': x_validate_profile_name__mutmut_3, 
    'x_validate_profile_name__mutmut_4': x_validate_profile_name__mutmut_4, 
    'x_validate_profile_name__mutmut_5': x_validate_profile_name__mutmut_5, 
    'x_validate_profile_name__mutmut_6': x_validate_profile_name__mutmut_6, 
    'x_validate_profile_name__mutmut_7': x_validate_profile_name__mutmut_7, 
    'x_validate_profile_name__mutmut_8': x_validate_profile_name__mutmut_8, 
    'x_validate_profile_name__mutmut_9': x_validate_profile_name__mutmut_9, 
    'x_validate_profile_name__mutmut_10': x_validate_profile_name__mutmut_10, 
    'x_validate_profile_name__mutmut_11': x_validate_profile_name__mutmut_11, 
    'x_validate_profile_name__mutmut_12': x_validate_profile_name__mutmut_12, 
    'x_validate_profile_name__mutmut_13': x_validate_profile_name__mutmut_13, 
    'x_validate_profile_name__mutmut_14': x_validate_profile_name__mutmut_14, 
    'x_validate_profile_name__mutmut_15': x_validate_profile_name__mutmut_15, 
    'x_validate_profile_name__mutmut_16': x_validate_profile_name__mutmut_16, 
    'x_validate_profile_name__mutmut_17': x_validate_profile_name__mutmut_17, 
    'x_validate_profile_name__mutmut_18': x_validate_profile_name__mutmut_18, 
    'x_validate_profile_name__mutmut_19': x_validate_profile_name__mutmut_19
}

def validate_profile_name(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_profile_name__mutmut_orig, x_validate_profile_name__mutmut_mutants, args, kwargs)
    return result 

validate_profile_name.__signature__ = _mutmut_signature(x_validate_profile_name__mutmut_orig)
x_validate_profile_name__mutmut_orig.__name__ = 'x_validate_profile_name'


def x_validate_package_name_validator__mutmut_orig(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_1(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_2(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError(None)
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_3(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("XXPackage name cannot be emptyXX")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_4(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_5(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("PACKAGE NAME CANNOT BE EMPTY")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_6(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_7(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace(None, "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_8(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", None).isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_9(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_10(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", ).isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_11(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace(None, "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_12(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", None).replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_13(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_14(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", ).replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_15(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("XX-XX", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_16(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "XX_XX").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_17(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("XX_XX", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_18(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "XXXX").isalnum():
        raise ValueError(f"Invalid package name: {value}")


def x_validate_package_name_validator__mutmut_19(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate package name."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(None)

x_validate_package_name_validator__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_package_name_validator__mutmut_1': x_validate_package_name_validator__mutmut_1, 
    'x_validate_package_name_validator__mutmut_2': x_validate_package_name_validator__mutmut_2, 
    'x_validate_package_name_validator__mutmut_3': x_validate_package_name_validator__mutmut_3, 
    'x_validate_package_name_validator__mutmut_4': x_validate_package_name_validator__mutmut_4, 
    'x_validate_package_name_validator__mutmut_5': x_validate_package_name_validator__mutmut_5, 
    'x_validate_package_name_validator__mutmut_6': x_validate_package_name_validator__mutmut_6, 
    'x_validate_package_name_validator__mutmut_7': x_validate_package_name_validator__mutmut_7, 
    'x_validate_package_name_validator__mutmut_8': x_validate_package_name_validator__mutmut_8, 
    'x_validate_package_name_validator__mutmut_9': x_validate_package_name_validator__mutmut_9, 
    'x_validate_package_name_validator__mutmut_10': x_validate_package_name_validator__mutmut_10, 
    'x_validate_package_name_validator__mutmut_11': x_validate_package_name_validator__mutmut_11, 
    'x_validate_package_name_validator__mutmut_12': x_validate_package_name_validator__mutmut_12, 
    'x_validate_package_name_validator__mutmut_13': x_validate_package_name_validator__mutmut_13, 
    'x_validate_package_name_validator__mutmut_14': x_validate_package_name_validator__mutmut_14, 
    'x_validate_package_name_validator__mutmut_15': x_validate_package_name_validator__mutmut_15, 
    'x_validate_package_name_validator__mutmut_16': x_validate_package_name_validator__mutmut_16, 
    'x_validate_package_name_validator__mutmut_17': x_validate_package_name_validator__mutmut_17, 
    'x_validate_package_name_validator__mutmut_18': x_validate_package_name_validator__mutmut_18, 
    'x_validate_package_name_validator__mutmut_19': x_validate_package_name_validator__mutmut_19
}

def validate_package_name_validator(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_package_name_validator__mutmut_orig, x_validate_package_name_validator__mutmut_mutants, args, kwargs)
    return result 

validate_package_name_validator.__signature__ = _mutmut_signature(x_validate_package_name_validator__mutmut_orig)
x_validate_package_name_validator__mutmut_orig.__name__ = 'x_validate_package_name_validator'


def x_convert_package_name__mutmut_orig(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_1(value: str) -> str:
    """Convert package name to lowercase."""
    if value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_2(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError(None)
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_3(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("XXPackage name cannot be emptyXX")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_4(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_5(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("PACKAGE NAME CANNOT BE EMPTY")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_6(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_7(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace(None, "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_8(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", None).isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_9(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_10(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", ).isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_11(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace(None, "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_12(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", None).replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_13(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_14(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", ).replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_15(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("XX-XX", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_16(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "XX_XX").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_17(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("XX_XX", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_18(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "XXXX").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.lower()


def x_convert_package_name__mutmut_19(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(None)
    return value.lower()


def x_convert_package_name__mutmut_20(value: str) -> str:
    """Convert package name to lowercase."""
    if not value:
        raise ValueError("Package name cannot be empty")
    # Package names should follow Python naming conventions
    if not value.replace("-", "_").replace("_", "").isalnum():
        raise ValueError(f"Invalid package name: {value}")
    return value.upper()

x_convert_package_name__mutmut_mutants : ClassVar[MutantDict] = {
'x_convert_package_name__mutmut_1': x_convert_package_name__mutmut_1, 
    'x_convert_package_name__mutmut_2': x_convert_package_name__mutmut_2, 
    'x_convert_package_name__mutmut_3': x_convert_package_name__mutmut_3, 
    'x_convert_package_name__mutmut_4': x_convert_package_name__mutmut_4, 
    'x_convert_package_name__mutmut_5': x_convert_package_name__mutmut_5, 
    'x_convert_package_name__mutmut_6': x_convert_package_name__mutmut_6, 
    'x_convert_package_name__mutmut_7': x_convert_package_name__mutmut_7, 
    'x_convert_package_name__mutmut_8': x_convert_package_name__mutmut_8, 
    'x_convert_package_name__mutmut_9': x_convert_package_name__mutmut_9, 
    'x_convert_package_name__mutmut_10': x_convert_package_name__mutmut_10, 
    'x_convert_package_name__mutmut_11': x_convert_package_name__mutmut_11, 
    'x_convert_package_name__mutmut_12': x_convert_package_name__mutmut_12, 
    'x_convert_package_name__mutmut_13': x_convert_package_name__mutmut_13, 
    'x_convert_package_name__mutmut_14': x_convert_package_name__mutmut_14, 
    'x_convert_package_name__mutmut_15': x_convert_package_name__mutmut_15, 
    'x_convert_package_name__mutmut_16': x_convert_package_name__mutmut_16, 
    'x_convert_package_name__mutmut_17': x_convert_package_name__mutmut_17, 
    'x_convert_package_name__mutmut_18': x_convert_package_name__mutmut_18, 
    'x_convert_package_name__mutmut_19': x_convert_package_name__mutmut_19, 
    'x_convert_package_name__mutmut_20': x_convert_package_name__mutmut_20
}

def convert_package_name(*args, **kwargs):
    result = _mutmut_trampoline(x_convert_package_name__mutmut_orig, x_convert_package_name__mutmut_mutants, args, kwargs)
    return result 

convert_package_name.__signature__ = _mutmut_signature(x_convert_package_name__mutmut_orig)
x_convert_package_name__mutmut_orig.__name__ = 'x_convert_package_name'


def x_convert_registry_url__mutmut_orig(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_1(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if value.startswith(("http://", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_2(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(None):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_3(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("XXhttp://XX", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_4(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("HTTP://", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_5(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "XXhttps://XX")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_6(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "HTTPS://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("/")


def x_convert_registry_url__mutmut_7(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "https://")):
        raise ValueError(None)
    return value.rstrip("/")


def x_convert_registry_url__mutmut_8(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip(None)


def x_convert_registry_url__mutmut_9(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.lstrip("/")


def x_convert_registry_url__mutmut_10(value: str) -> str:
    """Convert registry URL by removing trailing slash."""
    if not value.startswith(("http://", "https://")):
        raise ValueError(f"Invalid registry URL: {value}")
    return value.rstrip("XX/XX")

x_convert_registry_url__mutmut_mutants : ClassVar[MutantDict] = {
'x_convert_registry_url__mutmut_1': x_convert_registry_url__mutmut_1, 
    'x_convert_registry_url__mutmut_2': x_convert_registry_url__mutmut_2, 
    'x_convert_registry_url__mutmut_3': x_convert_registry_url__mutmut_3, 
    'x_convert_registry_url__mutmut_4': x_convert_registry_url__mutmut_4, 
    'x_convert_registry_url__mutmut_5': x_convert_registry_url__mutmut_5, 
    'x_convert_registry_url__mutmut_6': x_convert_registry_url__mutmut_6, 
    'x_convert_registry_url__mutmut_7': x_convert_registry_url__mutmut_7, 
    'x_convert_registry_url__mutmut_8': x_convert_registry_url__mutmut_8, 
    'x_convert_registry_url__mutmut_9': x_convert_registry_url__mutmut_9, 
    'x_convert_registry_url__mutmut_10': x_convert_registry_url__mutmut_10
}

def convert_registry_url(*args, **kwargs):
    result = _mutmut_trampoline(x_convert_registry_url__mutmut_orig, x_convert_registry_url__mutmut_mutants, args, kwargs)
    return result 

convert_registry_url.__signature__ = _mutmut_signature(x_convert_registry_url__mutmut_orig)
x_convert_registry_url__mutmut_orig.__name__ = 'x_convert_registry_url'


def x_validate_timeout__mutmut_orig(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_1(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value < 0:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_2(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 1:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_3(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError(None)
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_4(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("XXTimeout must be positiveXX")
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_5(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("timeout must be positive")
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_6(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("TIMEOUT MUST BE POSITIVE")
    if value > 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_7(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value >= 300:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_8(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value > 301:
        raise ValueError("Timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_9(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError(None)


def x_validate_timeout__mutmut_10(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError("XXTimeout cannot exceed 5 minutesXX")


def x_validate_timeout__mutmut_11(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError("timeout cannot exceed 5 minutes")


def x_validate_timeout__mutmut_12(instance: Any, attribute: Attribute[Any], value: int) -> None:
    """Validate timeout value."""
    if value <= 0:
        raise ValueError("Timeout must be positive")
    if value > 300:
        raise ValueError("TIMEOUT CANNOT EXCEED 5 MINUTES")

x_validate_timeout__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_timeout__mutmut_1': x_validate_timeout__mutmut_1, 
    'x_validate_timeout__mutmut_2': x_validate_timeout__mutmut_2, 
    'x_validate_timeout__mutmut_3': x_validate_timeout__mutmut_3, 
    'x_validate_timeout__mutmut_4': x_validate_timeout__mutmut_4, 
    'x_validate_timeout__mutmut_5': x_validate_timeout__mutmut_5, 
    'x_validate_timeout__mutmut_6': x_validate_timeout__mutmut_6, 
    'x_validate_timeout__mutmut_7': x_validate_timeout__mutmut_7, 
    'x_validate_timeout__mutmut_8': x_validate_timeout__mutmut_8, 
    'x_validate_timeout__mutmut_9': x_validate_timeout__mutmut_9, 
    'x_validate_timeout__mutmut_10': x_validate_timeout__mutmut_10, 
    'x_validate_timeout__mutmut_11': x_validate_timeout__mutmut_11, 
    'x_validate_timeout__mutmut_12': x_validate_timeout__mutmut_12
}

def validate_timeout(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_timeout__mutmut_orig, x_validate_timeout__mutmut_mutants, args, kwargs)
    return result 

validate_timeout.__signature__ = _mutmut_signature(x_validate_timeout__mutmut_orig)
x_validate_timeout__mutmut_orig.__name__ = 'x_validate_timeout'


def x_validate_volume_mapping__mutmut_orig(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_1(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_2(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return True

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_3(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = None
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_4(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(None)
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_5(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split("XX:XX")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_6(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 and len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_7(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) <= 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_8(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 3 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_9(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) >= 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_10(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 4:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_11(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return True

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_12(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] and not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_13(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_14(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[1] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_15(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_16(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[2]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_17(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return True

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_18(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) != 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_19(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 4:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_20(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = None
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_21(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[3]
        if mode not in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_22(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode in ["ro", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_23(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["XXroXX", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_24(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["RO", "rw"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_25(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "XXrwXX"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_26(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "RW"]:
            return False

    return True


def x_validate_volume_mapping__mutmut_27(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return True

    return True


def x_validate_volume_mapping__mutmut_28(mapping: str) -> bool:
    """Validate a single volume mapping string."""
    if not mapping:
        return False

    parts = mapping.split(":")
    if len(parts) < 2 or len(parts) > 3:
        return False

    # Check host and container paths are not empty
    if not parts[0] or not parts[1]:
        return False

    # If mode is specified, check it's valid
    if len(parts) == 3:
        mode = parts[2]
        if mode not in ["ro", "rw"]:
            return False

    return False

x_validate_volume_mapping__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_volume_mapping__mutmut_1': x_validate_volume_mapping__mutmut_1, 
    'x_validate_volume_mapping__mutmut_2': x_validate_volume_mapping__mutmut_2, 
    'x_validate_volume_mapping__mutmut_3': x_validate_volume_mapping__mutmut_3, 
    'x_validate_volume_mapping__mutmut_4': x_validate_volume_mapping__mutmut_4, 
    'x_validate_volume_mapping__mutmut_5': x_validate_volume_mapping__mutmut_5, 
    'x_validate_volume_mapping__mutmut_6': x_validate_volume_mapping__mutmut_6, 
    'x_validate_volume_mapping__mutmut_7': x_validate_volume_mapping__mutmut_7, 
    'x_validate_volume_mapping__mutmut_8': x_validate_volume_mapping__mutmut_8, 
    'x_validate_volume_mapping__mutmut_9': x_validate_volume_mapping__mutmut_9, 
    'x_validate_volume_mapping__mutmut_10': x_validate_volume_mapping__mutmut_10, 
    'x_validate_volume_mapping__mutmut_11': x_validate_volume_mapping__mutmut_11, 
    'x_validate_volume_mapping__mutmut_12': x_validate_volume_mapping__mutmut_12, 
    'x_validate_volume_mapping__mutmut_13': x_validate_volume_mapping__mutmut_13, 
    'x_validate_volume_mapping__mutmut_14': x_validate_volume_mapping__mutmut_14, 
    'x_validate_volume_mapping__mutmut_15': x_validate_volume_mapping__mutmut_15, 
    'x_validate_volume_mapping__mutmut_16': x_validate_volume_mapping__mutmut_16, 
    'x_validate_volume_mapping__mutmut_17': x_validate_volume_mapping__mutmut_17, 
    'x_validate_volume_mapping__mutmut_18': x_validate_volume_mapping__mutmut_18, 
    'x_validate_volume_mapping__mutmut_19': x_validate_volume_mapping__mutmut_19, 
    'x_validate_volume_mapping__mutmut_20': x_validate_volume_mapping__mutmut_20, 
    'x_validate_volume_mapping__mutmut_21': x_validate_volume_mapping__mutmut_21, 
    'x_validate_volume_mapping__mutmut_22': x_validate_volume_mapping__mutmut_22, 
    'x_validate_volume_mapping__mutmut_23': x_validate_volume_mapping__mutmut_23, 
    'x_validate_volume_mapping__mutmut_24': x_validate_volume_mapping__mutmut_24, 
    'x_validate_volume_mapping__mutmut_25': x_validate_volume_mapping__mutmut_25, 
    'x_validate_volume_mapping__mutmut_26': x_validate_volume_mapping__mutmut_26, 
    'x_validate_volume_mapping__mutmut_27': x_validate_volume_mapping__mutmut_27, 
    'x_validate_volume_mapping__mutmut_28': x_validate_volume_mapping__mutmut_28
}

def validate_volume_mapping(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_volume_mapping__mutmut_orig, x_validate_volume_mapping__mutmut_mutants, args, kwargs)
    return result 

validate_volume_mapping.__signature__ = _mutmut_signature(x_validate_volume_mapping__mutmut_orig)
x_validate_volume_mapping__mutmut_orig.__name__ = 'x_validate_volume_mapping'


def x_validate_volume_mappings__mutmut_orig(
    instance: Any,
    attribute: Attribute[Any],
    value: dict[str, str],
) -> None:
    """Validate volume mappings dictionary."""
    for name, mapping in value.items():
        if not validate_volume_mapping(mapping):
            raise ValueError(f"Invalid volume mapping for '{name}': {mapping}")


def x_validate_volume_mappings__mutmut_1(
    instance: Any,
    attribute: Attribute[Any],
    value: dict[str, str],
) -> None:
    """Validate volume mappings dictionary."""
    for name, mapping in value.items():
        if validate_volume_mapping(mapping):
            raise ValueError(f"Invalid volume mapping for '{name}': {mapping}")


def x_validate_volume_mappings__mutmut_2(
    instance: Any,
    attribute: Attribute[Any],
    value: dict[str, str],
) -> None:
    """Validate volume mappings dictionary."""
    for name, mapping in value.items():
        if not validate_volume_mapping(None):
            raise ValueError(f"Invalid volume mapping for '{name}': {mapping}")


def x_validate_volume_mappings__mutmut_3(
    instance: Any,
    attribute: Attribute[Any],
    value: dict[str, str],
) -> None:
    """Validate volume mappings dictionary."""
    for name, mapping in value.items():
        if not validate_volume_mapping(mapping):
            raise ValueError(None)

x_validate_volume_mappings__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_volume_mappings__mutmut_1': x_validate_volume_mappings__mutmut_1, 
    'x_validate_volume_mappings__mutmut_2': x_validate_volume_mappings__mutmut_2, 
    'x_validate_volume_mappings__mutmut_3': x_validate_volume_mappings__mutmut_3
}

def validate_volume_mappings(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_volume_mappings__mutmut_orig, x_validate_volume_mappings__mutmut_mutants, args, kwargs)
    return result 

validate_volume_mappings.__signature__ = _mutmut_signature(x_validate_volume_mappings__mutmut_orig)
x_validate_volume_mappings__mutmut_orig.__name__ = 'x_validate_volume_mappings'


def x_validate_project_name__mutmut_orig(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate project name."""
    if not value:
        raise ValueError("Project name cannot be empty")


def x_validate_project_name__mutmut_1(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate project name."""
    if value:
        raise ValueError("Project name cannot be empty")


def x_validate_project_name__mutmut_2(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate project name."""
    if not value:
        raise ValueError(None)


def x_validate_project_name__mutmut_3(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate project name."""
    if not value:
        raise ValueError("XXProject name cannot be emptyXX")


def x_validate_project_name__mutmut_4(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate project name."""
    if not value:
        raise ValueError("project name cannot be empty")


def x_validate_project_name__mutmut_5(instance: Any, attribute: Attribute[Any], value: str) -> None:
    """Validate project name."""
    if not value:
        raise ValueError("PROJECT NAME CANNOT BE EMPTY")

x_validate_project_name__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_project_name__mutmut_1': x_validate_project_name__mutmut_1, 
    'x_validate_project_name__mutmut_2': x_validate_project_name__mutmut_2, 
    'x_validate_project_name__mutmut_3': x_validate_project_name__mutmut_3, 
    'x_validate_project_name__mutmut_4': x_validate_project_name__mutmut_4, 
    'x_validate_project_name__mutmut_5': x_validate_project_name__mutmut_5
}

def validate_project_name(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_project_name__mutmut_orig, x_validate_project_name__mutmut_mutants, args, kwargs)
    return result 

validate_project_name.__signature__ = _mutmut_signature(x_validate_project_name__mutmut_orig)
x_validate_project_name__mutmut_orig.__name__ = 'x_validate_project_name'


def x_convert_log_level__mutmut_orig(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_1(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = None
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_2(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["XXDEBUGXX", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_3(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["debug", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_4(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "XXINFOXX", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_5(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "info", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_6(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "XXWARNINGXX", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_7(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "warning", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_8(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "XXERRORXX", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_9(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "error", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_10(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "XXCRITICALXX"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_11(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "critical"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_12(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = None
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_13(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = value.lower()
    if value not in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_14(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value in valid_levels:
        raise ValueError(f"Invalid log level: {value}")
    return value


def x_convert_log_level__mutmut_15(value: str) -> str:
    """Convert log level to uppercase and validate."""
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    value = value.upper()
    if value not in valid_levels:
        raise ValueError(None)
    return value

x_convert_log_level__mutmut_mutants : ClassVar[MutantDict] = {
'x_convert_log_level__mutmut_1': x_convert_log_level__mutmut_1, 
    'x_convert_log_level__mutmut_2': x_convert_log_level__mutmut_2, 
    'x_convert_log_level__mutmut_3': x_convert_log_level__mutmut_3, 
    'x_convert_log_level__mutmut_4': x_convert_log_level__mutmut_4, 
    'x_convert_log_level__mutmut_5': x_convert_log_level__mutmut_5, 
    'x_convert_log_level__mutmut_6': x_convert_log_level__mutmut_6, 
    'x_convert_log_level__mutmut_7': x_convert_log_level__mutmut_7, 
    'x_convert_log_level__mutmut_8': x_convert_log_level__mutmut_8, 
    'x_convert_log_level__mutmut_9': x_convert_log_level__mutmut_9, 
    'x_convert_log_level__mutmut_10': x_convert_log_level__mutmut_10, 
    'x_convert_log_level__mutmut_11': x_convert_log_level__mutmut_11, 
    'x_convert_log_level__mutmut_12': x_convert_log_level__mutmut_12, 
    'x_convert_log_level__mutmut_13': x_convert_log_level__mutmut_13, 
    'x_convert_log_level__mutmut_14': x_convert_log_level__mutmut_14, 
    'x_convert_log_level__mutmut_15': x_convert_log_level__mutmut_15
}

def convert_log_level(*args, **kwargs):
    result = _mutmut_trampoline(x_convert_log_level__mutmut_orig, x_convert_log_level__mutmut_mutants, args, kwargs)
    return result 

convert_log_level.__signature__ = _mutmut_signature(x_convert_log_level__mutmut_orig)
x_convert_log_level__mutmut_orig.__name__ = 'x_convert_log_level'


@define
class GitignoreConfig:
    """Configuration for gitignore generation."""

    templates: list[str] = field(factory=list, validator=validators.instance_of(list))
    templates_path: str | None = field(
        default=None, validator=validators.optional(validators.instance_of(str))
    )
    auto_detect: bool = field(default=DEFAULT_TOOL_AUTO_DETECT, validator=validators.instance_of(bool))
    custom_rules: list[str] = field(factory=list, validator=validators.instance_of(list))
    exclude_patterns: list[str] = field(factory=list, validator=validators.instance_of(list))


@define
class ToolConfig:
    """Configuration for a specific tool."""

    version: str = field(validator=[validators.instance_of(str), validate_version])
    enabled: bool = field(default=DEFAULT_TOOL_ENABLED, validator=validators.instance_of(bool))
    source_url: str | None = field(default=None, validator=validators.optional(validators.instance_of(str)))
    install_path: str | None = field(default=None, validator=validators.optional(validators.instance_of(str)))
    environment: dict[str, str] = field(factory=dict, validator=validators.instance_of(dict))


@define
class ContainerConfig:
    """Configuration for container operations."""

    enabled: bool = field(default=DEFAULT_CONTAINER_ENABLED, validator=validators.instance_of(bool))
    base_image: str = field(default=DEFAULT_CONTAINER_BASE_IMAGE, validator=validators.instance_of(str))
    python_version: str = field(
        default=DEFAULT_PYTHON_VERSION, validator=[validators.instance_of(str), validate_python_version]
    )
    additional_packages: list[str] = field(factory=list, validator=validators.instance_of(list))
    environment: dict[str, str] = field(factory=dict, validator=validators.instance_of(dict))
    volumes: list[str] = field(factory=list, validator=validators.instance_of(list))
    ports: list[str] = field(factory=list, validator=validators.instance_of(list))

    # New storage-related fields
    storage_path: str = field(default=DEFAULT_CONTAINER_STORAGE_PATH, validator=validators.instance_of(str))
    persistent_volumes: list[str] = field(
        factory=lambda: ["workspace", "cache", "config"], validator=validators.instance_of(list)
    )
    volume_mappings: dict[str, str] = field(
        factory=dict, validator=[validators.instance_of(dict), validate_volume_mappings]
    )

    def to_dict(self) -> dict[str, Any]:
        """Convert ContainerConfig to dictionary."""
        return cattrs.unstructure(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContainerConfig:
        """Create ContainerConfig from dictionary."""
        return cattrs.structure(data, cls)


@define
class ProfileConfig:
    """Configuration for a workenv profile."""

    name: str = field(validator=[validators.instance_of(str), validate_profile_name])
    description: str = field(default="", validator=validators.instance_of(str))
    tools: dict[str, ToolConfig] = field(factory=dict, validator=validators.instance_of(dict))
    container: ContainerConfig | None = field(
        default=None,
        validator=validators.optional(validators.instance_of(ContainerConfig)),
    )
    environment: dict[str, str] = field(factory=dict, validator=validators.instance_of(dict))
    scripts: dict[str, str] = field(factory=dict, validator=validators.instance_of(dict))

    def model_dump(self) -> dict[str, Any]:
        """Convert to dictionary (compatibility method)."""
        return cattrs.unstructure(self)


@define
class PackageConfig:
    """Configuration for package operations."""

    name: str = field(validator=validators.instance_of(str), converter=convert_package_name)
    version: str = field(validator=validators.instance_of(str))
    entry_point: str = field(validator=validators.instance_of(str))
    author: str = field(default="", validator=validators.instance_of(str))
    description: str = field(default="", validator=validators.instance_of(str))
    license: str = field(default=DEFAULT_PACKAGE_LICENSE, validator=validators.instance_of(str))
    dependencies: list[str] = field(factory=list, validator=validators.instance_of(list))
    metadata: dict[str, Any] = field(factory=dict, validator=validators.instance_of(dict))


@define
class RegistryConfig:
    """Configuration for package registry."""

    url: str = field(default=DEFAULT_REGISTRY_WRKNV_URL, converter=convert_registry_url)
    username: str | None = field(default=None, validator=validators.optional(validators.instance_of(str)))
    token: str | None = field(default=None, validator=validators.optional(validators.instance_of(str)))
    verify_ssl: bool = field(default=DEFAULT_REGISTRY_VERIFY_SSL, validator=validators.instance_of(bool))
    timeout: int = field(
        default=DEFAULT_REGISTRY_TIMEOUT, validator=[validators.instance_of(int), validate_timeout]
    )


@define
class WorkenvSchema:
    """Schema for wrknv configuration validation (use wrknv.config.WorkenvConfig for runtime)."""

    project_name: str = field(validator=[validators.instance_of(str), validate_project_name])
    version: str = field(default=DEFAULT_VERSION, validator=validators.instance_of(str))
    description: str = field(default="", validator=validators.instance_of(str))

    # Tool configurations
    tools: dict[str, ToolConfig] = field(factory=dict, validator=validators.instance_of(dict))

    # Container configuration
    container: ContainerConfig | None = field(
        default=None,
        validator=validators.optional(validators.instance_of(ContainerConfig)),
    )

    # Package configuration
    package: PackageConfig | None = field(
        default=None,
        validator=validators.optional(validators.instance_of(PackageConfig)),
    )

    # Registry configuration
    registry: RegistryConfig | None = field(
        default=None,
        validator=validators.optional(validators.instance_of(RegistryConfig)),
    )

    # Profiles
    profiles: dict[str, ProfileConfig] = field(factory=dict, validator=validators.instance_of(dict))

    # Global settings
    install_dir: str = field(default=DEFAULT_WORKENV_INSTALL_DIR, validator=validators.instance_of(str))
    cache_dir: str = field(default=DEFAULT_WORKENV_CACHE_DIR, validator=validators.instance_of(str))
    log_level: str = field(default=DEFAULT_LOG_LEVEL, converter=convert_log_level)
    telemetry_enabled: bool = field(default=DEFAULT_TELEMETRY_ENABLED, validator=validators.instance_of(bool))
    auto_update: bool = field(default=DEFAULT_AUTO_UPDATE, validator=validators.instance_of(bool))

    # Task execution settings
    task_runner_prefix: str | None = field(
        default=None, validator=validators.optional(validators.instance_of(str))
    )
    task_auto_detect: bool = field(default=True, validator=validators.instance_of(bool))

    # Environment variables
    environment: dict[str, str] = field(factory=dict, validator=validators.instance_of(dict))

    # Custom scripts
    scripts: dict[str, str] = field(factory=dict, validator=validators.instance_of(dict))

    # Gitignore configuration
    gitignore: GitignoreConfig | None = field(
        default=None,
        validator=validators.optional(validators.instance_of(GitignoreConfig)),
    )

    def __attrs_post_init__(self) -> None:
        """Post-initialization processing."""
        # Expand user home directory
        self.install_dir = str(pathlib.Path(self.install_dir).expanduser())
        self.cache_dir = str(pathlib.Path(self.cache_dir).expanduser())

    def get_tool_config(self, tool_name: str) -> ToolConfig | None:
        """Get configuration for a specific tool."""
        return self.tools.get(tool_name)

    def get_profile(self, profile_name: str) -> ProfileConfig | None:
        """Get a specific profile configuration."""
        return self.profiles.get(profile_name)

    def merge_with_profile(self, profile_name: str) -> WorkenvSchema:
        """Create a new config merged with a profile."""
        profile = self.get_profile(profile_name)
        if not profile:
            return self

        # Create a copy of the current config
        merged_dict = cattrs.unstructure(self)

        # Merge tool configurations
        for tool_name, tool_config in profile.tools.items():
            merged_dict["tools"][tool_name] = cattrs.unstructure(tool_config)

        # Merge container config if present
        if profile.container:
            merged_dict["container"] = cattrs.unstructure(profile.container)

        # Merge environment variables
        merged_dict["environment"].update(profile.environment)

        # Merge scripts
        merged_dict["scripts"].update(profile.scripts)

        # Create new instance from merged dict
        return cattrs.structure(merged_dict, WorkenvSchema)

    def model_dump(self, exclude_none: bool = False) -> dict[str, Any]:
        """Convert to dictionary (compatibility method)."""
        data = cattrs.unstructure(self)
        if exclude_none:
            data = remove_none_values(data)
        return data


def x_remove_none_values__mutmut_orig(data: Any) -> Any:
    """Recursively remove None values from dictionary."""
    if isinstance(data, dict):
        return {k: remove_none_values(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [remove_none_values(item) for item in data]
    return data


def x_remove_none_values__mutmut_1(data: Any) -> Any:
    """Recursively remove None values from dictionary."""
    if isinstance(data, dict):
        return {k: remove_none_values(None) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [remove_none_values(item) for item in data]
    return data


def x_remove_none_values__mutmut_2(data: Any) -> Any:
    """Recursively remove None values from dictionary."""
    if isinstance(data, dict):
        return {k: remove_none_values(v) for k, v in data.items() if v is None}
    if isinstance(data, list):
        return [remove_none_values(item) for item in data]
    return data


def x_remove_none_values__mutmut_3(data: Any) -> Any:
    """Recursively remove None values from dictionary."""
    if isinstance(data, dict):
        return {k: remove_none_values(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [remove_none_values(None) for item in data]
    return data

x_remove_none_values__mutmut_mutants : ClassVar[MutantDict] = {
'x_remove_none_values__mutmut_1': x_remove_none_values__mutmut_1, 
    'x_remove_none_values__mutmut_2': x_remove_none_values__mutmut_2, 
    'x_remove_none_values__mutmut_3': x_remove_none_values__mutmut_3
}

def remove_none_values(*args, **kwargs):
    result = _mutmut_trampoline(x_remove_none_values__mutmut_orig, x_remove_none_values__mutmut_mutants, args, kwargs)
    return result 

remove_none_values.__signature__ = _mutmut_signature(x_remove_none_values__mutmut_orig)
x_remove_none_values__mutmut_orig.__name__ = 'x_remove_none_values'


def x_validate_config_dict__mutmut_orig(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_1(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = None

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_2(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = None
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_3(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(None, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_4(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, None)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_5(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_6(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, )
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_7(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return False, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_8(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") or e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_9(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(None, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_10(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, None) and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_11(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr("__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_12(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, ) and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_13(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "XX__cause__XX") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_14(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__CAUSE__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_15(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(None)
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_16(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(None))
        else:
            errors.append(str(e))

        return False, errors


def x_validate_config_dict__mutmut_17(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(None)

        return False, errors


def x_validate_config_dict__mutmut_18(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(None))

        return False, errors


def x_validate_config_dict__mutmut_19(config_dict: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate a configuration dictionary.

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        converter = cattrs.Converter()
        converter.structure(config_dict, WorkenvSchema)
        return True, []
    except Exception as e:
        if hasattr(e, "__cause__") and e.__cause__:
            # Extract validation errors from attrs/cattrs
            errors.append(str(e.__cause__))
        else:
            errors.append(str(e))

        return True, errors

x_validate_config_dict__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_config_dict__mutmut_1': x_validate_config_dict__mutmut_1, 
    'x_validate_config_dict__mutmut_2': x_validate_config_dict__mutmut_2, 
    'x_validate_config_dict__mutmut_3': x_validate_config_dict__mutmut_3, 
    'x_validate_config_dict__mutmut_4': x_validate_config_dict__mutmut_4, 
    'x_validate_config_dict__mutmut_5': x_validate_config_dict__mutmut_5, 
    'x_validate_config_dict__mutmut_6': x_validate_config_dict__mutmut_6, 
    'x_validate_config_dict__mutmut_7': x_validate_config_dict__mutmut_7, 
    'x_validate_config_dict__mutmut_8': x_validate_config_dict__mutmut_8, 
    'x_validate_config_dict__mutmut_9': x_validate_config_dict__mutmut_9, 
    'x_validate_config_dict__mutmut_10': x_validate_config_dict__mutmut_10, 
    'x_validate_config_dict__mutmut_11': x_validate_config_dict__mutmut_11, 
    'x_validate_config_dict__mutmut_12': x_validate_config_dict__mutmut_12, 
    'x_validate_config_dict__mutmut_13': x_validate_config_dict__mutmut_13, 
    'x_validate_config_dict__mutmut_14': x_validate_config_dict__mutmut_14, 
    'x_validate_config_dict__mutmut_15': x_validate_config_dict__mutmut_15, 
    'x_validate_config_dict__mutmut_16': x_validate_config_dict__mutmut_16, 
    'x_validate_config_dict__mutmut_17': x_validate_config_dict__mutmut_17, 
    'x_validate_config_dict__mutmut_18': x_validate_config_dict__mutmut_18, 
    'x_validate_config_dict__mutmut_19': x_validate_config_dict__mutmut_19
}

def validate_config_dict(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_config_dict__mutmut_orig, x_validate_config_dict__mutmut_mutants, args, kwargs)
    return result 

validate_config_dict.__signature__ = _mutmut_signature(x_validate_config_dict__mutmut_orig)
x_validate_config_dict__mutmut_orig.__name__ = 'x_validate_config_dict'


def x_load_config_from_dict__mutmut_orig(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_1(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = None
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_2(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(None)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_3(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_4(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = None
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_5(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" - "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_6(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "XXConfiguration validation failed:\nXX" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_7(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_8(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "CONFIGURATION VALIDATION FAILED:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_9(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(None)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_10(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "XX\nXX".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_11(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(None)

    converter = cattrs.Converter()
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_12(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = None
    return converter.structure(config_dict, WorkenvSchema)


def x_load_config_from_dict__mutmut_13(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(None, WorkenvSchema)


def x_load_config_from_dict__mutmut_14(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, None)


def x_load_config_from_dict__mutmut_15(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(WorkenvSchema)


def x_load_config_from_dict__mutmut_16(config_dict: dict[str, Any]) -> WorkenvSchema:
    """
    Load configuration from a dictionary with validation.

    Raises:
        ValueError: If configuration is invalid
    """
    is_valid, errors = validate_config_dict(config_dict)
    if not is_valid:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    converter = cattrs.Converter()
    return converter.structure(config_dict, )

x_load_config_from_dict__mutmut_mutants : ClassVar[MutantDict] = {
'x_load_config_from_dict__mutmut_1': x_load_config_from_dict__mutmut_1, 
    'x_load_config_from_dict__mutmut_2': x_load_config_from_dict__mutmut_2, 
    'x_load_config_from_dict__mutmut_3': x_load_config_from_dict__mutmut_3, 
    'x_load_config_from_dict__mutmut_4': x_load_config_from_dict__mutmut_4, 
    'x_load_config_from_dict__mutmut_5': x_load_config_from_dict__mutmut_5, 
    'x_load_config_from_dict__mutmut_6': x_load_config_from_dict__mutmut_6, 
    'x_load_config_from_dict__mutmut_7': x_load_config_from_dict__mutmut_7, 
    'x_load_config_from_dict__mutmut_8': x_load_config_from_dict__mutmut_8, 
    'x_load_config_from_dict__mutmut_9': x_load_config_from_dict__mutmut_9, 
    'x_load_config_from_dict__mutmut_10': x_load_config_from_dict__mutmut_10, 
    'x_load_config_from_dict__mutmut_11': x_load_config_from_dict__mutmut_11, 
    'x_load_config_from_dict__mutmut_12': x_load_config_from_dict__mutmut_12, 
    'x_load_config_from_dict__mutmut_13': x_load_config_from_dict__mutmut_13, 
    'x_load_config_from_dict__mutmut_14': x_load_config_from_dict__mutmut_14, 
    'x_load_config_from_dict__mutmut_15': x_load_config_from_dict__mutmut_15, 
    'x_load_config_from_dict__mutmut_16': x_load_config_from_dict__mutmut_16
}

def load_config_from_dict(*args, **kwargs):
    result = _mutmut_trampoline(x_load_config_from_dict__mutmut_orig, x_load_config_from_dict__mutmut_mutants, args, kwargs)
    return result 

load_config_from_dict.__signature__ = _mutmut_signature(x_load_config_from_dict__mutmut_orig)
x_load_config_from_dict__mutmut_orig.__name__ = 'x_load_config_from_dict'


def x_get_default_config__mutmut_orig(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_1(project_name: str = "XXmy-projectXX") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_2(project_name: str = "MY-PROJECT") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_3(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=None,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_4(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools=None,
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_5(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=None,
    )


def x_get_default_config__mutmut_6(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_7(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_8(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        )


def x_get_default_config__mutmut_9(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "XXterraformXX": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_10(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "TERRAFORM": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_11(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version=None),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_12(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="XX1.5.0XX"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_13(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "XXtofuXX": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_14(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "TOFU": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_15(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version=None, enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_16(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=None),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_17(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_18(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", ),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_19(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="XX1.6.0XX", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_20(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=True),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_21(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "XXgoXX": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_22(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "GO": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_23(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version=None),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_24(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="XX1.21.0XX"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_25(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "XXuvXX": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_26(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "UV": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_27(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version=None),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_28(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="XX0.4.0XX"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_29(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=None,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_30(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image=None,
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_31(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version=None,
        ),
    )


def x_get_default_config__mutmut_32(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_33(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_34(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            ),
    )


def x_get_default_config__mutmut_35(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=True,
            base_image="ubuntu:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_36(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="XXubuntu:22.04XX",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_37(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="UBUNTU:22.04",
            python_version="3.11",
        ),
    )


def x_get_default_config__mutmut_38(project_name: str = "my-project") -> WorkenvSchema:
    """Get a default configuration schema."""
    return WorkenvSchema(
        project_name=project_name,
        tools={
            "terraform": ToolConfig(version="1.5.0"),
            "tofu": ToolConfig(version="1.6.0", enabled=False),
            "go": ToolConfig(version="1.21.0"),
            "uv": ToolConfig(version="0.4.0"),
        },
        container=ContainerConfig(
            enabled=False,
            base_image="ubuntu:22.04",
            python_version="XX3.11XX",
        ),
    )

x_get_default_config__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_default_config__mutmut_1': x_get_default_config__mutmut_1, 
    'x_get_default_config__mutmut_2': x_get_default_config__mutmut_2, 
    'x_get_default_config__mutmut_3': x_get_default_config__mutmut_3, 
    'x_get_default_config__mutmut_4': x_get_default_config__mutmut_4, 
    'x_get_default_config__mutmut_5': x_get_default_config__mutmut_5, 
    'x_get_default_config__mutmut_6': x_get_default_config__mutmut_6, 
    'x_get_default_config__mutmut_7': x_get_default_config__mutmut_7, 
    'x_get_default_config__mutmut_8': x_get_default_config__mutmut_8, 
    'x_get_default_config__mutmut_9': x_get_default_config__mutmut_9, 
    'x_get_default_config__mutmut_10': x_get_default_config__mutmut_10, 
    'x_get_default_config__mutmut_11': x_get_default_config__mutmut_11, 
    'x_get_default_config__mutmut_12': x_get_default_config__mutmut_12, 
    'x_get_default_config__mutmut_13': x_get_default_config__mutmut_13, 
    'x_get_default_config__mutmut_14': x_get_default_config__mutmut_14, 
    'x_get_default_config__mutmut_15': x_get_default_config__mutmut_15, 
    'x_get_default_config__mutmut_16': x_get_default_config__mutmut_16, 
    'x_get_default_config__mutmut_17': x_get_default_config__mutmut_17, 
    'x_get_default_config__mutmut_18': x_get_default_config__mutmut_18, 
    'x_get_default_config__mutmut_19': x_get_default_config__mutmut_19, 
    'x_get_default_config__mutmut_20': x_get_default_config__mutmut_20, 
    'x_get_default_config__mutmut_21': x_get_default_config__mutmut_21, 
    'x_get_default_config__mutmut_22': x_get_default_config__mutmut_22, 
    'x_get_default_config__mutmut_23': x_get_default_config__mutmut_23, 
    'x_get_default_config__mutmut_24': x_get_default_config__mutmut_24, 
    'x_get_default_config__mutmut_25': x_get_default_config__mutmut_25, 
    'x_get_default_config__mutmut_26': x_get_default_config__mutmut_26, 
    'x_get_default_config__mutmut_27': x_get_default_config__mutmut_27, 
    'x_get_default_config__mutmut_28': x_get_default_config__mutmut_28, 
    'x_get_default_config__mutmut_29': x_get_default_config__mutmut_29, 
    'x_get_default_config__mutmut_30': x_get_default_config__mutmut_30, 
    'x_get_default_config__mutmut_31': x_get_default_config__mutmut_31, 
    'x_get_default_config__mutmut_32': x_get_default_config__mutmut_32, 
    'x_get_default_config__mutmut_33': x_get_default_config__mutmut_33, 
    'x_get_default_config__mutmut_34': x_get_default_config__mutmut_34, 
    'x_get_default_config__mutmut_35': x_get_default_config__mutmut_35, 
    'x_get_default_config__mutmut_36': x_get_default_config__mutmut_36, 
    'x_get_default_config__mutmut_37': x_get_default_config__mutmut_37, 
    'x_get_default_config__mutmut_38': x_get_default_config__mutmut_38
}

def get_default_config(*args, **kwargs):
    result = _mutmut_trampoline(x_get_default_config__mutmut_orig, x_get_default_config__mutmut_mutants, args, kwargs)
    return result 

get_default_config.__signature__ = _mutmut_signature(x_get_default_config__mutmut_orig)
x_get_default_config__mutmut_orig.__name__ = 'x_get_default_config'


def x_config_to_toml__mutmut_orig(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_1(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = None

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_2(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=None)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_3(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=False)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_4(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(None) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_5(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v or (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_6(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) and v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_7(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_8(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(None) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_9(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = None

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_10(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(None)

    # Convert to TOML
    return toml_dumps(config_dict)


def x_config_to_toml__mutmut_11(config: WorkenvConfig) -> str:
    """Convert configuration to TOML format."""
    from provide.foundation.file.formats import toml_dumps

    # Convert to dictionary
    config_dict = config.model_dump(exclude_none=True)

    # Remove empty collections
    def remove_empty(data: Any) -> Any:
        if isinstance(data, dict):
            return {
                k: remove_empty(v) for k, v in data.items() if v and (not isinstance(v, (dict, list)) or v)
            }
        if isinstance(data, list):
            return [remove_empty(item) for item in data if item]
        return data

    config_dict = remove_empty(config_dict)

    # Convert to TOML
    return toml_dumps(None)

x_config_to_toml__mutmut_mutants : ClassVar[MutantDict] = {
'x_config_to_toml__mutmut_1': x_config_to_toml__mutmut_1, 
    'x_config_to_toml__mutmut_2': x_config_to_toml__mutmut_2, 
    'x_config_to_toml__mutmut_3': x_config_to_toml__mutmut_3, 
    'x_config_to_toml__mutmut_4': x_config_to_toml__mutmut_4, 
    'x_config_to_toml__mutmut_5': x_config_to_toml__mutmut_5, 
    'x_config_to_toml__mutmut_6': x_config_to_toml__mutmut_6, 
    'x_config_to_toml__mutmut_7': x_config_to_toml__mutmut_7, 
    'x_config_to_toml__mutmut_8': x_config_to_toml__mutmut_8, 
    'x_config_to_toml__mutmut_9': x_config_to_toml__mutmut_9, 
    'x_config_to_toml__mutmut_10': x_config_to_toml__mutmut_10, 
    'x_config_to_toml__mutmut_11': x_config_to_toml__mutmut_11
}

def config_to_toml(*args, **kwargs):
    result = _mutmut_trampoline(x_config_to_toml__mutmut_orig, x_config_to_toml__mutmut_mutants, args, kwargs)
    return result 

config_to_toml.__signature__ = _mutmut_signature(x_config_to_toml__mutmut_orig)
x_config_to_toml__mutmut_orig.__name__ = 'x_config_to_toml'


# 🧰🌍🔚
