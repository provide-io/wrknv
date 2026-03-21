#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""OpenBao Tool Manager for wrknv
===============================
Manages OpenBao (open source Vault fork) versions for development."""

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


class BaoManager(BaseToolManager):
    """Manages OpenBao versions using GitHub releases API."""

    def xǁBaoManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = None

    def xǁBaoManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)
        self._github_client: GitHubReleasesClient | None = None

    def xǁBaoManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = ""
    
    xǁBaoManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoManagerǁ__init____mutmut_1': xǁBaoManagerǁ__init____mutmut_1, 
        'xǁBaoManagerǁ__init____mutmut_2': xǁBaoManagerǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBaoManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBaoManagerǁ__init____mutmut_orig)
    xǁBaoManagerǁ__init____mutmut_orig.__name__ = 'xǁBaoManagerǁ__init__'

    @property
    def github_client(self) -> GitHubReleasesClient:
        """Get or create GitHub client for OpenBao repository."""
        if self._github_client is None:
            self._github_client = GitHubReleasesClient("openbao/openbao")
        return self._github_client

    @property
    def tool_name(self) -> str:
        return "bao"

    @property
    def executable_name(self) -> str:
        return "bao"

    def xǁBaoManagerǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug(None)

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("XXFetching OpenBao versions from GitHubXX")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("fetching openbao versions from github")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("FETCHING OPENBAO VERSIONS FROM GITHUB")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = None

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting(None, False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", None)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting(False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", )

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("XXinclude_prereleasesXX", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("INCLUDE_PRERELEASES", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", True)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = None

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(None)

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=None))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(None)
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoManagerǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁBaoManagerǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoManagerǁget_available_versions__mutmut_1': xǁBaoManagerǁget_available_versions__mutmut_1, 
        'xǁBaoManagerǁget_available_versions__mutmut_2': xǁBaoManagerǁget_available_versions__mutmut_2, 
        'xǁBaoManagerǁget_available_versions__mutmut_3': xǁBaoManagerǁget_available_versions__mutmut_3, 
        'xǁBaoManagerǁget_available_versions__mutmut_4': xǁBaoManagerǁget_available_versions__mutmut_4, 
        'xǁBaoManagerǁget_available_versions__mutmut_5': xǁBaoManagerǁget_available_versions__mutmut_5, 
        'xǁBaoManagerǁget_available_versions__mutmut_6': xǁBaoManagerǁget_available_versions__mutmut_6, 
        'xǁBaoManagerǁget_available_versions__mutmut_7': xǁBaoManagerǁget_available_versions__mutmut_7, 
        'xǁBaoManagerǁget_available_versions__mutmut_8': xǁBaoManagerǁget_available_versions__mutmut_8, 
        'xǁBaoManagerǁget_available_versions__mutmut_9': xǁBaoManagerǁget_available_versions__mutmut_9, 
        'xǁBaoManagerǁget_available_versions__mutmut_10': xǁBaoManagerǁget_available_versions__mutmut_10, 
        'xǁBaoManagerǁget_available_versions__mutmut_11': xǁBaoManagerǁget_available_versions__mutmut_11, 
        'xǁBaoManagerǁget_available_versions__mutmut_12': xǁBaoManagerǁget_available_versions__mutmut_12, 
        'xǁBaoManagerǁget_available_versions__mutmut_13': xǁBaoManagerǁget_available_versions__mutmut_13, 
        'xǁBaoManagerǁget_available_versions__mutmut_14': xǁBaoManagerǁget_available_versions__mutmut_14, 
        'xǁBaoManagerǁget_available_versions__mutmut_15': xǁBaoManagerǁget_available_versions__mutmut_15, 
        'xǁBaoManagerǁget_available_versions__mutmut_16': xǁBaoManagerǁget_available_versions__mutmut_16, 
        'xǁBaoManagerǁget_available_versions__mutmut_17': xǁBaoManagerǁget_available_versions__mutmut_17
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoManagerǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁBaoManagerǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁBaoManagerǁget_available_versions__mutmut_orig)
    xǁBaoManagerǁget_available_versions__mutmut_orig.__name__ = 'xǁBaoManagerǁget_available_versions'

    def xǁBaoManagerǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoManagerǁget_download_url__mutmut_8(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = None

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"
    
    xǁBaoManagerǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoManagerǁget_download_url__mutmut_1': xǁBaoManagerǁget_download_url__mutmut_1, 
        'xǁBaoManagerǁget_download_url__mutmut_2': xǁBaoManagerǁget_download_url__mutmut_2, 
        'xǁBaoManagerǁget_download_url__mutmut_3': xǁBaoManagerǁget_download_url__mutmut_3, 
        'xǁBaoManagerǁget_download_url__mutmut_4': xǁBaoManagerǁget_download_url__mutmut_4, 
        'xǁBaoManagerǁget_download_url__mutmut_5': xǁBaoManagerǁget_download_url__mutmut_5, 
        'xǁBaoManagerǁget_download_url__mutmut_6': xǁBaoManagerǁget_download_url__mutmut_6, 
        'xǁBaoManagerǁget_download_url__mutmut_7': xǁBaoManagerǁget_download_url__mutmut_7, 
        'xǁBaoManagerǁget_download_url__mutmut_8': xǁBaoManagerǁget_download_url__mutmut_8
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoManagerǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁBaoManagerǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁBaoManagerǁget_download_url__mutmut_orig)
    xǁBaoManagerǁget_download_url__mutmut_orig.__name__ = 'xǁBaoManagerǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """Get checksum URL for OpenBao version."""
        # OpenBao provides SHA256SUMS file
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_SHA256SUMS"

    def xǁBaoManagerǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = None
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name * version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path * self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=None, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=None)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, )

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=False, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=False)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = None
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir * "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "XXbinXX"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "BIN"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=None)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=False)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
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

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir * f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(None, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, None)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, )

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = ""
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob(None):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("XXbao*XX"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("BAO*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() or file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name not in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["XXbaoXX", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["BAO", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "XXbao.exeXX"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "BAO.EXE"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = None
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    return

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_36(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_37(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError(None)

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_38(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("XXOpenBao binary not found in archiveXX")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_39(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("openbao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_40(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OPENBAO BINARY NOT FOUND IN ARCHIVE")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_41(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = None
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_42(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir * bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_43(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(None, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_44(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, None, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_45(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=None)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_46(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_47(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_48(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, )

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_49(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=False)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_50(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(None)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_51(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(None)

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_52(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_53(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_54(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_55(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(None, missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_56(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=None)

    def xǁBaoManagerǁ_install_from_archive__mutmut_57(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(missing_ok=True)

    def xǁBaoManagerǁ_install_from_archive__mutmut_58(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, )

    def xǁBaoManagerǁ_install_from_archive__mutmut_59(self, archive_path: pathlib.Path, version: str) -> None:
        """Install OpenBao from downloaded archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create bin subdirectory
        bin_dir = version_dir / "bin"
        bin_dir.mkdir(exist_ok=True)

        # Extract archive
        extract_dir = self.cache_dir / f"bao_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find bao binary in extracted files
            bao_binary = None
            for file_path in extract_dir.rglob("bao*"):
                if file_path.is_file() and file_path.name in ["bao", "bao.exe"]:
                    bao_binary = file_path
                    break

            if not bao_binary:
                raise ToolManagerError("OpenBao binary not found in archive")

            # Copy to bin directory
            target_path = bin_dir / bao_binary.name
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_copy(bao_binary, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed OpenBao binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"OpenBao {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_copy, safe_rmtree

            safe_rmtree(extract_dir, missing_ok=False)
    
    xǁBaoManagerǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoManagerǁ_install_from_archive__mutmut_1': xǁBaoManagerǁ_install_from_archive__mutmut_1, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_2': xǁBaoManagerǁ_install_from_archive__mutmut_2, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_3': xǁBaoManagerǁ_install_from_archive__mutmut_3, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_4': xǁBaoManagerǁ_install_from_archive__mutmut_4, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_5': xǁBaoManagerǁ_install_from_archive__mutmut_5, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_6': xǁBaoManagerǁ_install_from_archive__mutmut_6, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_7': xǁBaoManagerǁ_install_from_archive__mutmut_7, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_8': xǁBaoManagerǁ_install_from_archive__mutmut_8, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_9': xǁBaoManagerǁ_install_from_archive__mutmut_9, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_10': xǁBaoManagerǁ_install_from_archive__mutmut_10, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_11': xǁBaoManagerǁ_install_from_archive__mutmut_11, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_12': xǁBaoManagerǁ_install_from_archive__mutmut_12, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_13': xǁBaoManagerǁ_install_from_archive__mutmut_13, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_14': xǁBaoManagerǁ_install_from_archive__mutmut_14, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_15': xǁBaoManagerǁ_install_from_archive__mutmut_15, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_16': xǁBaoManagerǁ_install_from_archive__mutmut_16, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_17': xǁBaoManagerǁ_install_from_archive__mutmut_17, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_18': xǁBaoManagerǁ_install_from_archive__mutmut_18, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_19': xǁBaoManagerǁ_install_from_archive__mutmut_19, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_20': xǁBaoManagerǁ_install_from_archive__mutmut_20, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_21': xǁBaoManagerǁ_install_from_archive__mutmut_21, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_22': xǁBaoManagerǁ_install_from_archive__mutmut_22, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_23': xǁBaoManagerǁ_install_from_archive__mutmut_23, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_24': xǁBaoManagerǁ_install_from_archive__mutmut_24, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_25': xǁBaoManagerǁ_install_from_archive__mutmut_25, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_26': xǁBaoManagerǁ_install_from_archive__mutmut_26, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_27': xǁBaoManagerǁ_install_from_archive__mutmut_27, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_28': xǁBaoManagerǁ_install_from_archive__mutmut_28, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_29': xǁBaoManagerǁ_install_from_archive__mutmut_29, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_30': xǁBaoManagerǁ_install_from_archive__mutmut_30, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_31': xǁBaoManagerǁ_install_from_archive__mutmut_31, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_32': xǁBaoManagerǁ_install_from_archive__mutmut_32, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_33': xǁBaoManagerǁ_install_from_archive__mutmut_33, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_34': xǁBaoManagerǁ_install_from_archive__mutmut_34, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_35': xǁBaoManagerǁ_install_from_archive__mutmut_35, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_36': xǁBaoManagerǁ_install_from_archive__mutmut_36, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_37': xǁBaoManagerǁ_install_from_archive__mutmut_37, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_38': xǁBaoManagerǁ_install_from_archive__mutmut_38, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_39': xǁBaoManagerǁ_install_from_archive__mutmut_39, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_40': xǁBaoManagerǁ_install_from_archive__mutmut_40, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_41': xǁBaoManagerǁ_install_from_archive__mutmut_41, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_42': xǁBaoManagerǁ_install_from_archive__mutmut_42, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_43': xǁBaoManagerǁ_install_from_archive__mutmut_43, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_44': xǁBaoManagerǁ_install_from_archive__mutmut_44, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_45': xǁBaoManagerǁ_install_from_archive__mutmut_45, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_46': xǁBaoManagerǁ_install_from_archive__mutmut_46, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_47': xǁBaoManagerǁ_install_from_archive__mutmut_47, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_48': xǁBaoManagerǁ_install_from_archive__mutmut_48, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_49': xǁBaoManagerǁ_install_from_archive__mutmut_49, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_50': xǁBaoManagerǁ_install_from_archive__mutmut_50, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_51': xǁBaoManagerǁ_install_from_archive__mutmut_51, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_52': xǁBaoManagerǁ_install_from_archive__mutmut_52, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_53': xǁBaoManagerǁ_install_from_archive__mutmut_53, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_54': xǁBaoManagerǁ_install_from_archive__mutmut_54, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_55': xǁBaoManagerǁ_install_from_archive__mutmut_55, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_56': xǁBaoManagerǁ_install_from_archive__mutmut_56, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_57': xǁBaoManagerǁ_install_from_archive__mutmut_57, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_58': xǁBaoManagerǁ_install_from_archive__mutmut_58, 
        'xǁBaoManagerǁ_install_from_archive__mutmut_59': xǁBaoManagerǁ_install_from_archive__mutmut_59
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoManagerǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁBaoManagerǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁBaoManagerǁ_install_from_archive__mutmut_orig)
    xǁBaoManagerǁ_install_from_archive__mutmut_orig.__name__ = 'xǁBaoManagerǁ_install_from_archive'

    def xǁBaoManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(None)
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return True

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = None

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
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
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=None,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=None,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=None,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(None), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "XXversionXX"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "VERSION"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=False,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=False,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=11,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode != 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 1:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout and f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version not in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" not in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(None)
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return False
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(None)
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(None)

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return True

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return False

    def xǁBaoManagerǁverify_installation__mutmut_31(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(None)
            return False

    def xǁBaoManagerǁverify_installation__mutmut_32(self, version: str) -> bool:
        """Verify that OpenBao installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenBao binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # OpenBao version output: "Bao v2.1.0 (1234abcd), built 2024-01-01T00:00:00Z"
                if version in result.stdout or f"v{version}" in result.stdout:
                    if logger.is_debug_enabled():
                        logger.debug(f"OpenBao {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenBao output: {result.stdout}")
            else:
                logger.error(f"OpenBao version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenBao installation: {e}")
            return True
    
    xǁBaoManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoManagerǁverify_installation__mutmut_1': xǁBaoManagerǁverify_installation__mutmut_1, 
        'xǁBaoManagerǁverify_installation__mutmut_2': xǁBaoManagerǁverify_installation__mutmut_2, 
        'xǁBaoManagerǁverify_installation__mutmut_3': xǁBaoManagerǁverify_installation__mutmut_3, 
        'xǁBaoManagerǁverify_installation__mutmut_4': xǁBaoManagerǁverify_installation__mutmut_4, 
        'xǁBaoManagerǁverify_installation__mutmut_5': xǁBaoManagerǁverify_installation__mutmut_5, 
        'xǁBaoManagerǁverify_installation__mutmut_6': xǁBaoManagerǁverify_installation__mutmut_6, 
        'xǁBaoManagerǁverify_installation__mutmut_7': xǁBaoManagerǁverify_installation__mutmut_7, 
        'xǁBaoManagerǁverify_installation__mutmut_8': xǁBaoManagerǁverify_installation__mutmut_8, 
        'xǁBaoManagerǁverify_installation__mutmut_9': xǁBaoManagerǁverify_installation__mutmut_9, 
        'xǁBaoManagerǁverify_installation__mutmut_10': xǁBaoManagerǁverify_installation__mutmut_10, 
        'xǁBaoManagerǁverify_installation__mutmut_11': xǁBaoManagerǁverify_installation__mutmut_11, 
        'xǁBaoManagerǁverify_installation__mutmut_12': xǁBaoManagerǁverify_installation__mutmut_12, 
        'xǁBaoManagerǁverify_installation__mutmut_13': xǁBaoManagerǁverify_installation__mutmut_13, 
        'xǁBaoManagerǁverify_installation__mutmut_14': xǁBaoManagerǁverify_installation__mutmut_14, 
        'xǁBaoManagerǁverify_installation__mutmut_15': xǁBaoManagerǁverify_installation__mutmut_15, 
        'xǁBaoManagerǁverify_installation__mutmut_16': xǁBaoManagerǁverify_installation__mutmut_16, 
        'xǁBaoManagerǁverify_installation__mutmut_17': xǁBaoManagerǁverify_installation__mutmut_17, 
        'xǁBaoManagerǁverify_installation__mutmut_18': xǁBaoManagerǁverify_installation__mutmut_18, 
        'xǁBaoManagerǁverify_installation__mutmut_19': xǁBaoManagerǁverify_installation__mutmut_19, 
        'xǁBaoManagerǁverify_installation__mutmut_20': xǁBaoManagerǁverify_installation__mutmut_20, 
        'xǁBaoManagerǁverify_installation__mutmut_21': xǁBaoManagerǁverify_installation__mutmut_21, 
        'xǁBaoManagerǁverify_installation__mutmut_22': xǁBaoManagerǁverify_installation__mutmut_22, 
        'xǁBaoManagerǁverify_installation__mutmut_23': xǁBaoManagerǁverify_installation__mutmut_23, 
        'xǁBaoManagerǁverify_installation__mutmut_24': xǁBaoManagerǁverify_installation__mutmut_24, 
        'xǁBaoManagerǁverify_installation__mutmut_25': xǁBaoManagerǁverify_installation__mutmut_25, 
        'xǁBaoManagerǁverify_installation__mutmut_26': xǁBaoManagerǁverify_installation__mutmut_26, 
        'xǁBaoManagerǁverify_installation__mutmut_27': xǁBaoManagerǁverify_installation__mutmut_27, 
        'xǁBaoManagerǁverify_installation__mutmut_28': xǁBaoManagerǁverify_installation__mutmut_28, 
        'xǁBaoManagerǁverify_installation__mutmut_29': xǁBaoManagerǁverify_installation__mutmut_29, 
        'xǁBaoManagerǁverify_installation__mutmut_30': xǁBaoManagerǁverify_installation__mutmut_30, 
        'xǁBaoManagerǁverify_installation__mutmut_31': xǁBaoManagerǁverify_installation__mutmut_31, 
        'xǁBaoManagerǁverify_installation__mutmut_32': xǁBaoManagerǁverify_installation__mutmut_32
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁBaoManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁBaoManagerǁverify_installation__mutmut_orig)
    xǁBaoManagerǁverify_installation__mutmut_orig.__name__ = 'xǁBaoManagerǁverify_installation'


__all__ = [
    "BaoManager",
]

# 🧰🌍🔚
