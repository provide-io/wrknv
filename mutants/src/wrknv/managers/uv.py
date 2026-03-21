#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""UV Tool Manager for wrknv
============================
Manages UV (Python package manager) versions for development."""

from __future__ import annotations

import asyncio
import pathlib
from typing import TYPE_CHECKING

from provide.foundation import logger

from wrknv.managers.base import BaseToolManager, ToolManagerError
from wrknv.managers.github import GitHubReleasesClient

if TYPE_CHECKING:
    from wrknv.config import WorkenvConfig
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


class UvManager(BaseToolManager):
    """Manages UV versions using GitHub releases API."""

    def xǁUvManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = None

    def xǁUvManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)
        self._github_client: GitHubReleasesClient | None = None

    def xǁUvManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = ""
    
    xǁUvManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁ__init____mutmut_1': xǁUvManagerǁ__init____mutmut_1, 
        'xǁUvManagerǁ__init____mutmut_2': xǁUvManagerǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUvManagerǁ__init____mutmut_orig)
    xǁUvManagerǁ__init____mutmut_orig.__name__ = 'xǁUvManagerǁ__init__'

    @property
    def github_client(self) -> GitHubReleasesClient:
        """Get or create GitHub client for UV repository."""
        if self._github_client is None:
            self._github_client = GitHubReleasesClient("astral-sh/uv")
        return self._github_client

    @property
    def tool_name(self) -> str:
        return "uv"

    @property
    def executable_name(self) -> str:
        return "uv"

    def xǁUvManagerǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug(None)

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("XXFetching UV versions from GitHubXX")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("fetching uv versions from github")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("FETCHING UV VERSIONS FROM GITHUB")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = None

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting(None, False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", None)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting(False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", )

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("XXinclude_prereleasesXX", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("INCLUDE_PRERELEASES", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", True)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = None

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(None)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=None))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(None)
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch UV versions: {e}") from e

    def xǁUvManagerǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available UV versions from GitHub releases."""
        try:
            logger.debug("Fetching UV versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} UV versions")
            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁUvManagerǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁget_available_versions__mutmut_1': xǁUvManagerǁget_available_versions__mutmut_1, 
        'xǁUvManagerǁget_available_versions__mutmut_2': xǁUvManagerǁget_available_versions__mutmut_2, 
        'xǁUvManagerǁget_available_versions__mutmut_3': xǁUvManagerǁget_available_versions__mutmut_3, 
        'xǁUvManagerǁget_available_versions__mutmut_4': xǁUvManagerǁget_available_versions__mutmut_4, 
        'xǁUvManagerǁget_available_versions__mutmut_5': xǁUvManagerǁget_available_versions__mutmut_5, 
        'xǁUvManagerǁget_available_versions__mutmut_6': xǁUvManagerǁget_available_versions__mutmut_6, 
        'xǁUvManagerǁget_available_versions__mutmut_7': xǁUvManagerǁget_available_versions__mutmut_7, 
        'xǁUvManagerǁget_available_versions__mutmut_8': xǁUvManagerǁget_available_versions__mutmut_8, 
        'xǁUvManagerǁget_available_versions__mutmut_9': xǁUvManagerǁget_available_versions__mutmut_9, 
        'xǁUvManagerǁget_available_versions__mutmut_10': xǁUvManagerǁget_available_versions__mutmut_10, 
        'xǁUvManagerǁget_available_versions__mutmut_11': xǁUvManagerǁget_available_versions__mutmut_11, 
        'xǁUvManagerǁget_available_versions__mutmut_12': xǁUvManagerǁget_available_versions__mutmut_12, 
        'xǁUvManagerǁget_available_versions__mutmut_13': xǁUvManagerǁget_available_versions__mutmut_13, 
        'xǁUvManagerǁget_available_versions__mutmut_14': xǁUvManagerǁget_available_versions__mutmut_14, 
        'xǁUvManagerǁget_available_versions__mutmut_15': xǁUvManagerǁget_available_versions__mutmut_15, 
        'xǁUvManagerǁget_available_versions__mutmut_16': xǁUvManagerǁget_available_versions__mutmut_16, 
        'xǁUvManagerǁget_available_versions__mutmut_17': xǁUvManagerǁget_available_versions__mutmut_17
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁUvManagerǁget_available_versions__mutmut_orig)
    xǁUvManagerǁget_available_versions__mutmut_orig.__name__ = 'xǁUvManagerǁget_available_versions'

    def xǁUvManagerǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_8(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name != "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_9(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "XXdarwinXX":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_10(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "DARWIN":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_11(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = None
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_12(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "XXapple-darwinXX"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_13(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "APPLE-DARWIN"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_14(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name != "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_15(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "XXlinuxXX":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_16(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "LINUX":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_17(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = None
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_18(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "XXunknown-linux-gnuXX"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_19(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "UNKNOWN-LINUX-GNU"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_20(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name != "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_21(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "XXwindowsXX":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_22(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "WINDOWS":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_23(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = None
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_24(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "XXpc-windows-msvcXX"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_25(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "PC-WINDOWS-MSVC"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_26(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(None)

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_27(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch != "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_28(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "XXamd64XX":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_29(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "AMD64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_30(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = None
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_31(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "XXx86_64XX"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_32(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "X86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_33(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch != "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_34(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "XXarm64XX":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_35(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "ARM64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_36(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = None

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_37(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "XXaarch64XX"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_38(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "AARCH64"

        # Return appropriate archive format
        if os_name == "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_39(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name != "windows":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_40(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "XXwindowsXX":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )

    def xǁUvManagerǁget_download_url__mutmut_41(self, version: str) -> str:
        """Get download URL for UV version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # UV uses different naming convention
        if os_name == "darwin":
            platform_name = "apple-darwin"
        elif os_name == "linux":
            platform_name = "unknown-linux-gnu"
        elif os_name == "windows":
            platform_name = "pc-windows-msvc"
        else:
            raise ToolManagerError(f"Unsupported platform for UV: {os_name}")

        # UV uses specific architecture names
        if arch == "amd64":
            arch = "x86_64"
        elif arch == "arm64":
            arch = "aarch64"

        # Return appropriate archive format
        if os_name == "WINDOWS":
            return f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.zip"
        else:
            return (
                f"https://github.com/astral-sh/uv/releases/download/{version}/uv-{arch}-{platform_name}.tar.gz"
            )
    
    xǁUvManagerǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁget_download_url__mutmut_1': xǁUvManagerǁget_download_url__mutmut_1, 
        'xǁUvManagerǁget_download_url__mutmut_2': xǁUvManagerǁget_download_url__mutmut_2, 
        'xǁUvManagerǁget_download_url__mutmut_3': xǁUvManagerǁget_download_url__mutmut_3, 
        'xǁUvManagerǁget_download_url__mutmut_4': xǁUvManagerǁget_download_url__mutmut_4, 
        'xǁUvManagerǁget_download_url__mutmut_5': xǁUvManagerǁget_download_url__mutmut_5, 
        'xǁUvManagerǁget_download_url__mutmut_6': xǁUvManagerǁget_download_url__mutmut_6, 
        'xǁUvManagerǁget_download_url__mutmut_7': xǁUvManagerǁget_download_url__mutmut_7, 
        'xǁUvManagerǁget_download_url__mutmut_8': xǁUvManagerǁget_download_url__mutmut_8, 
        'xǁUvManagerǁget_download_url__mutmut_9': xǁUvManagerǁget_download_url__mutmut_9, 
        'xǁUvManagerǁget_download_url__mutmut_10': xǁUvManagerǁget_download_url__mutmut_10, 
        'xǁUvManagerǁget_download_url__mutmut_11': xǁUvManagerǁget_download_url__mutmut_11, 
        'xǁUvManagerǁget_download_url__mutmut_12': xǁUvManagerǁget_download_url__mutmut_12, 
        'xǁUvManagerǁget_download_url__mutmut_13': xǁUvManagerǁget_download_url__mutmut_13, 
        'xǁUvManagerǁget_download_url__mutmut_14': xǁUvManagerǁget_download_url__mutmut_14, 
        'xǁUvManagerǁget_download_url__mutmut_15': xǁUvManagerǁget_download_url__mutmut_15, 
        'xǁUvManagerǁget_download_url__mutmut_16': xǁUvManagerǁget_download_url__mutmut_16, 
        'xǁUvManagerǁget_download_url__mutmut_17': xǁUvManagerǁget_download_url__mutmut_17, 
        'xǁUvManagerǁget_download_url__mutmut_18': xǁUvManagerǁget_download_url__mutmut_18, 
        'xǁUvManagerǁget_download_url__mutmut_19': xǁUvManagerǁget_download_url__mutmut_19, 
        'xǁUvManagerǁget_download_url__mutmut_20': xǁUvManagerǁget_download_url__mutmut_20, 
        'xǁUvManagerǁget_download_url__mutmut_21': xǁUvManagerǁget_download_url__mutmut_21, 
        'xǁUvManagerǁget_download_url__mutmut_22': xǁUvManagerǁget_download_url__mutmut_22, 
        'xǁUvManagerǁget_download_url__mutmut_23': xǁUvManagerǁget_download_url__mutmut_23, 
        'xǁUvManagerǁget_download_url__mutmut_24': xǁUvManagerǁget_download_url__mutmut_24, 
        'xǁUvManagerǁget_download_url__mutmut_25': xǁUvManagerǁget_download_url__mutmut_25, 
        'xǁUvManagerǁget_download_url__mutmut_26': xǁUvManagerǁget_download_url__mutmut_26, 
        'xǁUvManagerǁget_download_url__mutmut_27': xǁUvManagerǁget_download_url__mutmut_27, 
        'xǁUvManagerǁget_download_url__mutmut_28': xǁUvManagerǁget_download_url__mutmut_28, 
        'xǁUvManagerǁget_download_url__mutmut_29': xǁUvManagerǁget_download_url__mutmut_29, 
        'xǁUvManagerǁget_download_url__mutmut_30': xǁUvManagerǁget_download_url__mutmut_30, 
        'xǁUvManagerǁget_download_url__mutmut_31': xǁUvManagerǁget_download_url__mutmut_31, 
        'xǁUvManagerǁget_download_url__mutmut_32': xǁUvManagerǁget_download_url__mutmut_32, 
        'xǁUvManagerǁget_download_url__mutmut_33': xǁUvManagerǁget_download_url__mutmut_33, 
        'xǁUvManagerǁget_download_url__mutmut_34': xǁUvManagerǁget_download_url__mutmut_34, 
        'xǁUvManagerǁget_download_url__mutmut_35': xǁUvManagerǁget_download_url__mutmut_35, 
        'xǁUvManagerǁget_download_url__mutmut_36': xǁUvManagerǁget_download_url__mutmut_36, 
        'xǁUvManagerǁget_download_url__mutmut_37': xǁUvManagerǁget_download_url__mutmut_37, 
        'xǁUvManagerǁget_download_url__mutmut_38': xǁUvManagerǁget_download_url__mutmut_38, 
        'xǁUvManagerǁget_download_url__mutmut_39': xǁUvManagerǁget_download_url__mutmut_39, 
        'xǁUvManagerǁget_download_url__mutmut_40': xǁUvManagerǁget_download_url__mutmut_40, 
        'xǁUvManagerǁget_download_url__mutmut_41': xǁUvManagerǁget_download_url__mutmut_41
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁUvManagerǁget_download_url__mutmut_orig)
    xǁUvManagerǁget_download_url__mutmut_orig.__name__ = 'xǁUvManagerǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """UV doesn't provide separate checksum files."""
        return None

    def xǁUvManagerǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = None
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name * version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path * self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=None, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=None)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, )

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=False, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=False)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = None
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir * "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "XXbinXX"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "BIN"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=None)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=False)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = None
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir * f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(None, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, None)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, )

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = ""
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob(None):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("XXuv*XX"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("UV*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() or file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name not in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["XXuvXX", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["UV", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "XXuv.exeXX"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "UV.EXE"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = None
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    return

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_36(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_37(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError(None)

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_38(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("XXUV binary not found in archiveXX")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_39(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("uv binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_40(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV BINARY NOT FOUND IN ARCHIVE")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_41(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = None
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_42(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir * uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_43(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(None, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_44(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, None, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_45(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=None)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_46(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_47(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_48(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, )

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_49(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=False)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_50(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(None)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_51(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(None)

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_52(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_53(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_54(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_55(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(None, missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_56(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=None)

    def xǁUvManagerǁ_install_from_archive__mutmut_57(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(missing_ok=True)

    def xǁUvManagerǁ_install_from_archive__mutmut_58(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, )

    def xǁUvManagerǁ_install_from_archive__mutmut_59(self, archive_path: pathlib.Path, version: str) -> None:
        """Install UV from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"uv_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find uv binary in extracted files
            uv_binary = None
            for file_path in extract_dir.rglob("uv*"):
                if file_path.is_file() and file_path.name in ["uv", "uv.exe"]:
                    uv_binary = file_path
                    break

            if not uv_binary:
                raise ToolManagerError("UV binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / uv_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(uv_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed UV binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"UV {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=False)
    
    xǁUvManagerǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁ_install_from_archive__mutmut_1': xǁUvManagerǁ_install_from_archive__mutmut_1, 
        'xǁUvManagerǁ_install_from_archive__mutmut_2': xǁUvManagerǁ_install_from_archive__mutmut_2, 
        'xǁUvManagerǁ_install_from_archive__mutmut_3': xǁUvManagerǁ_install_from_archive__mutmut_3, 
        'xǁUvManagerǁ_install_from_archive__mutmut_4': xǁUvManagerǁ_install_from_archive__mutmut_4, 
        'xǁUvManagerǁ_install_from_archive__mutmut_5': xǁUvManagerǁ_install_from_archive__mutmut_5, 
        'xǁUvManagerǁ_install_from_archive__mutmut_6': xǁUvManagerǁ_install_from_archive__mutmut_6, 
        'xǁUvManagerǁ_install_from_archive__mutmut_7': xǁUvManagerǁ_install_from_archive__mutmut_7, 
        'xǁUvManagerǁ_install_from_archive__mutmut_8': xǁUvManagerǁ_install_from_archive__mutmut_8, 
        'xǁUvManagerǁ_install_from_archive__mutmut_9': xǁUvManagerǁ_install_from_archive__mutmut_9, 
        'xǁUvManagerǁ_install_from_archive__mutmut_10': xǁUvManagerǁ_install_from_archive__mutmut_10, 
        'xǁUvManagerǁ_install_from_archive__mutmut_11': xǁUvManagerǁ_install_from_archive__mutmut_11, 
        'xǁUvManagerǁ_install_from_archive__mutmut_12': xǁUvManagerǁ_install_from_archive__mutmut_12, 
        'xǁUvManagerǁ_install_from_archive__mutmut_13': xǁUvManagerǁ_install_from_archive__mutmut_13, 
        'xǁUvManagerǁ_install_from_archive__mutmut_14': xǁUvManagerǁ_install_from_archive__mutmut_14, 
        'xǁUvManagerǁ_install_from_archive__mutmut_15': xǁUvManagerǁ_install_from_archive__mutmut_15, 
        'xǁUvManagerǁ_install_from_archive__mutmut_16': xǁUvManagerǁ_install_from_archive__mutmut_16, 
        'xǁUvManagerǁ_install_from_archive__mutmut_17': xǁUvManagerǁ_install_from_archive__mutmut_17, 
        'xǁUvManagerǁ_install_from_archive__mutmut_18': xǁUvManagerǁ_install_from_archive__mutmut_18, 
        'xǁUvManagerǁ_install_from_archive__mutmut_19': xǁUvManagerǁ_install_from_archive__mutmut_19, 
        'xǁUvManagerǁ_install_from_archive__mutmut_20': xǁUvManagerǁ_install_from_archive__mutmut_20, 
        'xǁUvManagerǁ_install_from_archive__mutmut_21': xǁUvManagerǁ_install_from_archive__mutmut_21, 
        'xǁUvManagerǁ_install_from_archive__mutmut_22': xǁUvManagerǁ_install_from_archive__mutmut_22, 
        'xǁUvManagerǁ_install_from_archive__mutmut_23': xǁUvManagerǁ_install_from_archive__mutmut_23, 
        'xǁUvManagerǁ_install_from_archive__mutmut_24': xǁUvManagerǁ_install_from_archive__mutmut_24, 
        'xǁUvManagerǁ_install_from_archive__mutmut_25': xǁUvManagerǁ_install_from_archive__mutmut_25, 
        'xǁUvManagerǁ_install_from_archive__mutmut_26': xǁUvManagerǁ_install_from_archive__mutmut_26, 
        'xǁUvManagerǁ_install_from_archive__mutmut_27': xǁUvManagerǁ_install_from_archive__mutmut_27, 
        'xǁUvManagerǁ_install_from_archive__mutmut_28': xǁUvManagerǁ_install_from_archive__mutmut_28, 
        'xǁUvManagerǁ_install_from_archive__mutmut_29': xǁUvManagerǁ_install_from_archive__mutmut_29, 
        'xǁUvManagerǁ_install_from_archive__mutmut_30': xǁUvManagerǁ_install_from_archive__mutmut_30, 
        'xǁUvManagerǁ_install_from_archive__mutmut_31': xǁUvManagerǁ_install_from_archive__mutmut_31, 
        'xǁUvManagerǁ_install_from_archive__mutmut_32': xǁUvManagerǁ_install_from_archive__mutmut_32, 
        'xǁUvManagerǁ_install_from_archive__mutmut_33': xǁUvManagerǁ_install_from_archive__mutmut_33, 
        'xǁUvManagerǁ_install_from_archive__mutmut_34': xǁUvManagerǁ_install_from_archive__mutmut_34, 
        'xǁUvManagerǁ_install_from_archive__mutmut_35': xǁUvManagerǁ_install_from_archive__mutmut_35, 
        'xǁUvManagerǁ_install_from_archive__mutmut_36': xǁUvManagerǁ_install_from_archive__mutmut_36, 
        'xǁUvManagerǁ_install_from_archive__mutmut_37': xǁUvManagerǁ_install_from_archive__mutmut_37, 
        'xǁUvManagerǁ_install_from_archive__mutmut_38': xǁUvManagerǁ_install_from_archive__mutmut_38, 
        'xǁUvManagerǁ_install_from_archive__mutmut_39': xǁUvManagerǁ_install_from_archive__mutmut_39, 
        'xǁUvManagerǁ_install_from_archive__mutmut_40': xǁUvManagerǁ_install_from_archive__mutmut_40, 
        'xǁUvManagerǁ_install_from_archive__mutmut_41': xǁUvManagerǁ_install_from_archive__mutmut_41, 
        'xǁUvManagerǁ_install_from_archive__mutmut_42': xǁUvManagerǁ_install_from_archive__mutmut_42, 
        'xǁUvManagerǁ_install_from_archive__mutmut_43': xǁUvManagerǁ_install_from_archive__mutmut_43, 
        'xǁUvManagerǁ_install_from_archive__mutmut_44': xǁUvManagerǁ_install_from_archive__mutmut_44, 
        'xǁUvManagerǁ_install_from_archive__mutmut_45': xǁUvManagerǁ_install_from_archive__mutmut_45, 
        'xǁUvManagerǁ_install_from_archive__mutmut_46': xǁUvManagerǁ_install_from_archive__mutmut_46, 
        'xǁUvManagerǁ_install_from_archive__mutmut_47': xǁUvManagerǁ_install_from_archive__mutmut_47, 
        'xǁUvManagerǁ_install_from_archive__mutmut_48': xǁUvManagerǁ_install_from_archive__mutmut_48, 
        'xǁUvManagerǁ_install_from_archive__mutmut_49': xǁUvManagerǁ_install_from_archive__mutmut_49, 
        'xǁUvManagerǁ_install_from_archive__mutmut_50': xǁUvManagerǁ_install_from_archive__mutmut_50, 
        'xǁUvManagerǁ_install_from_archive__mutmut_51': xǁUvManagerǁ_install_from_archive__mutmut_51, 
        'xǁUvManagerǁ_install_from_archive__mutmut_52': xǁUvManagerǁ_install_from_archive__mutmut_52, 
        'xǁUvManagerǁ_install_from_archive__mutmut_53': xǁUvManagerǁ_install_from_archive__mutmut_53, 
        'xǁUvManagerǁ_install_from_archive__mutmut_54': xǁUvManagerǁ_install_from_archive__mutmut_54, 
        'xǁUvManagerǁ_install_from_archive__mutmut_55': xǁUvManagerǁ_install_from_archive__mutmut_55, 
        'xǁUvManagerǁ_install_from_archive__mutmut_56': xǁUvManagerǁ_install_from_archive__mutmut_56, 
        'xǁUvManagerǁ_install_from_archive__mutmut_57': xǁUvManagerǁ_install_from_archive__mutmut_57, 
        'xǁUvManagerǁ_install_from_archive__mutmut_58': xǁUvManagerǁ_install_from_archive__mutmut_58, 
        'xǁUvManagerǁ_install_from_archive__mutmut_59': xǁUvManagerǁ_install_from_archive__mutmut_59
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁUvManagerǁ_install_from_archive__mutmut_orig)
    xǁUvManagerǁ_install_from_archive__mutmut_orig.__name__ = 'xǁUvManagerǁ_install_from_archive'

    def xǁUvManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(None)
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return True

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = None

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                None,
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=None,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=None,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=None,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(None), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "XX--versionXX"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--VERSION"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=False,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=False,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=11,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode != 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 1:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version not in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(None)
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return False
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(None)
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(None)

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return True

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return False

    def xǁUvManagerǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(None)
            return False

    def xǁUvManagerǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that UV installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"UV binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches (UV outputs "uv 0.4.15")
                if version in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"UV {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in UV output: {result.stdout}")
            else:
                logger.error(f"UV version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify UV installation: {e}")
            return True
    
    xǁUvManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁverify_installation__mutmut_1': xǁUvManagerǁverify_installation__mutmut_1, 
        'xǁUvManagerǁverify_installation__mutmut_2': xǁUvManagerǁverify_installation__mutmut_2, 
        'xǁUvManagerǁverify_installation__mutmut_3': xǁUvManagerǁverify_installation__mutmut_3, 
        'xǁUvManagerǁverify_installation__mutmut_4': xǁUvManagerǁverify_installation__mutmut_4, 
        'xǁUvManagerǁverify_installation__mutmut_5': xǁUvManagerǁverify_installation__mutmut_5, 
        'xǁUvManagerǁverify_installation__mutmut_6': xǁUvManagerǁverify_installation__mutmut_6, 
        'xǁUvManagerǁverify_installation__mutmut_7': xǁUvManagerǁverify_installation__mutmut_7, 
        'xǁUvManagerǁverify_installation__mutmut_8': xǁUvManagerǁverify_installation__mutmut_8, 
        'xǁUvManagerǁverify_installation__mutmut_9': xǁUvManagerǁverify_installation__mutmut_9, 
        'xǁUvManagerǁverify_installation__mutmut_10': xǁUvManagerǁverify_installation__mutmut_10, 
        'xǁUvManagerǁverify_installation__mutmut_11': xǁUvManagerǁverify_installation__mutmut_11, 
        'xǁUvManagerǁverify_installation__mutmut_12': xǁUvManagerǁverify_installation__mutmut_12, 
        'xǁUvManagerǁverify_installation__mutmut_13': xǁUvManagerǁverify_installation__mutmut_13, 
        'xǁUvManagerǁverify_installation__mutmut_14': xǁUvManagerǁverify_installation__mutmut_14, 
        'xǁUvManagerǁverify_installation__mutmut_15': xǁUvManagerǁverify_installation__mutmut_15, 
        'xǁUvManagerǁverify_installation__mutmut_16': xǁUvManagerǁverify_installation__mutmut_16, 
        'xǁUvManagerǁverify_installation__mutmut_17': xǁUvManagerǁverify_installation__mutmut_17, 
        'xǁUvManagerǁverify_installation__mutmut_18': xǁUvManagerǁverify_installation__mutmut_18, 
        'xǁUvManagerǁverify_installation__mutmut_19': xǁUvManagerǁverify_installation__mutmut_19, 
        'xǁUvManagerǁverify_installation__mutmut_20': xǁUvManagerǁverify_installation__mutmut_20, 
        'xǁUvManagerǁverify_installation__mutmut_21': xǁUvManagerǁverify_installation__mutmut_21, 
        'xǁUvManagerǁverify_installation__mutmut_22': xǁUvManagerǁverify_installation__mutmut_22, 
        'xǁUvManagerǁverify_installation__mutmut_23': xǁUvManagerǁverify_installation__mutmut_23, 
        'xǁUvManagerǁverify_installation__mutmut_24': xǁUvManagerǁverify_installation__mutmut_24, 
        'xǁUvManagerǁverify_installation__mutmut_25': xǁUvManagerǁverify_installation__mutmut_25, 
        'xǁUvManagerǁverify_installation__mutmut_26': xǁUvManagerǁverify_installation__mutmut_26, 
        'xǁUvManagerǁverify_installation__mutmut_27': xǁUvManagerǁverify_installation__mutmut_27, 
        'xǁUvManagerǁverify_installation__mutmut_28': xǁUvManagerǁverify_installation__mutmut_28, 
        'xǁUvManagerǁverify_installation__mutmut_29': xǁUvManagerǁverify_installation__mutmut_29, 
        'xǁUvManagerǁverify_installation__mutmut_30': xǁUvManagerǁverify_installation__mutmut_30
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁUvManagerǁverify_installation__mutmut_orig)
    xǁUvManagerǁverify_installation__mutmut_orig.__name__ = 'xǁUvManagerǁverify_installation'

    def xǁUvManagerǁget_harness_compatibility__mutmut_orig(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_1(self) -> dict:
        """Get compatibility information for Python tools."""
        version = None
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_2(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_3(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"XXstatusXX": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_4(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"STATUS": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_5(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "XXnot_installedXX"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_6(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "NOT_INSTALLED"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_7(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = None

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_8(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "XXstatusXX": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_9(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "STATUS": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_10(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "XXcompatibleXX",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_11(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "COMPATIBLE",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_12(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "XXversionXX": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_13(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "VERSION": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_14(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "XXharnessXX": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_15(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "HARNESS": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_16(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "XXpython.ctyXX": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_17(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "PYTHON.CTY": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_18(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(None),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_19(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "XXpython.hclXX": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_20(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "PYTHON.HCL": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_21(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(None),
                "python.wire": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_22(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "XXpython.wireXX": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_23(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "PYTHON.WIRE": self._check_python_wire_compatibility(version),
            },
        }

        return compatibility

    def xǁUvManagerǁget_harness_compatibility__mutmut_24(self) -> dict:
        """Get compatibility information for Python tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Python tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "python.cty": self._check_python_cty_compatibility(version),
                "python.hcl": self._check_python_hcl_compatibility(version),
                "python.wire": self._check_python_wire_compatibility(None),
            },
        }

        return compatibility
    
    xǁUvManagerǁget_harness_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁget_harness_compatibility__mutmut_1': xǁUvManagerǁget_harness_compatibility__mutmut_1, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_2': xǁUvManagerǁget_harness_compatibility__mutmut_2, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_3': xǁUvManagerǁget_harness_compatibility__mutmut_3, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_4': xǁUvManagerǁget_harness_compatibility__mutmut_4, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_5': xǁUvManagerǁget_harness_compatibility__mutmut_5, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_6': xǁUvManagerǁget_harness_compatibility__mutmut_6, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_7': xǁUvManagerǁget_harness_compatibility__mutmut_7, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_8': xǁUvManagerǁget_harness_compatibility__mutmut_8, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_9': xǁUvManagerǁget_harness_compatibility__mutmut_9, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_10': xǁUvManagerǁget_harness_compatibility__mutmut_10, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_11': xǁUvManagerǁget_harness_compatibility__mutmut_11, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_12': xǁUvManagerǁget_harness_compatibility__mutmut_12, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_13': xǁUvManagerǁget_harness_compatibility__mutmut_13, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_14': xǁUvManagerǁget_harness_compatibility__mutmut_14, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_15': xǁUvManagerǁget_harness_compatibility__mutmut_15, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_16': xǁUvManagerǁget_harness_compatibility__mutmut_16, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_17': xǁUvManagerǁget_harness_compatibility__mutmut_17, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_18': xǁUvManagerǁget_harness_compatibility__mutmut_18, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_19': xǁUvManagerǁget_harness_compatibility__mutmut_19, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_20': xǁUvManagerǁget_harness_compatibility__mutmut_20, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_21': xǁUvManagerǁget_harness_compatibility__mutmut_21, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_22': xǁUvManagerǁget_harness_compatibility__mutmut_22, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_23': xǁUvManagerǁget_harness_compatibility__mutmut_23, 
        'xǁUvManagerǁget_harness_compatibility__mutmut_24': xǁUvManagerǁget_harness_compatibility__mutmut_24
    }
    
    def get_harness_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁget_harness_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁget_harness_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_harness_compatibility.__signature__ = _mutmut_signature(xǁUvManagerǁget_harness_compatibility__mutmut_orig)
    xǁUvManagerǁget_harness_compatibility__mutmut_orig.__name__ = 'xǁUvManagerǁget_harness_compatibility'

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": True,
            "notes": "Python CTY tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "XXcompatibleXX": True,
            "notes": "Python CTY tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "COMPATIBLE": True,
            "notes": "Python CTY tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": False,
            "notes": "Python CTY tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": True,
            "XXnotesXX": "Python CTY tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": True,
            "NOTES": "Python CTY tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": True,
            "notes": "XXPython CTY tools compatible with all UV versionsXX",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": True,
            "notes": "python cty tools compatible with all uv versions",
        }

    def xǁUvManagerǁ_check_python_cty_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with Python CTY tools."""
        return {
            "compatible": True,
            "notes": "PYTHON CTY TOOLS COMPATIBLE WITH ALL UV VERSIONS",
        }
    
    xǁUvManagerǁ_check_python_cty_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_1': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_1, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_2': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_2, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_3': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_3, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_4': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_4, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_5': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_5, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_6': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_6, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_7': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_7, 
        'xǁUvManagerǁ_check_python_cty_compatibility__mutmut_8': xǁUvManagerǁ_check_python_cty_compatibility__mutmut_8
    }
    
    def _check_python_cty_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁ_check_python_cty_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁ_check_python_cty_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_python_cty_compatibility.__signature__ = _mutmut_signature(xǁUvManagerǁ_check_python_cty_compatibility__mutmut_orig)
    xǁUvManagerǁ_check_python_cty_compatibility__mutmut_orig.__name__ = 'xǁUvManagerǁ_check_python_cty_compatibility'

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": True,
            "notes": "Python HCL tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "XXcompatibleXX": True,
            "notes": "Python HCL tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "COMPATIBLE": True,
            "notes": "Python HCL tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": False,
            "notes": "Python HCL tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": True,
            "XXnotesXX": "Python HCL tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": True,
            "NOTES": "Python HCL tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": True,
            "notes": "XXPython HCL tools compatible with all UV versionsXX",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": True,
            "notes": "python hcl tools compatible with all uv versions",
        }

    def xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with Python HCL tools."""
        return {
            "compatible": True,
            "notes": "PYTHON HCL TOOLS COMPATIBLE WITH ALL UV VERSIONS",
        }
    
    xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_1': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_1, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_2': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_2, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_3': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_3, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_4': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_4, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_5': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_5, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_6': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_6, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_7': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_7, 
        'xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_8': xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_8
    }
    
    def _check_python_hcl_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_python_hcl_compatibility.__signature__ = _mutmut_signature(xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_orig)
    xǁUvManagerǁ_check_python_hcl_compatibility__mutmut_orig.__name__ = 'xǁUvManagerǁ_check_python_hcl_compatibility'

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": True,
            "notes": "Python wire protocol tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "XXcompatibleXX": True,
            "notes": "Python wire protocol tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "COMPATIBLE": True,
            "notes": "Python wire protocol tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": False,
            "notes": "Python wire protocol tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": True,
            "XXnotesXX": "Python wire protocol tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": True,
            "NOTES": "Python wire protocol tools compatible with all UV versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": True,
            "notes": "XXPython wire protocol tools compatible with all UV versionsXX",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": True,
            "notes": "python wire protocol tools compatible with all uv versions",
        }

    def xǁUvManagerǁ_check_python_wire_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with Python wire protocol tools."""
        return {
            "compatible": True,
            "notes": "PYTHON WIRE PROTOCOL TOOLS COMPATIBLE WITH ALL UV VERSIONS",
        }
    
    xǁUvManagerǁ_check_python_wire_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_1': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_1, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_2': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_2, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_3': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_3, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_4': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_4, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_5': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_5, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_6': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_6, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_7': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_7, 
        'xǁUvManagerǁ_check_python_wire_compatibility__mutmut_8': xǁUvManagerǁ_check_python_wire_compatibility__mutmut_8
    }
    
    def _check_python_wire_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUvManagerǁ_check_python_wire_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁUvManagerǁ_check_python_wire_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_python_wire_compatibility.__signature__ = _mutmut_signature(xǁUvManagerǁ_check_python_wire_compatibility__mutmut_orig)
    xǁUvManagerǁ_check_python_wire_compatibility__mutmut_orig.__name__ = 'xǁUvManagerǁ_check_python_wire_compatibility'


# 🧰🌍🔚
