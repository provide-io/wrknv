#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Version Resolution Utilities
============================
Handles resolution of version patterns like "1.11.x" to specific versions."""

from __future__ import annotations

from provide.foundation.logger import get_logger
import semver

from wrknv.managers.base import BaseToolManager

logger = get_logger(__name__)
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


class VersionResolver:
    """Resolves version patterns to specific versions from available versions list."""

    def xǁVersionResolverǁ__init____mutmut_orig(self, available_versions: list[str]) -> None:
        """Initialize with list of available versions."""
        self.available_versions = available_versions

    def xǁVersionResolverǁ__init____mutmut_1(self, available_versions: list[str]) -> None:
        """Initialize with list of available versions."""
        self.available_versions = None
    
    xǁVersionResolverǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁ__init____mutmut_1': xǁVersionResolverǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁVersionResolverǁ__init____mutmut_orig)
    xǁVersionResolverǁ__init____mutmut_orig.__name__ = 'xǁVersionResolverǁ__init__'

    def xǁVersionResolverǁresolve_version__mutmut_orig(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_1(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = None

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_2(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern not in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_3(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("XXlatestXX", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_4(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("LATEST", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_5(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "XXstableXX"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_6(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "STABLE"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_7(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_8(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError(None)
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_9(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("XXNo versions availableXX")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_10(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("no versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_11(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("NO VERSIONS AVAILABLE")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_12(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[1]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_13(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(None):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_14(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern not in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_15(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(None)

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_16(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(None):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_17(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith("XX.xXX"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_18(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".X"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_19(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(None)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_20(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(None):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_21(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(None)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_22(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern not in self.available_versions:
            return version_pattern
        else:
            raise ValueError(f"Version pattern '{version_pattern}' could not be resolved")

    def xǁVersionResolverǁresolve_version__mutmut_23(self, version_pattern: str) -> str:
        """
        Resolve a version pattern to a specific version.

        Examples:
            "1.11.x" -> "1.11.5" (latest patch in 1.11 series)
            "1.13" -> "1.13.7" (latest patch in 1.13 series)
            "1.15.0" -> "1.15.0" (exact version)
            "latest" -> "1.16.2" (latest overall version)

        Args:
            version_pattern: Version pattern to resolve

        Returns:
            Resolved specific version string

        Raises:
            ValueError: If pattern cannot be resolved
        """
        version_pattern = version_pattern.strip()

        # Handle special cases
        if version_pattern in ("latest", "stable"):
            if not self.available_versions:
                raise ValueError("No versions available")
            return self.available_versions[0]  # Assuming sorted with latest first

        # Handle exact version (already specific)
        if self._is_exact_version(version_pattern):
            if version_pattern in self.available_versions:
                return version_pattern
            else:
                raise ValueError(f"Version {version_pattern} not available")

        # Handle .x suffix patterns like "1.11.x"
        if version_pattern.endswith(".x"):
            return self._resolve_x_pattern(version_pattern)

        # Handle major.minor patterns like "1.11" (no patch specified)
        if self._is_major_minor_only(version_pattern):
            return self._resolve_major_minor(version_pattern)

        # If no pattern matches, treat as exact version
        if version_pattern in self.available_versions:
            return version_pattern
        else:
            raise ValueError(None)
    
    xǁVersionResolverǁresolve_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁresolve_version__mutmut_1': xǁVersionResolverǁresolve_version__mutmut_1, 
        'xǁVersionResolverǁresolve_version__mutmut_2': xǁVersionResolverǁresolve_version__mutmut_2, 
        'xǁVersionResolverǁresolve_version__mutmut_3': xǁVersionResolverǁresolve_version__mutmut_3, 
        'xǁVersionResolverǁresolve_version__mutmut_4': xǁVersionResolverǁresolve_version__mutmut_4, 
        'xǁVersionResolverǁresolve_version__mutmut_5': xǁVersionResolverǁresolve_version__mutmut_5, 
        'xǁVersionResolverǁresolve_version__mutmut_6': xǁVersionResolverǁresolve_version__mutmut_6, 
        'xǁVersionResolverǁresolve_version__mutmut_7': xǁVersionResolverǁresolve_version__mutmut_7, 
        'xǁVersionResolverǁresolve_version__mutmut_8': xǁVersionResolverǁresolve_version__mutmut_8, 
        'xǁVersionResolverǁresolve_version__mutmut_9': xǁVersionResolverǁresolve_version__mutmut_9, 
        'xǁVersionResolverǁresolve_version__mutmut_10': xǁVersionResolverǁresolve_version__mutmut_10, 
        'xǁVersionResolverǁresolve_version__mutmut_11': xǁVersionResolverǁresolve_version__mutmut_11, 
        'xǁVersionResolverǁresolve_version__mutmut_12': xǁVersionResolverǁresolve_version__mutmut_12, 
        'xǁVersionResolverǁresolve_version__mutmut_13': xǁVersionResolverǁresolve_version__mutmut_13, 
        'xǁVersionResolverǁresolve_version__mutmut_14': xǁVersionResolverǁresolve_version__mutmut_14, 
        'xǁVersionResolverǁresolve_version__mutmut_15': xǁVersionResolverǁresolve_version__mutmut_15, 
        'xǁVersionResolverǁresolve_version__mutmut_16': xǁVersionResolverǁresolve_version__mutmut_16, 
        'xǁVersionResolverǁresolve_version__mutmut_17': xǁVersionResolverǁresolve_version__mutmut_17, 
        'xǁVersionResolverǁresolve_version__mutmut_18': xǁVersionResolverǁresolve_version__mutmut_18, 
        'xǁVersionResolverǁresolve_version__mutmut_19': xǁVersionResolverǁresolve_version__mutmut_19, 
        'xǁVersionResolverǁresolve_version__mutmut_20': xǁVersionResolverǁresolve_version__mutmut_20, 
        'xǁVersionResolverǁresolve_version__mutmut_21': xǁVersionResolverǁresolve_version__mutmut_21, 
        'xǁVersionResolverǁresolve_version__mutmut_22': xǁVersionResolverǁresolve_version__mutmut_22, 
        'xǁVersionResolverǁresolve_version__mutmut_23': xǁVersionResolverǁresolve_version__mutmut_23
    }
    
    def resolve_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁresolve_version__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁresolve_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resolve_version.__signature__ = _mutmut_signature(xǁVersionResolverǁresolve_version__mutmut_orig)
    xǁVersionResolverǁresolve_version__mutmut_orig.__name__ = 'xǁVersionResolverǁresolve_version'

    def xǁVersionResolverǁ_is_exact_version__mutmut_orig(self, version: str) -> bool:
        """Check if version string is an exact semantic version."""
        try:
            semver.VersionInfo.parse(version)
            return True
        except ValueError:
            return False

    def xǁVersionResolverǁ_is_exact_version__mutmut_1(self, version: str) -> bool:
        """Check if version string is an exact semantic version."""
        try:
            semver.VersionInfo.parse(None)
            return True
        except ValueError:
            return False

    def xǁVersionResolverǁ_is_exact_version__mutmut_2(self, version: str) -> bool:
        """Check if version string is an exact semantic version."""
        try:
            semver.VersionInfo.parse(version)
            return False
        except ValueError:
            return False

    def xǁVersionResolverǁ_is_exact_version__mutmut_3(self, version: str) -> bool:
        """Check if version string is an exact semantic version."""
        try:
            semver.VersionInfo.parse(version)
            return True
        except ValueError:
            return True
    
    xǁVersionResolverǁ_is_exact_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁ_is_exact_version__mutmut_1': xǁVersionResolverǁ_is_exact_version__mutmut_1, 
        'xǁVersionResolverǁ_is_exact_version__mutmut_2': xǁVersionResolverǁ_is_exact_version__mutmut_2, 
        'xǁVersionResolverǁ_is_exact_version__mutmut_3': xǁVersionResolverǁ_is_exact_version__mutmut_3
    }
    
    def _is_exact_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁ_is_exact_version__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁ_is_exact_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_exact_version.__signature__ = _mutmut_signature(xǁVersionResolverǁ_is_exact_version__mutmut_orig)
    xǁVersionResolverǁ_is_exact_version__mutmut_orig.__name__ = 'xǁVersionResolverǁ_is_exact_version'

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_orig(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split(".")
        return len(parts) == 2 and all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_1(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = None
        return len(parts) == 2 and all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_2(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split(None)
        return len(parts) == 2 and all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_3(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split("XX.XX")
        return len(parts) == 2 and all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_4(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split(".")
        return len(parts) == 2 or all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_5(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split(".")
        return len(parts) != 2 and all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_6(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split(".")
        return len(parts) == 3 and all(part.isdigit() for part in parts)

    def xǁVersionResolverǁ_is_major_minor_only__mutmut_7(self, version: str) -> bool:
        """Check if version is in major.minor format (no patch)."""
        parts = version.split(".")
        return len(parts) == 2 and all(None)
    
    xǁVersionResolverǁ_is_major_minor_only__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁ_is_major_minor_only__mutmut_1': xǁVersionResolverǁ_is_major_minor_only__mutmut_1, 
        'xǁVersionResolverǁ_is_major_minor_only__mutmut_2': xǁVersionResolverǁ_is_major_minor_only__mutmut_2, 
        'xǁVersionResolverǁ_is_major_minor_only__mutmut_3': xǁVersionResolverǁ_is_major_minor_only__mutmut_3, 
        'xǁVersionResolverǁ_is_major_minor_only__mutmut_4': xǁVersionResolverǁ_is_major_minor_only__mutmut_4, 
        'xǁVersionResolverǁ_is_major_minor_only__mutmut_5': xǁVersionResolverǁ_is_major_minor_only__mutmut_5, 
        'xǁVersionResolverǁ_is_major_minor_only__mutmut_6': xǁVersionResolverǁ_is_major_minor_only__mutmut_6, 
        'xǁVersionResolverǁ_is_major_minor_only__mutmut_7': xǁVersionResolverǁ_is_major_minor_only__mutmut_7
    }
    
    def _is_major_minor_only(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁ_is_major_minor_only__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁ_is_major_minor_only__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_major_minor_only.__signature__ = _mutmut_signature(xǁVersionResolverǁ_is_major_minor_only__mutmut_orig)
    xǁVersionResolverǁ_is_major_minor_only__mutmut_orig.__name__ = 'xǁVersionResolverǁ_is_major_minor_only'

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_orig(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_1(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = None  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_2(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:+2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_3(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-3]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_4(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = None

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_5(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(None)]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_6(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix - ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_7(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + "XX.XX")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_8(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_9(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(None)

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_10(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=None, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_11(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=None)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_12(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_13(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, )
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_14(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=False)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_15(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = None

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_16(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[1]

        logger.debug(f"Resolved {pattern} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_x_pattern__mutmut_17(self, pattern: str) -> str:
        """Resolve patterns like '1.11.x' to latest patch version."""
        # Extract major.minor from pattern
        prefix = pattern[:-2]  # Remove ".x"

        # Find all versions matching the prefix
        matching_versions = [v for v in self.available_versions if v.startswith(prefix + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found matching pattern {pattern}")

        # Sort and return latest (first in sorted list)
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(None)
        return resolved
    
    xǁVersionResolverǁ_resolve_x_pattern__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁ_resolve_x_pattern__mutmut_1': xǁVersionResolverǁ_resolve_x_pattern__mutmut_1, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_2': xǁVersionResolverǁ_resolve_x_pattern__mutmut_2, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_3': xǁVersionResolverǁ_resolve_x_pattern__mutmut_3, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_4': xǁVersionResolverǁ_resolve_x_pattern__mutmut_4, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_5': xǁVersionResolverǁ_resolve_x_pattern__mutmut_5, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_6': xǁVersionResolverǁ_resolve_x_pattern__mutmut_6, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_7': xǁVersionResolverǁ_resolve_x_pattern__mutmut_7, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_8': xǁVersionResolverǁ_resolve_x_pattern__mutmut_8, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_9': xǁVersionResolverǁ_resolve_x_pattern__mutmut_9, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_10': xǁVersionResolverǁ_resolve_x_pattern__mutmut_10, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_11': xǁVersionResolverǁ_resolve_x_pattern__mutmut_11, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_12': xǁVersionResolverǁ_resolve_x_pattern__mutmut_12, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_13': xǁVersionResolverǁ_resolve_x_pattern__mutmut_13, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_14': xǁVersionResolverǁ_resolve_x_pattern__mutmut_14, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_15': xǁVersionResolverǁ_resolve_x_pattern__mutmut_15, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_16': xǁVersionResolverǁ_resolve_x_pattern__mutmut_16, 
        'xǁVersionResolverǁ_resolve_x_pattern__mutmut_17': xǁVersionResolverǁ_resolve_x_pattern__mutmut_17
    }
    
    def _resolve_x_pattern(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁ_resolve_x_pattern__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁ_resolve_x_pattern__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _resolve_x_pattern.__signature__ = _mutmut_signature(xǁVersionResolverǁ_resolve_x_pattern__mutmut_orig)
    xǁVersionResolverǁ_resolve_x_pattern__mutmut_orig.__name__ = 'xǁVersionResolverǁ_resolve_x_pattern'

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_orig(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_1(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = None

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_2(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(None)]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_3(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version - ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_4(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + "XX.XX")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_5(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_6(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(None)

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_7(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=None, reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_8(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=None)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_9(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(reverse=True)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_10(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, )
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_11(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=False)
        resolved = matching_versions[0]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_12(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = None

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_13(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[1]

        logger.debug(f"Resolved {version} to {resolved}")
        return resolved

    def xǁVersionResolverǁ_resolve_major_minor__mutmut_14(self, version: str) -> str:
        """Resolve major.minor to latest patch version."""
        # Find all versions matching major.minor
        matching_versions = [v for v in self.available_versions if v.startswith(version + ".")]

        if not matching_versions:
            raise ValueError(f"No versions found for {version}")

        # Sort and return latest
        matching_versions.sort(key=self._version_sort_key, reverse=True)
        resolved = matching_versions[0]

        logger.debug(None)
        return resolved
    
    xǁVersionResolverǁ_resolve_major_minor__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁ_resolve_major_minor__mutmut_1': xǁVersionResolverǁ_resolve_major_minor__mutmut_1, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_2': xǁVersionResolverǁ_resolve_major_minor__mutmut_2, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_3': xǁVersionResolverǁ_resolve_major_minor__mutmut_3, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_4': xǁVersionResolverǁ_resolve_major_minor__mutmut_4, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_5': xǁVersionResolverǁ_resolve_major_minor__mutmut_5, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_6': xǁVersionResolverǁ_resolve_major_minor__mutmut_6, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_7': xǁVersionResolverǁ_resolve_major_minor__mutmut_7, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_8': xǁVersionResolverǁ_resolve_major_minor__mutmut_8, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_9': xǁVersionResolverǁ_resolve_major_minor__mutmut_9, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_10': xǁVersionResolverǁ_resolve_major_minor__mutmut_10, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_11': xǁVersionResolverǁ_resolve_major_minor__mutmut_11, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_12': xǁVersionResolverǁ_resolve_major_minor__mutmut_12, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_13': xǁVersionResolverǁ_resolve_major_minor__mutmut_13, 
        'xǁVersionResolverǁ_resolve_major_minor__mutmut_14': xǁVersionResolverǁ_resolve_major_minor__mutmut_14
    }
    
    def _resolve_major_minor(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁ_resolve_major_minor__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁ_resolve_major_minor__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _resolve_major_minor.__signature__ = _mutmut_signature(xǁVersionResolverǁ_resolve_major_minor__mutmut_orig)
    xǁVersionResolverǁ_resolve_major_minor__mutmut_orig.__name__ = 'xǁVersionResolverǁ_resolve_major_minor'

    def xǁVersionResolverǁ_version_sort_key__mutmut_orig(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_1(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_2(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_3(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_4(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_5(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_6(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_7(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_8(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_9(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_10(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_11(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_12(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_13(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_14(self, version: str) -> semver.VersionInfo:
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

    def xǁVersionResolverǁ_version_sort_key__mutmut_15(self, version: str) -> semver.VersionInfo:
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
    
    xǁVersionResolverǁ_version_sort_key__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁ_version_sort_key__mutmut_1': xǁVersionResolverǁ_version_sort_key__mutmut_1, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_2': xǁVersionResolverǁ_version_sort_key__mutmut_2, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_3': xǁVersionResolverǁ_version_sort_key__mutmut_3, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_4': xǁVersionResolverǁ_version_sort_key__mutmut_4, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_5': xǁVersionResolverǁ_version_sort_key__mutmut_5, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_6': xǁVersionResolverǁ_version_sort_key__mutmut_6, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_7': xǁVersionResolverǁ_version_sort_key__mutmut_7, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_8': xǁVersionResolverǁ_version_sort_key__mutmut_8, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_9': xǁVersionResolverǁ_version_sort_key__mutmut_9, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_10': xǁVersionResolverǁ_version_sort_key__mutmut_10, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_11': xǁVersionResolverǁ_version_sort_key__mutmut_11, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_12': xǁVersionResolverǁ_version_sort_key__mutmut_12, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_13': xǁVersionResolverǁ_version_sort_key__mutmut_13, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_14': xǁVersionResolverǁ_version_sort_key__mutmut_14, 
        'xǁVersionResolverǁ_version_sort_key__mutmut_15': xǁVersionResolverǁ_version_sort_key__mutmut_15
    }
    
    def _version_sort_key(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁ_version_sort_key__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁ_version_sort_key__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _version_sort_key.__signature__ = _mutmut_signature(xǁVersionResolverǁ_version_sort_key__mutmut_orig)
    xǁVersionResolverǁ_version_sort_key__mutmut_orig.__name__ = 'xǁVersionResolverǁ_version_sort_key'

    def xǁVersionResolverǁresolve_versions__mutmut_orig(self, version_patterns: list[str]) -> list[str]:
        """Resolve multiple version patterns."""
        resolved_versions = []
        for pattern in version_patterns:
            try:
                resolved = self.resolve_version(pattern)
                resolved_versions.append(resolved)
            except ValueError as e:
                logger.warning(f"Failed to resolve version pattern '{pattern}': {e}")
        return resolved_versions

    def xǁVersionResolverǁresolve_versions__mutmut_1(self, version_patterns: list[str]) -> list[str]:
        """Resolve multiple version patterns."""
        resolved_versions = None
        for pattern in version_patterns:
            try:
                resolved = self.resolve_version(pattern)
                resolved_versions.append(resolved)
            except ValueError as e:
                logger.warning(f"Failed to resolve version pattern '{pattern}': {e}")
        return resolved_versions

    def xǁVersionResolverǁresolve_versions__mutmut_2(self, version_patterns: list[str]) -> list[str]:
        """Resolve multiple version patterns."""
        resolved_versions = []
        for pattern in version_patterns:
            try:
                resolved = None
                resolved_versions.append(resolved)
            except ValueError as e:
                logger.warning(f"Failed to resolve version pattern '{pattern}': {e}")
        return resolved_versions

    def xǁVersionResolverǁresolve_versions__mutmut_3(self, version_patterns: list[str]) -> list[str]:
        """Resolve multiple version patterns."""
        resolved_versions = []
        for pattern in version_patterns:
            try:
                resolved = self.resolve_version(None)
                resolved_versions.append(resolved)
            except ValueError as e:
                logger.warning(f"Failed to resolve version pattern '{pattern}': {e}")
        return resolved_versions

    def xǁVersionResolverǁresolve_versions__mutmut_4(self, version_patterns: list[str]) -> list[str]:
        """Resolve multiple version patterns."""
        resolved_versions = []
        for pattern in version_patterns:
            try:
                resolved = self.resolve_version(pattern)
                resolved_versions.append(None)
            except ValueError as e:
                logger.warning(f"Failed to resolve version pattern '{pattern}': {e}")
        return resolved_versions

    def xǁVersionResolverǁresolve_versions__mutmut_5(self, version_patterns: list[str]) -> list[str]:
        """Resolve multiple version patterns."""
        resolved_versions = []
        for pattern in version_patterns:
            try:
                resolved = self.resolve_version(pattern)
                resolved_versions.append(resolved)
            except ValueError as e:
                logger.warning(None)
        return resolved_versions
    
    xǁVersionResolverǁresolve_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVersionResolverǁresolve_versions__mutmut_1': xǁVersionResolverǁresolve_versions__mutmut_1, 
        'xǁVersionResolverǁresolve_versions__mutmut_2': xǁVersionResolverǁresolve_versions__mutmut_2, 
        'xǁVersionResolverǁresolve_versions__mutmut_3': xǁVersionResolverǁresolve_versions__mutmut_3, 
        'xǁVersionResolverǁresolve_versions__mutmut_4': xǁVersionResolverǁresolve_versions__mutmut_4, 
        'xǁVersionResolverǁresolve_versions__mutmut_5': xǁVersionResolverǁresolve_versions__mutmut_5
    }
    
    def resolve_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVersionResolverǁresolve_versions__mutmut_orig"), object.__getattribute__(self, "xǁVersionResolverǁresolve_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resolve_versions.__signature__ = _mutmut_signature(xǁVersionResolverǁresolve_versions__mutmut_orig)
    xǁVersionResolverǁresolve_versions__mutmut_orig.__name__ = 'xǁVersionResolverǁresolve_versions'


def x_resolve_tool_versions__mutmut_orig(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = [version_patterns]

    # Get available versions from tool manager
    try:
        available_versions = tool_manager.get_available_versions()
    except Exception as e:
        logger.error(f"Failed to get available versions for {tool_manager.tool_name}: {e}")
        return []

    # Create resolver and resolve patterns
    resolver = VersionResolver(available_versions)
    return resolver.resolve_versions(version_patterns)


def x_resolve_tool_versions__mutmut_1(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = None

    # Get available versions from tool manager
    try:
        available_versions = tool_manager.get_available_versions()
    except Exception as e:
        logger.error(f"Failed to get available versions for {tool_manager.tool_name}: {e}")
        return []

    # Create resolver and resolve patterns
    resolver = VersionResolver(available_versions)
    return resolver.resolve_versions(version_patterns)


def x_resolve_tool_versions__mutmut_2(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = [version_patterns]

    # Get available versions from tool manager
    try:
        available_versions = None
    except Exception as e:
        logger.error(f"Failed to get available versions for {tool_manager.tool_name}: {e}")
        return []

    # Create resolver and resolve patterns
    resolver = VersionResolver(available_versions)
    return resolver.resolve_versions(version_patterns)


def x_resolve_tool_versions__mutmut_3(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = [version_patterns]

    # Get available versions from tool manager
    try:
        available_versions = tool_manager.get_available_versions()
    except Exception as e:
        logger.error(None)
        return []

    # Create resolver and resolve patterns
    resolver = VersionResolver(available_versions)
    return resolver.resolve_versions(version_patterns)


def x_resolve_tool_versions__mutmut_4(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = [version_patterns]

    # Get available versions from tool manager
    try:
        available_versions = tool_manager.get_available_versions()
    except Exception as e:
        logger.error(f"Failed to get available versions for {tool_manager.tool_name}: {e}")
        return []

    # Create resolver and resolve patterns
    resolver = None
    return resolver.resolve_versions(version_patterns)


def x_resolve_tool_versions__mutmut_5(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = [version_patterns]

    # Get available versions from tool manager
    try:
        available_versions = tool_manager.get_available_versions()
    except Exception as e:
        logger.error(f"Failed to get available versions for {tool_manager.tool_name}: {e}")
        return []

    # Create resolver and resolve patterns
    resolver = VersionResolver(None)
    return resolver.resolve_versions(version_patterns)


def x_resolve_tool_versions__mutmut_6(
    tool_manager: BaseToolManager,
    version_patterns: str | list[str],
) -> list[str]:
    """
    Convenience function to resolve version patterns using a tool manager.

    Args:
        tool_manager: Tool manager instance with get_available_versions() method
        version_patterns: Single pattern string or list of patterns

    Returns:
        List of resolved specific versions
    """
    if isinstance(version_patterns, str):
        version_patterns = [version_patterns]

    # Get available versions from tool manager
    try:
        available_versions = tool_manager.get_available_versions()
    except Exception as e:
        logger.error(f"Failed to get available versions for {tool_manager.tool_name}: {e}")
        return []

    # Create resolver and resolve patterns
    resolver = VersionResolver(available_versions)
    return resolver.resolve_versions(None)

x_resolve_tool_versions__mutmut_mutants : ClassVar[MutantDict] = {
'x_resolve_tool_versions__mutmut_1': x_resolve_tool_versions__mutmut_1, 
    'x_resolve_tool_versions__mutmut_2': x_resolve_tool_versions__mutmut_2, 
    'x_resolve_tool_versions__mutmut_3': x_resolve_tool_versions__mutmut_3, 
    'x_resolve_tool_versions__mutmut_4': x_resolve_tool_versions__mutmut_4, 
    'x_resolve_tool_versions__mutmut_5': x_resolve_tool_versions__mutmut_5, 
    'x_resolve_tool_versions__mutmut_6': x_resolve_tool_versions__mutmut_6
}

def resolve_tool_versions(*args, **kwargs):
    result = _mutmut_trampoline(x_resolve_tool_versions__mutmut_orig, x_resolve_tool_versions__mutmut_mutants, args, kwargs)
    return result 

resolve_tool_versions.__signature__ = _mutmut_signature(x_resolve_tool_versions__mutmut_orig)
x_resolve_tool_versions__mutmut_orig.__name__ = 'x_resolve_tool_versions'


# 🧰🌍🔚
