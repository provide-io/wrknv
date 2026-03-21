# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#
# wrknv/workenv/managers/tofu.py
#
"""
OpenTofu Tool Manager for wrknv
==================================
Manages OpenTofu versions for development environment.
"""

import re

from provide.foundation import logger
from provide.foundation.process import run as process_run
import semver

from .tf_base import TfVersionsManager, ToolManagerError
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


class TofuManager(TfVersionsManager):
    """Manages OpenTofu versions using GitHub releases API with wrknv's directory structure."""

    @property
    def tool_name(self) -> str:
        return "tofu"

    @property
    def executable_name(self) -> str:
        return "tofu"

    @property
    def tool_prefix(self) -> str:
        return "opentofu"

    def xǁTofuManagerǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = None
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "XXhttps://api.github.com/repos/opentofu/opentofu/releasesXX"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "HTTPS://API.GITHUB.COM/REPOS/OPENTOFU/OPENTOFU/RELEASES"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = None

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(None)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = None
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = None
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get(None, "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", None)
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", )
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("XXtag_nameXX", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("TAG_NAME", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "XXXX")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith(None):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("XXvXX"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("V"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_18(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = None  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_19(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[2:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_20(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) or not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_21(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get(None, False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_22(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", None) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_23(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get(False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_24(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", ) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_25(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("XXprereleaseXX", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_26(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("PRERELEASE", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_27(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_28(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_29(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        None, False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_30(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", None
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_31(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_32(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_33(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "XXinclude_prereleasesXX", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_34(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "INCLUDE_PRERELEASES", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_35(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", True
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_36(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        break

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_37(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(None)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_38(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=None, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_39(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=None)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_40(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_41(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, )

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_42(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=False)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_43(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(None)
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch OpenTofu versions: {e}") from e

    def xǁTofuManagerǁget_available_versions__mutmut_44(self) -> list[str]:
        """Get available OpenTofu versions from GitHub releases."""
        try:
            api_url = "https://api.github.com/repos/opentofu/opentofu/releases"
            data = self.fetch_json_secure(api_url)

            versions = []
            for release in data:
                tag_name = release.get("tag_name", "")
                if tag_name.startswith("v"):
                    version = tag_name[1:]  # Remove 'v' prefix

                    # Skip prereleases unless configured to include them
                    if release.get("prerelease", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} OpenTofu versions")
            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁTofuManagerǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁget_available_versions__mutmut_1': xǁTofuManagerǁget_available_versions__mutmut_1, 
        'xǁTofuManagerǁget_available_versions__mutmut_2': xǁTofuManagerǁget_available_versions__mutmut_2, 
        'xǁTofuManagerǁget_available_versions__mutmut_3': xǁTofuManagerǁget_available_versions__mutmut_3, 
        'xǁTofuManagerǁget_available_versions__mutmut_4': xǁTofuManagerǁget_available_versions__mutmut_4, 
        'xǁTofuManagerǁget_available_versions__mutmut_5': xǁTofuManagerǁget_available_versions__mutmut_5, 
        'xǁTofuManagerǁget_available_versions__mutmut_6': xǁTofuManagerǁget_available_versions__mutmut_6, 
        'xǁTofuManagerǁget_available_versions__mutmut_7': xǁTofuManagerǁget_available_versions__mutmut_7, 
        'xǁTofuManagerǁget_available_versions__mutmut_8': xǁTofuManagerǁget_available_versions__mutmut_8, 
        'xǁTofuManagerǁget_available_versions__mutmut_9': xǁTofuManagerǁget_available_versions__mutmut_9, 
        'xǁTofuManagerǁget_available_versions__mutmut_10': xǁTofuManagerǁget_available_versions__mutmut_10, 
        'xǁTofuManagerǁget_available_versions__mutmut_11': xǁTofuManagerǁget_available_versions__mutmut_11, 
        'xǁTofuManagerǁget_available_versions__mutmut_12': xǁTofuManagerǁget_available_versions__mutmut_12, 
        'xǁTofuManagerǁget_available_versions__mutmut_13': xǁTofuManagerǁget_available_versions__mutmut_13, 
        'xǁTofuManagerǁget_available_versions__mutmut_14': xǁTofuManagerǁget_available_versions__mutmut_14, 
        'xǁTofuManagerǁget_available_versions__mutmut_15': xǁTofuManagerǁget_available_versions__mutmut_15, 
        'xǁTofuManagerǁget_available_versions__mutmut_16': xǁTofuManagerǁget_available_versions__mutmut_16, 
        'xǁTofuManagerǁget_available_versions__mutmut_17': xǁTofuManagerǁget_available_versions__mutmut_17, 
        'xǁTofuManagerǁget_available_versions__mutmut_18': xǁTofuManagerǁget_available_versions__mutmut_18, 
        'xǁTofuManagerǁget_available_versions__mutmut_19': xǁTofuManagerǁget_available_versions__mutmut_19, 
        'xǁTofuManagerǁget_available_versions__mutmut_20': xǁTofuManagerǁget_available_versions__mutmut_20, 
        'xǁTofuManagerǁget_available_versions__mutmut_21': xǁTofuManagerǁget_available_versions__mutmut_21, 
        'xǁTofuManagerǁget_available_versions__mutmut_22': xǁTofuManagerǁget_available_versions__mutmut_22, 
        'xǁTofuManagerǁget_available_versions__mutmut_23': xǁTofuManagerǁget_available_versions__mutmut_23, 
        'xǁTofuManagerǁget_available_versions__mutmut_24': xǁTofuManagerǁget_available_versions__mutmut_24, 
        'xǁTofuManagerǁget_available_versions__mutmut_25': xǁTofuManagerǁget_available_versions__mutmut_25, 
        'xǁTofuManagerǁget_available_versions__mutmut_26': xǁTofuManagerǁget_available_versions__mutmut_26, 
        'xǁTofuManagerǁget_available_versions__mutmut_27': xǁTofuManagerǁget_available_versions__mutmut_27, 
        'xǁTofuManagerǁget_available_versions__mutmut_28': xǁTofuManagerǁget_available_versions__mutmut_28, 
        'xǁTofuManagerǁget_available_versions__mutmut_29': xǁTofuManagerǁget_available_versions__mutmut_29, 
        'xǁTofuManagerǁget_available_versions__mutmut_30': xǁTofuManagerǁget_available_versions__mutmut_30, 
        'xǁTofuManagerǁget_available_versions__mutmut_31': xǁTofuManagerǁget_available_versions__mutmut_31, 
        'xǁTofuManagerǁget_available_versions__mutmut_32': xǁTofuManagerǁget_available_versions__mutmut_32, 
        'xǁTofuManagerǁget_available_versions__mutmut_33': xǁTofuManagerǁget_available_versions__mutmut_33, 
        'xǁTofuManagerǁget_available_versions__mutmut_34': xǁTofuManagerǁget_available_versions__mutmut_34, 
        'xǁTofuManagerǁget_available_versions__mutmut_35': xǁTofuManagerǁget_available_versions__mutmut_35, 
        'xǁTofuManagerǁget_available_versions__mutmut_36': xǁTofuManagerǁget_available_versions__mutmut_36, 
        'xǁTofuManagerǁget_available_versions__mutmut_37': xǁTofuManagerǁget_available_versions__mutmut_37, 
        'xǁTofuManagerǁget_available_versions__mutmut_38': xǁTofuManagerǁget_available_versions__mutmut_38, 
        'xǁTofuManagerǁget_available_versions__mutmut_39': xǁTofuManagerǁget_available_versions__mutmut_39, 
        'xǁTofuManagerǁget_available_versions__mutmut_40': xǁTofuManagerǁget_available_versions__mutmut_40, 
        'xǁTofuManagerǁget_available_versions__mutmut_41': xǁTofuManagerǁget_available_versions__mutmut_41, 
        'xǁTofuManagerǁget_available_versions__mutmut_42': xǁTofuManagerǁget_available_versions__mutmut_42, 
        'xǁTofuManagerǁget_available_versions__mutmut_43': xǁTofuManagerǁget_available_versions__mutmut_43, 
        'xǁTofuManagerǁget_available_versions__mutmut_44': xǁTofuManagerǁget_available_versions__mutmut_44
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁTofuManagerǁget_available_versions__mutmut_orig)
    xǁTofuManagerǁget_available_versions__mutmut_orig.__name__ = 'xǁTofuManagerǁget_available_versions'

    def xǁTofuManagerǁ_version_sort_key__mutmut_orig(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_1(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_2(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_3(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_4(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_5(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_6(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_7(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_8(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_9(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_10(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_11(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_12(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_13(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_14(self, version: str) -> tuple[int, ...]:
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

    def xǁTofuManagerǁ_version_sort_key__mutmut_15(self, version: str) -> tuple[int, ...]:
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
    
    xǁTofuManagerǁ_version_sort_key__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁ_version_sort_key__mutmut_1': xǁTofuManagerǁ_version_sort_key__mutmut_1, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_2': xǁTofuManagerǁ_version_sort_key__mutmut_2, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_3': xǁTofuManagerǁ_version_sort_key__mutmut_3, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_4': xǁTofuManagerǁ_version_sort_key__mutmut_4, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_5': xǁTofuManagerǁ_version_sort_key__mutmut_5, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_6': xǁTofuManagerǁ_version_sort_key__mutmut_6, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_7': xǁTofuManagerǁ_version_sort_key__mutmut_7, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_8': xǁTofuManagerǁ_version_sort_key__mutmut_8, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_9': xǁTofuManagerǁ_version_sort_key__mutmut_9, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_10': xǁTofuManagerǁ_version_sort_key__mutmut_10, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_11': xǁTofuManagerǁ_version_sort_key__mutmut_11, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_12': xǁTofuManagerǁ_version_sort_key__mutmut_12, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_13': xǁTofuManagerǁ_version_sort_key__mutmut_13, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_14': xǁTofuManagerǁ_version_sort_key__mutmut_14, 
        'xǁTofuManagerǁ_version_sort_key__mutmut_15': xǁTofuManagerǁ_version_sort_key__mutmut_15
    }
    
    def _version_sort_key(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁ_version_sort_key__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁ_version_sort_key__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _version_sort_key.__signature__ = _mutmut_signature(xǁTofuManagerǁ_version_sort_key__mutmut_orig)
    xǁTofuManagerǁ_version_sort_key__mutmut_orig.__name__ = 'xǁTofuManagerǁ_version_sort_key'

    def xǁTofuManagerǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"

    def xǁTofuManagerǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for OpenTofu version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_{os_name}_{arch}.zip"
    
    xǁTofuManagerǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁget_download_url__mutmut_1': xǁTofuManagerǁget_download_url__mutmut_1, 
        'xǁTofuManagerǁget_download_url__mutmut_2': xǁTofuManagerǁget_download_url__mutmut_2, 
        'xǁTofuManagerǁget_download_url__mutmut_3': xǁTofuManagerǁget_download_url__mutmut_3, 
        'xǁTofuManagerǁget_download_url__mutmut_4': xǁTofuManagerǁget_download_url__mutmut_4, 
        'xǁTofuManagerǁget_download_url__mutmut_5': xǁTofuManagerǁget_download_url__mutmut_5, 
        'xǁTofuManagerǁget_download_url__mutmut_6': xǁTofuManagerǁget_download_url__mutmut_6, 
        'xǁTofuManagerǁget_download_url__mutmut_7': xǁTofuManagerǁget_download_url__mutmut_7
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁTofuManagerǁget_download_url__mutmut_orig)
    xǁTofuManagerǁget_download_url__mutmut_orig.__name__ = 'xǁTofuManagerǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """Get checksum URL for OpenTofu version."""
        return f"https://github.com/opentofu/opentofu/releases/download/v{version}/tofu_{version}_SHA256SUMS"

    # _install_from_archive is inherited from TfVersionsManager

    def xǁTofuManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(None)
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return True

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = None

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                None,
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=None,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=None,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=None,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=None,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(None), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "XX-versionXX"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-VERSION"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=False,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=False,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=11.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=True,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode != 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 1:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = None
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(None)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(None, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, None):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_31(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, ):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_32(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_33(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_34(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_35(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_36(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_37(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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

    def xǁTofuManagerǁverify_installation__mutmut_38(self, version: str) -> bool:
        """Verify that OpenTofu installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"OpenTofu binary not found at {binary_path}")
            return False

        try:
            result = process_run(
                [str(binary_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10.0,
                check=False,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"OpenTofu v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
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
    
    xǁTofuManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁverify_installation__mutmut_1': xǁTofuManagerǁverify_installation__mutmut_1, 
        'xǁTofuManagerǁverify_installation__mutmut_2': xǁTofuManagerǁverify_installation__mutmut_2, 
        'xǁTofuManagerǁverify_installation__mutmut_3': xǁTofuManagerǁverify_installation__mutmut_3, 
        'xǁTofuManagerǁverify_installation__mutmut_4': xǁTofuManagerǁverify_installation__mutmut_4, 
        'xǁTofuManagerǁverify_installation__mutmut_5': xǁTofuManagerǁverify_installation__mutmut_5, 
        'xǁTofuManagerǁverify_installation__mutmut_6': xǁTofuManagerǁverify_installation__mutmut_6, 
        'xǁTofuManagerǁverify_installation__mutmut_7': xǁTofuManagerǁverify_installation__mutmut_7, 
        'xǁTofuManagerǁverify_installation__mutmut_8': xǁTofuManagerǁverify_installation__mutmut_8, 
        'xǁTofuManagerǁverify_installation__mutmut_9': xǁTofuManagerǁverify_installation__mutmut_9, 
        'xǁTofuManagerǁverify_installation__mutmut_10': xǁTofuManagerǁverify_installation__mutmut_10, 
        'xǁTofuManagerǁverify_installation__mutmut_11': xǁTofuManagerǁverify_installation__mutmut_11, 
        'xǁTofuManagerǁverify_installation__mutmut_12': xǁTofuManagerǁverify_installation__mutmut_12, 
        'xǁTofuManagerǁverify_installation__mutmut_13': xǁTofuManagerǁverify_installation__mutmut_13, 
        'xǁTofuManagerǁverify_installation__mutmut_14': xǁTofuManagerǁverify_installation__mutmut_14, 
        'xǁTofuManagerǁverify_installation__mutmut_15': xǁTofuManagerǁverify_installation__mutmut_15, 
        'xǁTofuManagerǁverify_installation__mutmut_16': xǁTofuManagerǁverify_installation__mutmut_16, 
        'xǁTofuManagerǁverify_installation__mutmut_17': xǁTofuManagerǁverify_installation__mutmut_17, 
        'xǁTofuManagerǁverify_installation__mutmut_18': xǁTofuManagerǁverify_installation__mutmut_18, 
        'xǁTofuManagerǁverify_installation__mutmut_19': xǁTofuManagerǁverify_installation__mutmut_19, 
        'xǁTofuManagerǁverify_installation__mutmut_20': xǁTofuManagerǁverify_installation__mutmut_20, 
        'xǁTofuManagerǁverify_installation__mutmut_21': xǁTofuManagerǁverify_installation__mutmut_21, 
        'xǁTofuManagerǁverify_installation__mutmut_22': xǁTofuManagerǁverify_installation__mutmut_22, 
        'xǁTofuManagerǁverify_installation__mutmut_23': xǁTofuManagerǁverify_installation__mutmut_23, 
        'xǁTofuManagerǁverify_installation__mutmut_24': xǁTofuManagerǁverify_installation__mutmut_24, 
        'xǁTofuManagerǁverify_installation__mutmut_25': xǁTofuManagerǁverify_installation__mutmut_25, 
        'xǁTofuManagerǁverify_installation__mutmut_26': xǁTofuManagerǁverify_installation__mutmut_26, 
        'xǁTofuManagerǁverify_installation__mutmut_27': xǁTofuManagerǁverify_installation__mutmut_27, 
        'xǁTofuManagerǁverify_installation__mutmut_28': xǁTofuManagerǁverify_installation__mutmut_28, 
        'xǁTofuManagerǁverify_installation__mutmut_29': xǁTofuManagerǁverify_installation__mutmut_29, 
        'xǁTofuManagerǁverify_installation__mutmut_30': xǁTofuManagerǁverify_installation__mutmut_30, 
        'xǁTofuManagerǁverify_installation__mutmut_31': xǁTofuManagerǁverify_installation__mutmut_31, 
        'xǁTofuManagerǁverify_installation__mutmut_32': xǁTofuManagerǁverify_installation__mutmut_32, 
        'xǁTofuManagerǁverify_installation__mutmut_33': xǁTofuManagerǁverify_installation__mutmut_33, 
        'xǁTofuManagerǁverify_installation__mutmut_34': xǁTofuManagerǁverify_installation__mutmut_34, 
        'xǁTofuManagerǁverify_installation__mutmut_35': xǁTofuManagerǁverify_installation__mutmut_35, 
        'xǁTofuManagerǁverify_installation__mutmut_36': xǁTofuManagerǁverify_installation__mutmut_36, 
        'xǁTofuManagerǁverify_installation__mutmut_37': xǁTofuManagerǁverify_installation__mutmut_37, 
        'xǁTofuManagerǁverify_installation__mutmut_38': xǁTofuManagerǁverify_installation__mutmut_38
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁTofuManagerǁverify_installation__mutmut_orig)
    xǁTofuManagerǁverify_installation__mutmut_orig.__name__ = 'xǁTofuManagerǁverify_installation'

    def xǁTofuManagerǁget_harness_compatibility__mutmut_orig(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_1(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_2(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_3(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_4(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_5(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_6(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_7(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = None

        return compatibility

    def xǁTofuManagerǁget_harness_compatibility__mutmut_8(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_9(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_10(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_11(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_12(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_13(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_14(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_15(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_16(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_17(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_18(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_19(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_20(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_21(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_22(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_23(self) -> dict:
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

    def xǁTofuManagerǁget_harness_compatibility__mutmut_24(self) -> dict:
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
    
    xǁTofuManagerǁget_harness_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁget_harness_compatibility__mutmut_1': xǁTofuManagerǁget_harness_compatibility__mutmut_1, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_2': xǁTofuManagerǁget_harness_compatibility__mutmut_2, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_3': xǁTofuManagerǁget_harness_compatibility__mutmut_3, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_4': xǁTofuManagerǁget_harness_compatibility__mutmut_4, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_5': xǁTofuManagerǁget_harness_compatibility__mutmut_5, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_6': xǁTofuManagerǁget_harness_compatibility__mutmut_6, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_7': xǁTofuManagerǁget_harness_compatibility__mutmut_7, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_8': xǁTofuManagerǁget_harness_compatibility__mutmut_8, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_9': xǁTofuManagerǁget_harness_compatibility__mutmut_9, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_10': xǁTofuManagerǁget_harness_compatibility__mutmut_10, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_11': xǁTofuManagerǁget_harness_compatibility__mutmut_11, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_12': xǁTofuManagerǁget_harness_compatibility__mutmut_12, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_13': xǁTofuManagerǁget_harness_compatibility__mutmut_13, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_14': xǁTofuManagerǁget_harness_compatibility__mutmut_14, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_15': xǁTofuManagerǁget_harness_compatibility__mutmut_15, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_16': xǁTofuManagerǁget_harness_compatibility__mutmut_16, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_17': xǁTofuManagerǁget_harness_compatibility__mutmut_17, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_18': xǁTofuManagerǁget_harness_compatibility__mutmut_18, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_19': xǁTofuManagerǁget_harness_compatibility__mutmut_19, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_20': xǁTofuManagerǁget_harness_compatibility__mutmut_20, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_21': xǁTofuManagerǁget_harness_compatibility__mutmut_21, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_22': xǁTofuManagerǁget_harness_compatibility__mutmut_22, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_23': xǁTofuManagerǁget_harness_compatibility__mutmut_23, 
        'xǁTofuManagerǁget_harness_compatibility__mutmut_24': xǁTofuManagerǁget_harness_compatibility__mutmut_24
    }
    
    def get_harness_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁget_harness_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁget_harness_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_harness_compatibility.__signature__ = _mutmut_signature(xǁTofuManagerǁget_harness_compatibility__mutmut_orig)
    xǁTofuManagerǁget_harness_compatibility__mutmut_orig.__name__ = 'xǁTofuManagerǁget_harness_compatibility'

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "XXcompatibleXX": True,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "COMPATIBLE": True,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": False,
            "notes": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "XXnotesXX": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "NOTES": "CTY testing compatible with all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "XXCTY testing compatible with all OpenTofu versionsXX",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "cty testing compatible with all opentofu versions",
        }

    def xǁTofuManagerǁ_check_cty_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        return {
            "compatible": True,
            "notes": "CTY TESTING COMPATIBLE WITH ALL OPENTOFU VERSIONS",
        }
    
    xǁTofuManagerǁ_check_cty_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁ_check_cty_compatibility__mutmut_1': xǁTofuManagerǁ_check_cty_compatibility__mutmut_1, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_2': xǁTofuManagerǁ_check_cty_compatibility__mutmut_2, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_3': xǁTofuManagerǁ_check_cty_compatibility__mutmut_3, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_4': xǁTofuManagerǁ_check_cty_compatibility__mutmut_4, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_5': xǁTofuManagerǁ_check_cty_compatibility__mutmut_5, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_6': xǁTofuManagerǁ_check_cty_compatibility__mutmut_6, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_7': xǁTofuManagerǁ_check_cty_compatibility__mutmut_7, 
        'xǁTofuManagerǁ_check_cty_compatibility__mutmut_8': xǁTofuManagerǁ_check_cty_compatibility__mutmut_8
    }
    
    def _check_cty_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁ_check_cty_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁ_check_cty_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_cty_compatibility.__signature__ = _mutmut_signature(xǁTofuManagerǁ_check_cty_compatibility__mutmut_orig)
    xǁTofuManagerǁ_check_cty_compatibility__mutmut_orig.__name__ = 'xǁTofuManagerǁ_check_cty_compatibility'

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = None

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(None)

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = "XX.XX".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(None)[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split("XX.XX")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:3])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = None
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(None, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, None)
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, )
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split(None))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_13(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("XX.XX"))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_14(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = None
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_15(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 and (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_16(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major >= 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_17(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 2 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_18(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 or minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_19(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major != 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_20(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 2 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_21(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor > 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_22(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 7)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_23(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_24(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = True

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_25(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_26(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_27(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }

    def xǁTofuManagerǁ_check_wire_compatibility__mutmut_28(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # OpenTofu 1.6+ is compatible with Terraform wire protocol
        major_minor = ".".join(version.split(".")[:2])

        try:
            major, minor = map(int, major_minor.split("."))
            is_compatible = major > 1 or (major == 1 and minor >= 6)
        except Exception:
            is_compatible = False

        return {
            "compatible": is_compatible,
            "NOTES": f"Wire protocol testing requires OpenTofu 1.6+ (current: {version})",
        }
    
    xǁTofuManagerǁ_check_wire_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁ_check_wire_compatibility__mutmut_1': xǁTofuManagerǁ_check_wire_compatibility__mutmut_1, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_2': xǁTofuManagerǁ_check_wire_compatibility__mutmut_2, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_3': xǁTofuManagerǁ_check_wire_compatibility__mutmut_3, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_4': xǁTofuManagerǁ_check_wire_compatibility__mutmut_4, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_5': xǁTofuManagerǁ_check_wire_compatibility__mutmut_5, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_6': xǁTofuManagerǁ_check_wire_compatibility__mutmut_6, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_7': xǁTofuManagerǁ_check_wire_compatibility__mutmut_7, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_8': xǁTofuManagerǁ_check_wire_compatibility__mutmut_8, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_9': xǁTofuManagerǁ_check_wire_compatibility__mutmut_9, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_10': xǁTofuManagerǁ_check_wire_compatibility__mutmut_10, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_11': xǁTofuManagerǁ_check_wire_compatibility__mutmut_11, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_12': xǁTofuManagerǁ_check_wire_compatibility__mutmut_12, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_13': xǁTofuManagerǁ_check_wire_compatibility__mutmut_13, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_14': xǁTofuManagerǁ_check_wire_compatibility__mutmut_14, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_15': xǁTofuManagerǁ_check_wire_compatibility__mutmut_15, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_16': xǁTofuManagerǁ_check_wire_compatibility__mutmut_16, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_17': xǁTofuManagerǁ_check_wire_compatibility__mutmut_17, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_18': xǁTofuManagerǁ_check_wire_compatibility__mutmut_18, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_19': xǁTofuManagerǁ_check_wire_compatibility__mutmut_19, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_20': xǁTofuManagerǁ_check_wire_compatibility__mutmut_20, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_21': xǁTofuManagerǁ_check_wire_compatibility__mutmut_21, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_22': xǁTofuManagerǁ_check_wire_compatibility__mutmut_22, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_23': xǁTofuManagerǁ_check_wire_compatibility__mutmut_23, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_24': xǁTofuManagerǁ_check_wire_compatibility__mutmut_24, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_25': xǁTofuManagerǁ_check_wire_compatibility__mutmut_25, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_26': xǁTofuManagerǁ_check_wire_compatibility__mutmut_26, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_27': xǁTofuManagerǁ_check_wire_compatibility__mutmut_27, 
        'xǁTofuManagerǁ_check_wire_compatibility__mutmut_28': xǁTofuManagerǁ_check_wire_compatibility__mutmut_28
    }
    
    def _check_wire_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁ_check_wire_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁ_check_wire_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_wire_compatibility.__signature__ = _mutmut_signature(xǁTofuManagerǁ_check_wire_compatibility__mutmut_orig)
    xǁTofuManagerǁ_check_wire_compatibility__mutmut_orig.__name__ = 'xǁTofuManagerǁ_check_wire_compatibility'

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "XXcompatibleXX": True,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "COMPATIBLE": True,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": False,
            "notes": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "XXnotesXX": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "NOTES": "Conformance testing supports all OpenTofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "XXConformance testing supports all OpenTofu versionsXX",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "conformance testing supports all opentofu versions",
        }

    def xǁTofuManagerǁ_check_conformance_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "CONFORMANCE TESTING SUPPORTS ALL OPENTOFU VERSIONS",
        }
    
    xǁTofuManagerǁ_check_conformance_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_1': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_1, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_2': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_2, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_3': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_3, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_4': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_4, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_5': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_5, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_6': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_6, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_7': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_7, 
        'xǁTofuManagerǁ_check_conformance_compatibility__mutmut_8': xǁTofuManagerǁ_check_conformance_compatibility__mutmut_8
    }
    
    def _check_conformance_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTofuManagerǁ_check_conformance_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁTofuManagerǁ_check_conformance_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_conformance_compatibility.__signature__ = _mutmut_signature(xǁTofuManagerǁ_check_conformance_compatibility__mutmut_orig)
    xǁTofuManagerǁ_check_conformance_compatibility__mutmut_orig.__name__ = 'xǁTofuManagerǁ_check_conformance_compatibility'


# 🍲🥄📄🪄
