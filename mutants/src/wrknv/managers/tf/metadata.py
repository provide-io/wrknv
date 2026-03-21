#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tf Metadata Management
======================
Metadata and RECENT file management for Terraform/OpenTofu managers."""

from __future__ import annotations

import json
import pathlib

from provide.foundation import logger
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


class TfMetadataManager:
    """Manages metadata and RECENT files for tf tools."""

    def xǁTfMetadataManagerǁ__init____mutmut_orig(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = tool_name
        self.metadata_file = install_path / "metadata.json"
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_1(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = None
        self.tool_name = tool_name
        self.metadata_file = install_path / "metadata.json"
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_2(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = None
        self.metadata_file = install_path / "metadata.json"
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_3(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = tool_name
        self.metadata_file = None
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_4(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = tool_name
        self.metadata_file = install_path * "metadata.json"
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_5(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = tool_name
        self.metadata_file = install_path / "XXmetadata.jsonXX"
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_6(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = tool_name
        self.metadata_file = install_path / "METADATA.JSON"
        self.metadata: dict = {}

    def xǁTfMetadataManagerǁ__init____mutmut_7(self, install_path: pathlib.Path, tool_name: str) -> None:
        self.install_path = install_path
        self.tool_name = tool_name
        self.metadata_file = install_path / "metadata.json"
        self.metadata: dict = None
    
    xǁTfMetadataManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfMetadataManagerǁ__init____mutmut_1': xǁTfMetadataManagerǁ__init____mutmut_1, 
        'xǁTfMetadataManagerǁ__init____mutmut_2': xǁTfMetadataManagerǁ__init____mutmut_2, 
        'xǁTfMetadataManagerǁ__init____mutmut_3': xǁTfMetadataManagerǁ__init____mutmut_3, 
        'xǁTfMetadataManagerǁ__init____mutmut_4': xǁTfMetadataManagerǁ__init____mutmut_4, 
        'xǁTfMetadataManagerǁ__init____mutmut_5': xǁTfMetadataManagerǁ__init____mutmut_5, 
        'xǁTfMetadataManagerǁ__init____mutmut_6': xǁTfMetadataManagerǁ__init____mutmut_6, 
        'xǁTfMetadataManagerǁ__init____mutmut_7': xǁTfMetadataManagerǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfMetadataManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTfMetadataManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTfMetadataManagerǁ__init____mutmut_orig)
    xǁTfMetadataManagerǁ__init____mutmut_orig.__name__ = 'xǁTfMetadataManagerǁ__init__'

    def xǁTfMetadataManagerǁload_metadata__mutmut_orig(self) -> None:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    self.metadata = json.load(f)
                # Migrate old format if needed
                self._migrate_metadata_format()
            except Exception as e:
                logger.warning(f"Failed to load metadata: {e}")
                self.metadata = {}
        else:
            self.metadata = {}

    def xǁTfMetadataManagerǁload_metadata__mutmut_1(self) -> None:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    self.metadata = None
                # Migrate old format if needed
                self._migrate_metadata_format()
            except Exception as e:
                logger.warning(f"Failed to load metadata: {e}")
                self.metadata = {}
        else:
            self.metadata = {}

    def xǁTfMetadataManagerǁload_metadata__mutmut_2(self) -> None:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    self.metadata = json.load(None)
                # Migrate old format if needed
                self._migrate_metadata_format()
            except Exception as e:
                logger.warning(f"Failed to load metadata: {e}")
                self.metadata = {}
        else:
            self.metadata = {}

    def xǁTfMetadataManagerǁload_metadata__mutmut_3(self) -> None:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    self.metadata = json.load(f)
                # Migrate old format if needed
                self._migrate_metadata_format()
            except Exception as e:
                logger.warning(None)
                self.metadata = {}
        else:
            self.metadata = {}

    def xǁTfMetadataManagerǁload_metadata__mutmut_4(self) -> None:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    self.metadata = json.load(f)
                # Migrate old format if needed
                self._migrate_metadata_format()
            except Exception as e:
                logger.warning(f"Failed to load metadata: {e}")
                self.metadata = None
        else:
            self.metadata = {}

    def xǁTfMetadataManagerǁload_metadata__mutmut_5(self) -> None:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    self.metadata = json.load(f)
                # Migrate old format if needed
                self._migrate_metadata_format()
            except Exception as e:
                logger.warning(f"Failed to load metadata: {e}")
                self.metadata = {}
        else:
            self.metadata = None
    
    xǁTfMetadataManagerǁload_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfMetadataManagerǁload_metadata__mutmut_1': xǁTfMetadataManagerǁload_metadata__mutmut_1, 
        'xǁTfMetadataManagerǁload_metadata__mutmut_2': xǁTfMetadataManagerǁload_metadata__mutmut_2, 
        'xǁTfMetadataManagerǁload_metadata__mutmut_3': xǁTfMetadataManagerǁload_metadata__mutmut_3, 
        'xǁTfMetadataManagerǁload_metadata__mutmut_4': xǁTfMetadataManagerǁload_metadata__mutmut_4, 
        'xǁTfMetadataManagerǁload_metadata__mutmut_5': xǁTfMetadataManagerǁload_metadata__mutmut_5
    }
    
    def load_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfMetadataManagerǁload_metadata__mutmut_orig"), object.__getattribute__(self, "xǁTfMetadataManagerǁload_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_metadata.__signature__ = _mutmut_signature(xǁTfMetadataManagerǁload_metadata__mutmut_orig)
    xǁTfMetadataManagerǁload_metadata__mutmut_orig.__name__ = 'xǁTfMetadataManagerǁload_metadata'

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_orig(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_1(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = None

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_2(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = True

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_3(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["XXactive_tofuXX", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_4(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["ACTIVE_TOFU", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_5(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "XXactive_terraformXX"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_6(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "ACTIVE_TERRAFORM"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_7(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key not in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_8(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = None
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_9(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace(None, "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_10(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", None)
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_11(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_12(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", )
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_13(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("XXactive_XX", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_14(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("ACTIVE_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_15(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "XXXX")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_16(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = None

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_17(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(None)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_18(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "XXworkenvXX" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_19(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "WORKENV" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_20(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_21(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = None
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_22(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["XXworkenvXX"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_23(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["WORKENV"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_24(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "XXdefaultXX" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_25(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "DEFAULT" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_26(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_27(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["XXworkenvXX"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_28(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["WORKENV"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_29(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = None

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_30(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["XXworkenvXX"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_31(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["WORKENV"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_32(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["XXdefaultXX"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_33(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["DEFAULT"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_34(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = None

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_35(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "XXopentofu_versionXX" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_36(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "OPENTOFU_VERSION" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_37(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool != "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_38(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "XXtofuXX" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_39(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "TOFU" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_40(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = None
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_41(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["XXworkenvXX"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_42(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["WORKENV"]["default"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_43(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["XXdefaultXX"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_44(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["DEFAULT"][version_key] = version
                needs_save = True

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_45(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = None

        if needs_save:
            self.save_metadata()

    def xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_46(self) -> None:
        """Migrate old metadata format to new workenv structure."""
        needs_save = False

        # Migrate old active_* keys to workenv structure
        for old_key in ["active_tofu", "active_terraform"]:
            if old_key in self.metadata:
                tool = old_key.replace("active_", "")
                version = self.metadata.pop(old_key)

                # Ensure workenv structure exists
                if "workenv" not in self.metadata:
                    self.metadata["workenv"] = {}
                if "default" not in self.metadata["workenv"]:
                    self.metadata["workenv"]["default"] = {}

                # Set version in new structure
                # Use 'opentofu_version' for tofu
                version_key = "opentofu_version" if tool == "tofu" else f"{tool}_version"

                self.metadata["workenv"]["default"][version_key] = version
                needs_save = False

        if needs_save:
            self.save_metadata()
    
    xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_1': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_1, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_2': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_2, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_3': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_3, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_4': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_4, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_5': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_5, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_6': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_6, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_7': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_7, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_8': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_8, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_9': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_9, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_10': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_10, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_11': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_11, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_12': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_12, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_13': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_13, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_14': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_14, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_15': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_15, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_16': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_16, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_17': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_17, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_18': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_18, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_19': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_19, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_20': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_20, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_21': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_21, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_22': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_22, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_23': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_23, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_24': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_24, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_25': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_25, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_26': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_26, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_27': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_27, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_28': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_28, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_29': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_29, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_30': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_30, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_31': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_31, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_32': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_32, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_33': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_33, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_34': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_34, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_35': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_35, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_36': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_36, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_37': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_37, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_38': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_38, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_39': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_39, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_40': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_40, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_41': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_41, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_42': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_42, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_43': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_43, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_44': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_44, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_45': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_45, 
        'xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_46': xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_46
    }
    
    def _migrate_metadata_format(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_orig"), object.__getattribute__(self, "xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _migrate_metadata_format.__signature__ = _mutmut_signature(xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_orig)
    xǁTfMetadataManagerǁ_migrate_metadata_format__mutmut_orig.__name__ = 'xǁTfMetadataManagerǁ_migrate_metadata_format'

    def xǁTfMetadataManagerǁsave_metadata__mutmut_orig(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_1(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open(None) as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_2(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("XXwXX") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_3(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("W") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_4(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(None, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_5(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, None, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_6(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=None, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_7(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=None, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_8(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=None)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_9(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_10(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_11(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_12(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_13(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, )
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_14(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=3, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_15(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=False, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfMetadataManagerǁsave_metadata__mutmut_16(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(None)
    
    xǁTfMetadataManagerǁsave_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfMetadataManagerǁsave_metadata__mutmut_1': xǁTfMetadataManagerǁsave_metadata__mutmut_1, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_2': xǁTfMetadataManagerǁsave_metadata__mutmut_2, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_3': xǁTfMetadataManagerǁsave_metadata__mutmut_3, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_4': xǁTfMetadataManagerǁsave_metadata__mutmut_4, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_5': xǁTfMetadataManagerǁsave_metadata__mutmut_5, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_6': xǁTfMetadataManagerǁsave_metadata__mutmut_6, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_7': xǁTfMetadataManagerǁsave_metadata__mutmut_7, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_8': xǁTfMetadataManagerǁsave_metadata__mutmut_8, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_9': xǁTfMetadataManagerǁsave_metadata__mutmut_9, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_10': xǁTfMetadataManagerǁsave_metadata__mutmut_10, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_11': xǁTfMetadataManagerǁsave_metadata__mutmut_11, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_12': xǁTfMetadataManagerǁsave_metadata__mutmut_12, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_13': xǁTfMetadataManagerǁsave_metadata__mutmut_13, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_14': xǁTfMetadataManagerǁsave_metadata__mutmut_14, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_15': xǁTfMetadataManagerǁsave_metadata__mutmut_15, 
        'xǁTfMetadataManagerǁsave_metadata__mutmut_16': xǁTfMetadataManagerǁsave_metadata__mutmut_16
    }
    
    def save_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfMetadataManagerǁsave_metadata__mutmut_orig"), object.__getattribute__(self, "xǁTfMetadataManagerǁsave_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    save_metadata.__signature__ = _mutmut_signature(xǁTfMetadataManagerǁsave_metadata__mutmut_orig)
    xǁTfMetadataManagerǁsave_metadata__mutmut_orig.__name__ = 'xǁTfMetadataManagerǁsave_metadata'

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_orig(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_1(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = None
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_2(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path * "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_3(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "XXRECENTXX"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_4(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "recent"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_5(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = None

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_6(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = None
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_7(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(None)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_8(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = None

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_9(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = None

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_10(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name == "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_11(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "XXtofuXX" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_12(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "TOFU" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_13(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "XXopentofuXX"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_14(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "OPENTOFU"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_15(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = None
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_16(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:6]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_17(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key not in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_18(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open(None) as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_19(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("XXwXX") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_20(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("W") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_21(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(None, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_22(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, None)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_23(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_24(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, )
        except Exception as e:
            logger.warning(f"Failed to update RECENT file: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file__mutmut_25(self, installed_versions: list[str]) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key for RECENT file
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        if installed_versions:
            # Keep only the 5 most recent versions
            recent_data[tool_key] = installed_versions[:5]
        elif tool_key in recent_data:
            # Remove tool if no versions installed
            del recent_data[tool_key]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(None)
    
    xǁTfMetadataManagerǁupdate_recent_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfMetadataManagerǁupdate_recent_file__mutmut_1': xǁTfMetadataManagerǁupdate_recent_file__mutmut_1, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_2': xǁTfMetadataManagerǁupdate_recent_file__mutmut_2, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_3': xǁTfMetadataManagerǁupdate_recent_file__mutmut_3, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_4': xǁTfMetadataManagerǁupdate_recent_file__mutmut_4, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_5': xǁTfMetadataManagerǁupdate_recent_file__mutmut_5, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_6': xǁTfMetadataManagerǁupdate_recent_file__mutmut_6, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_7': xǁTfMetadataManagerǁupdate_recent_file__mutmut_7, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_8': xǁTfMetadataManagerǁupdate_recent_file__mutmut_8, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_9': xǁTfMetadataManagerǁupdate_recent_file__mutmut_9, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_10': xǁTfMetadataManagerǁupdate_recent_file__mutmut_10, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_11': xǁTfMetadataManagerǁupdate_recent_file__mutmut_11, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_12': xǁTfMetadataManagerǁupdate_recent_file__mutmut_12, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_13': xǁTfMetadataManagerǁupdate_recent_file__mutmut_13, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_14': xǁTfMetadataManagerǁupdate_recent_file__mutmut_14, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_15': xǁTfMetadataManagerǁupdate_recent_file__mutmut_15, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_16': xǁTfMetadataManagerǁupdate_recent_file__mutmut_16, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_17': xǁTfMetadataManagerǁupdate_recent_file__mutmut_17, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_18': xǁTfMetadataManagerǁupdate_recent_file__mutmut_18, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_19': xǁTfMetadataManagerǁupdate_recent_file__mutmut_19, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_20': xǁTfMetadataManagerǁupdate_recent_file__mutmut_20, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_21': xǁTfMetadataManagerǁupdate_recent_file__mutmut_21, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_22': xǁTfMetadataManagerǁupdate_recent_file__mutmut_22, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_23': xǁTfMetadataManagerǁupdate_recent_file__mutmut_23, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_24': xǁTfMetadataManagerǁupdate_recent_file__mutmut_24, 
        'xǁTfMetadataManagerǁupdate_recent_file__mutmut_25': xǁTfMetadataManagerǁupdate_recent_file__mutmut_25
    }
    
    def update_recent_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfMetadataManagerǁupdate_recent_file__mutmut_orig"), object.__getattribute__(self, "xǁTfMetadataManagerǁupdate_recent_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_recent_file.__signature__ = _mutmut_signature(xǁTfMetadataManagerǁupdate_recent_file__mutmut_orig)
    xǁTfMetadataManagerǁupdate_recent_file__mutmut_orig.__name__ = 'xǁTfMetadataManagerǁupdate_recent_file'

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_orig(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_1(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = None
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_2(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path * "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_3(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "XXRECENTXX"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_4(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "recent"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_5(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = None

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_6(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = None
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_7(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(None)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_8(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = None

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_9(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = None

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_10(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name == "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_11(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "XXtofuXX" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_12(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "TOFU" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_13(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "XXopentofuXX"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_14(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "OPENTOFU"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_15(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = None
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_16(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version or len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_17(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v == version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_18(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) <= 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_19(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 6:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_20(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(None)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_21(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = None

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_22(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open(None) as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_23(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("XXwXX") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_24(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("W") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_25(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(None, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_26(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, None)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_27(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_28(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, )
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_29(self, version: str, installed_versions: list[str]) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Put active version first, then other recent versions
        versions_list = [version]
        for v in installed_versions:
            if v != version and len(versions_list) < 5:
                versions_list.append(v)

        recent_data[tool_key] = versions_list

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(None)
    
    xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_1': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_1, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_2': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_2, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_3': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_3, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_4': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_4, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_5': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_5, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_6': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_6, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_7': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_7, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_8': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_8, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_9': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_9, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_10': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_10, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_11': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_11, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_12': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_12, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_13': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_13, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_14': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_14, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_15': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_15, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_16': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_16, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_17': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_17, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_18': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_18, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_19': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_19, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_20': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_20, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_21': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_21, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_22': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_22, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_23': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_23, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_24': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_24, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_25': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_25, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_26': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_26, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_27': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_27, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_28': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_28, 
        'xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_29': xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_29
    }
    
    def update_recent_file_with_active(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_orig"), object.__getattribute__(self, "xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_recent_file_with_active.__signature__ = _mutmut_signature(xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_orig)
    xǁTfMetadataManagerǁupdate_recent_file_with_active__mutmut_orig.__name__ = 'xǁTfMetadataManagerǁupdate_recent_file_with_active'


# 🧰🌍🔚
