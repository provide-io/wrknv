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

# 🧰🌍🔚
