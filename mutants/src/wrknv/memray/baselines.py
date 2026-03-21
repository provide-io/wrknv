#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Baseline management for memray allocation regression testing.

Provides functions to load, update, compare, and assert allocation
baselines stored in a project's tests/memray/baselines.json.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
from typing import Any

import pytest

# Default tolerance: 15% above baseline triggers regression
DEFAULT_ALLOCATION_THRESHOLD = 0.15
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


def x_load_baselines__mutmut_orig(baselines_path: Path) -> dict[str, Any]:
    """Load baselines from a JSON file.

    Args:
        baselines_path: Path to baselines.json

    Returns:
        Dictionary of baseline key -> allocation count
    """
    if baselines_path.exists():
        return json.loads(baselines_path.read_text())
    return {}


def x_load_baselines__mutmut_1(baselines_path: Path) -> dict[str, Any]:
    """Load baselines from a JSON file.

    Args:
        baselines_path: Path to baselines.json

    Returns:
        Dictionary of baseline key -> allocation count
    """
    if baselines_path.exists():
        return json.loads(None)
    return {}

x_load_baselines__mutmut_mutants : ClassVar[MutantDict] = {
'x_load_baselines__mutmut_1': x_load_baselines__mutmut_1
}

def load_baselines(*args, **kwargs):
    result = _mutmut_trampoline(x_load_baselines__mutmut_orig, x_load_baselines__mutmut_mutants, args, kwargs)
    return result 

load_baselines.__signature__ = _mutmut_signature(x_load_baselines__mutmut_orig)
x_load_baselines__mutmut_orig.__name__ = 'x_load_baselines'


def x_update_baseline__mutmut_orig(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_1(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = None
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_2(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = None
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_3(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(None)
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_4(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = None
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_5(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(None)


def x_update_baseline__mutmut_6(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) - "\n")


def x_update_baseline__mutmut_7(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(None, indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_8(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=None, sort_keys=True) + "\n")


def x_update_baseline__mutmut_9(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=None) + "\n")


def x_update_baseline__mutmut_10(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(indent=2, sort_keys=True) + "\n")


def x_update_baseline__mutmut_11(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, sort_keys=True) + "\n")


def x_update_baseline__mutmut_12(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, ) + "\n")


def x_update_baseline__mutmut_13(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=3, sort_keys=True) + "\n")


def x_update_baseline__mutmut_14(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=False) + "\n")


def x_update_baseline__mutmut_15(baselines_path: Path, key: str, value: int) -> None:
    """Update a single baseline value in baselines.json.

    Reads existing baselines, updates the key, and writes back atomically.

    Args:
        baselines_path: Path to baselines.json
        key: Baseline key (e.g., "logging_total_allocations")
        value: Measured allocation count
    """
    baselines: dict[str, Any] = {}
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text())
    baselines[key] = value
    baselines_path.write_text(json.dumps(baselines, indent=2, sort_keys=True) + "XX\nXX")

x_update_baseline__mutmut_mutants : ClassVar[MutantDict] = {
'x_update_baseline__mutmut_1': x_update_baseline__mutmut_1, 
    'x_update_baseline__mutmut_2': x_update_baseline__mutmut_2, 
    'x_update_baseline__mutmut_3': x_update_baseline__mutmut_3, 
    'x_update_baseline__mutmut_4': x_update_baseline__mutmut_4, 
    'x_update_baseline__mutmut_5': x_update_baseline__mutmut_5, 
    'x_update_baseline__mutmut_6': x_update_baseline__mutmut_6, 
    'x_update_baseline__mutmut_7': x_update_baseline__mutmut_7, 
    'x_update_baseline__mutmut_8': x_update_baseline__mutmut_8, 
    'x_update_baseline__mutmut_9': x_update_baseline__mutmut_9, 
    'x_update_baseline__mutmut_10': x_update_baseline__mutmut_10, 
    'x_update_baseline__mutmut_11': x_update_baseline__mutmut_11, 
    'x_update_baseline__mutmut_12': x_update_baseline__mutmut_12, 
    'x_update_baseline__mutmut_13': x_update_baseline__mutmut_13, 
    'x_update_baseline__mutmut_14': x_update_baseline__mutmut_14, 
    'x_update_baseline__mutmut_15': x_update_baseline__mutmut_15
}

def update_baseline(*args, **kwargs):
    result = _mutmut_trampoline(x_update_baseline__mutmut_orig, x_update_baseline__mutmut_mutants, args, kwargs)
    return result 

update_baseline.__signature__ = _mutmut_signature(x_update_baseline__mutmut_orig)
x_update_baseline__mutmut_orig.__name__ = 'x_update_baseline'


def x_assert_allocation_within_threshold__mutmut_orig(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_1(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = None

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_2(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get(None) == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_3(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("XXMEMRAY_UPDATE_BASELINEXX") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_4(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("memray_update_baseline") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_5(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") != "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_6(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "XX1XX"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_7(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update and baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_8(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_9(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(None, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_10(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, None, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_11(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, None)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_12(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_13(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_14(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, )
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_15(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_16(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(None)
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_17(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = None
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_18(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = None

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_19(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(None)

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_20(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected / (1 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_21(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 - threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_22(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (2 + threshold))

    assert measured_allocations <= max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )


def x_assert_allocation_within_threshold__mutmut_23(
    baseline_key: str,
    measured_allocations: int,
    baselines: dict[str, Any],
    baselines_path: Path,
    threshold: float = DEFAULT_ALLOCATION_THRESHOLD,
) -> None:
    """Assert that measured allocations are within threshold of baseline.

    On first run (no baseline exists), records the baseline and skips.
    If MEMRAY_UPDATE_BASELINE=1 is set, updates the baseline silently.

    Args:
        baseline_key: Key to look up/store in baselines.json
        measured_allocations: Current allocation count
        baselines: Current baselines dict
        baselines_path: Path to baselines.json (for updates)
        threshold: Allowed regression fraction (default 0.15 = 15%)
    """
    should_update = os.environ.get("MEMRAY_UPDATE_BASELINE") == "1"

    if should_update or baseline_key not in baselines:
        update_baseline(baselines_path, baseline_key, measured_allocations)
        if baseline_key not in baselines:
            pytest.skip(f"First run — recorded baseline for {baseline_key}: {measured_allocations}")
        return

    expected = baselines[baseline_key]
    max_allowed = int(expected * (1 + threshold))

    assert measured_allocations < max_allowed, (
        f"Allocation regression for {baseline_key}: "
        f"measured {measured_allocations:,} > allowed {max_allowed:,} "
        f"(baseline {expected:,} + {threshold:.0%} threshold)"
    )

x_assert_allocation_within_threshold__mutmut_mutants : ClassVar[MutantDict] = {
'x_assert_allocation_within_threshold__mutmut_1': x_assert_allocation_within_threshold__mutmut_1, 
    'x_assert_allocation_within_threshold__mutmut_2': x_assert_allocation_within_threshold__mutmut_2, 
    'x_assert_allocation_within_threshold__mutmut_3': x_assert_allocation_within_threshold__mutmut_3, 
    'x_assert_allocation_within_threshold__mutmut_4': x_assert_allocation_within_threshold__mutmut_4, 
    'x_assert_allocation_within_threshold__mutmut_5': x_assert_allocation_within_threshold__mutmut_5, 
    'x_assert_allocation_within_threshold__mutmut_6': x_assert_allocation_within_threshold__mutmut_6, 
    'x_assert_allocation_within_threshold__mutmut_7': x_assert_allocation_within_threshold__mutmut_7, 
    'x_assert_allocation_within_threshold__mutmut_8': x_assert_allocation_within_threshold__mutmut_8, 
    'x_assert_allocation_within_threshold__mutmut_9': x_assert_allocation_within_threshold__mutmut_9, 
    'x_assert_allocation_within_threshold__mutmut_10': x_assert_allocation_within_threshold__mutmut_10, 
    'x_assert_allocation_within_threshold__mutmut_11': x_assert_allocation_within_threshold__mutmut_11, 
    'x_assert_allocation_within_threshold__mutmut_12': x_assert_allocation_within_threshold__mutmut_12, 
    'x_assert_allocation_within_threshold__mutmut_13': x_assert_allocation_within_threshold__mutmut_13, 
    'x_assert_allocation_within_threshold__mutmut_14': x_assert_allocation_within_threshold__mutmut_14, 
    'x_assert_allocation_within_threshold__mutmut_15': x_assert_allocation_within_threshold__mutmut_15, 
    'x_assert_allocation_within_threshold__mutmut_16': x_assert_allocation_within_threshold__mutmut_16, 
    'x_assert_allocation_within_threshold__mutmut_17': x_assert_allocation_within_threshold__mutmut_17, 
    'x_assert_allocation_within_threshold__mutmut_18': x_assert_allocation_within_threshold__mutmut_18, 
    'x_assert_allocation_within_threshold__mutmut_19': x_assert_allocation_within_threshold__mutmut_19, 
    'x_assert_allocation_within_threshold__mutmut_20': x_assert_allocation_within_threshold__mutmut_20, 
    'x_assert_allocation_within_threshold__mutmut_21': x_assert_allocation_within_threshold__mutmut_21, 
    'x_assert_allocation_within_threshold__mutmut_22': x_assert_allocation_within_threshold__mutmut_22, 
    'x_assert_allocation_within_threshold__mutmut_23': x_assert_allocation_within_threshold__mutmut_23
}

def assert_allocation_within_threshold(*args, **kwargs):
    result = _mutmut_trampoline(x_assert_allocation_within_threshold__mutmut_orig, x_assert_allocation_within_threshold__mutmut_mutants, args, kwargs)
    return result 

assert_allocation_within_threshold.__signature__ = _mutmut_signature(x_assert_allocation_within_threshold__mutmut_orig)
x_assert_allocation_within_threshold__mutmut_orig.__name__ = 'x_assert_allocation_within_threshold'


def x_parse_total_allocations__mutmut_orig(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_1(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = None
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_2(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(None):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_3(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() or i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_4(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "XXtotal allocationsXX" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_5(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "TOTAL ALLOCATIONS" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_6(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" not in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_7(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.upper() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_8(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i - 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_9(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 2 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_10(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 <= len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_11(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = None
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_12(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(None, lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_13(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", None)
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_14(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_15(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", )
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_16(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"XX(\d[\d,]*)XX", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_17(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i - 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_18(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 2])
            if match:
                return int(match.group(1).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_19(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(None)
    return 0


def x_parse_total_allocations__mutmut_20(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(None, ""))
    return 0


def x_parse_total_allocations__mutmut_21(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", None))
    return 0


def x_parse_total_allocations__mutmut_22(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(""))
    return 0


def x_parse_total_allocations__mutmut_23(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ))
    return 0


def x_parse_total_allocations__mutmut_24(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(None).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_25(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(2).replace(",", ""))
    return 0


def x_parse_total_allocations__mutmut_26(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace("XX,XX", ""))
    return 0


def x_parse_total_allocations__mutmut_27(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", "XXXX"))
    return 0


def x_parse_total_allocations__mutmut_28(stats_output: str) -> int:
    """Extract total allocation count from memray stats output.

    Memray stats format uses label on one line, value on the next::

        Total allocations:
            3878431

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total allocation count, or 0 if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total allocations" in line.lower() and i + 1 < len(lines):
            match = re.search(r"(\d[\d,]*)", lines[i + 1])
            if match:
                return int(match.group(1).replace(",", ""))
    return 1

x_parse_total_allocations__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_total_allocations__mutmut_1': x_parse_total_allocations__mutmut_1, 
    'x_parse_total_allocations__mutmut_2': x_parse_total_allocations__mutmut_2, 
    'x_parse_total_allocations__mutmut_3': x_parse_total_allocations__mutmut_3, 
    'x_parse_total_allocations__mutmut_4': x_parse_total_allocations__mutmut_4, 
    'x_parse_total_allocations__mutmut_5': x_parse_total_allocations__mutmut_5, 
    'x_parse_total_allocations__mutmut_6': x_parse_total_allocations__mutmut_6, 
    'x_parse_total_allocations__mutmut_7': x_parse_total_allocations__mutmut_7, 
    'x_parse_total_allocations__mutmut_8': x_parse_total_allocations__mutmut_8, 
    'x_parse_total_allocations__mutmut_9': x_parse_total_allocations__mutmut_9, 
    'x_parse_total_allocations__mutmut_10': x_parse_total_allocations__mutmut_10, 
    'x_parse_total_allocations__mutmut_11': x_parse_total_allocations__mutmut_11, 
    'x_parse_total_allocations__mutmut_12': x_parse_total_allocations__mutmut_12, 
    'x_parse_total_allocations__mutmut_13': x_parse_total_allocations__mutmut_13, 
    'x_parse_total_allocations__mutmut_14': x_parse_total_allocations__mutmut_14, 
    'x_parse_total_allocations__mutmut_15': x_parse_total_allocations__mutmut_15, 
    'x_parse_total_allocations__mutmut_16': x_parse_total_allocations__mutmut_16, 
    'x_parse_total_allocations__mutmut_17': x_parse_total_allocations__mutmut_17, 
    'x_parse_total_allocations__mutmut_18': x_parse_total_allocations__mutmut_18, 
    'x_parse_total_allocations__mutmut_19': x_parse_total_allocations__mutmut_19, 
    'x_parse_total_allocations__mutmut_20': x_parse_total_allocations__mutmut_20, 
    'x_parse_total_allocations__mutmut_21': x_parse_total_allocations__mutmut_21, 
    'x_parse_total_allocations__mutmut_22': x_parse_total_allocations__mutmut_22, 
    'x_parse_total_allocations__mutmut_23': x_parse_total_allocations__mutmut_23, 
    'x_parse_total_allocations__mutmut_24': x_parse_total_allocations__mutmut_24, 
    'x_parse_total_allocations__mutmut_25': x_parse_total_allocations__mutmut_25, 
    'x_parse_total_allocations__mutmut_26': x_parse_total_allocations__mutmut_26, 
    'x_parse_total_allocations__mutmut_27': x_parse_total_allocations__mutmut_27, 
    'x_parse_total_allocations__mutmut_28': x_parse_total_allocations__mutmut_28
}

def parse_total_allocations(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_total_allocations__mutmut_orig, x_parse_total_allocations__mutmut_mutants, args, kwargs)
    return result 

parse_total_allocations.__signature__ = _mutmut_signature(x_parse_total_allocations__mutmut_orig)
x_parse_total_allocations__mutmut_orig.__name__ = 'x_parse_total_allocations'


def x_parse_peak_memory__mutmut_orig(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_1(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = None
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_2(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(None):
        if "peak memory" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_3(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() or i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_4(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "XXpeak memoryXX" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_5(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "PEAK MEMORY" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_6(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" not in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_7(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.upper() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_8(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i - 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_9(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 2 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_10(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 1 <= len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_peak_memory__mutmut_11(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 1 < len(lines):
            return lines[i - 1].strip()
    return ""


def x_parse_peak_memory__mutmut_12(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 1 < len(lines):
            return lines[i + 2].strip()
    return ""


def x_parse_peak_memory__mutmut_13(stats_output: str) -> str:
    """Extract peak memory usage from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Peak memory string (e.g., "44.394MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "peak memory" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return "XXXX"

x_parse_peak_memory__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_peak_memory__mutmut_1': x_parse_peak_memory__mutmut_1, 
    'x_parse_peak_memory__mutmut_2': x_parse_peak_memory__mutmut_2, 
    'x_parse_peak_memory__mutmut_3': x_parse_peak_memory__mutmut_3, 
    'x_parse_peak_memory__mutmut_4': x_parse_peak_memory__mutmut_4, 
    'x_parse_peak_memory__mutmut_5': x_parse_peak_memory__mutmut_5, 
    'x_parse_peak_memory__mutmut_6': x_parse_peak_memory__mutmut_6, 
    'x_parse_peak_memory__mutmut_7': x_parse_peak_memory__mutmut_7, 
    'x_parse_peak_memory__mutmut_8': x_parse_peak_memory__mutmut_8, 
    'x_parse_peak_memory__mutmut_9': x_parse_peak_memory__mutmut_9, 
    'x_parse_peak_memory__mutmut_10': x_parse_peak_memory__mutmut_10, 
    'x_parse_peak_memory__mutmut_11': x_parse_peak_memory__mutmut_11, 
    'x_parse_peak_memory__mutmut_12': x_parse_peak_memory__mutmut_12, 
    'x_parse_peak_memory__mutmut_13': x_parse_peak_memory__mutmut_13
}

def parse_peak_memory(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_peak_memory__mutmut_orig, x_parse_peak_memory__mutmut_mutants, args, kwargs)
    return result 

parse_peak_memory.__signature__ = _mutmut_signature(x_parse_peak_memory__mutmut_orig)
x_parse_peak_memory__mutmut_orig.__name__ = 'x_parse_peak_memory'


def x_parse_total_memory__mutmut_orig(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_1(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = None
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_2(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(None):
        if "total memory allocated" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_3(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() or i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_4(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "XXtotal memory allocatedXX" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_5(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "TOTAL MEMORY ALLOCATED" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_6(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" not in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_7(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.upper() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_8(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i - 1 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_9(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 2 < len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_10(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 1 <= len(lines):
            return lines[i + 1].strip()
    return ""


def x_parse_total_memory__mutmut_11(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 1 < len(lines):
            return lines[i - 1].strip()
    return ""


def x_parse_total_memory__mutmut_12(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 1 < len(lines):
            return lines[i + 2].strip()
    return ""


def x_parse_total_memory__mutmut_13(stats_output: str) -> str:
    """Extract total memory allocated from memray stats output.

    Args:
        stats_output: Raw stdout from ``memray stats``

    Returns:
        Total memory string (e.g., "569.040MB"), or "" if parsing fails
    """
    lines = stats_output.splitlines()
    for i, line in enumerate(lines):
        if "total memory allocated" in line.lower() and i + 1 < len(lines):
            return lines[i + 1].strip()
    return "XXXX"

x_parse_total_memory__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_total_memory__mutmut_1': x_parse_total_memory__mutmut_1, 
    'x_parse_total_memory__mutmut_2': x_parse_total_memory__mutmut_2, 
    'x_parse_total_memory__mutmut_3': x_parse_total_memory__mutmut_3, 
    'x_parse_total_memory__mutmut_4': x_parse_total_memory__mutmut_4, 
    'x_parse_total_memory__mutmut_5': x_parse_total_memory__mutmut_5, 
    'x_parse_total_memory__mutmut_6': x_parse_total_memory__mutmut_6, 
    'x_parse_total_memory__mutmut_7': x_parse_total_memory__mutmut_7, 
    'x_parse_total_memory__mutmut_8': x_parse_total_memory__mutmut_8, 
    'x_parse_total_memory__mutmut_9': x_parse_total_memory__mutmut_9, 
    'x_parse_total_memory__mutmut_10': x_parse_total_memory__mutmut_10, 
    'x_parse_total_memory__mutmut_11': x_parse_total_memory__mutmut_11, 
    'x_parse_total_memory__mutmut_12': x_parse_total_memory__mutmut_12, 
    'x_parse_total_memory__mutmut_13': x_parse_total_memory__mutmut_13
}

def parse_total_memory(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_total_memory__mutmut_orig, x_parse_total_memory__mutmut_mutants, args, kwargs)
    return result 

parse_total_memory.__signature__ = _mutmut_signature(x_parse_total_memory__mutmut_orig)
x_parse_total_memory__mutmut_orig.__name__ = 'x_parse_total_memory'


# 🧰🌍🔚
