# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#
# wrknv/workenv/managers/ibm_tf.py
#
"""
IBM Terraform Tool Manager for wrknv
=====================================
Manages IBM Terraform (formerly HashiCorp Terraform) versions for development environment.
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


class IbmTfManager(TfVersionsManager):
    """Manages IBM Terraform (formerly HashiCorp Terraform) versions using HashiCorp's releases API."""

    @property
    def tool_name(self) -> str:
        return "ibmtf"

    @property
    def executable_name(self) -> str:
        return "ibmtf"

    @property
    def tool_prefix(self) -> str:
        return "terraform"

    def xǁIbmTfManagerǁget_available_versions__mutmut_orig(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_1(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = None
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_2(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                None, "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_3(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", None
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_4(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_5(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_6(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "XXterraform_mirrorXX", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_7(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "TERRAFORM_MIRROR", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_8(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "XXhttps://releases.hashicorp.com/terraformXX"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_9(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "HTTPS://RELEASES.HASHICORP.COM/TERRAFORM"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_10(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = None
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_11(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip(None)}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_12(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.lstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_13(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('XX/XX')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_14(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = None

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_15(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(None)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_16(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = None
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_17(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get(None, {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_18(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", None).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_19(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get({}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_20(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", ).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_21(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("XXversionsXX", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_22(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("VERSIONS", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_23(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = None
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_24(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get(None)
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_25(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("XXversionXX")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_26(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("VERSION")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_27(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version or not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_28(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_29(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(None):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_30(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(None)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_31(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=None, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_32(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=None)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_33(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_34(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, )

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_35(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=False)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_36(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(None)
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_37(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(None)

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_38(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:6]}")

            return versions

        except Exception as e:
            raise ToolManagerError(f"Failed to fetch IBM Terraform versions: {e}") from e

    def xǁIbmTfManagerǁget_available_versions__mutmut_39(self) -> list[str]:
        """Get available IBM Terraform versions from HashiCorp releases API."""
        try:
            # Use custom mirror if configured
            mirror_url = self.config.get_setting(
                "terraform_mirror", "https://releases.hashicorp.com/terraform"
            )
            api_url = f"{mirror_url.rstrip('/')}/index.json"
            data = self.fetch_json_secure(api_url)

            versions = []
            for version_info in data.get("versions", {}).values():
                version = version_info.get("version")
                if version and not self._is_prerelease(version):
                    versions.append(version)

            # Sort versions in descending order (latest first)
            versions.sort(key=self._version_sort_key, reverse=True)

            logger.debug(f"Found {len(versions)} IBM Terraform versions")
            # Log the first few versions to debug
            if versions:
                logger.debug(f"Latest versions: {versions[:5]}")

            return versions

        except Exception as e:
            raise ToolManagerError(None) from e
    
    xǁIbmTfManagerǁget_available_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁget_available_versions__mutmut_1': xǁIbmTfManagerǁget_available_versions__mutmut_1, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_2': xǁIbmTfManagerǁget_available_versions__mutmut_2, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_3': xǁIbmTfManagerǁget_available_versions__mutmut_3, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_4': xǁIbmTfManagerǁget_available_versions__mutmut_4, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_5': xǁIbmTfManagerǁget_available_versions__mutmut_5, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_6': xǁIbmTfManagerǁget_available_versions__mutmut_6, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_7': xǁIbmTfManagerǁget_available_versions__mutmut_7, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_8': xǁIbmTfManagerǁget_available_versions__mutmut_8, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_9': xǁIbmTfManagerǁget_available_versions__mutmut_9, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_10': xǁIbmTfManagerǁget_available_versions__mutmut_10, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_11': xǁIbmTfManagerǁget_available_versions__mutmut_11, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_12': xǁIbmTfManagerǁget_available_versions__mutmut_12, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_13': xǁIbmTfManagerǁget_available_versions__mutmut_13, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_14': xǁIbmTfManagerǁget_available_versions__mutmut_14, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_15': xǁIbmTfManagerǁget_available_versions__mutmut_15, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_16': xǁIbmTfManagerǁget_available_versions__mutmut_16, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_17': xǁIbmTfManagerǁget_available_versions__mutmut_17, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_18': xǁIbmTfManagerǁget_available_versions__mutmut_18, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_19': xǁIbmTfManagerǁget_available_versions__mutmut_19, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_20': xǁIbmTfManagerǁget_available_versions__mutmut_20, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_21': xǁIbmTfManagerǁget_available_versions__mutmut_21, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_22': xǁIbmTfManagerǁget_available_versions__mutmut_22, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_23': xǁIbmTfManagerǁget_available_versions__mutmut_23, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_24': xǁIbmTfManagerǁget_available_versions__mutmut_24, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_25': xǁIbmTfManagerǁget_available_versions__mutmut_25, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_26': xǁIbmTfManagerǁget_available_versions__mutmut_26, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_27': xǁIbmTfManagerǁget_available_versions__mutmut_27, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_28': xǁIbmTfManagerǁget_available_versions__mutmut_28, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_29': xǁIbmTfManagerǁget_available_versions__mutmut_29, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_30': xǁIbmTfManagerǁget_available_versions__mutmut_30, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_31': xǁIbmTfManagerǁget_available_versions__mutmut_31, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_32': xǁIbmTfManagerǁget_available_versions__mutmut_32, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_33': xǁIbmTfManagerǁget_available_versions__mutmut_33, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_34': xǁIbmTfManagerǁget_available_versions__mutmut_34, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_35': xǁIbmTfManagerǁget_available_versions__mutmut_35, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_36': xǁIbmTfManagerǁget_available_versions__mutmut_36, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_37': xǁIbmTfManagerǁget_available_versions__mutmut_37, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_38': xǁIbmTfManagerǁget_available_versions__mutmut_38, 
        'xǁIbmTfManagerǁget_available_versions__mutmut_39': xǁIbmTfManagerǁget_available_versions__mutmut_39
    }
    
    def get_available_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁget_available_versions__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁget_available_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_available_versions.__signature__ = _mutmut_signature(xǁIbmTfManagerǁget_available_versions__mutmut_orig)
    xǁIbmTfManagerǁget_available_versions__mutmut_orig.__name__ = 'xǁIbmTfManagerǁget_available_versions'

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_orig(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_1(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = None
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_2(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting(None, False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_3(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", None)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_4(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting(False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_5(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", )
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_6(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("XXinclude_prereleasesXX", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_7(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("INCLUDE_PRERELEASES", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_8(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", True)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_9(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return True

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_10(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = None
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_11(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["XXalphaXX", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_12(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["ALPHA", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_13(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "XXbetaXX", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_14(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "BETA", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_15(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "XXrcXX", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_16(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "RC", "pre"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_17(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "XXpreXX"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_18(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "PRE"]
        version_lower = version.lower()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_19(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = None
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_20(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.upper()
        return any(pattern in version_lower for pattern in prerelease_patterns)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_21(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(None)

    def xǁIbmTfManagerǁ_is_prerelease__mutmut_22(self, version: str) -> bool:
        """Check if version is a prerelease."""
        include_prereleases = self.config.get_setting("include_prereleases", False)
        if include_prereleases:
            return False

        # Check for prerelease indicators
        prerelease_patterns = ["alpha", "beta", "rc", "pre"]
        version_lower = version.lower()
        return any(pattern not in version_lower for pattern in prerelease_patterns)
    
    xǁIbmTfManagerǁ_is_prerelease__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁ_is_prerelease__mutmut_1': xǁIbmTfManagerǁ_is_prerelease__mutmut_1, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_2': xǁIbmTfManagerǁ_is_prerelease__mutmut_2, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_3': xǁIbmTfManagerǁ_is_prerelease__mutmut_3, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_4': xǁIbmTfManagerǁ_is_prerelease__mutmut_4, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_5': xǁIbmTfManagerǁ_is_prerelease__mutmut_5, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_6': xǁIbmTfManagerǁ_is_prerelease__mutmut_6, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_7': xǁIbmTfManagerǁ_is_prerelease__mutmut_7, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_8': xǁIbmTfManagerǁ_is_prerelease__mutmut_8, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_9': xǁIbmTfManagerǁ_is_prerelease__mutmut_9, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_10': xǁIbmTfManagerǁ_is_prerelease__mutmut_10, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_11': xǁIbmTfManagerǁ_is_prerelease__mutmut_11, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_12': xǁIbmTfManagerǁ_is_prerelease__mutmut_12, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_13': xǁIbmTfManagerǁ_is_prerelease__mutmut_13, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_14': xǁIbmTfManagerǁ_is_prerelease__mutmut_14, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_15': xǁIbmTfManagerǁ_is_prerelease__mutmut_15, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_16': xǁIbmTfManagerǁ_is_prerelease__mutmut_16, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_17': xǁIbmTfManagerǁ_is_prerelease__mutmut_17, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_18': xǁIbmTfManagerǁ_is_prerelease__mutmut_18, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_19': xǁIbmTfManagerǁ_is_prerelease__mutmut_19, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_20': xǁIbmTfManagerǁ_is_prerelease__mutmut_20, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_21': xǁIbmTfManagerǁ_is_prerelease__mutmut_21, 
        'xǁIbmTfManagerǁ_is_prerelease__mutmut_22': xǁIbmTfManagerǁ_is_prerelease__mutmut_22
    }
    
    def _is_prerelease(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁ_is_prerelease__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁ_is_prerelease__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_prerelease.__signature__ = _mutmut_signature(xǁIbmTfManagerǁ_is_prerelease__mutmut_orig)
    xǁIbmTfManagerǁ_is_prerelease__mutmut_orig.__name__ = 'xǁIbmTfManagerǁ_is_prerelease'

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_orig(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_1(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_2(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_3(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_4(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_5(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_6(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_7(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_8(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_9(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_10(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_11(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_12(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_13(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_14(self, version: str) -> tuple[int, ...]:
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

    def xǁIbmTfManagerǁ_version_sort_key__mutmut_15(self, version: str) -> tuple[int, ...]:
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
    
    xǁIbmTfManagerǁ_version_sort_key__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁ_version_sort_key__mutmut_1': xǁIbmTfManagerǁ_version_sort_key__mutmut_1, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_2': xǁIbmTfManagerǁ_version_sort_key__mutmut_2, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_3': xǁIbmTfManagerǁ_version_sort_key__mutmut_3, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_4': xǁIbmTfManagerǁ_version_sort_key__mutmut_4, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_5': xǁIbmTfManagerǁ_version_sort_key__mutmut_5, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_6': xǁIbmTfManagerǁ_version_sort_key__mutmut_6, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_7': xǁIbmTfManagerǁ_version_sort_key__mutmut_7, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_8': xǁIbmTfManagerǁ_version_sort_key__mutmut_8, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_9': xǁIbmTfManagerǁ_version_sort_key__mutmut_9, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_10': xǁIbmTfManagerǁ_version_sort_key__mutmut_10, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_11': xǁIbmTfManagerǁ_version_sort_key__mutmut_11, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_12': xǁIbmTfManagerǁ_version_sort_key__mutmut_12, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_13': xǁIbmTfManagerǁ_version_sort_key__mutmut_13, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_14': xǁIbmTfManagerǁ_version_sort_key__mutmut_14, 
        'xǁIbmTfManagerǁ_version_sort_key__mutmut_15': xǁIbmTfManagerǁ_version_sort_key__mutmut_15
    }
    
    def _version_sort_key(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁ_version_sort_key__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁ_version_sort_key__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _version_sort_key.__signature__ = _mutmut_signature(xǁIbmTfManagerǁ_version_sort_key__mutmut_orig)
    xǁIbmTfManagerǁ_version_sort_key__mutmut_orig.__name__ = 'xǁIbmTfManagerǁ_version_sort_key'

    def xǁIbmTfManagerǁget_download_url__mutmut_orig(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_1(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = None
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_2(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = None
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_3(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["XXosXX"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_4(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["OS"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_5(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = None

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_6(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["XXarchXX"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_7(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["ARCH"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_8(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = None

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_9(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting(None, "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_10(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", None)

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_11(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_12(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", )

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_13(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("XXterraform_mirrorXX", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_14(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("TERRAFORM_MIRROR", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_15(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "XXhttps://releases.hashicorp.com/terraformXX")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_16(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "HTTPS://RELEASES.HASHICORP.COM/TERRAFORM")

        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_17(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip(None)}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_18(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.lstrip('/')}/{version}/terraform_{version}_{os_name}_{arch}.zip"

    def xǁIbmTfManagerǁget_download_url__mutmut_19(self, version: str) -> str:
        """Get download URL for IBM Terraform version."""
        platform_info = self.get_platform_info()
        os_name = platform_info["os"]
        arch = platform_info["arch"]

        # Use custom mirror if configured
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")

        return f"{mirror_url.rstrip('XX/XX')}/{version}/terraform_{version}_{os_name}_{arch}.zip"
    
    xǁIbmTfManagerǁget_download_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁget_download_url__mutmut_1': xǁIbmTfManagerǁget_download_url__mutmut_1, 
        'xǁIbmTfManagerǁget_download_url__mutmut_2': xǁIbmTfManagerǁget_download_url__mutmut_2, 
        'xǁIbmTfManagerǁget_download_url__mutmut_3': xǁIbmTfManagerǁget_download_url__mutmut_3, 
        'xǁIbmTfManagerǁget_download_url__mutmut_4': xǁIbmTfManagerǁget_download_url__mutmut_4, 
        'xǁIbmTfManagerǁget_download_url__mutmut_5': xǁIbmTfManagerǁget_download_url__mutmut_5, 
        'xǁIbmTfManagerǁget_download_url__mutmut_6': xǁIbmTfManagerǁget_download_url__mutmut_6, 
        'xǁIbmTfManagerǁget_download_url__mutmut_7': xǁIbmTfManagerǁget_download_url__mutmut_7, 
        'xǁIbmTfManagerǁget_download_url__mutmut_8': xǁIbmTfManagerǁget_download_url__mutmut_8, 
        'xǁIbmTfManagerǁget_download_url__mutmut_9': xǁIbmTfManagerǁget_download_url__mutmut_9, 
        'xǁIbmTfManagerǁget_download_url__mutmut_10': xǁIbmTfManagerǁget_download_url__mutmut_10, 
        'xǁIbmTfManagerǁget_download_url__mutmut_11': xǁIbmTfManagerǁget_download_url__mutmut_11, 
        'xǁIbmTfManagerǁget_download_url__mutmut_12': xǁIbmTfManagerǁget_download_url__mutmut_12, 
        'xǁIbmTfManagerǁget_download_url__mutmut_13': xǁIbmTfManagerǁget_download_url__mutmut_13, 
        'xǁIbmTfManagerǁget_download_url__mutmut_14': xǁIbmTfManagerǁget_download_url__mutmut_14, 
        'xǁIbmTfManagerǁget_download_url__mutmut_15': xǁIbmTfManagerǁget_download_url__mutmut_15, 
        'xǁIbmTfManagerǁget_download_url__mutmut_16': xǁIbmTfManagerǁget_download_url__mutmut_16, 
        'xǁIbmTfManagerǁget_download_url__mutmut_17': xǁIbmTfManagerǁget_download_url__mutmut_17, 
        'xǁIbmTfManagerǁget_download_url__mutmut_18': xǁIbmTfManagerǁget_download_url__mutmut_18, 
        'xǁIbmTfManagerǁget_download_url__mutmut_19': xǁIbmTfManagerǁget_download_url__mutmut_19
    }
    
    def get_download_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁget_download_url__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁget_download_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_download_url.__signature__ = _mutmut_signature(xǁIbmTfManagerǁget_download_url__mutmut_orig)
    xǁIbmTfManagerǁget_download_url__mutmut_orig.__name__ = 'xǁIbmTfManagerǁget_download_url'

    def xǁIbmTfManagerǁget_checksum_url__mutmut_orig(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_1(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = None
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_2(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting(None, "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_3(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", None)
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_4(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_5(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", )
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_6(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("XXterraform_mirrorXX", "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_7(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("TERRAFORM_MIRROR", "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_8(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", "XXhttps://releases.hashicorp.com/terraformXX")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_9(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", "HTTPS://RELEASES.HASHICORP.COM/TERRAFORM")
        return f"{mirror_url.rstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_10(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip(None)}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_11(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.lstrip('/')}/{version}/terraform_{version}_SHA256SUMS"

    def xǁIbmTfManagerǁget_checksum_url__mutmut_12(self, version: str) -> str | None:
        """Get checksum URL for IBM Terraform version."""
        mirror_url = self.config.get_setting("terraform_mirror", "https://releases.hashicorp.com/terraform")
        return f"{mirror_url.rstrip('XX/XX')}/{version}/terraform_{version}_SHA256SUMS"
    
    xǁIbmTfManagerǁget_checksum_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁget_checksum_url__mutmut_1': xǁIbmTfManagerǁget_checksum_url__mutmut_1, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_2': xǁIbmTfManagerǁget_checksum_url__mutmut_2, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_3': xǁIbmTfManagerǁget_checksum_url__mutmut_3, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_4': xǁIbmTfManagerǁget_checksum_url__mutmut_4, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_5': xǁIbmTfManagerǁget_checksum_url__mutmut_5, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_6': xǁIbmTfManagerǁget_checksum_url__mutmut_6, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_7': xǁIbmTfManagerǁget_checksum_url__mutmut_7, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_8': xǁIbmTfManagerǁget_checksum_url__mutmut_8, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_9': xǁIbmTfManagerǁget_checksum_url__mutmut_9, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_10': xǁIbmTfManagerǁget_checksum_url__mutmut_10, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_11': xǁIbmTfManagerǁget_checksum_url__mutmut_11, 
        'xǁIbmTfManagerǁget_checksum_url__mutmut_12': xǁIbmTfManagerǁget_checksum_url__mutmut_12
    }
    
    def get_checksum_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁget_checksum_url__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁget_checksum_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_checksum_url.__signature__ = _mutmut_signature(xǁIbmTfManagerǁget_checksum_url__mutmut_orig)
    xǁIbmTfManagerǁget_checksum_url__mutmut_orig.__name__ = 'xǁIbmTfManagerǁget_checksum_url'

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
            return False

        try:
            result = None

            if result.returncode == 0:
                # Check if version matches
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(None)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(None, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, None):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_31(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, ):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_32(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(None)
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_33(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return False
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_34(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(None)
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_35(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(None)

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_36(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return True

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_37(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(None)
            return False

    # _install_from_archive is inherited from TfVersionsManager

    def xǁIbmTfManagerǁverify_installation__mutmut_38(self, version: str) -> bool:
        """Verify that IBM Terraform installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"IBM Terraform binary not found at {binary_path}")
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
                version_pattern = rf"Terraform v{re.escape(version)}"
                if re.search(version_pattern, result.stdout):
                    logger.debug(f"IBM Terraform {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in IBM Terraform output: {result.stdout}")
            else:
                logger.error(f"IBM Terraform version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify IBM Terraform installation: {e}")
            return True
    
    xǁIbmTfManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁverify_installation__mutmut_1': xǁIbmTfManagerǁverify_installation__mutmut_1, 
        'xǁIbmTfManagerǁverify_installation__mutmut_2': xǁIbmTfManagerǁverify_installation__mutmut_2, 
        'xǁIbmTfManagerǁverify_installation__mutmut_3': xǁIbmTfManagerǁverify_installation__mutmut_3, 
        'xǁIbmTfManagerǁverify_installation__mutmut_4': xǁIbmTfManagerǁverify_installation__mutmut_4, 
        'xǁIbmTfManagerǁverify_installation__mutmut_5': xǁIbmTfManagerǁverify_installation__mutmut_5, 
        'xǁIbmTfManagerǁverify_installation__mutmut_6': xǁIbmTfManagerǁverify_installation__mutmut_6, 
        'xǁIbmTfManagerǁverify_installation__mutmut_7': xǁIbmTfManagerǁverify_installation__mutmut_7, 
        'xǁIbmTfManagerǁverify_installation__mutmut_8': xǁIbmTfManagerǁverify_installation__mutmut_8, 
        'xǁIbmTfManagerǁverify_installation__mutmut_9': xǁIbmTfManagerǁverify_installation__mutmut_9, 
        'xǁIbmTfManagerǁverify_installation__mutmut_10': xǁIbmTfManagerǁverify_installation__mutmut_10, 
        'xǁIbmTfManagerǁverify_installation__mutmut_11': xǁIbmTfManagerǁverify_installation__mutmut_11, 
        'xǁIbmTfManagerǁverify_installation__mutmut_12': xǁIbmTfManagerǁverify_installation__mutmut_12, 
        'xǁIbmTfManagerǁverify_installation__mutmut_13': xǁIbmTfManagerǁverify_installation__mutmut_13, 
        'xǁIbmTfManagerǁverify_installation__mutmut_14': xǁIbmTfManagerǁverify_installation__mutmut_14, 
        'xǁIbmTfManagerǁverify_installation__mutmut_15': xǁIbmTfManagerǁverify_installation__mutmut_15, 
        'xǁIbmTfManagerǁverify_installation__mutmut_16': xǁIbmTfManagerǁverify_installation__mutmut_16, 
        'xǁIbmTfManagerǁverify_installation__mutmut_17': xǁIbmTfManagerǁverify_installation__mutmut_17, 
        'xǁIbmTfManagerǁverify_installation__mutmut_18': xǁIbmTfManagerǁverify_installation__mutmut_18, 
        'xǁIbmTfManagerǁverify_installation__mutmut_19': xǁIbmTfManagerǁverify_installation__mutmut_19, 
        'xǁIbmTfManagerǁverify_installation__mutmut_20': xǁIbmTfManagerǁverify_installation__mutmut_20, 
        'xǁIbmTfManagerǁverify_installation__mutmut_21': xǁIbmTfManagerǁverify_installation__mutmut_21, 
        'xǁIbmTfManagerǁverify_installation__mutmut_22': xǁIbmTfManagerǁverify_installation__mutmut_22, 
        'xǁIbmTfManagerǁverify_installation__mutmut_23': xǁIbmTfManagerǁverify_installation__mutmut_23, 
        'xǁIbmTfManagerǁverify_installation__mutmut_24': xǁIbmTfManagerǁverify_installation__mutmut_24, 
        'xǁIbmTfManagerǁverify_installation__mutmut_25': xǁIbmTfManagerǁverify_installation__mutmut_25, 
        'xǁIbmTfManagerǁverify_installation__mutmut_26': xǁIbmTfManagerǁverify_installation__mutmut_26, 
        'xǁIbmTfManagerǁverify_installation__mutmut_27': xǁIbmTfManagerǁverify_installation__mutmut_27, 
        'xǁIbmTfManagerǁverify_installation__mutmut_28': xǁIbmTfManagerǁverify_installation__mutmut_28, 
        'xǁIbmTfManagerǁverify_installation__mutmut_29': xǁIbmTfManagerǁverify_installation__mutmut_29, 
        'xǁIbmTfManagerǁverify_installation__mutmut_30': xǁIbmTfManagerǁverify_installation__mutmut_30, 
        'xǁIbmTfManagerǁverify_installation__mutmut_31': xǁIbmTfManagerǁverify_installation__mutmut_31, 
        'xǁIbmTfManagerǁverify_installation__mutmut_32': xǁIbmTfManagerǁverify_installation__mutmut_32, 
        'xǁIbmTfManagerǁverify_installation__mutmut_33': xǁIbmTfManagerǁverify_installation__mutmut_33, 
        'xǁIbmTfManagerǁverify_installation__mutmut_34': xǁIbmTfManagerǁverify_installation__mutmut_34, 
        'xǁIbmTfManagerǁverify_installation__mutmut_35': xǁIbmTfManagerǁverify_installation__mutmut_35, 
        'xǁIbmTfManagerǁverify_installation__mutmut_36': xǁIbmTfManagerǁverify_installation__mutmut_36, 
        'xǁIbmTfManagerǁverify_installation__mutmut_37': xǁIbmTfManagerǁverify_installation__mutmut_37, 
        'xǁIbmTfManagerǁverify_installation__mutmut_38': xǁIbmTfManagerǁverify_installation__mutmut_38
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁIbmTfManagerǁverify_installation__mutmut_orig)
    xǁIbmTfManagerǁverify_installation__mutmut_orig.__name__ = 'xǁIbmTfManagerǁverify_installation'

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_orig(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_1(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_2(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_3(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_4(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_5(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_6(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_7(self) -> dict:
        """Get compatibility information for development tools."""
        version = self.get_installed_version()
        if not version:
            return {"status": "not_installed"}

        # Check compatibility with development tools
        compatibility = None

        return compatibility

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_8(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_9(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_10(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_11(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_12(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_13(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_14(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_15(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_16(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_17(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_18(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_19(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_20(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_21(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_22(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_23(self) -> dict:
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

    def xǁIbmTfManagerǁget_harness_compatibility__mutmut_24(self) -> dict:
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
    
    xǁIbmTfManagerǁget_harness_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁget_harness_compatibility__mutmut_1': xǁIbmTfManagerǁget_harness_compatibility__mutmut_1, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_2': xǁIbmTfManagerǁget_harness_compatibility__mutmut_2, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_3': xǁIbmTfManagerǁget_harness_compatibility__mutmut_3, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_4': xǁIbmTfManagerǁget_harness_compatibility__mutmut_4, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_5': xǁIbmTfManagerǁget_harness_compatibility__mutmut_5, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_6': xǁIbmTfManagerǁget_harness_compatibility__mutmut_6, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_7': xǁIbmTfManagerǁget_harness_compatibility__mutmut_7, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_8': xǁIbmTfManagerǁget_harness_compatibility__mutmut_8, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_9': xǁIbmTfManagerǁget_harness_compatibility__mutmut_9, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_10': xǁIbmTfManagerǁget_harness_compatibility__mutmut_10, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_11': xǁIbmTfManagerǁget_harness_compatibility__mutmut_11, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_12': xǁIbmTfManagerǁget_harness_compatibility__mutmut_12, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_13': xǁIbmTfManagerǁget_harness_compatibility__mutmut_13, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_14': xǁIbmTfManagerǁget_harness_compatibility__mutmut_14, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_15': xǁIbmTfManagerǁget_harness_compatibility__mutmut_15, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_16': xǁIbmTfManagerǁget_harness_compatibility__mutmut_16, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_17': xǁIbmTfManagerǁget_harness_compatibility__mutmut_17, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_18': xǁIbmTfManagerǁget_harness_compatibility__mutmut_18, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_19': xǁIbmTfManagerǁget_harness_compatibility__mutmut_19, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_20': xǁIbmTfManagerǁget_harness_compatibility__mutmut_20, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_21': xǁIbmTfManagerǁget_harness_compatibility__mutmut_21, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_22': xǁIbmTfManagerǁget_harness_compatibility__mutmut_22, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_23': xǁIbmTfManagerǁget_harness_compatibility__mutmut_23, 
        'xǁIbmTfManagerǁget_harness_compatibility__mutmut_24': xǁIbmTfManagerǁget_harness_compatibility__mutmut_24
    }
    
    def get_harness_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁget_harness_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁget_harness_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_harness_compatibility.__signature__ = _mutmut_signature(xǁIbmTfManagerǁget_harness_compatibility__mutmut_orig)
    xǁIbmTfManagerǁget_harness_compatibility__mutmut_orig.__name__ = 'xǁIbmTfManagerǁget_harness_compatibility'

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": True,
            "notes": "CTY testing compatible with all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "XXcompatibleXX": True,
            "notes": "CTY testing compatible with all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "COMPATIBLE": True,
            "notes": "CTY testing compatible with all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": False,
            "notes": "CTY testing compatible with all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": True,
            "XXnotesXX": "CTY testing compatible with all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": True,
            "NOTES": "CTY testing compatible with all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": True,
            "notes": "XXCTY testing compatible with all IBM Terraform versionsXX",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": True,
            "notes": "cty testing compatible with all ibm terraform versions",
        }

    def xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with CTY tools."""
        # CTY tools work with most Terraform versions
        return {
            "compatible": True,
            "notes": "CTY TESTING COMPATIBLE WITH ALL IBM TERRAFORM VERSIONS",
        }
    
    xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_1': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_1, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_2': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_2, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_3': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_3, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_4': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_4, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_5': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_5, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_6': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_6, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_7': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_7, 
        'xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_8': xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_8
    }
    
    def _check_cty_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_cty_compatibility.__signature__ = _mutmut_signature(xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_orig)
    xǁIbmTfManagerǁ_check_cty_compatibility__mutmut_orig.__name__ = 'xǁIbmTfManagerǁ_check_cty_compatibility'

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = None

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(None)

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = "XX.XX".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(None)[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split("XX.XX")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:3])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = None
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["XX1.5XX", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_9(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "XX1.6XX", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_10(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "XX1.7XX"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_11(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = None

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_12(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor not in compatible_versions

        return {
            "compatible": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_13(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "XXcompatibleXX": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_14(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "COMPATIBLE": is_compatible,
            "notes": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_15(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "XXnotesXX": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }

    def xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_16(self, version: str) -> dict:
        """Check compatibility with wire protocol tools."""
        # Wire protocol compatibility depends on Terraform version
        major_minor = ".".join(version.split(".")[:2])

        compatible_versions = ["1.5", "1.6", "1.7"]
        is_compatible = major_minor in compatible_versions

        return {
            "compatible": is_compatible,
            "NOTES": f"Wire protocol testing requires IBM Terraform 1.5+ (current: {version})",
        }
    
    xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_1': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_1, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_2': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_2, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_3': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_3, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_4': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_4, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_5': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_5, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_6': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_6, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_7': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_7, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_8': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_8, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_9': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_9, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_10': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_10, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_11': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_11, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_12': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_12, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_13': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_13, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_14': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_14, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_15': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_15, 
        'xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_16': xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_16
    }
    
    def _check_wire_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_wire_compatibility.__signature__ = _mutmut_signature(xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_orig)
    xǁIbmTfManagerǁ_check_wire_compatibility__mutmut_orig.__name__ = 'xǁIbmTfManagerǁ_check_wire_compatibility'

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_orig(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "Conformance testing supports all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_1(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "XXcompatibleXX": True,
            "notes": "Conformance testing supports all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_2(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "COMPATIBLE": True,
            "notes": "Conformance testing supports all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_3(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": False,
            "notes": "Conformance testing supports all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_4(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "XXnotesXX": "Conformance testing supports all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_5(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "NOTES": "Conformance testing supports all IBM Terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_6(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "XXConformance testing supports all IBM Terraform versionsXX",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_7(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "conformance testing supports all ibm terraform versions",
        }

    def xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_8(self, version: str) -> dict:
        """Check compatibility with conformance testing."""
        return {
            "compatible": True,
            "notes": "CONFORMANCE TESTING SUPPORTS ALL IBM TERRAFORM VERSIONS",
        }
    
    xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_1': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_1, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_2': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_2, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_3': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_3, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_4': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_4, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_5': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_5, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_6': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_6, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_7': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_7, 
        'xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_8': xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_8
    }
    
    def _check_conformance_compatibility(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_orig"), object.__getattribute__(self, "xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_conformance_compatibility.__signature__ = _mutmut_signature(xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_orig)
    xǁIbmTfManagerǁ_check_conformance_compatibility__mutmut_orig.__name__ = 'xǁIbmTfManagerǁ_check_conformance_compatibility'


# 🍲🥄📄🪄
