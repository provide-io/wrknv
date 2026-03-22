#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Security Allowlist Manager
==========================
Generate security scanner configuration files from a unified allowlist."""

from __future__ import annotations

from pathlib import Path
import re
from typing import TYPE_CHECKING

from provide.foundation import logger
import yaml

if TYPE_CHECKING:
    from wrknv.security.config import SecurityConfig
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


def x_glob_to_regex__mutmut_orig(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_1(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = None
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_2(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(None)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_3(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = None  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_4(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(None, "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_5(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", None)  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_6(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace("(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_7(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", )  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_8(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"XX\*\*/XX", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_9(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "XX(.*/)?XX")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_10(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = None  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_11(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(None, ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_12(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", None)  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_13(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_14(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", )  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_15(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"XX\*\*XX", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_16(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", "XX.*XX")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_17(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = None  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_18(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(None, "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_19(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", None)  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_20(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace("[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_21(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", )  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_22(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"XX\*XX", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_23(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "XX[^/]*XX")  # * matches anything except /
    result = result.replace(r"\?", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_24(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = None  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_25(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(None, ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_26(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", None)  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_27(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_28(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", )  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_29(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"XX\?XX", ".")  # ? matches single char
    return f"{result}$"


def x_glob_to_regex__mutmut_30(pattern: str) -> str:
    """Convert glob pattern to regex pattern.

    Args:
        pattern: Glob pattern (e.g., "tests/certs/*.key", "docs/**/*.md")

    Returns:
        Regex pattern suitable for TruffleHog and Gitleaks
    """
    # Escape regex special chars except * and ?
    result = re.escape(pattern)
    # Convert glob wildcards to regex
    # Handle **/ (zero or more directories) - must come before ** replacement
    result = result.replace(r"\*\*/", "(.*/)?")  # **/ matches zero or more dirs
    result = result.replace(r"\*\*", ".*")  # ** matches anything including /
    result = result.replace(r"\*", "[^/]*")  # * matches anything except /
    result = result.replace(r"\?", "XX.XX")  # ? matches single char
    return f"{result}$"

x_glob_to_regex__mutmut_mutants : ClassVar[MutantDict] = {
'x_glob_to_regex__mutmut_1': x_glob_to_regex__mutmut_1, 
    'x_glob_to_regex__mutmut_2': x_glob_to_regex__mutmut_2, 
    'x_glob_to_regex__mutmut_3': x_glob_to_regex__mutmut_3, 
    'x_glob_to_regex__mutmut_4': x_glob_to_regex__mutmut_4, 
    'x_glob_to_regex__mutmut_5': x_glob_to_regex__mutmut_5, 
    'x_glob_to_regex__mutmut_6': x_glob_to_regex__mutmut_6, 
    'x_glob_to_regex__mutmut_7': x_glob_to_regex__mutmut_7, 
    'x_glob_to_regex__mutmut_8': x_glob_to_regex__mutmut_8, 
    'x_glob_to_regex__mutmut_9': x_glob_to_regex__mutmut_9, 
    'x_glob_to_regex__mutmut_10': x_glob_to_regex__mutmut_10, 
    'x_glob_to_regex__mutmut_11': x_glob_to_regex__mutmut_11, 
    'x_glob_to_regex__mutmut_12': x_glob_to_regex__mutmut_12, 
    'x_glob_to_regex__mutmut_13': x_glob_to_regex__mutmut_13, 
    'x_glob_to_regex__mutmut_14': x_glob_to_regex__mutmut_14, 
    'x_glob_to_regex__mutmut_15': x_glob_to_regex__mutmut_15, 
    'x_glob_to_regex__mutmut_16': x_glob_to_regex__mutmut_16, 
    'x_glob_to_regex__mutmut_17': x_glob_to_regex__mutmut_17, 
    'x_glob_to_regex__mutmut_18': x_glob_to_regex__mutmut_18, 
    'x_glob_to_regex__mutmut_19': x_glob_to_regex__mutmut_19, 
    'x_glob_to_regex__mutmut_20': x_glob_to_regex__mutmut_20, 
    'x_glob_to_regex__mutmut_21': x_glob_to_regex__mutmut_21, 
    'x_glob_to_regex__mutmut_22': x_glob_to_regex__mutmut_22, 
    'x_glob_to_regex__mutmut_23': x_glob_to_regex__mutmut_23, 
    'x_glob_to_regex__mutmut_24': x_glob_to_regex__mutmut_24, 
    'x_glob_to_regex__mutmut_25': x_glob_to_regex__mutmut_25, 
    'x_glob_to_regex__mutmut_26': x_glob_to_regex__mutmut_26, 
    'x_glob_to_regex__mutmut_27': x_glob_to_regex__mutmut_27, 
    'x_glob_to_regex__mutmut_28': x_glob_to_regex__mutmut_28, 
    'x_glob_to_regex__mutmut_29': x_glob_to_regex__mutmut_29, 
    'x_glob_to_regex__mutmut_30': x_glob_to_regex__mutmut_30
}

def glob_to_regex(*args, **kwargs):
    result = _mutmut_trampoline(x_glob_to_regex__mutmut_orig, x_glob_to_regex__mutmut_mutants, args, kwargs)
    return result 

glob_to_regex.__signature__ = _mutmut_signature(x_glob_to_regex__mutmut_orig)
x_glob_to_regex__mutmut_orig.__name__ = 'x_glob_to_regex'


class SecurityAllowlistManager:
    """Manages security scanner allowlist configurations.

    Generates configuration files for:
    - TruffleHog (.trufflehog-exclude-paths.txt)
    - Gitleaks (.gitleaks.toml)
    - GitGuardian (.gitguardian.yaml)
    """

    def xǁSecurityAllowlistManagerǁ__init____mutmut_orig(
        self,
        project_dir: Path | None = None,
        config: SecurityConfig | None = None,
    ) -> None:
        """Initialize the manager.

        Args:
            project_dir: Project directory to work with
            config: Security configuration (optional, can be set later)
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.config = config

        logger.debug(f"SecurityAllowlistManager initialized for: {self.project_dir}")

    def xǁSecurityAllowlistManagerǁ__init____mutmut_1(
        self,
        project_dir: Path | None = None,
        config: SecurityConfig | None = None,
    ) -> None:
        """Initialize the manager.

        Args:
            project_dir: Project directory to work with
            config: Security configuration (optional, can be set later)
        """
        self.project_dir = None
        self.config = config

        logger.debug(f"SecurityAllowlistManager initialized for: {self.project_dir}")

    def xǁSecurityAllowlistManagerǁ__init____mutmut_2(
        self,
        project_dir: Path | None = None,
        config: SecurityConfig | None = None,
    ) -> None:
        """Initialize the manager.

        Args:
            project_dir: Project directory to work with
            config: Security configuration (optional, can be set later)
        """
        self.project_dir = Path(None) if project_dir else Path.cwd()
        self.config = config

        logger.debug(f"SecurityAllowlistManager initialized for: {self.project_dir}")

    def xǁSecurityAllowlistManagerǁ__init____mutmut_3(
        self,
        project_dir: Path | None = None,
        config: SecurityConfig | None = None,
    ) -> None:
        """Initialize the manager.

        Args:
            project_dir: Project directory to work with
            config: Security configuration (optional, can be set later)
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.config = None

        logger.debug(f"SecurityAllowlistManager initialized for: {self.project_dir}")

    def xǁSecurityAllowlistManagerǁ__init____mutmut_4(
        self,
        project_dir: Path | None = None,
        config: SecurityConfig | None = None,
    ) -> None:
        """Initialize the manager.

        Args:
            project_dir: Project directory to work with
            config: Security configuration (optional, can be set later)
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.config = config

        logger.debug(None)
    
    xǁSecurityAllowlistManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁ__init____mutmut_1': xǁSecurityAllowlistManagerǁ__init____mutmut_1, 
        'xǁSecurityAllowlistManagerǁ__init____mutmut_2': xǁSecurityAllowlistManagerǁ__init____mutmut_2, 
        'xǁSecurityAllowlistManagerǁ__init____mutmut_3': xǁSecurityAllowlistManagerǁ__init____mutmut_3, 
        'xǁSecurityAllowlistManagerǁ__init____mutmut_4': xǁSecurityAllowlistManagerǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁ__init____mutmut_orig)
    xǁSecurityAllowlistManagerǁ__init____mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁ__init__'

    def xǁSecurityAllowlistManagerǁset_config__mutmut_orig(self, config: SecurityConfig) -> None:
        """Set the security configuration.

        Args:
            config: Security configuration object
        """
        self.config = config

    def xǁSecurityAllowlistManagerǁset_config__mutmut_1(self, config: SecurityConfig) -> None:
        """Set the security configuration.

        Args:
            config: Security configuration object
        """
        self.config = None
    
    xǁSecurityAllowlistManagerǁset_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁset_config__mutmut_1': xǁSecurityAllowlistManagerǁset_config__mutmut_1
    }
    
    def set_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁset_config__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁset_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_config.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁset_config__mutmut_orig)
    xǁSecurityAllowlistManagerǁset_config__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁset_config'

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_orig(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_1(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_2(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = None
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_3(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "XXNo security configuration setXX"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_4(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "no security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_5(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "NO SECURITY CONFIGURATION SET"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_6(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(None)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_7(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = None
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_8(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "XX# TruffleHog path exclusionsXX",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_9(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# trufflehog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_10(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TRUFFLEHOG PATH EXCLUSIONS",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_11(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "XX# Auto-generated by wrknv security.generateXX",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_12(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_13(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# AUTO-GENERATED BY WRKNV SECURITY.GENERATE",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_14(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "XXXX",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_15(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(None)
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_16(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(None))
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_17(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) - "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_18(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(None) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_19(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "XX\nXX".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_20(self) -> str:
        """Generate .trufflehog-exclude-paths.txt content.

        Returns:
            Content for TruffleHog exclusion file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# TruffleHog path exclusions",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "",
        ]
        for path in self.config.allowed_paths:
            lines.append(glob_to_regex(path))
        return "\n".join(lines) + "XX\nXX"
    
    xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_1': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_1, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_2': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_2, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_3': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_3, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_4': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_4, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_5': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_5, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_6': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_6, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_7': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_7, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_8': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_8, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_9': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_9, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_10': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_10, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_11': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_11, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_12': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_12, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_13': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_13, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_14': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_14, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_15': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_15, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_16': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_16, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_17': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_17, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_18': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_18, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_19': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_19, 
        'xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_20': xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_20
    }
    
    def generate_trufflehog(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_mutants"), args, kwargs, self)
        return result 
    
    generate_trufflehog.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_orig)
    xǁSecurityAllowlistManagerǁgenerate_trufflehog__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁgenerate_trufflehog'

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_orig(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_1(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_2(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = None
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_3(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "XXNo security configuration setXX"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_4(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "no security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_5(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "NO SECURITY CONFIGURATION SET"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_6(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(None)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_7(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = None
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_8(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "XX# Gitleaks configurationXX",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_9(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_10(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# GITLEAKS CONFIGURATION",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_11(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "XX# Auto-generated by wrknv security.generateXX",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_12(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_13(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# AUTO-GENERATED BY WRKNV SECURITY.GENERATE",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_14(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "XX# https://github.com/gitleaks/gitleaksXX",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_15(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# HTTPS://GITHUB.COM/GITLEAKS/GITLEAKS",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_16(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "XXXX",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_17(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "XX[extend]XX",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_18(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[EXTEND]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_19(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "XXuseDefault = trueXX",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_20(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "usedefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_21(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "USEDEFAULT = TRUE",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_22(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "XXXX",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_23(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "XX[[allowlists]]XX",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_24(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[ALLOWLISTS]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_25(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "XXpaths = [XX",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_26(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "PATHS = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_27(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = None
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_28(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(None)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_29(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(None)
        lines.append("]")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_30(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append(None)
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_31(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("XX]XX")
        return "\n".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_32(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) - "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_33(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(None) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_34(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "XX\nXX".join(lines) + "\n"

    def xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_35(self) -> str:
        """Generate .gitleaks.toml content.

        Returns:
            Content for Gitleaks configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        lines = [
            "# Gitleaks configuration",
            f"# {self.config.description}",
            "# Auto-generated by wrknv security.generate",
            "# https://github.com/gitleaks/gitleaks",
            "",
            "[extend]",
            "useDefault = true",
            "",
            "[[allowlists]]",
            f'description = "{self.config.description}"',
            "paths = [",
        ]
        for path in self.config.allowed_paths:
            regex = glob_to_regex(path)
            lines.append(f"    '''{regex}''',")
        lines.append("]")
        return "\n".join(lines) + "XX\nXX"
    
    xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_1': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_1, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_2': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_2, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_3': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_3, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_4': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_4, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_5': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_5, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_6': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_6, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_7': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_7, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_8': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_8, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_9': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_9, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_10': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_10, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_11': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_11, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_12': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_12, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_13': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_13, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_14': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_14, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_15': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_15, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_16': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_16, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_17': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_17, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_18': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_18, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_19': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_19, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_20': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_20, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_21': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_21, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_22': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_22, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_23': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_23, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_24': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_24, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_25': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_25, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_26': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_26, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_27': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_27, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_28': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_28, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_29': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_29, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_30': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_30, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_31': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_31, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_32': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_32, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_33': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_33, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_34': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_34, 
        'xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_35': xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_35
    }
    
    def generate_gitleaks(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_mutants"), args, kwargs, self)
        return result 
    
    generate_gitleaks.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_orig)
    xǁSecurityAllowlistManagerǁgenerate_gitleaks__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁgenerate_gitleaks'

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_orig(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_1(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_2(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = None
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_3(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "XXNo security configuration setXX"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_4(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "no security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_5(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "NO SECURITY CONFIGURATION SET"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_6(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(None)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_7(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = None
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_8(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "XXversionXX": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_9(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "VERSION": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_10(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 3,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_11(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "XXsecretXX": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_12(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "SECRET": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_13(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "XXignored_pathsXX": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_14(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "IGNORED_PATHS": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_15(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = None
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_16(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header - str(yaml.dump(config_dict, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_17(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(None)

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_18(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(None, default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_19(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=None, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_20(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=None))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_21(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(default_flow_style=False, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_22(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_23(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, ))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_24(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=True, sort_keys=False))

    def xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_25(self) -> str:
        """Generate .gitguardian.yaml content.

        Returns:
            Content for GitGuardian configuration file
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        config_dict = {
            "version": 2,
            "secret": {
                "ignored_paths": self.config.allowed_paths,
            },
        }
        header = f"""\
# GitGuardian configuration
# {self.config.description}
# Auto-generated by wrknv security.generate
# https://docs.gitguardian.com/ggshield-docs/configuration

"""
        return header + str(yaml.dump(config_dict, default_flow_style=False, sort_keys=True))
    
    xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_1': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_1, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_2': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_2, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_3': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_3, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_4': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_4, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_5': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_5, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_6': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_6, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_7': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_7, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_8': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_8, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_9': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_9, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_10': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_10, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_11': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_11, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_12': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_12, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_13': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_13, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_14': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_14, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_15': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_15, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_16': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_16, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_17': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_17, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_18': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_18, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_19': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_19, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_20': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_20, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_21': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_21, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_22': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_22, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_23': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_23, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_24': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_24, 
        'xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_25': xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_25
    }
    
    def generate_gitguardian(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_mutants"), args, kwargs, self)
        return result 
    
    generate_gitguardian.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_orig)
    xǁSecurityAllowlistManagerǁgenerate_gitguardian__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁgenerate_gitguardian'

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_orig(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_1(self, dry_run: bool = True) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_2(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_3(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = None
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_4(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "XXNo security configuration setXX"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_5(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "no security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_6(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "NO SECURITY CONFIGURATION SET"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_7(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(None)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_8(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = None

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_9(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            "XX.trufflehog-exclude-paths.txtXX": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_10(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".TRUFFLEHOG-EXCLUDE-PATHS.TXT": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_11(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            "XX.gitleaks.tomlXX": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_12(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".GITLEAKS.TOML": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_13(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            "XX.gitguardian.yamlXX": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_14(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".GITGUARDIAN.YAML": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_15(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = None
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_16(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = None
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_17(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir * filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_18(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(None)
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_19(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = None
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_20(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = False
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_21(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(None)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_22(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(None)
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_23(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = None
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_24(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = False
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_25(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(None)
                    results[filename] = False

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_26(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = None

        return results

    def xǁSecurityAllowlistManagerǁwrite_all__mutmut_27(self, dry_run: bool = False) -> dict[str, bool]:
        """Write all security scanner configuration files.

        Args:
            dry_run: If True, don't write files, just report what would be done

        Returns:
            Dict mapping filename to success status
        """
        if not self.config:
            msg = "No security configuration set"
            raise ValueError(msg)

        files = {
            ".trufflehog-exclude-paths.txt": self.generate_trufflehog(),
            ".gitleaks.toml": self.generate_gitleaks(),
            ".gitguardian.yaml": self.generate_gitguardian(),
        }

        results = {}
        for filename, content in files.items():
            filepath = self.project_dir / filename
            if dry_run:
                logger.info(f"[DRY-RUN] Would write {filepath}")
                results[filename] = True
            else:
                try:
                    filepath.write_text(content)
                    logger.info(f"Generated {filepath}")
                    results[filename] = True
                except OSError as e:
                    logger.error(f"Failed to write {filepath}: {e}")
                    results[filename] = True

        return results
    
    xǁSecurityAllowlistManagerǁwrite_all__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁwrite_all__mutmut_1': xǁSecurityAllowlistManagerǁwrite_all__mutmut_1, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_2': xǁSecurityAllowlistManagerǁwrite_all__mutmut_2, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_3': xǁSecurityAllowlistManagerǁwrite_all__mutmut_3, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_4': xǁSecurityAllowlistManagerǁwrite_all__mutmut_4, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_5': xǁSecurityAllowlistManagerǁwrite_all__mutmut_5, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_6': xǁSecurityAllowlistManagerǁwrite_all__mutmut_6, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_7': xǁSecurityAllowlistManagerǁwrite_all__mutmut_7, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_8': xǁSecurityAllowlistManagerǁwrite_all__mutmut_8, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_9': xǁSecurityAllowlistManagerǁwrite_all__mutmut_9, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_10': xǁSecurityAllowlistManagerǁwrite_all__mutmut_10, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_11': xǁSecurityAllowlistManagerǁwrite_all__mutmut_11, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_12': xǁSecurityAllowlistManagerǁwrite_all__mutmut_12, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_13': xǁSecurityAllowlistManagerǁwrite_all__mutmut_13, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_14': xǁSecurityAllowlistManagerǁwrite_all__mutmut_14, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_15': xǁSecurityAllowlistManagerǁwrite_all__mutmut_15, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_16': xǁSecurityAllowlistManagerǁwrite_all__mutmut_16, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_17': xǁSecurityAllowlistManagerǁwrite_all__mutmut_17, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_18': xǁSecurityAllowlistManagerǁwrite_all__mutmut_18, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_19': xǁSecurityAllowlistManagerǁwrite_all__mutmut_19, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_20': xǁSecurityAllowlistManagerǁwrite_all__mutmut_20, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_21': xǁSecurityAllowlistManagerǁwrite_all__mutmut_21, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_22': xǁSecurityAllowlistManagerǁwrite_all__mutmut_22, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_23': xǁSecurityAllowlistManagerǁwrite_all__mutmut_23, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_24': xǁSecurityAllowlistManagerǁwrite_all__mutmut_24, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_25': xǁSecurityAllowlistManagerǁwrite_all__mutmut_25, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_26': xǁSecurityAllowlistManagerǁwrite_all__mutmut_26, 
        'xǁSecurityAllowlistManagerǁwrite_all__mutmut_27': xǁSecurityAllowlistManagerǁwrite_all__mutmut_27
    }
    
    def write_all(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁwrite_all__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁwrite_all__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write_all.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁwrite_all__mutmut_orig)
    xǁSecurityAllowlistManagerǁwrite_all__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁwrite_all'

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_orig(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_1(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = None

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_2(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_3(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append(None)
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_4(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("XXNo security configuration setXX")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_5(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("no security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_6(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("NO SECURITY CONFIGURATION SET")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_7(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return True, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_8(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_9(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append(None)

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_10(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("XXNo allowed_paths defined in security configurationXX")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_11(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("no allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_12(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("NO ALLOWED_PATHS DEFINED IN SECURITY CONFIGURATION")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_13(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_14(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append(None)
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_15(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("XXEmpty path in allowed_pathsXX")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_16(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_17(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("EMPTY PATH IN ALLOWED_PATHS")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_18(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                break
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_19(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path and "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_20(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "XX\nXX" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_21(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" not in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_22(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "XX\rXX" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_23(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" not in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_24(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(None)

        return len(errors) == 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_25(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) != 0, errors

    def xǁSecurityAllowlistManagerǁvalidate__mutmut_26(self) -> tuple[bool, list[str]]:
        """Validate the security configuration.

        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []

        if not self.config:
            errors.append("No security configuration set")
            return False, errors

        if not self.config.allowed_paths:
            errors.append("No allowed_paths defined in security configuration")

        # Validate glob patterns
        for path in self.config.allowed_paths:
            if not path:
                errors.append("Empty path in allowed_paths")
                continue
            # Check for invalid characters
            if "\n" in path or "\r" in path:
                errors.append(f"Invalid characters in path: {path!r}")

        return len(errors) == 1, errors
    
    xǁSecurityAllowlistManagerǁvalidate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁvalidate__mutmut_1': xǁSecurityAllowlistManagerǁvalidate__mutmut_1, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_2': xǁSecurityAllowlistManagerǁvalidate__mutmut_2, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_3': xǁSecurityAllowlistManagerǁvalidate__mutmut_3, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_4': xǁSecurityAllowlistManagerǁvalidate__mutmut_4, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_5': xǁSecurityAllowlistManagerǁvalidate__mutmut_5, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_6': xǁSecurityAllowlistManagerǁvalidate__mutmut_6, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_7': xǁSecurityAllowlistManagerǁvalidate__mutmut_7, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_8': xǁSecurityAllowlistManagerǁvalidate__mutmut_8, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_9': xǁSecurityAllowlistManagerǁvalidate__mutmut_9, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_10': xǁSecurityAllowlistManagerǁvalidate__mutmut_10, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_11': xǁSecurityAllowlistManagerǁvalidate__mutmut_11, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_12': xǁSecurityAllowlistManagerǁvalidate__mutmut_12, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_13': xǁSecurityAllowlistManagerǁvalidate__mutmut_13, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_14': xǁSecurityAllowlistManagerǁvalidate__mutmut_14, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_15': xǁSecurityAllowlistManagerǁvalidate__mutmut_15, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_16': xǁSecurityAllowlistManagerǁvalidate__mutmut_16, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_17': xǁSecurityAllowlistManagerǁvalidate__mutmut_17, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_18': xǁSecurityAllowlistManagerǁvalidate__mutmut_18, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_19': xǁSecurityAllowlistManagerǁvalidate__mutmut_19, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_20': xǁSecurityAllowlistManagerǁvalidate__mutmut_20, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_21': xǁSecurityAllowlistManagerǁvalidate__mutmut_21, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_22': xǁSecurityAllowlistManagerǁvalidate__mutmut_22, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_23': xǁSecurityAllowlistManagerǁvalidate__mutmut_23, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_24': xǁSecurityAllowlistManagerǁvalidate__mutmut_24, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_25': xǁSecurityAllowlistManagerǁvalidate__mutmut_25, 
        'xǁSecurityAllowlistManagerǁvalidate__mutmut_26': xǁSecurityAllowlistManagerǁvalidate__mutmut_26
    }
    
    def validate(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁvalidate__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁvalidate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    validate.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁvalidate__mutmut_orig)
    xǁSecurityAllowlistManagerǁvalidate__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁvalidate'

    def xǁSecurityAllowlistManagerǁpreview__mutmut_orig(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_1(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_2(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "XXNo security configuration setXX"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_3(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "no security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_4(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "NO SECURITY CONFIGURATION SET"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_5(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = None
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_6(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.upper()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_7(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower != "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_8(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "XXtrufflehogXX":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_9(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "TRUFFLEHOG":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_10(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower != "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_11(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "XXgitleaksXX":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_12(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "GITLEAKS":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_13(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower != "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_14(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "XXgitguardianXX":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_15(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "GITGUARDIAN":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_16(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = None
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_17(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append(None)
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_18(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("XX=== .trufflehog-exclude-paths.txt ===XX")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_19(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .TRUFFLEHOG-EXCLUDE-PATHS.TXT ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_20(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(None)
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_21(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append(None)
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_22(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("XX\n=== .gitleaks.toml ===XX")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_23(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .GITLEAKS.TOML ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_24(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(None)
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_25(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append(None)
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_26(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("XX\n=== .gitguardian.yaml ===XX")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_27(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .GITGUARDIAN.YAML ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_28(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(None)
        return "\n".join(sections)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_29(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "\n".join(None)

    def xǁSecurityAllowlistManagerǁpreview__mutmut_30(self, tool: str | None = None) -> str:
        """Preview generated configuration.

        Args:
            tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
                  If None, preview all

        Returns:
            Preview content
        """
        if not self.config:
            return "No security configuration set"

        if tool:
            tool_lower = tool.lower()
            if tool_lower == "trufflehog":
                return self.generate_trufflehog()
            elif tool_lower == "gitleaks":
                return self.generate_gitleaks()
            elif tool_lower == "gitguardian":
                return self.generate_gitguardian()
            else:
                return f"Unknown tool: {tool}. Use: trufflehog, gitleaks, gitguardian"

        # Preview all
        sections = []
        sections.append("=== .trufflehog-exclude-paths.txt ===")
        sections.append(self.generate_trufflehog())
        sections.append("\n=== .gitleaks.toml ===")
        sections.append(self.generate_gitleaks())
        sections.append("\n=== .gitguardian.yaml ===")
        sections.append(self.generate_gitguardian())
        return "XX\nXX".join(sections)
    
    xǁSecurityAllowlistManagerǁpreview__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSecurityAllowlistManagerǁpreview__mutmut_1': xǁSecurityAllowlistManagerǁpreview__mutmut_1, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_2': xǁSecurityAllowlistManagerǁpreview__mutmut_2, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_3': xǁSecurityAllowlistManagerǁpreview__mutmut_3, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_4': xǁSecurityAllowlistManagerǁpreview__mutmut_4, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_5': xǁSecurityAllowlistManagerǁpreview__mutmut_5, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_6': xǁSecurityAllowlistManagerǁpreview__mutmut_6, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_7': xǁSecurityAllowlistManagerǁpreview__mutmut_7, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_8': xǁSecurityAllowlistManagerǁpreview__mutmut_8, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_9': xǁSecurityAllowlistManagerǁpreview__mutmut_9, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_10': xǁSecurityAllowlistManagerǁpreview__mutmut_10, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_11': xǁSecurityAllowlistManagerǁpreview__mutmut_11, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_12': xǁSecurityAllowlistManagerǁpreview__mutmut_12, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_13': xǁSecurityAllowlistManagerǁpreview__mutmut_13, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_14': xǁSecurityAllowlistManagerǁpreview__mutmut_14, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_15': xǁSecurityAllowlistManagerǁpreview__mutmut_15, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_16': xǁSecurityAllowlistManagerǁpreview__mutmut_16, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_17': xǁSecurityAllowlistManagerǁpreview__mutmut_17, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_18': xǁSecurityAllowlistManagerǁpreview__mutmut_18, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_19': xǁSecurityAllowlistManagerǁpreview__mutmut_19, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_20': xǁSecurityAllowlistManagerǁpreview__mutmut_20, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_21': xǁSecurityAllowlistManagerǁpreview__mutmut_21, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_22': xǁSecurityAllowlistManagerǁpreview__mutmut_22, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_23': xǁSecurityAllowlistManagerǁpreview__mutmut_23, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_24': xǁSecurityAllowlistManagerǁpreview__mutmut_24, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_25': xǁSecurityAllowlistManagerǁpreview__mutmut_25, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_26': xǁSecurityAllowlistManagerǁpreview__mutmut_26, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_27': xǁSecurityAllowlistManagerǁpreview__mutmut_27, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_28': xǁSecurityAllowlistManagerǁpreview__mutmut_28, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_29': xǁSecurityAllowlistManagerǁpreview__mutmut_29, 
        'xǁSecurityAllowlistManagerǁpreview__mutmut_30': xǁSecurityAllowlistManagerǁpreview__mutmut_30
    }
    
    def preview(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSecurityAllowlistManagerǁpreview__mutmut_orig"), object.__getattribute__(self, "xǁSecurityAllowlistManagerǁpreview__mutmut_mutants"), args, kwargs, self)
        return result 
    
    preview.__signature__ = _mutmut_signature(xǁSecurityAllowlistManagerǁpreview__mutmut_orig)
    xǁSecurityAllowlistManagerǁpreview__mutmut_orig.__name__ = 'xǁSecurityAllowlistManagerǁpreview'


# 🧰🌍🔚
