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


def x_scaffold_memray__mutmut_orig(project_root: Path) -> list[str]:
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


def x_scaffold_memray__mutmut_1(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = None

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


def x_scaffold_memray__mutmut_2(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = None
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


def x_scaffold_memray__mutmut_3(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" * "memray"
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


def x_scaffold_memray__mutmut_4(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root * "tests" / "memray"
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


def x_scaffold_memray__mutmut_5(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "XXtestsXX" / "memray"
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


def x_scaffold_memray__mutmut_6(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "TESTS" / "memray"
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


def x_scaffold_memray__mutmut_7(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "XXmemrayXX"
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


def x_scaffold_memray__mutmut_8(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "MEMRAY"
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


def x_scaffold_memray__mutmut_9(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(parents=None, exist_ok=True)

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


def x_scaffold_memray__mutmut_10(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(parents=True, exist_ok=None)

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


def x_scaffold_memray__mutmut_11(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(exist_ok=True)

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


def x_scaffold_memray__mutmut_12(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(parents=True, )

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


def x_scaffold_memray__mutmut_13(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(parents=False, exist_ok=True)

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


def x_scaffold_memray__mutmut_14(project_root: Path) -> list[str]:
    """Create memray stress testing scaffolding in a project.

    Args:
        project_root: Root directory of the project

    Returns:
        List of actions taken (for reporting)
    """
    actions: list[str] = []

    # 1. Create tests/memray/ directory
    memray_test_dir = project_root / "tests" / "memray"
    memray_test_dir.mkdir(parents=True, exist_ok=False)

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


def x_scaffold_memray__mutmut_15(project_root: Path) -> list[str]:
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
    init_path = None
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


def x_scaffold_memray__mutmut_16(project_root: Path) -> list[str]:
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
    init_path = memray_test_dir * "__init__.py"
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


def x_scaffold_memray__mutmut_17(project_root: Path) -> list[str]:
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
    init_path = memray_test_dir / "XX__init__.pyXX"
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


def x_scaffold_memray__mutmut_18(project_root: Path) -> list[str]:
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
    init_path = memray_test_dir / "__INIT__.PY"
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


def x_scaffold_memray__mutmut_19(project_root: Path) -> list[str]:
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
    if init_path.exists():
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


def x_scaffold_memray__mutmut_20(project_root: Path) -> list[str]:
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
        init_path.write_text(None)
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


def x_scaffold_memray__mutmut_21(project_root: Path) -> list[str]:
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
        actions.append(None)

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


def x_scaffold_memray__mutmut_22(project_root: Path) -> list[str]:
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
        actions.append(f"Created {init_path.relative_to(None)}")

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


def x_scaffold_memray__mutmut_23(project_root: Path) -> list[str]:
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
    conftest_path = None
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


def x_scaffold_memray__mutmut_24(project_root: Path) -> list[str]:
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
    conftest_path = memray_test_dir * "conftest.py"
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


def x_scaffold_memray__mutmut_25(project_root: Path) -> list[str]:
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
    conftest_path = memray_test_dir / "XXconftest.pyXX"
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


def x_scaffold_memray__mutmut_26(project_root: Path) -> list[str]:
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
    conftest_path = memray_test_dir / "CONFTEST.PY"
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


def x_scaffold_memray__mutmut_27(project_root: Path) -> list[str]:
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
    if conftest_path.exists():
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


def x_scaffold_memray__mutmut_28(project_root: Path) -> list[str]:
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
        conftest_path.write_text(None)
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


def x_scaffold_memray__mutmut_29(project_root: Path) -> list[str]:
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
        actions.append(None)
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


def x_scaffold_memray__mutmut_30(project_root: Path) -> list[str]:
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
        actions.append(f"Created {conftest_path.relative_to(None)}")
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


def x_scaffold_memray__mutmut_31(project_root: Path) -> list[str]:
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
        actions.append(None)

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


def x_scaffold_memray__mutmut_32(project_root: Path) -> list[str]:
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
        actions.append(f"Skipped {conftest_path.relative_to(None)} (already exists)")

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


def x_scaffold_memray__mutmut_33(project_root: Path) -> list[str]:
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
    baselines_path = None
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


def x_scaffold_memray__mutmut_34(project_root: Path) -> list[str]:
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
    baselines_path = memray_test_dir * "baselines.json"
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


def x_scaffold_memray__mutmut_35(project_root: Path) -> list[str]:
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
    baselines_path = memray_test_dir / "XXbaselines.jsonXX"
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


def x_scaffold_memray__mutmut_36(project_root: Path) -> list[str]:
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
    baselines_path = memray_test_dir / "BASELINES.JSON"
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


def x_scaffold_memray__mutmut_37(project_root: Path) -> list[str]:
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
    if baselines_path.exists():
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


def x_scaffold_memray__mutmut_38(project_root: Path) -> list[str]:
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
        baselines_path.write_text(None)
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


def x_scaffold_memray__mutmut_39(project_root: Path) -> list[str]:
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
        baselines_path.write_text("XX{}\nXX")
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


def x_scaffold_memray__mutmut_40(project_root: Path) -> list[str]:
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
        actions.append(None)

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


def x_scaffold_memray__mutmut_41(project_root: Path) -> list[str]:
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
        actions.append(f"Created {baselines_path.relative_to(None)}")

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


def x_scaffold_memray__mutmut_42(project_root: Path) -> list[str]:
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
    example_test_path = None
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


def x_scaffold_memray__mutmut_43(project_root: Path) -> list[str]:
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
    example_test_path = memray_test_dir * "test_example_stress.py"
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


def x_scaffold_memray__mutmut_44(project_root: Path) -> list[str]:
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
    example_test_path = memray_test_dir / "XXtest_example_stress.pyXX"
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


def x_scaffold_memray__mutmut_45(project_root: Path) -> list[str]:
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
    example_test_path = memray_test_dir / "TEST_EXAMPLE_STRESS.PY"
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


def x_scaffold_memray__mutmut_46(project_root: Path) -> list[str]:
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
    if example_test_path.exists():
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


def x_scaffold_memray__mutmut_47(project_root: Path) -> list[str]:
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
        example_test_path.write_text(None)
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


def x_scaffold_memray__mutmut_48(project_root: Path) -> list[str]:
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
        actions.append(None)

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


def x_scaffold_memray__mutmut_49(project_root: Path) -> list[str]:
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
        actions.append(f"Created {example_test_path.relative_to(None)}")

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


def x_scaffold_memray__mutmut_50(project_root: Path) -> list[str]:
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
    scripts_dir = None
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


def x_scaffold_memray__mutmut_51(project_root: Path) -> list[str]:
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
    scripts_dir = project_root * "scripts"
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


def x_scaffold_memray__mutmut_52(project_root: Path) -> list[str]:
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
    scripts_dir = project_root / "XXscriptsXX"
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


def x_scaffold_memray__mutmut_53(project_root: Path) -> list[str]:
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
    scripts_dir = project_root / "SCRIPTS"
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


def x_scaffold_memray__mutmut_54(project_root: Path) -> list[str]:
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
    scripts_dir.mkdir(exist_ok=None)
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


def x_scaffold_memray__mutmut_55(project_root: Path) -> list[str]:
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
    scripts_dir.mkdir(exist_ok=False)
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


def x_scaffold_memray__mutmut_56(project_root: Path) -> list[str]:
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
    example_script = None
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


def x_scaffold_memray__mutmut_57(project_root: Path) -> list[str]:
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
    example_script = scripts_dir * "memray_example_stress.py"
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


def x_scaffold_memray__mutmut_58(project_root: Path) -> list[str]:
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
    example_script = scripts_dir / "XXmemray_example_stress.pyXX"
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


def x_scaffold_memray__mutmut_59(project_root: Path) -> list[str]:
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
    example_script = scripts_dir / "MEMRAY_EXAMPLE_STRESS.PY"
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


def x_scaffold_memray__mutmut_60(project_root: Path) -> list[str]:
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
    if example_script.exists():
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


def x_scaffold_memray__mutmut_61(project_root: Path) -> list[str]:
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
        example_script.write_text(None)
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


def x_scaffold_memray__mutmut_62(project_root: Path) -> list[str]:
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
        actions.append(None)

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


def x_scaffold_memray__mutmut_63(project_root: Path) -> list[str]:
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
        actions.append(f"Created {example_script.relative_to(None)}")

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


def x_scaffold_memray__mutmut_64(project_root: Path) -> list[str]:
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
    gitignore_path = None
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


def x_scaffold_memray__mutmut_65(project_root: Path) -> list[str]:
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
    gitignore_path = project_root * ".gitignore"
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


def x_scaffold_memray__mutmut_66(project_root: Path) -> list[str]:
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
    gitignore_path = project_root / "XX.gitignoreXX"
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


def x_scaffold_memray__mutmut_67(project_root: Path) -> list[str]:
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
    gitignore_path = project_root / ".GITIGNORE"
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


def x_scaffold_memray__mutmut_68(project_root: Path) -> list[str]:
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
        content = None
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


def x_scaffold_memray__mutmut_69(project_root: Path) -> list[str]:
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
        if GITIGNORE_ENTRY in content:
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


def x_scaffold_memray__mutmut_70(project_root: Path) -> list[str]:
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
            with gitignore_path.open(None) as f:
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


def x_scaffold_memray__mutmut_71(project_root: Path) -> list[str]:
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
            with gitignore_path.open("XXaXX") as f:
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


def x_scaffold_memray__mutmut_72(project_root: Path) -> list[str]:
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
            with gitignore_path.open("A") as f:
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


def x_scaffold_memray__mutmut_73(project_root: Path) -> list[str]:
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
                f.write(None)
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


def x_scaffold_memray__mutmut_74(project_root: Path) -> list[str]:
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
            actions.append(None)
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


def x_scaffold_memray__mutmut_75(project_root: Path) -> list[str]:
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
        gitignore_path.write_text(None)
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


def x_scaffold_memray__mutmut_76(project_root: Path) -> list[str]:
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
        actions.append(None)

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


def x_scaffold_memray__mutmut_77(project_root: Path) -> list[str]:
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
    wrknv_toml = None
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


def x_scaffold_memray__mutmut_78(project_root: Path) -> list[str]:
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
    wrknv_toml = project_root * "wrknv.toml"
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


def x_scaffold_memray__mutmut_79(project_root: Path) -> list[str]:
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
    wrknv_toml = project_root / "XXwrknv.tomlXX"
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


def x_scaffold_memray__mutmut_80(project_root: Path) -> list[str]:
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
    wrknv_toml = project_root / "WRKNV.TOML"
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


def x_scaffold_memray__mutmut_81(project_root: Path) -> list[str]:
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
        content = None
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


def x_scaffold_memray__mutmut_82(project_root: Path) -> list[str]:
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
        if "XX[tasks.memray]XX" not in content:
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


def x_scaffold_memray__mutmut_83(project_root: Path) -> list[str]:
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
        if "[TASKS.MEMRAY]" not in content:
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


def x_scaffold_memray__mutmut_84(project_root: Path) -> list[str]:
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
        if "[tasks.memray]" in content:
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


def x_scaffold_memray__mutmut_85(project_root: Path) -> list[str]:
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
            with wrknv_toml.open(None) as f:
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


def x_scaffold_memray__mutmut_86(project_root: Path) -> list[str]:
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
            with wrknv_toml.open("XXaXX") as f:
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


def x_scaffold_memray__mutmut_87(project_root: Path) -> list[str]:
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
            with wrknv_toml.open("A") as f:
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


def x_scaffold_memray__mutmut_88(project_root: Path) -> list[str]:
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
                f.write(None)
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


def x_scaffold_memray__mutmut_89(project_root: Path) -> list[str]:
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
            actions.append(None)
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


def x_scaffold_memray__mutmut_90(project_root: Path) -> list[str]:
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
            actions.append("XXAdded [tasks.memray] to wrknv.tomlXX")
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


def x_scaffold_memray__mutmut_91(project_root: Path) -> list[str]:
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
            actions.append("added [tasks.memray] to wrknv.toml")
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


def x_scaffold_memray__mutmut_92(project_root: Path) -> list[str]:
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
            actions.append("ADDED [TASKS.MEMRAY] TO WRKNV.TOML")
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


def x_scaffold_memray__mutmut_93(project_root: Path) -> list[str]:
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
            actions.append(None)
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


def x_scaffold_memray__mutmut_94(project_root: Path) -> list[str]:
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
            actions.append("XXSkipped wrknv.toml (memray tasks already exist)XX")
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


def x_scaffold_memray__mutmut_95(project_root: Path) -> list[str]:
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
            actions.append("skipped wrknv.toml (memray tasks already exist)")
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


def x_scaffold_memray__mutmut_96(project_root: Path) -> list[str]:
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
            actions.append("SKIPPED WRKNV.TOML (MEMRAY TASKS ALREADY EXIST)")
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


def x_scaffold_memray__mutmut_97(project_root: Path) -> list[str]:
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
        actions.append(None)

    # 9. Remind about pyproject.toml marker
    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_98(project_root: Path) -> list[str]:
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
        actions.append("XXSkipped wrknv.toml (file not found)XX")

    # 9. Remind about pyproject.toml marker
    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_99(project_root: Path) -> list[str]:
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
        actions.append("skipped wrknv.toml (file not found)")

    # 9. Remind about pyproject.toml marker
    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_100(project_root: Path) -> list[str]:
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
        actions.append("SKIPPED WRKNV.TOML (FILE NOT FOUND)")

    # 9. Remind about pyproject.toml marker
    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_101(project_root: Path) -> list[str]:
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
    pyproject = None
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_102(project_root: Path) -> list[str]:
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
    pyproject = project_root * "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_103(project_root: Path) -> list[str]:
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
    pyproject = project_root / "XXpyproject.tomlXX"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_104(project_root: Path) -> list[str]:
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
    pyproject = project_root / "PYPROJECT.TOML"
    if pyproject.exists():
        content = pyproject.read_text()
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_105(project_root: Path) -> list[str]:
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
        content = None
        if '"memray' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_106(project_root: Path) -> list[str]:
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
        if '"memray' not in content or "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_107(project_root: Path) -> list[str]:
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
        if 'XX"memrayXX' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_108(project_root: Path) -> list[str]:
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
        if '"MEMRAY' not in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_109(project_root: Path) -> list[str]:
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
        if '"memray' in content and "'memray" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_110(project_root: Path) -> list[str]:
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
        if '"memray' not in content and "XX'memrayXX" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_111(project_root: Path) -> list[str]:
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
        if '"memray' not in content and "'MEMRAY" not in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_112(project_root: Path) -> list[str]:
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
        if '"memray' not in content and "'memray" in content:
            actions.append("NOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_113(project_root: Path) -> list[str]:
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
            actions.append(None)

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_114(project_root: Path) -> list[str]:
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
            actions.append("XXNOTE: Add memray marker to pyproject.toml [tool.pytest.ini_options] markersXX")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_115(project_root: Path) -> list[str]:
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
            actions.append("note: add memray marker to pyproject.toml [tool.pytest.ini_options] markers")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_116(project_root: Path) -> list[str]:
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
            actions.append("NOTE: ADD MEMRAY MARKER TO PYPROJECT.TOML [TOOL.PYTEST.INI_OPTIONS] MARKERS")

    for action in actions:
        logger.debug("memray_scaffold_action", action=action)

    return actions


def x_scaffold_memray__mutmut_117(project_root: Path) -> list[str]:
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
        logger.debug(None, action=action)

    return actions


def x_scaffold_memray__mutmut_118(project_root: Path) -> list[str]:
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
        logger.debug("memray_scaffold_action", action=None)

    return actions


def x_scaffold_memray__mutmut_119(project_root: Path) -> list[str]:
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
        logger.debug(action=action)

    return actions


def x_scaffold_memray__mutmut_120(project_root: Path) -> list[str]:
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
        logger.debug("memray_scaffold_action", )

    return actions


def x_scaffold_memray__mutmut_121(project_root: Path) -> list[str]:
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
        logger.debug("XXmemray_scaffold_actionXX", action=action)

    return actions


def x_scaffold_memray__mutmut_122(project_root: Path) -> list[str]:
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
        logger.debug("MEMRAY_SCAFFOLD_ACTION", action=action)

    return actions

x_scaffold_memray__mutmut_mutants : ClassVar[MutantDict] = {
'x_scaffold_memray__mutmut_1': x_scaffold_memray__mutmut_1, 
    'x_scaffold_memray__mutmut_2': x_scaffold_memray__mutmut_2, 
    'x_scaffold_memray__mutmut_3': x_scaffold_memray__mutmut_3, 
    'x_scaffold_memray__mutmut_4': x_scaffold_memray__mutmut_4, 
    'x_scaffold_memray__mutmut_5': x_scaffold_memray__mutmut_5, 
    'x_scaffold_memray__mutmut_6': x_scaffold_memray__mutmut_6, 
    'x_scaffold_memray__mutmut_7': x_scaffold_memray__mutmut_7, 
    'x_scaffold_memray__mutmut_8': x_scaffold_memray__mutmut_8, 
    'x_scaffold_memray__mutmut_9': x_scaffold_memray__mutmut_9, 
    'x_scaffold_memray__mutmut_10': x_scaffold_memray__mutmut_10, 
    'x_scaffold_memray__mutmut_11': x_scaffold_memray__mutmut_11, 
    'x_scaffold_memray__mutmut_12': x_scaffold_memray__mutmut_12, 
    'x_scaffold_memray__mutmut_13': x_scaffold_memray__mutmut_13, 
    'x_scaffold_memray__mutmut_14': x_scaffold_memray__mutmut_14, 
    'x_scaffold_memray__mutmut_15': x_scaffold_memray__mutmut_15, 
    'x_scaffold_memray__mutmut_16': x_scaffold_memray__mutmut_16, 
    'x_scaffold_memray__mutmut_17': x_scaffold_memray__mutmut_17, 
    'x_scaffold_memray__mutmut_18': x_scaffold_memray__mutmut_18, 
    'x_scaffold_memray__mutmut_19': x_scaffold_memray__mutmut_19, 
    'x_scaffold_memray__mutmut_20': x_scaffold_memray__mutmut_20, 
    'x_scaffold_memray__mutmut_21': x_scaffold_memray__mutmut_21, 
    'x_scaffold_memray__mutmut_22': x_scaffold_memray__mutmut_22, 
    'x_scaffold_memray__mutmut_23': x_scaffold_memray__mutmut_23, 
    'x_scaffold_memray__mutmut_24': x_scaffold_memray__mutmut_24, 
    'x_scaffold_memray__mutmut_25': x_scaffold_memray__mutmut_25, 
    'x_scaffold_memray__mutmut_26': x_scaffold_memray__mutmut_26, 
    'x_scaffold_memray__mutmut_27': x_scaffold_memray__mutmut_27, 
    'x_scaffold_memray__mutmut_28': x_scaffold_memray__mutmut_28, 
    'x_scaffold_memray__mutmut_29': x_scaffold_memray__mutmut_29, 
    'x_scaffold_memray__mutmut_30': x_scaffold_memray__mutmut_30, 
    'x_scaffold_memray__mutmut_31': x_scaffold_memray__mutmut_31, 
    'x_scaffold_memray__mutmut_32': x_scaffold_memray__mutmut_32, 
    'x_scaffold_memray__mutmut_33': x_scaffold_memray__mutmut_33, 
    'x_scaffold_memray__mutmut_34': x_scaffold_memray__mutmut_34, 
    'x_scaffold_memray__mutmut_35': x_scaffold_memray__mutmut_35, 
    'x_scaffold_memray__mutmut_36': x_scaffold_memray__mutmut_36, 
    'x_scaffold_memray__mutmut_37': x_scaffold_memray__mutmut_37, 
    'x_scaffold_memray__mutmut_38': x_scaffold_memray__mutmut_38, 
    'x_scaffold_memray__mutmut_39': x_scaffold_memray__mutmut_39, 
    'x_scaffold_memray__mutmut_40': x_scaffold_memray__mutmut_40, 
    'x_scaffold_memray__mutmut_41': x_scaffold_memray__mutmut_41, 
    'x_scaffold_memray__mutmut_42': x_scaffold_memray__mutmut_42, 
    'x_scaffold_memray__mutmut_43': x_scaffold_memray__mutmut_43, 
    'x_scaffold_memray__mutmut_44': x_scaffold_memray__mutmut_44, 
    'x_scaffold_memray__mutmut_45': x_scaffold_memray__mutmut_45, 
    'x_scaffold_memray__mutmut_46': x_scaffold_memray__mutmut_46, 
    'x_scaffold_memray__mutmut_47': x_scaffold_memray__mutmut_47, 
    'x_scaffold_memray__mutmut_48': x_scaffold_memray__mutmut_48, 
    'x_scaffold_memray__mutmut_49': x_scaffold_memray__mutmut_49, 
    'x_scaffold_memray__mutmut_50': x_scaffold_memray__mutmut_50, 
    'x_scaffold_memray__mutmut_51': x_scaffold_memray__mutmut_51, 
    'x_scaffold_memray__mutmut_52': x_scaffold_memray__mutmut_52, 
    'x_scaffold_memray__mutmut_53': x_scaffold_memray__mutmut_53, 
    'x_scaffold_memray__mutmut_54': x_scaffold_memray__mutmut_54, 
    'x_scaffold_memray__mutmut_55': x_scaffold_memray__mutmut_55, 
    'x_scaffold_memray__mutmut_56': x_scaffold_memray__mutmut_56, 
    'x_scaffold_memray__mutmut_57': x_scaffold_memray__mutmut_57, 
    'x_scaffold_memray__mutmut_58': x_scaffold_memray__mutmut_58, 
    'x_scaffold_memray__mutmut_59': x_scaffold_memray__mutmut_59, 
    'x_scaffold_memray__mutmut_60': x_scaffold_memray__mutmut_60, 
    'x_scaffold_memray__mutmut_61': x_scaffold_memray__mutmut_61, 
    'x_scaffold_memray__mutmut_62': x_scaffold_memray__mutmut_62, 
    'x_scaffold_memray__mutmut_63': x_scaffold_memray__mutmut_63, 
    'x_scaffold_memray__mutmut_64': x_scaffold_memray__mutmut_64, 
    'x_scaffold_memray__mutmut_65': x_scaffold_memray__mutmut_65, 
    'x_scaffold_memray__mutmut_66': x_scaffold_memray__mutmut_66, 
    'x_scaffold_memray__mutmut_67': x_scaffold_memray__mutmut_67, 
    'x_scaffold_memray__mutmut_68': x_scaffold_memray__mutmut_68, 
    'x_scaffold_memray__mutmut_69': x_scaffold_memray__mutmut_69, 
    'x_scaffold_memray__mutmut_70': x_scaffold_memray__mutmut_70, 
    'x_scaffold_memray__mutmut_71': x_scaffold_memray__mutmut_71, 
    'x_scaffold_memray__mutmut_72': x_scaffold_memray__mutmut_72, 
    'x_scaffold_memray__mutmut_73': x_scaffold_memray__mutmut_73, 
    'x_scaffold_memray__mutmut_74': x_scaffold_memray__mutmut_74, 
    'x_scaffold_memray__mutmut_75': x_scaffold_memray__mutmut_75, 
    'x_scaffold_memray__mutmut_76': x_scaffold_memray__mutmut_76, 
    'x_scaffold_memray__mutmut_77': x_scaffold_memray__mutmut_77, 
    'x_scaffold_memray__mutmut_78': x_scaffold_memray__mutmut_78, 
    'x_scaffold_memray__mutmut_79': x_scaffold_memray__mutmut_79, 
    'x_scaffold_memray__mutmut_80': x_scaffold_memray__mutmut_80, 
    'x_scaffold_memray__mutmut_81': x_scaffold_memray__mutmut_81, 
    'x_scaffold_memray__mutmut_82': x_scaffold_memray__mutmut_82, 
    'x_scaffold_memray__mutmut_83': x_scaffold_memray__mutmut_83, 
    'x_scaffold_memray__mutmut_84': x_scaffold_memray__mutmut_84, 
    'x_scaffold_memray__mutmut_85': x_scaffold_memray__mutmut_85, 
    'x_scaffold_memray__mutmut_86': x_scaffold_memray__mutmut_86, 
    'x_scaffold_memray__mutmut_87': x_scaffold_memray__mutmut_87, 
    'x_scaffold_memray__mutmut_88': x_scaffold_memray__mutmut_88, 
    'x_scaffold_memray__mutmut_89': x_scaffold_memray__mutmut_89, 
    'x_scaffold_memray__mutmut_90': x_scaffold_memray__mutmut_90, 
    'x_scaffold_memray__mutmut_91': x_scaffold_memray__mutmut_91, 
    'x_scaffold_memray__mutmut_92': x_scaffold_memray__mutmut_92, 
    'x_scaffold_memray__mutmut_93': x_scaffold_memray__mutmut_93, 
    'x_scaffold_memray__mutmut_94': x_scaffold_memray__mutmut_94, 
    'x_scaffold_memray__mutmut_95': x_scaffold_memray__mutmut_95, 
    'x_scaffold_memray__mutmut_96': x_scaffold_memray__mutmut_96, 
    'x_scaffold_memray__mutmut_97': x_scaffold_memray__mutmut_97, 
    'x_scaffold_memray__mutmut_98': x_scaffold_memray__mutmut_98, 
    'x_scaffold_memray__mutmut_99': x_scaffold_memray__mutmut_99, 
    'x_scaffold_memray__mutmut_100': x_scaffold_memray__mutmut_100, 
    'x_scaffold_memray__mutmut_101': x_scaffold_memray__mutmut_101, 
    'x_scaffold_memray__mutmut_102': x_scaffold_memray__mutmut_102, 
    'x_scaffold_memray__mutmut_103': x_scaffold_memray__mutmut_103, 
    'x_scaffold_memray__mutmut_104': x_scaffold_memray__mutmut_104, 
    'x_scaffold_memray__mutmut_105': x_scaffold_memray__mutmut_105, 
    'x_scaffold_memray__mutmut_106': x_scaffold_memray__mutmut_106, 
    'x_scaffold_memray__mutmut_107': x_scaffold_memray__mutmut_107, 
    'x_scaffold_memray__mutmut_108': x_scaffold_memray__mutmut_108, 
    'x_scaffold_memray__mutmut_109': x_scaffold_memray__mutmut_109, 
    'x_scaffold_memray__mutmut_110': x_scaffold_memray__mutmut_110, 
    'x_scaffold_memray__mutmut_111': x_scaffold_memray__mutmut_111, 
    'x_scaffold_memray__mutmut_112': x_scaffold_memray__mutmut_112, 
    'x_scaffold_memray__mutmut_113': x_scaffold_memray__mutmut_113, 
    'x_scaffold_memray__mutmut_114': x_scaffold_memray__mutmut_114, 
    'x_scaffold_memray__mutmut_115': x_scaffold_memray__mutmut_115, 
    'x_scaffold_memray__mutmut_116': x_scaffold_memray__mutmut_116, 
    'x_scaffold_memray__mutmut_117': x_scaffold_memray__mutmut_117, 
    'x_scaffold_memray__mutmut_118': x_scaffold_memray__mutmut_118, 
    'x_scaffold_memray__mutmut_119': x_scaffold_memray__mutmut_119, 
    'x_scaffold_memray__mutmut_120': x_scaffold_memray__mutmut_120, 
    'x_scaffold_memray__mutmut_121': x_scaffold_memray__mutmut_121, 
    'x_scaffold_memray__mutmut_122': x_scaffold_memray__mutmut_122
}

def scaffold_memray(*args, **kwargs):
    result = _mutmut_trampoline(x_scaffold_memray__mutmut_orig, x_scaffold_memray__mutmut_mutants, args, kwargs)
    return result 

scaffold_memray.__signature__ = _mutmut_signature(x_scaffold_memray__mutmut_orig)
x_scaffold_memray__mutmut_orig.__name__ = 'x_scaffold_memray'


# 🧰🌍🔚
