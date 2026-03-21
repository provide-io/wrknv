#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Security Configuration
======================
Configuration loading and resolution for security scanning."""

from __future__ import annotations

from pathlib import Path
import tomllib

from attrs import define, field
from provide.foundation import logger
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


@define
class SecurityConfig:
    """Security scanning configuration."""

    description: str = "Allowlisted paths for secret scanning"
    allowed_paths: list[str] = field(factory=list)


def x_load_security_config__mutmut_orig(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_1(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = None

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_2(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(None) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_3(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = None
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_4(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path and project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_5(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir * "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_6(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "XXpyproject.tomlXX"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_7(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "PYPROJECT.TOML"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_8(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = None
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_9(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(None)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_10(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(None)
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_11(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = None
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_12(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path and project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_13(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir * "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_14(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "XXwrknv.tomlXX"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_15(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "WRKNV.TOML"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_16(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = None
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_17(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(None)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_18(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(None)
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_19(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = None
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_20(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir * ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_21(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / "XX.wrknv.tomlXX"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_22(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".WRKNV.TOML"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_23(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = None
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_24(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(None)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_25(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(None)
            return config

    logger.debug("No security configuration found")
    return None


def x_load_security_config__mutmut_26(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug(None)
    return None


def x_load_security_config__mutmut_27(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("XXNo security configuration foundXX")
    return None


def x_load_security_config__mutmut_28(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("no security configuration found")
    return None


def x_load_security_config__mutmut_29(
    project_dir: Path | None = None,
    pyproject_path: Path | None = None,
    wrknv_path: Path | None = None,
) -> SecurityConfig | None:
    """Load security configuration from pyproject.toml or wrknv.toml.

    Resolution order:
    1. pyproject.toml [tool.security]
    2. wrknv.toml [security]

    Args:
        project_dir: Project directory to search in
        pyproject_path: Explicit path to pyproject.toml
        wrknv_path: Explicit path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    project_dir = Path(project_dir) if project_dir else Path.cwd()

    # Try pyproject.toml first
    pyproject_file = pyproject_path or project_dir / "pyproject.toml"
    if pyproject_file.exists():
        config = _load_from_pyproject(pyproject_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {pyproject_file}")
            return config

    # Try wrknv.toml
    wrknv_file = wrknv_path or project_dir / "wrknv.toml"
    if wrknv_file.exists():
        config = _load_from_wrknv(wrknv_file)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_file}")
            return config

    # Try .wrknv.toml (hidden)
    wrknv_hidden = project_dir / ".wrknv.toml"
    if wrknv_hidden.exists():
        config = _load_from_wrknv(wrknv_hidden)
        if config:
            if logger.is_debug_enabled():
                logger.debug(f"Loaded security config from {wrknv_hidden}")
            return config

    logger.debug("NO SECURITY CONFIGURATION FOUND")
    return None

x_load_security_config__mutmut_mutants : ClassVar[MutantDict] = {
'x_load_security_config__mutmut_1': x_load_security_config__mutmut_1, 
    'x_load_security_config__mutmut_2': x_load_security_config__mutmut_2, 
    'x_load_security_config__mutmut_3': x_load_security_config__mutmut_3, 
    'x_load_security_config__mutmut_4': x_load_security_config__mutmut_4, 
    'x_load_security_config__mutmut_5': x_load_security_config__mutmut_5, 
    'x_load_security_config__mutmut_6': x_load_security_config__mutmut_6, 
    'x_load_security_config__mutmut_7': x_load_security_config__mutmut_7, 
    'x_load_security_config__mutmut_8': x_load_security_config__mutmut_8, 
    'x_load_security_config__mutmut_9': x_load_security_config__mutmut_9, 
    'x_load_security_config__mutmut_10': x_load_security_config__mutmut_10, 
    'x_load_security_config__mutmut_11': x_load_security_config__mutmut_11, 
    'x_load_security_config__mutmut_12': x_load_security_config__mutmut_12, 
    'x_load_security_config__mutmut_13': x_load_security_config__mutmut_13, 
    'x_load_security_config__mutmut_14': x_load_security_config__mutmut_14, 
    'x_load_security_config__mutmut_15': x_load_security_config__mutmut_15, 
    'x_load_security_config__mutmut_16': x_load_security_config__mutmut_16, 
    'x_load_security_config__mutmut_17': x_load_security_config__mutmut_17, 
    'x_load_security_config__mutmut_18': x_load_security_config__mutmut_18, 
    'x_load_security_config__mutmut_19': x_load_security_config__mutmut_19, 
    'x_load_security_config__mutmut_20': x_load_security_config__mutmut_20, 
    'x_load_security_config__mutmut_21': x_load_security_config__mutmut_21, 
    'x_load_security_config__mutmut_22': x_load_security_config__mutmut_22, 
    'x_load_security_config__mutmut_23': x_load_security_config__mutmut_23, 
    'x_load_security_config__mutmut_24': x_load_security_config__mutmut_24, 
    'x_load_security_config__mutmut_25': x_load_security_config__mutmut_25, 
    'x_load_security_config__mutmut_26': x_load_security_config__mutmut_26, 
    'x_load_security_config__mutmut_27': x_load_security_config__mutmut_27, 
    'x_load_security_config__mutmut_28': x_load_security_config__mutmut_28, 
    'x_load_security_config__mutmut_29': x_load_security_config__mutmut_29
}

def load_security_config(*args, **kwargs):
    result = _mutmut_trampoline(x_load_security_config__mutmut_orig, x_load_security_config__mutmut_mutants, args, kwargs)
    return result 

load_security_config.__signature__ = _mutmut_signature(x_load_security_config__mutmut_orig)
x_load_security_config__mutmut_orig.__name__ = 'x_load_security_config'


def x__load_from_pyproject__mutmut_orig(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_1(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open(None) as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_2(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("XXrbXX") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_3(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("RB") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_4(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = None

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_5(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(None)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_6(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = None
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_7(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get(None, {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_8(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", None)
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_9(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get({})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_10(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", )
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_11(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get(None, {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_12(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", None).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_13(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get({}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_14(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", ).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_15(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("XXtoolXX", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_16(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("TOOL", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_17(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("XXsecurityXX", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_18(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("SECURITY", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_19(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_20(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=None,
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_21(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=None,
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_22(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_23(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_24(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get(None, "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_25(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", None),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_26(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_27(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", ),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_28(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("XXdescriptionXX", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_29(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("DESCRIPTION", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_30(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "XXAllowlisted paths for secret scanningXX"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_31(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_32(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "ALLOWLISTED PATHS FOR SECRET SCANNING"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_33(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get(None, []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_34(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", None),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_35(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get([]),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_36(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", ),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_37(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("XXallowed_pathsXX", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_38(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("ALLOWED_PATHS", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_pyproject__mutmut_39(path: Path) -> SecurityConfig | None:
    """Load security config from pyproject.toml [tool.security].

    Args:
        path: Path to pyproject.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("tool", {}).get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(None)
        return None

x__load_from_pyproject__mutmut_mutants : ClassVar[MutantDict] = {
'x__load_from_pyproject__mutmut_1': x__load_from_pyproject__mutmut_1, 
    'x__load_from_pyproject__mutmut_2': x__load_from_pyproject__mutmut_2, 
    'x__load_from_pyproject__mutmut_3': x__load_from_pyproject__mutmut_3, 
    'x__load_from_pyproject__mutmut_4': x__load_from_pyproject__mutmut_4, 
    'x__load_from_pyproject__mutmut_5': x__load_from_pyproject__mutmut_5, 
    'x__load_from_pyproject__mutmut_6': x__load_from_pyproject__mutmut_6, 
    'x__load_from_pyproject__mutmut_7': x__load_from_pyproject__mutmut_7, 
    'x__load_from_pyproject__mutmut_8': x__load_from_pyproject__mutmut_8, 
    'x__load_from_pyproject__mutmut_9': x__load_from_pyproject__mutmut_9, 
    'x__load_from_pyproject__mutmut_10': x__load_from_pyproject__mutmut_10, 
    'x__load_from_pyproject__mutmut_11': x__load_from_pyproject__mutmut_11, 
    'x__load_from_pyproject__mutmut_12': x__load_from_pyproject__mutmut_12, 
    'x__load_from_pyproject__mutmut_13': x__load_from_pyproject__mutmut_13, 
    'x__load_from_pyproject__mutmut_14': x__load_from_pyproject__mutmut_14, 
    'x__load_from_pyproject__mutmut_15': x__load_from_pyproject__mutmut_15, 
    'x__load_from_pyproject__mutmut_16': x__load_from_pyproject__mutmut_16, 
    'x__load_from_pyproject__mutmut_17': x__load_from_pyproject__mutmut_17, 
    'x__load_from_pyproject__mutmut_18': x__load_from_pyproject__mutmut_18, 
    'x__load_from_pyproject__mutmut_19': x__load_from_pyproject__mutmut_19, 
    'x__load_from_pyproject__mutmut_20': x__load_from_pyproject__mutmut_20, 
    'x__load_from_pyproject__mutmut_21': x__load_from_pyproject__mutmut_21, 
    'x__load_from_pyproject__mutmut_22': x__load_from_pyproject__mutmut_22, 
    'x__load_from_pyproject__mutmut_23': x__load_from_pyproject__mutmut_23, 
    'x__load_from_pyproject__mutmut_24': x__load_from_pyproject__mutmut_24, 
    'x__load_from_pyproject__mutmut_25': x__load_from_pyproject__mutmut_25, 
    'x__load_from_pyproject__mutmut_26': x__load_from_pyproject__mutmut_26, 
    'x__load_from_pyproject__mutmut_27': x__load_from_pyproject__mutmut_27, 
    'x__load_from_pyproject__mutmut_28': x__load_from_pyproject__mutmut_28, 
    'x__load_from_pyproject__mutmut_29': x__load_from_pyproject__mutmut_29, 
    'x__load_from_pyproject__mutmut_30': x__load_from_pyproject__mutmut_30, 
    'x__load_from_pyproject__mutmut_31': x__load_from_pyproject__mutmut_31, 
    'x__load_from_pyproject__mutmut_32': x__load_from_pyproject__mutmut_32, 
    'x__load_from_pyproject__mutmut_33': x__load_from_pyproject__mutmut_33, 
    'x__load_from_pyproject__mutmut_34': x__load_from_pyproject__mutmut_34, 
    'x__load_from_pyproject__mutmut_35': x__load_from_pyproject__mutmut_35, 
    'x__load_from_pyproject__mutmut_36': x__load_from_pyproject__mutmut_36, 
    'x__load_from_pyproject__mutmut_37': x__load_from_pyproject__mutmut_37, 
    'x__load_from_pyproject__mutmut_38': x__load_from_pyproject__mutmut_38, 
    'x__load_from_pyproject__mutmut_39': x__load_from_pyproject__mutmut_39
}

def _load_from_pyproject(*args, **kwargs):
    result = _mutmut_trampoline(x__load_from_pyproject__mutmut_orig, x__load_from_pyproject__mutmut_mutants, args, kwargs)
    return result 

_load_from_pyproject.__signature__ = _mutmut_signature(x__load_from_pyproject__mutmut_orig)
x__load_from_pyproject__mutmut_orig.__name__ = 'x__load_from_pyproject'


def x__load_from_wrknv__mutmut_orig(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_1(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open(None) as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_2(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("XXrbXX") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_3(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("RB") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_4(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = None

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_5(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(None)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_6(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = None
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_7(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get(None, {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_8(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", None)
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_9(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get({})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_10(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", )
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_11(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("XXsecurityXX", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_12(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("SECURITY", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_13(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_14(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=None,
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_15(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=None,
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_16(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_17(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_18(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get(None, "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_19(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", None),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_20(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_21(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", ),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_22(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("XXdescriptionXX", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_23(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("DESCRIPTION", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_24(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "XXAllowlisted paths for secret scanningXX"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_25(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_26(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "ALLOWLISTED PATHS FOR SECRET SCANNING"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_27(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get(None, []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_28(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", None),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_29(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get([]),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_30(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", ),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_31(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("XXallowed_pathsXX", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_32(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("ALLOWED_PATHS", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"Failed to load {path}: {e}")
        return None


def x__load_from_wrknv__mutmut_33(path: Path) -> SecurityConfig | None:
    """Load security config from wrknv.toml [security].

    Args:
        path: Path to wrknv.toml

    Returns:
        SecurityConfig if found, None otherwise
    """
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)

        security_data = data.get("security", {})
        if not security_data:
            return None

        return SecurityConfig(
            description=security_data.get("description", "Allowlisted paths for secret scanning"),
            allowed_paths=security_data.get("allowed_paths", []),
        )
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(None)
        return None

x__load_from_wrknv__mutmut_mutants : ClassVar[MutantDict] = {
'x__load_from_wrknv__mutmut_1': x__load_from_wrknv__mutmut_1, 
    'x__load_from_wrknv__mutmut_2': x__load_from_wrknv__mutmut_2, 
    'x__load_from_wrknv__mutmut_3': x__load_from_wrknv__mutmut_3, 
    'x__load_from_wrknv__mutmut_4': x__load_from_wrknv__mutmut_4, 
    'x__load_from_wrknv__mutmut_5': x__load_from_wrknv__mutmut_5, 
    'x__load_from_wrknv__mutmut_6': x__load_from_wrknv__mutmut_6, 
    'x__load_from_wrknv__mutmut_7': x__load_from_wrknv__mutmut_7, 
    'x__load_from_wrknv__mutmut_8': x__load_from_wrknv__mutmut_8, 
    'x__load_from_wrknv__mutmut_9': x__load_from_wrknv__mutmut_9, 
    'x__load_from_wrknv__mutmut_10': x__load_from_wrknv__mutmut_10, 
    'x__load_from_wrknv__mutmut_11': x__load_from_wrknv__mutmut_11, 
    'x__load_from_wrknv__mutmut_12': x__load_from_wrknv__mutmut_12, 
    'x__load_from_wrknv__mutmut_13': x__load_from_wrknv__mutmut_13, 
    'x__load_from_wrknv__mutmut_14': x__load_from_wrknv__mutmut_14, 
    'x__load_from_wrknv__mutmut_15': x__load_from_wrknv__mutmut_15, 
    'x__load_from_wrknv__mutmut_16': x__load_from_wrknv__mutmut_16, 
    'x__load_from_wrknv__mutmut_17': x__load_from_wrknv__mutmut_17, 
    'x__load_from_wrknv__mutmut_18': x__load_from_wrknv__mutmut_18, 
    'x__load_from_wrknv__mutmut_19': x__load_from_wrknv__mutmut_19, 
    'x__load_from_wrknv__mutmut_20': x__load_from_wrknv__mutmut_20, 
    'x__load_from_wrknv__mutmut_21': x__load_from_wrknv__mutmut_21, 
    'x__load_from_wrknv__mutmut_22': x__load_from_wrknv__mutmut_22, 
    'x__load_from_wrknv__mutmut_23': x__load_from_wrknv__mutmut_23, 
    'x__load_from_wrknv__mutmut_24': x__load_from_wrknv__mutmut_24, 
    'x__load_from_wrknv__mutmut_25': x__load_from_wrknv__mutmut_25, 
    'x__load_from_wrknv__mutmut_26': x__load_from_wrknv__mutmut_26, 
    'x__load_from_wrknv__mutmut_27': x__load_from_wrknv__mutmut_27, 
    'x__load_from_wrknv__mutmut_28': x__load_from_wrknv__mutmut_28, 
    'x__load_from_wrknv__mutmut_29': x__load_from_wrknv__mutmut_29, 
    'x__load_from_wrknv__mutmut_30': x__load_from_wrknv__mutmut_30, 
    'x__load_from_wrknv__mutmut_31': x__load_from_wrknv__mutmut_31, 
    'x__load_from_wrknv__mutmut_32': x__load_from_wrknv__mutmut_32, 
    'x__load_from_wrknv__mutmut_33': x__load_from_wrknv__mutmut_33
}

def _load_from_wrknv(*args, **kwargs):
    result = _mutmut_trampoline(x__load_from_wrknv__mutmut_orig, x__load_from_wrknv__mutmut_mutants, args, kwargs)
    return result 

_load_from_wrknv.__signature__ = _mutmut_signature(x__load_from_wrknv__mutmut_orig)
x__load_from_wrknv__mutmut_orig.__name__ = 'x__load_from_wrknv'


# 🧰🌍🔚
