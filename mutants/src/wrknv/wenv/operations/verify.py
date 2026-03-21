#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Verification Operations
========================================
Functions for verifying tool installations."""

from __future__ import annotations

import pathlib

from provide.foundation import logger
from provide.foundation.process import ProcessError, run
from provide.foundation.resilience import retry
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


def x_verify_tool_installation__mutmut_orig(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_1(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_2(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(None)
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_3(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return True

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_4(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = None

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_5(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(None, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_6(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, None)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_7(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_8(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, )

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_9(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is not None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_10(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(None)
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_11(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return True

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_12(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version not in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_13(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(None)
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_14(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return False
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_15(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                None
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_16(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return True

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return False


def x_verify_tool_installation__mutmut_17(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(None)
        return False


def x_verify_tool_installation__mutmut_18(binary_path: pathlib.Path, expected_version: str, tool_name: str) -> bool:
    """Verify that tool installation works and version matches."""

    if not binary_path.exists():
        logger.error(f"{tool_name} binary not found at {binary_path}")
        return False

    try:
        version_output = run_version_check(binary_path, tool_name)

        if version_output is None:
            logger.error(f"{tool_name} version check failed")
            return False

        # Check if expected version is in the output
        if expected_version in version_output:
            if logger.is_debug_enabled():
                logger.debug(f"{tool_name} {expected_version} verification successful")
            return True
        else:
            logger.error(
                f"Version mismatch for {tool_name}: expected {expected_version}, got: {version_output}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify {tool_name} installation: {e}")
        return True

x_verify_tool_installation__mutmut_mutants : ClassVar[MutantDict] = {
'x_verify_tool_installation__mutmut_1': x_verify_tool_installation__mutmut_1, 
    'x_verify_tool_installation__mutmut_2': x_verify_tool_installation__mutmut_2, 
    'x_verify_tool_installation__mutmut_3': x_verify_tool_installation__mutmut_3, 
    'x_verify_tool_installation__mutmut_4': x_verify_tool_installation__mutmut_4, 
    'x_verify_tool_installation__mutmut_5': x_verify_tool_installation__mutmut_5, 
    'x_verify_tool_installation__mutmut_6': x_verify_tool_installation__mutmut_6, 
    'x_verify_tool_installation__mutmut_7': x_verify_tool_installation__mutmut_7, 
    'x_verify_tool_installation__mutmut_8': x_verify_tool_installation__mutmut_8, 
    'x_verify_tool_installation__mutmut_9': x_verify_tool_installation__mutmut_9, 
    'x_verify_tool_installation__mutmut_10': x_verify_tool_installation__mutmut_10, 
    'x_verify_tool_installation__mutmut_11': x_verify_tool_installation__mutmut_11, 
    'x_verify_tool_installation__mutmut_12': x_verify_tool_installation__mutmut_12, 
    'x_verify_tool_installation__mutmut_13': x_verify_tool_installation__mutmut_13, 
    'x_verify_tool_installation__mutmut_14': x_verify_tool_installation__mutmut_14, 
    'x_verify_tool_installation__mutmut_15': x_verify_tool_installation__mutmut_15, 
    'x_verify_tool_installation__mutmut_16': x_verify_tool_installation__mutmut_16, 
    'x_verify_tool_installation__mutmut_17': x_verify_tool_installation__mutmut_17, 
    'x_verify_tool_installation__mutmut_18': x_verify_tool_installation__mutmut_18
}

def verify_tool_installation(*args, **kwargs):
    result = _mutmut_trampoline(x_verify_tool_installation__mutmut_orig, x_verify_tool_installation__mutmut_mutants, args, kwargs)
    return result 

verify_tool_installation.__signature__ = _mutmut_signature(x_verify_tool_installation__mutmut_orig)
x_verify_tool_installation__mutmut_orig.__name__ = 'x_verify_tool_installation'


@retry(ProcessError, OSError, max_attempts=3, base_delay=1.0)
def run_version_check(binary_path: pathlib.Path, tool_name: str, timeout: int = 10) -> str | None:
    """Run version check command for a tool and return output.

    Includes automatic retry with exponential backoff for transient failures.
    """

    if not binary_path.exists():
        return None

    # Determine version command for different tools
    version_args = get_version_command_args(tool_name)

    cmd = [str(binary_path), *version_args]

    try:
        if logger.is_debug_enabled():
            logger.debug(f"Running version check: {' '.join(cmd)}")

        result = run(cmd, timeout=timeout)

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            logger.error(f"Version command failed for {tool_name}: {result.stderr}")
            return None

    except ProcessError as e:
        if e.timeout:
            logger.error(f"Version check timed out for {tool_name}")
        else:
            logger.error(f"Version check failed for {tool_name}: {e}")
        raise  # Re-raise to trigger retry
    except Exception as e:
        logger.error(f"Version check failed for {tool_name}: {e}")
        return None


def x_get_version_command_args__mutmut_orig(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_1(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = None

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_2(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "XXterraformXX": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_3(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "TERRAFORM": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_4(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["XXversionXX"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_5(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["VERSION"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_6(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "XXtofuXX": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_7(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "TOFU": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_8(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["XXversionXX"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_9(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["VERSION"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_10(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "XXgoXX": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_11(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "GO": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_12(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["XXversionXX"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_13(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["VERSION"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_14(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "XXuvXX": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_15(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "UV": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_16(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["XX--versionXX"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_17(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--VERSION"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_18(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "XXpythonXX": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_19(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "PYTHON": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_20(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["XX--versionXX"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_21(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--VERSION"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_22(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "XXnodeXX": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_23(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "NODE": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_24(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["XX--versionXX"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_25(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--VERSION"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_26(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "XXnpmXX": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_27(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "NPM": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_28(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["XX--versionXX"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_29(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--VERSION"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_30(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "XXdockerXX": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_31(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "DOCKER": ["--version"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_32(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["XX--versionXX"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_33(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--VERSION"],
    }

    return version_commands.get(tool_name, ["--version"])


def x_get_version_command_args__mutmut_34(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(None, ["--version"])


def x_get_version_command_args__mutmut_35(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, None)


def x_get_version_command_args__mutmut_36(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(["--version"])


def x_get_version_command_args__mutmut_37(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, )


def x_get_version_command_args__mutmut_38(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["XX--versionXX"])


def x_get_version_command_args__mutmut_39(tool_name: str) -> list[str]:
    """Get version command arguments for different tools."""

    # Map tool names to their version command arguments
    version_commands = {
        "terraform": ["version"],
        "tofu": ["version"],
        "go": ["version"],
        "uv": ["--version"],
        "python": ["--version"],
        "node": ["--version"],
        "npm": ["--version"],
        "docker": ["--version"],
    }

    return version_commands.get(tool_name, ["--VERSION"])

x_get_version_command_args__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_version_command_args__mutmut_1': x_get_version_command_args__mutmut_1, 
    'x_get_version_command_args__mutmut_2': x_get_version_command_args__mutmut_2, 
    'x_get_version_command_args__mutmut_3': x_get_version_command_args__mutmut_3, 
    'x_get_version_command_args__mutmut_4': x_get_version_command_args__mutmut_4, 
    'x_get_version_command_args__mutmut_5': x_get_version_command_args__mutmut_5, 
    'x_get_version_command_args__mutmut_6': x_get_version_command_args__mutmut_6, 
    'x_get_version_command_args__mutmut_7': x_get_version_command_args__mutmut_7, 
    'x_get_version_command_args__mutmut_8': x_get_version_command_args__mutmut_8, 
    'x_get_version_command_args__mutmut_9': x_get_version_command_args__mutmut_9, 
    'x_get_version_command_args__mutmut_10': x_get_version_command_args__mutmut_10, 
    'x_get_version_command_args__mutmut_11': x_get_version_command_args__mutmut_11, 
    'x_get_version_command_args__mutmut_12': x_get_version_command_args__mutmut_12, 
    'x_get_version_command_args__mutmut_13': x_get_version_command_args__mutmut_13, 
    'x_get_version_command_args__mutmut_14': x_get_version_command_args__mutmut_14, 
    'x_get_version_command_args__mutmut_15': x_get_version_command_args__mutmut_15, 
    'x_get_version_command_args__mutmut_16': x_get_version_command_args__mutmut_16, 
    'x_get_version_command_args__mutmut_17': x_get_version_command_args__mutmut_17, 
    'x_get_version_command_args__mutmut_18': x_get_version_command_args__mutmut_18, 
    'x_get_version_command_args__mutmut_19': x_get_version_command_args__mutmut_19, 
    'x_get_version_command_args__mutmut_20': x_get_version_command_args__mutmut_20, 
    'x_get_version_command_args__mutmut_21': x_get_version_command_args__mutmut_21, 
    'x_get_version_command_args__mutmut_22': x_get_version_command_args__mutmut_22, 
    'x_get_version_command_args__mutmut_23': x_get_version_command_args__mutmut_23, 
    'x_get_version_command_args__mutmut_24': x_get_version_command_args__mutmut_24, 
    'x_get_version_command_args__mutmut_25': x_get_version_command_args__mutmut_25, 
    'x_get_version_command_args__mutmut_26': x_get_version_command_args__mutmut_26, 
    'x_get_version_command_args__mutmut_27': x_get_version_command_args__mutmut_27, 
    'x_get_version_command_args__mutmut_28': x_get_version_command_args__mutmut_28, 
    'x_get_version_command_args__mutmut_29': x_get_version_command_args__mutmut_29, 
    'x_get_version_command_args__mutmut_30': x_get_version_command_args__mutmut_30, 
    'x_get_version_command_args__mutmut_31': x_get_version_command_args__mutmut_31, 
    'x_get_version_command_args__mutmut_32': x_get_version_command_args__mutmut_32, 
    'x_get_version_command_args__mutmut_33': x_get_version_command_args__mutmut_33, 
    'x_get_version_command_args__mutmut_34': x_get_version_command_args__mutmut_34, 
    'x_get_version_command_args__mutmut_35': x_get_version_command_args__mutmut_35, 
    'x_get_version_command_args__mutmut_36': x_get_version_command_args__mutmut_36, 
    'x_get_version_command_args__mutmut_37': x_get_version_command_args__mutmut_37, 
    'x_get_version_command_args__mutmut_38': x_get_version_command_args__mutmut_38, 
    'x_get_version_command_args__mutmut_39': x_get_version_command_args__mutmut_39
}

def get_version_command_args(*args, **kwargs):
    result = _mutmut_trampoline(x_get_version_command_args__mutmut_orig, x_get_version_command_args__mutmut_mutants, args, kwargs)
    return result 

get_version_command_args.__signature__ = _mutmut_signature(x_get_version_command_args__mutmut_orig)
x_get_version_command_args__mutmut_orig.__name__ = 'x_get_version_command_args'


def x_check_binary_compatibility__mutmut_orig(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_1(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_2(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"XXcompatibleXX": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_3(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"COMPATIBLE": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_4(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": True, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_5(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "XXerrorXX": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_6(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "ERROR": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_7(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "XXBinary not foundXX"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_8(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_9(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "BINARY NOT FOUND"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_10(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = None

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_11(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run(None, timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_12(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=None)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_13(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run(timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_14(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], )

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_15(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(None), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_16(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "XX--helpXX"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_17(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--HELP"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_18(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=6)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_19(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = None

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_20(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode != 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_21(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 1

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_22(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "XXcompatibleXX": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_23(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "COMPATIBLE": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_24(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "XXreturncodeXX": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_25(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "RETURNCODE": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_26(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "XXstdoutXX": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_27(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "STDOUT": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_28(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:201] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_29(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "XXXX",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_30(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "XXstderrXX": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_31(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "STDERR": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_32(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:201] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_33(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "XXXX",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_34(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"XXcompatibleXX": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_35(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"COMPATIBLE": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_36(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": True, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_37(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "XXerrorXX": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_38(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "ERROR": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_39(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "XXBinary execution timed outXX"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_40(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_41(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "BINARY EXECUTION TIMED OUT"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_42(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"XXcompatibleXX": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_43(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"COMPATIBLE": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_44(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": True, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_45(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "XXerrorXX": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_46(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "ERROR": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_47(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(None)}
    except Exception as e:
        return {"compatible": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_48(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"XXcompatibleXX": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_49(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"COMPATIBLE": False, "error": str(e)}


def x_check_binary_compatibility__mutmut_50(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": True, "error": str(e)}


def x_check_binary_compatibility__mutmut_51(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "XXerrorXX": str(e)}


def x_check_binary_compatibility__mutmut_52(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "ERROR": str(e)}


def x_check_binary_compatibility__mutmut_53(binary_path: pathlib.Path) -> dict[str, any]:
    """Check if binary is compatible with current platform."""

    if not binary_path.exists():
        return {"compatible": False, "error": "Binary not found"}

    try:
        # Try to run the binary with help/version flag
        result = run([str(binary_path), "--help"], timeout=5)

        # If it runs without error, it's likely compatible
        compatible = result.returncode == 0

        return {
            "compatible": compatible,
            "returncode": result.returncode,
            "stdout": result.stdout[:200] if result.stdout else "",
            "stderr": result.stderr[:200] if result.stderr else "",
        }

    except ProcessError as e:
        if e.timeout:
            return {"compatible": False, "error": "Binary execution timed out"}
        else:
            return {"compatible": False, "error": str(e)}
    except Exception as e:
        return {"compatible": False, "error": str(None)}

x_check_binary_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_binary_compatibility__mutmut_1': x_check_binary_compatibility__mutmut_1, 
    'x_check_binary_compatibility__mutmut_2': x_check_binary_compatibility__mutmut_2, 
    'x_check_binary_compatibility__mutmut_3': x_check_binary_compatibility__mutmut_3, 
    'x_check_binary_compatibility__mutmut_4': x_check_binary_compatibility__mutmut_4, 
    'x_check_binary_compatibility__mutmut_5': x_check_binary_compatibility__mutmut_5, 
    'x_check_binary_compatibility__mutmut_6': x_check_binary_compatibility__mutmut_6, 
    'x_check_binary_compatibility__mutmut_7': x_check_binary_compatibility__mutmut_7, 
    'x_check_binary_compatibility__mutmut_8': x_check_binary_compatibility__mutmut_8, 
    'x_check_binary_compatibility__mutmut_9': x_check_binary_compatibility__mutmut_9, 
    'x_check_binary_compatibility__mutmut_10': x_check_binary_compatibility__mutmut_10, 
    'x_check_binary_compatibility__mutmut_11': x_check_binary_compatibility__mutmut_11, 
    'x_check_binary_compatibility__mutmut_12': x_check_binary_compatibility__mutmut_12, 
    'x_check_binary_compatibility__mutmut_13': x_check_binary_compatibility__mutmut_13, 
    'x_check_binary_compatibility__mutmut_14': x_check_binary_compatibility__mutmut_14, 
    'x_check_binary_compatibility__mutmut_15': x_check_binary_compatibility__mutmut_15, 
    'x_check_binary_compatibility__mutmut_16': x_check_binary_compatibility__mutmut_16, 
    'x_check_binary_compatibility__mutmut_17': x_check_binary_compatibility__mutmut_17, 
    'x_check_binary_compatibility__mutmut_18': x_check_binary_compatibility__mutmut_18, 
    'x_check_binary_compatibility__mutmut_19': x_check_binary_compatibility__mutmut_19, 
    'x_check_binary_compatibility__mutmut_20': x_check_binary_compatibility__mutmut_20, 
    'x_check_binary_compatibility__mutmut_21': x_check_binary_compatibility__mutmut_21, 
    'x_check_binary_compatibility__mutmut_22': x_check_binary_compatibility__mutmut_22, 
    'x_check_binary_compatibility__mutmut_23': x_check_binary_compatibility__mutmut_23, 
    'x_check_binary_compatibility__mutmut_24': x_check_binary_compatibility__mutmut_24, 
    'x_check_binary_compatibility__mutmut_25': x_check_binary_compatibility__mutmut_25, 
    'x_check_binary_compatibility__mutmut_26': x_check_binary_compatibility__mutmut_26, 
    'x_check_binary_compatibility__mutmut_27': x_check_binary_compatibility__mutmut_27, 
    'x_check_binary_compatibility__mutmut_28': x_check_binary_compatibility__mutmut_28, 
    'x_check_binary_compatibility__mutmut_29': x_check_binary_compatibility__mutmut_29, 
    'x_check_binary_compatibility__mutmut_30': x_check_binary_compatibility__mutmut_30, 
    'x_check_binary_compatibility__mutmut_31': x_check_binary_compatibility__mutmut_31, 
    'x_check_binary_compatibility__mutmut_32': x_check_binary_compatibility__mutmut_32, 
    'x_check_binary_compatibility__mutmut_33': x_check_binary_compatibility__mutmut_33, 
    'x_check_binary_compatibility__mutmut_34': x_check_binary_compatibility__mutmut_34, 
    'x_check_binary_compatibility__mutmut_35': x_check_binary_compatibility__mutmut_35, 
    'x_check_binary_compatibility__mutmut_36': x_check_binary_compatibility__mutmut_36, 
    'x_check_binary_compatibility__mutmut_37': x_check_binary_compatibility__mutmut_37, 
    'x_check_binary_compatibility__mutmut_38': x_check_binary_compatibility__mutmut_38, 
    'x_check_binary_compatibility__mutmut_39': x_check_binary_compatibility__mutmut_39, 
    'x_check_binary_compatibility__mutmut_40': x_check_binary_compatibility__mutmut_40, 
    'x_check_binary_compatibility__mutmut_41': x_check_binary_compatibility__mutmut_41, 
    'x_check_binary_compatibility__mutmut_42': x_check_binary_compatibility__mutmut_42, 
    'x_check_binary_compatibility__mutmut_43': x_check_binary_compatibility__mutmut_43, 
    'x_check_binary_compatibility__mutmut_44': x_check_binary_compatibility__mutmut_44, 
    'x_check_binary_compatibility__mutmut_45': x_check_binary_compatibility__mutmut_45, 
    'x_check_binary_compatibility__mutmut_46': x_check_binary_compatibility__mutmut_46, 
    'x_check_binary_compatibility__mutmut_47': x_check_binary_compatibility__mutmut_47, 
    'x_check_binary_compatibility__mutmut_48': x_check_binary_compatibility__mutmut_48, 
    'x_check_binary_compatibility__mutmut_49': x_check_binary_compatibility__mutmut_49, 
    'x_check_binary_compatibility__mutmut_50': x_check_binary_compatibility__mutmut_50, 
    'x_check_binary_compatibility__mutmut_51': x_check_binary_compatibility__mutmut_51, 
    'x_check_binary_compatibility__mutmut_52': x_check_binary_compatibility__mutmut_52, 
    'x_check_binary_compatibility__mutmut_53': x_check_binary_compatibility__mutmut_53
}

def check_binary_compatibility(*args, **kwargs):
    result = _mutmut_trampoline(x_check_binary_compatibility__mutmut_orig, x_check_binary_compatibility__mutmut_mutants, args, kwargs)
    return result 

check_binary_compatibility.__signature__ = _mutmut_signature(x_check_binary_compatibility__mutmut_orig)
x_check_binary_compatibility__mutmut_orig.__name__ = 'x_check_binary_compatibility'


def x_validate_installation_directory__mutmut_orig(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_1(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_2(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(None)
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_3(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return True

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_4(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = None
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_5(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir * "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_6(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "XXbinXX"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_7(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "BIN"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_8(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_9(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(None)
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_10(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return True

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_11(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = None
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_12(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name - get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_13(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = None

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_14(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir * executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_15(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_16(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(None)
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_17(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return True

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_18(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_19(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(None):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_20(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(None)
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_21(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return True

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return True


def x_validate_installation_directory__mutmut_22(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(None)
    return True


def x_validate_installation_directory__mutmut_23(install_dir: pathlib.Path, tool_name: str, version: str) -> bool:
    """Validate that installation directory has expected structure."""

    if not install_dir.exists():
        logger.error(f"Installation directory not found: {install_dir}")
        return False

    # Check for bin directory
    bin_dir = install_dir / "bin"
    if not bin_dir.exists():
        logger.error(f"Bin directory not found: {bin_dir}")
        return False

    # Check for expected binary
    from ..operations.platform import get_executable_extension

    executable_name = tool_name + get_executable_extension()
    binary_path = bin_dir / executable_name

    if not binary_path.exists():
        logger.error(f"Binary not found: {binary_path}")
        return False

    # Check if binary is executable
    from ..operations.install import is_executable

    if not is_executable(binary_path):
        logger.error(f"Binary is not executable: {binary_path}")
        return False

    if logger.is_debug_enabled():
        logger.debug(f"Installation directory validation passed for {tool_name} {version}")
    return False

x_validate_installation_directory__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_installation_directory__mutmut_1': x_validate_installation_directory__mutmut_1, 
    'x_validate_installation_directory__mutmut_2': x_validate_installation_directory__mutmut_2, 
    'x_validate_installation_directory__mutmut_3': x_validate_installation_directory__mutmut_3, 
    'x_validate_installation_directory__mutmut_4': x_validate_installation_directory__mutmut_4, 
    'x_validate_installation_directory__mutmut_5': x_validate_installation_directory__mutmut_5, 
    'x_validate_installation_directory__mutmut_6': x_validate_installation_directory__mutmut_6, 
    'x_validate_installation_directory__mutmut_7': x_validate_installation_directory__mutmut_7, 
    'x_validate_installation_directory__mutmut_8': x_validate_installation_directory__mutmut_8, 
    'x_validate_installation_directory__mutmut_9': x_validate_installation_directory__mutmut_9, 
    'x_validate_installation_directory__mutmut_10': x_validate_installation_directory__mutmut_10, 
    'x_validate_installation_directory__mutmut_11': x_validate_installation_directory__mutmut_11, 
    'x_validate_installation_directory__mutmut_12': x_validate_installation_directory__mutmut_12, 
    'x_validate_installation_directory__mutmut_13': x_validate_installation_directory__mutmut_13, 
    'x_validate_installation_directory__mutmut_14': x_validate_installation_directory__mutmut_14, 
    'x_validate_installation_directory__mutmut_15': x_validate_installation_directory__mutmut_15, 
    'x_validate_installation_directory__mutmut_16': x_validate_installation_directory__mutmut_16, 
    'x_validate_installation_directory__mutmut_17': x_validate_installation_directory__mutmut_17, 
    'x_validate_installation_directory__mutmut_18': x_validate_installation_directory__mutmut_18, 
    'x_validate_installation_directory__mutmut_19': x_validate_installation_directory__mutmut_19, 
    'x_validate_installation_directory__mutmut_20': x_validate_installation_directory__mutmut_20, 
    'x_validate_installation_directory__mutmut_21': x_validate_installation_directory__mutmut_21, 
    'x_validate_installation_directory__mutmut_22': x_validate_installation_directory__mutmut_22, 
    'x_validate_installation_directory__mutmut_23': x_validate_installation_directory__mutmut_23
}

def validate_installation_directory(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_installation_directory__mutmut_orig, x_validate_installation_directory__mutmut_mutants, args, kwargs)
    return result 

validate_installation_directory.__signature__ = _mutmut_signature(x_validate_installation_directory__mutmut_orig)
x_validate_installation_directory__mutmut_orig.__name__ = 'x_validate_installation_directory'


def x_get_installed_version_info__mutmut_orig(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_1(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = None

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_2(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(None, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_3(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, None)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_4(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_5(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, )

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_6(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_7(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name != "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_8(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "XXterraformXX":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_9(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "TERRAFORM":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_10(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(None)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_11(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name != "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_12(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "XXtofuXX":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_13(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "TOFU":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_14(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(None)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_15(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name != "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_16(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "XXgoXX":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_17(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "GO":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_18(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(None)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_19(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name != "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_20(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "XXuvXX":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_21(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "UV":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_22(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(None)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, tool_name)


def x_get_installed_version_info__mutmut_23(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(None, tool_name)


def x_get_installed_version_info__mutmut_24(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, None)


def x_get_installed_version_info__mutmut_25(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(tool_name)


def x_get_installed_version_info__mutmut_26(binary_path: pathlib.Path, tool_name: str) -> dict[str, str] | None:
    """Get detailed version information from installed tool."""

    version_output = run_version_check(binary_path, tool_name)

    if not version_output:
        return None

    # Parse version information based on tool
    if tool_name == "terraform":
        return parse_terraform_version(version_output)
    elif tool_name == "tofu":
        return parse_tofu_version(version_output)
    elif tool_name == "go":
        return parse_go_version(version_output)
    elif tool_name == "uv":
        return parse_uv_version(version_output)
    else:
        # Generic version parsing
        return parse_generic_version(version_output, )

x_get_installed_version_info__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_installed_version_info__mutmut_1': x_get_installed_version_info__mutmut_1, 
    'x_get_installed_version_info__mutmut_2': x_get_installed_version_info__mutmut_2, 
    'x_get_installed_version_info__mutmut_3': x_get_installed_version_info__mutmut_3, 
    'x_get_installed_version_info__mutmut_4': x_get_installed_version_info__mutmut_4, 
    'x_get_installed_version_info__mutmut_5': x_get_installed_version_info__mutmut_5, 
    'x_get_installed_version_info__mutmut_6': x_get_installed_version_info__mutmut_6, 
    'x_get_installed_version_info__mutmut_7': x_get_installed_version_info__mutmut_7, 
    'x_get_installed_version_info__mutmut_8': x_get_installed_version_info__mutmut_8, 
    'x_get_installed_version_info__mutmut_9': x_get_installed_version_info__mutmut_9, 
    'x_get_installed_version_info__mutmut_10': x_get_installed_version_info__mutmut_10, 
    'x_get_installed_version_info__mutmut_11': x_get_installed_version_info__mutmut_11, 
    'x_get_installed_version_info__mutmut_12': x_get_installed_version_info__mutmut_12, 
    'x_get_installed_version_info__mutmut_13': x_get_installed_version_info__mutmut_13, 
    'x_get_installed_version_info__mutmut_14': x_get_installed_version_info__mutmut_14, 
    'x_get_installed_version_info__mutmut_15': x_get_installed_version_info__mutmut_15, 
    'x_get_installed_version_info__mutmut_16': x_get_installed_version_info__mutmut_16, 
    'x_get_installed_version_info__mutmut_17': x_get_installed_version_info__mutmut_17, 
    'x_get_installed_version_info__mutmut_18': x_get_installed_version_info__mutmut_18, 
    'x_get_installed_version_info__mutmut_19': x_get_installed_version_info__mutmut_19, 
    'x_get_installed_version_info__mutmut_20': x_get_installed_version_info__mutmut_20, 
    'x_get_installed_version_info__mutmut_21': x_get_installed_version_info__mutmut_21, 
    'x_get_installed_version_info__mutmut_22': x_get_installed_version_info__mutmut_22, 
    'x_get_installed_version_info__mutmut_23': x_get_installed_version_info__mutmut_23, 
    'x_get_installed_version_info__mutmut_24': x_get_installed_version_info__mutmut_24, 
    'x_get_installed_version_info__mutmut_25': x_get_installed_version_info__mutmut_25, 
    'x_get_installed_version_info__mutmut_26': x_get_installed_version_info__mutmut_26
}

def get_installed_version_info(*args, **kwargs):
    result = _mutmut_trampoline(x_get_installed_version_info__mutmut_orig, x_get_installed_version_info__mutmut_mutants, args, kwargs)
    return result 

get_installed_version_info.__signature__ = _mutmut_signature(x_get_installed_version_info__mutmut_orig)
x_get_installed_version_info__mutmut_orig.__name__ = 'x_get_installed_version_info'


def x_parse_terraform_version__mutmut_orig(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_1(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = None

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_2(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split(None)

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_3(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("XX\nXX")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_4(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = None

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_5(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"XXtoolXX": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_6(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"TOOL": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_7(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "XXterraformXX"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_8(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "TERRAFORM"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_9(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = None
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_10(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith(None):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_11(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("XXTerraform vXX"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_12(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_13(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("TERRAFORM V"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_14(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = None
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_15(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace(None, "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_16(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", None)
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_17(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_18(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", )
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_19(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("XXTerraform vXX", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_20(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_21(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("TERRAFORM V", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_22(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "XXXX")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_23(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = None
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_24(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["XXversionXX"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_25(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["VERSION"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_26(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith(None):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_27(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("XXon XX"):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_28(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("ON "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_29(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = None

    return info


def x_parse_terraform_version__mutmut_30(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["XXplatformXX"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_31(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["PLATFORM"] = line.replace("on ", "").strip()

    return info


def x_parse_terraform_version__mutmut_32(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace(None, "").strip()

    return info


def x_parse_terraform_version__mutmut_33(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", None).strip()

    return info


def x_parse_terraform_version__mutmut_34(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("").strip()

    return info


def x_parse_terraform_version__mutmut_35(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", ).strip()

    return info


def x_parse_terraform_version__mutmut_36(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("XXon XX", "").strip()

    return info


def x_parse_terraform_version__mutmut_37(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("ON ", "").strip()

    return info


def x_parse_terraform_version__mutmut_38(output: str) -> dict[str, str]:
    """Parse Terraform version output."""

    # Example: "Terraform v1.5.0"
    lines = output.split("\n")

    info = {"tool": "terraform"}

    for line in lines:
        line = line.strip()
        if line.startswith("Terraform v"):
            version = line.replace("Terraform v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on linux_amd64" format
            info["platform"] = line.replace("on ", "XXXX").strip()

    return info

x_parse_terraform_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_terraform_version__mutmut_1': x_parse_terraform_version__mutmut_1, 
    'x_parse_terraform_version__mutmut_2': x_parse_terraform_version__mutmut_2, 
    'x_parse_terraform_version__mutmut_3': x_parse_terraform_version__mutmut_3, 
    'x_parse_terraform_version__mutmut_4': x_parse_terraform_version__mutmut_4, 
    'x_parse_terraform_version__mutmut_5': x_parse_terraform_version__mutmut_5, 
    'x_parse_terraform_version__mutmut_6': x_parse_terraform_version__mutmut_6, 
    'x_parse_terraform_version__mutmut_7': x_parse_terraform_version__mutmut_7, 
    'x_parse_terraform_version__mutmut_8': x_parse_terraform_version__mutmut_8, 
    'x_parse_terraform_version__mutmut_9': x_parse_terraform_version__mutmut_9, 
    'x_parse_terraform_version__mutmut_10': x_parse_terraform_version__mutmut_10, 
    'x_parse_terraform_version__mutmut_11': x_parse_terraform_version__mutmut_11, 
    'x_parse_terraform_version__mutmut_12': x_parse_terraform_version__mutmut_12, 
    'x_parse_terraform_version__mutmut_13': x_parse_terraform_version__mutmut_13, 
    'x_parse_terraform_version__mutmut_14': x_parse_terraform_version__mutmut_14, 
    'x_parse_terraform_version__mutmut_15': x_parse_terraform_version__mutmut_15, 
    'x_parse_terraform_version__mutmut_16': x_parse_terraform_version__mutmut_16, 
    'x_parse_terraform_version__mutmut_17': x_parse_terraform_version__mutmut_17, 
    'x_parse_terraform_version__mutmut_18': x_parse_terraform_version__mutmut_18, 
    'x_parse_terraform_version__mutmut_19': x_parse_terraform_version__mutmut_19, 
    'x_parse_terraform_version__mutmut_20': x_parse_terraform_version__mutmut_20, 
    'x_parse_terraform_version__mutmut_21': x_parse_terraform_version__mutmut_21, 
    'x_parse_terraform_version__mutmut_22': x_parse_terraform_version__mutmut_22, 
    'x_parse_terraform_version__mutmut_23': x_parse_terraform_version__mutmut_23, 
    'x_parse_terraform_version__mutmut_24': x_parse_terraform_version__mutmut_24, 
    'x_parse_terraform_version__mutmut_25': x_parse_terraform_version__mutmut_25, 
    'x_parse_terraform_version__mutmut_26': x_parse_terraform_version__mutmut_26, 
    'x_parse_terraform_version__mutmut_27': x_parse_terraform_version__mutmut_27, 
    'x_parse_terraform_version__mutmut_28': x_parse_terraform_version__mutmut_28, 
    'x_parse_terraform_version__mutmut_29': x_parse_terraform_version__mutmut_29, 
    'x_parse_terraform_version__mutmut_30': x_parse_terraform_version__mutmut_30, 
    'x_parse_terraform_version__mutmut_31': x_parse_terraform_version__mutmut_31, 
    'x_parse_terraform_version__mutmut_32': x_parse_terraform_version__mutmut_32, 
    'x_parse_terraform_version__mutmut_33': x_parse_terraform_version__mutmut_33, 
    'x_parse_terraform_version__mutmut_34': x_parse_terraform_version__mutmut_34, 
    'x_parse_terraform_version__mutmut_35': x_parse_terraform_version__mutmut_35, 
    'x_parse_terraform_version__mutmut_36': x_parse_terraform_version__mutmut_36, 
    'x_parse_terraform_version__mutmut_37': x_parse_terraform_version__mutmut_37, 
    'x_parse_terraform_version__mutmut_38': x_parse_terraform_version__mutmut_38
}

def parse_terraform_version(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_terraform_version__mutmut_orig, x_parse_terraform_version__mutmut_mutants, args, kwargs)
    return result 

parse_terraform_version.__signature__ = _mutmut_signature(x_parse_terraform_version__mutmut_orig)
x_parse_terraform_version__mutmut_orig.__name__ = 'x_parse_terraform_version'


def x_parse_tofu_version__mutmut_orig(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_1(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = None

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_2(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split(None)

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_3(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("XX\nXX")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_4(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = None

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_5(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"XXtoolXX": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_6(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"TOOL": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_7(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "XXtofuXX"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_8(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "TOFU"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_9(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = None
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_10(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith(None):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_11(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("XXOpenTofu vXX"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_12(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("opentofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_13(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OPENTOFU V"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_14(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = None
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_15(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace(None, "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_16(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", None)
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_17(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_18(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", )
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_19(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("XXOpenTofu vXX", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_20(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("opentofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_21(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OPENTOFU V", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_22(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "XXXX")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_23(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = None
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_24(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["XXversionXX"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_25(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["VERSION"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_26(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith(None):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_27(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("XXon XX"):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_28(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("ON "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_29(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = None

    return info


def x_parse_tofu_version__mutmut_30(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["XXplatformXX"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_31(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["PLATFORM"] = line.replace("on ", "").strip()

    return info


def x_parse_tofu_version__mutmut_32(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace(None, "").strip()

    return info


def x_parse_tofu_version__mutmut_33(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", None).strip()

    return info


def x_parse_tofu_version__mutmut_34(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("").strip()

    return info


def x_parse_tofu_version__mutmut_35(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", ).strip()

    return info


def x_parse_tofu_version__mutmut_36(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("XXon XX", "").strip()

    return info


def x_parse_tofu_version__mutmut_37(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("ON ", "").strip()

    return info


def x_parse_tofu_version__mutmut_38(output: str) -> dict[str, str]:
    """Parse OpenTofu version output."""

    # Example: "OpenTofu v1.6.0"
    lines = output.split("\n")

    info = {"tool": "tofu"}

    for line in lines:
        line = line.strip()
        if line.startswith("OpenTofu v"):
            version = line.replace("OpenTofu v", "")
            info["version"] = version
        elif line.startswith("on "):
            # Extract platform from "on darwin_arm64" format
            info["platform"] = line.replace("on ", "XXXX").strip()

    return info

x_parse_tofu_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_tofu_version__mutmut_1': x_parse_tofu_version__mutmut_1, 
    'x_parse_tofu_version__mutmut_2': x_parse_tofu_version__mutmut_2, 
    'x_parse_tofu_version__mutmut_3': x_parse_tofu_version__mutmut_3, 
    'x_parse_tofu_version__mutmut_4': x_parse_tofu_version__mutmut_4, 
    'x_parse_tofu_version__mutmut_5': x_parse_tofu_version__mutmut_5, 
    'x_parse_tofu_version__mutmut_6': x_parse_tofu_version__mutmut_6, 
    'x_parse_tofu_version__mutmut_7': x_parse_tofu_version__mutmut_7, 
    'x_parse_tofu_version__mutmut_8': x_parse_tofu_version__mutmut_8, 
    'x_parse_tofu_version__mutmut_9': x_parse_tofu_version__mutmut_9, 
    'x_parse_tofu_version__mutmut_10': x_parse_tofu_version__mutmut_10, 
    'x_parse_tofu_version__mutmut_11': x_parse_tofu_version__mutmut_11, 
    'x_parse_tofu_version__mutmut_12': x_parse_tofu_version__mutmut_12, 
    'x_parse_tofu_version__mutmut_13': x_parse_tofu_version__mutmut_13, 
    'x_parse_tofu_version__mutmut_14': x_parse_tofu_version__mutmut_14, 
    'x_parse_tofu_version__mutmut_15': x_parse_tofu_version__mutmut_15, 
    'x_parse_tofu_version__mutmut_16': x_parse_tofu_version__mutmut_16, 
    'x_parse_tofu_version__mutmut_17': x_parse_tofu_version__mutmut_17, 
    'x_parse_tofu_version__mutmut_18': x_parse_tofu_version__mutmut_18, 
    'x_parse_tofu_version__mutmut_19': x_parse_tofu_version__mutmut_19, 
    'x_parse_tofu_version__mutmut_20': x_parse_tofu_version__mutmut_20, 
    'x_parse_tofu_version__mutmut_21': x_parse_tofu_version__mutmut_21, 
    'x_parse_tofu_version__mutmut_22': x_parse_tofu_version__mutmut_22, 
    'x_parse_tofu_version__mutmut_23': x_parse_tofu_version__mutmut_23, 
    'x_parse_tofu_version__mutmut_24': x_parse_tofu_version__mutmut_24, 
    'x_parse_tofu_version__mutmut_25': x_parse_tofu_version__mutmut_25, 
    'x_parse_tofu_version__mutmut_26': x_parse_tofu_version__mutmut_26, 
    'x_parse_tofu_version__mutmut_27': x_parse_tofu_version__mutmut_27, 
    'x_parse_tofu_version__mutmut_28': x_parse_tofu_version__mutmut_28, 
    'x_parse_tofu_version__mutmut_29': x_parse_tofu_version__mutmut_29, 
    'x_parse_tofu_version__mutmut_30': x_parse_tofu_version__mutmut_30, 
    'x_parse_tofu_version__mutmut_31': x_parse_tofu_version__mutmut_31, 
    'x_parse_tofu_version__mutmut_32': x_parse_tofu_version__mutmut_32, 
    'x_parse_tofu_version__mutmut_33': x_parse_tofu_version__mutmut_33, 
    'x_parse_tofu_version__mutmut_34': x_parse_tofu_version__mutmut_34, 
    'x_parse_tofu_version__mutmut_35': x_parse_tofu_version__mutmut_35, 
    'x_parse_tofu_version__mutmut_36': x_parse_tofu_version__mutmut_36, 
    'x_parse_tofu_version__mutmut_37': x_parse_tofu_version__mutmut_37, 
    'x_parse_tofu_version__mutmut_38': x_parse_tofu_version__mutmut_38
}

def parse_tofu_version(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_tofu_version__mutmut_orig, x_parse_tofu_version__mutmut_mutants, args, kwargs)
    return result 

parse_tofu_version.__signature__ = _mutmut_signature(x_parse_tofu_version__mutmut_orig)
x_parse_tofu_version__mutmut_orig.__name__ = 'x_parse_tofu_version'


def x_parse_go_version__mutmut_orig(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_1(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = None

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_2(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"XXtoolXX": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_3(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"TOOL": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_4(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "XXgoXX"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_5(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "GO"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_6(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = None
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_7(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) > 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_8(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 4:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_9(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = None
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_10(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[3]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_11(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith(None):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_12(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("XXgoXX"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_13(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("GO"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_14(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = None  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_15(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["XXversionXX"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_16(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["VERSION"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_17(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[3:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_18(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) > 4:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_19(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 5:
            info["platform"] = parts[3]

    return info


def x_parse_go_version__mutmut_20(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = None

    return info


def x_parse_go_version__mutmut_21(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["XXplatformXX"] = parts[3]

    return info


def x_parse_go_version__mutmut_22(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["PLATFORM"] = parts[3]

    return info


def x_parse_go_version__mutmut_23(output: str) -> dict[str, str]:
    """Parse Go version output."""

    # Example: "go version go1.21.0 linux/amd64"
    info = {"tool": "go"}

    parts = output.split()
    if len(parts) >= 3:
        version_part = parts[2]
        if version_part.startswith("go"):
            info["version"] = version_part[2:]  # Remove "go" prefix

        if len(parts) >= 4:
            info["platform"] = parts[4]

    return info

x_parse_go_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_go_version__mutmut_1': x_parse_go_version__mutmut_1, 
    'x_parse_go_version__mutmut_2': x_parse_go_version__mutmut_2, 
    'x_parse_go_version__mutmut_3': x_parse_go_version__mutmut_3, 
    'x_parse_go_version__mutmut_4': x_parse_go_version__mutmut_4, 
    'x_parse_go_version__mutmut_5': x_parse_go_version__mutmut_5, 
    'x_parse_go_version__mutmut_6': x_parse_go_version__mutmut_6, 
    'x_parse_go_version__mutmut_7': x_parse_go_version__mutmut_7, 
    'x_parse_go_version__mutmut_8': x_parse_go_version__mutmut_8, 
    'x_parse_go_version__mutmut_9': x_parse_go_version__mutmut_9, 
    'x_parse_go_version__mutmut_10': x_parse_go_version__mutmut_10, 
    'x_parse_go_version__mutmut_11': x_parse_go_version__mutmut_11, 
    'x_parse_go_version__mutmut_12': x_parse_go_version__mutmut_12, 
    'x_parse_go_version__mutmut_13': x_parse_go_version__mutmut_13, 
    'x_parse_go_version__mutmut_14': x_parse_go_version__mutmut_14, 
    'x_parse_go_version__mutmut_15': x_parse_go_version__mutmut_15, 
    'x_parse_go_version__mutmut_16': x_parse_go_version__mutmut_16, 
    'x_parse_go_version__mutmut_17': x_parse_go_version__mutmut_17, 
    'x_parse_go_version__mutmut_18': x_parse_go_version__mutmut_18, 
    'x_parse_go_version__mutmut_19': x_parse_go_version__mutmut_19, 
    'x_parse_go_version__mutmut_20': x_parse_go_version__mutmut_20, 
    'x_parse_go_version__mutmut_21': x_parse_go_version__mutmut_21, 
    'x_parse_go_version__mutmut_22': x_parse_go_version__mutmut_22, 
    'x_parse_go_version__mutmut_23': x_parse_go_version__mutmut_23
}

def parse_go_version(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_go_version__mutmut_orig, x_parse_go_version__mutmut_mutants, args, kwargs)
    return result 

parse_go_version.__signature__ = _mutmut_signature(x_parse_go_version__mutmut_orig)
x_parse_go_version__mutmut_orig.__name__ = 'x_parse_go_version'


def x_parse_uv_version__mutmut_orig(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_1(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = None

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_2(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"XXtoolXX": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_3(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"TOOL": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_4(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "XXuvXX"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_5(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "UV"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_6(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = None
    if len(parts) >= 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_7(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) > 2:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_8(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) >= 3:
        info["version"] = parts[1]

    return info


def x_parse_uv_version__mutmut_9(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = None

    return info


def x_parse_uv_version__mutmut_10(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["XXversionXX"] = parts[1]

    return info


def x_parse_uv_version__mutmut_11(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["VERSION"] = parts[1]

    return info


def x_parse_uv_version__mutmut_12(output: str) -> dict[str, str]:
    """Parse UV version output."""

    # Example: "uv 0.4.15"
    info = {"tool": "uv"}

    parts = output.split()
    if len(parts) >= 2:
        info["version"] = parts[2]

    return info

x_parse_uv_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_uv_version__mutmut_1': x_parse_uv_version__mutmut_1, 
    'x_parse_uv_version__mutmut_2': x_parse_uv_version__mutmut_2, 
    'x_parse_uv_version__mutmut_3': x_parse_uv_version__mutmut_3, 
    'x_parse_uv_version__mutmut_4': x_parse_uv_version__mutmut_4, 
    'x_parse_uv_version__mutmut_5': x_parse_uv_version__mutmut_5, 
    'x_parse_uv_version__mutmut_6': x_parse_uv_version__mutmut_6, 
    'x_parse_uv_version__mutmut_7': x_parse_uv_version__mutmut_7, 
    'x_parse_uv_version__mutmut_8': x_parse_uv_version__mutmut_8, 
    'x_parse_uv_version__mutmut_9': x_parse_uv_version__mutmut_9, 
    'x_parse_uv_version__mutmut_10': x_parse_uv_version__mutmut_10, 
    'x_parse_uv_version__mutmut_11': x_parse_uv_version__mutmut_11, 
    'x_parse_uv_version__mutmut_12': x_parse_uv_version__mutmut_12
}

def parse_uv_version(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_uv_version__mutmut_orig, x_parse_uv_version__mutmut_mutants, args, kwargs)
    return result 

parse_uv_version.__signature__ = _mutmut_signature(x_parse_uv_version__mutmut_orig)
x_parse_uv_version__mutmut_orig.__name__ = 'x_parse_uv_version'


def x_parse_generic_version__mutmut_orig(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_1(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = None

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_2(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"XXtoolXX": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_3(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"TOOL": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_4(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "XXraw_outputXX": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_5(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "RAW_OUTPUT": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_6(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = None

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_7(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"XXv?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)XX",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_8(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-za-z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_9(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"V?([0-9]+\.[0-9]+\.[0-9]+(?:-[A-ZA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_10(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"XX([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)XX",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_11(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-za-z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_12(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[A-ZA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_13(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"XX([0-9]+\.[0-9]+\.[0-9]+)XX",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_14(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = None
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_15(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(None, output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_16(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, None)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_17(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(output)
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_18(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, )
        if match:
            info["version"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_19(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = None
            break

    return info


def x_parse_generic_version__mutmut_20(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["XXversionXX"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_21(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["VERSION"] = match.group(1)
            break

    return info


def x_parse_generic_version__mutmut_22(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(None)
            break

    return info


def x_parse_generic_version__mutmut_23(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(2)
            break

    return info


def x_parse_generic_version__mutmut_24(output: str, tool_name: str) -> dict[str, str]:
    """Generic version parsing for unknown tools."""

    info = {"tool": tool_name, "raw_output": output}

    # Try to extract version number using common patterns
    import re

    # Look for version patterns like "1.2.3", "v1.2.3", etc.
    version_patterns = [
        r"v?([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+(?:-[a-zA-Z0-9]+)?)",
        r"([0-9]+\.[0-9]+\.[0-9]+)",
    ]

    for pattern in version_patterns:
        match = re.search(pattern, output)
        if match:
            info["version"] = match.group(1)
            return

    return info

x_parse_generic_version__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_generic_version__mutmut_1': x_parse_generic_version__mutmut_1, 
    'x_parse_generic_version__mutmut_2': x_parse_generic_version__mutmut_2, 
    'x_parse_generic_version__mutmut_3': x_parse_generic_version__mutmut_3, 
    'x_parse_generic_version__mutmut_4': x_parse_generic_version__mutmut_4, 
    'x_parse_generic_version__mutmut_5': x_parse_generic_version__mutmut_5, 
    'x_parse_generic_version__mutmut_6': x_parse_generic_version__mutmut_6, 
    'x_parse_generic_version__mutmut_7': x_parse_generic_version__mutmut_7, 
    'x_parse_generic_version__mutmut_8': x_parse_generic_version__mutmut_8, 
    'x_parse_generic_version__mutmut_9': x_parse_generic_version__mutmut_9, 
    'x_parse_generic_version__mutmut_10': x_parse_generic_version__mutmut_10, 
    'x_parse_generic_version__mutmut_11': x_parse_generic_version__mutmut_11, 
    'x_parse_generic_version__mutmut_12': x_parse_generic_version__mutmut_12, 
    'x_parse_generic_version__mutmut_13': x_parse_generic_version__mutmut_13, 
    'x_parse_generic_version__mutmut_14': x_parse_generic_version__mutmut_14, 
    'x_parse_generic_version__mutmut_15': x_parse_generic_version__mutmut_15, 
    'x_parse_generic_version__mutmut_16': x_parse_generic_version__mutmut_16, 
    'x_parse_generic_version__mutmut_17': x_parse_generic_version__mutmut_17, 
    'x_parse_generic_version__mutmut_18': x_parse_generic_version__mutmut_18, 
    'x_parse_generic_version__mutmut_19': x_parse_generic_version__mutmut_19, 
    'x_parse_generic_version__mutmut_20': x_parse_generic_version__mutmut_20, 
    'x_parse_generic_version__mutmut_21': x_parse_generic_version__mutmut_21, 
    'x_parse_generic_version__mutmut_22': x_parse_generic_version__mutmut_22, 
    'x_parse_generic_version__mutmut_23': x_parse_generic_version__mutmut_23, 
    'x_parse_generic_version__mutmut_24': x_parse_generic_version__mutmut_24
}

def parse_generic_version(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_generic_version__mutmut_orig, x_parse_generic_version__mutmut_mutants, args, kwargs)
    return result 

parse_generic_version.__signature__ = _mutmut_signature(x_parse_generic_version__mutmut_orig)
x_parse_generic_version__mutmut_orig.__name__ = 'x_parse_generic_version'


def x_verify_file__mutmut_orig(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_1(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_2(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(None)
        return False

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_3(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return True

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_4(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path or signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_5(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path and signature_path.exists():
        logger.info(None)
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_6(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return False
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return True


def x_verify_file__mutmut_7(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(None)
        return True


def x_verify_file__mutmut_8(file_path: pathlib.Path, signature_path: pathlib.Path | None = None) -> bool:
    """Verify file integrity using signature if available.

    Args:
        file_path: Path to file to verify
        signature_path: Optional path to signature file

    Returns:
        True if verification passes, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File not found for verification: {file_path}")
        return False

    if signature_path and signature_path.exists():
        logger.info(f"Verifying file signature: {file_path}")
        # For now, just check that signature file exists
        # In production, would verify actual signature
        return True
    else:
        if logger.is_debug_enabled():
            logger.debug(f"No signature file found, skipping verification: {file_path}")
        return False

x_verify_file__mutmut_mutants : ClassVar[MutantDict] = {
'x_verify_file__mutmut_1': x_verify_file__mutmut_1, 
    'x_verify_file__mutmut_2': x_verify_file__mutmut_2, 
    'x_verify_file__mutmut_3': x_verify_file__mutmut_3, 
    'x_verify_file__mutmut_4': x_verify_file__mutmut_4, 
    'x_verify_file__mutmut_5': x_verify_file__mutmut_5, 
    'x_verify_file__mutmut_6': x_verify_file__mutmut_6, 
    'x_verify_file__mutmut_7': x_verify_file__mutmut_7, 
    'x_verify_file__mutmut_8': x_verify_file__mutmut_8
}

def verify_file(*args, **kwargs):
    result = _mutmut_trampoline(x_verify_file__mutmut_orig, x_verify_file__mutmut_mutants, args, kwargs)
    return result 

verify_file.__signature__ = _mutmut_signature(x_verify_file__mutmut_orig)
x_verify_file__mutmut_orig.__name__ = 'x_verify_file'


# 🧰🌍🔚
