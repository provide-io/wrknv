#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tf Manager Utilities
====================
Utility functions for Terraform/OpenTofu managers."""

from __future__ import annotations

import hashlib
import pathlib

import semver
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


def x_calculate_file_hash__mutmut_orig(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_1(file_path: pathlib.Path, algorithm: str = "XXsha256XX") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_2(file_path: pathlib.Path, algorithm: str = "SHA256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_3(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = None
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_4(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(None)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_5(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open(None) as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_6(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("XXrbXX") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_7(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("RB") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_8(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(None, b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_9(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), None):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_10(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_11(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), ):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_12(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: None, b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_13(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(None), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_14(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4097), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_15(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b"XXXX"):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def x_calculate_file_hash__mutmut_16(file_path: pathlib.Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(None)
    return hash_func.hexdigest()

x_calculate_file_hash__mutmut_mutants : ClassVar[MutantDict] = {
'x_calculate_file_hash__mutmut_1': x_calculate_file_hash__mutmut_1, 
    'x_calculate_file_hash__mutmut_2': x_calculate_file_hash__mutmut_2, 
    'x_calculate_file_hash__mutmut_3': x_calculate_file_hash__mutmut_3, 
    'x_calculate_file_hash__mutmut_4': x_calculate_file_hash__mutmut_4, 
    'x_calculate_file_hash__mutmut_5': x_calculate_file_hash__mutmut_5, 
    'x_calculate_file_hash__mutmut_6': x_calculate_file_hash__mutmut_6, 
    'x_calculate_file_hash__mutmut_7': x_calculate_file_hash__mutmut_7, 
    'x_calculate_file_hash__mutmut_8': x_calculate_file_hash__mutmut_8, 
    'x_calculate_file_hash__mutmut_9': x_calculate_file_hash__mutmut_9, 
    'x_calculate_file_hash__mutmut_10': x_calculate_file_hash__mutmut_10, 
    'x_calculate_file_hash__mutmut_11': x_calculate_file_hash__mutmut_11, 
    'x_calculate_file_hash__mutmut_12': x_calculate_file_hash__mutmut_12, 
    'x_calculate_file_hash__mutmut_13': x_calculate_file_hash__mutmut_13, 
    'x_calculate_file_hash__mutmut_14': x_calculate_file_hash__mutmut_14, 
    'x_calculate_file_hash__mutmut_15': x_calculate_file_hash__mutmut_15, 
    'x_calculate_file_hash__mutmut_16': x_calculate_file_hash__mutmut_16
}

def calculate_file_hash(*args, **kwargs):
    result = _mutmut_trampoline(x_calculate_file_hash__mutmut_orig, x_calculate_file_hash__mutmut_mutants, args, kwargs)
    return result 

calculate_file_hash.__signature__ = _mutmut_signature(x_calculate_file_hash__mutmut_orig)
x_calculate_file_hash__mutmut_orig.__name__ = 'x_calculate_file_hash'


def x_version_sort_key__mutmut_orig(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_1(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(None)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_2(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = None
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_3(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(None)
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_4(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split("XX.XX")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_5(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) <= 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_6(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 4:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_7(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append(None)
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_8(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("XX0XX")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_9(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = None
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_10(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(None)
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_11(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = "XX.XX".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_12(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:4])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_13(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(None)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("0.0.0")


def x_version_sort_key__mutmut_14(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse(None)


def x_version_sort_key__mutmut_15(version: str) -> semver.VersionInfo:
    """Generate sort key for semantic versioning using semver module."""
    try:
        # Try to parse as a semantic version
        return semver.VersionInfo.parse(version)
    except ValueError:
        # If it fails, try to make it semver-compliant
        # Handle versions like "1.0" by adding ".0"
        parts = version.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            normalized = ".".join(parts[:3])
            return semver.VersionInfo.parse(normalized)
        except ValueError:
            # Last resort: return a very old version
            return semver.VersionInfo.parse("XX0.0.0XX")

x_version_sort_key__mutmut_mutants : ClassVar[MutantDict] = {
'x_version_sort_key__mutmut_1': x_version_sort_key__mutmut_1, 
    'x_version_sort_key__mutmut_2': x_version_sort_key__mutmut_2, 
    'x_version_sort_key__mutmut_3': x_version_sort_key__mutmut_3, 
    'x_version_sort_key__mutmut_4': x_version_sort_key__mutmut_4, 
    'x_version_sort_key__mutmut_5': x_version_sort_key__mutmut_5, 
    'x_version_sort_key__mutmut_6': x_version_sort_key__mutmut_6, 
    'x_version_sort_key__mutmut_7': x_version_sort_key__mutmut_7, 
    'x_version_sort_key__mutmut_8': x_version_sort_key__mutmut_8, 
    'x_version_sort_key__mutmut_9': x_version_sort_key__mutmut_9, 
    'x_version_sort_key__mutmut_10': x_version_sort_key__mutmut_10, 
    'x_version_sort_key__mutmut_11': x_version_sort_key__mutmut_11, 
    'x_version_sort_key__mutmut_12': x_version_sort_key__mutmut_12, 
    'x_version_sort_key__mutmut_13': x_version_sort_key__mutmut_13, 
    'x_version_sort_key__mutmut_14': x_version_sort_key__mutmut_14, 
    'x_version_sort_key__mutmut_15': x_version_sort_key__mutmut_15
}

def version_sort_key(*args, **kwargs):
    result = _mutmut_trampoline(x_version_sort_key__mutmut_orig, x_version_sort_key__mutmut_mutants, args, kwargs)
    return result 

version_sort_key.__signature__ = _mutmut_signature(x_version_sort_key__mutmut_orig)
x_version_sort_key__mutmut_orig.__name__ = 'x_version_sort_key'


def x_get_tool_version_key__mutmut_orig(tool_name: str) -> str:
    """Get the metadata key for storing tool version."""
    return "opentofu_version" if tool_name == "tofu" else f"{tool_name}_version"


def x_get_tool_version_key__mutmut_1(tool_name: str) -> str:
    """Get the metadata key for storing tool version."""
    return "XXopentofu_versionXX" if tool_name == "tofu" else f"{tool_name}_version"


def x_get_tool_version_key__mutmut_2(tool_name: str) -> str:
    """Get the metadata key for storing tool version."""
    return "OPENTOFU_VERSION" if tool_name == "tofu" else f"{tool_name}_version"


def x_get_tool_version_key__mutmut_3(tool_name: str) -> str:
    """Get the metadata key for storing tool version."""
    return "opentofu_version" if tool_name != "tofu" else f"{tool_name}_version"


def x_get_tool_version_key__mutmut_4(tool_name: str) -> str:
    """Get the metadata key for storing tool version."""
    return "opentofu_version" if tool_name == "XXtofuXX" else f"{tool_name}_version"


def x_get_tool_version_key__mutmut_5(tool_name: str) -> str:
    """Get the metadata key for storing tool version."""
    return "opentofu_version" if tool_name == "TOFU" else f"{tool_name}_version"

x_get_tool_version_key__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_tool_version_key__mutmut_1': x_get_tool_version_key__mutmut_1, 
    'x_get_tool_version_key__mutmut_2': x_get_tool_version_key__mutmut_2, 
    'x_get_tool_version_key__mutmut_3': x_get_tool_version_key__mutmut_3, 
    'x_get_tool_version_key__mutmut_4': x_get_tool_version_key__mutmut_4, 
    'x_get_tool_version_key__mutmut_5': x_get_tool_version_key__mutmut_5
}

def get_tool_version_key(*args, **kwargs):
    result = _mutmut_trampoline(x_get_tool_version_key__mutmut_orig, x_get_tool_version_key__mutmut_mutants, args, kwargs)
    return result 

get_tool_version_key.__signature__ = _mutmut_signature(x_get_tool_version_key__mutmut_orig)
x_get_tool_version_key__mutmut_orig.__name__ = 'x_get_tool_version_key'


# 🧰🌍🔚
