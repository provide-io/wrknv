#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Memray stress test runner for pytest integration.

Provides a helper to run a script under memray, collect stats, and
assert against baselines — all from a single function call in a test.

Usage in a pytest test::

    from wrknv.memray.runner import run_memray_stress

    def test_my_allocations(memray_output_dir, memray_baseline, memray_baselines_path):
        run_memray_stress(
            script="scripts/memray_my_stress.py",
            baseline_key="my_total_allocations",
            output_dir=memray_output_dir,
            baselines=memray_baseline,
            baselines_path=memray_baselines_path,
        )
"""

from __future__ import annotations

from pathlib import Path
import subprocess  # nosec
import sys
from typing import Any

from wrknv.memray.baselines import (
    assert_allocation_within_threshold,
    parse_total_allocations,
)


def run_memray_stress(
    script: str | Path,
    baseline_key: str,
    output_dir: Path,
    baselines: dict[str, Any],
    baselines_path: Path,
    output_name: str | None = None,
    threshold: float = 0.15,
    timeout: int = 300,
) -> int:
    """Run a stress script under memray and check allocations against baseline.

    Args:
        script: Path to the stress test script (relative to project root)
        baseline_key: Key in baselines.json for this test
        output_dir: Directory for memray output files
        baselines: Current baselines dict
        baselines_path: Path to baselines.json
        output_name: Name for the output .bin file (default: derived from script name)
        threshold: Allocation regression threshold (default: 15%)
        timeout: Maximum seconds for the stress script (default: 300)

    Returns:
        Total allocation count measured

    Raises:
        AssertionError: If allocations exceed baseline + threshold
    """
    script_path = Path(script)
    if not script_path.is_absolute():
        # Resolve relative to project root
        for candidate in [Path.cwd() / script, Path.cwd().parent / script]:
            if candidate.exists():
                script_path = candidate
                break

    if output_name is None:
        output_name = script_path.stem.replace("memray_", "").replace("_stress", "")

    output_file = output_dir / f"{output_name}_stress.bin"

    # Run script under memray
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "memray",
            "run",
            "--output",
            str(output_file),
            "--force",
            str(script_path),
        ],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    assert result.returncode == 0, f"Stress script failed:\n{result.stderr}"

    # Get stats
    stats_result = subprocess.run(
        [sys.executable, "-m", "memray", "stats", str(output_file)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert stats_result.returncode == 0, f"memray stats failed:\n{stats_result.stderr}"

    total_allocs = parse_total_allocations(stats_result.stdout)
    assert total_allocs > 0, f"Could not parse allocations from memray stats:\n{stats_result.stdout}"

    # Check against baseline
    assert_allocation_within_threshold(
        baseline_key=baseline_key,
        measured_allocations=total_allocs,
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


# 🧰🌍🔚
