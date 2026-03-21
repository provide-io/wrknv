#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Scaffold memray stress testing into a wrknv-managed project.

Creates the directory structure, conftest, example stress test,
baselines file, and wrknv.toml task entries needed for memray profiling.
"""

from __future__ import annotations

from pathlib import Path

from provide.foundation import logger

CONFTEST_TEMPLATE = '''\
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Memray stress test fixtures — provided by wrknv.memray."""

from wrknv.memray.fixtures import *  # noqa: F401, F403
'''

EXAMPLE_TEST_TEMPLATE = '''\
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Example memray stress test — customize for your project."""

from __future__ import annotations

import pytest

from wrknv.memray.runner import run_memray_stress

pytestmark = [pytest.mark.memray, pytest.mark.slow]


def test_example_allocations(memray_output_dir, memray_baseline, memray_baselines_path):
    """Run example stress test under memray and check allocations against baseline.

    To create your stress script:
      1. Copy scripts/memray_example_stress.py
      2. Add your hot-path workload in run_stress()
      3. Update the script path and baseline_key below
    """
    run_memray_stress(
        script="scripts/memray_example_stress.py",
        baseline_key="example_total_allocations",
        output_dir=memray_output_dir,
        baselines=memray_baseline,
        baselines_path=memray_baselines_path,
    )
'''

EXAMPLE_STRESS_SCRIPT_TEMPLATE = '''\
#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Memray stress test: Example workload.

Replace the warmup() and run_stress() bodies with your project's hot path.
"""

from __future__ import annotations

import sys


def warmup() -> None:
    """Warmup phase — import-time allocations are separated from the measurement."""
    # Import your project modules here
    pass


def run_stress() -> None:
    """Run the stress workload — this is what memray measures."""
    # Replace with your hot-path workload, e.g.:
    #   for i in range(10_000):
    #       my_function(data)
    iterations = 10_000
    results = []
    for i in range(iterations):
        results.append(str(i))

    print(f"Example stress complete: {iterations} iterations", file=sys.stderr)


if __name__ == "__main__":
    warmup()
    run_stress()
'''

INIT_TEMPLATE = """\
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""

WRKNV_TASKS_SNIPPET = """
# Memray memory profiling tasks
[tasks.memray]
_default = "pytest tests/memray/ -m memray -v --no-cov"
baseline = "MEMRAY_UPDATE_BASELINE=1 pytest tests/memray/ -m memray -v --no-cov"
"""

PYPROJECT_MARKER_SNIPPET = """
    # Memory profiling
    "memray: memory profiling stress tests (deselect by default, run with -m memray)",
"""

GITIGNORE_ENTRY = "memray-output/"


def scaffold_memray(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(parents=True, exist_ok=True)

    # 2. Create __init__.py
    init_path = memray_test_dir / "__init__.py"
    if not init_path.exists():
        init_path.write_text(INIT_TEMPLATE)
        actions.append(f"Created {init_path.relative_to(project_root)}")

    # 3. Create conftest.py
    conftest_path = memray_test_dir / "conftest.py"
    if not conftest_path.exists():
        conftest_path.write_text(CONFTEST_TEMPLATE)
        actions.append(f"Created {conftest_path.relative_to(project_root)}")
    else:
        actions.append(f"Skipped {conftest_path.relative_to(project_root)} (already exists)")

    # 4. Create baselines.json
    baselines_path = memray_test_dir / "baselines.json"
    if not baselines_path.exists():
        baselines_path.write_text("{}\n")
        actions.append(f"Created {baselines_path.relative_to(project_root)}")

    # 5. Create example test
    example_test_path = memray_test_dir / "test_example_stress.py"
    if not example_test_path.exists():
        example_test_path.write_text(EXAMPLE_TEST_TEMPLATE)
        actions.append(f"Created {example_test_path.relative_to(project_root)}")

    # 6. Create scripts/ directory and example stress script
    scripts_dir = project_root / "scripts"
    scripts_dir.mkdir(exist_ok=True)
    example_script = scripts_dir / "memray_example_stress.py"
    if not example_script.exists():
        example_script.write_text(EXAMPLE_STRESS_SCRIPT_TEMPLATE)
        actions.append(f"Created {example_script.relative_to(project_root)}")

    # 7. Add memray-output/ to .gitignore
    gitignore_path = project_root / ".gitignore"
    if gitignore_path.exists():
        content = gitignore_path.read_text()
        if GITIGNORE_ENTRY not in content:
            with gitignore_path.open("a") as f:
                f.write(f"\n# Memray output\n{GITIGNORE_ENTRY}\n")
            actions.append(f"Added {GITIGNORE_ENTRY} to .gitignore")
    else:
        gitignore_path.write_text(f"# Memray output\n{GITIGNORE_ENTRY}\n")
        actions.append(f"Created .gitignore with {GITIGNORE_ENTRY}")

    # 8. Check if wrknv.toml has memray tasks
    wrknv_toml = project_root / "wrknv.toml"
    if wrknv_toml.exists():
        content = wrknv_toml.read_text()
        if "[tasks.memray]" not in content:
            with wrknv_toml.open("a") as f:
                f.write(WRKNV_TASKS_SNIPPET)
            actions.append("Added [tasks.memray] to wrknv.toml")
        else:
            actions.append("Skipped wrknv.toml (memray tasks already exist)")
    else:
        actions.append("Skipped wrknv.toml (file not found)")

    # 9. Remind about pyproject.toml marker
    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


# 🧰🌍🔚
