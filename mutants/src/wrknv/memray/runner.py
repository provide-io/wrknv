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
import subprocess
import sys
from typing import Any

from wrknv.memray.baselines import (
    assert_allocation_within_threshold,
    parse_total_allocations,
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


def x_run_memray_stress__mutmut_orig(
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


def x_run_memray_stress__mutmut_1(
    script: str | Path,
    baseline_key: str,
    output_dir: Path,
    baselines: dict[str, Any],
    baselines_path: Path,
    output_name: str | None = None,
    threshold: float = 1.15,
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


def x_run_memray_stress__mutmut_2(
    script: str | Path,
    baseline_key: str,
    output_dir: Path,
    baselines: dict[str, Any],
    baselines_path: Path,
    output_name: str | None = None,
    threshold: float = 0.15,
    timeout: int = 301,
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


def x_run_memray_stress__mutmut_3(
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
    script_path = None
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


def x_run_memray_stress__mutmut_4(
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
    script_path = Path(None)
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


def x_run_memray_stress__mutmut_5(
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
    if script_path.is_absolute():
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


def x_run_memray_stress__mutmut_6(
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
        for candidate in [Path.cwd() * script, Path.cwd().parent / script]:
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


def x_run_memray_stress__mutmut_7(
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
        for candidate in [Path.cwd() / script, Path.cwd().parent * script]:
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


def x_run_memray_stress__mutmut_8(
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
                script_path = None
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


def x_run_memray_stress__mutmut_9(
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
                return

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


def x_run_memray_stress__mutmut_10(
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

    if output_name is not None:
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


def x_run_memray_stress__mutmut_11(
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
        output_name = None

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


def x_run_memray_stress__mutmut_12(
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
        output_name = script_path.stem.replace("memray_", "").replace(None, "")

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


def x_run_memray_stress__mutmut_13(
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
        output_name = script_path.stem.replace("memray_", "").replace("_stress", None)

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


def x_run_memray_stress__mutmut_14(
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
        output_name = script_path.stem.replace("memray_", "").replace("")

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


def x_run_memray_stress__mutmut_15(
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
        output_name = script_path.stem.replace("memray_", "").replace("_stress", )

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


def x_run_memray_stress__mutmut_16(
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
        output_name = script_path.stem.replace(None, "").replace("_stress", "")

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


def x_run_memray_stress__mutmut_17(
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
        output_name = script_path.stem.replace("memray_", None).replace("_stress", "")

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


def x_run_memray_stress__mutmut_18(
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
        output_name = script_path.stem.replace("").replace("_stress", "")

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


def x_run_memray_stress__mutmut_19(
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
        output_name = script_path.stem.replace("memray_", ).replace("_stress", "")

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


def x_run_memray_stress__mutmut_20(
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
        output_name = script_path.stem.replace("XXmemray_XX", "").replace("_stress", "")

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


def x_run_memray_stress__mutmut_21(
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
        output_name = script_path.stem.replace("MEMRAY_", "").replace("_stress", "")

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


def x_run_memray_stress__mutmut_22(
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
        output_name = script_path.stem.replace("memray_", "XXXX").replace("_stress", "")

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


def x_run_memray_stress__mutmut_23(
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
        output_name = script_path.stem.replace("memray_", "").replace("XX_stressXX", "")

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


def x_run_memray_stress__mutmut_24(
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
        output_name = script_path.stem.replace("memray_", "").replace("_STRESS", "")

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


def x_run_memray_stress__mutmut_25(
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
        output_name = script_path.stem.replace("memray_", "").replace("_stress", "XXXX")

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


def x_run_memray_stress__mutmut_26(
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

    output_file = None

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


def x_run_memray_stress__mutmut_27(
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

    output_file = output_dir * f"{output_name}_stress.bin"

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


def x_run_memray_stress__mutmut_28(
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
    result = None
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


def x_run_memray_stress__mutmut_29(
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
        None,
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


def x_run_memray_stress__mutmut_30(
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
        capture_output=None,
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


def x_run_memray_stress__mutmut_31(
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
        text=None,
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


def x_run_memray_stress__mutmut_32(
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
        timeout=None,
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


def x_run_memray_stress__mutmut_33(
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


def x_run_memray_stress__mutmut_34(
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


def x_run_memray_stress__mutmut_35(
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


def x_run_memray_stress__mutmut_36(
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


def x_run_memray_stress__mutmut_37(
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
            "XX-mXX",
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


def x_run_memray_stress__mutmut_38(
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
            "-M",
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


def x_run_memray_stress__mutmut_39(
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
            "XXmemrayXX",
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


def x_run_memray_stress__mutmut_40(
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
            "MEMRAY",
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


def x_run_memray_stress__mutmut_41(
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
            "XXrunXX",
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


def x_run_memray_stress__mutmut_42(
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
            "RUN",
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


def x_run_memray_stress__mutmut_43(
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
            "XX--outputXX",
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


def x_run_memray_stress__mutmut_44(
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
            "--OUTPUT",
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


def x_run_memray_stress__mutmut_45(
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
            str(None),
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


def x_run_memray_stress__mutmut_46(
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
            "XX--forceXX",
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


def x_run_memray_stress__mutmut_47(
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
            "--FORCE",
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


def x_run_memray_stress__mutmut_48(
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
            str(None),
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


def x_run_memray_stress__mutmut_49(
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
        capture_output=False,
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


def x_run_memray_stress__mutmut_50(
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
        text=False,
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


def x_run_memray_stress__mutmut_51(
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
    assert result.returncode != 0, f"Stress script failed:\n{result.stderr}"

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


def x_run_memray_stress__mutmut_52(
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
    assert result.returncode == 1, f"Stress script failed:\n{result.stderr}"

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


def x_run_memray_stress__mutmut_53(
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
    stats_result = None
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


def x_run_memray_stress__mutmut_54(
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
        None,
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


def x_run_memray_stress__mutmut_55(
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
        capture_output=None,
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


def x_run_memray_stress__mutmut_56(
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
        text=None,
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


def x_run_memray_stress__mutmut_57(
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
        timeout=None,
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


def x_run_memray_stress__mutmut_58(
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


def x_run_memray_stress__mutmut_59(
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


def x_run_memray_stress__mutmut_60(
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


def x_run_memray_stress__mutmut_61(
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


def x_run_memray_stress__mutmut_62(
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
        [sys.executable, "XX-mXX", "memray", "stats", str(output_file)],
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


def x_run_memray_stress__mutmut_63(
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
        [sys.executable, "-M", "memray", "stats", str(output_file)],
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


def x_run_memray_stress__mutmut_64(
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
        [sys.executable, "-m", "XXmemrayXX", "stats", str(output_file)],
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


def x_run_memray_stress__mutmut_65(
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
        [sys.executable, "-m", "MEMRAY", "stats", str(output_file)],
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


def x_run_memray_stress__mutmut_66(
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
        [sys.executable, "-m", "memray", "XXstatsXX", str(output_file)],
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


def x_run_memray_stress__mutmut_67(
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
        [sys.executable, "-m", "memray", "STATS", str(output_file)],
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


def x_run_memray_stress__mutmut_68(
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
        [sys.executable, "-m", "memray", "stats", str(None)],
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


def x_run_memray_stress__mutmut_69(
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
        capture_output=False,
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


def x_run_memray_stress__mutmut_70(
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
        text=False,
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


def x_run_memray_stress__mutmut_71(
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
        timeout=61,
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


def x_run_memray_stress__mutmut_72(
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
    assert stats_result.returncode != 0, f"memray stats failed:\n{stats_result.stderr}"

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


def x_run_memray_stress__mutmut_73(
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
    assert stats_result.returncode == 1, f"memray stats failed:\n{stats_result.stderr}"

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


def x_run_memray_stress__mutmut_74(
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

    total_allocs = None
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


def x_run_memray_stress__mutmut_75(
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

    total_allocs = parse_total_allocations(None)
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


def x_run_memray_stress__mutmut_76(
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
    assert total_allocs >= 0, f"Could not parse allocations from memray stats:\n{stats_result.stdout}"

    # Check against baseline
    assert_allocation_within_threshold(
        baseline_key=baseline_key,
        measured_allocations=total_allocs,
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_77(
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
    assert total_allocs > 1, f"Could not parse allocations from memray stats:\n{stats_result.stdout}"

    # Check against baseline
    assert_allocation_within_threshold(
        baseline_key=baseline_key,
        measured_allocations=total_allocs,
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_78(
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
        baseline_key=None,
        measured_allocations=total_allocs,
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_79(
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
        measured_allocations=None,
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_80(
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
        baselines=None,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_81(
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
        baselines_path=None,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_82(
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
        threshold=None,
    )

    return total_allocs


def x_run_memray_stress__mutmut_83(
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
        measured_allocations=total_allocs,
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_84(
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
        baselines=baselines,
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_85(
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
        baselines_path=baselines_path,
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_86(
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
        threshold=threshold,
    )

    return total_allocs


def x_run_memray_stress__mutmut_87(
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
        )

    return total_allocs

x_run_memray_stress__mutmut_mutants : ClassVar[MutantDict] = {
'x_run_memray_stress__mutmut_1': x_run_memray_stress__mutmut_1, 
    'x_run_memray_stress__mutmut_2': x_run_memray_stress__mutmut_2, 
    'x_run_memray_stress__mutmut_3': x_run_memray_stress__mutmut_3, 
    'x_run_memray_stress__mutmut_4': x_run_memray_stress__mutmut_4, 
    'x_run_memray_stress__mutmut_5': x_run_memray_stress__mutmut_5, 
    'x_run_memray_stress__mutmut_6': x_run_memray_stress__mutmut_6, 
    'x_run_memray_stress__mutmut_7': x_run_memray_stress__mutmut_7, 
    'x_run_memray_stress__mutmut_8': x_run_memray_stress__mutmut_8, 
    'x_run_memray_stress__mutmut_9': x_run_memray_stress__mutmut_9, 
    'x_run_memray_stress__mutmut_10': x_run_memray_stress__mutmut_10, 
    'x_run_memray_stress__mutmut_11': x_run_memray_stress__mutmut_11, 
    'x_run_memray_stress__mutmut_12': x_run_memray_stress__mutmut_12, 
    'x_run_memray_stress__mutmut_13': x_run_memray_stress__mutmut_13, 
    'x_run_memray_stress__mutmut_14': x_run_memray_stress__mutmut_14, 
    'x_run_memray_stress__mutmut_15': x_run_memray_stress__mutmut_15, 
    'x_run_memray_stress__mutmut_16': x_run_memray_stress__mutmut_16, 
    'x_run_memray_stress__mutmut_17': x_run_memray_stress__mutmut_17, 
    'x_run_memray_stress__mutmut_18': x_run_memray_stress__mutmut_18, 
    'x_run_memray_stress__mutmut_19': x_run_memray_stress__mutmut_19, 
    'x_run_memray_stress__mutmut_20': x_run_memray_stress__mutmut_20, 
    'x_run_memray_stress__mutmut_21': x_run_memray_stress__mutmut_21, 
    'x_run_memray_stress__mutmut_22': x_run_memray_stress__mutmut_22, 
    'x_run_memray_stress__mutmut_23': x_run_memray_stress__mutmut_23, 
    'x_run_memray_stress__mutmut_24': x_run_memray_stress__mutmut_24, 
    'x_run_memray_stress__mutmut_25': x_run_memray_stress__mutmut_25, 
    'x_run_memray_stress__mutmut_26': x_run_memray_stress__mutmut_26, 
    'x_run_memray_stress__mutmut_27': x_run_memray_stress__mutmut_27, 
    'x_run_memray_stress__mutmut_28': x_run_memray_stress__mutmut_28, 
    'x_run_memray_stress__mutmut_29': x_run_memray_stress__mutmut_29, 
    'x_run_memray_stress__mutmut_30': x_run_memray_stress__mutmut_30, 
    'x_run_memray_stress__mutmut_31': x_run_memray_stress__mutmut_31, 
    'x_run_memray_stress__mutmut_32': x_run_memray_stress__mutmut_32, 
    'x_run_memray_stress__mutmut_33': x_run_memray_stress__mutmut_33, 
    'x_run_memray_stress__mutmut_34': x_run_memray_stress__mutmut_34, 
    'x_run_memray_stress__mutmut_35': x_run_memray_stress__mutmut_35, 
    'x_run_memray_stress__mutmut_36': x_run_memray_stress__mutmut_36, 
    'x_run_memray_stress__mutmut_37': x_run_memray_stress__mutmut_37, 
    'x_run_memray_stress__mutmut_38': x_run_memray_stress__mutmut_38, 
    'x_run_memray_stress__mutmut_39': x_run_memray_stress__mutmut_39, 
    'x_run_memray_stress__mutmut_40': x_run_memray_stress__mutmut_40, 
    'x_run_memray_stress__mutmut_41': x_run_memray_stress__mutmut_41, 
    'x_run_memray_stress__mutmut_42': x_run_memray_stress__mutmut_42, 
    'x_run_memray_stress__mutmut_43': x_run_memray_stress__mutmut_43, 
    'x_run_memray_stress__mutmut_44': x_run_memray_stress__mutmut_44, 
    'x_run_memray_stress__mutmut_45': x_run_memray_stress__mutmut_45, 
    'x_run_memray_stress__mutmut_46': x_run_memray_stress__mutmut_46, 
    'x_run_memray_stress__mutmut_47': x_run_memray_stress__mutmut_47, 
    'x_run_memray_stress__mutmut_48': x_run_memray_stress__mutmut_48, 
    'x_run_memray_stress__mutmut_49': x_run_memray_stress__mutmut_49, 
    'x_run_memray_stress__mutmut_50': x_run_memray_stress__mutmut_50, 
    'x_run_memray_stress__mutmut_51': x_run_memray_stress__mutmut_51, 
    'x_run_memray_stress__mutmut_52': x_run_memray_stress__mutmut_52, 
    'x_run_memray_stress__mutmut_53': x_run_memray_stress__mutmut_53, 
    'x_run_memray_stress__mutmut_54': x_run_memray_stress__mutmut_54, 
    'x_run_memray_stress__mutmut_55': x_run_memray_stress__mutmut_55, 
    'x_run_memray_stress__mutmut_56': x_run_memray_stress__mutmut_56, 
    'x_run_memray_stress__mutmut_57': x_run_memray_stress__mutmut_57, 
    'x_run_memray_stress__mutmut_58': x_run_memray_stress__mutmut_58, 
    'x_run_memray_stress__mutmut_59': x_run_memray_stress__mutmut_59, 
    'x_run_memray_stress__mutmut_60': x_run_memray_stress__mutmut_60, 
    'x_run_memray_stress__mutmut_61': x_run_memray_stress__mutmut_61, 
    'x_run_memray_stress__mutmut_62': x_run_memray_stress__mutmut_62, 
    'x_run_memray_stress__mutmut_63': x_run_memray_stress__mutmut_63, 
    'x_run_memray_stress__mutmut_64': x_run_memray_stress__mutmut_64, 
    'x_run_memray_stress__mutmut_65': x_run_memray_stress__mutmut_65, 
    'x_run_memray_stress__mutmut_66': x_run_memray_stress__mutmut_66, 
    'x_run_memray_stress__mutmut_67': x_run_memray_stress__mutmut_67, 
    'x_run_memray_stress__mutmut_68': x_run_memray_stress__mutmut_68, 
    'x_run_memray_stress__mutmut_69': x_run_memray_stress__mutmut_69, 
    'x_run_memray_stress__mutmut_70': x_run_memray_stress__mutmut_70, 
    'x_run_memray_stress__mutmut_71': x_run_memray_stress__mutmut_71, 
    'x_run_memray_stress__mutmut_72': x_run_memray_stress__mutmut_72, 
    'x_run_memray_stress__mutmut_73': x_run_memray_stress__mutmut_73, 
    'x_run_memray_stress__mutmut_74': x_run_memray_stress__mutmut_74, 
    'x_run_memray_stress__mutmut_75': x_run_memray_stress__mutmut_75, 
    'x_run_memray_stress__mutmut_76': x_run_memray_stress__mutmut_76, 
    'x_run_memray_stress__mutmut_77': x_run_memray_stress__mutmut_77, 
    'x_run_memray_stress__mutmut_78': x_run_memray_stress__mutmut_78, 
    'x_run_memray_stress__mutmut_79': x_run_memray_stress__mutmut_79, 
    'x_run_memray_stress__mutmut_80': x_run_memray_stress__mutmut_80, 
    'x_run_memray_stress__mutmut_81': x_run_memray_stress__mutmut_81, 
    'x_run_memray_stress__mutmut_82': x_run_memray_stress__mutmut_82, 
    'x_run_memray_stress__mutmut_83': x_run_memray_stress__mutmut_83, 
    'x_run_memray_stress__mutmut_84': x_run_memray_stress__mutmut_84, 
    'x_run_memray_stress__mutmut_85': x_run_memray_stress__mutmut_85, 
    'x_run_memray_stress__mutmut_86': x_run_memray_stress__mutmut_86, 
    'x_run_memray_stress__mutmut_87': x_run_memray_stress__mutmut_87
}

def run_memray_stress(*args, **kwargs):
    result = _mutmut_trampoline(x_run_memray_stress__mutmut_orig, x_run_memray_stress__mutmut_mutants, args, kwargs)
    return result 

run_memray_stress.__signature__ = _mutmut_signature(x_run_memray_stress__mutmut_orig)
x_run_memray_stress__mutmut_orig.__name__ = 'x_run_memray_stress'


# 🧰🌍🔚
