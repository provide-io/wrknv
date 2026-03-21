#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""CLI commands for memray memory profiling integration."""

from __future__ import annotations

from pathlib import Path

from provide.foundation.cli import echo_info, echo_success
from provide.foundation.console.output import pout
from provide.foundation.hub import register_command
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


@register_command("memray", group=True, description="Memory profiling with memray")
def memray_group() -> None:
    """Memory profiling with memray."""


@register_command("memray.init", description="Scaffold memray stress testing into current project")
def memray_init(project_dir: str = ".") -> None:
    """Scaffold memray stress testing into the current project.

    Creates tests/memray/, example scripts, baselines.json,
    and adds wrknv.toml task entries.
    """
    from wrknv.memray.scaffold import scaffold_memray

    project_root = Path(project_dir).resolve()
    actions = scaffold_memray(project_root)

    echo_info(f"Memray scaffolding complete in {project_root.name}:")
    for action in actions:
        if action.startswith("NOTE:"):
            pout(f"  {action}")
        else:
            echo_success(f"  {action}")

    pout("\nNext steps:")
    pout("  1. Edit scripts/memray_example_stress.py with your workload")
    pout("  2. Run: we memray              # first run records baseline")
    pout("  3. Run: we memray              # subsequent runs check regression")
    pout("  4. Run: we memray baseline     # update baselines after optimization")


# 🧰🌍🔚
