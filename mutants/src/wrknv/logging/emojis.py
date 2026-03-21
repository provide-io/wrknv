#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Emoji Hierarchy Definitions
==================================
Defines the emoji hierarchy for wrknv modules."""

from __future__ import annotations

# wrknv emoji hierarchy - organized by functionality
WRKNV_EMOJI_HIERARCHY = {
    # Core wrknv
    # CLI interface
    "wrknv.cli": "⌨️",
    "wrknv.cli.commands": "🎯",
    "wrknv.cli.commands.terraform": "🟦",
    "wrknv.cli.commands.container": "🐳",
    "wrknv.cli.commands.profile": "👤",
    "wrknv.cli.commands.setup": "🌱",
    # Work environment management
    "wrknv.managers.terraform": "🟦",
    "wrknv.managers.tofu": "🌿",
    "wrknv.managers.ibm_tf": "🔵",
    "wrknv.managers.go": "🐹",
    "wrknv.managers.uv": "⚡",
    "wrknv.wenv.version_resolver": "🔍",
    "wrknv.wenv.env_generator": "📝",
    "wrknv.wenv.doctor": "🩺",
    # Configuration system
    "wrknv.config.core": "🔩",
    "wrknv.config.sources": "📋",
    # Package management
    "wrknv.package": "📤",
    # Container operations
    "wrknv.container": "🐳",
    # Gitignore management
    "wrknv.gitignore.manager": "📝",
}
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
