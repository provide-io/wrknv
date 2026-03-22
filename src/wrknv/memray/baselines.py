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


def load_baselines(baselines_path: Path) -> dict[str, Any]:
    """Load baselines from a JSON file.

    Args:
        baselines_path: Path to baselines.json

    Returns:
        Dictionary of baseline key -> allocation count
    """
    if baselines_path.exists():
        return dict[str, Any](json.loads(baselines_path.read_text()))
    return {}


def update_baseline(baselines_path: Path, key: str, value: int) -> None:
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


def assert_allocation_within_threshold(
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


def parse_total_allocations(stats_output: str) -> int:
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


def parse_peak_memory(stats_output: str) -> str:
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


def parse_total_memory(stats_output: str) -> str:
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


# 🧰🌍🔚
