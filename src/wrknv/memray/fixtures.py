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


def _find_project_root() -> Path:
    """Walk up from CWD to find the project root (contains pyproject.toml)."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    return current


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
