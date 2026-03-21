#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#


from pathlib import Path
from typing import Any

"""Centralized default values for wrknv configuration.
All defaults are defined here instead of inline in field definitions.
"""

# =================================
# Command Operation defaults
# =================================
DEFAULT_TIMEOUT = 10
DEFAULT_SHORT_TIMEOUT = 5
DEFAULT_DRY_RUN = False
DEFAULT_FORCE = False
DEFAULT_VERIFY = True
DEFAULT_ACTIVATE = True
DEFAULT_AUTO_DISCOVER = True

# =================================
# Version and Release defaults
# =================================
DEFAULT_VERSION = "1.0.0"
DEFAULT_WORKSPACE_VERSION = "1.0"

# =================================
# Workspace Configuration defaults
# =================================
DEFAULT_SYNC_STRATEGY = "manual"  # "manual", "auto", "check"

# =================================
# Container defaults
# =================================
DEFAULT_CONTAINER_RUNTIME = "docker"
DEFAULT_CONTAINER_PLATFORM = "linux/amd64"
DEFAULT_CONTAINER_ENABLED = False
DEFAULT_CONTAINER_BASE_IMAGE = "ubuntu:22.04"
DEFAULT_CONTAINER_STORAGE_PATH = "~/.wrknv/containers"

# =================================
# Package and Registry defaults
# =================================
DEFAULT_PACKAGE_FORMAT = "tar"
DEFAULT_SEARCH_LIMIT = 10
DEFAULT_PACKAGE_DESCRIPTION = ""
DEFAULT_PACKAGE_AUTHOR = ""
DEFAULT_PACKAGE_LICENSE = "MIT"
DEFAULT_REGISTRY_WRKNV_URL = "https://registry.wrknv.io"
DEFAULT_REGISTRY_VERIFY_SSL = True
DEFAULT_REGISTRY_TIMEOUT = 30

# =================================
# Tool Manager defaults
# =================================
DEFAULT_TOOL_TIMEOUT = 10
DEFAULT_DOWNLOAD_TIMEOUT = 30
DEFAULT_TOOL_ENABLED = True
DEFAULT_TOOL_AUTO_DETECT = False

# =================================
# Environment defaults
# =================================
DEFAULT_PYTHON_VERSION = "3.11"

# =================================
# Registry and URL defaults
# =================================
DEFAULT_REGISTRY_URL = None  # Will be set when registry is implemented

# =================================
# Template defaults
# =================================
DEFAULT_TEMPLATE_VERSION = None
DEFAULT_TEMPLATE_BRANCH = None

# =================================
# Logging defaults
# =================================
DEFAULT_LOG_LEVEL = "WARNING"

# =================================
# Configuration defaults
# =================================
DEFAULT_WORKENV_INSTALL_DIR = "~/.wrknv"
DEFAULT_WORKENV_CACHE_DIR = "~/.wrknv/cache"
DEFAULT_TELEMETRY_ENABLED = True
DEFAULT_AUTO_UPDATE = False

# =================================
# CLI defaults
# =================================
DEFAULT_CLI_NAME = "wrknv"
DEFAULT_CLI_VERSION = "0.3.0"
DEFAULT_CLI_HELP = (
    "wrknv provides cross-platform tool installation and version management "
    "for development environments, including Terraform, OpenTofu, Go, UV, and more."
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

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_orig() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "cache" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_1() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "cache" * "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_2() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" * "cache" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_3() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() * ".wrknv" / "cache" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_4() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / "XX.wrknvXX" / "cache" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_5() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".WRKNV" / "cache" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_6() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "XXcacheXX" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_7() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "CACHE" / "packages"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_8() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "cache" / "XXpackagesXX"

# =================================
# Factory functions for mutable defaults
# =================================


def x_default_workenv_cache_dir__mutmut_9() -> Path:
    """Factory for workenv cache directory."""
    return Path.home() / ".wrknv" / "cache" / "PACKAGES"

x_default_workenv_cache_dir__mutmut_mutants : ClassVar[MutantDict] = {
'x_default_workenv_cache_dir__mutmut_1': x_default_workenv_cache_dir__mutmut_1, 
    'x_default_workenv_cache_dir__mutmut_2': x_default_workenv_cache_dir__mutmut_2, 
    'x_default_workenv_cache_dir__mutmut_3': x_default_workenv_cache_dir__mutmut_3, 
    'x_default_workenv_cache_dir__mutmut_4': x_default_workenv_cache_dir__mutmut_4, 
    'x_default_workenv_cache_dir__mutmut_5': x_default_workenv_cache_dir__mutmut_5, 
    'x_default_workenv_cache_dir__mutmut_6': x_default_workenv_cache_dir__mutmut_6, 
    'x_default_workenv_cache_dir__mutmut_7': x_default_workenv_cache_dir__mutmut_7, 
    'x_default_workenv_cache_dir__mutmut_8': x_default_workenv_cache_dir__mutmut_8, 
    'x_default_workenv_cache_dir__mutmut_9': x_default_workenv_cache_dir__mutmut_9
}

def default_workenv_cache_dir(*args, **kwargs):
    result = _mutmut_trampoline(x_default_workenv_cache_dir__mutmut_orig, x_default_workenv_cache_dir__mutmut_mutants, args, kwargs)
    return result 

default_workenv_cache_dir.__signature__ = _mutmut_signature(x_default_workenv_cache_dir__mutmut_orig)
x_default_workenv_cache_dir__mutmut_orig.__name__ = 'x_default_workenv_cache_dir'


def x_default_config_dir__mutmut_orig() -> Path:
    """Factory for wrknv config directory."""
    return Path.home() / ".wrknv"


def x_default_config_dir__mutmut_1() -> Path:
    """Factory for wrknv config directory."""
    return Path.home() * ".wrknv"


def x_default_config_dir__mutmut_2() -> Path:
    """Factory for wrknv config directory."""
    return Path.home() / "XX.wrknvXX"


def x_default_config_dir__mutmut_3() -> Path:
    """Factory for wrknv config directory."""
    return Path.home() / ".WRKNV"

x_default_config_dir__mutmut_mutants : ClassVar[MutantDict] = {
'x_default_config_dir__mutmut_1': x_default_config_dir__mutmut_1, 
    'x_default_config_dir__mutmut_2': x_default_config_dir__mutmut_2, 
    'x_default_config_dir__mutmut_3': x_default_config_dir__mutmut_3
}

def default_config_dir(*args, **kwargs):
    result = _mutmut_trampoline(x_default_config_dir__mutmut_orig, x_default_config_dir__mutmut_mutants, args, kwargs)
    return result 

default_config_dir.__signature__ = _mutmut_signature(x_default_config_dir__mutmut_orig)
x_default_config_dir__mutmut_orig.__name__ = 'x_default_config_dir'


def x_default_workenv_dir__mutmut_orig() -> Path:
    """Factory for workenv directory."""
    return Path("workenv")


def x_default_workenv_dir__mutmut_1() -> Path:
    """Factory for workenv directory."""
    return Path(None)


def x_default_workenv_dir__mutmut_2() -> Path:
    """Factory for workenv directory."""
    return Path("XXworkenvXX")


def x_default_workenv_dir__mutmut_3() -> Path:
    """Factory for workenv directory."""
    return Path("WORKENV")

x_default_workenv_dir__mutmut_mutants : ClassVar[MutantDict] = {
'x_default_workenv_dir__mutmut_1': x_default_workenv_dir__mutmut_1, 
    'x_default_workenv_dir__mutmut_2': x_default_workenv_dir__mutmut_2, 
    'x_default_workenv_dir__mutmut_3': x_default_workenv_dir__mutmut_3
}

def default_workenv_dir(*args, **kwargs):
    result = _mutmut_trampoline(x_default_workenv_dir__mutmut_orig, x_default_workenv_dir__mutmut_mutants, args, kwargs)
    return result 

default_workenv_dir.__signature__ = _mutmut_signature(x_default_workenv_dir__mutmut_orig)
x_default_workenv_dir__mutmut_orig.__name__ = 'x_default_workenv_dir'


def default_empty_list() -> list[str]:
    """Factory for empty string lists."""
    return []


def default_empty_dict() -> dict[str, str]:
    """Factory for empty string dictionaries."""
    return {}


def default_custom_values() -> dict[str, Any]:
    """Factory for custom values dictionary."""
    return {}


# 🧰🌍🔚
