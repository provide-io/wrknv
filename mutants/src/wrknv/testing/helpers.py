#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Test helpers for using wrknv-managed workenv directories instead of .venv.

This ensures tests use the proper workenv/package_os_arch pattern
that wrknv is designed to manage."""

from __future__ import annotations

from collections.abc import Iterator
import contextlib
import os
from pathlib import Path
import platform
import sys
from typing import Any

from provide.foundation import logger
from provide.foundation.process import CompletedProcess, run
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


def x_get_workenv_dir__mutmut_orig(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_1(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is not None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_2(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = None

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_3(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = None
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_4(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().upper()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_5(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = None

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_6(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().upper()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_7(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine not in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_8(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["XXx86_64XX", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_9(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["X86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_10(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "XXamd64XX"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_11(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "AMD64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_12(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = None
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_13(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "XXamd64XX"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_14(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "AMD64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_15(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine not in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_16(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["XXarm64XX", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_17(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["ARM64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_18(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "XXaarch64XX"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_19(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "AARCH64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_20(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = None
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_21(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "XXarm64XX"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_22(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "ARM64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_23(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = None

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_24(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = None
    return workenv_dir


def x_get_workenv_dir__mutmut_25(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "workenv" * f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_26(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() * "workenv" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_27(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "XXworkenvXX" / f"{package_name}_{system}_{arch}"
    return workenv_dir


def x_get_workenv_dir__mutmut_28(package_name: str | None = None) -> Path:
    """
    Get the proper workenv directory path for the current platform.

    Args:
        package_name: Optional package name. If not provided, uses the
                     current directory name.

    Returns:
        Path to the workenv directory (e.g., workenv/package_darwin_arm64)
    """
    if package_name is None:
        package_name = Path.cwd().name

    # Get platform info
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["x86_64", "amd64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = machine

    # Build directory name: workenv/package_os_arch
    workenv_dir = Path.cwd() / "WORKENV" / f"{package_name}_{system}_{arch}"
    return workenv_dir

x_get_workenv_dir__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_workenv_dir__mutmut_1': x_get_workenv_dir__mutmut_1, 
    'x_get_workenv_dir__mutmut_2': x_get_workenv_dir__mutmut_2, 
    'x_get_workenv_dir__mutmut_3': x_get_workenv_dir__mutmut_3, 
    'x_get_workenv_dir__mutmut_4': x_get_workenv_dir__mutmut_4, 
    'x_get_workenv_dir__mutmut_5': x_get_workenv_dir__mutmut_5, 
    'x_get_workenv_dir__mutmut_6': x_get_workenv_dir__mutmut_6, 
    'x_get_workenv_dir__mutmut_7': x_get_workenv_dir__mutmut_7, 
    'x_get_workenv_dir__mutmut_8': x_get_workenv_dir__mutmut_8, 
    'x_get_workenv_dir__mutmut_9': x_get_workenv_dir__mutmut_9, 
    'x_get_workenv_dir__mutmut_10': x_get_workenv_dir__mutmut_10, 
    'x_get_workenv_dir__mutmut_11': x_get_workenv_dir__mutmut_11, 
    'x_get_workenv_dir__mutmut_12': x_get_workenv_dir__mutmut_12, 
    'x_get_workenv_dir__mutmut_13': x_get_workenv_dir__mutmut_13, 
    'x_get_workenv_dir__mutmut_14': x_get_workenv_dir__mutmut_14, 
    'x_get_workenv_dir__mutmut_15': x_get_workenv_dir__mutmut_15, 
    'x_get_workenv_dir__mutmut_16': x_get_workenv_dir__mutmut_16, 
    'x_get_workenv_dir__mutmut_17': x_get_workenv_dir__mutmut_17, 
    'x_get_workenv_dir__mutmut_18': x_get_workenv_dir__mutmut_18, 
    'x_get_workenv_dir__mutmut_19': x_get_workenv_dir__mutmut_19, 
    'x_get_workenv_dir__mutmut_20': x_get_workenv_dir__mutmut_20, 
    'x_get_workenv_dir__mutmut_21': x_get_workenv_dir__mutmut_21, 
    'x_get_workenv_dir__mutmut_22': x_get_workenv_dir__mutmut_22, 
    'x_get_workenv_dir__mutmut_23': x_get_workenv_dir__mutmut_23, 
    'x_get_workenv_dir__mutmut_24': x_get_workenv_dir__mutmut_24, 
    'x_get_workenv_dir__mutmut_25': x_get_workenv_dir__mutmut_25, 
    'x_get_workenv_dir__mutmut_26': x_get_workenv_dir__mutmut_26, 
    'x_get_workenv_dir__mutmut_27': x_get_workenv_dir__mutmut_27, 
    'x_get_workenv_dir__mutmut_28': x_get_workenv_dir__mutmut_28
}

def get_workenv_dir(*args, **kwargs):
    result = _mutmut_trampoline(x_get_workenv_dir__mutmut_orig, x_get_workenv_dir__mutmut_mutants, args, kwargs)
    return result 

get_workenv_dir.__signature__ = _mutmut_signature(x_get_workenv_dir__mutmut_orig)
x_get_workenv_dir__mutmut_orig.__name__ = 'x_get_workenv_dir'


def x_activate_workenv__mutmut_orig(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_1(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = None

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_2(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(None)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_3(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_4(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            None
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_5(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = None

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_6(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = None

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_7(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["XXVIRTUAL_ENVXX"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_8(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["virtual_env"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_9(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(None)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_10(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = None
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_11(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir * "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_12(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "XXbinXX"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_13(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "BIN"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_14(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = None

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_15(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["XXPATHXX"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_16(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["path"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_17(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get(None, '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_18(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', None)}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_19(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_20(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', )}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_21(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('XXPATHXX', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_22(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('path', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_23(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', 'XXXX')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_24(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = None
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_25(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" * "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_26(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" * f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_27(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir * "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_28(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "XXlibXX" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_29(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "LIB" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_30(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "XXsite-packagesXX"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_31(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "SITE-PACKAGES"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_32(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = None

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_33(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["XXPYTHONPATHXX"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_34(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["pythonpath"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_35(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get(None, '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_36(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', None)}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_37(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_38(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', )}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_39(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('XXPYTHONPATHXX', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_40(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('pythonpath', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_41(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', 'XXXX')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", None)

    return env


def x_activate_workenv__mutmut_42(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop(None, None)

    return env


def x_activate_workenv__mutmut_43(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop(None)

    return env


def x_activate_workenv__mutmut_44(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("PYTHONHOME", )

    return env


def x_activate_workenv__mutmut_45(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("XXPYTHONHOMEXX", None)

    return env


def x_activate_workenv__mutmut_46(package_name: str | None = None) -> dict[str, str]:
    """
    Get environment variables for activating a wrknv-managed workenv.

    Args:
        package_name: Optional package name.

    Returns:
        Dictionary of environment variables to set.
    """
    workenv_dir = get_workenv_dir(package_name)

    if not workenv_dir.exists():
        raise RuntimeError(
            f"Workenv directory not found: {workenv_dir}\nRun 'wrknv setup' or 'source env.sh' to create it."
        )

    # Build environment variables
    env = os.environ.copy()

    # Set VIRTUAL_ENV
    env["VIRTUAL_ENV"] = str(workenv_dir)

    # Update PATH to include workenv bin directory
    bin_dir = workenv_dir / "bin"
    if bin_dir.exists():
        env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    # Set PYTHONPATH to include site-packages
    site_packages = (
        workenv_dir / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    )
    if site_packages.exists():
        env["PYTHONPATH"] = f"{site_packages}:{env.get('PYTHONPATH', '')}"

    # Unset PYTHONHOME if set (can interfere with virtual env)
    env.pop("pythonhome", None)

    return env

x_activate_workenv__mutmut_mutants : ClassVar[MutantDict] = {
'x_activate_workenv__mutmut_1': x_activate_workenv__mutmut_1, 
    'x_activate_workenv__mutmut_2': x_activate_workenv__mutmut_2, 
    'x_activate_workenv__mutmut_3': x_activate_workenv__mutmut_3, 
    'x_activate_workenv__mutmut_4': x_activate_workenv__mutmut_4, 
    'x_activate_workenv__mutmut_5': x_activate_workenv__mutmut_5, 
    'x_activate_workenv__mutmut_6': x_activate_workenv__mutmut_6, 
    'x_activate_workenv__mutmut_7': x_activate_workenv__mutmut_7, 
    'x_activate_workenv__mutmut_8': x_activate_workenv__mutmut_8, 
    'x_activate_workenv__mutmut_9': x_activate_workenv__mutmut_9, 
    'x_activate_workenv__mutmut_10': x_activate_workenv__mutmut_10, 
    'x_activate_workenv__mutmut_11': x_activate_workenv__mutmut_11, 
    'x_activate_workenv__mutmut_12': x_activate_workenv__mutmut_12, 
    'x_activate_workenv__mutmut_13': x_activate_workenv__mutmut_13, 
    'x_activate_workenv__mutmut_14': x_activate_workenv__mutmut_14, 
    'x_activate_workenv__mutmut_15': x_activate_workenv__mutmut_15, 
    'x_activate_workenv__mutmut_16': x_activate_workenv__mutmut_16, 
    'x_activate_workenv__mutmut_17': x_activate_workenv__mutmut_17, 
    'x_activate_workenv__mutmut_18': x_activate_workenv__mutmut_18, 
    'x_activate_workenv__mutmut_19': x_activate_workenv__mutmut_19, 
    'x_activate_workenv__mutmut_20': x_activate_workenv__mutmut_20, 
    'x_activate_workenv__mutmut_21': x_activate_workenv__mutmut_21, 
    'x_activate_workenv__mutmut_22': x_activate_workenv__mutmut_22, 
    'x_activate_workenv__mutmut_23': x_activate_workenv__mutmut_23, 
    'x_activate_workenv__mutmut_24': x_activate_workenv__mutmut_24, 
    'x_activate_workenv__mutmut_25': x_activate_workenv__mutmut_25, 
    'x_activate_workenv__mutmut_26': x_activate_workenv__mutmut_26, 
    'x_activate_workenv__mutmut_27': x_activate_workenv__mutmut_27, 
    'x_activate_workenv__mutmut_28': x_activate_workenv__mutmut_28, 
    'x_activate_workenv__mutmut_29': x_activate_workenv__mutmut_29, 
    'x_activate_workenv__mutmut_30': x_activate_workenv__mutmut_30, 
    'x_activate_workenv__mutmut_31': x_activate_workenv__mutmut_31, 
    'x_activate_workenv__mutmut_32': x_activate_workenv__mutmut_32, 
    'x_activate_workenv__mutmut_33': x_activate_workenv__mutmut_33, 
    'x_activate_workenv__mutmut_34': x_activate_workenv__mutmut_34, 
    'x_activate_workenv__mutmut_35': x_activate_workenv__mutmut_35, 
    'x_activate_workenv__mutmut_36': x_activate_workenv__mutmut_36, 
    'x_activate_workenv__mutmut_37': x_activate_workenv__mutmut_37, 
    'x_activate_workenv__mutmut_38': x_activate_workenv__mutmut_38, 
    'x_activate_workenv__mutmut_39': x_activate_workenv__mutmut_39, 
    'x_activate_workenv__mutmut_40': x_activate_workenv__mutmut_40, 
    'x_activate_workenv__mutmut_41': x_activate_workenv__mutmut_41, 
    'x_activate_workenv__mutmut_42': x_activate_workenv__mutmut_42, 
    'x_activate_workenv__mutmut_43': x_activate_workenv__mutmut_43, 
    'x_activate_workenv__mutmut_44': x_activate_workenv__mutmut_44, 
    'x_activate_workenv__mutmut_45': x_activate_workenv__mutmut_45, 
    'x_activate_workenv__mutmut_46': x_activate_workenv__mutmut_46
}

def activate_workenv(*args, **kwargs):
    result = _mutmut_trampoline(x_activate_workenv__mutmut_orig, x_activate_workenv__mutmut_mutants, args, kwargs)
    return result 

activate_workenv.__signature__ = _mutmut_signature(x_activate_workenv__mutmut_orig)
x_activate_workenv__mutmut_orig.__name__ = 'x_activate_workenv'


@contextlib.contextmanager
def workenv_context(package_name: str | None = None) -> Iterator[None]:
    """
    Context manager for running code with workenv activated.

    Usage:
        with workenv_context('pyvider'):
            # Code here runs with workenv activated
            import pyvider
    """
    old_env = os.environ.copy()
    try:
        new_env = activate_workenv(package_name)
        os.environ.update(new_env)
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_env)


class WorkenvTestRunner:
    """
    Test runner that uses wrknv-managed workenv directories.

    This should be used instead of creating .venv directories.
    """

    def xǁWorkenvTestRunnerǁ__init____mutmut_orig(self, package_name: str | None = None) -> None:
        """
        Initialize the test runner.

        Args:
            package_name: Optional package name. Defaults to current directory name.
        """
        self.package_name = package_name or Path.cwd().name
        self.workenv_dir = get_workenv_dir(self.package_name)

    def xǁWorkenvTestRunnerǁ__init____mutmut_1(self, package_name: str | None = None) -> None:
        """
        Initialize the test runner.

        Args:
            package_name: Optional package name. Defaults to current directory name.
        """
        self.package_name = None
        self.workenv_dir = get_workenv_dir(self.package_name)

    def xǁWorkenvTestRunnerǁ__init____mutmut_2(self, package_name: str | None = None) -> None:
        """
        Initialize the test runner.

        Args:
            package_name: Optional package name. Defaults to current directory name.
        """
        self.package_name = package_name and Path.cwd().name
        self.workenv_dir = get_workenv_dir(self.package_name)

    def xǁWorkenvTestRunnerǁ__init____mutmut_3(self, package_name: str | None = None) -> None:
        """
        Initialize the test runner.

        Args:
            package_name: Optional package name. Defaults to current directory name.
        """
        self.package_name = package_name or Path.cwd().name
        self.workenv_dir = None

    def xǁWorkenvTestRunnerǁ__init____mutmut_4(self, package_name: str | None = None) -> None:
        """
        Initialize the test runner.

        Args:
            package_name: Optional package name. Defaults to current directory name.
        """
        self.package_name = package_name or Path.cwd().name
        self.workenv_dir = get_workenv_dir(None)
    
    xǁWorkenvTestRunnerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvTestRunnerǁ__init____mutmut_1': xǁWorkenvTestRunnerǁ__init____mutmut_1, 
        'xǁWorkenvTestRunnerǁ__init____mutmut_2': xǁWorkenvTestRunnerǁ__init____mutmut_2, 
        'xǁWorkenvTestRunnerǁ__init____mutmut_3': xǁWorkenvTestRunnerǁ__init____mutmut_3, 
        'xǁWorkenvTestRunnerǁ__init____mutmut_4': xǁWorkenvTestRunnerǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvTestRunnerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkenvTestRunnerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkenvTestRunnerǁ__init____mutmut_orig)
    xǁWorkenvTestRunnerǁ__init____mutmut_orig.__name__ = 'xǁWorkenvTestRunnerǁ__init__'

    def xǁWorkenvTestRunnerǁsetup__mutmut_orig(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_1(self, force: bool = True) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_2(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = None
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_3(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() * "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_4(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "XXenv.shXX"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_5(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "ENV.SH"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_6(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_7(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(None)

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_8(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force or self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_9(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info(None, path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_10(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=None)
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_11(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info(path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_12(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", )
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_13(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("XXremoving_workenvXX", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_14(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("REMOVING_WORKENV", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_15(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(None))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_16(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(None)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_17(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info(None)
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_18(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("XXsetting_up_workenvXX")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_19(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("SETTING_UP_WORKENV")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_20(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = None

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_21(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(None)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_22(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["XXbashXX", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_23(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["BASH", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_24(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "XX-cXX", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_25(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-C", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_26(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode == 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_27(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 1:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_28(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(None)

        logger.debug("workenv_setup_output", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_29(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug(None, stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_30(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", stdout=None)

    def xǁWorkenvTestRunnerǁsetup__mutmut_31(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug(stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_32(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("workenv_setup_output", )

    def xǁWorkenvTestRunnerǁsetup__mutmut_33(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("XXworkenv_setup_outputXX", stdout=result.stdout)

    def xǁWorkenvTestRunnerǁsetup__mutmut_34(self, force: bool = False) -> None:
        """
        Set up the workenv by sourcing env.sh.

        The env.sh script generated by wrknv will automatically:
        - Create the workenv directory if it doesn't exist
        - Install UV if needed
        - Set up the virtual environment
        - Install all dependencies

        Args:
            force: If True, recreate the workenv even if it exists.
        """
        # Check if env.sh exists
        env_script = Path.cwd() / "env.sh"
        if not env_script.exists():
            raise RuntimeError(f"env.sh not found in {Path.cwd()}\nRun 'wrknv generate' to create it.")

        if force and self.workenv_dir.exists():
            import shutil

            logger.info("removing_workenv", path=str(self.workenv_dir))
            shutil.rmtree(self.workenv_dir)

        # Source env.sh - this will create the workenv directory automatically
        logger.info("setting_up_workenv")
        result = run(["bash", "-c", f"source {env_script} && echo 'Workenv ready at: $VIRTUAL_ENV'"])

        if result.returncode != 0:
            raise RuntimeError(f"Failed to source env.sh: {result.stderr}")

        logger.debug("WORKENV_SETUP_OUTPUT", stdout=result.stdout)
    
    xǁWorkenvTestRunnerǁsetup__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvTestRunnerǁsetup__mutmut_1': xǁWorkenvTestRunnerǁsetup__mutmut_1, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_2': xǁWorkenvTestRunnerǁsetup__mutmut_2, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_3': xǁWorkenvTestRunnerǁsetup__mutmut_3, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_4': xǁWorkenvTestRunnerǁsetup__mutmut_4, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_5': xǁWorkenvTestRunnerǁsetup__mutmut_5, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_6': xǁWorkenvTestRunnerǁsetup__mutmut_6, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_7': xǁWorkenvTestRunnerǁsetup__mutmut_7, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_8': xǁWorkenvTestRunnerǁsetup__mutmut_8, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_9': xǁWorkenvTestRunnerǁsetup__mutmut_9, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_10': xǁWorkenvTestRunnerǁsetup__mutmut_10, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_11': xǁWorkenvTestRunnerǁsetup__mutmut_11, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_12': xǁWorkenvTestRunnerǁsetup__mutmut_12, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_13': xǁWorkenvTestRunnerǁsetup__mutmut_13, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_14': xǁWorkenvTestRunnerǁsetup__mutmut_14, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_15': xǁWorkenvTestRunnerǁsetup__mutmut_15, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_16': xǁWorkenvTestRunnerǁsetup__mutmut_16, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_17': xǁWorkenvTestRunnerǁsetup__mutmut_17, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_18': xǁWorkenvTestRunnerǁsetup__mutmut_18, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_19': xǁWorkenvTestRunnerǁsetup__mutmut_19, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_20': xǁWorkenvTestRunnerǁsetup__mutmut_20, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_21': xǁWorkenvTestRunnerǁsetup__mutmut_21, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_22': xǁWorkenvTestRunnerǁsetup__mutmut_22, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_23': xǁWorkenvTestRunnerǁsetup__mutmut_23, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_24': xǁWorkenvTestRunnerǁsetup__mutmut_24, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_25': xǁWorkenvTestRunnerǁsetup__mutmut_25, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_26': xǁWorkenvTestRunnerǁsetup__mutmut_26, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_27': xǁWorkenvTestRunnerǁsetup__mutmut_27, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_28': xǁWorkenvTestRunnerǁsetup__mutmut_28, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_29': xǁWorkenvTestRunnerǁsetup__mutmut_29, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_30': xǁWorkenvTestRunnerǁsetup__mutmut_30, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_31': xǁWorkenvTestRunnerǁsetup__mutmut_31, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_32': xǁWorkenvTestRunnerǁsetup__mutmut_32, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_33': xǁWorkenvTestRunnerǁsetup__mutmut_33, 
        'xǁWorkenvTestRunnerǁsetup__mutmut_34': xǁWorkenvTestRunnerǁsetup__mutmut_34
    }
    
    def setup(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvTestRunnerǁsetup__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvTestRunnerǁsetup__mutmut_mutants"), args, kwargs, self)
        return result 
    
    setup.__signature__ = _mutmut_signature(xǁWorkenvTestRunnerǁsetup__mutmut_orig)
    xǁWorkenvTestRunnerǁsetup__mutmut_orig.__name__ = 'xǁWorkenvTestRunnerǁsetup'

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_orig(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_1(self, editable: bool = False, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_2(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = None

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_3(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(None)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_4(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = None

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_5(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(None), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_6(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" * "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_7(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir * "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_8(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "XXbinXX" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_9(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "BIN" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_10(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "XXpythonXX"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_11(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "PYTHON"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_12(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "XX-mXX", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_13(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-M", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_14(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "XXpipXX", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_15(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "PIP", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_16(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "XXinstallXX"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_17(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "INSTALL"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_18(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append(None)

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_19(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("XX-eXX")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_20(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-E")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_21(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = None
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_22(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "XX.XX"
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_23(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = None
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_24(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(None)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_25(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info(None, cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_26(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=None)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_27(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info(cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_28(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", )
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_29(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("XXinstalling_dependenciesXX", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_30(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("INSTALLING_DEPENDENCIES", cmd=cmd)
        run(cmd, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_31(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(None, env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_32(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=None, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_33(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=None)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_34(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(env=env, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_35(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, check=True)

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_36(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, )

    def xǁWorkenvTestRunnerǁinstall_deps__mutmut_37(self, editable: bool = True, extras: str | None = None) -> None:
        """
        Install package dependencies in the workenv.

        Args:
            editable: If True, install in editable mode.
            extras: Optional extras to install (e.g., "dev,test").
        """
        env = activate_workenv(self.package_name)

        # Build install command
        cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pip", "install"]

        if editable:
            cmd.append("-e")

        # Add package path with extras if specified
        package_spec = "."
        if extras:
            package_spec = f".[{extras}]"
        cmd.append(package_spec)

        logger.info("installing_dependencies", cmd=cmd)
        run(cmd, env=env, check=False)
    
    xǁWorkenvTestRunnerǁinstall_deps__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvTestRunnerǁinstall_deps__mutmut_1': xǁWorkenvTestRunnerǁinstall_deps__mutmut_1, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_2': xǁWorkenvTestRunnerǁinstall_deps__mutmut_2, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_3': xǁWorkenvTestRunnerǁinstall_deps__mutmut_3, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_4': xǁWorkenvTestRunnerǁinstall_deps__mutmut_4, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_5': xǁWorkenvTestRunnerǁinstall_deps__mutmut_5, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_6': xǁWorkenvTestRunnerǁinstall_deps__mutmut_6, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_7': xǁWorkenvTestRunnerǁinstall_deps__mutmut_7, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_8': xǁWorkenvTestRunnerǁinstall_deps__mutmut_8, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_9': xǁWorkenvTestRunnerǁinstall_deps__mutmut_9, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_10': xǁWorkenvTestRunnerǁinstall_deps__mutmut_10, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_11': xǁWorkenvTestRunnerǁinstall_deps__mutmut_11, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_12': xǁWorkenvTestRunnerǁinstall_deps__mutmut_12, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_13': xǁWorkenvTestRunnerǁinstall_deps__mutmut_13, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_14': xǁWorkenvTestRunnerǁinstall_deps__mutmut_14, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_15': xǁWorkenvTestRunnerǁinstall_deps__mutmut_15, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_16': xǁWorkenvTestRunnerǁinstall_deps__mutmut_16, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_17': xǁWorkenvTestRunnerǁinstall_deps__mutmut_17, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_18': xǁWorkenvTestRunnerǁinstall_deps__mutmut_18, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_19': xǁWorkenvTestRunnerǁinstall_deps__mutmut_19, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_20': xǁWorkenvTestRunnerǁinstall_deps__mutmut_20, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_21': xǁWorkenvTestRunnerǁinstall_deps__mutmut_21, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_22': xǁWorkenvTestRunnerǁinstall_deps__mutmut_22, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_23': xǁWorkenvTestRunnerǁinstall_deps__mutmut_23, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_24': xǁWorkenvTestRunnerǁinstall_deps__mutmut_24, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_25': xǁWorkenvTestRunnerǁinstall_deps__mutmut_25, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_26': xǁWorkenvTestRunnerǁinstall_deps__mutmut_26, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_27': xǁWorkenvTestRunnerǁinstall_deps__mutmut_27, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_28': xǁWorkenvTestRunnerǁinstall_deps__mutmut_28, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_29': xǁWorkenvTestRunnerǁinstall_deps__mutmut_29, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_30': xǁWorkenvTestRunnerǁinstall_deps__mutmut_30, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_31': xǁWorkenvTestRunnerǁinstall_deps__mutmut_31, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_32': xǁWorkenvTestRunnerǁinstall_deps__mutmut_32, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_33': xǁWorkenvTestRunnerǁinstall_deps__mutmut_33, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_34': xǁWorkenvTestRunnerǁinstall_deps__mutmut_34, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_35': xǁWorkenvTestRunnerǁinstall_deps__mutmut_35, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_36': xǁWorkenvTestRunnerǁinstall_deps__mutmut_36, 
        'xǁWorkenvTestRunnerǁinstall_deps__mutmut_37': xǁWorkenvTestRunnerǁinstall_deps__mutmut_37
    }
    
    def install_deps(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvTestRunnerǁinstall_deps__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvTestRunnerǁinstall_deps__mutmut_mutants"), args, kwargs, self)
        return result 
    
    install_deps.__signature__ = _mutmut_signature(xǁWorkenvTestRunnerǁinstall_deps__mutmut_orig)
    xǁWorkenvTestRunnerǁinstall_deps__mutmut_orig.__name__ = 'xǁWorkenvTestRunnerǁinstall_deps'

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_orig(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_1(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = None

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_2(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(None)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_3(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = None
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_4(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(None), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_5(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" * "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_6(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir * "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_7(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "XXbinXX" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_8(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "BIN" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_9(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "XXpythonXX"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_10(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "PYTHON"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_11(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "XX-mXX", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_12(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-M", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_13(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "XXpytestXX"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_14(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "PYTEST"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_15(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(None)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_16(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info(None, cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_17(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=None)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_18(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info(cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_19(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", )
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_20(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("XXrunning_testsXX", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_21(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("RUNNING_TESTS", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_22(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(None, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_23(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=None, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_24(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_25(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, **kwargs)

    def xǁWorkenvTestRunnerǁrun_pytest__mutmut_26(self, *args: str, **kwargs: Any) -> CompletedProcess:
        """
        Run pytest with the workenv activated.

        Args:
            *args: Arguments to pass to pytest.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)

        # Build pytest command
        pytest_cmd = [str(self.workenv_dir / "bin" / "python"), "-m", "pytest"]
        pytest_cmd.extend(args)

        logger.info("running_tests", cmd=pytest_cmd)
        return run(pytest_cmd, env=env, )
    
    xǁWorkenvTestRunnerǁrun_pytest__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvTestRunnerǁrun_pytest__mutmut_1': xǁWorkenvTestRunnerǁrun_pytest__mutmut_1, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_2': xǁWorkenvTestRunnerǁrun_pytest__mutmut_2, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_3': xǁWorkenvTestRunnerǁrun_pytest__mutmut_3, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_4': xǁWorkenvTestRunnerǁrun_pytest__mutmut_4, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_5': xǁWorkenvTestRunnerǁrun_pytest__mutmut_5, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_6': xǁWorkenvTestRunnerǁrun_pytest__mutmut_6, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_7': xǁWorkenvTestRunnerǁrun_pytest__mutmut_7, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_8': xǁWorkenvTestRunnerǁrun_pytest__mutmut_8, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_9': xǁWorkenvTestRunnerǁrun_pytest__mutmut_9, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_10': xǁWorkenvTestRunnerǁrun_pytest__mutmut_10, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_11': xǁWorkenvTestRunnerǁrun_pytest__mutmut_11, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_12': xǁWorkenvTestRunnerǁrun_pytest__mutmut_12, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_13': xǁWorkenvTestRunnerǁrun_pytest__mutmut_13, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_14': xǁWorkenvTestRunnerǁrun_pytest__mutmut_14, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_15': xǁWorkenvTestRunnerǁrun_pytest__mutmut_15, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_16': xǁWorkenvTestRunnerǁrun_pytest__mutmut_16, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_17': xǁWorkenvTestRunnerǁrun_pytest__mutmut_17, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_18': xǁWorkenvTestRunnerǁrun_pytest__mutmut_18, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_19': xǁWorkenvTestRunnerǁrun_pytest__mutmut_19, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_20': xǁWorkenvTestRunnerǁrun_pytest__mutmut_20, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_21': xǁWorkenvTestRunnerǁrun_pytest__mutmut_21, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_22': xǁWorkenvTestRunnerǁrun_pytest__mutmut_22, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_23': xǁWorkenvTestRunnerǁrun_pytest__mutmut_23, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_24': xǁWorkenvTestRunnerǁrun_pytest__mutmut_24, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_25': xǁWorkenvTestRunnerǁrun_pytest__mutmut_25, 
        'xǁWorkenvTestRunnerǁrun_pytest__mutmut_26': xǁWorkenvTestRunnerǁrun_pytest__mutmut_26
    }
    
    def run_pytest(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvTestRunnerǁrun_pytest__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvTestRunnerǁrun_pytest__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run_pytest.__signature__ = _mutmut_signature(xǁWorkenvTestRunnerǁrun_pytest__mutmut_orig)
    xǁWorkenvTestRunnerǁrun_pytest__mutmut_orig.__name__ = 'xǁWorkenvTestRunnerǁrun_pytest'

    def xǁWorkenvTestRunnerǁrun__mutmut_orig(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)
        return run(cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_1(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = None
        return run(cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_2(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(None)
        return run(cmd, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_3(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)
        return run(None, env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_4(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)
        return run(cmd, env=None, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_5(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)
        return run(env=env, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_6(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)
        return run(cmd, **kwargs)

    def xǁWorkenvTestRunnerǁrun__mutmut_7(self, cmd: list[str], **kwargs: Any) -> CompletedProcess:
        """
        Run any command with the workenv activated.

        Args:
            cmd: Command to run as a list.
            **kwargs: Keyword arguments for subprocess.run.

        Returns:
            CompletedProcess instance with the result.
        """
        env = activate_workenv(self.package_name)
        return run(cmd, env=env, )
    
    xǁWorkenvTestRunnerǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvTestRunnerǁrun__mutmut_1': xǁWorkenvTestRunnerǁrun__mutmut_1, 
        'xǁWorkenvTestRunnerǁrun__mutmut_2': xǁWorkenvTestRunnerǁrun__mutmut_2, 
        'xǁWorkenvTestRunnerǁrun__mutmut_3': xǁWorkenvTestRunnerǁrun__mutmut_3, 
        'xǁWorkenvTestRunnerǁrun__mutmut_4': xǁWorkenvTestRunnerǁrun__mutmut_4, 
        'xǁWorkenvTestRunnerǁrun__mutmut_5': xǁWorkenvTestRunnerǁrun__mutmut_5, 
        'xǁWorkenvTestRunnerǁrun__mutmut_6': xǁWorkenvTestRunnerǁrun__mutmut_6, 
        'xǁWorkenvTestRunnerǁrun__mutmut_7': xǁWorkenvTestRunnerǁrun__mutmut_7
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvTestRunnerǁrun__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvTestRunnerǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁWorkenvTestRunnerǁrun__mutmut_orig)
    xǁWorkenvTestRunnerǁrun__mutmut_orig.__name__ = 'xǁWorkenvTestRunnerǁrun'


def x_pytest_with_workenv__mutmut_orig(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(package_name)
    runner.setup()
    result = runner.run_pytest(*pytest_args, capture_output=False)
    return result.returncode


def x_pytest_with_workenv__mutmut_1(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = None
    runner.setup()
    result = runner.run_pytest(*pytest_args, capture_output=False)
    return result.returncode


def x_pytest_with_workenv__mutmut_2(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(None)
    runner.setup()
    result = runner.run_pytest(*pytest_args, capture_output=False)
    return result.returncode


def x_pytest_with_workenv__mutmut_3(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(package_name)
    runner.setup()
    result = None
    return result.returncode


def x_pytest_with_workenv__mutmut_4(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(package_name)
    runner.setup()
    result = runner.run_pytest(*pytest_args, capture_output=None)
    return result.returncode


def x_pytest_with_workenv__mutmut_5(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(package_name)
    runner.setup()
    result = runner.run_pytest(capture_output=False)
    return result.returncode


def x_pytest_with_workenv__mutmut_6(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(package_name)
    runner.setup()
    result = runner.run_pytest(*pytest_args, )
    return result.returncode


def x_pytest_with_workenv__mutmut_7(package_name: str | None = None, *pytest_args: str) -> int:
    """
    Convenience function to run pytest with workenv activated.

    Args:
        package_name: Optional package name.
        *pytest_args: Arguments to pass to pytest.

    Returns:
        Exit code from pytest.
    """
    runner = WorkenvTestRunner(package_name)
    runner.setup()
    result = runner.run_pytest(*pytest_args, capture_output=True)
    return result.returncode

x_pytest_with_workenv__mutmut_mutants : ClassVar[MutantDict] = {
'x_pytest_with_workenv__mutmut_1': x_pytest_with_workenv__mutmut_1, 
    'x_pytest_with_workenv__mutmut_2': x_pytest_with_workenv__mutmut_2, 
    'x_pytest_with_workenv__mutmut_3': x_pytest_with_workenv__mutmut_3, 
    'x_pytest_with_workenv__mutmut_4': x_pytest_with_workenv__mutmut_4, 
    'x_pytest_with_workenv__mutmut_5': x_pytest_with_workenv__mutmut_5, 
    'x_pytest_with_workenv__mutmut_6': x_pytest_with_workenv__mutmut_6, 
    'x_pytest_with_workenv__mutmut_7': x_pytest_with_workenv__mutmut_7
}

def pytest_with_workenv(*args, **kwargs):
    result = _mutmut_trampoline(x_pytest_with_workenv__mutmut_orig, x_pytest_with_workenv__mutmut_mutants, args, kwargs)
    return result 

pytest_with_workenv.__signature__ = _mutmut_signature(x_pytest_with_workenv__mutmut_orig)
x_pytest_with_workenv__mutmut_orig.__name__ = 'x_pytest_with_workenv'


# 🧰🌍🔚
