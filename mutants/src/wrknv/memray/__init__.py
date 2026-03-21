#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Memray memory profiling suite for wrknv-managed projects.

Provides reusable fixtures, baseline management, and scaffold tooling
for integrating memray stress tests into any provide.io project.

Usage:
    # In your tests/memray/conftest.py:
    from wrknv.memray.fixtures import *  # noqa: F401, F403

    # In your wrknv.toml:
    [tasks.memray]
    _default = "pytest tests/memray/ -m memray -v --no-cov"
    baseline = "MEMRAY_UPDATE_BASELINE=1 pytest tests/memray/ -m memray -v --no-cov"
"""

from wrknv.memray.baselines import (
    assert_allocation_within_threshold,
    load_baselines,
    parse_total_allocations,
    update_baseline,
)
from wrknv.memray.fixtures import memray_baseline, memray_output_dir

__all__ = [
    "assert_allocation_within_threshold",
    "load_baselines",
    "memray_baseline",
    "memray_output_dir",
    "parse_total_allocations",
    "update_baseline",
]
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

# 🧰🌍🔚
