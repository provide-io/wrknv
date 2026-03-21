# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#
# wrknv/package/manager.py
#
"""
Package Manager
===============
Manages package build environment and tools.
"""

from pathlib import Path

from wrknv.config import WorkenvConfig
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


class PackageManager:
    """Manages package build environment and required tools."""

    def xǁPackageManagerǁ__init____mutmut_orig(self, config: WorkenvConfig) -> None:
        """Initialize package manager with config."""
        self.config = config

    def xǁPackageManagerǁ__init____mutmut_1(self, config: WorkenvConfig) -> None:
        """Initialize package manager with config."""
        self.config = None
    
    xǁPackageManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPackageManagerǁ__init____mutmut_1': xǁPackageManagerǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPackageManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPackageManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPackageManagerǁ__init____mutmut_orig)
    xǁPackageManagerǁ__init____mutmut_orig.__name__ = 'xǁPackageManagerǁ__init__'

    def xǁPackageManagerǁcheck_required_tools__mutmut_orig(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("python"),
            "uv": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_1(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = None
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_2(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "XXpythonXX": shutil.which("python"),
            "uv": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_3(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "PYTHON": shutil.which("python"),
            "uv": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_4(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which(None),
            "uv": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_5(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("XXpythonXX"),
            "uv": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_6(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("PYTHON"),
            "uv": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_7(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("python"),
            "XXuvXX": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_8(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("python"),
            "UV": shutil.which("uv"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_9(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("python"),
            "uv": shutil.which(None),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_10(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("python"),
            "uv": shutil.which("XXuvXX"),
        }
        return tools

    def xǁPackageManagerǁcheck_required_tools__mutmut_11(self) -> dict[str, str | None]:
        """Check for required build tools.

        Returns:
            Dictionary mapping tool names to their paths (or None if not found).
        """
        import shutil

        tools = {
            "python": shutil.which("python"),
            "uv": shutil.which("UV"),
        }
        return tools
    
    xǁPackageManagerǁcheck_required_tools__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPackageManagerǁcheck_required_tools__mutmut_1': xǁPackageManagerǁcheck_required_tools__mutmut_1, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_2': xǁPackageManagerǁcheck_required_tools__mutmut_2, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_3': xǁPackageManagerǁcheck_required_tools__mutmut_3, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_4': xǁPackageManagerǁcheck_required_tools__mutmut_4, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_5': xǁPackageManagerǁcheck_required_tools__mutmut_5, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_6': xǁPackageManagerǁcheck_required_tools__mutmut_6, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_7': xǁPackageManagerǁcheck_required_tools__mutmut_7, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_8': xǁPackageManagerǁcheck_required_tools__mutmut_8, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_9': xǁPackageManagerǁcheck_required_tools__mutmut_9, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_10': xǁPackageManagerǁcheck_required_tools__mutmut_10, 
        'xǁPackageManagerǁcheck_required_tools__mutmut_11': xǁPackageManagerǁcheck_required_tools__mutmut_11
    }
    
    def check_required_tools(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPackageManagerǁcheck_required_tools__mutmut_orig"), object.__getattribute__(self, "xǁPackageManagerǁcheck_required_tools__mutmut_mutants"), args, kwargs, self)
        return result 
    
    check_required_tools.__signature__ = _mutmut_signature(xǁPackageManagerǁcheck_required_tools__mutmut_orig)
    xǁPackageManagerǁcheck_required_tools__mutmut_orig.__name__ = 'xǁPackageManagerǁcheck_required_tools'

    def xǁPackageManagerǁsetup_build_environment__mutmut_orig(self) -> dict[str, str]:
        """Set up environment variables for build.

        Returns:
            Dictionary of environment variables.
        """
        import os

        env = os.environ.copy()
        # Add any wrknv-specific environment variables here
        return env

    def xǁPackageManagerǁsetup_build_environment__mutmut_1(self) -> dict[str, str]:
        """Set up environment variables for build.

        Returns:
            Dictionary of environment variables.
        """
        import os

        env = None
        # Add any wrknv-specific environment variables here
        return env
    
    xǁPackageManagerǁsetup_build_environment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPackageManagerǁsetup_build_environment__mutmut_1': xǁPackageManagerǁsetup_build_environment__mutmut_1
    }
    
    def setup_build_environment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPackageManagerǁsetup_build_environment__mutmut_orig"), object.__getattribute__(self, "xǁPackageManagerǁsetup_build_environment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    setup_build_environment.__signature__ = _mutmut_signature(xǁPackageManagerǁsetup_build_environment__mutmut_orig)
    xǁPackageManagerǁsetup_build_environment__mutmut_orig.__name__ = 'xǁPackageManagerǁsetup_build_environment'

    def xǁPackageManagerǁget_package_cache_dir__mutmut_orig(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_1(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = None
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_2(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" * "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_3(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" * "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_4(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() * ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_5(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / "XX.wrknvXX" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_6(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".WRKNV" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_7(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "XXcacheXX" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_8(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "CACHE" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_9(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "XXpackagesXX"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_10(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "PACKAGES"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_11(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=None, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_12(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=None)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_13(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_14(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=True, )
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_15(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=False, exist_ok=True)
        return cache_dir

    def xǁPackageManagerǁget_package_cache_dir__mutmut_16(self) -> Path:
        """Get the package cache directory.

        Returns:
            Path to the cache directory.
        """
        cache_dir = Path.home() / ".wrknv" / "cache" / "packages"
        cache_dir.mkdir(parents=True, exist_ok=False)
        return cache_dir
    
    xǁPackageManagerǁget_package_cache_dir__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPackageManagerǁget_package_cache_dir__mutmut_1': xǁPackageManagerǁget_package_cache_dir__mutmut_1, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_2': xǁPackageManagerǁget_package_cache_dir__mutmut_2, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_3': xǁPackageManagerǁget_package_cache_dir__mutmut_3, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_4': xǁPackageManagerǁget_package_cache_dir__mutmut_4, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_5': xǁPackageManagerǁget_package_cache_dir__mutmut_5, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_6': xǁPackageManagerǁget_package_cache_dir__mutmut_6, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_7': xǁPackageManagerǁget_package_cache_dir__mutmut_7, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_8': xǁPackageManagerǁget_package_cache_dir__mutmut_8, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_9': xǁPackageManagerǁget_package_cache_dir__mutmut_9, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_10': xǁPackageManagerǁget_package_cache_dir__mutmut_10, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_11': xǁPackageManagerǁget_package_cache_dir__mutmut_11, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_12': xǁPackageManagerǁget_package_cache_dir__mutmut_12, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_13': xǁPackageManagerǁget_package_cache_dir__mutmut_13, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_14': xǁPackageManagerǁget_package_cache_dir__mutmut_14, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_15': xǁPackageManagerǁget_package_cache_dir__mutmut_15, 
        'xǁPackageManagerǁget_package_cache_dir__mutmut_16': xǁPackageManagerǁget_package_cache_dir__mutmut_16
    }
    
    def get_package_cache_dir(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPackageManagerǁget_package_cache_dir__mutmut_orig"), object.__getattribute__(self, "xǁPackageManagerǁget_package_cache_dir__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_package_cache_dir.__signature__ = _mutmut_signature(xǁPackageManagerǁget_package_cache_dir__mutmut_orig)
    xǁPackageManagerǁget_package_cache_dir__mutmut_orig.__name__ = 'xǁPackageManagerǁget_package_cache_dir'

    def xǁPackageManagerǁget_package_output_dir__mutmut_orig(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_1(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = None
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_2(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" * "packages"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_3(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() * ".wrknv" / "packages"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_4(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / "XX.wrknvXX" / "packages"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_5(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".WRKNV" / "packages"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_6(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "XXpackagesXX"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_7(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "PACKAGES"
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_8(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(parents=None, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_9(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(parents=True, exist_ok=None)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_10(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_11(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(parents=True, )
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_12(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(parents=False, exist_ok=True)
        return output_dir

    def xǁPackageManagerǁget_package_output_dir__mutmut_13(self) -> Path:
        """Get the package output directory.

        Returns:
            Path to the output directory.
        """
        output_dir = Path.home() / ".wrknv" / "packages"
        output_dir.mkdir(parents=True, exist_ok=False)
        return output_dir
    
    xǁPackageManagerǁget_package_output_dir__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPackageManagerǁget_package_output_dir__mutmut_1': xǁPackageManagerǁget_package_output_dir__mutmut_1, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_2': xǁPackageManagerǁget_package_output_dir__mutmut_2, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_3': xǁPackageManagerǁget_package_output_dir__mutmut_3, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_4': xǁPackageManagerǁget_package_output_dir__mutmut_4, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_5': xǁPackageManagerǁget_package_output_dir__mutmut_5, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_6': xǁPackageManagerǁget_package_output_dir__mutmut_6, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_7': xǁPackageManagerǁget_package_output_dir__mutmut_7, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_8': xǁPackageManagerǁget_package_output_dir__mutmut_8, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_9': xǁPackageManagerǁget_package_output_dir__mutmut_9, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_10': xǁPackageManagerǁget_package_output_dir__mutmut_10, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_11': xǁPackageManagerǁget_package_output_dir__mutmut_11, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_12': xǁPackageManagerǁget_package_output_dir__mutmut_12, 
        'xǁPackageManagerǁget_package_output_dir__mutmut_13': xǁPackageManagerǁget_package_output_dir__mutmut_13
    }
    
    def get_package_output_dir(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPackageManagerǁget_package_output_dir__mutmut_orig"), object.__getattribute__(self, "xǁPackageManagerǁget_package_output_dir__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_package_output_dir.__signature__ = _mutmut_signature(xǁPackageManagerǁget_package_output_dir__mutmut_orig)
    xǁPackageManagerǁget_package_output_dir__mutmut_orig.__name__ = 'xǁPackageManagerǁget_package_output_dir'


# 🧰🌍🖥️🪄
