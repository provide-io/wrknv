#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Platform Detection
===================================
Platform and architecture information using provide.foundation."""

from __future__ import annotations

from provide.foundation.platform import (
    get_arch_name,
    get_os_name as foundation_get_os_name,
    get_platform_string,
    get_system_info,
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


def x_get_platform_info__mutmut_orig() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_1() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = None

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_2() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "XXosXX": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_3() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "OS": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_4() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "XXarchXX": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_5() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "ARCH": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_6() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "XXplatformXX": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_7() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "PLATFORM": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_8() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "XXpython_platformXX": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_9() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "PYTHON_PLATFORM": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_10() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "XXmachineXX": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_11() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "MACHINE": sys_info.arch,
        "system": sys_info.os_name,
    }


def x_get_platform_info__mutmut_12() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "XXsystemXX": sys_info.os_name,
    }


def x_get_platform_info__mutmut_13() -> dict[str, str]:
    """Get platform information for tool downloads.

    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()

    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "SYSTEM": sys_info.os_name,
    }

x_get_platform_info__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_platform_info__mutmut_1': x_get_platform_info__mutmut_1, 
    'x_get_platform_info__mutmut_2': x_get_platform_info__mutmut_2, 
    'x_get_platform_info__mutmut_3': x_get_platform_info__mutmut_3, 
    'x_get_platform_info__mutmut_4': x_get_platform_info__mutmut_4, 
    'x_get_platform_info__mutmut_5': x_get_platform_info__mutmut_5, 
    'x_get_platform_info__mutmut_6': x_get_platform_info__mutmut_6, 
    'x_get_platform_info__mutmut_7': x_get_platform_info__mutmut_7, 
    'x_get_platform_info__mutmut_8': x_get_platform_info__mutmut_8, 
    'x_get_platform_info__mutmut_9': x_get_platform_info__mutmut_9, 
    'x_get_platform_info__mutmut_10': x_get_platform_info__mutmut_10, 
    'x_get_platform_info__mutmut_11': x_get_platform_info__mutmut_11, 
    'x_get_platform_info__mutmut_12': x_get_platform_info__mutmut_12, 
    'x_get_platform_info__mutmut_13': x_get_platform_info__mutmut_13
}

def get_platform_info(*args, **kwargs):
    result = _mutmut_trampoline(x_get_platform_info__mutmut_orig, x_get_platform_info__mutmut_mutants, args, kwargs)
    return result 

get_platform_info.__signature__ = _mutmut_signature(x_get_platform_info__mutmut_orig)
x_get_platform_info__mutmut_orig.__name__ = 'x_get_platform_info'


def get_architecture() -> str:
    """Get normalized architecture name for tool downloads.

    Returns:
        Architecture string suitable for tool downloads (amd64, arm64, etc).
    """
    return get_arch_name()


def get_workenv_platform() -> str:
    """Get platform string for workenv directory naming.

    Returns:
        Platform string in format: {os}_{arch}
    """
    return get_platform_string()


def x_is_arm_mac__mutmut_orig() -> bool:
    """Check if running on Apple Silicon Mac.

    Returns:
        True if running on ARM-based Mac (M1/M2/M3).
    """
    from provide.foundation.platform import is_arm, is_macos

    return is_macos() and is_arm()


def x_is_arm_mac__mutmut_1() -> bool:
    """Check if running on Apple Silicon Mac.

    Returns:
        True if running on ARM-based Mac (M1/M2/M3).
    """
    from provide.foundation.platform import is_arm, is_macos

    return is_macos() or is_arm()

x_is_arm_mac__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_arm_mac__mutmut_1': x_is_arm_mac__mutmut_1
}

def is_arm_mac(*args, **kwargs):
    result = _mutmut_trampoline(x_is_arm_mac__mutmut_orig, x_is_arm_mac__mutmut_mutants, args, kwargs)
    return result 

is_arm_mac.__signature__ = _mutmut_signature(x_is_arm_mac__mutmut_orig)
x_is_arm_mac__mutmut_orig.__name__ = 'x_is_arm_mac'


def is_windows() -> bool:
    """Check if running on Windows.

    Returns:
        True if running on Windows.
    """
    from provide.foundation.platform import is_windows as foundation_is_windows

    return foundation_is_windows()


# Re-export for backward compatibility (remove these later)
def get_os_name() -> str:
    """Get normalized OS name for tool downloads.

    DEPRECATED: Use provide.foundation.platform.get_os_name directly.
    """
    return foundation_get_os_name()


def format_platform_string(os_name: str, arch: str) -> str:
    """Format platform string for tool downloads.

    Args:
        os_name: Operating system name
        arch: Architecture name

    Returns:
        Formatted platform string
    """
    return f"{os_name}_{arch}"


def x_parse_platform_string__mutmut_orig(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_1(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = None
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_2(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split(None, 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_3(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", None)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_4(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split(1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_5(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", )
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_6(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.rsplit("_", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_7(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("XX_XX", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_8(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 2)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_9(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 1)
    if len(parts) != 2:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_10(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 1)
    if len(parts) == 3:
        return parts[0], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_11(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 1)
    if len(parts) == 2:
        return parts[1], parts[1]
    return platform_str, ""


def x_parse_platform_string__mutmut_12(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 1)
    if len(parts) == 2:
        return parts[0], parts[2]
    return platform_str, ""


def x_parse_platform_string__mutmut_13(platform_str: str) -> tuple[str, str]:
    """Parse platform string into OS and architecture.

    Args:
        platform_str: Platform string in format os_arch

    Returns:
        Tuple of (os_name, arch)
    """
    parts = platform_str.split("_", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return platform_str, "XXXX"

x_parse_platform_string__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_platform_string__mutmut_1': x_parse_platform_string__mutmut_1, 
    'x_parse_platform_string__mutmut_2': x_parse_platform_string__mutmut_2, 
    'x_parse_platform_string__mutmut_3': x_parse_platform_string__mutmut_3, 
    'x_parse_platform_string__mutmut_4': x_parse_platform_string__mutmut_4, 
    'x_parse_platform_string__mutmut_5': x_parse_platform_string__mutmut_5, 
    'x_parse_platform_string__mutmut_6': x_parse_platform_string__mutmut_6, 
    'x_parse_platform_string__mutmut_7': x_parse_platform_string__mutmut_7, 
    'x_parse_platform_string__mutmut_8': x_parse_platform_string__mutmut_8, 
    'x_parse_platform_string__mutmut_9': x_parse_platform_string__mutmut_9, 
    'x_parse_platform_string__mutmut_10': x_parse_platform_string__mutmut_10, 
    'x_parse_platform_string__mutmut_11': x_parse_platform_string__mutmut_11, 
    'x_parse_platform_string__mutmut_12': x_parse_platform_string__mutmut_12, 
    'x_parse_platform_string__mutmut_13': x_parse_platform_string__mutmut_13
}

def parse_platform_string(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_platform_string__mutmut_orig, x_parse_platform_string__mutmut_mutants, args, kwargs)
    return result 

parse_platform_string.__signature__ = _mutmut_signature(x_parse_platform_string__mutmut_orig)
x_parse_platform_string__mutmut_orig.__name__ = 'x_parse_platform_string'


def x_get_archive_extension__mutmut_orig() -> str:
    """Get appropriate archive extension for current platform.

    Returns:
        Archive extension (.zip for Windows, .tar.gz otherwise)
    """
    return ".zip" if is_windows() else ".tar.gz"


def x_get_archive_extension__mutmut_1() -> str:
    """Get appropriate archive extension for current platform.

    Returns:
        Archive extension (.zip for Windows, .tar.gz otherwise)
    """
    return "XX.zipXX" if is_windows() else ".tar.gz"


def x_get_archive_extension__mutmut_2() -> str:
    """Get appropriate archive extension for current platform.

    Returns:
        Archive extension (.zip for Windows, .tar.gz otherwise)
    """
    return ".ZIP" if is_windows() else ".tar.gz"


def x_get_archive_extension__mutmut_3() -> str:
    """Get appropriate archive extension for current platform.

    Returns:
        Archive extension (.zip for Windows, .tar.gz otherwise)
    """
    return ".zip" if is_windows() else "XX.tar.gzXX"


def x_get_archive_extension__mutmut_4() -> str:
    """Get appropriate archive extension for current platform.

    Returns:
        Archive extension (.zip for Windows, .tar.gz otherwise)
    """
    return ".zip" if is_windows() else ".TAR.GZ"

x_get_archive_extension__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_archive_extension__mutmut_1': x_get_archive_extension__mutmut_1, 
    'x_get_archive_extension__mutmut_2': x_get_archive_extension__mutmut_2, 
    'x_get_archive_extension__mutmut_3': x_get_archive_extension__mutmut_3, 
    'x_get_archive_extension__mutmut_4': x_get_archive_extension__mutmut_4
}

def get_archive_extension(*args, **kwargs):
    result = _mutmut_trampoline(x_get_archive_extension__mutmut_orig, x_get_archive_extension__mutmut_mutants, args, kwargs)
    return result 

get_archive_extension.__signature__ = _mutmut_signature(x_get_archive_extension__mutmut_orig)
x_get_archive_extension__mutmut_orig.__name__ = 'x_get_archive_extension'


def x_get_executable_extension__mutmut_orig() -> str:
    """Get executable file extension for current platform.

    Returns:
        Executable extension (.exe for Windows, empty string otherwise)
    """
    return ".exe" if is_windows() else ""


def x_get_executable_extension__mutmut_1() -> str:
    """Get executable file extension for current platform.

    Returns:
        Executable extension (.exe for Windows, empty string otherwise)
    """
    return "XX.exeXX" if is_windows() else ""


def x_get_executable_extension__mutmut_2() -> str:
    """Get executable file extension for current platform.

    Returns:
        Executable extension (.exe for Windows, empty string otherwise)
    """
    return ".EXE" if is_windows() else ""


def x_get_executable_extension__mutmut_3() -> str:
    """Get executable file extension for current platform.

    Returns:
        Executable extension (.exe for Windows, empty string otherwise)
    """
    return ".exe" if is_windows() else "XXXX"

x_get_executable_extension__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_executable_extension__mutmut_1': x_get_executable_extension__mutmut_1, 
    'x_get_executable_extension__mutmut_2': x_get_executable_extension__mutmut_2, 
    'x_get_executable_extension__mutmut_3': x_get_executable_extension__mutmut_3
}

def get_executable_extension(*args, **kwargs):
    result = _mutmut_trampoline(x_get_executable_extension__mutmut_orig, x_get_executable_extension__mutmut_mutants, args, kwargs)
    return result 

get_executable_extension.__signature__ = _mutmut_signature(x_get_executable_extension__mutmut_orig)
x_get_executable_extension__mutmut_orig.__name__ = 'x_get_executable_extension'


def x_is_supported_platform__mutmut_orig() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_1() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = None
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_2() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["XXdarwinXX", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_3() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["DARWIN", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_4() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "XXlinuxXX", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_5() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "LINUX", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_6() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "XXwindowsXX"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_7() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "WINDOWS"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_8() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = None

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_9() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["XXamd64XX", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_10() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["AMD64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_11() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "XXarm64XX", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_12() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "ARM64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_13() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "XXx86_64XX", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_14() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "X86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_15() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "XXaarch64XX"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_16() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "AARCH64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_17() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = None
    arch = get_architecture()

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_18() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = None

    return os_name in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_19() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os or arch in supported_arch


def x_is_supported_platform__mutmut_20() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name not in supported_os and arch in supported_arch


def x_is_supported_platform__mutmut_21() -> bool:
    """Check if current platform is supported.

    Returns:
        True if platform is supported
    """
    supported_os = ["darwin", "linux", "windows"]
    supported_arch = ["amd64", "arm64", "x86_64", "aarch64"]

    os_name = get_os_name()
    arch = get_architecture()

    return os_name in supported_os and arch not in supported_arch

x_is_supported_platform__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_supported_platform__mutmut_1': x_is_supported_platform__mutmut_1, 
    'x_is_supported_platform__mutmut_2': x_is_supported_platform__mutmut_2, 
    'x_is_supported_platform__mutmut_3': x_is_supported_platform__mutmut_3, 
    'x_is_supported_platform__mutmut_4': x_is_supported_platform__mutmut_4, 
    'x_is_supported_platform__mutmut_5': x_is_supported_platform__mutmut_5, 
    'x_is_supported_platform__mutmut_6': x_is_supported_platform__mutmut_6, 
    'x_is_supported_platform__mutmut_7': x_is_supported_platform__mutmut_7, 
    'x_is_supported_platform__mutmut_8': x_is_supported_platform__mutmut_8, 
    'x_is_supported_platform__mutmut_9': x_is_supported_platform__mutmut_9, 
    'x_is_supported_platform__mutmut_10': x_is_supported_platform__mutmut_10, 
    'x_is_supported_platform__mutmut_11': x_is_supported_platform__mutmut_11, 
    'x_is_supported_platform__mutmut_12': x_is_supported_platform__mutmut_12, 
    'x_is_supported_platform__mutmut_13': x_is_supported_platform__mutmut_13, 
    'x_is_supported_platform__mutmut_14': x_is_supported_platform__mutmut_14, 
    'x_is_supported_platform__mutmut_15': x_is_supported_platform__mutmut_15, 
    'x_is_supported_platform__mutmut_16': x_is_supported_platform__mutmut_16, 
    'x_is_supported_platform__mutmut_17': x_is_supported_platform__mutmut_17, 
    'x_is_supported_platform__mutmut_18': x_is_supported_platform__mutmut_18, 
    'x_is_supported_platform__mutmut_19': x_is_supported_platform__mutmut_19, 
    'x_is_supported_platform__mutmut_20': x_is_supported_platform__mutmut_20, 
    'x_is_supported_platform__mutmut_21': x_is_supported_platform__mutmut_21
}

def is_supported_platform(*args, **kwargs):
    result = _mutmut_trampoline(x_is_supported_platform__mutmut_orig, x_is_supported_platform__mutmut_mutants, args, kwargs)
    return result 

is_supported_platform.__signature__ = _mutmut_signature(x_is_supported_platform__mutmut_orig)
x_is_supported_platform__mutmut_orig.__name__ = 'x_is_supported_platform'


def x_get_platform_mapping__mutmut_orig(tool_name: str) -> dict[str, str]:
    """Get platform mapping for a specific tool.

    Args:
        tool_name: Name of the tool

    Returns:
        Dictionary mapping standard names to tool-specific names
    """
    mappings = get_download_platform_mappings()
    return mappings.get(tool_name, {})


def x_get_platform_mapping__mutmut_1(tool_name: str) -> dict[str, str]:
    """Get platform mapping for a specific tool.

    Args:
        tool_name: Name of the tool

    Returns:
        Dictionary mapping standard names to tool-specific names
    """
    mappings = None
    return mappings.get(tool_name, {})


def x_get_platform_mapping__mutmut_2(tool_name: str) -> dict[str, str]:
    """Get platform mapping for a specific tool.

    Args:
        tool_name: Name of the tool

    Returns:
        Dictionary mapping standard names to tool-specific names
    """
    mappings = get_download_platform_mappings()
    return mappings.get(None, {})


def x_get_platform_mapping__mutmut_3(tool_name: str) -> dict[str, str]:
    """Get platform mapping for a specific tool.

    Args:
        tool_name: Name of the tool

    Returns:
        Dictionary mapping standard names to tool-specific names
    """
    mappings = get_download_platform_mappings()
    return mappings.get(tool_name, None)


def x_get_platform_mapping__mutmut_4(tool_name: str) -> dict[str, str]:
    """Get platform mapping for a specific tool.

    Args:
        tool_name: Name of the tool

    Returns:
        Dictionary mapping standard names to tool-specific names
    """
    mappings = get_download_platform_mappings()
    return mappings.get({})


def x_get_platform_mapping__mutmut_5(tool_name: str) -> dict[str, str]:
    """Get platform mapping for a specific tool.

    Args:
        tool_name: Name of the tool

    Returns:
        Dictionary mapping standard names to tool-specific names
    """
    mappings = get_download_platform_mappings()
    return mappings.get(tool_name, )

x_get_platform_mapping__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_platform_mapping__mutmut_1': x_get_platform_mapping__mutmut_1, 
    'x_get_platform_mapping__mutmut_2': x_get_platform_mapping__mutmut_2, 
    'x_get_platform_mapping__mutmut_3': x_get_platform_mapping__mutmut_3, 
    'x_get_platform_mapping__mutmut_4': x_get_platform_mapping__mutmut_4, 
    'x_get_platform_mapping__mutmut_5': x_get_platform_mapping__mutmut_5
}

def get_platform_mapping(*args, **kwargs):
    result = _mutmut_trampoline(x_get_platform_mapping__mutmut_orig, x_get_platform_mapping__mutmut_mutants, args, kwargs)
    return result 

get_platform_mapping.__signature__ = _mutmut_signature(x_get_platform_mapping__mutmut_orig)
x_get_platform_mapping__mutmut_orig.__name__ = 'x_get_platform_mapping'


def x_get_download_platform_mappings__mutmut_orig() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_1() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "XXterraformXX": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_2() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "TERRAFORM": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_3() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "XXdarwin_arm64XX": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_4() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "DARWIN_ARM64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_5() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "XXdarwin_arm64XX",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_6() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "DARWIN_ARM64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_7() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "XXdarwin_amd64XX": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_8() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "DARWIN_AMD64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_9() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "XXdarwin_amd64XX",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_10() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "DARWIN_AMD64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_11() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "XXlinux_arm64XX": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_12() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "LINUX_ARM64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_13() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "XXlinux_arm64XX",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_14() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "LINUX_ARM64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_15() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "XXlinux_amd64XX": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_16() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "LINUX_AMD64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_17() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "XXlinux_amd64XX",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_18() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "LINUX_AMD64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_19() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "XXwindows_amd64XX": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_20() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "WINDOWS_AMD64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_21() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "XXwindows_amd64XX",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_22() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "WINDOWS_AMD64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_23() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "XXtofuXX": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_24() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "TOFU": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_25() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "XXdarwin_arm64XX": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_26() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "DARWIN_ARM64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_27() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "XXdarwin_arm64XX",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_28() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "DARWIN_ARM64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_29() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "XXdarwin_amd64XX": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_30() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "DARWIN_AMD64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_31() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "XXdarwin_amd64XX",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_32() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "DARWIN_AMD64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_33() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "XXlinux_arm64XX": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_34() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "LINUX_ARM64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_35() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "XXlinux_arm64XX",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_36() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "LINUX_ARM64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_37() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "XXlinux_amd64XX": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_38() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "LINUX_AMD64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_39() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "XXlinux_amd64XX",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_40() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "LINUX_AMD64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_41() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "XXwindows_amd64XX": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_42() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "WINDOWS_AMD64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_43() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "XXwindows_amd64XX",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_44() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "WINDOWS_AMD64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_45() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "XXgoXX": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_46() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "GO": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_47() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "XXdarwin_arm64XX": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_48() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "DARWIN_ARM64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_49() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "XXdarwin-arm64XX",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_50() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "DARWIN-ARM64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_51() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "XXdarwin_amd64XX": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_52() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "DARWIN_AMD64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_53() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "XXdarwin-amd64XX",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_54() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "DARWIN-AMD64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_55() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "XXlinux_arm64XX": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_56() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "LINUX_ARM64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_57() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "XXlinux-arm64XX",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_58() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "LINUX-ARM64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_59() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "XXlinux_amd64XX": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_60() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "LINUX_AMD64": "linux-amd64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_61() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "XXlinux-amd64XX",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_62() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "LINUX-AMD64",
            "windows_amd64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_63() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "XXwindows_amd64XX": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_64() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "WINDOWS_AMD64": "windows-amd64",
        },
    }


def x_get_download_platform_mappings__mutmut_65() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "XXwindows-amd64XX",
        },
    }


def x_get_download_platform_mappings__mutmut_66() -> dict[str, dict[str, str]]:
    """Get platform naming mappings for various tools.

    Returns:
        Dictionary of tool-specific platform mappings
    """
    return {
        "terraform": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "tofu": {
            "darwin_arm64": "darwin_arm64",
            "darwin_amd64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_amd64": "linux_amd64",
            "windows_amd64": "windows_amd64",
        },
        "go": {
            "darwin_arm64": "darwin-arm64",
            "darwin_amd64": "darwin-amd64",
            "linux_arm64": "linux-arm64",
            "linux_amd64": "linux-amd64",
            "windows_amd64": "WINDOWS-AMD64",
        },
    }

x_get_download_platform_mappings__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_download_platform_mappings__mutmut_1': x_get_download_platform_mappings__mutmut_1, 
    'x_get_download_platform_mappings__mutmut_2': x_get_download_platform_mappings__mutmut_2, 
    'x_get_download_platform_mappings__mutmut_3': x_get_download_platform_mappings__mutmut_3, 
    'x_get_download_platform_mappings__mutmut_4': x_get_download_platform_mappings__mutmut_4, 
    'x_get_download_platform_mappings__mutmut_5': x_get_download_platform_mappings__mutmut_5, 
    'x_get_download_platform_mappings__mutmut_6': x_get_download_platform_mappings__mutmut_6, 
    'x_get_download_platform_mappings__mutmut_7': x_get_download_platform_mappings__mutmut_7, 
    'x_get_download_platform_mappings__mutmut_8': x_get_download_platform_mappings__mutmut_8, 
    'x_get_download_platform_mappings__mutmut_9': x_get_download_platform_mappings__mutmut_9, 
    'x_get_download_platform_mappings__mutmut_10': x_get_download_platform_mappings__mutmut_10, 
    'x_get_download_platform_mappings__mutmut_11': x_get_download_platform_mappings__mutmut_11, 
    'x_get_download_platform_mappings__mutmut_12': x_get_download_platform_mappings__mutmut_12, 
    'x_get_download_platform_mappings__mutmut_13': x_get_download_platform_mappings__mutmut_13, 
    'x_get_download_platform_mappings__mutmut_14': x_get_download_platform_mappings__mutmut_14, 
    'x_get_download_platform_mappings__mutmut_15': x_get_download_platform_mappings__mutmut_15, 
    'x_get_download_platform_mappings__mutmut_16': x_get_download_platform_mappings__mutmut_16, 
    'x_get_download_platform_mappings__mutmut_17': x_get_download_platform_mappings__mutmut_17, 
    'x_get_download_platform_mappings__mutmut_18': x_get_download_platform_mappings__mutmut_18, 
    'x_get_download_platform_mappings__mutmut_19': x_get_download_platform_mappings__mutmut_19, 
    'x_get_download_platform_mappings__mutmut_20': x_get_download_platform_mappings__mutmut_20, 
    'x_get_download_platform_mappings__mutmut_21': x_get_download_platform_mappings__mutmut_21, 
    'x_get_download_platform_mappings__mutmut_22': x_get_download_platform_mappings__mutmut_22, 
    'x_get_download_platform_mappings__mutmut_23': x_get_download_platform_mappings__mutmut_23, 
    'x_get_download_platform_mappings__mutmut_24': x_get_download_platform_mappings__mutmut_24, 
    'x_get_download_platform_mappings__mutmut_25': x_get_download_platform_mappings__mutmut_25, 
    'x_get_download_platform_mappings__mutmut_26': x_get_download_platform_mappings__mutmut_26, 
    'x_get_download_platform_mappings__mutmut_27': x_get_download_platform_mappings__mutmut_27, 
    'x_get_download_platform_mappings__mutmut_28': x_get_download_platform_mappings__mutmut_28, 
    'x_get_download_platform_mappings__mutmut_29': x_get_download_platform_mappings__mutmut_29, 
    'x_get_download_platform_mappings__mutmut_30': x_get_download_platform_mappings__mutmut_30, 
    'x_get_download_platform_mappings__mutmut_31': x_get_download_platform_mappings__mutmut_31, 
    'x_get_download_platform_mappings__mutmut_32': x_get_download_platform_mappings__mutmut_32, 
    'x_get_download_platform_mappings__mutmut_33': x_get_download_platform_mappings__mutmut_33, 
    'x_get_download_platform_mappings__mutmut_34': x_get_download_platform_mappings__mutmut_34, 
    'x_get_download_platform_mappings__mutmut_35': x_get_download_platform_mappings__mutmut_35, 
    'x_get_download_platform_mappings__mutmut_36': x_get_download_platform_mappings__mutmut_36, 
    'x_get_download_platform_mappings__mutmut_37': x_get_download_platform_mappings__mutmut_37, 
    'x_get_download_platform_mappings__mutmut_38': x_get_download_platform_mappings__mutmut_38, 
    'x_get_download_platform_mappings__mutmut_39': x_get_download_platform_mappings__mutmut_39, 
    'x_get_download_platform_mappings__mutmut_40': x_get_download_platform_mappings__mutmut_40, 
    'x_get_download_platform_mappings__mutmut_41': x_get_download_platform_mappings__mutmut_41, 
    'x_get_download_platform_mappings__mutmut_42': x_get_download_platform_mappings__mutmut_42, 
    'x_get_download_platform_mappings__mutmut_43': x_get_download_platform_mappings__mutmut_43, 
    'x_get_download_platform_mappings__mutmut_44': x_get_download_platform_mappings__mutmut_44, 
    'x_get_download_platform_mappings__mutmut_45': x_get_download_platform_mappings__mutmut_45, 
    'x_get_download_platform_mappings__mutmut_46': x_get_download_platform_mappings__mutmut_46, 
    'x_get_download_platform_mappings__mutmut_47': x_get_download_platform_mappings__mutmut_47, 
    'x_get_download_platform_mappings__mutmut_48': x_get_download_platform_mappings__mutmut_48, 
    'x_get_download_platform_mappings__mutmut_49': x_get_download_platform_mappings__mutmut_49, 
    'x_get_download_platform_mappings__mutmut_50': x_get_download_platform_mappings__mutmut_50, 
    'x_get_download_platform_mappings__mutmut_51': x_get_download_platform_mappings__mutmut_51, 
    'x_get_download_platform_mappings__mutmut_52': x_get_download_platform_mappings__mutmut_52, 
    'x_get_download_platform_mappings__mutmut_53': x_get_download_platform_mappings__mutmut_53, 
    'x_get_download_platform_mappings__mutmut_54': x_get_download_platform_mappings__mutmut_54, 
    'x_get_download_platform_mappings__mutmut_55': x_get_download_platform_mappings__mutmut_55, 
    'x_get_download_platform_mappings__mutmut_56': x_get_download_platform_mappings__mutmut_56, 
    'x_get_download_platform_mappings__mutmut_57': x_get_download_platform_mappings__mutmut_57, 
    'x_get_download_platform_mappings__mutmut_58': x_get_download_platform_mappings__mutmut_58, 
    'x_get_download_platform_mappings__mutmut_59': x_get_download_platform_mappings__mutmut_59, 
    'x_get_download_platform_mappings__mutmut_60': x_get_download_platform_mappings__mutmut_60, 
    'x_get_download_platform_mappings__mutmut_61': x_get_download_platform_mappings__mutmut_61, 
    'x_get_download_platform_mappings__mutmut_62': x_get_download_platform_mappings__mutmut_62, 
    'x_get_download_platform_mappings__mutmut_63': x_get_download_platform_mappings__mutmut_63, 
    'x_get_download_platform_mappings__mutmut_64': x_get_download_platform_mappings__mutmut_64, 
    'x_get_download_platform_mappings__mutmut_65': x_get_download_platform_mappings__mutmut_65, 
    'x_get_download_platform_mappings__mutmut_66': x_get_download_platform_mappings__mutmut_66
}

def get_download_platform_mappings(*args, **kwargs):
    result = _mutmut_trampoline(x_get_download_platform_mappings__mutmut_orig, x_get_download_platform_mappings__mutmut_mutants, args, kwargs)
    return result 

get_download_platform_mappings.__signature__ = _mutmut_signature(x_get_download_platform_mappings__mutmut_orig)
x_get_download_platform_mappings__mutmut_orig.__name__ = 'x_get_download_platform_mappings'


# 🧰🌍🔚
