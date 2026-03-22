#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Workenv Bin Management
======================
General utilities for managing workenv bin directories and tool binaries."""

from __future__ import annotations

import os
import pathlib
import shutil
import sys
from typing import Any

from provide.foundation import logger
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


def x_get_workenv_bin_dir__mutmut_orig(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_1(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = None
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_2(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(None)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_3(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = ""

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_4(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") and (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_5(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(None, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_6(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, None) or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_7(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr("real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_8(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, ) or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_9(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "XXreal_prefixXX") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_10(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "REAL_PREFIX") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_11(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") or sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_12(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(None, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_13(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, None) and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_14(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr("base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_15(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, ) and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_16(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "XXbase_prefixXX") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_17(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "BASE_PREFIX") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_18(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix == sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_19(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = None
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_20(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path * ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_21(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("XXScriptsXX" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_22(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_23(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("SCRIPTS" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_24(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name != "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_25(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "XXntXX" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_26(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "NT" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_27(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "XXbinXX")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_28(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "BIN")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_29(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = None
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_30(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = ""
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_31(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_32(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = None
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_33(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(None, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_34(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, None, None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_35(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr("get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_36(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_37(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", )
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_38(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "XXget_workenv_dir_nameXX", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_39(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "GET_WORKENV_DIR_NAME", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_40(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(None):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_41(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = None
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_42(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = None

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_43(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(None, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_44(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, None, None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_45(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr("workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_46(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_47(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", )

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_48(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "XXworkenv_dir_nameXX", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_49(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "WORKENV_DIR_NAME", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_50(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = None
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_51(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name * "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_52(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root * workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_53(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "XXbinXX"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_54(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "BIN"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_55(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = None

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_56(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" * "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_57(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() * ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_58(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / "XX.localXX" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_59(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".LOCAL" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_60(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "XXbinXX"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_61(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "BIN"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_62(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=None, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_63(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=None)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_64(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_65(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, )
    return bin_dir


def x_get_workenv_bin_dir__mutmut_66(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=False, exist_ok=True)
    return bin_dir


def x_get_workenv_bin_dir__mutmut_67(config: Any | None) -> pathlib.Path:
    """Get the workenv bin directory (or fallback location).

    Priority:
    1. If in a workenv virtualenv -> workenv/bin
    2. If in a regular venv -> venv/bin
    3. If not in venv, find workenv relative to project root
    4. Fallback to ~/.local/bin
    """
    venv_path = pathlib.Path(sys.prefix)
    bin_dir = None

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        # We're in a venv - determine bin directory based on platform
        bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    else:
        # Not in a venv, check for workenv directory relative to project root
        project_root = find_project_root()
        if project_root:
            workenv_dir_name = None
            if config is not None:
                get_dir_name = getattr(config, "get_workenv_dir_name", None)
                if callable(get_dir_name):
                    workenv_dir_name = get_dir_name()
                else:
                    workenv_dir_name = getattr(config, "workenv_dir_name", None)

            if workenv_dir_name:
                workenv_bin: pathlib.Path = project_root / workenv_dir_name / "bin"
                if workenv_bin.exists():
                    return workenv_bin

        # Fallback to .local/bin
        bin_dir = pathlib.Path.home() / ".local" / "bin"

    # Ensure directory exists
    bin_dir.mkdir(parents=True, exist_ok=False)
    return bin_dir

x_get_workenv_bin_dir__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_workenv_bin_dir__mutmut_1': x_get_workenv_bin_dir__mutmut_1, 
    'x_get_workenv_bin_dir__mutmut_2': x_get_workenv_bin_dir__mutmut_2, 
    'x_get_workenv_bin_dir__mutmut_3': x_get_workenv_bin_dir__mutmut_3, 
    'x_get_workenv_bin_dir__mutmut_4': x_get_workenv_bin_dir__mutmut_4, 
    'x_get_workenv_bin_dir__mutmut_5': x_get_workenv_bin_dir__mutmut_5, 
    'x_get_workenv_bin_dir__mutmut_6': x_get_workenv_bin_dir__mutmut_6, 
    'x_get_workenv_bin_dir__mutmut_7': x_get_workenv_bin_dir__mutmut_7, 
    'x_get_workenv_bin_dir__mutmut_8': x_get_workenv_bin_dir__mutmut_8, 
    'x_get_workenv_bin_dir__mutmut_9': x_get_workenv_bin_dir__mutmut_9, 
    'x_get_workenv_bin_dir__mutmut_10': x_get_workenv_bin_dir__mutmut_10, 
    'x_get_workenv_bin_dir__mutmut_11': x_get_workenv_bin_dir__mutmut_11, 
    'x_get_workenv_bin_dir__mutmut_12': x_get_workenv_bin_dir__mutmut_12, 
    'x_get_workenv_bin_dir__mutmut_13': x_get_workenv_bin_dir__mutmut_13, 
    'x_get_workenv_bin_dir__mutmut_14': x_get_workenv_bin_dir__mutmut_14, 
    'x_get_workenv_bin_dir__mutmut_15': x_get_workenv_bin_dir__mutmut_15, 
    'x_get_workenv_bin_dir__mutmut_16': x_get_workenv_bin_dir__mutmut_16, 
    'x_get_workenv_bin_dir__mutmut_17': x_get_workenv_bin_dir__mutmut_17, 
    'x_get_workenv_bin_dir__mutmut_18': x_get_workenv_bin_dir__mutmut_18, 
    'x_get_workenv_bin_dir__mutmut_19': x_get_workenv_bin_dir__mutmut_19, 
    'x_get_workenv_bin_dir__mutmut_20': x_get_workenv_bin_dir__mutmut_20, 
    'x_get_workenv_bin_dir__mutmut_21': x_get_workenv_bin_dir__mutmut_21, 
    'x_get_workenv_bin_dir__mutmut_22': x_get_workenv_bin_dir__mutmut_22, 
    'x_get_workenv_bin_dir__mutmut_23': x_get_workenv_bin_dir__mutmut_23, 
    'x_get_workenv_bin_dir__mutmut_24': x_get_workenv_bin_dir__mutmut_24, 
    'x_get_workenv_bin_dir__mutmut_25': x_get_workenv_bin_dir__mutmut_25, 
    'x_get_workenv_bin_dir__mutmut_26': x_get_workenv_bin_dir__mutmut_26, 
    'x_get_workenv_bin_dir__mutmut_27': x_get_workenv_bin_dir__mutmut_27, 
    'x_get_workenv_bin_dir__mutmut_28': x_get_workenv_bin_dir__mutmut_28, 
    'x_get_workenv_bin_dir__mutmut_29': x_get_workenv_bin_dir__mutmut_29, 
    'x_get_workenv_bin_dir__mutmut_30': x_get_workenv_bin_dir__mutmut_30, 
    'x_get_workenv_bin_dir__mutmut_31': x_get_workenv_bin_dir__mutmut_31, 
    'x_get_workenv_bin_dir__mutmut_32': x_get_workenv_bin_dir__mutmut_32, 
    'x_get_workenv_bin_dir__mutmut_33': x_get_workenv_bin_dir__mutmut_33, 
    'x_get_workenv_bin_dir__mutmut_34': x_get_workenv_bin_dir__mutmut_34, 
    'x_get_workenv_bin_dir__mutmut_35': x_get_workenv_bin_dir__mutmut_35, 
    'x_get_workenv_bin_dir__mutmut_36': x_get_workenv_bin_dir__mutmut_36, 
    'x_get_workenv_bin_dir__mutmut_37': x_get_workenv_bin_dir__mutmut_37, 
    'x_get_workenv_bin_dir__mutmut_38': x_get_workenv_bin_dir__mutmut_38, 
    'x_get_workenv_bin_dir__mutmut_39': x_get_workenv_bin_dir__mutmut_39, 
    'x_get_workenv_bin_dir__mutmut_40': x_get_workenv_bin_dir__mutmut_40, 
    'x_get_workenv_bin_dir__mutmut_41': x_get_workenv_bin_dir__mutmut_41, 
    'x_get_workenv_bin_dir__mutmut_42': x_get_workenv_bin_dir__mutmut_42, 
    'x_get_workenv_bin_dir__mutmut_43': x_get_workenv_bin_dir__mutmut_43, 
    'x_get_workenv_bin_dir__mutmut_44': x_get_workenv_bin_dir__mutmut_44, 
    'x_get_workenv_bin_dir__mutmut_45': x_get_workenv_bin_dir__mutmut_45, 
    'x_get_workenv_bin_dir__mutmut_46': x_get_workenv_bin_dir__mutmut_46, 
    'x_get_workenv_bin_dir__mutmut_47': x_get_workenv_bin_dir__mutmut_47, 
    'x_get_workenv_bin_dir__mutmut_48': x_get_workenv_bin_dir__mutmut_48, 
    'x_get_workenv_bin_dir__mutmut_49': x_get_workenv_bin_dir__mutmut_49, 
    'x_get_workenv_bin_dir__mutmut_50': x_get_workenv_bin_dir__mutmut_50, 
    'x_get_workenv_bin_dir__mutmut_51': x_get_workenv_bin_dir__mutmut_51, 
    'x_get_workenv_bin_dir__mutmut_52': x_get_workenv_bin_dir__mutmut_52, 
    'x_get_workenv_bin_dir__mutmut_53': x_get_workenv_bin_dir__mutmut_53, 
    'x_get_workenv_bin_dir__mutmut_54': x_get_workenv_bin_dir__mutmut_54, 
    'x_get_workenv_bin_dir__mutmut_55': x_get_workenv_bin_dir__mutmut_55, 
    'x_get_workenv_bin_dir__mutmut_56': x_get_workenv_bin_dir__mutmut_56, 
    'x_get_workenv_bin_dir__mutmut_57': x_get_workenv_bin_dir__mutmut_57, 
    'x_get_workenv_bin_dir__mutmut_58': x_get_workenv_bin_dir__mutmut_58, 
    'x_get_workenv_bin_dir__mutmut_59': x_get_workenv_bin_dir__mutmut_59, 
    'x_get_workenv_bin_dir__mutmut_60': x_get_workenv_bin_dir__mutmut_60, 
    'x_get_workenv_bin_dir__mutmut_61': x_get_workenv_bin_dir__mutmut_61, 
    'x_get_workenv_bin_dir__mutmut_62': x_get_workenv_bin_dir__mutmut_62, 
    'x_get_workenv_bin_dir__mutmut_63': x_get_workenv_bin_dir__mutmut_63, 
    'x_get_workenv_bin_dir__mutmut_64': x_get_workenv_bin_dir__mutmut_64, 
    'x_get_workenv_bin_dir__mutmut_65': x_get_workenv_bin_dir__mutmut_65, 
    'x_get_workenv_bin_dir__mutmut_66': x_get_workenv_bin_dir__mutmut_66, 
    'x_get_workenv_bin_dir__mutmut_67': x_get_workenv_bin_dir__mutmut_67
}

def get_workenv_bin_dir(*args, **kwargs):
    result = _mutmut_trampoline(x_get_workenv_bin_dir__mutmut_orig, x_get_workenv_bin_dir__mutmut_mutants, args, kwargs)
    return result 

get_workenv_bin_dir.__signature__ = _mutmut_signature(x_get_workenv_bin_dir__mutmut_orig)
x_get_workenv_bin_dir__mutmut_orig.__name__ = 'x_get_workenv_bin_dir'


def x_find_project_root__mutmut_orig() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent

    return None


def x_find_project_root__mutmut_1() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = None

    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent

    return None


def x_find_project_root__mutmut_2() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current == current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent

    return None


def x_find_project_root__mutmut_3() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current != current.parent:
        if (current * "pyproject.toml").exists():
            return current
        current = current.parent

    return None


def x_find_project_root__mutmut_4() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current != current.parent:
        if (current / "XXpyproject.tomlXX").exists():
            return current
        current = current.parent

    return None


def x_find_project_root__mutmut_5() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current != current.parent:
        if (current / "PYPROJECT.TOML").exists():
            return current
        current = current.parent

    return None


def x_find_project_root__mutmut_6() -> pathlib.Path | None:
    """Find the project root by looking for pyproject.toml."""
    current = pathlib.Path.cwd()

    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = None

    return None

x_find_project_root__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_project_root__mutmut_1': x_find_project_root__mutmut_1, 
    'x_find_project_root__mutmut_2': x_find_project_root__mutmut_2, 
    'x_find_project_root__mutmut_3': x_find_project_root__mutmut_3, 
    'x_find_project_root__mutmut_4': x_find_project_root__mutmut_4, 
    'x_find_project_root__mutmut_5': x_find_project_root__mutmut_5, 
    'x_find_project_root__mutmut_6': x_find_project_root__mutmut_6
}

def find_project_root(*args, **kwargs):
    result = _mutmut_trampoline(x_find_project_root__mutmut_orig, x_find_project_root__mutmut_mutants, args, kwargs)
    return result 

find_project_root.__signature__ = _mutmut_signature(x_find_project_root__mutmut_orig)
x_find_project_root__mutmut_orig.__name__ = 'x_find_project_root'


def x_copy_tool_binary__mutmut_orig(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_1(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_2(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(None)
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_3(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return True

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_4(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name != "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_5(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "XXntXX":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_6(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "NT":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_7(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name = ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_8(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name -= ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_9(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += "XX.exeXX"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_10(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".EXE"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_11(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = None

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_12(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir * target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_13(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(None, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_14(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, None)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_15(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_16(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, )

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_17(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name == "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_18(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "XXntXX":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_19(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "NT":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_20(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(None)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_21(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(494)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_22(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(None)
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_23(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return False

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return False


def x_copy_tool_binary__mutmut_24(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(None)
        return False


def x_copy_tool_binary__mutmut_25(source_path: pathlib.Path, target_name: str, bin_dir: pathlib.Path) -> bool:
    """Copy a tool binary to the bin directory.

    Args:
        source_path: Path to source binary
        target_name: Name for target binary (without .exe)
        bin_dir: Destination bin directory

    Returns:
        True if successful, False otherwise
    """
    if not source_path.exists():
        logger.warning(f"Source binary not found: {source_path}")
        return False

    # Add .exe extension on Windows
    if os.name == "nt":
        target_name += ".exe"

    target_path = bin_dir / target_name

    try:
        # Copy the binary
        shutil.copy2(source_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        logger.debug(f"Copied binary to {target_path}")
        return True

    except Exception as e:
        logger.warning(f"Failed to copy binary: {e}")
        return True

x_copy_tool_binary__mutmut_mutants : ClassVar[MutantDict] = {
'x_copy_tool_binary__mutmut_1': x_copy_tool_binary__mutmut_1, 
    'x_copy_tool_binary__mutmut_2': x_copy_tool_binary__mutmut_2, 
    'x_copy_tool_binary__mutmut_3': x_copy_tool_binary__mutmut_3, 
    'x_copy_tool_binary__mutmut_4': x_copy_tool_binary__mutmut_4, 
    'x_copy_tool_binary__mutmut_5': x_copy_tool_binary__mutmut_5, 
    'x_copy_tool_binary__mutmut_6': x_copy_tool_binary__mutmut_6, 
    'x_copy_tool_binary__mutmut_7': x_copy_tool_binary__mutmut_7, 
    'x_copy_tool_binary__mutmut_8': x_copy_tool_binary__mutmut_8, 
    'x_copy_tool_binary__mutmut_9': x_copy_tool_binary__mutmut_9, 
    'x_copy_tool_binary__mutmut_10': x_copy_tool_binary__mutmut_10, 
    'x_copy_tool_binary__mutmut_11': x_copy_tool_binary__mutmut_11, 
    'x_copy_tool_binary__mutmut_12': x_copy_tool_binary__mutmut_12, 
    'x_copy_tool_binary__mutmut_13': x_copy_tool_binary__mutmut_13, 
    'x_copy_tool_binary__mutmut_14': x_copy_tool_binary__mutmut_14, 
    'x_copy_tool_binary__mutmut_15': x_copy_tool_binary__mutmut_15, 
    'x_copy_tool_binary__mutmut_16': x_copy_tool_binary__mutmut_16, 
    'x_copy_tool_binary__mutmut_17': x_copy_tool_binary__mutmut_17, 
    'x_copy_tool_binary__mutmut_18': x_copy_tool_binary__mutmut_18, 
    'x_copy_tool_binary__mutmut_19': x_copy_tool_binary__mutmut_19, 
    'x_copy_tool_binary__mutmut_20': x_copy_tool_binary__mutmut_20, 
    'x_copy_tool_binary__mutmut_21': x_copy_tool_binary__mutmut_21, 
    'x_copy_tool_binary__mutmut_22': x_copy_tool_binary__mutmut_22, 
    'x_copy_tool_binary__mutmut_23': x_copy_tool_binary__mutmut_23, 
    'x_copy_tool_binary__mutmut_24': x_copy_tool_binary__mutmut_24, 
    'x_copy_tool_binary__mutmut_25': x_copy_tool_binary__mutmut_25
}

def copy_tool_binary(*args, **kwargs):
    result = _mutmut_trampoline(x_copy_tool_binary__mutmut_orig, x_copy_tool_binary__mutmut_mutants, args, kwargs)
    return result 

copy_tool_binary.__signature__ = _mutmut_signature(x_copy_tool_binary__mutmut_orig)
x_copy_tool_binary__mutmut_orig.__name__ = 'x_copy_tool_binary'


# 🧰🌍🔚
