#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#


from __future__ import annotations

import json
from pathlib import Path
import sys
import tomllib
from typing import Any

from packaging.specifiers import SpecifierSet
from packaging.version import Version
from provide.foundation.process import run
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


def x_get_venv_python_version__mutmut_orig(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_1(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = None
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_2(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" * "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_3(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir * "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_4(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "XXbinXX" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_5(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "BIN" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_6(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "XXpythonXX"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_7(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "PYTHON"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_8(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith(None):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_9(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("XXwinXX"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_10(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("WIN"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_11(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = None

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_12(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" * "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_13(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir * "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_14(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "XXScriptsXX" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_15(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_16(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "SCRIPTS" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_17(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "XXpython.exeXX"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_18(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "PYTHON.EXE"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_19(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_20(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = None
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_21(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(None),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_22(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "XX-cXX",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_23(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-C",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_24(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "XXimport sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))XX",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_25(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "IMPORT SYS, JSON; PRINT(JSON.DUMPS({'VERSION': '.'.JOIN(MAP(STR, SYS.VERSION_INFO[:3])), 'MAJOR': SYS.VERSION_INFO.MAJOR, 'MINOR': SYS.VERSION_INFO.MINOR, 'MICRO': SYS.VERSION_INFO.MICRO}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_26(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = None

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_27(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(None, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_28(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=None)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_29(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_30(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, )

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_31(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=True)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_32(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode != 0:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_33(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 1:
            result_dict: dict[str, Any] = json.loads(result.stdout)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_34(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = None
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None


def x_get_venv_python_version__mutmut_35(venv_dir: Path) -> dict[str, Any] | None:
    """Get Python version information from a virtual environment.

    Args:
        venv_dir: Path to the virtual environment directory

    Returns:
        Dict with version info or None if venv doesn't exist
    """
    python_bin = venv_dir / "bin" / "python"
    if sys.platform.startswith("win"):
        python_bin = venv_dir / "Scripts" / "python.exe"

    if not python_bin.exists():
        return None

    try:
        # Get version info as JSON for easy parsing
        cmd = [
            str(python_bin),
            "-c",
            "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))",
        ]
        result = run(cmd, check=False)

        if result.returncode == 0:
            result_dict: dict[str, Any] = json.loads(None)
            return result_dict
    except Exception:
        pass  # nosec B110 - Fallback to None if uv python list fails

    return None

x_get_venv_python_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_venv_python_version__mutmut_1': x_get_venv_python_version__mutmut_1, 
    'x_get_venv_python_version__mutmut_2': x_get_venv_python_version__mutmut_2, 
    'x_get_venv_python_version__mutmut_3': x_get_venv_python_version__mutmut_3, 
    'x_get_venv_python_version__mutmut_4': x_get_venv_python_version__mutmut_4, 
    'x_get_venv_python_version__mutmut_5': x_get_venv_python_version__mutmut_5, 
    'x_get_venv_python_version__mutmut_6': x_get_venv_python_version__mutmut_6, 
    'x_get_venv_python_version__mutmut_7': x_get_venv_python_version__mutmut_7, 
    'x_get_venv_python_version__mutmut_8': x_get_venv_python_version__mutmut_8, 
    'x_get_venv_python_version__mutmut_9': x_get_venv_python_version__mutmut_9, 
    'x_get_venv_python_version__mutmut_10': x_get_venv_python_version__mutmut_10, 
    'x_get_venv_python_version__mutmut_11': x_get_venv_python_version__mutmut_11, 
    'x_get_venv_python_version__mutmut_12': x_get_venv_python_version__mutmut_12, 
    'x_get_venv_python_version__mutmut_13': x_get_venv_python_version__mutmut_13, 
    'x_get_venv_python_version__mutmut_14': x_get_venv_python_version__mutmut_14, 
    'x_get_venv_python_version__mutmut_15': x_get_venv_python_version__mutmut_15, 
    'x_get_venv_python_version__mutmut_16': x_get_venv_python_version__mutmut_16, 
    'x_get_venv_python_version__mutmut_17': x_get_venv_python_version__mutmut_17, 
    'x_get_venv_python_version__mutmut_18': x_get_venv_python_version__mutmut_18, 
    'x_get_venv_python_version__mutmut_19': x_get_venv_python_version__mutmut_19, 
    'x_get_venv_python_version__mutmut_20': x_get_venv_python_version__mutmut_20, 
    'x_get_venv_python_version__mutmut_21': x_get_venv_python_version__mutmut_21, 
    'x_get_venv_python_version__mutmut_22': x_get_venv_python_version__mutmut_22, 
    'x_get_venv_python_version__mutmut_23': x_get_venv_python_version__mutmut_23, 
    'x_get_venv_python_version__mutmut_24': x_get_venv_python_version__mutmut_24, 
    'x_get_venv_python_version__mutmut_25': x_get_venv_python_version__mutmut_25, 
    'x_get_venv_python_version__mutmut_26': x_get_venv_python_version__mutmut_26, 
    'x_get_venv_python_version__mutmut_27': x_get_venv_python_version__mutmut_27, 
    'x_get_venv_python_version__mutmut_28': x_get_venv_python_version__mutmut_28, 
    'x_get_venv_python_version__mutmut_29': x_get_venv_python_version__mutmut_29, 
    'x_get_venv_python_version__mutmut_30': x_get_venv_python_version__mutmut_30, 
    'x_get_venv_python_version__mutmut_31': x_get_venv_python_version__mutmut_31, 
    'x_get_venv_python_version__mutmut_32': x_get_venv_python_version__mutmut_32, 
    'x_get_venv_python_version__mutmut_33': x_get_venv_python_version__mutmut_33, 
    'x_get_venv_python_version__mutmut_34': x_get_venv_python_version__mutmut_34, 
    'x_get_venv_python_version__mutmut_35': x_get_venv_python_version__mutmut_35
}

def get_venv_python_version(*args, **kwargs):
    result = _mutmut_trampoline(x_get_venv_python_version__mutmut_orig, x_get_venv_python_version__mutmut_mutants, args, kwargs)
    return result 

get_venv_python_version.__signature__ = _mutmut_signature(x_get_venv_python_version__mutmut_orig)
x_get_venv_python_version__mutmut_orig.__name__ = 'x_get_venv_python_version'


def x_get_project_python_requirement__mutmut_orig() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_1() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = None

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_2() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() * "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_3() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "XXpyproject.tomlXX"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_4() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "PYPROJECT.TOML"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_5() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_6() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open(None) as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_7() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("XXrbXX") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_8() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("RB") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_9() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = None

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_10() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(None)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_11() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data or "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_12() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "XXprojectXX" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_13() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "PROJECT" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_14() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" not in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_15() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "XXrequires-pythonXX" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_16() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "REQUIRES-PYTHON" in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_17() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" not in data["project"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_18() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["XXprojectXX"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_19() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["PROJECT"]:
            requires_python: str = data["project"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_20() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = None
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_21() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["XXprojectXX"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_22() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["PROJECT"]["requires-python"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_23() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["XXrequires-pythonXX"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None


def x_get_project_python_requirement__mutmut_24() -> str | None:
    """Get Python version requirement from pyproject.toml.

    Returns:
        Python version specifier string or None
    """
    pyproject_path = Path.cwd() / "pyproject.toml"

    if not pyproject_path.exists():
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)

        # Check for requires-python in [project] section
        if "project" in data and "requires-python" in data["project"]:
            requires_python: str = data["project"]["REQUIRES-PYTHON"]
            return requires_python
    except Exception:
        pass  # nosec B110 - Fallback to None if pyproject.toml parsing fails

    return None

x_get_project_python_requirement__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_project_python_requirement__mutmut_1': x_get_project_python_requirement__mutmut_1, 
    'x_get_project_python_requirement__mutmut_2': x_get_project_python_requirement__mutmut_2, 
    'x_get_project_python_requirement__mutmut_3': x_get_project_python_requirement__mutmut_3, 
    'x_get_project_python_requirement__mutmut_4': x_get_project_python_requirement__mutmut_4, 
    'x_get_project_python_requirement__mutmut_5': x_get_project_python_requirement__mutmut_5, 
    'x_get_project_python_requirement__mutmut_6': x_get_project_python_requirement__mutmut_6, 
    'x_get_project_python_requirement__mutmut_7': x_get_project_python_requirement__mutmut_7, 
    'x_get_project_python_requirement__mutmut_8': x_get_project_python_requirement__mutmut_8, 
    'x_get_project_python_requirement__mutmut_9': x_get_project_python_requirement__mutmut_9, 
    'x_get_project_python_requirement__mutmut_10': x_get_project_python_requirement__mutmut_10, 
    'x_get_project_python_requirement__mutmut_11': x_get_project_python_requirement__mutmut_11, 
    'x_get_project_python_requirement__mutmut_12': x_get_project_python_requirement__mutmut_12, 
    'x_get_project_python_requirement__mutmut_13': x_get_project_python_requirement__mutmut_13, 
    'x_get_project_python_requirement__mutmut_14': x_get_project_python_requirement__mutmut_14, 
    'x_get_project_python_requirement__mutmut_15': x_get_project_python_requirement__mutmut_15, 
    'x_get_project_python_requirement__mutmut_16': x_get_project_python_requirement__mutmut_16, 
    'x_get_project_python_requirement__mutmut_17': x_get_project_python_requirement__mutmut_17, 
    'x_get_project_python_requirement__mutmut_18': x_get_project_python_requirement__mutmut_18, 
    'x_get_project_python_requirement__mutmut_19': x_get_project_python_requirement__mutmut_19, 
    'x_get_project_python_requirement__mutmut_20': x_get_project_python_requirement__mutmut_20, 
    'x_get_project_python_requirement__mutmut_21': x_get_project_python_requirement__mutmut_21, 
    'x_get_project_python_requirement__mutmut_22': x_get_project_python_requirement__mutmut_22, 
    'x_get_project_python_requirement__mutmut_23': x_get_project_python_requirement__mutmut_23, 
    'x_get_project_python_requirement__mutmut_24': x_get_project_python_requirement__mutmut_24
}

def get_project_python_requirement(*args, **kwargs):
    result = _mutmut_trampoline(x_get_project_python_requirement__mutmut_orig, x_get_project_python_requirement__mutmut_mutants, args, kwargs)
    return result 

get_project_python_requirement.__signature__ = _mutmut_signature(x_get_project_python_requirement__mutmut_orig)
x_get_project_python_requirement__mutmut_orig.__name__ = 'x_get_project_python_requirement'


def x_check_python_version_compatibility__mutmut_orig(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = Version(version)
        spec = SpecifierSet(requirement)
        return version_obj in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return True


def x_check_python_version_compatibility__mutmut_1(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = None
        spec = SpecifierSet(requirement)
        return version_obj in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return True


def x_check_python_version_compatibility__mutmut_2(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = Version(None)
        spec = SpecifierSet(requirement)
        return version_obj in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return True


def x_check_python_version_compatibility__mutmut_3(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = Version(version)
        spec = None
        return version_obj in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return True


def x_check_python_version_compatibility__mutmut_4(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = Version(version)
        spec = SpecifierSet(None)
        return version_obj in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return True


def x_check_python_version_compatibility__mutmut_5(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = Version(version)
        spec = SpecifierSet(requirement)
        return version_obj not in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return True


def x_check_python_version_compatibility__mutmut_6(version: str, requirement: str) -> bool:
    """Check if a Python version meets the requirement.

    Args:
        version: Python version string (e.g., "3.11.5")
        requirement: PEP 440 version specifier (e.g., ">=3.11")

    Returns:
        True if version meets requirement
    """
    try:
        version_obj = Version(version)
        spec = SpecifierSet(requirement)
        return version_obj in spec
    except Exception:
        # If we can't parse, assume it's compatible
        return False

x_check_python_version_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_python_version_compatibility__mutmut_1': x_check_python_version_compatibility__mutmut_1, 
    'x_check_python_version_compatibility__mutmut_2': x_check_python_version_compatibility__mutmut_2, 
    'x_check_python_version_compatibility__mutmut_3': x_check_python_version_compatibility__mutmut_3, 
    'x_check_python_version_compatibility__mutmut_4': x_check_python_version_compatibility__mutmut_4, 
    'x_check_python_version_compatibility__mutmut_5': x_check_python_version_compatibility__mutmut_5, 
    'x_check_python_version_compatibility__mutmut_6': x_check_python_version_compatibility__mutmut_6
}

def check_python_version_compatibility(*args, **kwargs):
    result = _mutmut_trampoline(x_check_python_version_compatibility__mutmut_orig, x_check_python_version_compatibility__mutmut_mutants, args, kwargs)
    return result 

check_python_version_compatibility.__signature__ = _mutmut_signature(x_check_python_version_compatibility__mutmut_orig)
x_check_python_version_compatibility__mutmut_orig.__name__ = 'x_check_python_version_compatibility'


def x_should_recreate_venv__mutmut_orig(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_1(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_2(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (True, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_3(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = None

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_4(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(None)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_5(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_6(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (True, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_7(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = None

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_8(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["XXversionXX"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_9(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["VERSION"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_10(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_11(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(None, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_12(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, None):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_13(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_14(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, ):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_15(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            False,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (False, None)


def x_should_recreate_venv__mutmut_16(venv_dir: Path, project_requirement: str | None) -> tuple[bool, str | None]:
    """Determine if virtual environment should be recreated.

    Args:
        venv_dir: Path to virtual environment
        project_requirement: Python version requirement from project

    Returns:
        Tuple of (should_recreate, reason_message)
    """
    if not project_requirement:
        # No requirement specified, don't recreate
        return (False, None)

    version_info = get_venv_python_version(venv_dir)

    if not version_info:
        # No existing venv
        return (False, None)

    venv_version = version_info["version"]

    if not check_python_version_compatibility(venv_version, project_requirement):
        return (
            True,
            f"Virtual environment has Python {venv_version} but project requires {project_requirement}",
        )

    return (True, None)

x_should_recreate_venv__mutmut_mutants : ClassVar[MutantDict] = {
'x_should_recreate_venv__mutmut_1': x_should_recreate_venv__mutmut_1, 
    'x_should_recreate_venv__mutmut_2': x_should_recreate_venv__mutmut_2, 
    'x_should_recreate_venv__mutmut_3': x_should_recreate_venv__mutmut_3, 
    'x_should_recreate_venv__mutmut_4': x_should_recreate_venv__mutmut_4, 
    'x_should_recreate_venv__mutmut_5': x_should_recreate_venv__mutmut_5, 
    'x_should_recreate_venv__mutmut_6': x_should_recreate_venv__mutmut_6, 
    'x_should_recreate_venv__mutmut_7': x_should_recreate_venv__mutmut_7, 
    'x_should_recreate_venv__mutmut_8': x_should_recreate_venv__mutmut_8, 
    'x_should_recreate_venv__mutmut_9': x_should_recreate_venv__mutmut_9, 
    'x_should_recreate_venv__mutmut_10': x_should_recreate_venv__mutmut_10, 
    'x_should_recreate_venv__mutmut_11': x_should_recreate_venv__mutmut_11, 
    'x_should_recreate_venv__mutmut_12': x_should_recreate_venv__mutmut_12, 
    'x_should_recreate_venv__mutmut_13': x_should_recreate_venv__mutmut_13, 
    'x_should_recreate_venv__mutmut_14': x_should_recreate_venv__mutmut_14, 
    'x_should_recreate_venv__mutmut_15': x_should_recreate_venv__mutmut_15, 
    'x_should_recreate_venv__mutmut_16': x_should_recreate_venv__mutmut_16
}

def should_recreate_venv(*args, **kwargs):
    result = _mutmut_trampoline(x_should_recreate_venv__mutmut_orig, x_should_recreate_venv__mutmut_mutants, args, kwargs)
    return result 

should_recreate_venv.__signature__ = _mutmut_signature(x_should_recreate_venv__mutmut_orig)
x_should_recreate_venv__mutmut_orig.__name__ = 'x_should_recreate_venv'


def x_save_venv_python_version__mutmut_orig(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = venv_dir / ".python-version"
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    version_file.write_text(version)


def x_save_venv_python_version__mutmut_1(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = None
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    version_file.write_text(version)


def x_save_venv_python_version__mutmut_2(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = venv_dir * ".python-version"
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    version_file.write_text(version)


def x_save_venv_python_version__mutmut_3(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = venv_dir / "XX.python-versionXX"
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    version_file.write_text(version)


def x_save_venv_python_version__mutmut_4(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = venv_dir / ".PYTHON-VERSION"
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    version_file.write_text(version)


def x_save_venv_python_version__mutmut_5(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = venv_dir / ".python-version"
    version = None
    version_file.write_text(version)


def x_save_venv_python_version__mutmut_6(venv_dir: Path) -> None:
    """Save current Python version to a marker file in venv.

    This is used by the generated shell script to track the Python
    version used to create the venv.
    """
    version_file = venv_dir / ".python-version"
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    version_file.write_text(None)

x_save_venv_python_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_save_venv_python_version__mutmut_1': x_save_venv_python_version__mutmut_1, 
    'x_save_venv_python_version__mutmut_2': x_save_venv_python_version__mutmut_2, 
    'x_save_venv_python_version__mutmut_3': x_save_venv_python_version__mutmut_3, 
    'x_save_venv_python_version__mutmut_4': x_save_venv_python_version__mutmut_4, 
    'x_save_venv_python_version__mutmut_5': x_save_venv_python_version__mutmut_5, 
    'x_save_venv_python_version__mutmut_6': x_save_venv_python_version__mutmut_6
}

def save_venv_python_version(*args, **kwargs):
    result = _mutmut_trampoline(x_save_venv_python_version__mutmut_orig, x_save_venv_python_version__mutmut_mutants, args, kwargs)
    return result 

save_venv_python_version.__signature__ = _mutmut_signature(x_save_venv_python_version__mutmut_orig)
x_save_venv_python_version__mutmut_orig.__name__ = 'x_save_venv_python_version'


def x_read_venv_python_version__mutmut_orig(venv_dir: Path) -> str | None:
    """Read Python version from marker file in venv."""
    version_file = venv_dir / ".python-version"
    if version_file.exists():
        return version_file.read_text().strip()
    return None


def x_read_venv_python_version__mutmut_1(venv_dir: Path) -> str | None:
    """Read Python version from marker file in venv."""
    version_file = None
    if version_file.exists():
        return version_file.read_text().strip()
    return None


def x_read_venv_python_version__mutmut_2(venv_dir: Path) -> str | None:
    """Read Python version from marker file in venv."""
    version_file = venv_dir * ".python-version"
    if version_file.exists():
        return version_file.read_text().strip()
    return None


def x_read_venv_python_version__mutmut_3(venv_dir: Path) -> str | None:
    """Read Python version from marker file in venv."""
    version_file = venv_dir / "XX.python-versionXX"
    if version_file.exists():
        return version_file.read_text().strip()
    return None


def x_read_venv_python_version__mutmut_4(venv_dir: Path) -> str | None:
    """Read Python version from marker file in venv."""
    version_file = venv_dir / ".PYTHON-VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    return None

x_read_venv_python_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_read_venv_python_version__mutmut_1': x_read_venv_python_version__mutmut_1, 
    'x_read_venv_python_version__mutmut_2': x_read_venv_python_version__mutmut_2, 
    'x_read_venv_python_version__mutmut_3': x_read_venv_python_version__mutmut_3, 
    'x_read_venv_python_version__mutmut_4': x_read_venv_python_version__mutmut_4
}

def read_venv_python_version(*args, **kwargs):
    result = _mutmut_trampoline(x_read_venv_python_version__mutmut_orig, x_read_venv_python_version__mutmut_mutants, args, kwargs)
    return result 

read_venv_python_version.__signature__ = _mutmut_signature(x_read_venv_python_version__mutmut_orig)
x_read_venv_python_version__mutmut_orig.__name__ = 'x_read_venv_python_version'


def get_python_version() -> str:
    """Get current Python version string."""
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


# 🧰🌍🔚
