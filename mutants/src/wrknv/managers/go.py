#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Go Tool Manager for wrknv
============================
Manages Go versions for development."""

from __future__ import annotations

import asyncio
import pathlib
import re

from provide.foundation import logger
from provide.foundation.transport import get

from .base import BaseToolManager, ToolManagerError
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


class GoManager(BaseToolManager):
    """Manages Go versions using official Go download API."""

    @property
    def tool_name(self) -> str:
        return "go"

    @property
    def executable_name(self) -> str:
        return "go"

    def xǁGoManagerǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = None

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "XXhttps://go.dev/dl/?mode=jsonXX"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "HTTPS://GO.DEV/DL/?MODE=JSON"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(None)

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = None
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(None)
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(None))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = None

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = None
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = None
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get(None, "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", None)
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", )
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("XXversionXX", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("VERSION", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "XXXX")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_18(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith(None):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_19(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("XXgoXX"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_20(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("GO"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_21(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = None  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_22(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[3:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_23(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) or not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_24(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_25(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get(None, True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_26(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", None) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_27(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get(True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_28(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", ) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_29(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("XXstableXX", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_30(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("STABLE", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_31(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", False) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_32(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_33(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        None, False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_34(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", None
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_35(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_36(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_37(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "XXinclude_prereleasesXX", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_38(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "INCLUDE_PRERELEASES", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_39(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", True
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_40(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        break

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_41(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(None)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_42(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(None)
            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Go versions: {e}") from e

    def xǁGoManagerǁget_available_versions__mutmut_43(self) -> list[str]:
        """Get available Go versions from official API."""
        try:
            api_url = "https://go.dev/dl/?mode=json"

            if logger.is_debug_enabled():
                logger.debug(f"Fetching Go versions from {api_url}")

            # Use foundation transport for unified HTTP handling
            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            for release in data:
                version = release.get("version", "")
                if version.startswith("go"):
                    version = version[2:]  # Remove 'go' prefix

                    # Skip unstable versions unless configured to include them
                    if not release.get("stable", True) and not self.config.get_setting(
                        "include_prereleases", False
                    ):
                        continue

                    versions.append(version)

            if logger.is_debug_enabled():
                logger.debug(f"Found {len(versions)} Go versions")
            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁGoManagerǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁget_available_versions__mutmut_1': xǁGoManagerǁget_available_versions__mutmut_1, 
        'xǁGoManagerǁget_available_versions__mutmut_2': xǁGoManagerǁget_available_versions__mutmut_2, 
        'xǁGoManagerǁget_available_versions__mutmut_3': xǁGoManagerǁget_available_versions__mutmut_3, 
        'xǁGoManagerǁget_available_versions__mutmut_4': xǁGoManagerǁget_available_versions__mutmut_4, 
        'xǁGoManagerǁget_available_versions__mutmut_5': xǁGoManagerǁget_available_versions__mutmut_5, 
        'xǁGoManagerǁget_available_versions__mutmut_6': xǁGoManagerǁget_available_versions__mutmut_6, 
        'xǁGoManagerǁget_available_versions__mutmut_7': xǁGoManagerǁget_available_versions__mutmut_7, 
        'xǁGoManagerǁget_available_versions__mutmut_8': xǁGoManagerǁget_available_versions__mutmut_8, 
        'xǁGoManagerǁget_available_versions__mutmut_9': xǁGoManagerǁget_available_versions__mutmut_9, 
        'xǁGoManagerǁget_available_versions__mutmut_10': xǁGoManagerǁget_available_versions__mutmut_10, 
        'xǁGoManagerǁget_available_versions__mutmut_11': xǁGoManagerǁget_available_versions__mutmut_11, 
        'xǁGoManagerǁget_available_versions__mutmut_12': xǁGoManagerǁget_available_versions__mutmut_12, 
        'xǁGoManagerǁget_available_versions__mutmut_13': xǁGoManagerǁget_available_versions__mutmut_13, 
        'xǁGoManagerǁget_available_versions__mutmut_14': xǁGoManagerǁget_available_versions__mutmut_14, 
        'xǁGoManagerǁget_available_versions__mutmut_15': xǁGoManagerǁget_available_versions__mutmut_15, 
        'xǁGoManagerǁget_available_versions__mutmut_16': xǁGoManagerǁget_available_versions__mutmut_16, 
        'xǁGoManagerǁget_available_versions__mutmut_17': xǁGoManagerǁget_available_versions__mutmut_17, 
        'xǁGoManagerǁget_available_versions__mutmut_18': xǁGoManagerǁget_available_versions__mutmut_18, 
        'xǁGoManagerǁget_available_versions__mutmut_19': xǁGoManagerǁget_available_versions__mutmut_19, 
        'xǁGoManagerǁget_available_versions__mutmut_20': xǁGoManagerǁget_available_versions__mutmut_20, 
        'xǁGoManagerǁget_available_versions__mutmut_21': xǁGoManagerǁget_available_versions__mutmut_21, 
        'xǁGoManagerǁget_available_versions__mutmut_22': xǁGoManagerǁget_available_versions__mutmut_22, 
        'xǁGoManagerǁget_available_versions__mutmut_23': xǁGoManagerǁget_available_versions__mutmut_23, 
        'xǁGoManagerǁget_available_versions__mutmut_24': xǁGoManagerǁget_available_versions__mutmut_24, 
        'xǁGoManagerǁget_available_versions__mutmut_25': xǁGoManagerǁget_available_versions__mutmut_25, 
        'xǁGoManagerǁget_available_versions__mutmut_26': xǁGoManagerǁget_available_versions__mutmut_26, 
        'xǁGoManagerǁget_available_versions__mutmut_27': xǁGoManagerǁget_available_versions__mutmut_27, 
        'xǁGoManagerǁget_available_versions__mutmut_28': xǁGoManagerǁget_available_versions__mutmut_28, 
        'xǁGoManagerǁget_available_versions__mutmut_29': xǁGoManagerǁget_available_versions__mutmut_29, 
        'xǁGoManagerǁget_available_versions__mutmut_30': xǁGoManagerǁget_available_versions__mutmut_30, 
        'xǁGoManagerǁget_available_versions__mutmut_31': xǁGoManagerǁget_available_versions__mutmut_31, 
        'xǁGoManagerǁget_available_versions__mutmut_32': xǁGoManagerǁget_available_versions__mutmut_32, 
        'xǁGoManagerǁget_available_versions__mutmut_33': xǁGoManagerǁget_available_versions__mutmut_33, 
        'xǁGoManagerǁget_available_versions__mutmut_34': xǁGoManagerǁget_available_versions__mutmut_34, 
        'xǁGoManagerǁget_available_versions__mutmut_35': xǁGoManagerǁget_available_versions__mutmut_35, 
        'xǁGoManagerǁget_available_versions__mutmut_36': xǁGoManagerǁget_available_versions__mutmut_36, 
        'xǁGoManagerǁget_available_versions__mutmut_37': xǁGoManagerǁget_available_versions__mutmut_37, 
        'xǁGoManagerǁget_available_versions__mutmut_38': xǁGoManagerǁget_available_versions__mutmut_38, 
        'xǁGoManagerǁget_available_versions__mutmut_39': xǁGoManagerǁget_available_versions__mutmut_39, 
        'xǁGoManagerǁget_available_versions__mutmut_40': xǁGoManagerǁget_available_versions__mutmut_40, 
        'xǁGoManagerǁget_available_versions__mutmut_41': xǁGoManagerǁget_available_versions__mutmut_41, 
        'xǁGoManagerǁget_available_versions__mutmut_42': xǁGoManagerǁget_available_versions__mutmut_42, 
        'xǁGoManagerǁget_available_versions__mutmut_43': xǁGoManagerǁget_available_versions__mutmut_43
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁGoManagerǁget_available_versions__mutmut_orig)
    xǁGoManagerǁget_available_versions__mutmut_orig.__name__ = 'xǁGoManagerǁget_available_versions'

    def xǁGoManagerǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_8(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = None

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_9(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting(None, "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_10(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", None)

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_11(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_12(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", )

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_13(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("XXgo_mirrorXX", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_14(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("GO_MIRROR", "https://go.dev/dl")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_15(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "XXhttps://go.dev/dlXX")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_16(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "HTTPS://GO.DEV/DL")

        return f"{mirror_url.rstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_17(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip(None)}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_18(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.lstrip('/')}/go{version}.{os_name}-{arch}.tar.gz"

    def xǁGoManagerǁget_download_url__mutmut_19(self, version: str) -> str:
        """Get download URL for Go version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("go_mirror", "https://go.dev/dl")

        return f"{mirror_url.rstrip('XX/XX')}/go{version}.{os_name}-{arch}.tar.gz"
    
    xǁGoManagerǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁget_download_url__mutmut_1': xǁGoManagerǁget_download_url__mutmut_1, 
        'xǁGoManagerǁget_download_url__mutmut_2': xǁGoManagerǁget_download_url__mutmut_2, 
        'xǁGoManagerǁget_download_url__mutmut_3': xǁGoManagerǁget_download_url__mutmut_3, 
        'xǁGoManagerǁget_download_url__mutmut_4': xǁGoManagerǁget_download_url__mutmut_4, 
        'xǁGoManagerǁget_download_url__mutmut_5': xǁGoManagerǁget_download_url__mutmut_5, 
        'xǁGoManagerǁget_download_url__mutmut_6': xǁGoManagerǁget_download_url__mutmut_6, 
        'xǁGoManagerǁget_download_url__mutmut_7': xǁGoManagerǁget_download_url__mutmut_7, 
        'xǁGoManagerǁget_download_url__mutmut_8': xǁGoManagerǁget_download_url__mutmut_8, 
        'xǁGoManagerǁget_download_url__mutmut_9': xǁGoManagerǁget_download_url__mutmut_9, 
        'xǁGoManagerǁget_download_url__mutmut_10': xǁGoManagerǁget_download_url__mutmut_10, 
        'xǁGoManagerǁget_download_url__mutmut_11': xǁGoManagerǁget_download_url__mutmut_11, 
        'xǁGoManagerǁget_download_url__mutmut_12': xǁGoManagerǁget_download_url__mutmut_12, 
        'xǁGoManagerǁget_download_url__mutmut_13': xǁGoManagerǁget_download_url__mutmut_13, 
        'xǁGoManagerǁget_download_url__mutmut_14': xǁGoManagerǁget_download_url__mutmut_14, 
        'xǁGoManagerǁget_download_url__mutmut_15': xǁGoManagerǁget_download_url__mutmut_15, 
        'xǁGoManagerǁget_download_url__mutmut_16': xǁGoManagerǁget_download_url__mutmut_16, 
        'xǁGoManagerǁget_download_url__mutmut_17': xǁGoManagerǁget_download_url__mutmut_17, 
        'xǁGoManagerǁget_download_url__mutmut_18': xǁGoManagerǁget_download_url__mutmut_18, 
        'xǁGoManagerǁget_download_url__mutmut_19': xǁGoManagerǁget_download_url__mutmut_19
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁGoManagerǁget_download_url__mutmut_orig)
    xǁGoManagerǁget_download_url__mutmut_orig.__name__ = 'xǁGoManagerǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """Go doesn't provide separate checksum files, checksums are in the main API."""
        return None

    def xǁGoManagerǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = None
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name * version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path * self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=None, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=None)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, )

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=False, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=False)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = None
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir * f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(None, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, None)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, )

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = None
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir * "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "XXgoXX"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "GO"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError(None)

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("XXGo directory not found in archiveXX")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("GO DIRECTORY NOT FOUND IN ARCHIVE")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(None, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, None)

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, )

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir * "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "XXgoXX")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "GO")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = None
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir * "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_36(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "XXbinXX"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_37(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "BIN"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_38(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=None)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_39(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=False)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_40(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = None
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_41(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" * "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_42(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" * "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_43(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir * "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_44(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "XXgoXX" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_45(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "GO" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_46(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "XXbinXX" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_47(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "BIN" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_48(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "XXgoXX"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_49(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "GO"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_50(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = None
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_51(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir * "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_52(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "XXgoXX"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_53(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "GO"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_54(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(None)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_55(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(None)
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_56(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError(None)

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_57(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("XXGo binary not found in extracted archiveXX")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_58(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_59(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("GO BINARY NOT FOUND IN EXTRACTED ARCHIVE")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_60(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_61(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_62(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_63(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(None, missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_64(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=None)

    def xǁGoManagerǁ_install_from_archive__mutmut_65(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(missing_ok=True)

    def xǁGoManagerǁ_install_from_archive__mutmut_66(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, )

    def xǁGoManagerǁ_install_from_archive__mutmut_67(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Go from downloaded tar.gz archive."""
        # Create version-specific directory
        version_dir = self.install_path / self.tool_name / version
        version_dir.mkdir(parents=True, exist_ok=True)

        # Extract tar.gz file
        extract_dir = self.cache_dir / f"go_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Go archive contains 'go' directory with bin/go inside
            go_root = extract_dir / "go"
            if not go_root.exists():
                raise ToolManagerError("Go directory not found in archive")

            # Move the entire Go installation to version directory
            from provide.foundation.file import safe_move, safe_rmtree

            safe_move(go_root, version_dir / "go")

            # Create a bin directory in version_dir for consistency
            bin_dir = version_dir / "bin"
            bin_dir.mkdir(exist_ok=True)

            # Create symlink to go binary
            go_binary = version_dir / "go" / "bin" / "go"
            if go_binary.exists():
                target_path = bin_dir / "go"
                target_path.symlink_to(go_binary)
                logger.info(f"Installed Go to: {version_dir}")
            else:
                raise ToolManagerError("Go binary not found in extracted archive")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Go {version} installation verification failed")

        finally:
            # Clean up extraction directory
            from provide.foundation.file import safe_rmtree

            safe_rmtree(extract_dir, missing_ok=False)
    
    xǁGoManagerǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁ_install_from_archive__mutmut_1': xǁGoManagerǁ_install_from_archive__mutmut_1, 
        'xǁGoManagerǁ_install_from_archive__mutmut_2': xǁGoManagerǁ_install_from_archive__mutmut_2, 
        'xǁGoManagerǁ_install_from_archive__mutmut_3': xǁGoManagerǁ_install_from_archive__mutmut_3, 
        'xǁGoManagerǁ_install_from_archive__mutmut_4': xǁGoManagerǁ_install_from_archive__mutmut_4, 
        'xǁGoManagerǁ_install_from_archive__mutmut_5': xǁGoManagerǁ_install_from_archive__mutmut_5, 
        'xǁGoManagerǁ_install_from_archive__mutmut_6': xǁGoManagerǁ_install_from_archive__mutmut_6, 
        'xǁGoManagerǁ_install_from_archive__mutmut_7': xǁGoManagerǁ_install_from_archive__mutmut_7, 
        'xǁGoManagerǁ_install_from_archive__mutmut_8': xǁGoManagerǁ_install_from_archive__mutmut_8, 
        'xǁGoManagerǁ_install_from_archive__mutmut_9': xǁGoManagerǁ_install_from_archive__mutmut_9, 
        'xǁGoManagerǁ_install_from_archive__mutmut_10': xǁGoManagerǁ_install_from_archive__mutmut_10, 
        'xǁGoManagerǁ_install_from_archive__mutmut_11': xǁGoManagerǁ_install_from_archive__mutmut_11, 
        'xǁGoManagerǁ_install_from_archive__mutmut_12': xǁGoManagerǁ_install_from_archive__mutmut_12, 
        'xǁGoManagerǁ_install_from_archive__mutmut_13': xǁGoManagerǁ_install_from_archive__mutmut_13, 
        'xǁGoManagerǁ_install_from_archive__mutmut_14': xǁGoManagerǁ_install_from_archive__mutmut_14, 
        'xǁGoManagerǁ_install_from_archive__mutmut_15': xǁGoManagerǁ_install_from_archive__mutmut_15, 
        'xǁGoManagerǁ_install_from_archive__mutmut_16': xǁGoManagerǁ_install_from_archive__mutmut_16, 
        'xǁGoManagerǁ_install_from_archive__mutmut_17': xǁGoManagerǁ_install_from_archive__mutmut_17, 
        'xǁGoManagerǁ_install_from_archive__mutmut_18': xǁGoManagerǁ_install_from_archive__mutmut_18, 
        'xǁGoManagerǁ_install_from_archive__mutmut_19': xǁGoManagerǁ_install_from_archive__mutmut_19, 
        'xǁGoManagerǁ_install_from_archive__mutmut_20': xǁGoManagerǁ_install_from_archive__mutmut_20, 
        'xǁGoManagerǁ_install_from_archive__mutmut_21': xǁGoManagerǁ_install_from_archive__mutmut_21, 
        'xǁGoManagerǁ_install_from_archive__mutmut_22': xǁGoManagerǁ_install_from_archive__mutmut_22, 
        'xǁGoManagerǁ_install_from_archive__mutmut_23': xǁGoManagerǁ_install_from_archive__mutmut_23, 
        'xǁGoManagerǁ_install_from_archive__mutmut_24': xǁGoManagerǁ_install_from_archive__mutmut_24, 
        'xǁGoManagerǁ_install_from_archive__mutmut_25': xǁGoManagerǁ_install_from_archive__mutmut_25, 
        'xǁGoManagerǁ_install_from_archive__mutmut_26': xǁGoManagerǁ_install_from_archive__mutmut_26, 
        'xǁGoManagerǁ_install_from_archive__mutmut_27': xǁGoManagerǁ_install_from_archive__mutmut_27, 
        'xǁGoManagerǁ_install_from_archive__mutmut_28': xǁGoManagerǁ_install_from_archive__mutmut_28, 
        'xǁGoManagerǁ_install_from_archive__mutmut_29': xǁGoManagerǁ_install_from_archive__mutmut_29, 
        'xǁGoManagerǁ_install_from_archive__mutmut_30': xǁGoManagerǁ_install_from_archive__mutmut_30, 
        'xǁGoManagerǁ_install_from_archive__mutmut_31': xǁGoManagerǁ_install_from_archive__mutmut_31, 
        'xǁGoManagerǁ_install_from_archive__mutmut_32': xǁGoManagerǁ_install_from_archive__mutmut_32, 
        'xǁGoManagerǁ_install_from_archive__mutmut_33': xǁGoManagerǁ_install_from_archive__mutmut_33, 
        'xǁGoManagerǁ_install_from_archive__mutmut_34': xǁGoManagerǁ_install_from_archive__mutmut_34, 
        'xǁGoManagerǁ_install_from_archive__mutmut_35': xǁGoManagerǁ_install_from_archive__mutmut_35, 
        'xǁGoManagerǁ_install_from_archive__mutmut_36': xǁGoManagerǁ_install_from_archive__mutmut_36, 
        'xǁGoManagerǁ_install_from_archive__mutmut_37': xǁGoManagerǁ_install_from_archive__mutmut_37, 
        'xǁGoManagerǁ_install_from_archive__mutmut_38': xǁGoManagerǁ_install_from_archive__mutmut_38, 
        'xǁGoManagerǁ_install_from_archive__mutmut_39': xǁGoManagerǁ_install_from_archive__mutmut_39, 
        'xǁGoManagerǁ_install_from_archive__mutmut_40': xǁGoManagerǁ_install_from_archive__mutmut_40, 
        'xǁGoManagerǁ_install_from_archive__mutmut_41': xǁGoManagerǁ_install_from_archive__mutmut_41, 
        'xǁGoManagerǁ_install_from_archive__mutmut_42': xǁGoManagerǁ_install_from_archive__mutmut_42, 
        'xǁGoManagerǁ_install_from_archive__mutmut_43': xǁGoManagerǁ_install_from_archive__mutmut_43, 
        'xǁGoManagerǁ_install_from_archive__mutmut_44': xǁGoManagerǁ_install_from_archive__mutmut_44, 
        'xǁGoManagerǁ_install_from_archive__mutmut_45': xǁGoManagerǁ_install_from_archive__mutmut_45, 
        'xǁGoManagerǁ_install_from_archive__mutmut_46': xǁGoManagerǁ_install_from_archive__mutmut_46, 
        'xǁGoManagerǁ_install_from_archive__mutmut_47': xǁGoManagerǁ_install_from_archive__mutmut_47, 
        'xǁGoManagerǁ_install_from_archive__mutmut_48': xǁGoManagerǁ_install_from_archive__mutmut_48, 
        'xǁGoManagerǁ_install_from_archive__mutmut_49': xǁGoManagerǁ_install_from_archive__mutmut_49, 
        'xǁGoManagerǁ_install_from_archive__mutmut_50': xǁGoManagerǁ_install_from_archive__mutmut_50, 
        'xǁGoManagerǁ_install_from_archive__mutmut_51': xǁGoManagerǁ_install_from_archive__mutmut_51, 
        'xǁGoManagerǁ_install_from_archive__mutmut_52': xǁGoManagerǁ_install_from_archive__mutmut_52, 
        'xǁGoManagerǁ_install_from_archive__mutmut_53': xǁGoManagerǁ_install_from_archive__mutmut_53, 
        'xǁGoManagerǁ_install_from_archive__mutmut_54': xǁGoManagerǁ_install_from_archive__mutmut_54, 
        'xǁGoManagerǁ_install_from_archive__mutmut_55': xǁGoManagerǁ_install_from_archive__mutmut_55, 
        'xǁGoManagerǁ_install_from_archive__mutmut_56': xǁGoManagerǁ_install_from_archive__mutmut_56, 
        'xǁGoManagerǁ_install_from_archive__mutmut_57': xǁGoManagerǁ_install_from_archive__mutmut_57, 
        'xǁGoManagerǁ_install_from_archive__mutmut_58': xǁGoManagerǁ_install_from_archive__mutmut_58, 
        'xǁGoManagerǁ_install_from_archive__mutmut_59': xǁGoManagerǁ_install_from_archive__mutmut_59, 
        'xǁGoManagerǁ_install_from_archive__mutmut_60': xǁGoManagerǁ_install_from_archive__mutmut_60, 
        'xǁGoManagerǁ_install_from_archive__mutmut_61': xǁGoManagerǁ_install_from_archive__mutmut_61, 
        'xǁGoManagerǁ_install_from_archive__mutmut_62': xǁGoManagerǁ_install_from_archive__mutmut_62, 
        'xǁGoManagerǁ_install_from_archive__mutmut_63': xǁGoManagerǁ_install_from_archive__mutmut_63, 
        'xǁGoManagerǁ_install_from_archive__mutmut_64': xǁGoManagerǁ_install_from_archive__mutmut_64, 
        'xǁGoManagerǁ_install_from_archive__mutmut_65': xǁGoManagerǁ_install_from_archive__mutmut_65, 
        'xǁGoManagerǁ_install_from_archive__mutmut_66': xǁGoManagerǁ_install_from_archive__mutmut_66, 
        'xǁGoManagerǁ_install_from_archive__mutmut_67': xǁGoManagerǁ_install_from_archive__mutmut_67
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁGoManagerǁ_install_from_archive__mutmut_orig)
    xǁGoManagerǁ_install_from_archive__mutmut_orig.__name__ = 'xǁGoManagerǁ_install_from_archive'

    def xǁGoManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(None)
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return True

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = None
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent * "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "XXgoXX"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "GO"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = None

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"XXGOROOTXX": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"goroot": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(None)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = None

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                None,
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=None,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=None,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(None), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "XXversionXX"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "VERSION"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=11,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode != 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 1:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = None
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(None)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(None, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, None):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_31(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_32(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, ):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_33(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(None)
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_34(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return False
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_35(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(None)
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_36(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(None)

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_37(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return True

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return False

    def xǁGoManagerǁverify_installation__mutmut_38(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(None)
            return False

    def xǁGoManagerǁverify_installation__mutmut_39(self, version: str) -> bool:
        """Verify that Go installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"Go binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            # Set GOROOT for this Go installation
            go_root = binary_path.parent.parent / "go"
            env = {"GOROOT": str(go_root)}

            result = run(
                [str(binary_path), "version"],
                timeout=10,
                env=env,
            )

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"go{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    if logger.is_debug_enabled():
                        logger.debug(f"Go {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in Go output: {result.stdout}")
            else:
                logger.error(f"Go version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify Go installation: {e}")
            return True
    
    xǁGoManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁverify_installation__mutmut_1': xǁGoManagerǁverify_installation__mutmut_1, 
        'xǁGoManagerǁverify_installation__mutmut_2': xǁGoManagerǁverify_installation__mutmut_2, 
        'xǁGoManagerǁverify_installation__mutmut_3': xǁGoManagerǁverify_installation__mutmut_3, 
        'xǁGoManagerǁverify_installation__mutmut_4': xǁGoManagerǁverify_installation__mutmut_4, 
        'xǁGoManagerǁverify_installation__mutmut_5': xǁGoManagerǁverify_installation__mutmut_5, 
        'xǁGoManagerǁverify_installation__mutmut_6': xǁGoManagerǁverify_installation__mutmut_6, 
        'xǁGoManagerǁverify_installation__mutmut_7': xǁGoManagerǁverify_installation__mutmut_7, 
        'xǁGoManagerǁverify_installation__mutmut_8': xǁGoManagerǁverify_installation__mutmut_8, 
        'xǁGoManagerǁverify_installation__mutmut_9': xǁGoManagerǁverify_installation__mutmut_9, 
        'xǁGoManagerǁverify_installation__mutmut_10': xǁGoManagerǁverify_installation__mutmut_10, 
        'xǁGoManagerǁverify_installation__mutmut_11': xǁGoManagerǁverify_installation__mutmut_11, 
        'xǁGoManagerǁverify_installation__mutmut_12': xǁGoManagerǁverify_installation__mutmut_12, 
        'xǁGoManagerǁverify_installation__mutmut_13': xǁGoManagerǁverify_installation__mutmut_13, 
        'xǁGoManagerǁverify_installation__mutmut_14': xǁGoManagerǁverify_installation__mutmut_14, 
        'xǁGoManagerǁverify_installation__mutmut_15': xǁGoManagerǁverify_installation__mutmut_15, 
        'xǁGoManagerǁverify_installation__mutmut_16': xǁGoManagerǁverify_installation__mutmut_16, 
        'xǁGoManagerǁverify_installation__mutmut_17': xǁGoManagerǁverify_installation__mutmut_17, 
        'xǁGoManagerǁverify_installation__mutmut_18': xǁGoManagerǁverify_installation__mutmut_18, 
        'xǁGoManagerǁverify_installation__mutmut_19': xǁGoManagerǁverify_installation__mutmut_19, 
        'xǁGoManagerǁverify_installation__mutmut_20': xǁGoManagerǁverify_installation__mutmut_20, 
        'xǁGoManagerǁverify_installation__mutmut_21': xǁGoManagerǁverify_installation__mutmut_21, 
        'xǁGoManagerǁverify_installation__mutmut_22': xǁGoManagerǁverify_installation__mutmut_22, 
        'xǁGoManagerǁverify_installation__mutmut_23': xǁGoManagerǁverify_installation__mutmut_23, 
        'xǁGoManagerǁverify_installation__mutmut_24': xǁGoManagerǁverify_installation__mutmut_24, 
        'xǁGoManagerǁverify_installation__mutmut_25': xǁGoManagerǁverify_installation__mutmut_25, 
        'xǁGoManagerǁverify_installation__mutmut_26': xǁGoManagerǁverify_installation__mutmut_26, 
        'xǁGoManagerǁverify_installation__mutmut_27': xǁGoManagerǁverify_installation__mutmut_27, 
        'xǁGoManagerǁverify_installation__mutmut_28': xǁGoManagerǁverify_installation__mutmut_28, 
        'xǁGoManagerǁverify_installation__mutmut_29': xǁGoManagerǁverify_installation__mutmut_29, 
        'xǁGoManagerǁverify_installation__mutmut_30': xǁGoManagerǁverify_installation__mutmut_30, 
        'xǁGoManagerǁverify_installation__mutmut_31': xǁGoManagerǁverify_installation__mutmut_31, 
        'xǁGoManagerǁverify_installation__mutmut_32': xǁGoManagerǁverify_installation__mutmut_32, 
        'xǁGoManagerǁverify_installation__mutmut_33': xǁGoManagerǁverify_installation__mutmut_33, 
        'xǁGoManagerǁverify_installation__mutmut_34': xǁGoManagerǁverify_installation__mutmut_34, 
        'xǁGoManagerǁverify_installation__mutmut_35': xǁGoManagerǁverify_installation__mutmut_35, 
        'xǁGoManagerǁverify_installation__mutmut_36': xǁGoManagerǁverify_installation__mutmut_36, 
        'xǁGoManagerǁverify_installation__mutmut_37': xǁGoManagerǁverify_installation__mutmut_37, 
        'xǁGoManagerǁverify_installation__mutmut_38': xǁGoManagerǁverify_installation__mutmut_38, 
        'xǁGoManagerǁverify_installation__mutmut_39': xǁGoManagerǁverify_installation__mutmut_39
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁGoManagerǁverify_installation__mutmut_orig)
    xǁGoManagerǁverify_installation__mutmut_orig.__name__ = 'xǁGoManagerǁverify_installation'

    def xǁGoManagerǁget_harness_compatibility__mutmut_orig(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_1(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = None
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_2(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_3(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"XXstatusXX": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_4(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"STATUS": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_5(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "XXnot_installedXX"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_6(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "NOT_INSTALLED"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_7(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = None

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_8(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "XXstatusXX": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_9(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "STATUS": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_10(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "XXcompatibleXX",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_11(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "COMPATIBLE",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_12(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "XXversionXX": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_13(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "VERSION": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_14(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "XXharnessXX": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_15(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "HARNESS": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_16(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "XXgo.ctyXX": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_17(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "GO.CTY": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_18(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(None),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_19(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "XXgo.rpcXX": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_20(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "GO.RPC": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_21(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(None),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_22(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "XXgo.wireXX": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_23(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "GO.WIRE": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_24(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(None),
                "go.hcl": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_25(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "XXgo.hclXX": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_26(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "GO.HCL": self._check_go_hcl_compatibility(version),
            },
        }

        return compatibility

    def xǁGoManagerǁget_harness_compatibility__mutmut_27(self) -> dict:
        """Get compatibility information for Go-based tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with Go-based tools
        compatibility = {
            "status": "compatible",
            "version": version,
            "harness": {
                "go.cty": self._check_go_cty_compatibility(version),
                "go.rpc": self._check_go_rpc_compatibility(version),
                "go.wire": self._check_go_wire_compatibility(version),
                "go.hcl": self._check_go_hcl_compatibility(None),
            },
        }

        return compatibility
    
    xǁGoManagerǁget_harness_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁget_harness_compatibility__mutmut_1': xǁGoManagerǁget_harness_compatibility__mutmut_1, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_2': xǁGoManagerǁget_harness_compatibility__mutmut_2, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_3': xǁGoManagerǁget_harness_compatibility__mutmut_3, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_4': xǁGoManagerǁget_harness_compatibility__mutmut_4, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_5': xǁGoManagerǁget_harness_compatibility__mutmut_5, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_6': xǁGoManagerǁget_harness_compatibility__mutmut_6, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_7': xǁGoManagerǁget_harness_compatibility__mutmut_7, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_8': xǁGoManagerǁget_harness_compatibility__mutmut_8, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_9': xǁGoManagerǁget_harness_compatibility__mutmut_9, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_10': xǁGoManagerǁget_harness_compatibility__mutmut_10, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_11': xǁGoManagerǁget_harness_compatibility__mutmut_11, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_12': xǁGoManagerǁget_harness_compatibility__mutmut_12, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_13': xǁGoManagerǁget_harness_compatibility__mutmut_13, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_14': xǁGoManagerǁget_harness_compatibility__mutmut_14, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_15': xǁGoManagerǁget_harness_compatibility__mutmut_15, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_16': xǁGoManagerǁget_harness_compatibility__mutmut_16, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_17': xǁGoManagerǁget_harness_compatibility__mutmut_17, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_18': xǁGoManagerǁget_harness_compatibility__mutmut_18, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_19': xǁGoManagerǁget_harness_compatibility__mutmut_19, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_20': xǁGoManagerǁget_harness_compatibility__mutmut_20, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_21': xǁGoManagerǁget_harness_compatibility__mutmut_21, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_22': xǁGoManagerǁget_harness_compatibility__mutmut_22, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_23': xǁGoManagerǁget_harness_compatibility__mutmut_23, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_24': xǁGoManagerǁget_harness_compatibility__mutmut_24, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_25': xǁGoManagerǁget_harness_compatibility__mutmut_25, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_26': xǁGoManagerǁget_harness_compatibility__mutmut_26, 
        'xǁGoManagerǁget_harness_compatibility__mutmut_27': xǁGoManagerǁget_harness_compatibility__mutmut_27
    }
    
    def get_harness_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁget_harness_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁget_harness_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_harness_compatibility.__signature__ = _mutmut_signature(xǁGoManagerǁget_harness_compatibility__mutmut_orig)
    xǁGoManagerǁget_harness_compatibility__mutmut_orig.__name__ = 'xǁGoManagerǁget_harness_compatibility'

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(None, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, None) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare("1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, ) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "XX1.18.0XX") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") > 0

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 1

        return {
            "compatible": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"go-cty tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_cty_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with go-cty tools."""
        # go-cty requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "NOTES": f"go-cty tools require Go 1.18+ (current: {version})",
        }
    
    xǁGoManagerǁ_check_go_cty_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_1': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_1, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_2': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_2, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_3': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_3, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_4': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_4, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_5': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_5, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_6': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_6, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_7': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_7, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_8': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_8, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_9': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_9, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_10': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_10, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_11': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_11, 
        'xǁGoManagerǁ_check_go_cty_compatibility__mutmut_12': xǁGoManagerǁ_check_go_cty_compatibility__mutmut_12
    }
    
    def _check_go_cty_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁ_check_go_cty_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁ_check_go_cty_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_go_cty_compatibility.__signature__ = _mutmut_signature(xǁGoManagerǁ_check_go_cty_compatibility__mutmut_orig)
    xǁGoManagerǁ_check_go_cty_compatibility__mutmut_orig.__name__ = 'xǁGoManagerǁ_check_go_cty_compatibility'

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(None, "1.19.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, None) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare("1.19.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, ) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "XX1.19.0XX") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") > 0

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") >= 1

        return {
            "compatible": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") >= 0

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") >= 0

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") >= 0

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"go-rpc tools require Go 1.19+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with go-rpc tools."""
        # go-rpc requires Go 1.19+ for generics
        is_compatible = self._version_compare(version, "1.19.0") >= 0

        return {
            "compatible": is_compatible,
            "NOTES": f"go-rpc tools require Go 1.19+ (current: {version})",
        }
    
    xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_1': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_1, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_2': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_2, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_3': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_3, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_4': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_4, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_5': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_5, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_6': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_6, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_7': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_7, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_8': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_8, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_9': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_9, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_10': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_10, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_11': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_11, 
        'xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_12': xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_12
    }
    
    def _check_go_rpc_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_go_rpc_compatibility.__signature__ = _mutmut_signature(xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_orig)
    xǁGoManagerǁ_check_go_rpc_compatibility__mutmut_orig.__name__ = 'xǁGoManagerǁ_check_go_rpc_compatibility'

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(None, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, None) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare("1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, ) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "XX1.18.0XX") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") > 0

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 1

        return {
            "compatible": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"go-wire tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_wire_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with go-wire tools."""
        # go-wire requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "NOTES": f"go-wire tools require Go 1.18+ (current: {version})",
        }
    
    xǁGoManagerǁ_check_go_wire_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_1': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_1, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_2': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_2, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_3': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_3, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_4': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_4, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_5': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_5, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_6': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_6, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_7': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_7, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_8': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_8, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_9': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_9, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_10': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_10, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_11': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_11, 
        'xǁGoManagerǁ_check_go_wire_compatibility__mutmut_12': xǁGoManagerǁ_check_go_wire_compatibility__mutmut_12
    }
    
    def _check_go_wire_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁ_check_go_wire_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁ_check_go_wire_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_go_wire_compatibility.__signature__ = _mutmut_signature(xǁGoManagerǁ_check_go_wire_compatibility__mutmut_orig)
    xǁGoManagerǁ_check_go_wire_compatibility__mutmut_orig.__name__ = 'xǁGoManagerǁ_check_go_wire_compatibility'

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(None, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, None) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare("1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, ) >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "XX1.18.0XX") >= 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") > 0

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 1

        return {
            "compatible": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"go-hcl tools require Go 1.18+ (current: {version})",
        }

    def xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with go-hcl tools."""
        # go-hcl requires Go 1.18+
        is_compatible = self._version_compare(version, "1.18.0") >= 0

        return {
            "compatible": is_compatible,
            "NOTES": f"go-hcl tools require Go 1.18+ (current: {version})",
        }
    
    xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_1': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_1, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_2': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_2, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_3': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_3, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_4': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_4, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_5': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_5, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_6': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_6, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_7': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_7, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_8': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_8, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_9': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_9, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_10': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_10, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_11': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_11, 
        'xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_12': xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_12
    }
    
    def _check_go_hcl_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_go_hcl_compatibility.__signature__ = _mutmut_signature(xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_orig)
    xǁGoManagerǁ_check_go_hcl_compatibility__mutmut_orig.__name__ = 'xǁGoManagerǁ_check_go_hcl_compatibility'

    def xǁGoManagerǁ_version_compare__mutmut_orig(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_1(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(None)

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_2(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(None, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_3(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, None))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_4(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_5(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, ))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_6(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(None)))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_7(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split("XX.XX")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_8(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = None
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_9(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(None)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_10(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = None

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_11(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(None)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_12(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple <= v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_13(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return +1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_14(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -2
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_15(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple >= v2_tuple:
            return 1
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_16(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 2
        else:
            return 0

    def xǁGoManagerǁ_version_compare__mutmut_17(self, version1: str, version2: str) -> int:
        """Compare two version strings. Returns -1, 0, or 1."""

        def version_tuple(v: str) -> tuple[int, ...]:
            return tuple(map(int, v.split(".")))

        v1_tuple = version_tuple(version1)
        v2_tuple = version_tuple(version2)

        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 1
    
    xǁGoManagerǁ_version_compare__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁ_version_compare__mutmut_1': xǁGoManagerǁ_version_compare__mutmut_1, 
        'xǁGoManagerǁ_version_compare__mutmut_2': xǁGoManagerǁ_version_compare__mutmut_2, 
        'xǁGoManagerǁ_version_compare__mutmut_3': xǁGoManagerǁ_version_compare__mutmut_3, 
        'xǁGoManagerǁ_version_compare__mutmut_4': xǁGoManagerǁ_version_compare__mutmut_4, 
        'xǁGoManagerǁ_version_compare__mutmut_5': xǁGoManagerǁ_version_compare__mutmut_5, 
        'xǁGoManagerǁ_version_compare__mutmut_6': xǁGoManagerǁ_version_compare__mutmut_6, 
        'xǁGoManagerǁ_version_compare__mutmut_7': xǁGoManagerǁ_version_compare__mutmut_7, 
        'xǁGoManagerǁ_version_compare__mutmut_8': xǁGoManagerǁ_version_compare__mutmut_8, 
        'xǁGoManagerǁ_version_compare__mutmut_9': xǁGoManagerǁ_version_compare__mutmut_9, 
        'xǁGoManagerǁ_version_compare__mutmut_10': xǁGoManagerǁ_version_compare__mutmut_10, 
        'xǁGoManagerǁ_version_compare__mutmut_11': xǁGoManagerǁ_version_compare__mutmut_11, 
        'xǁGoManagerǁ_version_compare__mutmut_12': xǁGoManagerǁ_version_compare__mutmut_12, 
        'xǁGoManagerǁ_version_compare__mutmut_13': xǁGoManagerǁ_version_compare__mutmut_13, 
        'xǁGoManagerǁ_version_compare__mutmut_14': xǁGoManagerǁ_version_compare__mutmut_14, 
        'xǁGoManagerǁ_version_compare__mutmut_15': xǁGoManagerǁ_version_compare__mutmut_15, 
        'xǁGoManagerǁ_version_compare__mutmut_16': xǁGoManagerǁ_version_compare__mutmut_16, 
        'xǁGoManagerǁ_version_compare__mutmut_17': xǁGoManagerǁ_version_compare__mutmut_17
    }
    
    def _version_compare(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁ_version_compare__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁ_version_compare__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _version_compare.__signature__ = _mutmut_signature(xǁGoManagerǁ_version_compare__mutmut_orig)
    xǁGoManagerǁ_version_compare__mutmut_orig.__name__ = 'xǁGoManagerǁ_version_compare'

    def xǁGoManagerǁget_goroot__mutmut_orig(self, version: str) -> pathlib.Path:
        """Get GOROOT path for a specific Go version."""
        return self.install_path / self.tool_name / version / "go"

    def xǁGoManagerǁget_goroot__mutmut_1(self, version: str) -> pathlib.Path:
        """Get GOROOT path for a specific Go version."""
        return self.install_path / self.tool_name / version * "go"

    def xǁGoManagerǁget_goroot__mutmut_2(self, version: str) -> pathlib.Path:
        """Get GOROOT path for a specific Go version."""
        return self.install_path / self.tool_name * version / "go"

    def xǁGoManagerǁget_goroot__mutmut_3(self, version: str) -> pathlib.Path:
        """Get GOROOT path for a specific Go version."""
        return self.install_path * self.tool_name / version / "go"

    def xǁGoManagerǁget_goroot__mutmut_4(self, version: str) -> pathlib.Path:
        """Get GOROOT path for a specific Go version."""
        return self.install_path / self.tool_name / version / "XXgoXX"

    def xǁGoManagerǁget_goroot__mutmut_5(self, version: str) -> pathlib.Path:
        """Get GOROOT path for a specific Go version."""
        return self.install_path / self.tool_name / version / "GO"
    
    xǁGoManagerǁget_goroot__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁget_goroot__mutmut_1': xǁGoManagerǁget_goroot__mutmut_1, 
        'xǁGoManagerǁget_goroot__mutmut_2': xǁGoManagerǁget_goroot__mutmut_2, 
        'xǁGoManagerǁget_goroot__mutmut_3': xǁGoManagerǁget_goroot__mutmut_3, 
        'xǁGoManagerǁget_goroot__mutmut_4': xǁGoManagerǁget_goroot__mutmut_4, 
        'xǁGoManagerǁget_goroot__mutmut_5': xǁGoManagerǁget_goroot__mutmut_5
    }
    
    def get_goroot(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁget_goroot__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁget_goroot__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_goroot.__signature__ = _mutmut_signature(xǁGoManagerǁget_goroot__mutmut_orig)
    xǁGoManagerǁget_goroot__mutmut_orig.__name__ = 'xǁGoManagerǁget_goroot'

    def xǁGoManagerǁget_gopath__mutmut_orig(self, version: str) -> pathlib.Path:
        """Get default GOPATH for a specific Go version."""
        return self.install_path / self.tool_name / version / "gopath"

    def xǁGoManagerǁget_gopath__mutmut_1(self, version: str) -> pathlib.Path:
        """Get default GOPATH for a specific Go version."""
        return self.install_path / self.tool_name / version * "gopath"

    def xǁGoManagerǁget_gopath__mutmut_2(self, version: str) -> pathlib.Path:
        """Get default GOPATH for a specific Go version."""
        return self.install_path / self.tool_name * version / "gopath"

    def xǁGoManagerǁget_gopath__mutmut_3(self, version: str) -> pathlib.Path:
        """Get default GOPATH for a specific Go version."""
        return self.install_path * self.tool_name / version / "gopath"

    def xǁGoManagerǁget_gopath__mutmut_4(self, version: str) -> pathlib.Path:
        """Get default GOPATH for a specific Go version."""
        return self.install_path / self.tool_name / version / "XXgopathXX"

    def xǁGoManagerǁget_gopath__mutmut_5(self, version: str) -> pathlib.Path:
        """Get default GOPATH for a specific Go version."""
        return self.install_path / self.tool_name / version / "GOPATH"
    
    xǁGoManagerǁget_gopath__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGoManagerǁget_gopath__mutmut_1': xǁGoManagerǁget_gopath__mutmut_1, 
        'xǁGoManagerǁget_gopath__mutmut_2': xǁGoManagerǁget_gopath__mutmut_2, 
        'xǁGoManagerǁget_gopath__mutmut_3': xǁGoManagerǁget_gopath__mutmut_3, 
        'xǁGoManagerǁget_gopath__mutmut_4': xǁGoManagerǁget_gopath__mutmut_4, 
        'xǁGoManagerǁget_gopath__mutmut_5': xǁGoManagerǁget_gopath__mutmut_5
    }
    
    def get_gopath(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGoManagerǁget_gopath__mutmut_orig"), object.__getattribute__(self, "xǁGoManagerǁget_gopath__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_gopath.__signature__ = _mutmut_signature(xǁGoManagerǁget_gopath__mutmut_orig)
    xǁGoManagerǁget_gopath__mutmut_orig.__name__ = 'xǁGoManagerǁget_gopath'


# 🧰🌍🔚
