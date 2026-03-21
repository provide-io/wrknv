#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Installation Operations
========================================
Functions for extracting archives and making files executable."""

from __future__ import annotations

import pathlib
import stat

from provide.foundation import logger
from provide.foundation.archive.operations import ArchiveOperations
from provide.foundation.archive.tar import TarArchive
from provide.foundation.archive.zip import ZipArchive
from provide.foundation.errors import ResourceError, ValidationError, resilient
from provide.foundation.file import (
    ensure_dir,
    get_size,
    safe_copy,
    safe_delete,
    safe_rmtree,
)
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


@resilient
def extract_archive(archive_path: pathlib.Path, extract_dir: pathlib.Path) -> None:
    """Extract archive to specified directory."""

    if not archive_path.exists():
        raise ResourceError(f"Archive not found: {archive_path}")

    # Create extraction directory
    extract_dir.mkdir(parents=True, exist_ok=True)

    if logger.is_debug_enabled():
        logger.debug(f"Extracting {archive_path} to {extract_dir}")

    archive_name = archive_path.name.lower()

    try:
        if archive_name.endswith((".tar.gz", ".tgz")):
            # Use foundation's extract_tar_gz with built-in path traversal protection
            ArchiveOperations.extract_tar_gz(archive_path, extract_dir)
        elif archive_name.endswith(".tar"):
            # Use foundation's TarArchive with built-in path traversal protection
            TarArchive().extract(archive_path, extract_dir)
        elif archive_name.endswith(".zip"):
            # Use foundation's ZipArchive with built-in path traversal protection
            ZipArchive().extract(archive_path, extract_dir)
        else:
            raise ValidationError(f"Unsupported archive format: {archive_path}")

        if logger.is_debug_enabled():
            logger.debug(f"Successfully extracted {archive_path}")

    except Exception as e:
        raise ResourceError(f"Failed to extract {archive_path}: {e}") from e


@resilient
def make_executable(file_path: pathlib.Path) -> None:
    """Make file executable on Unix-like systems."""

    if not file_path.exists():
        raise ResourceError(f"File not found: {file_path}")

    # Only needed on Unix-like systems
    import platform

    if platform.system().lower() == "windows":
        if logger.is_debug_enabled():
            logger.debug(f"Skipping chmod on Windows for {file_path}")
        return

    try:
        # Get current permissions
        current_mode = file_path.stat().st_mode

        # Add execute permissions for owner, group, and others
        new_mode = current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH

        # Set new permissions
        file_path.chmod(new_mode)

        if logger.is_debug_enabled():
            logger.debug(f"Made {file_path} executable (mode: {oct(new_mode)})")

    except Exception as e:
        logger.warning(f"Failed to make {file_path} executable: {e}")


@resilient
def create_symlink(target: pathlib.Path, link_path: pathlib.Path) -> None:
    """Create symbolic link, handling platform differences."""

    if not target.exists():
        raise ResourceError(f"Target does not exist: {target}")

    # Remove existing link if it exists
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()

    # Create parent directories
    link_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        link_path.symlink_to(target)
        if logger.is_debug_enabled():
            logger.debug(f"Created symlink: {link_path} -> {target}")

    except OSError as e:
        # Fall back to copying on Windows if symlink fails
        import platform

        if platform.system().lower() == "windows":
            logger.warning(f"Symlink failed on Windows, copying instead: {e}")
            import shutil

            shutil.copy2(target, link_path)
        else:
            raise


def x_copy_file__mutmut_orig(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_1(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = False) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_2(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(None, destination, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_3(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, None, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_4(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=None, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_5(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=True, preserve_mode=None)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_6(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(destination, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_7(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_8(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_9(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=True, )
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_10(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=False, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(f"Copied {source} to {destination}")


def x_copy_file__mutmut_11(source: pathlib.Path, destination: pathlib.Path, preserve_permissions: bool = True) -> None:
    """Copy file with optional permission preservation."""
    # Use foundation's safe_copy which handles all edge cases
    safe_copy(source, destination, overwrite=True, preserve_mode=preserve_permissions)
    if logger.is_debug_enabled():
        logger.debug(None)

x_copy_file__mutmut_mutants : ClassVar[MutantDict] = {
'x_copy_file__mutmut_1': x_copy_file__mutmut_1, 
    'x_copy_file__mutmut_2': x_copy_file__mutmut_2, 
    'x_copy_file__mutmut_3': x_copy_file__mutmut_3, 
    'x_copy_file__mutmut_4': x_copy_file__mutmut_4, 
    'x_copy_file__mutmut_5': x_copy_file__mutmut_5, 
    'x_copy_file__mutmut_6': x_copy_file__mutmut_6, 
    'x_copy_file__mutmut_7': x_copy_file__mutmut_7, 
    'x_copy_file__mutmut_8': x_copy_file__mutmut_8, 
    'x_copy_file__mutmut_9': x_copy_file__mutmut_9, 
    'x_copy_file__mutmut_10': x_copy_file__mutmut_10, 
    'x_copy_file__mutmut_11': x_copy_file__mutmut_11
}

def copy_file(*args, **kwargs):
    result = _mutmut_trampoline(x_copy_file__mutmut_orig, x_copy_file__mutmut_mutants, args, kwargs)
    return result 

copy_file.__signature__ = _mutmut_signature(x_copy_file__mutmut_orig)
x_copy_file__mutmut_orig.__name__ = 'x_copy_file'


def x_ensure_directory__mutmut_orig(dir_path: pathlib.Path, mode: int = 0o755) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(dir_path, mode=mode)
    if logger.is_debug_enabled():
        logger.debug(f"Created/verified directory: {dir_path}")


def x_ensure_directory__mutmut_1(dir_path: pathlib.Path, mode: int = 494) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(dir_path, mode=mode)
    if logger.is_debug_enabled():
        logger.debug(f"Created/verified directory: {dir_path}")


def x_ensure_directory__mutmut_2(dir_path: pathlib.Path, mode: int = 0o755) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(None, mode=mode)
    if logger.is_debug_enabled():
        logger.debug(f"Created/verified directory: {dir_path}")


def x_ensure_directory__mutmut_3(dir_path: pathlib.Path, mode: int = 0o755) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(dir_path, mode=None)
    if logger.is_debug_enabled():
        logger.debug(f"Created/verified directory: {dir_path}")


def x_ensure_directory__mutmut_4(dir_path: pathlib.Path, mode: int = 0o755) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(mode=mode)
    if logger.is_debug_enabled():
        logger.debug(f"Created/verified directory: {dir_path}")


def x_ensure_directory__mutmut_5(dir_path: pathlib.Path, mode: int = 0o755) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(dir_path, )
    if logger.is_debug_enabled():
        logger.debug(f"Created/verified directory: {dir_path}")


def x_ensure_directory__mutmut_6(dir_path: pathlib.Path, mode: int = 0o755) -> None:
    """Ensure directory exists with specified permissions."""
    # Use foundation's ensure_dir which handles all edge cases
    ensure_dir(dir_path, mode=mode)
    if logger.is_debug_enabled():
        logger.debug(None)

x_ensure_directory__mutmut_mutants : ClassVar[MutantDict] = {
'x_ensure_directory__mutmut_1': x_ensure_directory__mutmut_1, 
    'x_ensure_directory__mutmut_2': x_ensure_directory__mutmut_2, 
    'x_ensure_directory__mutmut_3': x_ensure_directory__mutmut_3, 
    'x_ensure_directory__mutmut_4': x_ensure_directory__mutmut_4, 
    'x_ensure_directory__mutmut_5': x_ensure_directory__mutmut_5, 
    'x_ensure_directory__mutmut_6': x_ensure_directory__mutmut_6
}

def ensure_directory(*args, **kwargs):
    result = _mutmut_trampoline(x_ensure_directory__mutmut_orig, x_ensure_directory__mutmut_mutants, args, kwargs)
    return result 

ensure_directory.__signature__ = _mutmut_signature(x_ensure_directory__mutmut_orig)
x_ensure_directory__mutmut_orig.__name__ = 'x_ensure_directory'


def x_clean_directory__mutmut_orig(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_1(dir_path: pathlib.Path, keep_hidden: bool = False) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_2(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_3(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_4(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(None)

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_5(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden or item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_6(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith(None):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_7(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("XX.XX"):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_8(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            break

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_9(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(None, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_10(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=None)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_11(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_12(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, )
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_13(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=False)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_14(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(None, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_15(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=None)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_16(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_17(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, )
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_18(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=False)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_19(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(None)

    if logger.is_debug_enabled():
        logger.debug(f"Cleaned directory: {dir_path}")


def x_clean_directory__mutmut_20(dir_path: pathlib.Path, keep_hidden: bool = True) -> None:
    """Clean all files from directory, optionally keeping hidden files."""

    if not dir_path.exists():
        return

    if not dir_path.is_dir():
        raise Exception(f"Path is not a directory: {dir_path}")

    for item in dir_path.iterdir():
        if keep_hidden and item.name.startswith("."):
            continue

        try:
            if item.is_dir():
                safe_rmtree(item, missing_ok=True)
            else:
                safe_delete(item, missing_ok=True)
        except Exception as e:
            logger.warning(f"Failed to remove {item}: {e}")

    if logger.is_debug_enabled():
        logger.debug(None)

x_clean_directory__mutmut_mutants : ClassVar[MutantDict] = {
'x_clean_directory__mutmut_1': x_clean_directory__mutmut_1, 
    'x_clean_directory__mutmut_2': x_clean_directory__mutmut_2, 
    'x_clean_directory__mutmut_3': x_clean_directory__mutmut_3, 
    'x_clean_directory__mutmut_4': x_clean_directory__mutmut_4, 
    'x_clean_directory__mutmut_5': x_clean_directory__mutmut_5, 
    'x_clean_directory__mutmut_6': x_clean_directory__mutmut_6, 
    'x_clean_directory__mutmut_7': x_clean_directory__mutmut_7, 
    'x_clean_directory__mutmut_8': x_clean_directory__mutmut_8, 
    'x_clean_directory__mutmut_9': x_clean_directory__mutmut_9, 
    'x_clean_directory__mutmut_10': x_clean_directory__mutmut_10, 
    'x_clean_directory__mutmut_11': x_clean_directory__mutmut_11, 
    'x_clean_directory__mutmut_12': x_clean_directory__mutmut_12, 
    'x_clean_directory__mutmut_13': x_clean_directory__mutmut_13, 
    'x_clean_directory__mutmut_14': x_clean_directory__mutmut_14, 
    'x_clean_directory__mutmut_15': x_clean_directory__mutmut_15, 
    'x_clean_directory__mutmut_16': x_clean_directory__mutmut_16, 
    'x_clean_directory__mutmut_17': x_clean_directory__mutmut_17, 
    'x_clean_directory__mutmut_18': x_clean_directory__mutmut_18, 
    'x_clean_directory__mutmut_19': x_clean_directory__mutmut_19, 
    'x_clean_directory__mutmut_20': x_clean_directory__mutmut_20
}

def clean_directory(*args, **kwargs):
    result = _mutmut_trampoline(x_clean_directory__mutmut_orig, x_clean_directory__mutmut_mutants, args, kwargs)
    return result 

clean_directory.__signature__ = _mutmut_signature(x_clean_directory__mutmut_orig)
x_clean_directory__mutmut_orig.__name__ = 'x_clean_directory'


@resilient
def get_file_size(file_path: pathlib.Path) -> int:
    """Get file size in bytes."""
    # Use foundation's get_size which returns 0 for missing files
    size = get_size(file_path)
    if size == 0 and not file_path.exists():
        raise ResourceError(f"File not found: {file_path}")
    return size


def x_is_executable__mutmut_orig(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_1(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_2(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return True

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_3(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().upper() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_4(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() != "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_5(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "XXwindowsXX":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_6(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "WINDOWS":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_7(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.upper() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_8(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() not in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_9(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in ["XX.exeXX", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_10(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".EXE", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_11(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", "XX.batXX", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_12(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".BAT", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_13(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", "XX.cmdXX"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_14(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".CMD"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode & stat.S_IXUSR)


def x_is_executable__mutmut_15(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(None)


def x_is_executable__mutmut_16(file_path: pathlib.Path) -> bool:
    """Check if file is executable."""

    if not file_path.exists():
        return False

    import platform

    if platform.system().lower() == "windows":
        # On Windows, check file extension
        return file_path.suffix.lower() in [".exe", ".bat", ".cmd"]
    else:
        # On Unix-like systems, check execute permission
        return bool(file_path.stat().st_mode | stat.S_IXUSR)

x_is_executable__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_executable__mutmut_1': x_is_executable__mutmut_1, 
    'x_is_executable__mutmut_2': x_is_executable__mutmut_2, 
    'x_is_executable__mutmut_3': x_is_executable__mutmut_3, 
    'x_is_executable__mutmut_4': x_is_executable__mutmut_4, 
    'x_is_executable__mutmut_5': x_is_executable__mutmut_5, 
    'x_is_executable__mutmut_6': x_is_executable__mutmut_6, 
    'x_is_executable__mutmut_7': x_is_executable__mutmut_7, 
    'x_is_executable__mutmut_8': x_is_executable__mutmut_8, 
    'x_is_executable__mutmut_9': x_is_executable__mutmut_9, 
    'x_is_executable__mutmut_10': x_is_executable__mutmut_10, 
    'x_is_executable__mutmut_11': x_is_executable__mutmut_11, 
    'x_is_executable__mutmut_12': x_is_executable__mutmut_12, 
    'x_is_executable__mutmut_13': x_is_executable__mutmut_13, 
    'x_is_executable__mutmut_14': x_is_executable__mutmut_14, 
    'x_is_executable__mutmut_15': x_is_executable__mutmut_15, 
    'x_is_executable__mutmut_16': x_is_executable__mutmut_16
}

def is_executable(*args, **kwargs):
    result = _mutmut_trampoline(x_is_executable__mutmut_orig, x_is_executable__mutmut_mutants, args, kwargs)
    return result 

is_executable.__signature__ = _mutmut_signature(x_is_executable__mutmut_orig)
x_is_executable__mutmut_orig.__name__ = 'x_is_executable'


# 🧰🌍🔚
