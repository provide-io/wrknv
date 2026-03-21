#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Reusable pytest fixtures for memray stress tests.

Import these in your project's tests/memray/conftest.py::

    from wrknv.memray.fixtures import *  # noqa: F401, F403

This provides:
    - memray_output_dir: Path to memray-output/ (auto-created)
    - memray_baseline: Current baselines dict from baselines.json
    - memray_baselines_path: Path to baselines.json
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from wrknv.memray.baselines import load_baselines
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


def x__find_project_root__mutmut_orig() -> Path:
    """Walk up from CWD to find the project root (contains pyproject.toml)."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    return current


def x__find_project_root__mutmut_1() -> Path:
    """Walk up from CWD to find the project root (contains pyproject.toml)."""
    current = None
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    return current


def x__find_project_root__mutmut_2() -> Path:
    """Walk up from CWD to find the project root (contains pyproject.toml)."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent * "pyproject.toml").exists():
            return parent
    return current


def x__find_project_root__mutmut_3() -> Path:
    """Walk up from CWD to find the project root (contains pyproject.toml)."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "XXpyproject.tomlXX").exists():
            return parent
    return current


def x__find_project_root__mutmut_4() -> Path:
    """Walk up from CWD to find the project root (contains pyproject.toml)."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "PYPROJECT.TOML").exists():
            return parent
    return current

x__find_project_root__mutmut_mutants : ClassVar[MutantDict] = {
'x__find_project_root__mutmut_1': x__find_project_root__mutmut_1, 
    'x__find_project_root__mutmut_2': x__find_project_root__mutmut_2, 
    'x__find_project_root__mutmut_3': x__find_project_root__mutmut_3, 
    'x__find_project_root__mutmut_4': x__find_project_root__mutmut_4
}

def _find_project_root(*args, **kwargs):
    result = _mutmut_trampoline(x__find_project_root__mutmut_orig, x__find_project_root__mutmut_mutants, args, kwargs)
    return result 

_find_project_root.__signature__ = _mutmut_signature(x__find_project_root__mutmut_orig)
x__find_project_root__mutmut_orig.__name__ = 'x__find_project_root'


@pytest.fixture
def memray_output_dir() -> Path:
    """Return the memray output directory, creating it if needed."""
    output_dir = _find_project_root() / "memray-output"
    output_dir.mkdir(exist_ok=True)
    return output_dir


@pytest.fixture
def memray_baselines_path() -> Path:
    """Return the path to baselines.json."""
    return _find_project_root() / "tests" / "memray" / "baselines.json"


@pytest.fixture
def memray_baseline(memray_baselines_path: Path) -> dict[str, Any]:
    """Load the current baselines from baselines.json."""
    return load_baselines(memray_baselines_path)


# 🧰🌍🔚
