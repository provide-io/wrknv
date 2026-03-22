#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""OpenBao Variant for SubRosaManager
===================================
Manages OpenBao (open source Vault fork) versions for development."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

from provide.foundation import logger

from wrknv.managers.base import ToolManagerError
from wrknv.managers.github import GitHubReleasesClient
from wrknv.managers.subrosa.base import SubRosaManager

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


class BaoVariant(SubRosaManager):
    """OpenBao variant of secret management tools."""

    def xǁBaoVariantǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = None

    def xǁBaoVariantǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)
        self._github_client: GitHubReleasesClient | None = None

    def xǁBaoVariantǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = ""
    
    xǁBaoVariantǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoVariantǁ__init____mutmut_1': xǁBaoVariantǁ__init____mutmut_1, 
        'xǁBaoVariantǁ__init____mutmut_2': xǁBaoVariantǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoVariantǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBaoVariantǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBaoVariantǁ__init____mutmut_orig)
    xǁBaoVariantǁ__init____mutmut_orig.__name__ = 'xǁBaoVariantǁ__init__'

    @property
    def variant_name(self) -> str:
        """Variant name for this secret manager."""
        return "bao"

    @property
    def github_client(self) -> GitHubReleasesClient:
        """Get or create GitHub client for OpenBao repository."""
        if self._github_client is None:
            self._github_client = GitHubReleasesClient("openbao/openbao")
        return self._github_client

    def xǁBaoVariantǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug(None)

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("XXFetching OpenBao versions from GitHubXX")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("fetching openbao versions from github")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("FETCHING OPENBAO VERSIONS FROM GITHUB")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = None

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting(None, False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", None)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting(False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", )

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("XXinclude_prereleasesXX", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("INCLUDE_PRERELEASES", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", True)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = None

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(None)

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=None))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(None)
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenBao versions: {e}") from e

    def xǁBaoVariantǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available OpenBao versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenBao versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            # OpenBao versions have 'v' prefix in tags, already stripped by client
            logger.debug(f"Found {len(versions)} OpenBao versions")
            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁBaoVariantǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoVariantǁget_available_versions__mutmut_1': xǁBaoVariantǁget_available_versions__mutmut_1, 
        'xǁBaoVariantǁget_available_versions__mutmut_2': xǁBaoVariantǁget_available_versions__mutmut_2, 
        'xǁBaoVariantǁget_available_versions__mutmut_3': xǁBaoVariantǁget_available_versions__mutmut_3, 
        'xǁBaoVariantǁget_available_versions__mutmut_4': xǁBaoVariantǁget_available_versions__mutmut_4, 
        'xǁBaoVariantǁget_available_versions__mutmut_5': xǁBaoVariantǁget_available_versions__mutmut_5, 
        'xǁBaoVariantǁget_available_versions__mutmut_6': xǁBaoVariantǁget_available_versions__mutmut_6, 
        'xǁBaoVariantǁget_available_versions__mutmut_7': xǁBaoVariantǁget_available_versions__mutmut_7, 
        'xǁBaoVariantǁget_available_versions__mutmut_8': xǁBaoVariantǁget_available_versions__mutmut_8, 
        'xǁBaoVariantǁget_available_versions__mutmut_9': xǁBaoVariantǁget_available_versions__mutmut_9, 
        'xǁBaoVariantǁget_available_versions__mutmut_10': xǁBaoVariantǁget_available_versions__mutmut_10, 
        'xǁBaoVariantǁget_available_versions__mutmut_11': xǁBaoVariantǁget_available_versions__mutmut_11, 
        'xǁBaoVariantǁget_available_versions__mutmut_12': xǁBaoVariantǁget_available_versions__mutmut_12, 
        'xǁBaoVariantǁget_available_versions__mutmut_13': xǁBaoVariantǁget_available_versions__mutmut_13, 
        'xǁBaoVariantǁget_available_versions__mutmut_14': xǁBaoVariantǁget_available_versions__mutmut_14, 
        'xǁBaoVariantǁget_available_versions__mutmut_15': xǁBaoVariantǁget_available_versions__mutmut_15, 
        'xǁBaoVariantǁget_available_versions__mutmut_16': xǁBaoVariantǁget_available_versions__mutmut_16, 
        'xǁBaoVariantǁget_available_versions__mutmut_17': xǁBaoVariantǁget_available_versions__mutmut_17
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoVariantǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁBaoVariantǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁBaoVariantǁget_available_versions__mutmut_orig)
    xǁBaoVariantǁget_available_versions__mutmut_orig.__name__ = 'xǁBaoVariantǁget_available_versions'

    def xǁBaoVariantǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = os_name.capitalize()

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"

    def xǁBaoVariantǁget_download_url__mutmut_8(self, version: str) -> str:
        """Get download URL for OpenBao version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # OpenBao uses capitalized OS names: Darwin, Linux, Windows
        os_capitalized = None

        # OpenBao naming: bao_2.1.0_Darwin_arm64.tar.gz
        # Note: They use tar.gz for all platforms
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_{os_capitalized}_{arch}.tar.gz"
    
    xǁBaoVariantǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBaoVariantǁget_download_url__mutmut_1': xǁBaoVariantǁget_download_url__mutmut_1, 
        'xǁBaoVariantǁget_download_url__mutmut_2': xǁBaoVariantǁget_download_url__mutmut_2, 
        'xǁBaoVariantǁget_download_url__mutmut_3': xǁBaoVariantǁget_download_url__mutmut_3, 
        'xǁBaoVariantǁget_download_url__mutmut_4': xǁBaoVariantǁget_download_url__mutmut_4, 
        'xǁBaoVariantǁget_download_url__mutmut_5': xǁBaoVariantǁget_download_url__mutmut_5, 
        'xǁBaoVariantǁget_download_url__mutmut_6': xǁBaoVariantǁget_download_url__mutmut_6, 
        'xǁBaoVariantǁget_download_url__mutmut_7': xǁBaoVariantǁget_download_url__mutmut_7, 
        'xǁBaoVariantǁget_download_url__mutmut_8': xǁBaoVariantǁget_download_url__mutmut_8
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBaoVariantǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁBaoVariantǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁBaoVariantǁget_download_url__mutmut_orig)
    xǁBaoVariantǁget_download_url__mutmut_orig.__name__ = 'xǁBaoVariantǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """Get checksum URL for OpenBao version."""
        # OpenBao provides SHA256SUMS file
        return f"https://github.com/openbao/openbao/releases/download/v{version}/bao_{version}_SHA256SUMS"


__all__ = [
    "BaoVariant",
]

# 🧰🌍🔚
