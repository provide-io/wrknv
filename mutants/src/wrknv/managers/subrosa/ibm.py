#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""IBM Vault Variant for SubRosaManager
=====================================
Manages IBM Vault (HashiCorp Vault) versions for development."""

from __future__ import annotations

import asyncio
import pathlib

from provide.foundation import logger
from provide.foundation.file import safe_copy, safe_rmtree
from provide.foundation.transport import get

from wrknv.managers.base import ToolManagerError
from wrknv.managers.subrosa.base import SubRosaManager
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


class IbmVaultVariant(SubRosaManager):
    """IBM Vault (HashiCorp Vault) variant of secret management tools."""

    @property
    def variant_name(self) -> str:
        """Variant name for this secret manager."""
        return "vault"

    def xǁIbmVaultVariantǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = None

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "XXhttps://releases.hashicorp.com/vault/index.jsonXX"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "HTTPS://RELEASES.HASHICORP.COM/VAULT/INDEX.JSON"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(None)

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = None
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(None)
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(None))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = None

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = None
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = None

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting(None, False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", None)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting(False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", )

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("XXinclude_prereleasesXX", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("INCLUDE_PRERELEASES", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", True)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_18(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get(None, {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_19(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", None).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_20(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get({}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_21(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", ).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_22(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("XXversionsXX", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_23(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("VERSIONS", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_24(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases or any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_25(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_26(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    None
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_27(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag not in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_28(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["XX-rcXX", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_29(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-RC", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_30(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "XX-betaXX", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_31(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-BETA", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_32(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "XX-alphaXX", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_33(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-ALPHA", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_34(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "XX-devXX"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_35(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-DEV"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_36(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    break

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_37(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(None)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_38(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(None)

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_39(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=None, reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_40(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=None)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_41(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_42(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), )
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_43(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: None, reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_44(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(None), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_45(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=False)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_46(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=None)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_47(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=False)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch Vault versions: {e}") from e

    def xǁIbmVaultVariantǁget_available_versions__mutmut_48(self) -> list[str]:
        """Get available HashiCorp Vault versions from releases API."""
        try:
            # HashiCorp provides a JSON API for releases
            api_url = "https://releases.hashicorp.com/vault/index.json"

            logger.debug(f"Fetching Vault versions from {api_url}")

            response = asyncio.run(get(api_url))
            data = response.json()

            versions = []
            include_prereleases = self.config.get_setting("include_prereleases", False)

            # Parse versions from release data
            for version_str, _version_data in data.get("versions", {}).items():
                # Skip pre-releases unless configured
                if not include_prereleases and any(
                    tag in version_str for tag in ["-rc", "-beta", "-alpha", "-dev"]
                ):
                    continue

                versions.append(version_str)

            logger.debug(f"Found {len(versions)} Vault versions")

            # Sort versions
            try:
                from packaging.version import parse as parse_version

                versions.sort(key=lambda v: parse_version(v), reverse=True)
            except Exception:
                versions.sort(reverse=True)

            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁIbmVaultVariantǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmVaultVariantǁget_available_versions__mutmut_1': xǁIbmVaultVariantǁget_available_versions__mutmut_1, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_2': xǁIbmVaultVariantǁget_available_versions__mutmut_2, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_3': xǁIbmVaultVariantǁget_available_versions__mutmut_3, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_4': xǁIbmVaultVariantǁget_available_versions__mutmut_4, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_5': xǁIbmVaultVariantǁget_available_versions__mutmut_5, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_6': xǁIbmVaultVariantǁget_available_versions__mutmut_6, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_7': xǁIbmVaultVariantǁget_available_versions__mutmut_7, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_8': xǁIbmVaultVariantǁget_available_versions__mutmut_8, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_9': xǁIbmVaultVariantǁget_available_versions__mutmut_9, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_10': xǁIbmVaultVariantǁget_available_versions__mutmut_10, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_11': xǁIbmVaultVariantǁget_available_versions__mutmut_11, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_12': xǁIbmVaultVariantǁget_available_versions__mutmut_12, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_13': xǁIbmVaultVariantǁget_available_versions__mutmut_13, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_14': xǁIbmVaultVariantǁget_available_versions__mutmut_14, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_15': xǁIbmVaultVariantǁget_available_versions__mutmut_15, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_16': xǁIbmVaultVariantǁget_available_versions__mutmut_16, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_17': xǁIbmVaultVariantǁget_available_versions__mutmut_17, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_18': xǁIbmVaultVariantǁget_available_versions__mutmut_18, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_19': xǁIbmVaultVariantǁget_available_versions__mutmut_19, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_20': xǁIbmVaultVariantǁget_available_versions__mutmut_20, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_21': xǁIbmVaultVariantǁget_available_versions__mutmut_21, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_22': xǁIbmVaultVariantǁget_available_versions__mutmut_22, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_23': xǁIbmVaultVariantǁget_available_versions__mutmut_23, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_24': xǁIbmVaultVariantǁget_available_versions__mutmut_24, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_25': xǁIbmVaultVariantǁget_available_versions__mutmut_25, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_26': xǁIbmVaultVariantǁget_available_versions__mutmut_26, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_27': xǁIbmVaultVariantǁget_available_versions__mutmut_27, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_28': xǁIbmVaultVariantǁget_available_versions__mutmut_28, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_29': xǁIbmVaultVariantǁget_available_versions__mutmut_29, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_30': xǁIbmVaultVariantǁget_available_versions__mutmut_30, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_31': xǁIbmVaultVariantǁget_available_versions__mutmut_31, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_32': xǁIbmVaultVariantǁget_available_versions__mutmut_32, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_33': xǁIbmVaultVariantǁget_available_versions__mutmut_33, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_34': xǁIbmVaultVariantǁget_available_versions__mutmut_34, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_35': xǁIbmVaultVariantǁget_available_versions__mutmut_35, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_36': xǁIbmVaultVariantǁget_available_versions__mutmut_36, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_37': xǁIbmVaultVariantǁget_available_versions__mutmut_37, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_38': xǁIbmVaultVariantǁget_available_versions__mutmut_38, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_39': xǁIbmVaultVariantǁget_available_versions__mutmut_39, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_40': xǁIbmVaultVariantǁget_available_versions__mutmut_40, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_41': xǁIbmVaultVariantǁget_available_versions__mutmut_41, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_42': xǁIbmVaultVariantǁget_available_versions__mutmut_42, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_43': xǁIbmVaultVariantǁget_available_versions__mutmut_43, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_44': xǁIbmVaultVariantǁget_available_versions__mutmut_44, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_45': xǁIbmVaultVariantǁget_available_versions__mutmut_45, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_46': xǁIbmVaultVariantǁget_available_versions__mutmut_46, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_47': xǁIbmVaultVariantǁget_available_versions__mutmut_47, 
        'xǁIbmVaultVariantǁget_available_versions__mutmut_48': xǁIbmVaultVariantǁget_available_versions__mutmut_48
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmVaultVariantǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁIbmVaultVariantǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁIbmVaultVariantǁget_available_versions__mutmut_orig)
    xǁIbmVaultVariantǁget_available_versions__mutmut_orig.__name__ = 'xǁIbmVaultVariantǁget_available_versions'

    def xǁIbmVaultVariantǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = None
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = None  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = None  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["XXarchXX"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["ARCH"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_8(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch != "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_9(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "XXarm64XX":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_10(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "ARM64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_11(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = None
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_12(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "XXarm64XX"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_13(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "ARM64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_14(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch not in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_15(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"XXamd64XX", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_16(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"AMD64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_17(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "XXx86_64XX"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_18(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "X86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_19(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = None
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_20(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "XXamd64XX"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_21(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "AMD64"
        else:
            hc_arch = arch

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"

    def xǁIbmVaultVariantǁget_download_url__mutmut_22(self, version: str) -> str:
        """Get download URL for HashiCorp Vault version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]  # darwin, linux, windows
        arch = platform_info["arch"]  # amd64, arm64, etc.

        # HashiCorp uses different arch naming for ARM
        if arch == "arm64":
            hc_arch = "arm64"
        elif arch in {"amd64", "x86_64"}:
            hc_arch = "amd64"
        else:
            hc_arch = None

        # HashiCorp naming: vault_1.15.0_darwin_arm64.zip
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_{os_name}_{hc_arch}.zip"
    
    xǁIbmVaultVariantǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmVaultVariantǁget_download_url__mutmut_1': xǁIbmVaultVariantǁget_download_url__mutmut_1, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_2': xǁIbmVaultVariantǁget_download_url__mutmut_2, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_3': xǁIbmVaultVariantǁget_download_url__mutmut_3, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_4': xǁIbmVaultVariantǁget_download_url__mutmut_4, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_5': xǁIbmVaultVariantǁget_download_url__mutmut_5, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_6': xǁIbmVaultVariantǁget_download_url__mutmut_6, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_7': xǁIbmVaultVariantǁget_download_url__mutmut_7, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_8': xǁIbmVaultVariantǁget_download_url__mutmut_8, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_9': xǁIbmVaultVariantǁget_download_url__mutmut_9, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_10': xǁIbmVaultVariantǁget_download_url__mutmut_10, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_11': xǁIbmVaultVariantǁget_download_url__mutmut_11, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_12': xǁIbmVaultVariantǁget_download_url__mutmut_12, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_13': xǁIbmVaultVariantǁget_download_url__mutmut_13, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_14': xǁIbmVaultVariantǁget_download_url__mutmut_14, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_15': xǁIbmVaultVariantǁget_download_url__mutmut_15, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_16': xǁIbmVaultVariantǁget_download_url__mutmut_16, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_17': xǁIbmVaultVariantǁget_download_url__mutmut_17, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_18': xǁIbmVaultVariantǁget_download_url__mutmut_18, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_19': xǁIbmVaultVariantǁget_download_url__mutmut_19, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_20': xǁIbmVaultVariantǁget_download_url__mutmut_20, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_21': xǁIbmVaultVariantǁget_download_url__mutmut_21, 
        'xǁIbmVaultVariantǁget_download_url__mutmut_22': xǁIbmVaultVariantǁget_download_url__mutmut_22
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmVaultVariantǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁIbmVaultVariantǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁIbmVaultVariantǁget_download_url__mutmut_orig)
    xǁIbmVaultVariantǁget_download_url__mutmut_orig.__name__ = 'xǁIbmVaultVariantǁget_download_url'

    def get_checksum_url(self, version: str) -> str | None:
        """Get checksum URL for HashiCorp Vault version."""
        # HashiCorp provides SHA256SUMS file
        return f"https://releases.hashicorp.com/vault/{version}/vault_{version}_SHA256SUMS"

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = None
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir * f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(None, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, None)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, )

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = ""
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(None):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("XXvault*XX"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("VAULT*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() or file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name not in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["XXvaultXX", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["VAULT", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "XXvault.exeXX"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "VAULT.EXE"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = None
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    return

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(None)

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("XXVault binary not found in archiveXX")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("VAULT BINARY NOT FOUND IN ARCHIVE")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = None
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(None)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(None, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, None, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=None)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, )

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=False)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(None)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_36(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(None)

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_37(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_38(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_39(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_40(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(None, missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_41(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=None)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_42(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(missing_ok=True)

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_43(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, )

    def xǁIbmVaultVariantǁ_install_from_archive__mutmut_44(self, archive_path: pathlib.Path, version: str) -> None:
        """Install Vault from downloaded ZIP archive.

        HashiCorp uses .zip format, not .tar.gz like OpenBao.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"vault_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            # Extract ZIP archive
            self.extract_archive(archive_path, extract_dir)

            # Find vault binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob("vault*"):
                if file_path.is_file() and file_path.name in ["vault", "vault.exe"]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError("Vault binary not found in archive")

            # Copy to target location with variant-specific naming
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed Vault binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"Vault {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=False)
    
    xǁIbmVaultVariantǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmVaultVariantǁ_install_from_archive__mutmut_1': xǁIbmVaultVariantǁ_install_from_archive__mutmut_1, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_2': xǁIbmVaultVariantǁ_install_from_archive__mutmut_2, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_3': xǁIbmVaultVariantǁ_install_from_archive__mutmut_3, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_4': xǁIbmVaultVariantǁ_install_from_archive__mutmut_4, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_5': xǁIbmVaultVariantǁ_install_from_archive__mutmut_5, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_6': xǁIbmVaultVariantǁ_install_from_archive__mutmut_6, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_7': xǁIbmVaultVariantǁ_install_from_archive__mutmut_7, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_8': xǁIbmVaultVariantǁ_install_from_archive__mutmut_8, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_9': xǁIbmVaultVariantǁ_install_from_archive__mutmut_9, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_10': xǁIbmVaultVariantǁ_install_from_archive__mutmut_10, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_11': xǁIbmVaultVariantǁ_install_from_archive__mutmut_11, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_12': xǁIbmVaultVariantǁ_install_from_archive__mutmut_12, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_13': xǁIbmVaultVariantǁ_install_from_archive__mutmut_13, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_14': xǁIbmVaultVariantǁ_install_from_archive__mutmut_14, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_15': xǁIbmVaultVariantǁ_install_from_archive__mutmut_15, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_16': xǁIbmVaultVariantǁ_install_from_archive__mutmut_16, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_17': xǁIbmVaultVariantǁ_install_from_archive__mutmut_17, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_18': xǁIbmVaultVariantǁ_install_from_archive__mutmut_18, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_19': xǁIbmVaultVariantǁ_install_from_archive__mutmut_19, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_20': xǁIbmVaultVariantǁ_install_from_archive__mutmut_20, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_21': xǁIbmVaultVariantǁ_install_from_archive__mutmut_21, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_22': xǁIbmVaultVariantǁ_install_from_archive__mutmut_22, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_23': xǁIbmVaultVariantǁ_install_from_archive__mutmut_23, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_24': xǁIbmVaultVariantǁ_install_from_archive__mutmut_24, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_25': xǁIbmVaultVariantǁ_install_from_archive__mutmut_25, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_26': xǁIbmVaultVariantǁ_install_from_archive__mutmut_26, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_27': xǁIbmVaultVariantǁ_install_from_archive__mutmut_27, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_28': xǁIbmVaultVariantǁ_install_from_archive__mutmut_28, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_29': xǁIbmVaultVariantǁ_install_from_archive__mutmut_29, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_30': xǁIbmVaultVariantǁ_install_from_archive__mutmut_30, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_31': xǁIbmVaultVariantǁ_install_from_archive__mutmut_31, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_32': xǁIbmVaultVariantǁ_install_from_archive__mutmut_32, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_33': xǁIbmVaultVariantǁ_install_from_archive__mutmut_33, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_34': xǁIbmVaultVariantǁ_install_from_archive__mutmut_34, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_35': xǁIbmVaultVariantǁ_install_from_archive__mutmut_35, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_36': xǁIbmVaultVariantǁ_install_from_archive__mutmut_36, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_37': xǁIbmVaultVariantǁ_install_from_archive__mutmut_37, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_38': xǁIbmVaultVariantǁ_install_from_archive__mutmut_38, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_39': xǁIbmVaultVariantǁ_install_from_archive__mutmut_39, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_40': xǁIbmVaultVariantǁ_install_from_archive__mutmut_40, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_41': xǁIbmVaultVariantǁ_install_from_archive__mutmut_41, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_42': xǁIbmVaultVariantǁ_install_from_archive__mutmut_42, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_43': xǁIbmVaultVariantǁ_install_from_archive__mutmut_43, 
        'xǁIbmVaultVariantǁ_install_from_archive__mutmut_44': xǁIbmVaultVariantǁ_install_from_archive__mutmut_44
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmVaultVariantǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁIbmVaultVariantǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁIbmVaultVariantǁ_install_from_archive__mutmut_orig)
    xǁIbmVaultVariantǁ_install_from_archive__mutmut_orig.__name__ = 'xǁIbmVaultVariantǁ_install_from_archive'


__all__ = [
    "IbmVaultVariant",
]

# 🧰🌍🔚
