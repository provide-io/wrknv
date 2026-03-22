#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""OpenTofu Tool Manager for wrknv
==================================
Manages OpenTofu versions for development environment."""

from __future__ import annotations

import asyncio
import re
from typing import TYPE_CHECKING

from provide.foundation.logger import get_logger

from wrknv.managers.base import ToolManagerError
from wrknv.managers.github import GitHubReleasesClient
from wrknv.managers.tf.base import TfManager

if TYPE_CHECKING:
    from wrknv.config import WorkenvConfig

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


class TofuTfVariant(TfManager):
    """OpenTofu Tf variant - manages OpenTofu versions using GitHub releases API with wrknv's directory structure."""

    def xǁTofuTfVariantǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = None

    def xǁTofuTfVariantǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)
        self._github_client: GitHubReleasesClient | None = None

    def xǁTofuTfVariantǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        self._github_client: GitHubReleasesClient | None = ""
    
    xǁTofuTfVariantǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁ__init____mutmut_1': xǁTofuTfVariantǁ__init____mutmut_1, 
        'xǁTofuTfVariantǁ__init____mutmut_2': xǁTofuTfVariantǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTofuTfVariantǁ__init____mutmut_orig)
    xǁTofuTfVariantǁ__init____mutmut_orig.__name__ = 'xǁTofuTfVariantǁ__init__'

    @property
    def github_client(self) -> GitHubReleasesClient:
        """Get or create GitHub client for OpenTofu repository."""
        if self._github_client is None:
            self._github_client = GitHubReleasesClient("opentofu/opentofu")
        return self._github_client

    @property
    def tool_name(self) -> str:
        return "tofu"

    @property
    def executable_name(self) -> str:
        return "tofu"

    @property
    def tool_prefix(self) -> str:
        return "opentofu"

    def xǁTofuTfVariantǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug(None)

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("XXFetching OpenTofu versions from GitHubXX")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("fetching opentofu versions from github")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("FETCHING OPENTOFU VERSIONS FROM GITHUB")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = None

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting(None, False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", None)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting(False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", )

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("XXinclude_prereleasesXX", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("INCLUDE_PRERELEASES", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", True)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = None

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(None)

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=None))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(None)
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuTfVariantǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            logger.debug("Fetching OpenTofu versions from GitHub")

            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Use GitHub client to fetch versions
            versions = asyncio.run(self.github_client.get_versions(include_prereleases=include_prereleases))

            logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁTofuTfVariantǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁget_available_versions__mutmut_1': xǁTofuTfVariantǁget_available_versions__mutmut_1, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_2': xǁTofuTfVariantǁget_available_versions__mutmut_2, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_3': xǁTofuTfVariantǁget_available_versions__mutmut_3, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_4': xǁTofuTfVariantǁget_available_versions__mutmut_4, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_5': xǁTofuTfVariantǁget_available_versions__mutmut_5, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_6': xǁTofuTfVariantǁget_available_versions__mutmut_6, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_7': xǁTofuTfVariantǁget_available_versions__mutmut_7, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_8': xǁTofuTfVariantǁget_available_versions__mutmut_8, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_9': xǁTofuTfVariantǁget_available_versions__mutmut_9, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_10': xǁTofuTfVariantǁget_available_versions__mutmut_10, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_11': xǁTofuTfVariantǁget_available_versions__mutmut_11, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_12': xǁTofuTfVariantǁget_available_versions__mutmut_12, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_13': xǁTofuTfVariantǁget_available_versions__mutmut_13, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_14': xǁTofuTfVariantǁget_available_versions__mutmut_14, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_15': xǁTofuTfVariantǁget_available_versions__mutmut_15, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_16': xǁTofuTfVariantǁget_available_versions__mutmut_16, 
        'xǁTofuTfVariantǁget_available_versions__mutmut_17': xǁTofuTfVariantǁget_available_versions__mutmut_17
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁTofuTfVariantǁget_available_versions__mutmut_orig)
    xǁTofuTfVariantǁget_available_versions__mutmut_orig.__name__ = 'xǁTofuTfVariantǁget_available_versions'

    def xǁTofuTfVariantǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuTfVariantǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"
    
    xǁTofuTfVariantǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁget_download_url__mutmut_1': xǁTofuTfVariantǁget_download_url__mutmut_1, 
        'xǁTofuTfVariantǁget_download_url__mutmut_2': xǁTofuTfVariantǁget_download_url__mutmut_2, 
        'xǁTofuTfVariantǁget_download_url__mutmut_3': xǁTofuTfVariantǁget_download_url__mutmut_3, 
        'xǁTofuTfVariantǁget_download_url__mutmut_4': xǁTofuTfVariantǁget_download_url__mutmut_4, 
        'xǁTofuTfVariantǁget_download_url__mutmut_5': xǁTofuTfVariantǁget_download_url__mutmut_5, 
        'xǁTofuTfVariantǁget_download_url__mutmut_6': xǁTofuTfVariantǁget_download_url__mutmut_6, 
        'xǁTofuTfVariantǁget_download_url__mutmut_7': xǁTofuTfVariantǁget_download_url__mutmut_7
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁTofuTfVariantǁget_download_url__mutmut_orig)
    xǁTofuTfVariantǁget_download_url__mutmut_orig.__name__ = 'xǁTofuTfVariantǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """Get checksum URL for OpenTofu version."""
        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_SHA256SUMS"

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(None)
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return True

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = None

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
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
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=None,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=None,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=None,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(None), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "XX-versionXX"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-VERSION"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=False,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=False,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=11,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode != 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 1:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = None
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(None)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(None, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, None):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, ):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(None)
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return False
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_31(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(None)
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_32(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(None)

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_33(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return True

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_34(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(None)
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuTfVariantǁverify_installation__mutmut_35(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"OpenTofu {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in OpenTofu output: {result.stdout}")
            else:
                logger.error(f"OpenTofu version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify OpenTofu installation: {e}")
            return True
    
    xǁTofuTfVariantǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁverify_installation__mutmut_1': xǁTofuTfVariantǁverify_installation__mutmut_1, 
        'xǁTofuTfVariantǁverify_installation__mutmut_2': xǁTofuTfVariantǁverify_installation__mutmut_2, 
        'xǁTofuTfVariantǁverify_installation__mutmut_3': xǁTofuTfVariantǁverify_installation__mutmut_3, 
        'xǁTofuTfVariantǁverify_installation__mutmut_4': xǁTofuTfVariantǁverify_installation__mutmut_4, 
        'xǁTofuTfVariantǁverify_installation__mutmut_5': xǁTofuTfVariantǁverify_installation__mutmut_5, 
        'xǁTofuTfVariantǁverify_installation__mutmut_6': xǁTofuTfVariantǁverify_installation__mutmut_6, 
        'xǁTofuTfVariantǁverify_installation__mutmut_7': xǁTofuTfVariantǁverify_installation__mutmut_7, 
        'xǁTofuTfVariantǁverify_installation__mutmut_8': xǁTofuTfVariantǁverify_installation__mutmut_8, 
        'xǁTofuTfVariantǁverify_installation__mutmut_9': xǁTofuTfVariantǁverify_installation__mutmut_9, 
        'xǁTofuTfVariantǁverify_installation__mutmut_10': xǁTofuTfVariantǁverify_installation__mutmut_10, 
        'xǁTofuTfVariantǁverify_installation__mutmut_11': xǁTofuTfVariantǁverify_installation__mutmut_11, 
        'xǁTofuTfVariantǁverify_installation__mutmut_12': xǁTofuTfVariantǁverify_installation__mutmut_12, 
        'xǁTofuTfVariantǁverify_installation__mutmut_13': xǁTofuTfVariantǁverify_installation__mutmut_13, 
        'xǁTofuTfVariantǁverify_installation__mutmut_14': xǁTofuTfVariantǁverify_installation__mutmut_14, 
        'xǁTofuTfVariantǁverify_installation__mutmut_15': xǁTofuTfVariantǁverify_installation__mutmut_15, 
        'xǁTofuTfVariantǁverify_installation__mutmut_16': xǁTofuTfVariantǁverify_installation__mutmut_16, 
        'xǁTofuTfVariantǁverify_installation__mutmut_17': xǁTofuTfVariantǁverify_installation__mutmut_17, 
        'xǁTofuTfVariantǁverify_installation__mutmut_18': xǁTofuTfVariantǁverify_installation__mutmut_18, 
        'xǁTofuTfVariantǁverify_installation__mutmut_19': xǁTofuTfVariantǁverify_installation__mutmut_19, 
        'xǁTofuTfVariantǁverify_installation__mutmut_20': xǁTofuTfVariantǁverify_installation__mutmut_20, 
        'xǁTofuTfVariantǁverify_installation__mutmut_21': xǁTofuTfVariantǁverify_installation__mutmut_21, 
        'xǁTofuTfVariantǁverify_installation__mutmut_22': xǁTofuTfVariantǁverify_installation__mutmut_22, 
        'xǁTofuTfVariantǁverify_installation__mutmut_23': xǁTofuTfVariantǁverify_installation__mutmut_23, 
        'xǁTofuTfVariantǁverify_installation__mutmut_24': xǁTofuTfVariantǁverify_installation__mutmut_24, 
        'xǁTofuTfVariantǁverify_installation__mutmut_25': xǁTofuTfVariantǁverify_installation__mutmut_25, 
        'xǁTofuTfVariantǁverify_installation__mutmut_26': xǁTofuTfVariantǁverify_installation__mutmut_26, 
        'xǁTofuTfVariantǁverify_installation__mutmut_27': xǁTofuTfVariantǁverify_installation__mutmut_27, 
        'xǁTofuTfVariantǁverify_installation__mutmut_28': xǁTofuTfVariantǁverify_installation__mutmut_28, 
        'xǁTofuTfVariantǁverify_installation__mutmut_29': xǁTofuTfVariantǁverify_installation__mutmut_29, 
        'xǁTofuTfVariantǁverify_installation__mutmut_30': xǁTofuTfVariantǁverify_installation__mutmut_30, 
        'xǁTofuTfVariantǁverify_installation__mutmut_31': xǁTofuTfVariantǁverify_installation__mutmut_31, 
        'xǁTofuTfVariantǁverify_installation__mutmut_32': xǁTofuTfVariantǁverify_installation__mutmut_32, 
        'xǁTofuTfVariantǁverify_installation__mutmut_33': xǁTofuTfVariantǁverify_installation__mutmut_33, 
        'xǁTofuTfVariantǁverify_installation__mutmut_34': xǁTofuTfVariantǁverify_installation__mutmut_34, 
        'xǁTofuTfVariantǁverify_installation__mutmut_35': xǁTofuTfVariantǁverify_installation__mutmut_35
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁTofuTfVariantǁverify_installation__mutmut_orig)
    xǁTofuTfVariantǁverify_installation__mutmut_orig.__name__ = 'xǁTofuTfVariantǁverify_installation'

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_orig(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_1(self) -> dict:
        """Get compatibility information for development tools."""
        version = None
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_2(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_3(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"XXstatusXX": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_4(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"STATUS": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_5(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "XXnot_installedXX"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_6(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "NOT_INSTALLED"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_7(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = None

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_8(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "XXstatusXX": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_9(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "STATUS": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_10(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "XXcompatibleXX",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_11(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "COMPATIBLE",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_12(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "XXversionXX": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_13(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "VERSION": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_14(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "XXharnessXX": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_15(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "HARNESS": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_16(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "XXgo.ctyXX": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_17(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "GO.CTY": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_18(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(None),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_19(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "XXgo.wireXX": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_20(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "GO.WIRE": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_21(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(None),
                "conformance": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_22(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "XXconformanceXX": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_23(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "CONFORMANCE": self._check_conformance_compatibility(version),
            },
        }

        return compatibility

    def xǁTofuTfVariantǁget_harness_compatibility__mutmut_24(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_cty_compatibility(version),
                "go.wire": self._check_wire_compatibility(version),
                "conformance": self._check_conformance_compatibility(None),
            },
        }

        return compatibility
    
    xǁTofuTfVariantǁget_harness_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁget_harness_compatibility__mutmut_1': xǁTofuTfVariantǁget_harness_compatibility__mutmut_1, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_2': xǁTofuTfVariantǁget_harness_compatibility__mutmut_2, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_3': xǁTofuTfVariantǁget_harness_compatibility__mutmut_3, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_4': xǁTofuTfVariantǁget_harness_compatibility__mutmut_4, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_5': xǁTofuTfVariantǁget_harness_compatibility__mutmut_5, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_6': xǁTofuTfVariantǁget_harness_compatibility__mutmut_6, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_7': xǁTofuTfVariantǁget_harness_compatibility__mutmut_7, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_8': xǁTofuTfVariantǁget_harness_compatibility__mutmut_8, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_9': xǁTofuTfVariantǁget_harness_compatibility__mutmut_9, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_10': xǁTofuTfVariantǁget_harness_compatibility__mutmut_10, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_11': xǁTofuTfVariantǁget_harness_compatibility__mutmut_11, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_12': xǁTofuTfVariantǁget_harness_compatibility__mutmut_12, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_13': xǁTofuTfVariantǁget_harness_compatibility__mutmut_13, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_14': xǁTofuTfVariantǁget_harness_compatibility__mutmut_14, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_15': xǁTofuTfVariantǁget_harness_compatibility__mutmut_15, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_16': xǁTofuTfVariantǁget_harness_compatibility__mutmut_16, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_17': xǁTofuTfVariantǁget_harness_compatibility__mutmut_17, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_18': xǁTofuTfVariantǁget_harness_compatibility__mutmut_18, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_19': xǁTofuTfVariantǁget_harness_compatibility__mutmut_19, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_20': xǁTofuTfVariantǁget_harness_compatibility__mutmut_20, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_21': xǁTofuTfVariantǁget_harness_compatibility__mutmut_21, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_22': xǁTofuTfVariantǁget_harness_compatibility__mutmut_22, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_23': xǁTofuTfVariantǁget_harness_compatibility__mutmut_23, 
        'xǁTofuTfVariantǁget_harness_compatibility__mutmut_24': xǁTofuTfVariantǁget_harness_compatibility__mutmut_24
    }
    
    def get_harness_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁget_harness_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁget_harness_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_harness_compatibility.__signature__ = _mutmut_signature(xǁTofuTfVariantǁget_harness_compatibility__mutmut_orig)
    xǁTofuTfVariantǁget_harness_compatibility__mutmut_orig.__name__ = 'xǁTofuTfVariantǁget_harness_compatibility'

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "XXcompatibleXX": True,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "COMPATIBLE": True,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": False,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "XXnotesXX": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "NOTES": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "XXCTY testing compatible with all OpenTofu versionsXX",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "cty testing compatible with all opentofu versions",
        }

    def xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "CTY TESTING COMPATIBLE WITH ALL OPENTOFU VERSIONS",
        }
    
    xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_1': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_1, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_2': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_2, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_3': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_3, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_4': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_4, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_5': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_5, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_6': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_6, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_7': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_7, 
        'xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_8': xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_8
    }
    
    def _check_cty_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_cty_compatibility.__signature__ = _mutmut_signature(xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_orig)
    xǁTofuTfVariantǁ_check_cty_compatibility__mutmut_orig.__name__ = 'xǁTofuTfVariantǁ_check_cty_compatibility'

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = None

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(None)

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = "XX.XX".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(None)[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split("XX.XX")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:3])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = None
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(None, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, None)
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, )
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split(None))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_13(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("XX.XX"))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_14(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = None
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_15(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 and (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_16(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major >= 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_17(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 2 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_18(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 or minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_19(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major != 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_20(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 2 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_21(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor > 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_22(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 7)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_23(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_24(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = True

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_25(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_26(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_27(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_28(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except (ValueError, TypeError):
            is_compatible = False

        return {
            "compatible": is_compatible,
            "NOTES": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }
    
    xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_1': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_1, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_2': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_2, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_3': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_3, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_4': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_4, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_5': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_5, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_6': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_6, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_7': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_7, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_8': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_8, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_9': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_9, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_10': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_10, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_11': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_11, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_12': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_12, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_13': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_13, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_14': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_14, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_15': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_15, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_16': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_16, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_17': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_17, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_18': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_18, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_19': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_19, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_20': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_20, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_21': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_21, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_22': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_22, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_23': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_23, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_24': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_24, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_25': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_25, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_26': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_26, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_27': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_27, 
        'xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_28': xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_28
    }
    
    def _check_wire_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_wire_compatibility.__signature__ = _mutmut_signature(xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_orig)
    xǁTofuTfVariantǁ_check_wire_compatibility__mutmut_orig.__name__ = 'xǁTofuTfVariantǁ_check_wire_compatibility'

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "XXcompatibleXX": True,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "COMPATIBLE": True,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": False,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "XXnotesXX": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "NOTES": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "XXConformance testing supports all OpenTofu versionsXX",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "conformance testing supports all opentofu versions",
        }

    def xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "CONFORMANCE TESTING SUPPORTS ALL OPENTOFU VERSIONS",
        }
    
    xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_1': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_1, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_2': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_2, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_3': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_3, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_4': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_4, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_5': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_5, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_6': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_6, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_7': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_7, 
        'xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_8': xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_8
    }
    
    def _check_conformance_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_conformance_compatibility.__signature__ = _mutmut_signature(xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_orig)
    xǁTofuTfVariantǁ_check_conformance_compatibility__mutmut_orig.__name__ = 'xǁTofuTfVariantǁ_check_conformance_compatibility'


# 🧰🌍🔚
