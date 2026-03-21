#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Logging Setup
===================
Provides setup functions for wrknv logging configuration."""

from __future__ import annotations
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

# Note: emoji hierarchy registration disabled - module not available in Foundation
# from provide.foundation.logger.emoji.hierarchy import register_emoji_hierarchy
# from .emojis import WRKNV_EMOJI_HIERARCHY


def setup_wrknv_logging() -> None:
    """
    Set up wrknv-specific logging configuration.

    Currently a placeholder as emoji hierarchy registration is disabled.
    """
    # Note: Emoji hierarchy registration disabled - module not available
    # register_emoji_hierarchy("wrknv", WRKNV_EMOJI_HIERARCHY)


def setup_wrknv_config_logging() -> None:
    """
    Set up logging based on wrknv configuration.

    Currently a placeholder as emoji hierarchy registration is disabled.
    The actual log level configuration is handled by WorkenvConfig.
    """
    # Note: Emoji hierarchy registration disabled - module not available
    # register_emoji_hierarchy("wrknv", WRKNV_EMOJI_HIERARCHY)


# 🧰🌍🔚
